#!/usr/bin/env python3
"""
pdf_extract.py — vision-LLM PDF -> text/markdown extractor for equity research.

Uses the OpenCode Go gateway with the GLM-5.3-Flash vision model. Pages are
rendered to images IN MEMORY (never written to disk), grouped into batches, and
sent to the model in parallel. The model returns a JSON object holding one
transcription string per page image, in order; this script attaches the
"===== PAGE <n> =====" markers itself using the PDF page indices, so the model
never has to reason about page numbers at all.

Examples
--------
    pdf_extract.py --pdf deck.pdf --out deck.md
    pdf_extract.py --pdf AR2026.pdf --out AR2026.md --start 1 --end 344
    pdf_extract.py --pdf transcript.pdf --out t.md --batch-size 10 --parallel 3
    pdf_extract.py --pdf deck.pdf --out deck.md --dry-run

API key resolution order:
    1. --api-key
    2. $OPENCODE_GO_API_KEY
    3. opencode auth store  (~/.local/share/opencode/auth.json -> opencode-go.key)
"""
from __future__ import annotations

import argparse
import base64
import concurrent.futures as cf
import json
import os
import sys
import threading
import time

# ----------------------------------------------------------------------------
# constants
# ----------------------------------------------------------------------------
BASE_URL = "https://opencode.ai/zen/go/v1"
DEFAULT_MODEL = "glm-5.3-flash"
DEFAULT_BATCH_SIZE = 20
MAX_PARALLEL = 5
DEFAULT_DPI = 150
DEFAULT_MAX_TOKENS = 16000
DEFAULT_MAX_PAYLOAD_MB = 2.5
PRICING = {"glm-5.3-flash": (0.15, 0.50), "qwen3.8-flash": (0.15, 0.47)}

EXTRACTION_PROMPT = """\
You are a meticulous document-transcription engine used by equity analysts.

You are given N consecutive pages (as images) of ONE document, in order. \
Transcribe every page faithfully and completely.

RULES
1. VERBATIM. Never summarise, paraphrase, condense, interpret, or add commentary.
2. Reproduce all text, numbers, symbols, currency units, percentages and dates \
EXACTLY as shown (e.g. "Rs. 1,434 Crores", "36.7%", "(1,119)").
3. TABLES: transcribe every row and column. Render as a GitHub-markdown table \
when the grid is regular; if the layout is irregular or multi-block, transcribe \
each row as "label: value1 | value2 | ..." lines. Never omit a figure.
4. CHARTS / GRAPHS / DIAGRAMS / INFOGRAPHICS / PROCESS FLOWS: state the title, \
axis labels and units, legend / series names, then LIST EVERY printed data-label \
value, and finish with one short sentence describing the trend or structure. \
Never invent values that are not printed.
5. Preserve headings, bullet hierarchy and reading order.
6. TRANSCRIPTS / Q&A: keep speaker names and the full text of every question and \
answer, including the management guidance and any numbers stated verbally.
7. SKIP ONLY content with no value to an investor: full-page legal \
disclaimers / "Safe Harbor" pages, blank pages, back covers, and pure \
transmittal/covering letters whose only content is a regulatory submission note. \
If a page mixes boilerplate with ANY substantive information, transcribe the \
substantive part.
8. Do NOT print page numbers or any "PAGE n" / "===== PAGE n =====" headings.

OUTPUT FORMAT
Return ONLY a JSON object of exactly this shape:
{"pages": ["<transcription of image 1>", "<transcription of image 2>", ...]}
- The "pages" array MUST contain exactly one string per image, in the same order \
as the images supplied.
- Each string is the COMPLETE transcription of a single page. Never merge two \
pages into one string and never skip a page.
- For a page with no extractable content use the empty string "".
- Emit no commentary, no markdown code fences, and nothing outside the JSON object.
"""


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------
def log(msg: str) -> None:
    print(msg, flush=True)


