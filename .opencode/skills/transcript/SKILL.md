---
name: transcript
description: Use whenever the user wants to extract content from a concall/earnings-call transcript PDF for equity research. Converts the PDF to markdown via PyMuPDF text extraction (fast, exact, no LLM), then reads and interprets the content — the LLM extracts key financial data, management commentary, guidance, Q&A highlights, and risk factors from the transcript. Trigger on "extract this transcript", "parse this concall", "convert transcript to markdown", or any request to pull content from a transcript PDF.
allowed-tools: Bash(python .opencode/utils/*)
---

# Transcript Analyzer for Equity Research

Two-step pipeline:
1. **Convert** the transcript PDF to markdown using `pdf_text_to_md.py` (PyMuPDF — no LLM, just text extraction from the document's text layer).
2. **Read & interpret** the resulting `.md` file — the agent/LLM reads the full transcript and extracts equity-relevant information: financial figures, management outlook/guidance, segment commentary, Q&A highlights, risk flags, and competitive positioning.

## Prerequisites

- Python venv at `.venv/` with `PyMuPDF` installed
- No poppler, no API keys needed for conversion

## Usage

```bash
source .venv/bin/activate

# Convert PDF → markdown
python .opencode/utils/pdf_text_to_md.py \
  --pdf COMPANY/concall/Transcript_May2026.pdf

# Custom output path
python .opencode/utils/pdf_text_to_md.py \
  --pdf COMPANY/concall/Transcript_May2026.pdf \
  --output COMPANY/concall/Transcript_May2026.md
```

## Output

For `COMPANY/concall/Transcript_May2026.pdf`:
- `COMPANY/concall/Transcript_May2026.md` — full text with `## Page N` headings and `---` separators.

## Pipeline

1. **Extract** — read every page's text layer via PyMuPDF (`page.get_text()`), preserving all formatting and content verbatim.
2. **Write** — output a single markdown file with page headings and separators.
3. **Interpret** — the calling agent/LLM reads the `.md` in full and extracts all equity-relevant data (no API call, the interpretation is done in-context).