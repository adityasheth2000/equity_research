#!/usr/bin/env python3
"""PDF Vision → Markdown: extract equity-relevant content from a PDF using vision models.

Renders each PDF page to an image, then uses a vision LLM to extract only
equity-research-relevant content, caching per-page results and concatenating
them into a single markdown file.

Works on any PDF — investor presentations, BSE/NSE announcements, credit rating
reports, annual reports, exchange filings, etc. Use `--doc-type` to tailor the
extraction prompt, or `--prompt` to supply a fully custom prompt.

3-phase pipeline:
  1. Convert PDF → page images (pdf2image)
  2. Per-page: vision model extracts equity-research-relevant content only
  3. Concatenate all page markdowns into a single {pdf_name}.md
"""

import sys
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from pdf2image import convert_from_path

from _common import (
    MODEL,
    PARALLEL,
    MAX_PAGES,
    call_vision_model,
    concatenate_markdowns,
    require_api_key,
)

COMMON_DO_EXTRACT = """DO extract:
- Financial metrics (revenue, PAT, EBITDA, margins, growth rates, ROE, ROCE, EPS, borrowings, debt, etc.)
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
- Photographs of factories/offices/people (unless directly tied to capacity/expansion data)"""

DOC_TYPE_PROMPTS = {
    "presentation": (
        "You are analyzing slides from an investor presentation for EQUITY RESEARCH purposes. "
        "Extract only information relevant to an equity analyst evaluating this company.\n\n"
        + COMMON_DO_EXTRACT
    ),
    "announcement": (
        "You are analyzing a stock-exchange announcement/filing (e.g., BSE/NSE disclosure under SEBI LODR) "
        "for EQUITY RESEARCH purposes. Extract only information relevant to an equity analyst evaluating this company.\n\n"
        "DO additionally extract:\n"
        "- The exact subject/category of the announcement (e.g., board meeting outcome, award of order, "
        "acquisition, divestment, change in management, financial results, dividend, shareholding change)\n"
        "- The date of the announcement and the effective/record dates mentioned\n"
        "- Names of counterparties, entities acquired/divested, and percentage stake involved\n"
        "- Deal values, consideration, and any monetary figures (in original currency, e.g., Rs Cr / Rs Mn)\n"
        "- Regulatory references (e.g., SEBI LODR Regulation numbers, stock exchange names)\n"
        "- Any conditions precedent, approvals required, or timelines\n\n"
        + COMMON_DO_EXTRACT
    ),
    "credit-rating": (
        "You are analyzing a credit rating report for EQUITY RESEARCH purposes. "
        "Extract all credit-relevant information that an equity analyst evaluating this company needs.\n\n"
        "DO extract:\n"
        "- Rating action (reaffirmed/upgraded/downgraded) and the specific rating (e.g., CRISIL A, CRISIL BBB+, etc.)\n"
        "- Outlook (Stable, Positive, Negative) and any change from previous outlook\n"
        "- Total bank facilities rated and their amounts\n"
        "- Breakup of facilities by bank (bank name, facility type, amount in Rs.Cr)\n"
        "- Key financial metrics cited (revenue, EBITDA, PAT, margins, debt/equity, interest coverage, NWC days, ROCE, etc.)\n"
        "- Rationale for the rating action — what factors led to the rating/outlook decision\n"
        "- Business risk profile assessment (market position, diversification, customer concentration, etc.)\n"
        "- Financial risk profile assessment (leverage, liquidity, debt protection metrics)\n"
        "- Any specific risks flagged by the rating agency (demand risk, raw material risk, geopolitical, regulatory, etc.)\n"
        "- Debt maturity profile, repayment obligations, upcoming capex commitments\n"
        "- Subsidiary/joint-venture details that factor into the consolidated rating\n"
        "- Any covenants, security details, or specific terms on bank facilities\n"
        "- Comparative metrics vs previous rating cycle (if mentioned in the report)\n"
        "- Analyst names, date of report, next review timeline\n\n"
        "DO NOT extract:\n"
        "- Standard legal boilerplate and disclaimers\n"
        "- Rating agency's own disclaimers about methodology (unless contains specific methodology changes)\n"
        "- Page numbers, headers, footers without substance\n"
        "- Generic \"About the Rating Agency\" sections"
    ),
    "generic": (
        "You are analyzing a financial document for EQUITY RESEARCH purposes. "
        "Extract only information relevant to an equity analyst evaluating the company.\n\n"
        + COMMON_DO_EXTRACT
    ),
}

CLOSING_INSTRUCTION = """

If a page contains NO material equity research information, respond with exactly: "No material content."

Otherwise, transcribe the relevant content faithfully — keep numbers exact, use markdown tables for tabular data, describe chart data accurately. Precede each extraction with the page's apparent title or topic."""


def pdf_to_images(pdf_path, image_dir, dpi=200, start_page=1, num_pages=None):
    """Convert PDF pages to PNG images."""
    image_dir.mkdir(parents=True, exist_ok=True)

    first_page = start_page
    last_page = (start_page + num_pages - 1) if num_pages else None

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


