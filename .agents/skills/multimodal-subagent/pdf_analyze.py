#!/usr/bin/env python3
"""Send one or more PDFs to an OpenRouter multimodal model with a custom prompt.

Usage:
  python pdf_analyze.py --prompt "Extract key financials" a.pdf b.pdf
  python pdf_analyze.py -p "Summarise risks" -o out.md *.pdf
"""

import argparse
import base64
import json
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "google/gemini-3.8-flash"


def pdf_to_data_uri(pdf_path):
    data = Path(pdf_path).read_bytes()
    b64 = base64.b64encode(data).decode("utf-8")
    return f"data:application/pdf;base64,{b64}"


def build_messages(prompt, pdf_paths):
    content = [{"type": "text", "text": prompt}]
    for path in pdf_paths:
        content.append({
            "type": "image_url",
            "image_url": {"url": pdf_to_data_uri(path)},
        })
    return [{"role": "user", "content": content}]


def call_openrouter(messages, model=DEFAULT_MODEL):
    resp = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={"model": model, "messages": messages},
        timeout=300,
    )
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser(description="Analyse PDFs via OpenRouter multimodal model")
    parser.add_argument("pdfs", nargs="+", type=Path, help="One or more PDF files")
    parser.add_argument("--prompt", "-p", required=True, help="Analysis prompt")
    parser.add_argument("--model", "-m", default=DEFAULT_MODEL, help=f"Model (default: {DEFAULT_MODEL})")
    parser.add_argument("--output", "-o", type=Path, help="Write response to file")
    args = parser.parse_args()

    if not API_KEY:
        print("ERROR: OPENROUTER_API_KEY not set in .env", file=sys.stderr)
        sys.exit(1)

    for path in args.pdfs:
        if not path.exists():
            print(f"ERROR: file not found: {path}", file=sys.stderr)
            sys.exit(1)

    print(f"Sending {len(args.pdfs)} PDF(s) to {args.model}...", flush=True)
    messages = build_messages(args.prompt, args.pdfs)
    result = call_openrouter(messages, args.model)
    content = result["choices"][0]["message"]["content"]

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
        print(f"  -> {args.output}")
    else:
        print(content)


if __name__ == "__main__":
    main()