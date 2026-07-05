#!/usr/bin/env python3
"""PPT Analyzer: Extract equity-relevant content from investor presentation PDFs using vision models.

3-phase pipeline:
  1. Convert PDF → page images (pdf2image)
  2. Per-page: vision model extracts equity-research-relevant content only
  3. Concatenate all page markdowns into a single {pdf_name}.md
"""

import os
import sys
import time
import base64
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from dotenv import load_dotenv
from pdf2image import convert_from_path

load_dotenv()

MODEL = os.getenv("PPT_ANALYZER_MODEL", "qwen/qwen3.5-flash-02-23")
PARALLEL = int(os.getenv("PPT_ANALYZER_PARALLEL", "50"))
API_KEY = os.getenv("OPENROUTER_API_KEY", "")

VISION_PROMPT = """You are analyzing slides from an investor presentation for EQUITY RESEARCH purposes. Extract only information relevant to an equity analyst evaluating this company.

DO extract:
- Financial metrics (revenue, PAT, EBITDA, margins, growth rates, ROE, ROCE, EPS, etc.)
- Business metrics (capacity, utilization, volumes, order book, client count, ASP, etc.)
- Strategic initiatives, expansion plans, capex, new projects, M&A
- Competitive advantages, moats, market share, industry positioning
- Guidance, outlook, management targets, growth visibility
- Risk factors that could materially impact the business
- Management commentary on performance or strategy
- Segment-wise or geography-wise breakdowns
- Key charts showing financial/business trends (describe data and trends, not visual styling)
- New product launches, diversification, regulatory developments

DO NOT extract:
- Company logos, brand imagery, decorative photos
- Standard legal disclaimers (unless they contain specific, unusual risk disclosures)
- Table of contents / section dividers with no data
- Contact information, addresses, registrar details
- Generic "About Us" fluff or marketing slogans with no substance
- Page numbers, headers, footers without substance
- Photographs of factories/offices/people (unless directly tied to capacity/expansion data)

If a slide contains NO material equity research information, respond with exactly: "No material content."

Otherwise, transcribe the relevant content faithfully — keep numbers exact, use markdown tables for tabular data, describe chart data accurately. Precede each extraction with the slide's apparent title or topic."""


def pdf_to_images(pdf_path, image_dir, dpi=200, start_page=1, end_page=None):
    """Convert PDF pages to PNG images."""
    image_dir.mkdir(parents=True, exist_ok=True)

    first_page = start_page
    last_page = end_page

    images = convert_from_path(
        str(pdf_path), dpi=dpi, first_page=first_page, last_page=last_page, fmt="png"
    )

    image_paths = []
    for i, img in enumerate(images, start=first_page):
        img_path = image_dir / f"page_{i:03d}.png"
        img.save(str(img_path), "PNG")
        image_paths.append(img_path)
        print(f"  Saved: {img_path.name}")

    return image_paths


def image_to_base64(image_path):
    """Convert image to base64 data URI."""
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    ext = image_path.suffix.lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}.get(ext, "image/png")
    return f"data:{mime};base64,{data}"


def call_vision_model(image_path, model):
    """Call OpenRouter vision model to extract equity-relevant content from a page image."""

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": VISION_PROMPT},
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


def extract_page(img_path, pages_dir, page_num, total):
    """Extract content from a single page image. Returns (page_num, success, char_count)."""
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
    """Extract content from all page images in parallel."""
    pages_dir.mkdir(parents=True, exist_ok=True)
    image_paths = sorted(image_dir.glob("page_*.png"))
    total = len(image_paths)

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
            executor.submit(extract_page, img_path, pages_dir, page_num, total): page_num
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
    """Concatenate all page markdowns into a single file with separators."""
    md_files = sorted(pages_dir.glob("page_*.md"))

    if not md_files:
        print("  No markdown files to combine", flush=True)
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
        description="Extract equity-relevant content from investor presentation PDFs using vision models"
    )
    parser.add_argument("--pdf", required=True, help="Path to PDF file")
    parser.add_argument("--dpi", type=int, default=200, help="Image resolution (default: 200)")
    parser.add_argument("--start-page", type=int, default=1)
    parser.add_argument("--end-page", type=int)
    parser.add_argument("--parallel", type=int, default=PARALLEL, help=f"Parallel workers (default: {PARALLEL})")
    parser.add_argument("--skip-images", action="store_true", help="Skip PDF→images step")
    parser.add_argument("--skip-pages", action="store_true", help="Skip per-page extraction step")
    args = parser.parse_args()

    if not API_KEY:
        print("ERROR: OPENROUTER_API_KEY not set in .env")
        sys.exit(1)

    pdf_path = Path(args.pdf).resolve()
    if not pdf_path.exists():
        print(f"ERROR: PDF not found: {pdf_path}")
        sys.exit(1)

    stem = pdf_path.stem
    out_dir = pdf_path.parent  # output .md alongside the PDF
    tmp_dir = pdf_path.parent.parent / "tmp"  # tmp at company level
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
