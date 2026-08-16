#!/usr/bin/env python3
"""Shared helpers for the equity-research extraction utilities.

Used by pdf_vision_to_md.py, pdf_text_to_md.py, and html_text_to_md.py.
Holds the OpenRouter API helpers (vision + text), image encoding, and the
markdown concatenation helper so they aren't duplicated across tools.
"""

import os
import time
import base64

import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY", "")

DEFAULT_MODEL = "qwen/qwen3.5-flash-02-23"
MODEL = os.getenv(
    "PDF_ANALYZER_MODEL",
    os.getenv("PPT_ANALYZER_MODEL", DEFAULT_MODEL),
)
PARALLEL = int(
    os.getenv(
        "PDF_ANALYZER_PARALLEL",
        os.getenv("PPT_ANALYZER_PARALLEL", "50"),
    )
)

# Each page is a separate LLM call — hard cap on pages per run to avoid runaway API usage.
MAX_PAGES = 30
# Max raw text chars fed to the structuring LLM in a single call (cost guardrail).
MAX_TEXT_CHARS = 100_000


def image_to_base64(image_path):
    """Convert an image file to a base64 data URI."""
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    ext = image_path.suffix.lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}.get(ext, "image/png")
    return f"data:{mime};base64,{data}"


def _post_chat(payload, timeout):
    """POST to OpenRouter with basic retry on timeout / 5xx."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    max_retries = 3
    for attempt in range(max_retries):
        try:
            resp = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=timeout)
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]
        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                wait = 2 ** attempt
                print(f"    Timeout, retrying in {wait}s...", flush=True)
                time.sleep(wait)
            else:
                raise
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1 and getattr(e.response, "status_code", 0) >= 500:
                wait = 2 ** attempt
                print(f"    Server error (attempt {attempt + 1}), retrying in {wait}s...", flush=True)
                time.sleep(wait)
            else:
                raise


def call_vision_model(image_path, prompt, model=MODEL, max_tokens=4096, timeout=120):
    """Call the vision model on a single page image with the given prompt."""
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
        "max_tokens": max_tokens,
    }
    return _post_chat(payload, timeout)


def call_text_model(prompt, model=MODEL, max_tokens=8192, timeout=180):
    """Call the text model with the given prompt."""
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
    }
    return _post_chat(payload, timeout)


def concatenate_markdowns(pages_dir, output_path):
    """Concatenate all page_NNN.md files in pages_dir into a single file with separators."""
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


def require_api_key():
    """Exit if OPENROUTER_API_KEY is not configured."""
    import sys

    if not API_KEY:
        print("ERROR: OPENROUTER_API_KEY not set in .env")
        sys.exit(1)
