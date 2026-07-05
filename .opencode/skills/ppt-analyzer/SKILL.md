---
name: ppt-analyzer
description: Use whenever the user wants to extract content from investor presentation PDFs/PPTs for equity research. Extracts only equity-relevant information using vision models. Handles converting slides to images, parallel vision-OCR extraction per page, and concatenation into a single markdown.
---

# PPT Analyzer for Equity Research

Extracts equity-relevant content from investor presentation PDFs using vision models — preserving charts, tables, and numerical data that plain PDF-to-text libraries lose. Skips non-material content (logos, disclaimers, generic fluff). Idempotent: skips if the output `.md` already exists.

## Configuration (`.env` file at repo root)

```
OPENROUTER_API_KEY=sk-or-v1-...
PPT_ANALYZER_MODEL=qwen/qwen3.5-flash-02-23
PPT_ANALYZER_PARALLEL=50
```

## Prerequisites

- Python venv at `.venv/` with dependencies installed
- System dependency: `poppler` (`brew install poppler` on macOS)

## Usage

```bash
source .venv/bin/activate

# Run once per PPT — output .md lands alongside the PDF, tmp/ at company level
python .opencode/skills/ppt-analyzer/ppt_analyzer.py \
  --pdf COMPANY/presentation/PPT_May2026.pdf

# Resume from specific phase:
python .opencode/skills/ppt-analyzer/ppt_analyzer.py \
  --pdf COMPANY/presentation/PPT_May2026.pdf --skip-images --parallel 20
```

## Output

For `COMPANY/presentation/PPT_May2026.pdf`, produces:
- `COMPANY/tmp/PPT_May2026_images/` — one PNG per page (gitignored)
- `COMPANY/tmp/PPT_May2026_pages/` — one `.md` per page (gitignored)
- `COMPANY/presentation/PPT_May2026.md` — all pages concatenated with `---` separators

## Pipeline

1. **PDF → Images** (`pdf2image`, 200 DPI)
2. **Per-page extraction** (OpenRouter vision model, up to 50 parallel calls) — extracts only equity-relevant content, returns "No material content." for non-substantive pages
3. **Concatenate** — all page markdowns merged into a single file
