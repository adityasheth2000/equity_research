#!/usr/bin/env python3
"""Credit Rating Analyzer: Extract rating actions, outlook, financials, debt profile, and risk factors
from credit rating PDFs and HTML pages using vision models and text extraction.

3-phase pipeline:
  1. Input → page images (PDF via pdf2image, HTML via BeautifulSoup + LLM structuring)
  2. Per-page: vision model extracts credit-rating-relevant content only
  3. Concatenate all page markdowns into a single {name}.md
"""

import os
import sys
import re
import time
import base64
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from dotenv import load_dotenv
from pdf2image import convert_from_path
from bs4 import BeautifulSoup

load_dotenv()

MODEL = os.getenv("CREDIT_RATING_MODEL", os.getenv("PPT_ANALYZER_MODEL", "qwen/qwen3.5-flash-02-23"))
PARALLEL = int(os.getenv("CREDIT_RATING_PARALLEL", os.getenv("PPT_ANALYZER_PARALLEL", "50")))
API_KEY = os.getenv("OPENROUTER_API_KEY", "")

RATING_PROMPT = """You are analyzing a credit rating report for EQUITY RESEARCH purposes. Extract all credit-relevant information that an equity analyst evaluating this company needs.

DO extract:
- Rating action (reaffirmed/upgraded/downgraded) and the specific rating (e.g., CRISIL A, CRISIL BBB+, etc.)
- Outlook (Stable, Positive, Negative) and any change from previous outlook
- Total bank facilities rated and their amounts
- Breakup of facilities by bank (bank name, facility type, amount in Rs.Cr)
- Key financial metrics cited (revenue, EBITDA, PAT, margins, debt/equity, interest coverage, NWC days, ROCE, etc.)
- Rationale for the rating action — what factors led to the rating/outlook decision
- Business risk profile assessment (market position, diversification, customer concentration, etc.)
- Financial risk profile assessment (leverage, liquidity, debt protection metrics)
- Any specific risks flagged by the rating agency (demand risk, raw material risk, geopolitical, regulatory, etc.)
- Debt maturity profile, repayment obligations, upcoming capex commitments
- Subsidiary/joint-venture details that factor into the consolidated rating
- Any covenants, security details, or specific terms on bank facilities
- Comparative metrics vs previous rating cycle (if mentioned in the report)
- Analyst names, date of report, next review timeline

DO NOT extract:
- Standard legal boilerplate and disclaimers
- Rating agency's own disclaimers about methodology (unless contains specific methodology changes)
- Page numbers, headers, footers without substance
- Generic "About the Rating Agency" sections

If a page contains NO material credit rating information, respond with exactly: "No material content."

Otherwise, transcribe the relevant content faithfully — keep all numbers exact, use markdown tables for tabular data, preserve all financial ratios precisely."""


HTML_STRUCTURE_PROMPT = """You are an equity analyst extracting a credit rating report from raw text. Structure this into a well-organized markdown report.

The raw text below is scraped from a credit rating agency's HTML page. Organize it into these sections:

## Rating Action
- Rating, outlook, date, agency name, total facilities rated

## Detailed Rationale
- Summary paragraph explaining the rating/outlook decision

## Key Rating Drivers — Strengths
- List each strength with supporting data

## Key Rating Drivers — Weaknesses
- List each weakness with supporting data

## Liquidity
- Liquidity assessment, cash accruals, bank limit utilisation

## Outlook & Rating Sensitivity
- Outlook statement, upward factors, downward factors

## Key Financial Indicators
- Present as a markdown table if tabular data exists

## Bank Facilities
- Bank-wise breakup as a markdown table

## Company & Subsidiaries
- Company info, consolidated entities

Raw text:

{raw_text}"""


def pdf_to_images(pdf_path, image_dir, dpi=200, start_page=1, end_page=None):
    image_dir.mkdir(parents=True, exist_ok=True)
    images = convert_from_path(
        str(pdf_path), dpi=dpi, first_page=start_page, last_page=end_page, fmt="png"
    )
    image_paths = []
    for i, img in enumerate(images, start=start_page):
        img_path = image_dir / f"page_{i:03d}.png"
        img.save(str(img_path), "PNG")
        image_paths.append(img_path)
        print(f"  Saved: {img_path.name}")
    return image_paths


