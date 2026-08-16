#!/usr/bin/env python3
"""HTML Text → Markdown: extract and structure text from an HTML page using BeautifulSoup + LLM.

For structured HTML pages (e.g. credit rating rationales on CRISIL/ICRA sites),
scrape the raw text and send it through an LLM to organize it into a clean markdown
report. Takes either a URL or a local HTML file.

Pipeline:
  1. Fetch HTML (URL) or read file
  2. BeautifulSoup → clean raw text (truncated to a safe size)
  3. LLM structuring pass using a preset prompt
  4. Write output markdown
"""

import re
import sys
import argparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from _common import MODEL, MAX_TEXT_CHARS, call_text_model, require_api_key

HTML_STRUCTURE_PROMPTS = {
    "credit-rating": """You are an equity analyst extracting a credit rating report from raw text. Structure this into a well-organized markdown report.

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

{raw_text}""",
    "generic": """You are an equity analyst cleaning up a raw scraped web page into well-structured markdown.
Extract only the substantive financial/business content relevant to equity research. Preserve all
numbers and facts exactly, use markdown tables where tabular data exists, and drop navigation,
boilerplate, disclaimers, and advertisements.

Raw text:

{raw_text}""",
}


def fetch_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.text


def html_to_raw_text(html_content):
    """Extract cleaned plain text from HTML via BeautifulSoup."""
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator="\n")
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    return "\n".join(lines)


def extract_date_from_url(url):
    """Try to derive a YYYY/MM date from a CRISIL/ICRA-style URL, e.g. '.../ShowRationaleReport/?Id=...'."""
    decoded = url.replace("%20", " ")
    match = re.search(
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}[,_]\s*(\d{4})",
        decoded,
    )
    if match:
        return f"{match.group(1)[:3]}{match.group(2)}"
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Extract and structure text from an HTML page (URL or local file) to markdown"
    )
    parser.add_argument("--html", required=True, help="URL or path to a local HTML file")
    parser.add_argument(
        "--preset",
        choices=list(HTML_STRUCTURE_PROMPTS.keys()),
        default="credit-rating",
        help="Structuring prompt preset (default: credit-rating)",
    )
    parser.add_argument("--output", help="Output markdown path (default: {name}.md in CWD)")
    parser.add_argument(
        "--name",
        help="Output filename stem. Auto-detected from the URL/file otherwise.",
    )
    args = parser.parse_args()

    require_api_key()

    html_input = args.html
    out_path = Path(args.output).resolve() if args.output else None

    if args.name:
        stem = args.name
    elif html_input.startswith("http"):
        stem = extract_date_from_url(html_input) or Path(html_input.split("/")[-1].replace(".html", "")).stem[:50]
    else:
        stem = Path(html_input).stem

    if out_path is None:
        out_path = (Path.cwd() / f"{stem}.md").resolve()

    print(f"HTML   : {html_input}")
    print(f"Name   : {stem}")
    print(f"Preset : {args.preset}")
    print(f"Model  : {MODEL}\n")

    if html_input.startswith("http"):
        print(f"  Downloading: {html_input}", flush=True)
        html_content = fetch_url(html_input)
    else:
        html_content = Path(html_input).read_text(encoding="utf-8")

    raw_text = html_to_raw_text(html_content)
    print(f"  Extracted {len(html_content)} chars of HTML -> {len(raw_text)} chars of text", flush=True)

    if len(raw_text) > MAX_TEXT_CHARS:
        raw_text = raw_text[:MAX_TEXT_CHARS] + "\n\n[... content truncated ...]"

    print("  Structuring with LLM...", flush=True)
    prompt = HTML_STRUCTURE_PROMPTS[args.preset].format(raw_text=raw_text)
    markdown = call_text_model(prompt, model=MODEL, max_tokens=8192)

    out_path.write_text(markdown, encoding="utf-8")
    print(f"\nDone -> {out_path} ({len(markdown)} chars)")


if __name__ == "__main__":
    main()