def resolve_api_key(args) -> str:
    if args.api_key:
        return args.api_key.strip()
    env = os.environ.get("OPENCODE_GO_API_KEY")
    if env:
        return env.strip()
    auth = os.path.expanduser("~/.local/share/opencode/auth.json")
    if os.path.exists(auth):
        try:
            key = (json.load(open(auth)).get("opencode-go") or {}).get("key")
            if key:
                return key.strip()
        except Exception:
            pass
    sys.exit("ERROR: no API key. Pass --api-key, set OPENCODE_GO_API_KEY, "
             "or log in to OpenCode Go.")


def page_count(pdf: str) -> int:
    import pymupdf
    with pymupdf.open(pdf) as doc:
        return doc.page_count


def render_pages(pdf: str, pages, dpi: int):
    """Return {page_no: base64_png}. Images live only in memory."""
    import pymupdf
    out = {}
    with pymupdf.open(pdf) as doc:
        for p in pages:
            png = doc[p - 1].get_pixmap(dpi=dpi).tobytes("png")
            out[p] = base64.b64encode(png).decode()
    return out


def split_by_payload(pages, imgs, budget_chars):
    """Greedily split pages into groups whose base64 sizes fit the budget."""
    groups, cur, cur_sz = [], [], 0
    for p in pages:
        sz = len(imgs[p])
        if cur and cur_sz + sz > budget_chars:
            groups.append(cur)
            cur, cur_sz = [], 0
        cur.append(p)
        cur_sz += sz
    if cur:
        groups.append(cur)
    return groups


def is_payload_error(exc: Exception) -> bool:
    s = str(exc).lower()
    return any(t in s for t in ("tcp payload", "payload budget", "exceeds", "too large",
                                "request entity", "413", "too many images", "context length"))


def is_response_format_error(exc: Exception) -> bool:
    s = str(exc).lower()
    return any(t in s for t in ("response_format", "json_object", "json mode",
                                "unsupported parameter", "invalid parameter", "unknown parameter"))


