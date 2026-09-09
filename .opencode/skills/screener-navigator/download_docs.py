#!/usr/bin/env python3
"""Download investor presentations, concall transcripts, and annual reports from a screener.in company URL.

Fetches the page HTML, parses the Concalls and Annual Reports sections, downloads PPTs to
presentation/, transcripts to concall/, and annual reports to annual_reports/ with proper naming.
Transcripts are auto-converted to plain text via PyMuPDF.
"""

import os
import sys
import re
import argparse
from pathlib import Path

import requests
import fitz  # PyMuPDF
from bs4 import BeautifulSoup


def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.text


def extract_concall_entries(html):
    soup = BeautifulSoup(html, "html.parser")

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


def extract_annual_report_entries(html):
    soup = BeautifulSoup(html, "html.parser")

    for h3 in soup.find_all("h3"):
        if h3.text.strip() != "Annual reports":
            continue

        parent = h3.parent
        while parent:
            entries = []
            for a in parent.find_all("a", href=True):
                text = a.text.strip()
                m = re.search(r"Annual Report (\d{4})", text)
                if m:
                    year = m.group(1)
                    entries.append({"year": year, "url": a["href"]})
            if entries:
                return sorted(entries, key=lambda e: e["year"], reverse=True)
            parent = parent.parent
        break

    return []


def resolve_filename(prefix, quarter, target_dir, used_names):
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
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=120, stream=True)
        resp.raise_for_status()
        dest_path.write_bytes(resp.content)
        return True, len(resp.content) // 1024
    except Exception as e:
        return False, str(e)


def download_docs(entries, ppt_dir, concall_dir):
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
                    print(f"-> {ppt_dir.name}/{dest.name} ({info} KB)")
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
                    print(f"-> {concall_dir.name}/{dest.name} ({info} KB)")
                    transcript_downloaded.append(dest)
                else:
                    print(f"FAILED: {info}")
        print()

    return ppt_downloaded, transcript_downloaded


def download_annual_reports(entries, annual_dir):
    annual_dir.mkdir(parents=True, exist_ok=True)
    downloaded = []

    for entry in entries:
        year = entry["year"]
        dest = annual_dir / f"AnnualReport_{year}.pdf"
        if dest.exists():
            print(f"  {year}: skip (already exists: {dest.name})")
            continue
        print(f"  {year}: downloading...", end=" ", flush=True)
        ok, info = download_file(entry["url"], dest)
        if ok:
            print(f"-> {annual_dir.name}/{dest.name} ({info} KB)")
            downloaded.append(dest)
        else:
            print(f"FAILED: {info}")

    return downloaded


def convert_transcripts_to_text(transcript_pdfs):
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
        description="Download investor presentations, concall transcripts, and annual reports from screener.in"
    )
    parser.add_argument("--url", required=True, help="Screener.in company URL (e.g. https://www.screener.in/company/TCS/consolidated/)")
    parser.add_argument("--max", type=int, default=5, help="Max recent concall entries to download (default: 5)")
    parser.add_argument("--max-annual-reports", type=int, default=2, help="Max annual reports to download (default: 2)")
    parser.add_argument("--skip-annual-reports", action="store_true", help="Skip annual report downloads")
    parser.add_argument("--skip-download", action="store_true", help="Skip downloading, only list entries")
    parser.add_argument("--skip-transcript-text", action="store_true", help="Skip transcript -> text conversion")
    args = parser.parse_args()

    url = args.url.rstrip("/")
    ticker = url.split("/company/")[1].split("/")[0]
    company_dir = Path(ticker)
    ppt_dir = company_dir / "presentation"
    concall_dir = company_dir / "concall"
    annual_dir = company_dir / "annual_reports"

    print(f"URL      : {url}")
    print(f"Ticker   : {ticker}")
    print(f"PPTs     : {ticker}/presentation/")
    print(f"Concalls : {ticker}/concall/")
    print(f"Annual   : {ticker}/annual_reports/")
    print(f"Max      : {args.max} recent quarters\n")

    print("Fetching page...", flush=True)
    try:
        html = fetch_page(url)
    except Exception as e:
        print(f"ERROR fetching page: {e}")
        sys.exit(1)

    entries = extract_concall_entries(html)
    if not entries:
        print("No concall entries found.")
        sys.exit(1)

    print(f"Concalls found ({len(entries)}):")
    for e in entries:
        t = "\u2713" if e["transcript_url"] else "\u2717"
        p = "\u2713" if e["ppt_url"] else "\u2717"
        print(f"  {e['quarter']:12s}  Transcript: {t}  PPT: {p}")
    print()

    annual_entries = []
    if not args.skip_annual_reports:
        annual_entries = extract_annual_report_entries(html)
        if annual_entries:
            print(f"Annual reports found ({len(annual_entries)}):")
            for a in annual_entries[: args.max_annual_reports]:
                print(f"  {a['year']}")
            print()

    if args.skip_download:
        return

    print("=== Downloading ===")
    ppt_list, transcript_list = download_docs(entries[: args.max], ppt_dir, concall_dir)

    if annual_entries and not args.skip_annual_reports:
        print("\n=== Downloading Annual Reports ===")
        download_annual_reports(annual_entries[: args.max_annual_reports], annual_dir)

    if not args.skip_transcript_text and transcript_list:
        print("\n=== Converting Transcripts to Text ===")
        convert_transcripts_to_text(transcript_list)

    print("\nDone.")


if __name__ == "__main__":
    main()