def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    ext = image_path.suffix.lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}.get(ext, "image/png")
    return f"data:{mime};base64,{data}"


def call_vision_model(image_path, model):
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": RATING_PROMPT},
                    {"type": "image_url", "image_url": {"url": image_to_base64(image_path), "detail": "high"}},
                ],
            }
        ],
        "max_tokens": 4096,
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    max_retries = 3
    for attempt in range(max_retries):
        try:
            resp = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=120,
            )
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]
        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                wait = 2**attempt
                print(f"    Timeout, retrying in {wait}s...", flush=True)
                time.sleep(wait)
            else:
                raise
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1 and getattr(e.response, "status_code", 0) >= 500:
                wait = 2**attempt
                print(f"    Server error (attempt {attempt+1}), retrying in {wait}s...", flush=True)
                time.sleep(wait)
            else:
                raise


def call_text_model(prompt, max_tokens=8192):
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    resp = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def download_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.text


def extract_date_from_crisil_url(url):
    decoded = url.replace("%20", " ")
    match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}[,_]\s*(\d{4})', decoded)
    if match:
        month = match.group(1)[:3]
        year = match.group(2)
        return f"{month}{year}"
    return None


def html_to_markdown(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator="\n")
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    cleaned = "\n".join(lines)
    if len(cleaned) > 50000:
        cleaned = cleaned[:50000] + "\n\n[... content truncated ...]"
    prompt = HTML_STRUCTURE_PROMPT.format(raw_text=cleaned)
    print("  Structuring with LLM...", flush=True)
    return call_text_model(prompt, max_tokens=8192)


def extract_page(img_path, pages_dir, page_num, total):
    md_path = pages_dir / f"page_{page_num:03d}.md"
    if md_path.exists():
        return (page_num, "skip")
    try:
        content = call_vision_model(img_path, MODEL)
        md_path.write_text(f"## Page {page_num}\n\n{content}\n", encoding="utf-8")
        return (page_num, "ok", len(content))
    except Exception as e:
        print(f"  ERROR page {page_num}: {e}", flush=True)
        md_path.write_text(f"## Page {page_num}\n\n*Extraction failed: {e}*\n", encoding="utf-8")
        return (page_num, "fail")


def analyze_pages(image_dir, pages_dir, parallel):
    pages_dir.mkdir(parents=True, exist_ok=True)
    image_paths = sorted(image_dir.glob("page_*.png"))
    tasks = []
    for img_path in image_paths:
        page_num = int(img_path.stem.split("_")[1])
        md_path = pages_dir / f"page_{page_num:03d}.md"
        if md_path.exists():
            print(f"  [skip] page {page_num} (already exists)", flush=True)
            continue
        tasks.append((img_path, page_num))

    if not tasks:
        print("  All pages already extracted", flush=True)
        return

    print(f"  Processing {len(tasks)} pages with {parallel} parallel workers...\n", flush=True)
    completed = 0
    with ThreadPoolExecutor(max_workers=parallel) as executor:
        futures = {
            executor.submit(extract_page, img_path, pages_dir, page_num, len(image_paths)): page_num
            for img_path, page_num in tasks
        }
        for future in as_completed(futures):
            result = future.result()
            completed += 1
            page_num = result[0]
            status = result[1]
            if status == "ok":
                print(f"  [{completed}/{len(tasks)}] page {page_num} -> {result[2]} chars", flush=True)
            elif status == "fail":
                print(f"  [{completed}/{len(tasks)}] page {page_num} -> FAILED", flush=True)


def concatenate_markdowns(pages_dir, output_path):
    md_files = sorted(pages_dir.glob("page_*.md"))
    if not md_files:
        output_path.write_text("", encoding="utf-8")
        return
    with open(output_path, "w", encoding="utf-8") as out:
        for i, md_file in enumerate(md_files):
            out.write(md_file.read_text(encoding="utf-8"))
            out.write("\n")
            if i < len(md_files) - 1:
                out.write("---\n\n")
    print(f"  Combined {len(md_files)} pages -> {output_path.name}", flush=True)


