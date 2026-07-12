---
name: stock-analyzer
description: Use whenever the user wants to set up a full stock analysis workflow. Handles navigating screener.in to capture financial data and download investor presentations, concall transcripts, and credit ratings. Use for bootstrapping a new company analysis, setting up research artifacts, or when the user says "analyze this stock", "set up analysis for...", "download concalls", "gather documents".
---

# Stock Analyzer

Orchestrates a complete equity research workflow starting from a screener.in company URL. Uses **screener-navigator** skill for browser automation, data extraction, and document downloads. PPTs, transcripts, and credit ratings are stored at the **company level** (shared across analysis dates). Each dated folder contains the analysis outputs.

## Prerequisites

- Repo-level `.venv` with dependencies installed
- `OPENROUTER_API_KEY` in repo `.env`
- `agent-browser` CLI installed
- `brew install poppler`

## Workflow

**Tip:** Steps 2 and 3 are independent and can run in parallel. Step 1 must complete first. Step 4 must run after Steps 2 and 3 finish, and Step 5 must wait until Step 4 is complete.

### Step 1: Fetch Screener Data & Download Documents

Invoke the **screener-navigator** skill on the company URL:

```
https://www.screener.in/company/{TICKER}/consolidated/
```

This does:
- Opens screener.in, logs in, takes a full-page screenshot → `{TICKER}/tmp/screener_full.png`
- Vision extraction of all financial data → `{TICKER}/tmp/screener_analysis.md`
- Downloads 5 most recent PPTs → `{TICKER}/presentation/`
- Downloads 5 most recent transcripts → `{TICKER}/concall/` (with `.txt` conversion)

### Step 2: Analyze PPTs (parallel with Step 3)

Invoke the **ppt-analyzer** skill — run its script on each downloaded PPT to extract content via vision model. Idempotent — skips if `.md` already exists.

```bash
source .venv/bin/activate
python .opencode/skills/ppt-analyzer/ppt_analyzer.py --pdf {TICKER}/presentation/PPT_May2026.pdf
```

### Step 3: Extract Credit Ratings (parallel with Step 2)

Invoke the **credit-rating-analyzer** skill — find rating links in the `screener_analysis.md` (documents → credit ratings section) and extract each one. Most CRISIL reports are HTML pages; use `--html`. Older reports may be PDFs; use `--pdf`.

### Step 4: Read All PPTs & Transcripts (Parallel Subagents)

**CRITICAL — Do NOT skip.** Vision-extracted `.md` files are lossy. Read every PPT `.md` and transcript `.txt` in full before writing the verdict.

Launch a `task` subagent per file, all in one message for parallelism. Each subagent reads the entire file and returns all equity-relevant data (financial figures, order book, segment mix, guidance, Q&A, risks). Skip files under 50 lines (error pages).

```bash
wc -l {TICKER}/presentation/PPT_*.md {TICKER}/concall/Transcript_*.txt
```

### Step 5: Compile Verdict

Synthesize ALL sources — `screener_analysis.md`, PPT subagent outputs, transcript subagent outputs, credit ratings — and write `verdict.md` in a dated folder covering:

- Company overview and industry positioning
- Financial analysis (from `screener_analysis.md` — all tables already extracted)
- Quarterly progression and trends
- Strategy, growth outlook, and management quality
- Risks including credit rating trajectory (from `credit_ratings/*.md`)
- Valuation context and peer comparison
- Key monitorables

**IMPORTANT — Units:** All screener.in data is in **Rs Crore**. PPT and concall reports often use Rs Mn — convert to Rs Cr before mixing sources (1 Cr = 10 Mn). Sanity-check all figures in the verdict against BV/share and other cross-references.

```bash
mkdir -p {TICKER}/$(date +%-d-%-B-%Y | tr '[:upper:]' '[:lower:]')
```

## Output Structure

```
TICKER/
├── presentation/                   # PPTs + vision-extracted .md (shared across dates)
│   ├── PPT_May2026.pdf
│   └── PPT_May2026.md
├── concall/                        # Transcript PDFs + .txt (shared across dates)
│   ├── Transcript_May2026.pdf
│   └── Transcript_May2026.txt
├── credit_ratings/                 # Rating reports .md (shared across dates)
├── tmp/                            # Intermediate artifacts (gitignored)
│   ├── screener_full.png
│   └── screener_analysis.md
└── 9-july-2026/                    # Analysis snapshot
    ├── screener_full.png           # copy of the full-page screenshot
    └── verdict.md                  # Final analysis summary
```

## Comparison with Old Workflow

Previously this skill used manually downloaded screener.in HTML snapshots (`screener.html` + `screener_files/`) and a static `download_docs.py`. That approach is deprecated. Use **screener-navigator** instead — it gives live data, handles login automatically, and produces both a screenshot and structured analysis via vision models.
