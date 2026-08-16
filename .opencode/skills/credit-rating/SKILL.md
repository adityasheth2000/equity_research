---
name: credit-rating
description: Use whenever the user wants to analyze credit rating reports (CRISIL, ICRA, CARE, India Ratings, etc.) for equity research. Extracts rating actions, outlook changes, financial metrics, debt profile, rationale, and key risk factors. Supports both PDF (via pdf_vision_to_md.py) and HTML (via html_text_to_md.py). Use for understanding credit profile, bank facility details, and risk factors flagged by agencies.
allowed-tools: Bash(python .opencode/utils/*)
---

# Credit Rating Analyzer for Equity Research

Extracts credit rating reports into structured markdown. PDFs go through the vision-model pipeline (`pdf_vision_to_md.py --doc-type credit-rating`). HTML pages (e.g., CRISIL rationale) are scraped with BeautifulSoup and structured by the LLM (`html_text_to_md.py --preset credit-rating`).

For comparison across reports, just extract each one individually and the LLM will compare them during analysis — no separate compare step needed.

## Configuration (`.env` file at repo root)

```
OPENROUTER_API_KEY=sk-or-v1-...
PDF_ANALYZER_MODEL=qwen/qwen3.5-flash-02-23
PDF_ANALYZER_PARALLEL=50
```

## Prerequisites

- Python venv at `.venv/` with `beautifulsoup4`, `pdf2image`, `requests`, `python-dotenv`, `PyMuPDF`
- `poppler` (`brew install poppler` on macOS) — only for PDF reports; HTML mode doesn't need it

## Usage

### PDF extraction (vision)

```bash
source .venv/bin/activate

python .opencode/utils/pdf_vision_to_md.py \
  --pdf COMPANY/credit_ratings/CRISIL_Sep2025.pdf \
  --doc-type credit-rating --start-page 1 --num-pages 20
```

### HTML extraction (CRISIL rationale pages)

```bash
# From a URL (date auto-detected from CRISIL/ICRA URL):
python .opencode/utils/html_text_to_md.py \
  --html "https://www.crisil.com/mnt/winshare/Ratings/RatingList/RatingDocs/CompanyName_March%2010_%202026_RR_xxx.html" \
  --preset credit-rating --output COMPANY/credit_ratings/CRISIL_Mar2026.md

# With explicit name + output:
python .opencode/utils/html_text_to_md.py \
  --html "https://..." --name CRISIL_Mar2026 --output COMPANY/credit_ratings/CRISIL_Mar2026.md

# From a saved local .html file:
python .opencode/utils/html_text_to_md.py \
  --html COMPANY/credit_ratings/crisil_page.html --name CRISIL_Dec2024 \
  --output COMPANY/credit_ratings/CRISIL_Dec2024.md
```

## Output

For `COMPANY/credit_ratings/CRISIL_Mar2026.pdf` (or `--html` with `--name CRISIL_Mar2026`):

- **PDF mode:** `COMPANY/tmp/CRISIL_Mar2026_images/` (gitignored), `COMPANY/tmp/CRISIL_Mar2026_pages/` (gitignored)
- **Both modes:** `COMPANY/credit_ratings/CRISIL_Mar2026.md` — structured markdown with sections:
  - Rating Action
  - Detailed Rationale
  - Key Rating Drivers (Strengths / Weaknesses)
  - Liquidity
  - Outlook & Rating Sensitivity
  - Key Financial Indicators
  - Bank Facilities
  - Company & Subsidiaries

## Pipeline

1. **PDF:** PDF → page images (pdf2image, 200 DPI) → vision model per page (`--doc-type credit-rating`) → concatenate
2. **HTML:** Download/read HTML → BeautifulSoup text extraction → LLM structures into markdown (`--preset credit-rating`)
