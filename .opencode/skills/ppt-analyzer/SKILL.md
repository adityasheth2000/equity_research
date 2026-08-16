---
name: ppt-analyzer
description: Use whenever the user wants to extract content from an investor presentation PPT/PDF (or any vision-only financial PDF such as BSE/NSE announcements, exchange filings, annual reports) for equity research. Extracts only equity-relevant information using vision models — preserving charts, tables, and numerical data that plain text extraction loses. Trigger on "analyze this presentation", "extract this PPT", "analyze this BSE filing", "extract this announcement", or any request to pull content from a financial PDF via vision.
allowed-tools: Bash(python .opencode/utils/*)
---

# PPT / Vision PDF Analyzer for Equity Research

Extracts equity-relevant content from PDFs using vision models — preserving charts, tables, and numerical data that plain PDF-to-text libraries lose. Best for investor presentations, announcements, and filings where layout/charts matter. Skips non-material content (logos, disclaimers, generic fluff). Idempotent at the page level: already-extracted pages (cached `.md` in `tmp/`) are skipped on re-runs.

Uses the shared `pdf_vision_to_md.py` utility.

## Configuration (`.env` file at repo root)

```
OPENROUTER_API_KEY=sk-or-v1-...
PDF_ANALYZER_MODEL=qwen/qwen3.5-flash-02-23
PDF_ANALYZER_PARALLEL=50
```

## Prerequisites

- Python venv at `.venv/` with dependencies installed
- System dependency: `poppler` (`brew install poppler` on macOS)

## Usage

```bash
source .venv/bin/activate

# Investor presentation (default doc-type) — first 30 pages
python .opencode/utils/pdf_vision_to_md.py \
  --pdf COMPANY/presentation/PPT_May2026.pdf \
  --start-page 1 --num-pages 30

# BSE/NSE announcement or exchange filing (usually a few pages)
python .opencode/utils/pdf_vision_to_md.py \
  --pdf COMPANY/announcements/BSE_Announcement_23Jul.pdf \
  --doc-type announcement --start-page 1 --num-pages 3

# Any other financial document (annual report, etc.)
python .opencode/utils/pdf_vision_to_md.py \
  --pdf COMPANY/annual_reports/AR_FY2026.pdf \
  --doc-type generic --start-page 1 --num-pages 30

# Resume from specific phase:
python .opencode/utils/pdf_vision_to_md.py \
  --pdf COMPANY/presentation/PPT_May2026.pdf \
  --start-page 1 --num-pages 30 --skip-images --parallel 20
```

## Page Range (required)

`--start-page` and `--num-pages` are **both required** — this is a hard safety guardrail because **each page is a separate LLM (vision) call**.

- `--start-page`: 1-indexed page to begin reading from (must be >= 1).
- `--num-pages`: number of pages to read (must be >= 1).
- **Max 30 pages per run** (`--num-pages` > 30 aborts with an error). For larger PDFs, run in chunks:
  ```bash
  python .opencode/utils/pdf_vision_to_md.py --pdf big.pdf --start-page 1  --num-pages 30
  python .opencode/utils/pdf_vision_to_md.py --pdf big.pdf --start-page 31 --num-pages 30
  ```
  (Each run writes the same output `.md`; chunking appends pages incrementally since per-page `.md` files are cached in `tmp/`.)

## Document Types

| `--doc-type` | Use for | Additional extraction focus |
|--------------|---------|------------------------------|
| `presentation` | Investor presentations, PPTs | (default) financials, business metrics, guidance, moats, segments |
| `announcement` | BSE/NSE filings, exchange disclosures | announcement subject/category, dates, counterparties, stake %, deal values, regulatory references |
| `credit-rating` | Credit rating report PDFs | rating action, outlook, bank facilities, rationale, risk factors |
| `generic` | Annual reports, misc | standard equity extraction only |

## Output

For `COMPANY/presentation/PPT_May2026.pdf`, produces:
- `COMPANY/tmp/PPT_May2026_images/` — one PNG per page (gitignored)
- `COMPANY/tmp/PPT_May2026_pages/` — one `.md` per page (gitignored)
- `COMPANY/presentation/PPT_May2026.md` — all pages concatenated with `---` separators

## Pipeline

1. **PDF → Images** (`pdf2image`, 200 DPI)
2. **Per-page extraction** (OpenRouter vision model, up to 50 parallel calls) — extracts only equity-relevant content using the doc-type-specific prompt, returns "No material content." for non-substantive pages
3. **Concatenate** — all page markdowns merged into a single file
