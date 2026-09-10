---
name: multimodal-subagent
description: Use whenever the user wants to analyse one or more PDF documents via OpenRouter multimodal models. Sends PDFs directly (no image conversion) with a user-supplied prompt. Use for "analyse this PDF", "extract this document", "read this presentation via model".
allowed-tools: Bash(python .agents/skills/multimodal-subagent/*)
---

# Multimodal PDF Subagent

Sends one or more PDF files directly to an OpenRouter multimodal model with a custom prompt. No image conversion needed — PDFs are base64-encoded and sent inline.

## Prerequisites

- `OPENROUTER_API_KEY` in repo `.env`
- Python: `requests`, `python-dotenv`

## Usage

```bash
source .venv/bin/activate

# Single file:
python .agents/skills/multimodal-subagent/pdf_analyze.py TICKER/presentation/PPT_May2026.pdf \
  -p "Extract all financial data, segment breakdowns, and guidance"

# Multiple files:
python .agents/skills/multimodal-subagent/pdf_analyze.py TICKER/concall/*.pdf \
  -p "Summarise management commentary and Q&A highlights across these transcripts"

# Write output to file:
python .agents/skills/multimodal-subagent/pdf_analyze.py *.pdf \
  -p "Compare financials and strategy across these reports" -o analysis.md
```

## Calling from the Main Agent

```
source .venv/bin/activate
python .agents/skills/multimodal-subagent/pdf_analyze.py <pdf-files...> -p "<prompt>" [-o <output.md>]
```

The calling agent supplies the specific prompt and the PDF paths. There are no hardcoded prompts — the agent decides what question to ask for each document or batch.
