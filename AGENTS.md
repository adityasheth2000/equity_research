# AGENTS.md

## Git Configuration

Always use the personal GitHub account for pushing changes to this repository.

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
├── .opencode/
│   └── skills/
│       ├── screener-navigator/   # Screener.in browser automation + downloads
│       │   ├── SKILL.md          # agent-browser navigation + download_docs.py usage
│       │   └── download_docs.py  # Downloads PPTs + transcripts + annual reports
│       │                         #   → TICKER/presentation/
│       │                         #   → TICKER/concall/
│       │                         #   → TICKER/annual_reports/
│       └── multimodal-subagent/  # PDF → OpenRouter multimodal analysis
│           ├── SKILL.md          # Usage instructions
│           └── pdf_analyze.py    # Sends PDF(s) to Gemini via OpenRouter with custom prompt
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

### Step 1: Navigate Screener.in & Download Documents

This step must complete first. Use the **screener-navigator** skill to:
- Open screener.in, log in, take full-page screenshot → `TICKER/tmp/screener_full.png`
- Download PPTs, transcripts, and annual reports via `download_docs.py`
- Close browser

Refer to `.opencode/skills/screener-navigator/SKILL.md` for exact agent-browser and download commands.

### Step 2: Parallel Analysis (run all simultaneously after Step 1)

**2a. Read Presentations** — launch task subagents per PPT file in `TICKER/presentation/`. Each subagent invokes the **multimodal-subagent** skill:

```bash
source .venv/bin/activate
python .opencode/skills/multimodal-subagent/pdf_analyze.py TICKER/presentation/PPT_May2026.pdf \
  -p "Extract all financial data, segment breakdowns, guidance, capex plans, KPIs, and strategic commentary. Be thorough." \
  -o TICKER/tmp/analysis_PPT_May2026.md
```

**2b. Read Transcripts** — launch task subagents per transcript in `TICKER/concall/`. Each subagent invokes the **multimodal-subagent** skill:

```bash
source .venv/bin/activate
python .opencode/skills/multimodal-subagent/pdf_analyze.py TICKER/concall/Transcript_May2026.pdf \
  -p "Extract management commentary on demand and margins, all Q&A highlights and analyst concerns, guidance, risk flags, and competitive positioning." \
  -o TICKER/tmp/analysis_Transcript_May2026.md
```

**2c. Read Annual Reports** — launch a task subagent for the latest annual report in `TICKER/annual_reports/`. Invoke the **multimodal-subagent** skill:

```bash
source .venv/bin/activate
python .opencode/skills/multimodal-subagent/pdf_analyze.py TICKER/annual_reports/AnnualReport_2026.pdf \
  -p "Extract business overview, segment details, director's report, MD&A, corporate governance, auditor qualifications, risk factors, and financial statement commentary." \
  -o TICKER/tmp/analysis_AnnualReport_2026.md
```

**2d. Web Research** — search online for recent news, stock price movement, analyst ratings, and industry developments.

**2e. Read Screener Screenshot** — read `TICKER/tmp/screener_full.png` to extract financial data (P&L, balance sheet, cash flows, ratios, shareholding, peers).

### Step 3: Synthesize Verdict

Once all parallel steps complete, write `TICKER/<dated-folder>/verdict.md`. Do not follow a rigid template — the model should decide what matters most for this specific company and present it clearly. Cover everything needed to understand the business, its financial position, strategic direction, and investment case in simple, accessible language. Assume the reader knows nothing about the industry. Use tables, comparisons, and data visualizations where helpful. Every claim must be traceable to a source document.

Skills provide specialized instructions and workflows for specific tasks.
Use the skill tool to load a skill when a task matches its description.