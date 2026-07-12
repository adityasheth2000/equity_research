---
name: screener-navigator
description: Use whenever the user wants to navigate screener.in to extract financial data, quarterly results, profit & loss, balance sheet, cash flows, ratios, shareholding patterns, peer comparisons, concall links, credit ratings, or annual reports for a company. Trigger on "fetch screener data for...", "get financials from screener", "extract quarterly results", "download screener data", "screener snapshot for X", "export screener data", or any task requiring screener.in interaction via agent-browser.
allowed-tools: Bash(agent-browser:*), Bash(source .opencode/skills/screener-navigator/.env:*)
---

# screener-navigator

Automates navigation and data extraction from screener.in using agent-browser. Handles login, full-page screenshots, vision-based financial data extraction, and document downloads (PPTs, transcripts, credit ratings).

## Prerequisites

- `agent-browser` CLI installed (`npm i -g agent-browser && agent-browser install`)
- Repo-level `.venv` with dependencies installed (`requests`, `python-dotenv`, `beautifulsoup4`, `PyMuPDF`)
- Credentials in `.opencode/skills/screener-navigator/.env`
- `OPENROUTER_API_KEY` in repo `.env`

## Primary Workflow: Full Company Analysis

This is the end-to-end workflow for analyzing a company on screener.in. Steps 3 and 4 can run in parallel.

### Step 1: Open Company Page & Login

```bash
source .opencode/skills/screener-navigator/.env
agent-browser open "https://www.screener.in/company/{TICKER}/consolidated/"
agent-browser wait --load networkidle

# Login (click the "LOGIN" link in top nav)
agent-browser snapshot -i
agent-browser click @eX                    # link "LOGIN"
agent-browser wait --load networkidle
agent-browser snapshot -i
agent-browser fill @eX "$SCREENER_EMAIL"   # textbox "Email"
agent-browser fill @eY "$SCREENER_PASSWORD" # textbox "Password"
agent-browser click @eZ                    # button "LOGIN"
agent-browser wait --url "**/company/**"
agent-browser wait --load networkidle
```

### Step 2: Full-Page Screenshot

```bash
agent-browser screenshot --full {TICKER}/tmp/screener_full.png
```

The screenshot is saved to `{TICKER}/tmp/screener_full.png`. All intermediate artifacts go under the company's `tmp/` directory (gitignored).

### Step 3: Vision Analysis of Screenshot

```bash
source .venv/bin/activate
python .opencode/skills/screener-navigator/image_analyzer.py \
  --image {TICKER}/tmp/screener_full.png \
  --screener \
  --output {TICKER}/tmp/screener_analysis.md
```

This uses the OpenRouter vision model (`qwen/qwen3.5-flash-02-23`) to extract ALL financial data from the screenshot — quarterly results, annual P&L, balance sheet, cash flows, ratios, shareholding pattern, peer comparison, and documents listing. Output is a comprehensive markdown file.

For custom analysis of any image:

```bash
python .opencode/skills/screener-navigator/image_analyzer.py \
  --image path/to/image.png \
  --prompt "Your custom prompt here" \
  --output analysis.md
```

### Step 4: Download Documents (parallel with Step 3)

```bash
source .venv/bin/activate
python .opencode/skills/screener-navigator/download_docs.py \
  --url "https://www.screener.in/company/{TICKER}/consolidated/" \
  --max 5
```

Downloads the 5 most recent investor presentations to `{TICKER}/presentation/` and concall transcripts to `{TICKER}/concall/`. Transcript PDFs are auto-converted to `.txt`. Idempotent — skips existing files.

### Step 5: Close Browser

```bash
agent-browser close
```

## Output Structure After Full Workflow

```
TICKER/
├── presentation/                       # PPT PDFs downloaded from concalls
├── concall/                            # Transcript PDFs + .txt files
├── tmp/                                # Intermediate artifacts (gitignored)
│   ├── screener_full.png               # Full-page screenshot
│   └── screener_analysis.md            # Vision-extracted financial data
└── (later: dated analysis folders)
```

## Ad-Hoc Navigation Workflow

For interactive exploration of specific sections without screenshot + analysis:

### URL Conventions

```
https://www.screener.in/company/{TICKER}/consolidated/   # main company page
https://www.screener.in/login/                            # login page
```

### Snapshot & Navigate

```bash
agent-browser snapshot -i -u
```

The snapshot reveals all interactive elements. Key sections to identify:

| Section | Snapshot Marker |
|---------|----------------|
| **Peer Comparison** | `heading "Peer comparison"` |
| **Quarterly Results** | `heading "Quarterly Results"` |
| **Profit & Loss** | `heading "Profit & Loss"` |
| **Balance Sheet** | `heading "Balance Sheet"` |
| **Cash Flows** | `heading "Cash Flows"` |
| **Ratios** | `heading "Ratios"` |
| **Shareholding** | `heading "Shareholding Pattern"` |
| **Documents** | `heading "Documents"` |

### Navigate Between Tabs

```bash
agent-browser click @eX          # e.g., click "Profit & Loss"
agent-browser wait --load networkidle
agent-browser snapshot -i
```

Tab links: Chart, Analysis, Peers, Quarters, Profit & Loss, Balance Sheet, Cash Flow, Ratios, Investors, Documents.

### Extract Data

```bash
agent-browser read              # full page rendered text
agent-browser screenshot --full output.png   # full-page visual capture
```

## Navigation Reference

### Key Sections Deep Dive

**Quarterly Results** — 12+ quarters, expandable rows (Sales+, Expenses+, Other Income+, Net Profit+). Click the `+` buttons to expand/collapse.

**Profit & Loss (Annual)** — 10+ years. Key rows: Sales, Operating Profit, OPM %, Net Profit, EPS, Dividend Payout %. Bottom: Compounded Sales/Profit Growth, Stock Price CAGR, ROE.

**Balance Sheet (Annual)** — 10+ years. Key rows: Equity Capital, Reserves, Borrowings, Fixed Assets, Investments.

**Cash Flows (Annual)** — Operating/Investing/Financing activities, Free Cash Flow, CFO/OP ratio.

**Ratios (Annual)** — Debtor Days, Working Capital Days, ROCE %.

**Shareholding (Quarterly)** — Promoters, FIIs, DIIs, Government, Public % + No. of Shareholders.

**Insights (Login Required)** — Headcount, client metrics, revenue mix, order book, attrition, AI revenue, R&D spend.

**Documents** — Announcements, Annual reports, Credit ratings, Concalls (PPT/REC/Transcript links).

## Important Notes

- Always `source .opencode/skills/screener-navigator/.env` before using credentials.
- Re-snapshot after every navigation or page change (refs become stale).
- Use `wait --load networkidle` after tab switches or form submissions.
- The screenshot flag is `--full` (not `--fullpage`).
- Some rows have `+` suffix (e.g., "Sales+") meaning they are expandable clickable buttons.
- Avoid hardcoding credentials in commands; always use `$SCREENER_EMAIL` / `$SCREENER_PASSWORD`.
