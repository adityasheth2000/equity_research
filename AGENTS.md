# AGENTS.md

## Git Configuration

Always use the personal GitHub account for pushing changes to this repository.

Work directly on the current checkout and branch for local changes. Do not create or switch to a separate git worktree for this repository. Keep all changes on the branch currently checked out.

**Remote:** `git@github.com-personal:adityasheth2000/equity_research.git`

The SSH alias `github.com-personal` is configured in `~/.ssh/config`:
```
Host github.com-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/personal-github
    IdentitiesOnly yes
```

## Repository Structure

```
equity_research/
├── .env                          # API keys (OPENROUTER_API_KEY, etc.)
├── .venv/                        # Python virtual environment
├── .agents/
│   └── skills/
│       ├── screener-navigator/   # Screener.in browser automation + downloads
│       │   ├── SKILL.md          # agent-browser navigation + download_docs.py usage
│       │   └── download_docs.py  # Downloads PPTs + transcripts + annual reports
│       │                         #   → TICKER/presentation/
│       │                         #   → TICKER/concall/
│       │                         #   → TICKER/annual_reports/
└── TICKER/
    ├── presentation/             # Investor PPTs (shared across dates)
    ├── concall/                  # Transcripts PDFs (shared across dates)
    ├── annual_reports/           # Annual report PDFs from BSE (shared across dates)
    ├── credit_ratings/           # Rating reports (shared across dates)
    ├── tmp/                      # Intermediate artifacts (gitignored)
    └── dated-folder/             # e.g., 9-september-2026
        ├── screener_full.png     # Screener.in full-page screenshot
        └── verdict.md            # Final analysis summary
```

## Stock Analysis Workflow

### Step 0: Setup

Extract the TICKER from the screener.in URL. The folder name must match the screener link symbol:

```
URL:  https://www.screener.in/company/GRAVITA/consolidated/
TICKER: GRAVITA
Folder: ./GRAVITA/
```

Create the folder structure and dated analysis folder:

```bash
mkdir -p GRAVITA/{presentation,concall,annual_reports,tmp}
mkdir -p GRAVITA/$(date -u +%-d-%-B-%Y | tr '[:upper:]' '[:lower:]')
```

### Step 1: Download Documents

This step must complete first (it unblocks all parallel subagents). Use `download_docs.py` to fetch PPTs, transcripts, and annual reports into the TICKER folder:

```bash
source .venv/bin/activate
python .agents/skills/screener-navigator/download_docs.py \
  --url "https://www.screener.in/company/{TICKER}/consolidated/" \
  --max 5
```

Refer to `.agents/skills/screener-navigator/SKILL.md` for full usage.

### Step 2: Parallel Analysis (run all simultaneously after Step 1)

**2a. Read PDF documents** — launch running agents/subagents directly for the PDFs in `TICKER/presentation/`, `TICKER/concall/`, and `TICKER/annual_reports/`. Do not invoke a PDF-analysis script or a separate multimodal skill. Give each agent the relevant PDF path and ask it to read the document directly, preserving page-level references and extracting the information needed for the final verdict:

- Presentations: financial data, segment breakdowns, guidance, capex plans, KPIs, and strategic commentary.
- Transcripts: management commentary on demand and margins, Q&A highlights, analyst concerns, guidance, risk flags, and competitive positioning.
- Annual reports: business overview, segment details, director's report, MD&A, corporate governance, auditor qualifications, risk factors, and financial-statement commentary.

**2b. Web Research** — search online for recent news, stock price movement, analyst ratings, and industry developments.

**2c. Screener Data & Competitor Analysis** — navigate screener.in via the **screener-navigator** skill to:
- Open the company page, log in, take a full-page screenshot → `TICKER/tmp/screener_full.png`
- Read and extract financial data from the screenshot (P&L, balance sheet, cash flows, ratios, shareholding, peers)
- Close browser

### Step 3: Synthesize Verdict

Once all parallel steps complete, write `TICKER/<dated-folder>/verdict.md`. Do not follow a rigid template — the model should decide what matters most for this specific company and present it clearly. Cover everything needed to understand the business, its financial position, strategic direction, and investment case in simple, accessible language. Assume the reader knows nothing about the industry. Use tables, comparisons, and data visualizations where helpful. Every claim must be traceable to a source document.

Skills provide specialized instructions and workflows for specific tasks.
Use the skill tool to load a skill when a task matches its description.
