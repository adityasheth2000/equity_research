---
name: screener-navigator
description: Use whenever the user wants to download investor presentations and concall transcripts from screener.in. Trigger on "download docs from screener", "fetch screener documents for...", "get PPTs and transcripts", or any task requiring screener.in document downloads.
allowed-tools: Bash(python .opencode/skills/screener-navigator/*)
---

# Screener Navigator

Downloads investor presentations (PPTs) and concall transcripts from a screener.in company page into the proper stock folder structure.

## Prerequisites

- Repo-level `.venv` with `requests`, `beautifulsoup4`, and `PyMuPDF` installed
- `OPENROUTER_API_KEY` in repo `.env` (not needed for downloads)

## Usage

```bash
source .venv/bin/activate

python .opencode/skills/screener-navigator/download_docs.py \
  --url "https://www.screener.in/company/{TICKER}/consolidated/" \
  --max 5
```

Downloads the 5 most recent investor presentations to `{TICKER}/presentation/` and concall transcripts to `{TICKER}/concall/`. Transcript PDFs are auto-converted to `.txt` via PyMuPDF. Idempotent — skips existing files.

## Output Structure After Download

```
TICKER/
├── presentation/                       # PPT PDFs downloaded from concalls
│   ├── PPT_May2026.pdf
│   └── ...
├── concall/                            # Transcript PDFs + .txt files
│   ├── Transcript_May2026.pdf
│   ├── Transcript_May2026.txt
│   └── ...
└── (analysis folders and artifacts are managed separately)
```

## Analysis Workflow

Since modern LLMs can directly read PDFs, the analysis workflow is now model-driven rather than script-driven:

1. **Download documents** using this skill
2. **Read PDFs directly** — use the read tool on PPT PDFs and transcript PDFs for direct model interpretation
3. **Read financial data** from the Screener.in webpage snapshot
4. **Synthesize** into a verdict — no intermediate extraction scripts needed