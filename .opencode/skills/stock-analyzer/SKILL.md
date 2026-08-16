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

**IMPORTANT — Be thorough.** Do not skip or rush through any step. Do not hallucinate figures or fabricate data. Every number and claim in the verdict must be traceable to a source document. It is fine if the workflow takes a long time — accuracy and completeness come first.

**Tip:** Steps 2, 3, and 4 are independent and can run in parallel. Step 1 must complete first. Step 5 must run after Steps 2, 3, and 4 finish, and Step 6 must wait until Step 5 is complete.

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

### Step 2: Analyze PPTs (parallel with Steps 3 & 4)

Invoke the **ppt-analyzer** skill — run `pdf_vision_to_md.py` on each downloaded PPT to extract content via vision model. Requires `--start-page` and `--num-pages` (max 30 per run). Idempotent at page level — already-extracted pages are skipped.

```bash
source .venv/bin/activate
python .opencode/utils/pdf_vision_to_md.py \
  --pdf {TICKER}/presentation/PPT_May2026.pdf --start-page 1 --num-pages 30
```

### Step 3: Extract Credit Ratings (parallel with Steps 2 & 4)

Invoke the **credit-rating** skill — find rating links in the `screener_analysis.md` (documents → credit ratings section) and extract each one. Most CRISIL reports are HTML pages; use `html_text_to_md.py --preset credit-rating`. Older reports may be PDFs; use `pdf_vision_to_md.py --doc-type credit-rating`.

### Step 4: Web Research (parallel with Steps 2 & 3)

Use **tavily-research** skill — run `tvly research` twice for the company (uses `--model mini`):

```bash
source .venv/bin/activate

# 1. Latest company info, business, management, industry
tvly research "latest news, business overview, management outlook, and industry analysis for {COMPANY_NAME} {TICKER} India" --model mini --stream -o {TICKER}/tmp/tavily_company.md

# 2. Recent stock price movement and sentiment
tvly research "recent stock price movement, analyst ratings, and market sentiment for {COMPANY_NAME} {TICKER} India 2026" --model mini --stream -o {TICKER}/tmp/tavily_stock.md
```

### Step 5: Read All PPTs & Transcripts (Parallel Subagents)

**CRITICAL — Do NOT skip.** Vision-extracted `.md` files are lossy. Read every PPT `.md` and transcript `.txt` in full before writing the verdict.

Launch a `task` subagent per file, all in one message for parallelism. Each subagent reads the entire file and returns all equity-relevant data (financial figures, order book, segment mix, guidance, Q&A, risks). Skip files under 50 lines (error pages).

```bash
wc -l {TICKER}/presentation/PPT_*.md {TICKER}/concall/Transcript_*.txt
```

### Step 6: Compile Verdict

Synthesize ALL sources — `screener_analysis.md`, `tavily_company.md`, `tavily_stock.md`, PPT subagent outputs, transcript subagent outputs, credit ratings — and write `verdict.md` in a dated folder covering:

- **What the company does** — explain the business model in plain, simple language. Assume the reader knows nothing about the industry. What products/services do they sell? Who are their customers? How do they make money? This should be the very first section.
- Company overview and industry positioning
- **Key metrics to track** — the 5–8 most important KPIs for this company (e.g., order book, revenue visibility, margin profile, ROE/ROCE, working capital days, debt/equity, asset turns, industry-specific metrics like subscriber adds, loan growth, occupancy, etc.). Explain why each matters.
- **Management track record** — has management walked the talk? List major hits and misses on forward-looking statements (guidance vs actuals, capex delivered vs promised, targets achieved vs missed).
- Financial analysis 
- Quarterly progression and trends
- Strategy, growth outlook, and management quality
- **Thesis and anti-thesis** — a table with two columns: **Thesis (bull case)** and **Anti-thesis (bear case)**. These are the points to *track across the next 2–4 quarters* to judge whether the investment case is playing out. Rules:
  - Each thesis/anti-thesis point must be **falsifiable and specific** (e.g., "new plant ramps to 70% utilization by Q3FY27" — not "company will grow").
  - For **every** point, explicitly state **why it matters and its direct impact on the financials** — tie it to a concrete line item and direction (revenue growth, gross/EBITDA margin, ROE/ROCE, working capital, debt/equity, cash flow, EPS). Example: "Delay in capex → higher depreciation before revenue arrives → EBITDA margin dilution of ~X bps."
  - Structure each row as: the claim + the metric it moves + the direction and rough magnitude of the impact.
  - End with a **"What would change my mind"** line for each side — the single data point (quarterly result, KPI, macro indicator) that would invalidate that case.
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
│   ├── screener_analysis.md
│   ├── tavily_company.md
│   └── tavily_stock.md
└── 9-july-2026/                    # Analysis snapshot
    ├── screener_full.png           # copy of the full-page screenshot
    └── verdict.md                  # Final analysis summary
```

## Comparison with Old Workflow

Previously this skill used manually downloaded screener.in HTML snapshots (`screener.html` + `screener_files/`) and a static `download_docs.py`. That approach is deprecated. Use **screener-navigator** instead — it gives live data, handles login automatically, and produces both a screenshot and structured analysis via vision models.
