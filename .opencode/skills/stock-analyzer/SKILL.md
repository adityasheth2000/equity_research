---
name: stock-analyzer
description: Use whenever the user wants to set up a full stock analysis workflow from a screener.in HTML snapshot. Handles downloading investor presentations and concall transcripts, running vision-based PPT analysis, and converting transcripts to text. Use for bootstrapping a new company analysis, setting up research artifacts, or when the user says "analyze this stock", "set up analysis for...", "download concalls", "gather documents".
---

# Stock Analyzer

Orchestrates a complete equity research workflow starting from a screener.in HTML snapshot. PPTs, transcripts, and credit ratings are stored at the **company level** (shared across analysis dates). Each dated folder contains only the screener snapshot and analysis outputs.

## Prerequisites

- Repo-level `.venv` with dependencies installed
- `OPENROUTER_API_KEY` in `.env`
- `brew install poppler`

## Workflow

**Tip:** Steps 2 and 3 are independent and can run in parallel via subagents for faster results. Step 4 should wait until all extractions complete.

### Step 1: Download Documents

Run `download_docs.py` — parses the screener HTML's "Concalls" section, downloads PPTs and transcripts, converts transcripts to `.txt`. Idempotent.

### Step 2: Analyze PPTs (parallel with Step 3)

Invoke the **ppt-analyzer** skill — run its script on each downloaded PPT to extract content via vision model. Idempotent.

### Step 3: Extract Credit Ratings (parallel with Step 2)

Invoke the **credit-rating-analyzer** skill — find rating links in the screener HTML's "Credit ratings" section and extract each one. Most CRISIL reports are HTML pages; use `--html`. Older reports may be PDFs; use `--pdf`.

### Step 4: Compile Verdict

Read all sources chronologically (screener.html, credit_ratings/*.md, PPT_*.md, Transcript_*.txt) and write `verdict.md` in the dated folder covering: company overview, financial analysis, quarterly progression, strategy & growth, management quality, risks (including credit rating trajectory), valuation context, and key monitorables.

## Output Structure

```
COMPANY/
├── presentation/                   # PPTs + vision-extracted .md
├── concall/                        # Transcript PDFs + .txt
├── credit_ratings/                 # Rating reports .md
├── tmp/                            # Intermediate artifacts (gitignored)
└── 8-july-2026/                    # Analysis snapshot
    ├── screener.html
    ├── screener_files/
    └── verdict.md
```
