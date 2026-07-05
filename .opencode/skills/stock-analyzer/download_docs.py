#!/usr/bin/env python3
"""Download investor presentations and concall transcripts from a screener.in HTML snapshot.

Parses the Concalls section of a saved screener.in page, downloads PPTs to
presentation/ and transcripts to concall/ with proper naming, and converts
transcripts to plain text.
"""

import os
import sys
import argparse
from pathlib import Path

import requests
import fitz  # PyMuPDF
from bs4 import BeautifulSoup


def extract_concall_entries(html_path):
    """Parse screener.in HTML and extract concall entries: (quarter, transcript_url, ppt_url)."""
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")

    concalls_section = None
    for h3 in soup.find_all("h3"):
        if h3.text.strip() == "Concalls":
            parent = h3.parent
            while parent:
                ul = parent.find("ul", class_="list-links")
                if ul:
                    concalls_section = ul
                    break
                parent = parent.parent
            break

    if not concalls_section:
        print("ERROR: Could not find Concalls section")
        return []

    entries = []
    for li in concalls_section.find_all("li", class_="flex"):
        date_div = li.find("div", class_=lambda c: c and "ink-600" in c and "nowrap" in c)
        if not date_div:
            continue
        quarter = date_div.text.strip()

        transcript_url = None
        ppt_url = None

        for a in li.find_all("a", class_="concall-link"):
            if not a.get("href"):
                continue
            title = a.get("title", "")
            text = a.text.strip()
            if "Raw Transcript" in title:
                transcript_url = a["href"]
            elif text == "PPT":
                ppt_url = a["href"]

        entries.append({"quarter": quarter, "transcript_url": transcript_url, "ppt_url": ppt_url})

    return entries


def resolve_filename(prefix, quarter, target_dir, used_names):
    """Resolve filename, handling duplicate months with _2, _3 suffixes."""
    base = f"{prefix}_{quarter.replace(' ', '')}"
    if base not in used_names:
        used_names.add(base)
        return target_dir / f"{base}.pdf"
    count = 2
    while f"{base}_{count}" in used_names:
        count += 1
    name = f"{base}_{count}"
    used_names.add(name)
    return target_dir / f"{name}.pdf"


def download_file(url, dest_path):
    """Download a file from URL to dest_path. Returns (True, size_kb) or (False, error)."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=60, stream=True)
        resp.raise_for_status()
        dest_path.write_bytes(resp.content)
        return True, len(resp.content) // 1024
    except Exception as e:
        return False, str(e)


def download_docs(entries, ppt_dir, concall_dir):
    """Download all PPTs and transcripts from parsed entries."""
    ppt_dir.mkdir(parents=True, exist_ok=True)
    concall_dir.mkdir(parents=True, exist_ok=True)

    used_ppt = set()
    used_transcript = set()
    ppt_downloaded = []
    transcript_downloaded = []

    for entry in entries:
        quarter = entry["quarter"]
        print(f"  {quarter}:")

        if entry["ppt_url"]:
            dest = resolve_filename("PPT", quarter, ppt_dir, used_ppt)
            if dest.exists():
                print(f"    PPT: skip (already exists: {dest.name})")
            else:
                print(f"    PPT: downloading...", end=" ", flush=True)
                ok, info = download_file(entry["ppt_url"], dest)
                if ok:
                    print(f"-> presentation/{dest.name} ({info} KB)")
                    ppt_downloaded.append(dest)
                else:
                    print(f"FAILED: {info}")

        if entry["transcript_url"]:
            dest = resolve_filename("Transcript", quarter, concall_dir, used_transcript)
            if dest.exists():
                print(f"    Transcript: skip (already exists: {dest.name})")
            else:
                print(f"    Transcript: downloading...", end=" ", flush=True)
                ok, info = download_file(entry["transcript_url"], dest)
                if ok:
                    print(f"-> concall/{dest.name} ({info} KB)")
                    transcript_downloaded.append(dest)
                else:
                    print(f"FAILED: {info}")
        print()

    return ppt_downloaded, transcript_downloaded


def convert_transcripts_to_text(transcript_pdfs):
    """Convert transcript PDFs to plain text using PyMuPDF."""
    for pdf_path in transcript_pdfs:
        txt_path = pdf_path.with_suffix(".txt")
        if txt_path.exists():
            print(f"  skip: {txt_path.name} already exists")
            continue

        print(f"  Converting: {pdf_path.name}...", end=" ", flush=True)
        try:
            doc = fitz.open(str(pdf_path))
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            txt_path.write_text(text, encoding="utf-8")
            print(f"-> {txt_path.name} ({len(text)} chars)")
        except Exception as e:
            print(f"FAILED: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Download investor presentations and concall transcripts from screener.in HTML"
    )
    parser.add_argument("--html", required=True, help="Path to screener.in HTML file")
    parser.add_argument("--output-dir", help="Dated analysis directory (default: parent of HTML)")
    parser.add_argument("--max", type=int, default=5, help="Max recent concall entries to download (default: 5)")
    parser.add_argument("--skip-download", action="store_true", help="Skip downloading, only list entries")
    parser.add_argument("--skip-transcript-text", action="store_true", help="Skip transcript → text conversion")
    args = parser.parse_args()

    html_path = Path(args.html).resolve()
    if not html_path.exists():
        print(f"ERROR: HTML file not found: {html_path}")
        sys.exit(1)

    dated_dir = Path(args.output_dir).resolve() if args.output_dir else html_path.parent
    ppt_dir = dated_dir / "presentation"
    concall_dir = dated_dir / "concall"

    print(f"HTML : {html_path.name}")
    print(f"Dir  : {dated_dir}")
    print(f"PPTs : presentation/")
    print(f"Con  : concall/")
    print(f"Max  : {args.max} recent quarters\n")

    entries = extract_concall_entries(html_path)
    if not entries:
        print("No concall entries found.")
        sys.exit(1)

    print(f"Concalls found ({len(entries)}):")
    for e in entries:
        t = "✓" if e["transcript_url"] else "✗"
        p = "✓" if e["ppt_url"] else "✗"
        print(f"  {e['quarter']:12s}  Transcript: {t}  PPT: {p}")
    print()

    if args.skip_download:
        return

    print("=== Downloading ===")
    ppt_list, transcript_list = download_docs(entries[:args.max], ppt_dir, concall_dir)

    if not args.skip_transcript_text and transcript_list:
        print("\n=== Converting Transcripts to Text ===")
        convert_transcripts_to_text(transcript_list)

    print("\nDone.")


if __name__ == "__main__":
    main()