def build_prompt(doc_type, custom_prompt=None):
    """Return the vision prompt for a given document type (or a custom prompt)."""
    if custom_prompt:
        return custom_prompt + CLOSING_INSTRUCTION
    return DOC_TYPE_PROMPTS.get(doc_type, DOC_TYPE_PROMPTS["generic"]) + CLOSING_INSTRUCTION


def extract_page(img_path, pages_dir, page_num, prompt):
    """Extract content from a single page image. Returns (page_num, status[, char_count])."""
    md_path = pages_dir / f"page_{page_num:03d}.md"

    if md_path.exists():
        return (page_num, "skip")

    try:
        content = call_vision_model(img_path, prompt, model=MODEL)
        md_path.write_text(f"## Page {page_num}\n\n{content}\n", encoding="utf-8")
        return (page_num, "ok", len(content))
    except Exception as e:
        print(f"  ERROR page {page_num}: {e}", flush=True)
        md_path.write_text(f"## Page {page_num}\n\n*Extraction failed: {e}*\n", encoding="utf-8")
        return (page_num, "fail")


def analyze_pages(image_dir, pages_dir, parallel, prompt, start_page, num_pages):
    """Extract content from page images within [start_page, start_page+num_pages-1] in parallel."""
    pages_dir.mkdir(parents=True, exist_ok=True)
    last_page = start_page + num_pages - 1

    image_paths = sorted(image_dir.glob("page_*.png"))
    image_paths = [
        p for p in image_paths
        if start_page <= int(p.stem.split("_")[1]) <= last_page
    ]
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
            executor.submit(extract_page, img_path, pages_dir, page_num, prompt): page_num
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


def main():
    parser = argparse.ArgumentParser(
        description="Extract equity-relevant content from financial PDFs using vision models"
    )
    parser.add_argument("--pdf", required=True, help="Path to PDF file")
    parser.add_argument(
        "--doc-type",
        choices=list(DOC_TYPE_PROMPTS.keys()),
        default="presentation",
        help="Document type to tailor the extraction prompt (default: presentation)",
    )
    parser.add_argument(
        "--prompt",
        help="Custom extraction prompt (overrides --doc-type). Use for ad-hoc one-off extractions.",
    )
    parser.add_argument("--dpi", type=int, default=200, help="Image resolution (default: 200)")
    parser.add_argument(
        "--start-page",
        type=int,
        required=True,
        help="1-indexed page to start reading from (required)",
    )
    parser.add_argument(
        "--num-pages",
        type=int,
        required=True,
        help=f"Number of pages to read (required, max {MAX_PAGES})",
    )
    parser.add_argument("--parallel", type=int, default=PARALLEL, help=f"Parallel workers (default: {PARALLEL})")
    parser.add_argument("--skip-images", action="store_true", help="Skip PDF→images step")
    parser.add_argument("--skip-pages", action="store_true", help="Skip per-page extraction step")
    args = parser.parse_args()

    require_api_key()

    if args.start_page < 1:
        print(f"ERROR: --start-page must be >= 1 (got {args.start_page})")
        sys.exit(1)

    if args.num_pages < 1:
        print(f"ERROR: --num-pages must be >= 1 (got {args.num_pages})")
        sys.exit(1)

    if args.num_pages > MAX_PAGES:
        print(
            f"ERROR: --num-pages cannot exceed {MAX_PAGES} (got {args.num_pages}). "
            f"Each page is a separate LLM call. Split into multiple runs, e.g. "
            f"--start-page {args.start_page + MAX_PAGES} --num-pages {args.num_pages - MAX_PAGES}."
        )
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

    prompt = build_prompt(args.doc_type, args.prompt)

    print(f"PDF     : {pdf_path.name}")
    print(f"Dir     : {out_dir}")
    print(f"DocType : {'custom' if args.prompt else args.doc_type}")
    print(f"Pages   : {args.start_page}-{args.start_page + args.num_pages - 1} ({args.num_pages} pages)")
    print(f"Model   : {MODEL}")
    print(f"Parallel: {args.parallel}\n")

    if not args.skip_images:
        print("=== Phase 1: PDF → Images ===")
        img_paths = pdf_to_images(pdf_path, image_dir, args.dpi, args.start_page, args.num_pages)
        print(f"  Done: {len(img_paths)} images\n")
    else:
        print("=== Phase 1: SKIPPED ===\n")

    if not args.skip_pages:
        print("=== Phase 2: Extract per page ===")
        analyze_pages(image_dir, pages_dir, args.parallel, prompt, args.start_page, args.num_pages)
        print()
    else:
        print("=== Phase 2: SKIPPED ===\n")

    print("=== Phase 3: Combine ===")
    concatenate_markdowns(pages_dir, output_md)
    print(f"\nDone -> {output_md}")


if __name__ == "__main__":
    main()
