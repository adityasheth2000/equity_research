---
name: stock-analyzer
description: Use whenever the user wants to set up a full stock analysis workflow from a screener.in HTML snapshot. Handles downloading investor presentations and concall transcripts, running vision-based PPT analysis, and converting transcripts to text. Use for bootstrapping a new company analysis, setting up research artifacts, or when the user says "analyze this stock", "set up analysis for...", "download concalls", "gather documents".
---

# Stock Analyzer

Orchestrates a complete equity research workflow starting from a screener.in HTML snapshot.

PPTs and transcripts are stored at the **company level** (shared across analysis dates). Each dated folder contains only the screener snapshot and analysis outputs.

## Prerequisites

- Repo-level `.venv` with dependencies installed
- `OPENROUTER_API_KEY` in `.env` (for ppt-analyzer)
- `brew install poppler` (for ppt-analyzer)

## Full Workflow

### Step 1: Download Documents

```bash
source .venv/bin/activate

# Parse screener HTML — PPTs go to COMPANY/presentation/, transcripts to COMPANY/concall/
python .opencode/skills/stock-analyzer/download_docs.py \
  --html COMPANY/dated-folder/screener.html \
  --max 5

# Preview only (no download):
python .opencode/skills/stock-analyzer/download_docs.py \
  --html COMPANY/dated-folder/screener.html --skip-download
```

This parses the screener.in "Concalls" section and downloads:
- `COMPANY/presentation/PPT_MonYYYY.pdf` — investor presentations
- `COMPANY/concall/Transcript_MonYYYY.pdf` — concall transcripts

Transcripts are automatically converted to `.txt` via PyMuPDF. All steps are idempotent — existing files are skipped.

### Step 2: Analyze PPTs with Vision Model

```bash
# Run once per PPT — output .md lands alongside the PDF
python .opencode/skills/ppt-analyzer/ppt_analyzer.py \
  --pdf COMPANY/presentation/PPT_May2026.pdf

python .opencode/skills/ppt-analyzer/ppt_analyzer.py \
  --pdf COMPANY/presentation/PPT_Feb2026.pdf
```

Each PPT is processed through the vision model, producing a `.md` in `COMPANY/presentation/`. Already-processed PPTs are skipped (idempotent).

### Step 3: Analyze

At this point, three clean information sources are ready. **Read ALL information across the last 3-4 quarters before forming conclusions.** Work through each source systematically:

1. **`COMPANY/dated-folder/screener.html`** — financial snapshot (P&L, balance sheet, ratios, peers)
2. **`COMPANY/presentation/PPT_MonYYYY.md`** — vision-extracted presentation content (charts, tables, strategy)
3. **`COMPANY/concall/Transcript_MonYYYY.txt`** — management commentary and Q&A

**Read chronologically:**
- Start with `screener.html` — understand the financial trajectory, ratios, and peer positioning
- Read all `presentation/PPT_*.md` files chronologically — track how strategy, guidance, and metrics evolve
- Read all `concall/Transcript_*.txt` files chronologically — management tone, capex updates, margin commentary, risks flagged

Only after absorbing ALL sources, write a detailed `verdict.md` covering:
- **Company Overview** — business model, moats, competitive position
- **Financial Analysis** — revenue/PAT/EBITDA trends, margins, ROE/ROCE, balance sheet health, working capital
- **Quarterly Progression** — how key metrics and guidance evolved across quarters
- **Strategy & Growth** — capacity expansion, new products, geographic expansion, capex plans
- **Management Quality** — consistency of messaging, execution track record, capital allocation
- **Risks** — business, financial, and execution risks; any red flags across quarters
- **Valuation Context** — current multiples vs peers, growth-adjusted valuation
- **Key Monitorables** — what to watch in upcoming quarters

## Output Structure

```
COMPANY/
├── presentation/                   # Investor presentations (shared across dates)
│   ├── PPT_May2026.pdf
│   ├── PPT_May2026.md              # Vision-extracted content
│   ├── PPT_Feb2026.pdf
│   ├── PPT_Feb2026.md
│   └── ...
├── concall/                        # Concall transcripts (shared across dates)
│   ├── Transcript_May2026.pdf
│   ├── Transcript_May2026.txt
│   ├── Transcript_Feb2026.pdf
│   ├── Transcript_Feb2026.txt
│   └── ...
├── tmp/                            # Intermediate artifacts (gitignored)
└── 5-july-2026/                    # Analysis snapshot
    ├── screener.html
    ├── screener_files/
    └── verdict.md
```

## Naming Convention

- PPTs: `PPT_MonYYYY.pdf` → `PPT_May2026.pdf`
- PPT markdowns: `PPT_MonYYYY.md` → `PPT_May2026.md`
- Transcripts: `Transcript_MonYYYY.pdf` → `Transcript_May2026.pdf`
- Transcript texts: `Transcript_MonYYYY.txt` → `Transcript_May2026.txt`
- Duplicate months get `_2`, `_3` suffixes
- Missing transcripts are skipped gracefully
