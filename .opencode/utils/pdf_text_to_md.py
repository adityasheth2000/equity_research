#!/usr/bin/env python3
"""PDF Text → Markdown: convert a PDF with a selectable text layer to markdown using PyMuPDF.

For documents where the PDF already contains a text layer (e.g. concall transcripts,
exchange filings generated from text) direct text extraction is fast, exact, and free.
Extracts text from every page and writes a single markdown file with `## Page N`
headings and `---` separators. No LLM involved — the interpretation/extraction is
left to the caller (see the `transcript` skill).

Pipeline:
  1. Extract text from all pages (PyMuPDF)
  2. Write output markdown
"""

import sys
import argparse
from pathlib import Path

import fitz  # PyMuPDF


def extract_pdf_text(pdf_path):
    """Extract raw text from every page. Returns list of (page_num, text)."""
    doc = fitz.open(str(pdf_path))
    pages = []
    for pno in range(doc.page_count):
        pages.append((pno + 1, doc[pno].get_text()))
    doc.close()
    return pages


def main():
    parser = argparse.ArgumentParser(
        description="Convert a PDF (with text layer) to markdown using PyMuPDF"
    )
    parser.add_argument("--pdf", required=True, help="Path to PDF file")
    parser.add_argument(
        "--output",
        help="Output markdown path. Defaults to {pdf}.md next to the PDF.",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf).resolve()
    if not pdf_path.exists():
        print(f"ERROR: PDF not found: {pdf_path}")
        sys.exit(1)

    out_path = Path(args.output).resolve() if args.output else (pdf_path.parent / f"{pdf_path.stem}.md")

    print(f"PDF : {pdf_path.name}\n")

    pages = extract_pdf_text(pdf_path)

    parts = [f"## Page {pno}\n\n{text}" for pno, text in pages]
    out_path.write_text("\n\n---\n\n".join(parts), encoding="utf-8")

    print(f"Done -> {out_path} ({len(pages)} pages)")


if __name__ == "__main__":
    main()