def main():
    parser = argparse.ArgumentParser(
        description="Extract credit rating content from rating PDFs/HTML using vision models"
    )
    parser.add_argument("--pdf", help="Path to rating PDF file")
    parser.add_argument("--html", help="URL or path to HTML rating report (e.g., CRISIL page)")
    parser.add_argument("--html-name", help="Output filename stem for --html. Auto-detected from CRISIL URLs.")
    parser.add_argument("--output-dir", help="Output directory for --html (default: CWD)")
    parser.add_argument("--dpi", type=int, default=200, help="Image resolution for PDFs (default: 200)")
    parser.add_argument("--start-page", type=int, default=1)
    parser.add_argument("--end-page", type=int)
    parser.add_argument("--parallel", type=int, default=PARALLEL, help=f"Parallel workers (default: {PARALLEL})")
    parser.add_argument("--skip-images", action="store_true", help="Skip PDF→images step")
    parser.add_argument("--skip-pages", action="store_true", help="Skip per-page extraction step")
    args = parser.parse_args()

    if not API_KEY:
        print("ERROR: OPENROUTER_API_KEY not set in .env")
        sys.exit(1)

    if args.html:
        html_input = args.html
        out_dir = Path(args.output_dir).resolve() if args.output_dir else Path.cwd()

        if args.html_name:
            stem = args.html_name
        elif html_input.startswith("http"):
            stem = extract_date_from_crisil_url(html_input)
            if stem:
                stem = f"CRISIL_{stem}"
            else:
                stem = Path(html_input.split("/")[-1].replace(".html", "")).stem[:50]
        else:
            stem = Path(html_input).stem

        print(f"HTML    : {html_input}")
        print(f"Name    : {stem}")
        print(f"Model   : {MODEL}\n")

        output_md = out_dir / f"{stem}.md"
        if output_md.exists():
            print(f"SKIP: {output_md.name} already exists\n")
            return

        if html_input.startswith("http"):
            print(f"  Downloading: {html_input}", flush=True)
            html_content = download_html(html_input)
        else:
            html_content = Path(html_input).read_text(encoding="utf-8")

        print(f"  Extracted {len(html_content)} chars of HTML", flush=True)
        markdown = html_to_markdown(html_content)
        output_md.write_text(markdown, encoding="utf-8")
        print(f"  Done -> {output_md.name} ({len(markdown)} chars)", flush=True)
        return

    if not args.pdf:
        print("ERROR: --pdf or --html required")
        sys.exit(1)

    pdf_path = Path(args.pdf).resolve()
    if not pdf_path.exists():
        print(f"ERROR: PDF not found: {pdf_path}")
        sys.exit(1)

    stem = pdf_path.stem
    out_dir = pdf_path.parent
    tmp_dir = out_dir.parent / "tmp"
    image_dir = tmp_dir / f"{stem}_images"
    pages_dir = tmp_dir / f"{stem}_pages"
    output_md = out_dir / f"{stem}.md"

    print(f"PDF     : {pdf_path.name}")
    print(f"Dir     : {out_dir}")
    print(f"Model   : {MODEL}")
    print(f"Parallel: {args.parallel}\n")

    if output_md.exists():
        print(f"SKIP: {output_md.name} already exists\n")
        return

    if not args.skip_images:
        print("=== Phase 1: PDF → Images ===")
        img_paths = pdf_to_images(pdf_path, image_dir, args.dpi, args.start_page, args.end_page)
        print(f"  Done: {len(img_paths)} images\n")
    else:
        print("=== Phase 1: SKIPPED ===\n")

    if not args.skip_pages:
        print("=== Phase 2: Extract per page ===")
        analyze_pages(image_dir, pages_dir, args.parallel)
        print()
    else:
        print("=== Phase 2: SKIPPED ===\n")

    print("=== Phase 3: Combine ===")
    concatenate_markdowns(pages_dir, output_md)
    print(f"\nDone -> {output_md}")


if __name__ == "__main__":
    main()
