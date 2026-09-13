#!/usr/bin/env python3
"""
pdf_extract.py — vision-LLM PDF -> text/markdown extractor for equity research.

Uses the OpenCode Go gateway with the GLM-5.3-Flash vision model. Pages are
rendered to images IN MEMORY (never written to disk), grouped into batches, and
sent to the model in parallel. Designed for investor presentations, annual
reports (300+ pages) and concall transcripts.

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
DEFAULT_BATCH_SIZE = 20                    # pages per scheduling unit
MAX_PARALLEL = 5                           # concurrent batch workers (hard cap)
DEFAULT_DPI = 150
DEFAULT_MAX_TOKENS = 16000
DEFAULT_MAX_PAYLOAD_MB = 2.5               # per HTTP request body budget (base64 chars)
# OpenCode Go pricing, $/1M tokens (input, output)
PRICING = {"glm-5.3-flash": (0.15, 0.50), "qwen3.8-flash": (0.15, 0.47)}

EXTRACTION_PROMPT = """\
You are a meticulous document-transcription engine used by equity analysts.

You are given consecutive pages (as images) of ONE document, in order. \
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
8. If a page is empty or illegible, output exactly "[page N: no extractable content]".

OUTPUT FORMAT
Begin each page with a line exactly:
===== PAGE <n> =====
where <n> is the page number supplied below, then the transcription. Emit nothing \
before the first page marker or after the last page. Never merge pages.
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


def chunks(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


# ----------------------------------------------------------------------------
# model call
# ----------------------------------------------------------------------------
def call_group(client, model, pages, images, max_tokens, retries=4):
    content = [{
        "type": "text",
        "text": EXTRACTION_PROMPT + "\nPages in this batch, in order: " + ", ".join(map(str, pages)),
    }]
    for im in images:
        content.append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{im}"}})

    last = None
    for attempt in range(retries):
        try:
            r = client.chat.completions.create(
                model=model, messages=[{"role": "user", "content": content}],
                max_tokens=max_tokens,
            )
            return (r.choices[0].message.content or ""), r.usage
        except Exception as e:                      # noqa: BLE001
            last = e
            if is_payload_error(e):
                raise
            wait = 3 * (2 ** attempt)
            log(f"    retry {attempt + 1}/{retries} pages {pages[0]}-{pages[-1]} "
                f"({type(e).__name__}: {str(e)[:100]}) sleeping {wait}s")
            time.sleep(wait)
    raise last


def _extract_group(client, model, pdf, pages, dpi, max_tokens, budget_chars, depth=0):
    """Render (once) then call; recursively halve the page list on payload errors."""
    t0 = time.perf_counter()
    seg = f"{pages[0]}-{pages[-1]}"
    try:
        imgs = render_pages(pdf, pages, dpi)
        groups = split_by_payload(pages, imgs, budget_chars)
        text_parts, tin, tout = [], 0, 0
        for g in groups:
            txt, usage = call_group(client, model, g, [imgs[p] for p in g], max_tokens)
            text_parts.append(txt)
            tin += getattr(usage, "prompt_tokens", 0)
            tout += getattr(usage, "completion_tokens", 0)
        return {"pages": pages, "text": "\n\n".join(text_parts), "seconds": round(time.perf_counter() - t0, 2),
                "input_tokens": tin, "output_tokens": tout, "error": None}
    except Exception as e:                          # noqa: BLE001
        if is_payload_error(e) and len(pages) > 1:
            mid = len(pages) // 2
            log(f"    split {seg} -> {len(pages[:mid])}+{len(pages[mid:])} "
                f"({type(e).__name__}: {str(e)[:70]})")
            return [_extract_group(client, model, pdf, pages[:mid], dpi, max_tokens, budget_chars, depth + 1),
                    _extract_group(client, model, pdf, pages[mid:], dpi, max_tokens, budget_chars, depth + 1)]
        log(f"    batch {seg}: FAILED ({type(e).__name__}: {str(e)[:120]})")
        body = "\n".join(f"[page {p}: extraction failed: {type(e).__name__}]" for p in pages)
        return {"pages": pages, "text": body, "seconds": round(time.perf_counter() - t0, 2),
                "input_tokens": 0, "output_tokens": 0, "error": str(e)[:200]}


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
                r["cached"] = True
                with lock:
                    log(f"  batch {b[0]}-{b[-1]}: cache hit")
                return r
            except Exception:
                pass
        r = _extract_group(client, args.model, args.pdf, b, args.dpi, args.max_tokens, budget_chars)
        out = r if isinstance(r, list) else [r]
        for rr in out:
            save(rr)
            with lock:
                log(f"  batch {rr['pages'][0]}-{rr['pages'][-1]}: {rr['seconds']}s "
                    f"in={rr['input_tokens']} out={rr['output_tokens']}")
        return r

    t0 = time.perf_counter()
    results = []
    with cf.ThreadPoolExecutor(max_workers=parallel) as pool:
        for res in pool.map(execute, batches):
            results.extend(res if isinstance(res, list) else [res])
    elapsed = time.perf_counter() - t0

    results.sort(key=lambda r: r["pages"][0])
    body = "\n\n".join((r["text"] or "").strip() for r in results)
    header = (f"<!-- extracted by pdf_extract.py | model={args.model} | "
              f"pages={pages[0]}-{pages[-1]} | source={os.path.basename(args.pdf)} -->\n\n")
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(header + body + "\n")

    tin = sum(r["input_tokens"] for r in results)
    tout = sum(r["output_tokens"] for r in results)
    pin, pout = PRICING.get(args.model, (0.15, 0.50))
    cost = tin / 1e6 * pin + tout / 1e6 * pout
    meta = {
        "source": os.path.abspath(args.pdf), "output": os.path.abspath(args.out),
        "model": args.model, "pages": f"{pages[0]}-{pages[-1]}", "page_count": len(pages),
        "batch_size": args.batch_size, "parallel": parallel, "dpi": args.dpi,
        "elapsed_seconds": round(elapsed, 1),
        "input_tokens": tin, "output_tokens": tout, "est_cost_usd": round(cost, 4),
        "failed_batches": len([r for r in results if r.get("error")]),
        "batches": [{"pages": [r["pages"][0], r["pages"][-1]], "seconds": r["seconds"],
                     "in": r["input_tokens"], "out": r["output_tokens"],
                     "cached": r.get("cached", False), "error": r.get("error")} for r in results],
    }
    json.dump(meta, open(args.out + ".meta.json", "w"), indent=2)
    log(f"[pdf_extract] done: {len(pages)} pages in {elapsed:.1f}s | "
        f"in={tin:,} out={tout:,} tokens | est ${cost:.4f} | failures={meta['failed_batches']}\n"
        f"  -> {args.out}")


if __name__ == "__main__":
    main()
