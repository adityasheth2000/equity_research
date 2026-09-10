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
    ├── broker_reports/           # Broker and analyst research reports
    ├── credit_ratings/           # Rating reports (shared across dates)
    ├── tmp/                      # Intermediate artifacts (gitignored)
    └── dated-folder/             # e.g., 9-september-2026
        ├── screener_full.png     # Screener.in full-page screenshot
        └── verdict.md            # Final analysis summary
```

## Stock Analysis Workflow

The AI agent acts as an expert equity researcher hunting for potential multibaggers. It must think independently, remain evidence-based, and assess both the probability and magnitude of outcomes. It should look beyond recent financial performance to identify durable competitive advantages, operating leverage, reinvestment opportunities, management quality, execution capability, and the conditions required for exceptional long-term compounding. It must also actively search for what could invalidate the thesis rather than writing a one-sided investment narrative.

### Step 0: Setup

Extract the TICKER from the screener.in URL. The folder name must match the screener link symbol:

```
URL:  https://www.screener.in/company/GRAVITA/consolidated/
TICKER: GRAVITA
Folder: ./GRAVITA/
```

Create the folder structure and dated analysis folder:

```bash
mkdir -p GRAVITA/{presentation,concall,annual_reports,broker_reports,tmp}
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

**2a. Read PDF documents** — launch running agents/subagents directly for every relevant PDF in `TICKER/presentation/`, `TICKER/concall/`, `TICKER/annual_reports/`, and `TICKER/broker_reports/`. Do not invoke a PDF-analysis script or a separate multimodal skill. Give each agent the relevant PDF path and ask it to read the document fully, decide for itself what is material to understanding the business and investment case, and report the key findings with page-level references. Agents should use their judgment rather than follow a fixed extraction checklist. Do not skip older documents when they provide historical context, reveal changes in management commentary, or help test whether current claims are consistent over time.

**2b. Dedicated Web Research** — launch a separate web-research subagent to investigate the company's recent external context. It should independently determine the most relevant developments, with particular emphasis on:

- Analyst and broker ratings, target-price changes, consensus expectations, upgrades/downgrades, and the reasoning behind them.
- Industry developments, including demand and supply trends, competitors, market structure, commodity or input-cost movements, and relevant tailwinds or headwinds.
- Government policy, regulation, budgets, incentives, trade measures, and other policy developments that could materially affect the company or its industry.
- Recent company news and stock-price movement, with dates, credible source links, and a clear distinction between reported facts and analytical inference.

**2c. Screener Data & Competitor Analysis** — navigate screener.in via the **screener-navigator** skill to:
- Open the company page, log in, take a full-page screenshot → `TICKER/tmp/screener_full.png`
- Read and extract financial data from the screenshot (P&L, balance sheet, cash flows, ratios, shareholding, peers)
- Close browser

### Step 3: Synthesize Verdict

Once all parallel steps complete, write `TICKER/<dated-folder>/verdict.md`. The verdict must be a comprehensive, evidence-backed investment assessment based on all available documents and research: annual reports, concall reports, investor presentations, broker reports, credit-rating reports, Screener data, and relevant web research. Read across documents rather than summarising them in isolation, reconcile conflicting claims, identify changes over time, and cite the underlying document or source for material claims.

The verdict should explain the business in accessible language and use the agent's judgment to decide which perspectives are most relevant to this particular company and investment case. The following are illustrative areas to consider, not a mandatory checklist:

- Financial quality: growth, margins, cash generation, return ratios, balance-sheet strength, working capital, capital allocation, dilution, and valuation.
- Strategic quality: market opportunity, competitive advantages, industry structure, reinvestment runway, scalability, operating leverage, and the company's ability to become substantially larger.
- Management and leadership: the quality and credibility of management discussion, leadership perspective, capital-allocation record, execution against prior promises, governance, incentives, and evidence of honest communication.
- Downside and failure modes: what can go wrong, the most material business and financial risks, weak points in the thesis, early warning indicators, bear-case scenarios, and what would permanently impair the investment.
- Multibagger potential: the specific drivers that could produce exceptional long-term returns, the addressable opportunity, required growth and profitability, reinvestment needs, valuation assumptions, time horizon, and key assumptions that must prove correct.
- Contradictions and open questions: disagreements between management, broker reports, financial statements, industry data, and market expectations; unresolved issues that require monitoring; and information that is unavailable or uncertain.

The agent may cover only a subset of these areas when others are immaterial, and should add any other perspectives revealed by the documents, industry, business model, competitive context, or valuation. Prioritise depth and relevance over exhaustive categorisation. Do not omit material evidence merely because it does not fit one of the illustrative areas.

Do not force a bullish conclusion. State clearly what the evidence supports, whether that is a potential multibagger, a more ordinary investment, avoidance, or watchlist status, and explain why. Separate facts, management claims, analyst opinions, and the agent's own inferences. Do not omit inconvenient evidence merely because it weakens the thesis. Use tables, comparisons, timelines, and data visualizations where they materially improve understanding, but do not follow a rigid template when a different structure better communicates the company-specific investment case.

Skills provide specialized instructions and workflows for specific tasks.
Use the skill tool to load a skill when a task matches its description.
