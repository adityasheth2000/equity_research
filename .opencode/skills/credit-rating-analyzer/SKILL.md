---
name: credit-rating-analyzer
description: Use whenever the user wants to analyze credit rating reports (CRISIL, ICRA, CARE, India Ratings, etc.) for equity research. Extracts rating actions, outlook changes, financial metrics, debt profile, rationale, and key risk factors. Supports both PDF (vision model via qwen) and HTML (BeautifulSoup + LLM structuring). Use for understanding credit profile, bank facility details, and risk factors flagged by agencies.
allowed-tools: Bash(python .opencode/skills/credit-rating-analyzer/*)
---

# Credit Rating Analyzer for Equity Research

Extracts credit rating reports into structured markdown. PDFs go through vision-model extraction (like ppt-analyzer). HTML pages (e.g., CRISIL rationale) are downloaded, parsed with BeautifulSoup, and structured by the LLM. Idempotent — skips if the output `.md` already exists.

For comparison across reports, just extract each one individually and the LLM will compare them during analysis — no separate compare step needed.

## Configuration (`.env` file at repo root)

```
OPENROUTER_API_KEY=sk-or-v1-...
CREDIT_RATING_MODEL=qwen/qwen3.5-flash-02-23
CREDIT_RATING_PARALLEL=50
```

## Prerequisites

- Python venv at `.venv/` with `beautifulsoup4`, `pdf2image`, `requests`, `python-dotenv`
- `poppler` (`brew install poppler` on macOS) — only for PDF reports; HTML mode doesn't need it

## Usage

### PDF extraction

```bash
source .venv/bin/activate

python .opencode/skills/credit-rating-analyzer/credit_rating_analyzer.py \
  --pdf COMPANY/credit_ratings/CRISIL_Sep2025.pdf
```

### HTML extraction (CRISIL rationale pages)

```bash
# From a URL (date auto-detected from CRISIL URL):
python .opencode/skills/credit-rating-analyzer/credit_rating_analyzer.py \
  --html "https://www.crisil.com/mnt/winshare/Ratings/RatingList/RatingDocs/CompanyName_March%2010_%202026_RR_xxx.html" \
  --output-dir COMPANY/credit_ratings

# With explicit name:
python .opencode/skills/credit-rating-analyzer/credit_rating_analyzer.py \
  --html "https://..." --html-name CRISIL_Mar2026 --output-dir COMPANY/credit_ratings

# From a saved local .html file:
python .opencode/skills/credit-rating-analyzer/credit_rating_analyzer.py \
  --html COMPANY/credit_ratings/crisil_page.html --html-name CRISIL_Dec2024
```

## Output

For `COMPANY/credit_ratings/CRISIL_Mar2026.pdf` or `--html` with `--html-name CRISIL_Mar2026`:

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

1. **PDF:** PDF → page images (pdf2image, 200 DPI) → vision model per page → concatenate
2. **HTML:** Download/read HTML → BeautifulSoup text extraction → LLM structures into markdown
