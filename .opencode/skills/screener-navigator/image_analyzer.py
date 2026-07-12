#!/usr/bin/env python3
"""Generic image analysis via OpenRouter vision models.

Takes any image and a prompt, calls an OpenRouter vision model, and writes
the analysis to a file or stdout. Defaults to a screener.in financial analysis
prompt when no custom prompt is provided.
"""

import os
import sys
import time
import base64
import argparse
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("IMAGE_ANALYZER_MODEL", "qwen/qwen3.5-flash-02-23")
API_KEY = os.getenv("OPENROUTER_API_KEY", "")

DEFAULT_SCREENER_PROMPT = """You are analyzing a screenshot of a screener.in company page for EQUITY RESEARCH purposes. Extract ALL financial data visible in the image. Be thorough and precise.

Extract every section visible:

1. Company Overview: Name, current price, market cap, P/E, dividend yield, 52-week range, face value, book value, sector, industry, website links.

2. Peer Comparison Table: All columns for every peer company — CMP, P/E, Mar Cap, Div Yld, NP Qtr, Qtr Profit Var %, Sales Qtr, Qtr Sales Var %, ROCE %. Include Median row.

3. Quarterly Results: Full table with all quarter columns. Extract every row — Sales, Expenses, Operating Profit, OPM %, Other Income, Interest, Depreciation, Profit before tax, Tax %, Net Profit, EPS. Include all visible quarter columns with exact values.

4. Profit & Loss (Annual): Full table with all year columns. Extract Sales, Expenses, Operating Profit, OPM %, Other Income, Interest, Depreciation, Profit before tax, Tax %, Net Profit, EPS, Dividend Payout %. Include Compounded Sales Growth, Compounded Profit Growth, Stock Price CAGR, Return on Equity.

5. Balance Sheet (Annual): Full table. Extract Equity Capital, Reserves, Borrowings, Other Liabilities, Total Liabilities, Fixed Assets, CWIP, Investments, Other Assets, Total Assets.

6. Cash Flows (Annual): Full table. Extract Cash from Operating Activity, Investing Activity, Financing Activity, Net Cash Flow, Free Cash Flow, CFO/OP.

7. Ratios: All ratio rows across all years — Debtor Days, Inventory Days, Days Payable, Cash Conversion Cycle, Working Capital Days, ROCE %.

8. Shareholding Pattern: Promoters, FIIs, DIIs, Government, Public percentages across all quarters. Include No. of Shareholders.

9. Documents section: List all concall entries with their date and available links (PPT/Transcript/REC). List credit ratings with dates and agency. List annual reports with years.

10. Insights (if visible): Any headcount, client metrics, revenue mix, order book, attrition, AI revenue data.

Format all data in markdown tables with exact numbers. For sections not visible in the screenshot, note "Not visible in screenshot". Do NOT summarize or skip rows — extract every visible data point."""


def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    ext = image_path.suffix.lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}.get(ext, "image/png")
    return f"data:{mime};base64,{data}"


def call_vision_model(image_path, prompt, model):
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_to_base64(image_path), "detail": "high"}},
                ],
            }
        ],
        "max_tokens": 8192,
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
                timeout=180,
            )
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]
        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                wait = 2 ** attempt
                print(f"  Timeout, retrying in {wait}s...", flush=True)
                time.sleep(wait)
            else:
                raise
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1 and getattr(e.response, "status_code", 0) >= 500:
                wait = 2 ** attempt
                print(f"  Server error (attempt {attempt+1}), retrying in {wait}s...", flush=True)
                time.sleep(wait)
            else:
                raise


def main():
    parser = argparse.ArgumentParser(
        description="Analyze an image using OpenRouter vision models"
    )
    parser.add_argument("--image", required=True, help="Path to image file (PNG, JPG)")
    parser.add_argument("--output", help="Output file path (default: stdout)")
    parser.add_argument("--prompt", help="Custom prompt text")
    parser.add_argument("--prompt-file", help="Read prompt from a file")
    parser.add_argument("--screener", action="store_true", help="Use default screener.in analysis prompt")
    parser.add_argument("--model", default=MODEL, help=f"Vision model (default: {MODEL})")
    args = parser.parse_args()

    if not API_KEY:
        print("ERROR: OPENROUTER_API_KEY not set in .env")
        sys.exit(1)

    image_path = Path(args.image).resolve()
    if not image_path.exists():
        print(f"ERROR: Image not found: {image_path}")
        sys.exit(1)

    if args.prompt:
        prompt = args.prompt
    elif args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    elif args.screener:
        prompt = DEFAULT_SCREENER_PROMPT
    else:
        prompt = DEFAULT_SCREENER_PROMPT

    print(f"Image  : {image_path.name}")
    print(f"Model  : {args.model}")
    print(f"Output : {args.output or 'stdout'}")
    print(f"Prompt : {'screener default' if not args.prompt and not args.prompt_file else 'custom'}")
    print()

    output_path = Path(args.output) if args.output else None
    if output_path and output_path.exists():
        print(f"SKIP: {output_path.name} already exists\n")
        return

    print("Analyzing...", flush=True)
    try:
        content = call_vision_model(image_path, prompt, args.model)
    except Exception as e:
        print(f"ERROR: {e}", flush=True)
        sys.exit(1)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
        print(f"Done -> {output_path} ({len(content)} chars)")
    else:
        print(content)


if __name__ == "__main__":
    main()