def chunks(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


def _account(stats, usage) -> None:
    stats["input_tokens"] += getattr(usage, "prompt_tokens", 0) or 0
    stats["output_tokens"] += getattr(usage, "completion_tokens", 0) or 0


# ----------------------------------------------------------------------------
# JSON parsing of per-page output
# ----------------------------------------------------------------------------
def _coerce_pages(obj):
    if isinstance(obj, list):
        return obj
    if isinstance(obj, dict):
        for key in ("pages", "page", "items", "result", "data"):
            val = obj.get(key)
            if isinstance(val, list):
                return val
        for val in obj.values():
            if isinstance(val, list):
                return val
    return None


def parse_pages_json(raw, n):
    """Return (list_of_strings or None, problem or None)."""
    if raw is None or not raw.strip():
        return None, "empty response"
    s = raw.strip()
    if s.startswith("```"):
        nl = s.find("\n")
        s = s[nl + 1:] if nl != -1 else ""
        if s.rstrip().endswith("```"):
            s = s.rstrip()[:-3].rstrip()

    candidates = [s]
    for open_c, close_c in (("{", "}"), ("[", "]")):
        i, j = s.find(open_c), s.rfind(close_c)
        if 0 <= i < j:
            candidates.append(s[i:j + 1])

    for cand in candidates:
        try:
            obj = json.loads(cand, strict=False)
        except Exception:
            continue
        lst = _coerce_pages(obj)
        if lst is None:
            continue
        lst = [x if isinstance(x, str) else ("" if x is None else str(x)) for x in lst]
        if len(lst) == n:
            return lst, None
        return lst, f"expected {n} items, got {len(lst)}"
    return None, "response was not valid JSON"


# ----------------------------------------------------------------------------
# model calls
# ----------------------------------------------------------------------------
def _call_model(client, model, pages, images, max_tokens, retries=4,
                prior_raw=None, correction=None):
    content = [{"type": "text",
                "text": EXTRACTION_PROMPT + f"\nThere are {len(pages)} page images below, in order."}]
    for im in images:
        content.append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{im}"}})
    messages = [{"role": "user", "content": content}]
    if prior_raw is not None and correction is not None:
        messages.append({"role": "assistant", "content": prior_raw})
        messages.append({"role": "user", "content": correction})

    use_json = True
    last = None
    for attempt in range(retries):
        try:
            kwargs = {"model": model, "messages": messages, "max_tokens": max_tokens}
            if use_json:
                kwargs["response_format"] = {"type": "json_object"}
            r = client.chat.completions.create(**kwargs)
            choice = r.choices[0]
            return (choice.message.content or ""), r.usage, choice.finish_reason
        except Exception as e:                      # noqa: BLE001
            last = e
            if use_json and is_response_format_error(e):
                log("    response_format unsupported by gateway; retrying without it")
                use_json = False
                continue
            if is_payload_error(e):
                raise
            wait = 3 * (2 ** attempt)
            log(f"    retry {attempt + 1}/{retries} pages {pages[0]}-{pages[-1]} "
                f"({type(e).__name__}: {str(e)[:100]}) sleeping {wait}s")
            time.sleep(wait)
    raise last


def _extract_subgroup(client, model, imgs, pages, max_tokens, stats, depth=0):
    """One request for a contiguous page list; validate, repair, then halve."""
    images = [imgs[p] for p in pages]
    seg = f"{pages[0]}-{pages[-1]}"

    raw, usage, finish = _call_model(client, model, pages, images, max_tokens)
    _account(stats, usage)
    parsed, problem = parse_pages_json(raw, len(pages))
    if parsed is not None and problem is None and finish != "length":
        return dict(zip(pages, parsed))

    if finish != "length":
        stats["repairs"] += 1
        correction = (f"Your previous response was invalid: {problem}. Return ONLY the JSON "
                      f"object {{\"pages\": [...]}} containing exactly {len(pages)} strings, one "
                      f"per page image, in the same order, with no other text.")
        log(f"    repair {seg}: {problem}")
        raw2, usage2, finish2 = _call_model(client, model, pages, images, max_tokens,
                                            prior_raw=raw, correction=correction)
        _account(stats, usage2)
        parsed2, problem2 = parse_pages_json(raw2, len(pages))
        if parsed2 is not None and problem2 is None and finish2 != "length":
            return dict(zip(pages, parsed2))
        problem = problem2 or f"finish={finish2}"

    if len(pages) > 1:
        stats["splits"] += 1
        mid = len(pages) // 2
        log(f"    split {seg} -> {len(pages[:mid])}+{len(pages[mid:])} ({problem})")
        left = _extract_subgroup(client, model, imgs, pages[:mid], max_tokens, stats, depth + 1)
        right = _extract_subgroup(client, model, imgs, pages[mid:], max_tokens, stats, depth + 1)
        return {**left, **right}

    stats["failed_pages"].append(pages[0])
    log(f"    page {pages[0]}: FAILED ({problem})")
    return {pages[0]: ""}


def _extract_group(client, model, pdf, pages, dpi, max_tokens, budget_chars, stats, depth=0):
    """Extract one scheduled batch; returns {page_no: text}."""
    seg = f"{pages[0]}-{pages[-1]}"
    try:
        imgs = render_pages(pdf, pages, dpi)
    except Exception as e:                          # noqa: BLE001
        log(f"    render {seg}: FAILED ({type(e).__name__}: {str(e)[:120]})")
        stats["failed_pages"].extend(pages)
        return {p: "" for p in pages}

    try:
        groups = split_by_payload(pages, imgs, budget_chars)
        if len(groups) > 1:
            stats["payload_splits"] += 1
        page_texts = {}
        for g in groups:
            page_texts.update(_extract_subgroup(client, model, imgs, g, max_tokens, stats, depth))
        return page_texts
    except Exception as e:                          # noqa: BLE001
        if is_payload_error(e) and len(pages) > 1:
            stats["payload_splits"] += 1
            mid = len(pages) // 2
            log(f"    split {seg} -> {len(pages[:mid])}+{len(pages[mid:])} "
                f"({type(e).__name__}: {str(e)[:70]})")
            left = _extract_group(client, model, pdf, pages[:mid], dpi, max_tokens, budget_chars,
                                  stats, depth + 1)
            right = _extract_group(client, model, pdf, pages[mid:], dpi, max_tokens, budget_chars,
                                   stats, depth + 1)
            return {**left, **right}
        log(f"    batch {seg}: FAILED ({type(e).__name__}: {str(e)[:120]})")
        stats["failed_pages"].extend(pages)
        return {p: "" for p in pages}


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------
def main() -> None:
    ap = argparse.ArgumentParser(description="Vision-LLM PDF -> text/markdown extractor.")
    ap.add_argument("--pdf", required=True, help="input PDF path")
    ap.add_argument("--out", required=True, help="output markdown path")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE,
                    help=f"pages per scheduling unit (default {DEFAULT_BATCH_SIZE})")
    ap.add_argument("--parallel", type=int, default=MAX_PARALLEL,
                    help=f"concurrent batch workers (default {MAX_PARALLEL}, capped at {MAX_PARALLEL})")
    ap.add_argument("--dpi", type=int, default=DEFAULT_DPI)
    ap.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    ap.add_argument("--max-payload-mb", type=float, default=DEFAULT_MAX_PAYLOAD_MB,
                    help="per-request body budget in MB (base64); auto-split above this")
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--end", type=int, default=None)
    ap.add_argument("--api-key", default=None)
    ap.add_argument("--no-cache", action="store_true", help="ignore per-batch cache / re-run all")
    ap.add_argument("--dry-run", action="store_true", help="list batches and exit")
    args = ap.parse_args()

    n = page_count(args.pdf)
    end = args.end or n
    pages = list(range(args.start, min(end, n) + 1))
    if not pages:
        sys.exit("ERROR: empty page range")
    batches = list(chunks(pages, args.batch_size))
    parallel = max(1, min(args.parallel, MAX_PARALLEL))
    budget_chars = int(args.max_payload_mb * 1024 * 1024)

    log(f"[pdf_extract] {os.path.basename(args.pdf)}  pages={n}  extracting={pages[0]}-{pages[-1]}"
        f"  batch_size={args.batch_size}  batches={len(batches)}  parallel={parallel}"
        f"  model={args.model}  dpi={args.dpi}  payload<={args.max_payload_mb}MB")
    if args.dry_run:
        for b in batches:
            log(f"  batch {b[0]:>4}-{b[-1]:<4} ({len(b)} pages)")
        return

    import openai
    client = openai.OpenAI(base_url=BASE_URL, api_key=resolve_api_key(args), timeout=600,
                           default_headers={"x-opencode-session": f"pdf-extract/{os.getpid()}"})

    cache_dir = args.out + ".batches"
    os.makedirs(cache_dir, exist_ok=True)
    lock = threading.Lock()

    def cache_path(b):
        return os.path.join(cache_dir, f"batch_{b[0]:05d}_{b[-1]:05d}.json")

    def save(r):
        json.dump(r, open(cache_path(r["pages"]), "w"))

    def execute(b):
        cp = cache_path(b)
        if not args.no_cache and os.path.exists(cp):
            try:
                r = json.load(open(cp))
                if "page_texts" in r:               # new schema only
                    r["cached"] = True
                    with lock:
                        log(f"  batch {b[0]}-{b[-1]}: cache hit")
                    return r
            except Exception:
                pass
        stats = {"input_tokens": 0, "output_tokens": 0, "repairs": 0, "splits": 0,
                 "payload_splits": 0, "failed_pages": []}
        t0 = time.perf_counter()
        page_texts = _extract_group(client, args.model, args.pdf, b, args.dpi,
                                    args.max_tokens, budget_chars, stats)
        secs = round(time.perf_counter() - t0, 2)
        r = {"pages": b, "page_texts": {str(p): t for p, t in page_texts.items()},
             "seconds": secs, "input_tokens": stats["input_tokens"],
             "output_tokens": stats["output_tokens"], "repairs": stats["repairs"],
             "splits": stats["splits"], "payload_splits": stats["payload_splits"],
             "failed_pages": stats["failed_pages"],
             "error": "some pages failed" if stats["failed_pages"] else None}
        save(r)
        with lock:
            log(f"  batch {r['pages'][0]}-{r['pages'][-1]}: {secs}s "
                f"in={r['input_tokens']} out={r['output_tokens']} "
                f"repairs={r['repairs']} splits={r['splits']} failed={len(r['failed_pages'])}")
        return r

    t0 = time.perf_counter()
    results = []
    with cf.ThreadPoolExecutor(max_workers=parallel) as pool:
        for res in pool.map(execute, batches):
            results.append(res)
    elapsed = time.perf_counter() - t0

    results.sort(key=lambda r: r["pages"][0])
    page_texts = {}
    for r in results:
        for key, val in r["page_texts"].items():
            page_texts[int(key)] = val

    parts = []
    for p in pages:
        txt = (page_texts.get(p) or "").strip() or "[no extractable content]"
        parts.append(f"===== PAGE {p} =====\n{txt}")
    header = (f"<!-- extracted by pdf_extract.py | model={args.model} | "
              f"pages={pages[0]}-{pages[-1]} | source={os.path.basename(args.pdf)} -->\n\n")
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(header + "\n\n".join(parts) + "\n")

    tin = sum(r["input_tokens"] for r in results)
    tout = sum(r["output_tokens"] for r in results)
    failed_pages = [p for r in results for p in r.get("failed_pages", [])]
    pin, pout = PRICING.get(args.model, (0.15, 0.50))
    cost = tin / 1e6 * pin + tout / 1e6 * pout
    meta = {
        "source": os.path.abspath(args.pdf), "output": os.path.abspath(args.out),
        "model": args.model, "pages": f"{pages[0]}-{pages[-1]}", "page_count": len(pages),
        "batch_size": args.batch_size, "parallel": parallel, "dpi": args.dpi,
        "elapsed_seconds": round(elapsed, 1),
        "input_tokens": tin, "output_tokens": tout, "est_cost_usd": round(cost, 4),
        "failed_batches": len([r for r in results if r.get("error")]),
        "failed_pages": len(failed_pages),
        "repairs": sum(r.get("repairs", 0) for r in results),
        "splits": sum(r.get("splits", 0) for r in results),
        "payload_splits": sum(r.get("payload_splits", 0) for r in results),
        "batches": [{"pages": [r["pages"][0], r["pages"][-1]], "seconds": r["seconds"],
                     "in": r["input_tokens"], "out": r["output_tokens"],
                     "cached": r.get("cached", False), "repairs": r.get("repairs", 0),
                     "splits": r.get("splits", 0), "payload_splits": r.get("payload_splits", 0),
                     "failed_pages": r.get("failed_pages", []), "error": r.get("error")}
                    for r in results],
    }
    json.dump(meta, open(args.out + ".meta.json", "w"), indent=2)
    log(f"[pdf_extract] done: {len(pages)} pages in {elapsed:.1f}s | "
        f"in={tin:,} out={tout:,} tokens | est ${cost:.4f} | "
        f"failed_pages={meta['failed_pages']} repairs={meta['repairs']} "
        f"splits={meta['splits']}\n  -> {args.out}")


if __name__ == "__main__":
    main()
