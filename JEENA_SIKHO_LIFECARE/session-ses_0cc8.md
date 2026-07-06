# JEENA_SIKHO_LIFECARE

**Session ID:** ses_0cc8185a0ffePHHd1sk39giM7n
**Created:** 7/5/2026, 11:45:54 PM
**Updated:** 7/6/2026, 11:47:52 PM

---

## User

Analyze JEENA_SIKHO_LIFECARE stock 

---

## Assistant (Build · DeepSeek V4 Pro · 3.2s)

_Thinking:_

The user wants me to analyze a stock called "JEENA_SIKHO_LIFECARE". Let me first load the stock-analyzer skill to understand how to set up the analysis workflow.

**Tool: skill**

**Input:**
```json
{
  "name": "stock-analyzer"
}
```

**Output:**
```
<skill_content name="stock-analyzer">
# Skill: stock-analyzer

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

Base directory for this skill: /Users/asheth/Documents/personal/equity_research/.opencode/skills/stock-analyzer
Relative paths in this skill (e.g., scripts/, reference/) are relative to this base directory.
Note: file list is sampled.

<skill_files>
<file>/Users/asheth/Documents/personal/equity_research/.opencode/skills/stock-analyzer/download_docs.py</file>
</skill_files>
</skill_content>
```

---

## Assistant (Build · DeepSeek V4 Pro · 2.8s)

_Thinking:_

The user wants to analyze JEENA_SIKHO_LIFECARE stock. I need to follow the stock-analyzer workflow. Let me first check if a screener.html exists for this company and what dated folders are available.

Let me set up the analysis. First, let me check what exists for this company.

**Tool: read**

**Input:**
```json
{
  "filePath": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE"
}
```

**Output:**
```
<path>/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE</path>
<type>directory</type>
<entries>
5-July-2026/

(1 entries)
</entries>
```

---

## Assistant (Build · DeepSeek V4 Pro · 2.4s)

_Thinking:_

There's a dated folder `5-July-2026`. Let me check what's inside it and whether there's a screener.html.

**Tool: read**

**Input:**
```json
{
  "filePath": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/5-July-2026"
}
```

**Output:**
```
<path>/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/5-July-2026</path>
<type>directory</type>
<entries>
Jeena Sikho Lifecare Ltd share price _ About Jeena Sikho _ Key Insights - Screener_files/
Jeena Sikho Lifecare Ltd share price _ About Jeena Sikho _ Key Insights - Screener.html

(2 entries)
</entries>
```

---

## Assistant (Build · DeepSeek V4 Pro · 4.0s)

_Thinking:_

The screener.html file is there but has a different naming convention than expected (`Jeena Sikho Lifecare Ltd share price _ About Jeena Sikho _ Key Insights - Screener.html`). Let me first run the download step to get PPTs and transcripts. I'll need to rename/move the screener.html or use it as-is. Let me just point the download script at this file.

Let me start with Step 1: Download documents.

Good — there's a screener.html file. Let me run the full workflow: download documents, then analyze PPTs.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Step 1: Download documents (PPTs & transcripts) from screener",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Step 2: Analyze PPTs with vision model",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Step 3: Read all sources and write verdict.md",
      "status": "pending",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Step 1: Download documents (PPTs & transcripts) from screener",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Step 2: Analyze PPTs with vision model",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Step 3: Read all sources and write verdict.md",
    "status": "pending",
    "priority": "high"
  }
]
```

---

## Assistant (Build · DeepSeek V4 Pro · 9.3s)

_Thinking:_

Let me run the download script to get documents.

**Tool: bash**

**Input:**
```json
{
  "command": "source .venv/bin/activate && python .opencode/skills/stock-analyzer/download_docs.py --html \"JEENA_SIKHO_LIFECARE/5-July-2026/Jeena Sikho Lifecare Ltd share price _ About Jeena Sikho _ Key Insights - Screener.html\" --max 5",
  "description": "Download PPTs and transcripts from screener.html",
  "timeout": 120000
}
```

**Output:**
```
HTML     : Jeena Sikho Lifecare Ltd share price _ About Jeena Sikho _ Key Insights - Screener.html
Company  : JEENA_SIKHO_LIFECARE
PPTs     : JEENA_SIKHO_LIFECARE/presentation/
Concalls : JEENA_SIKHO_LIFECARE/concall/
Max      : 5 recent quarters

Concalls found (14):
  Jun 2026      Transcript: ✓  PPT: ✓
  May 2026      Transcript: ✗  PPT: ✓
  Feb 2026      Transcript: ✓  PPT: ✓
  Nov 2025      Transcript: ✓  PPT: ✓
  Aug 2025      Transcript: ✓  PPT: ✓
  Aug 2025      Transcript: ✗  PPT: ✓
  Jul 2025      Transcript: ✗  PPT: ✗
  May 2025      Transcript: ✓  PPT: ✓
  Nov 2024      Transcript: ✓  PPT: ✓
  Nov 2024      Transcript: ✗  PPT: ✓
  May 2024      Transcript: ✓  PPT: ✓
  Feb 2024      Transcript: ✗  PPT: ✓
  Aug 2023      Transcript: ✗  PPT: ✓
  Aug 2023      Transcript: ✗  PPT: ✓

=== Downloading ===
  Jun 2026:
    PPT: downloading... -> presentation/PPT_Jun2026.pdf (12250 KB)
    Transcript: downloading... -> concall/Transcript_Jun2026.pdf (654 KB)

  May 2026:
    PPT: downloading... -> presentation/PPT_May2026.pdf (12222 KB)

  Feb 2026:
    PPT: downloading... -> presentation/PPT_Feb2026.pdf (7899 KB)
    Transcript: downloading... -> concall/Transcript_Feb2026.pdf (1101 KB)

  Nov 2025:
    PPT: downloading... -> presentation/PPT_Nov2025.pdf (7569 KB)
    Transcript: downloading... -> concall/Transcript_Nov2025.pdf (966 KB)

  Aug 2025:
    PPT: downloading... -> presentation/PPT_Aug2025.pdf (9575 KB)
    Transcript: downloading... -> concall/Transcript_Aug2025.pdf (1194 KB)


=== Converting Transcripts to Text ===
  Converting: Transcript_Jun2026.pdf... -> Transcript_Jun2026.txt (66539 chars)
  Converting: Transcript_Feb2026.pdf... -> Transcript_Feb2026.txt (73884 chars)
  Converting: Transcript_Nov2025.pdf... -> Transcript_Nov2025.txt (62749 chars)
  Converting: Transcript_Aug2025.pdf... -> Transcript_Aug2025.txt (88423 chars)

Done.

```

---

## Assistant (Build · DeepSeek V4 Pro · 3.7s)

_Thinking:_

Downloads are done. Now I have:
- PPTs: Jun 2026, May 2026, Feb 2026, Nov 2025, Aug 2025
- Transcripts: Jun 2026, Feb 2026, Nov 2025, Aug 2025

Now Step 2: Analyze PPTs with vision model. Let me run all of them. But first let me check if any already have .md files.

Downloads complete. Now let me analyze PPTs with the vision model.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "priority": "high",
      "content": "Step 1: Download documents (PPTs & transcripts) from screener",
      "status": "completed"
    },
    {
      "priority": "high",
      "content": "Step 2: Analyze PPTs with vision model",
      "status": "in_progress"
    },
    {
      "priority": "high",
      "content": "Step 3: Read all sources and write verdict.md",
      "status": "pending"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Step 1: Download documents (PPTs & transcripts) from screener",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Step 2: Analyze PPTs with vision model",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Step 3: Read all sources and write verdict.md",
    "status": "pending",
    "priority": "high"
  }
]
```

---

## Assistant (Build · DeepSeek V4 Pro · 3.3s)

_Thinking:_

Let me run all PPT analyses in parallel. Let me check which ones already have .md files first.

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/*.md",
  "path": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation"
}
```

**Output:**
```
No files found
```

---

## Assistant (Build · DeepSeek V4 Pro · 148.8s)

_Thinking:_

No existing .md files. Let me run them all. I'll run them in parallel since they're independent.

Running all 5 PPT analyses in parallel:

**Tool: bash**

**Input:**
```json
{
  "command": "source .venv/bin/activate && python .opencode/skills/ppt-analyzer/ppt_analyzer.py --pdf JEENA_SIKHO_LIFECARE/presentation/PPT_Jun2026.pdf",
  "description": "Analyze PPT_Jun2026",
  "timeout": 600000
}
```

**Output:**
```
PDF     : PPT_Jun2026.pdf
Dir     : /Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation
Model   : qwen/qwen3.5-flash-02-23
Parallel: 50

=== Phase 1: PDF → Images ===
  Saved: page_001.png
  Saved: page_002.png
  Saved: page_003.png
  Saved: page_004.png
  Saved: page_005.png
  Saved: page_006.png
  Saved: page_007.png
  Saved: page_008.png
  Saved: page_009.png
  Saved: page_010.png
  Saved: page_011.png
  Saved: page_012.png
  Saved: page_013.png
  Saved: page_014.png
  Saved: page_015.png
  Saved: page_016.png
  Saved: page_017.png
  Saved: page_018.png
  Saved: page_019.png
  Saved: page_020.png
  Saved: page_021.png
  Saved: page_022.png
  Saved: page_023.png
  Saved: page_024.png
  Saved: page_025.png
  Saved: page_026.png
  Saved: page_027.png
  Saved: page_028.png
  Saved: page_029.png
  Saved: page_030.png
  Saved: page_031.png
  Saved: page_032.png
  Saved: page_033.png
  Saved: page_034.png
  Saved: page_035.png
  Saved: page_036.png
  Saved: page_037.png
  Saved: page_038.png
  Saved: page_039.png
  Saved: page_040.png
  Saved: page_041.png
  Saved: page_042.png
  Saved: page_043.png
  Saved: page_044.png
  Saved: page_045.png
  Saved: page_046.png
  Saved: page_047.png
  Saved: page_048.png
  Saved: page_049.png
  Saved: page_050.png
  Saved: page_051.png
  Saved: page_052.png
  Saved: page_053.png
  Done: 53 images

=== Phase 2: Extract per page ===
  Processing 53 pages with 50 parallel workers...

  ERROR page 22: object of type 'NoneType' has no len()
  [1/53] page 22 -> FAILED
  [2/53] page 5 -> 20 chars
  [3/53] page 21 -> 20 chars
  [4/53] page 18 -> 20 chars
  [5/53] page 50 -> 20 chars
  ERROR page 24: object of type 'NoneType' has no len()
  [6/53] page 24 -> FAILED
  [7/53] page 20 -> 20 chars
  [8/53] page 10 -> 20 chars
  [9/53] page 27 -> 20 chars
  [10/53] page 14 -> 20 chars
  [11/53] page 12 -> 1337 chars
  [12/53] page 36 -> 20 chars
  [13/53] page 2 -> 20 chars
  [14/53] page 37 -> 1269 chars
  [15/53] page 30 -> 1269 chars
  [16/53] page 47 -> 1180 chars
  [17/53] page 49 -> 20 chars
  [18/53] page 39 -> 983 chars
  [19/53] page 19 -> 20 chars
  [20/53] page 53 -> 20 chars
  [21/53] page 16 -> 1005 chars
  [22/53] page 46 -> 946 chars
  [23/53] page 23 -> 20 chars
  [24/53] page 45 -> 1096 chars
  [25/53] page 38 -> 1315 chars
  [26/53] page 44 -> 648 chars
  [27/53] page 28 -> 1724 chars
  [28/53] page 6 -> 2308 chars
  [29/53] page 1 -> 20 chars
  [30/53] page 4 -> 20 chars
  [31/53] page 40 -> 1204 chars
  [32/53] page 8 -> 1948 chars
  [33/53] page 51 -> 745 chars
  [34/53] page 33 -> 1314 chars
  [35/53] page 29 -> 948 chars
  [36/53] page 41 -> 20 chars
  [37/53] page 11 -> 2270 chars
  [38/53] page 9 -> 2907 chars
  [39/53] page 13 -> 2122 chars
  [40/53] page 17 -> 1598 chars
  [41/53] page 42 -> 984 chars
  [42/53] page 52 -> 1083 chars
  [43/53] page 26 -> 20 chars
  [44/53] page 7 -> 2589 chars
  [45/53] page 3 -> 494 chars
  [46/53] page 31 -> 1192 chars
  [47/53] page 34 -> 2475 chars
  [48/53] page 35 -> 1131 chars
  [49/53] page 25 -> 20 chars
  [50/53] page 15 -> 1219 chars
  [51/53] page 43 -> 593 chars
  [52/53] page 32 -> 2910 chars
  [53/53] page 48 -> 1331 chars

=== Phase 3: Combine ===
  Combined 53 pages -> PPT_Jun2026.md

Done -> /Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Jun2026.md

```

---

## Assistant (Build · DeepSeek V4 Pro · 179.3s)

_Thinking:_

PPT_Jun2026 is done. Now let me run the remaining 4 in parallel.

**Tool: bash**

**Input:**
```json
{
  "command": "source .venv/bin/activate && python .opencode/skills/ppt-analyzer/ppt_analyzer.py --pdf JEENA_SIKHO_LIFECARE/presentation/PPT_May2026.pdf",
  "description": "Analyze PPT_May2026",
  "timeout": 600000
}
```

**Output:**
```
PDF     : PPT_May2026.pdf
Dir     : /Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation
Model   : qwen/qwen3.5-flash-02-23
Parallel: 50

=== Phase 1: PDF → Images ===
  Saved: page_001.png
  Saved: page_002.png
  Saved: page_003.png
  Saved: page_004.png
  Saved: page_005.png
  Saved: page_006.png
  Saved: page_007.png
  Saved: page_008.png
  Saved: page_009.png
  Saved: page_010.png
  Saved: page_011.png
  Saved: page_012.png
  Saved: page_013.png
  Saved: page_014.png
  Saved: page_015.png
  Saved: page_016.png
  Saved: page_017.png
  Saved: page_018.png
  Saved: page_019.png
  Saved: page_020.png
  Saved: page_021.png
  Saved: page_022.png
  Saved: page_023.png
  Saved: page_024.png
  Saved: page_025.png
  Saved: page_026.png
  Saved: page_027.png
  Saved: page_028.png
  Saved: page_029.png
  Saved: page_030.png
  Saved: page_031.png
  Saved: page_032.png
  Saved: page_033.png
  Saved: page_034.png
  Saved: page_035.png
  Saved: page_036.png
  Saved: page_037.png
  Saved: page_038.png
  Saved: page_039.png
  Saved: page_040.png
  Saved: page_041.png
  Saved: page_042.png
  Saved: page_043.png
  Saved: page_044.png
  Saved: page_045.png
  Saved: page_046.png
  Saved: page_047.png
  Saved: page_048.png
  Saved: page_049.png
  Saved: page_050.png
  Saved: page_051.png
  Saved: page_052.png
  Saved: page_053.png
  Saved: page_054.png
  Done: 54 images

=== Phase 2: Extract per page ===
  Processing 54 pages with 50 parallel workers...

  [1/54] page 48 -> 20 chars
  [2/54] page 10 -> 20 chars
  [3/54] page 46 -> 20 chars
  [4/54] page 5 -> 20 chars
  [5/54] page 11 -> 20 chars
  [6/54] page 2 -> 20 chars
  [7/54] page 32 -> 20 chars
  [8/54] page 23 -> 20 chars
  [9/54] page 20 -> 20 chars
  [10/54] page 16 -> 20 chars
  [11/54] page 4 -> 20 chars
  [12/54] page 7 -> 1339 chars
  [13/54] page 24 -> 1619 chars
  [14/54] page 35 -> 1092 chars
  [15/54] page 1 -> 20 chars
  [16/54] page 17 -> 20 chars
  [17/54] page 25 -> 1046 chars
  [18/54] page 47 -> 709 chars
  [19/54] page 19 -> 20 chars
  [20/54] page 8 -> 1374 chars
  [21/54] page 45 -> 20 chars
  [22/54] page 29 -> 1377 chars
  [23/54] page 40 -> 1055 chars
  [24/54] page 49 -> 1274 chars
  [25/54] page 36 -> 858 chars
  [26/54] page 12 -> 943 chars
  [27/54] page 44 -> 20 chars
  [28/54] page 42 -> 937 chars
  [29/54] page 41 -> 1083 chars
  [30/54] page 6 -> 1688 chars
  [31/54] page 34 -> 1195 chars
  [32/54] page 26 -> 1577 chars
  [33/54] page 15 -> 20 chars
  [34/54] page 3 -> 747 chars
  ERROR page 18: object of type 'NoneType' has no len()
  [35/54] page 18 -> FAILED
  [36/54] page 33 -> 1729 chars
  [37/54] page 9 -> 2442 chars
  [38/54] page 54 -> 20 chars
  [39/54] page 43 -> 1407 chars
  [40/54] page 50 -> 2821 chars
  [41/54] page 28 -> 2306 chars
  [42/54] page 22 -> 832 chars
  [43/54] page 53 -> 570 chars
  [44/54] page 27 -> 1510 chars
  [45/54] page 52 -> 1588 chars
  [46/54] page 51 -> 2528 chars
  [47/54] page 30 -> 2130 chars
  [48/54] page 31 -> 1315 chars
  [49/54] page 21 -> 20 chars
  [50/54] page 13 -> 2291 chars
  [51/54] page 14 -> 921 chars
  [52/54] page 37 -> 233 chars
  [53/54] page 38 -> 20 chars
  [54/54] page 39 -> 1226 chars

=== Phase 3: Combine ===
  Combined 54 pages -> PPT_May2026.md

Done -> /Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_May2026.md

```

---

## Assistant (Build · DeepSeek V4 Pro · 115.8s)

_Thinking:_

Good, 2 down. Let me do the remaining 3 in parallel.

**Tool: bash**

**Input:**
```json
{
  "command": "source .venv/bin/activate && python .opencode/skills/ppt-analyzer/ppt_analyzer.py --pdf JEENA_SIKHO_LIFECARE/presentation/PPT_Feb2026.pdf",
  "description": "Analyze PPT_Feb2026",
  "timeout": 600000
}
```

**Output:**
```
PDF     : PPT_Feb2026.pdf
Dir     : /Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation
Model   : qwen/qwen3.5-flash-02-23
Parallel: 50

=== Phase 1: PDF → Images ===
  Saved: page_001.png
  Saved: page_002.png
  Saved: page_003.png
  Saved: page_004.png
  Saved: page_005.png
  Saved: page_006.png
  Saved: page_007.png
  Saved: page_008.png
  Saved: page_009.png
  Saved: page_010.png
  Saved: page_011.png
  Saved: page_012.png
  Saved: page_013.png
  Saved: page_014.png
  Saved: page_015.png
  Saved: page_016.png
  Saved: page_017.png
  Saved: page_018.png
  Saved: page_019.png
  Saved: page_020.png
  Saved: page_021.png
  Saved: page_022.png
  Saved: page_023.png
  Saved: page_024.png
  Saved: page_025.png
  Saved: page_026.png
  Saved: page_027.png
  Saved: page_028.png
  Saved: page_029.png
  Saved: page_030.png
  Saved: page_031.png
  Saved: page_032.png
  Saved: page_033.png
  Saved: page_034.png
  Saved: page_035.png
  Saved: page_036.png
  Saved: page_037.png
  Saved: page_038.png
  Saved: page_039.png
  Saved: page_040.png
  Saved: page_041.png
  Saved: page_042.png
  Saved: page_043.png
  Saved: page_044.png
  Saved: page_045.png
  Saved: page_046.png
  Saved: page_047.png
  Saved: page_048.png
  Saved: page_049.png
  Saved: page_050.png
  Saved: page_051.png
  Saved: page_052.png
  Done: 52 images

=== Phase 2: Extract per page ===
  Processing 52 pages with 50 parallel workers...

  ERROR page 19: object of type 'NoneType' has no len()
  [1/52] page 19 -> FAILED
  [2/52] page 10 -> 20 chars
  [3/52] page 36 -> 20 chars
  [4/52] page 46 -> 20 chars
  [5/52] page 5 -> 20 chars
  [6/52] page 16 -> 20 chars
  [7/52] page 7 -> 1391 chars
  [8/52] page 15 -> 20 chars
  [9/52] page 31 -> 20 chars
  [10/52] page 20 -> 20 chars
  [11/52] page 17 -> 20 chars
  [12/52] page 8 -> 633 chars
  [13/52] page 43 -> 20 chars
  [14/52] page 11 -> 20 chars
  [15/52] page 44 -> 20 chars
  [16/52] page 4 -> 20 chars
  [17/52] page 22 -> 20 chars
  [18/52] page 25 -> 1304 chars
  [19/52] page 3 -> 369 chars
  [20/52] page 50 -> 701 chars
  [21/52] page 33 -> 680 chars
  [22/52] page 48 -> 1251 chars
  [23/52] page 24 -> 926 chars
  [24/52] page 49 -> 1254 chars
  [25/52] page 41 -> 1166 chars
  [26/52] page 28 -> 1453 chars
  [27/52] page 34 -> 848 chars
  [28/52] page 47 -> 1661 chars
  [29/52] page 39 -> 794 chars
  [30/52] page 18 -> 20 chars
  [31/52] page 23 -> 1183 chars
  [32/52] page 51 -> 606 chars
  [33/52] page 9 -> 1973 chars
  [34/52] page 6 -> 1442 chars
  [35/52] page 35 -> 908 chars
  [36/52] page 52 -> 20 chars
  [37/52] page 26 -> 1135 chars
  [38/52] page 45 -> 944 chars
  [39/52] page 40 -> 675 chars
  [40/52] page 42 -> 20 chars
  [41/52] page 2 -> 20 chars
  [42/52] page 12 -> 873 chars
  [43/52] page 21 -> 20 chars
  [44/52] page 30 -> 1178 chars
  [45/52] page 14 -> 20 chars
  [46/52] page 29 -> 2697 chars
  [47/52] page 38 -> 1283 chars
  [48/52] page 32 -> 1471 chars
  [49/52] page 13 -> 1564 chars
  [50/52] page 27 -> 2346 chars
  [51/52] page 1 -> 20 chars
  [52/52] page 37 -> 20 chars

=== Phase 3: Combine ===
  Combined 52 pages -> PPT_Feb2026.md

Done -> /Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Feb2026.md

```

---

## Assistant (Build · DeepSeek V4 Pro · 196.3s)

_Thinking:_

3 more to do.

**Tool: bash**

**Input:**
```json
{
  "command": "source .venv/bin/activate && python .opencode/skills/ppt-analyzer/ppt_analyzer.py --pdf JEENA_SIKHO_LIFECARE/presentation/PPT_Nov2025.pdf",
  "description": "Analyze PPT_Nov2025",
  "timeout": 600000
}
```

**Output:**
```
PDF     : PPT_Nov2025.pdf
Dir     : /Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation
Model   : qwen/qwen3.5-flash-02-23
Parallel: 50

=== Phase 1: PDF → Images ===
  Saved: page_001.png
  Saved: page_002.png
  Saved: page_003.png
  Saved: page_004.png
  Saved: page_005.png
  Saved: page_006.png
  Saved: page_007.png
  Saved: page_008.png
  Saved: page_009.png
  Saved: page_010.png
  Saved: page_011.png
  Saved: page_012.png
  Saved: page_013.png
  Saved: page_014.png
  Saved: page_015.png
  Saved: page_016.png
  Saved: page_017.png
  Saved: page_018.png
  Saved: page_019.png
  Saved: page_020.png
  Saved: page_021.png
  Saved: page_022.png
  Saved: page_023.png
  Saved: page_024.png
  Saved: page_025.png
  Saved: page_026.png
  Saved: page_027.png
  Saved: page_028.png
  Saved: page_029.png
  Saved: page_030.png
  Saved: page_031.png
  Saved: page_032.png
  Saved: page_033.png
  Saved: page_034.png
  Saved: page_035.png
  Saved: page_036.png
  Saved: page_037.png
  Saved: page_038.png
  Saved: page_039.png
  Saved: page_040.png
  Saved: page_041.png
  Saved: page_042.png
  Saved: page_043.png
  Saved: page_044.png
  Saved: page_045.png
  Saved: page_046.png
  Saved: page_047.png
  Saved: page_048.png
  Done: 48 images

=== Phase 2: Extract per page ===
  Processing 48 pages with 50 parallel workers...

  [1/48] page 42 -> 20 chars
  [2/48] page 10 -> 20 chars
  [3/48] page 5 -> 20 chars
  [4/48] page 17 -> 20 chars
  [5/48] page 39 -> 20 chars
  [6/48] page 11 -> 20 chars
  [7/48] page 40 -> 20 chars
  [8/48] page 6 -> 1223 chars
  [9/48] page 48 -> 20 chars
  [10/48] page 32 -> 20 chars
  [11/48] page 8 -> 1200 chars
  [12/48] page 47 -> 675 chars
  [13/48] page 36 -> 799 chars
  [14/48] page 4 -> 20 chars
  [15/48] page 26 -> 20 chars
  [16/48] page 7 -> 1181 chars
  [17/48] page 23 -> 1150 chars
  [18/48] page 46 -> 1771 chars
  [19/48] page 45 -> 1183 chars
  [20/48] page 37 -> 779 chars
  [21/48] page 18 -> 1451 chars
  [22/48] page 38 -> 987 chars
  [23/48] page 19 -> 1033 chars
  [24/48] page 20 -> 1281 chars
  [25/48] page 41 -> 881 chars
  [26/48] page 43 -> 1600 chars
  [27/48] page 3 -> 626 chars
  [28/48] page 44 -> 1332 chars
  [29/48] page 16 -> 20 chars
  [30/48] page 28 -> 1404 chars
  [31/48] page 9 -> 2439 chars
  [32/48] page 27 -> 1831 chars
  [33/48] page 35 -> 721 chars
  [34/48] page 21 -> 1162 chars
  [35/48] page 12 -> 856 chars
  [36/48] page 29 -> 1328 chars
  [37/48] page 22 -> 2284 chars
  [38/48] page 25 -> 1419 chars
  [39/48] page 34 -> 20 chars
  [40/48] page 13 -> 1249 chars
  [41/48] page 24 -> 2430 chars
  [42/48] page 30 -> 3011 chars
  [43/48] page 14 -> 1096 chars
  [44/48] page 1 -> 20 chars
  [45/48] page 31 -> 1983 chars
  [46/48] page 2 -> 533 chars
  [47/48] page 33 -> 4219 chars
  [48/48] page 15 -> 593 chars

=== Phase 3: Combine ===
  Combined 48 pages -> PPT_Nov2025.md

Done -> /Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Nov2025.md

```

---

## Assistant (Build · DeepSeek V4 Pro · 229.2s)

_Thinking:_

One more left.

**Tool: bash**

**Input:**
```json
{
  "command": "source .venv/bin/activate && python .opencode/skills/ppt-analyzer/ppt_analyzer.py --pdf JEENA_SIKHO_LIFECARE/presentation/PPT_Aug2025.pdf",
  "description": "Analyze PPT_Aug2025",
  "timeout": 600000
}
```

**Output:**
```
PDF     : PPT_Aug2025.pdf
Dir     : /Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation
Model   : qwen/qwen3.5-flash-02-23
Parallel: 50

=== Phase 1: PDF → Images ===
  Saved: page_001.png
  Saved: page_002.png
  Saved: page_003.png
  Saved: page_004.png
  Saved: page_005.png
  Saved: page_006.png
  Saved: page_007.png
  Saved: page_008.png
  Saved: page_009.png
  Saved: page_010.png
  Saved: page_011.png
  Saved: page_012.png
  Saved: page_013.png
  Saved: page_014.png
  Saved: page_015.png
  Saved: page_016.png
  Saved: page_017.png
  Saved: page_018.png
  Saved: page_019.png
  Saved: page_020.png
  Saved: page_021.png
  Saved: page_022.png
  Saved: page_023.png
  Saved: page_024.png
  Saved: page_025.png
  Saved: page_026.png
  Saved: page_027.png
  Saved: page_028.png
  Saved: page_029.png
  Saved: page_030.png
  Saved: page_031.png
  Saved: page_032.png
  Saved: page_033.png
  Saved: page_034.png
  Saved: page_035.png
  Saved: page_036.png
  Saved: page_037.png
  Saved: page_038.png
  Saved: page_039.png
  Saved: page_040.png
  Saved: page_041.png
  Saved: page_042.png
  Saved: page_043.png
  Saved: page_044.png
  Saved: page_045.png
  Saved: page_046.png
  Done: 46 images

=== Phase 2: Extract per page ===
  Processing 46 pages with 50 parallel workers...

  [1/46] page 10 -> 20 chars
  [2/46] page 46 -> 20 chars
  [3/46] page 26 -> 20 chars
  [4/46] page 37 -> 20 chars
  [5/46] page 14 -> 20 chars
  [6/46] page 5 -> 20 chars
  [7/46] page 40 -> 20 chars
  [8/46] page 4 -> 20 chars
  [9/46] page 11 -> 20 chars
  [10/46] page 38 -> 20 chars
  [11/46] page 45 -> 670 chars
  [12/46] page 17 -> 20 chars
  [13/46] page 44 -> 1462 chars
  [14/46] page 3 -> 349 chars
  [15/46] page 32 -> 324 chars
  [16/46] page 8 -> 1205 chars
  [17/46] page 34 -> 822 chars
  [18/46] page 42 -> 1721 chars
  [19/46] page 7 -> 1434 chars
  [20/46] page 35 -> 707 chars
  [21/46] page 23 -> 1187 chars
  [22/46] page 18 -> 1599 chars
  [23/46] page 19 -> 925 chars
  [24/46] page 41 -> 1505 chars
  [25/46] page 20 -> 1131 chars
  [26/46] page 28 -> 1695 chars
  [27/46] page 36 -> 1339 chars
  [28/46] page 6 -> 1759 chars
  [29/46] page 2 -> 20 chars
  [30/46] page 27 -> 1557 chars
  [31/46] page 12 -> 1367 chars
  [32/46] page 29 -> 1217 chars
  [33/46] page 16 -> 911 chars
  [34/46] page 9 -> 1664 chars
  [35/46] page 43 -> 2512 chars
  [36/46] page 13 -> 1347 chars
  [37/46] page 21 -> 1440 chars
  [38/46] page 33 -> 693 chars
  [39/46] page 1 -> 20 chars
  [40/46] page 25 -> 1326 chars
  [41/46] page 39 -> 1317 chars
  [42/46] page 22 -> 1844 chars
  [43/46] page 24 -> 2774 chars
  [44/46] page 15 -> 20 chars
  [45/46] page 30 -> 1873 chars
  [46/46] page 31 -> 3826 chars

=== Phase 3: Combine ===
  Combined 46 pages -> PPT_Aug2025.md

Done -> /Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Aug2025.md

```

---

## Assistant (Build · DeepSeek V4 Pro · 7.0s)

_Thinking:_

All 5 PPTs analyzed. Now I need to read all sources and write the verdict. Let me read them all now. I'll read the screener.html and all the PPT .md files and transcript .txt files. Let me start reading everything in parallel since I need to process a lot of sources.

Let me read all the key sources:
1. screener.html
2. PPT_Jun2026.md, PPT_May2026.md, PPT_Feb2026.md, PPT_Nov2025.md, PPT_Aug2025.md
3. Transcript_Jun2026.txt, Transcript_Feb2026.txt, Transcript_Nov2025.txt, Transcript_Aug2025.txt

That's a lot of files. Let me use task agents to read and summarize them in parallel. I'll use multiple agents to process different types of sources.

All PPTs analyzed. Now Step 3 — reading all sources to write the verdict.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Step 1: Download documents (PPTs & transcripts) from screener",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Step 2: Analyze PPTs with vision model",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Step 3: Read all sources and write verdict.md",
      "priority": "high",
      "status": "in_progress"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Step 1: Download documents (PPTs & transcripts) from screener",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Step 2: Analyze PPTs with vision model",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Step 3: Read all sources and write verdict.md",
    "status": "in_progress",
    "priority": "high"
  }
]
```

---

## Assistant (Build · DeepSeek V4 Pro · 91.4s)

_Thinking:_

Let me read all the source materials. I'll use task agents to read and summarize the PPTs and transcripts in parallel since they're independent.

Let me read all sources in parallel using agents for efficiency:

**Tool: task**

**Input:**
```json
{
  "description": "Read screener.html summary",
  "prompt": "Read the file at \"/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/5-July-2026/Jeena Sikho Lifecare Ltd share price _ About Jeena Sikho _ Key Insights - Screener.html\". This is a screener.in HTML snapshot for Jeena Sikho Lifecare Ltd. \n\nExtract ALL the numbers and data from it — this is critical for financial analysis. Specifically find and return:\n1. P&L statement (revenue, EBITDA, PAT, margins for last 5-7 years and quarters)\n2. Balance sheet (equity, debt, reserves, fixed assets, WC, cash)\n3. Cash flow (OCF, capex, FCF)\n4. Ratios (ROE, ROCE, P/E, P/B, debt/equity, working capital days)\n5. Shareholding pattern\n6. Peer comparison table if present\n7. Any quarterly data tables\n\nReturn all the data in a clean structured format. Include actual numbers, not just descriptions. Don't summarize — return the full data.",
  "subagent_type": "general"
}
```

**Output:**
```
<task id="ses_0cc739f08ffe7l7NpU1ff9xKKl" state="completed">
<task_result>
Now I have all sections. Here is the complete extracted data:

---

# JEENA SIKHO LIFECARE LTD — Screener.in Data (as of ~July 5, 2026)

## KEY METRICS (Top Bar)
| Metric | Value |
|---|---|
| Market Cap | ₹7,160 Cr |
| Current Price | ₹576 |
| High / Low | ₹850 / ₹492 |
| Stock P/E | 32.2 |
| Book Value | ₹37.6 |
| Dividend Yield | 0.19% |
| ROCE | 70.7% |
| ROE | 60.0% |
| Face Value | ₹2.00 |
| Price to Book | 15.3 |
| ROE 3Yr | 49.6% |
| ROE 5Yr | 48.4% |
| ROCE 3Yr | 59.6% |
| ROCE 5Yr | 54.1% |
| Return on Assets | 44.4% |
| ROA 3Yr | 37.7% |
| ROA 5Yr | 32.8% |
| Quick Ratio | 3.00 |
| Current Ratio | 3.19 |
| Promoter Holding | 63.6% |
| Sales Growth 5Yr | 42.6% |
| Profit Var 3Yrs | 88.2% |
| Profit Var 5Yrs | 84.5% |
| Sales Growth 3Yrs | 57.8% |
| Debt/Equity | 0.27 |
| Pledged % | 0.00% |
| Int Coverage | 24.2 |
| PAT | ₹222 Cr |
| EV/EBITDA | 20.0 |
| EPS Growth 3Yrs | 88.2% |
| EPS Growth 5Yrs | -28.3% |

---

## PROFIT & LOSS (Annual, Standalone, Rs. Crores)

| Line Item | Mar 2019 | Mar 2020 | Mar 2021 | Mar 2022 | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|---|---|---|---|
| Sales | 106 | 94 | 136 | 146 | 204 | 324 | 469 | 801 |
| Expenses | 95 | 84 | 119 | 128 | 158 | 231 | 344 | 452 |
| **Operating Profit** | **11** | **11** | **17** | **18** | **46** | **93** | **125** | **350** |
| OPM % | 10% | 11% | 13% | 12% | 23% | 29% | 27% | 44% |
| Other Income | 0 | 1 | 1 | 1 | 2 | 6 | 6 | 9 |
| Interest | 1 | 2 | 1 | 1 | 1 | 0 | 1 | 13 |
| Depreciation | 1 | 2 | 2 | 3 | 3 | 5 | 9 | 48 |
| **Profit before tax** | **8** | **8** | **14** | **15** | **45** | **94** | **122** | **298** |
| Tax % | 28% | 26% | 27% | 26% | 24% | 26% | 26% | 25% |
| **Net Profit** | **6** | **6** | **10** | **11** | **34** | **69** | **91** | **222** |
| EPS (Rs.) | 66.67 | 63.67 | 93.55 | 1.24 | 2.71 | 5.57 | 7.30 | 17.87 |
| Dividend Payout % | 0% | 0% | 0% | 0% | 8% | 17% | 15% | 25% |

### Compounded Growth (P&L footer)
- **Sales CAGR:** 5Yr: 43%, 3Yr: 58%, TTM: 71%
- **Profit CAGR:** 5Yr: 85%, 3Yr: 88%, TTM: 152%
- **Stock Price CAGR:** 3Yr: 115%, 1Yr: 10%
- **ROE:** 5Yr: 48%, 3Yr: 50%, Last Year: 60%

---

## QUARTERLY RESULTS (Standalone, Rs. Crores)

| Line Item | Jun 2024 | Sep 2024 | Dec 2024 | Mar 2025 | Jun 2025 | Sep 2025 | Dec 2025 | Mar 2026 |
|---|---|---|---|---|---|---|---|---|
| Sales | 100 | 114 | 116 | 139 | 174 | 190 | 222 | 216 |
| Expenses | 75 | 74 | 86 | 93 | 96 | 98 | 121 | 138 |
| **Operating Profit** | **25** | **40** | **30** | **46** | **79** | **92** | **101** | **78** |
| OPM % | 25% | 35% | 26% | 33% | 45% | 48% | 45% | 36% |
| Other Income | 3 | 3 | 0 | 0 | 1 | 1 | 3 | 4 |
| Interest | 1 | 2 | 4 | 3 | 2 | 4 | 3 | 4 |
| Depreciation | 5 | 6 | 8 | 9 | 10 | 10 | 11 | 16 |
| **Profit before tax** | **21** | **35** | **18** | **34** | **69** | **79** | **89** | **62** |
| Tax % | 23% | 25% | 26% | 25% | 25% | 25% | 25% | 26% |
| **Net Profit** | **16** | **27** | **13** | **25** | **51** | **59** | **67** | **45** |
| EPS (Rs.) | 1.30 | 2.14 | 1.06 | 2.04 | 4.13 | 4.73 | 5.37 | 3.65 |

---

## BALANCE SHEET (Standalone, Rs. Crores)

| Line Item | Mar 2019 | Mar 2020 | Mar 2021 | Mar 2022 | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|---|---|---|---|
| **LIABILITIES** | | | | | | | | |
| Equity Capital | 0.10 | 0.10 | 0.10 | 10 | 14 | 25 | 25 | 25 |
| Reserves | 8 | 14 | 24 | 26 | 112 | 167 | 248 | 443 |
| Borrowings | 16 | 12 | 12 | 7 | 1 | 1 | 11 | 127 |
| Other Liabilities | 12 | 12 | 13 | 18 | 24 | 28 | 45 | 78 |
| **Total Liabilities** | **36** | **38** | **49** | **62** | **151** | **221** | **328** | **673** |
| | | | | | | | | |
| **ASSETS** | | | | | | | | |
| Fixed Assets | 13 | 17 | 23 | 28 | 60 | 67 | 153 | 307 |
| CWIP | 0 | 0 | 0 | 5 | 1 | 4 | 13 | 2 |
| Investments | 0 | 0 | 0 | 0 | 5 | 4 | 4 | 95 |
| Other Assets | 23 | 21 | 26 | 28 | 86 | 146 | 159 | 269 |
| **Total Assets** | **36** | **38** | **49** | **62** | **151** | **221** | **328** | **673** |

> Net Worth (Equity + Reserves): 8 → 14 → 24 → 36 → 126 → 192 → 273 → 468 Cr

---

## CASH FLOWS (Standalone, Rs. Crores)

| Line Item | Mar 2019 | Mar 2020 | Mar 2021 | Mar 2022 | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|---|---|---|---|
| Cash from Operating Activity | 1 | 12 | 18 | 17 | 17 | 37 | 69 | 262 |
| Cash from Investing Activity | -11 | -6 | -8 | -20 | -57 | -18 | -70 | -211 |
| Cash from Financing Activity | 7 | -5 | -2 | -5 | 48 | -3 | -1 | -59 |
| **Net Cash Flow** | **-2** | **1** | **8** | **-7** | **8** | **15** | **-2** | **-8** |
| **Free Cash Flow** | **-10** | **6** | **9** | **-1** | **-13** | **23** | **-40** | **231** |
| CFO/OP | 35% | 130% | 125% | 118% | 55% | 66% | 81% | 96% |

---

## RATIOS (Annual)

| Ratio | Mar 2019 | Mar 2020 | Mar 2021 | Mar 2022 | Mar 2023 | Mar 2024 | Mar 2025 | Mar 2026 |
|---|---|---|---|---|---|---|---|---|
| Debtor Days | 15 | 17 | 9 | 22 | 40 | 46 | 76 | 32 |
| Inventory Days | 204 | 315 | 208 | 136 | 87 | 121 | 135 | 80 |
| Days Payable | 125 | 168 | 73 | 109 | 129 | 75 | 111 | 86 |
| Cash Conversion Cycle | 94 | 163 | 143 | 49 | -2 | 92 | 100 | 26 |
| Working Capital Days | -16 | -15 | -19 | -11 | 29 | 58 | 55 | 54 |
| ROCE % | — | 38% | 50% | 39% | 53% | 58% | 50% | 71% |

---

## PEER COMPARISON (Wellness Industry)

| # | Company | CMP (Rs.) | % Fall 52H | Mkt Cap (Cr) | P/E | CMP/BV | ROE % | ROE 3Yr | ROE 5Yr | EV/EBITDA | Payout % | Avg Div 3Yr | Debt/Eq | Quick Rat | Profit Var 3Yr | Profit Var 5Yr | Sales Var 3Yr | Sales Var 5Yr | ROCE 3Yr | ROCE 5Yr | Int Coverage | ROA 12M | BV Growth 3Yr | FCF (Cr) | FCF 3Yr | FCF 5Yr | 1D % | 1Wk % | 1M % | 6M % | 1Yr % | 3Yr % | 5Yr % |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Jeena Sikho** | 576.05 | 32.23 | 7160.34 | 32.23 | 15.32 | 60.01 | 49.65 | 48.36 | 20.04 | 25.18 | 19.13 | 0.27 | 3.00 | 88.18 | 84.51 | 57.83 | 42.62 | 59.64 | 54.09 | 24.22 | 44.37 | 3.72 | 230.52 | 213.38 | 199.77 | 0.29 | -4.35 | -8.54 | -14.58 | 9.65 | 114.55 | — |
| 2 | Kaya Ltd | 245.72 | 49.64 | 373.19 | — | — | — | — | — | -44.22 | 0.00 | 0.00 | — | 0.30 | 6.08 | — | -16.10 | -4.15 | -36.71 | -35.31 | -1.66 | -36.81 | 1.27 | 84.52 | -20.02 | -26.69 | 27.46 | 1.70 | -0.49 | -0.94 | -36.76 | -43.28 | -9.72 | -6.44 |
| 3 | Lloyds Luxuries | 74.40 | 26.70 | 179.56 | — | 5.33 | -4.31 | -9.26 | -8.39 | 134.84 | 0.00 | 0.00 | 0.00 | 0.92 | 14.32 | 6.22 | 21.67 | 27.38 | -8.85 | -6.02 | — | -3.72 | 0.46 | — | 0.00 | -17.75 | -20.91 | 3.62 | 2.55 | -20.13 | 11.04 | -25.64 | 3.30 | — |
| **Median (3 Co.)** | 245.72 | 32.23 | 373.19 | 32.23 | 10.32 | 27.85 | 20.20 | 19.98 | 20.04 | 0.00 | 0.00 | 0.14 | 0.92 | 14.32 | 45.37 | 21.67 | 27.38 | -8.85 | -6.02 | 11.28 | -3.72 | 1.27 | 84.52 | 0.00 | -17.75 | 27.46 | 1.70 | -0.49 | -8.54 | -14.58 | -25.64 | 3.30 | -6.44 |

---

## SHAREHOLDING PATTERN (Quarterly, %)

| Period | Promoters | FIIs | DIIs | Public | No. of Shareholders |
|---|---|---|---|---|---|
| Apr 2022 | 65.89 | 0.00 | 0.00 | 34.11 | 1,951 |
| Sep 2022 | 65.89 | 0.00 | 0.00 | 34.11 | 834 |
| Mar 2023 | 66.20 | 0.00 | 0.00 | 33.80 | 663 |
| Sep 2023 | 67.91 | 2.00 | 0.04 | 30.05 | 815 |
| Nov 2023 | 67.91 | 1.79 | 0.00 | 30.30 | 1,107 |
| Mar 2024 | 67.91 | 0.26 | 0.00 | 31.83 | 2,721 |
| Sep 2024 | 65.84 | 4.05 | 0.07 | 30.04 | 3,423 |
| Mar 2025 | 63.53 | 5.95 | 0.17 | 30.34 | 5,967 |
| Jun 2025 | 63.53 | 5.91 | 0.18 | 30.38 | 6,603 |
| Sep 2025 | 63.61 | 6.59 | 0.15 | 29.65 | 16,362 |
| Dec 2025 | 63.62 | 6.31 | 0.11 | 29.97 | 22,181 |
| Mar 2026 | 63.62 | 6.17 | 0.46 | 29.77 | 25,905 |

### Shareholding Yearly
| Period | Promoters | FIIs | DIIs | Public | Shareholders |
|---|---|---|---|---|---|
| Mar 2023 | 66.20% | 0.00% | 0.00% | 33.80% | 663 |
| Mar 2024 | 67.91% | 0.26% | 0.00% | 31.83% | 2,721 |
| Mar 2025 | 63.53% | 5.95% | 0.17% | 30.34% | 5,967 |
| Mar 2026 | 63.62% | 6.17% | 0.46% | 29.77% | 25,905 |

> Sector: Consumer Discretionary → Consumer Services → Leisure Services → Wellness  
> Part of: Nifty Microcap 250, Nifty Total Market, Nifty Smallcap 500

---

### Key Observations:
- **FY26 Revenue:** ₹801 Cr (up 71% YoY); **PAT:** ₹222 Cr (up 144% YoY); **OPM:** 43.6%
- **FY26 FCF:** ₹231 Cr (turned strongly positive after -₹40 Cr in FY25)
- **Q4 FY26 (Mar 2026):** Sequential decline — Sales ₹216 Cr vs ₹222 Cr in Q3, PAT ₹45 Cr vs ₹67 Cr
- **Balance Sheet:** Net Worth ₹468 Cr, Borrowings surged to ₹127 Cr (from ₹11 Cr), Investments jumped to ₹95 Cr
- **Debt/Equity:** 0.27 (moderate)
- **ROCE:** 70.7%, **ROE:** 60% — strong profitability
- **Shareholding:** Promoters stable at ~63.6%, FII up from 0% to 6.17%, shareholders surged from 663 to 25,905
- **Peers:** Only Jeena Sikho profitable in peer group; Kaya and Lloyds Luxuries both loss-making
</task_result>
</task>
```

---

## Assistant (Build · DeepSeek V4 Pro · 99.2s)

_Thinking:_

Excellent. Now let me read the PPT markdowns and transcripts in parallel. I'll use multiple task agents.

Now reading PPTs and transcripts in parallel:

**Tool: task**

**Input:**
```json
{
  "description": "Read PPT markdown files",
  "prompt": "Read the following 5 PPT markdown files for Jeena Sikho Lifecare. These are vision-extracted content from investor presentations. Read ALL of them chronologically (oldest first):\n\n1. \"/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Aug2025.md\"\n2. \"/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Nov2025.md\"\n3. \"/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Feb2026.md\"\n4. \"/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_May2026.md\"\n5. \"/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Jun2026.md\"\n\nFor each PPT, extract and return ALL data in a structured way:\n- Business model description, competitive advantages\n- Key financial metrics (revenue, EBITDA, PAT, margins, guidance)\n- Growth strategy (capacity expansion, new centers, new services)\n- Capex plans, ROI targets\n- Geographic spread, center count\n- Any specific metrics tracked (ARPU, patient count, etc.)\n- Any changes in messaging or strategy across the quarters\n\nTrack how numbers and guidance evolve across quarters. Return the full comprehensive data.",
  "subagent_type": "general"
}
```

**Output:**
```
<task id="ses_0cc7237e5ffe26svYdu2VhzVfh" state="completed">
<task_result>
# Jeena Sikho Lifecare — Comprehensive PPT Analysis Across 5 Quarters

---

## 1. PPT_Aug2025 (Q1FY26 — August 2025)

### Business Model & Competitive Advantages
- **Dual-vertical model:** Ayurveda Healthcare Services (54% of FY25 revenue: ₹254 Cr) + Ayurveda Healthcare Products (46% of FY25 revenue: ₹215 Cr)
- **Services:** Hub-and-spoke via hospitals & clinics; CAPEX/OPEX-light; high operating leverage beyond break-even
- **Products:** ~85% gross margins; outsourced manufacturing; sold via company centers, tele-calling, e-com
- **Franchise model:** 36/116 facilities franchised; franchisee bears CAPEX/OPEX; JSLL controls doctors & exclusive medicine supply
- **Capital-light:** CAPEX ₹3-4 lakh/bed; 3Y avg ROCE: 71%; debt-free balance sheet
- **Flywheel effect:** Satisfied patients → word-of-mouth → more volumes → scale → cost-effective treatment → reinvestment
- **Research moat:** 17+ clinical papers published (Jan 2024–Feb 2025), heavy CKD focus
- **NABH accreditation:** 45 NABH-accredited hospitals/clinics; ~9% market share in NABH Panchkarma/AYUSH

### Key Financial Metrics (Q1FY26)
| Metric | Q1FY25 | Q4FY25 | Q1FY26 | QoQ | YoY |
|--------|--------|--------|--------|-----|-----|
| Revenue (₹ Cr) | 100.04 | 139.02 | 174.29 | +25% | +74% |
| EBITDA (₹ Cr) | 24.65 | 46.72 | 78.79 | +69% | +220% |
| EBITDA Margin | 25% | 34% | 45% | | |
| PAT (₹ Cr) | 16.14 | 27.35 | 51.31 | +88% | +218% |
| PAT Margin | 16% | 20% | 29% | | |
| EPS (₹) | 1.30 | 2.20 | 4.13 | +88% | +218% |

**Revenue Mix Q1FY26:** Medicine ₹80.65 Cr (46%), Private Panchkarma ₹78.13 Cr (45%), Govt Panchkarma ₹15.51 Cr (9%)

### Annual Financials (FY21-FY25)
| Year | Revenue (₹ Lakh) | EBITDA% | PAT% | EPS (₹) |
|------|-----------------|---------|------|---------|
| FY21 | 13,581 | 12% | 8% | 10.19 |
| FY22 | 14,645 | 12% | 8% | 11.15 |
| FY23 | 20,390 | 23% | 16% | 13.69 |
| FY24 | 32,441 | 29% | 21% | 27.84 |
| FY25 | 46,907 | 27% | 19% | 36.50 |

- FY22-25 revenue CAGR: 47%
- FY25 Total Assets: ₹32,831 Lakhs; Equity: ₹27,302 Lakhs
- FY25 OCF: ₹6,862.68 Lakhs; Investing: (₹7,036.81) Lakhs

### Key Operating Metrics (FY23-FY25)
| Metric | FY23 | FY24 | FY25 |
|--------|------|------|------|
| Operational Beds | 460 | 1,277 | 1,600 |
| Beds Occupied | 280 | 490 | 850 |
| ARPB (₹) | 6,100 | 7,900 | 8,200 |
| IPD Volumes | 5,728 | 13,159 | 24,578 |
| OPD Volumes (Lakh) | 1.57 | 2.52 | 3.37 |
| Medicine Orders (Lakh) | 2.27 | 2.09 | 4.43 |
| Services Rev (₹ Cr) | 62.6 | 138.7 | 253.8 |
| Products Rev (₹ Cr) | 141.3 | 185.9 | 215.3 |
| Govt Rev (₹ Cr) / % | 23.9/12% | 52.0/16% | 117.8/25% |
| Active Centres | 124 | 111 | 115 |

### Center Count & Geographic Spread
- 55 hospitals + 61 clinics/daycare = 116 total (77 units in FY25 context)
- 2,179 beds operational; 391 recently added; 360 in pipeline (5 facilities)
- 23 states, 100+ cities; concentrated in UP (12 hospitals), Rajasthan (10), Haryana (6)
- Top hospitals: Meerut (612 beds), Navi Mumbai (163), Lucknow (115), Derabassi (113)

### Growth Strategy & Guidance
- Operational efficiency → improve utilization of existing assets
- Capacity expansion: new centres + bed additions in existing centres
- OTC pharma channel for medicine sales
- New product launches (10 upcoming: Dr. LVR, Dr. Kidney Care, Dr. Madhu Care, etc.)
- Cashless insurance enablement
- Government Panel/AYUSH coverage expansion
- **Overseas expansion starting with UAE**

### Unit Economics (100-bed facility)
- CAPEX: ₹250-350 L (₹3-4 L/bed); Payback: <6 months
- Monthly OPEX: ₹50-55 L payroll + ₹10-12 L rent; Variable: 12-15% of sales
- Revenue/bed/day: ₹8,287; Break-even: ~35% occupancy; 70% utilization in 12-18 months

### Market Stats (Aug 14, 2025)
- CMP: ₹654; Mcap: ₹8,129 Cr; 52W H/L: ₹670/₹241
- Shareholding: Promoters 63.53%, Public 30.30%, FII/DII 6.17%

### Strategic Messaging
- "Freedom from 2D: Disease & Drugs"
- Migration to NSE/BSE mainboard (Aug 2025)
- Ind AS accounting shift
- Strategic shift toward Private Panchkarma (better margins, better cash conversion vs Govt Panel)

---

## 2. PPT_Nov2025 (Q2FY26 — November 2025)

### Key Financial Metrics (Q2FY26)
| Metric | Q2FY25 | Q1FY26 | Q2FY26 | QoQ | YoY |
|--------|--------|--------|--------|-----|-----|
| Revenue (₹ Cr) | 114.09 | 174.29 | 189.85 | +9% | +66% |
| EBITDA (₹ Cr) | 40.27 | 78.79 | 92.06 | +17% | +129% |
| EBITDA Margin | 35% | 45% | 48% | | |
| PAT (₹ Cr) | 26.60 | 51.31 | 58.78 | +15% | +121% |
| PAT Margin | 23% | 29% | 31% | | |
| EPS (₹) | 2.14 | 4.13 | 4.73 | +15% | +121% |

**Revenue Mix Q2FY26:** Medicine ₹95.30 Cr (50%), Private Panchkarma ₹85.78 Cr (45%), Govt Panchkarma ₹8.77 Cr (5%)

**H1FY26 Revenue Mix:** Services ₹188 Cr (52%), Products ₹176 Cr (48%) → **Total ₹364 Cr**

### Operating Metrics (Q2FY26)
| Metric | Q2FY25 | Q1FY26 | Q2FY26 | QoQ | YoY |
|--------|--------|--------|--------|-----|-----|
| IPD Volumes | 6,111 | 8,616 | 9,614 | +12% | +57% |
| OPD Volumes (Lakh) | 0.84 | 1.24 | 1.40 | +13% | +67% |
| Day Care Volumes | 6,380 | 14,828 | 17,154 | +16% | +169% |
| OPD+COD+VC (Lakh) | 1.40 | 2.07 | 2.59 | +25% | +85% |
| Video-Call Consultations | 25,469 | 41,789 | 56,347 | +35% | +121% |

### Center Count & Capacity (Changes from Aug 2025)
- **Hospitals:** 55 → **58** (+3 new hospitals operational in Q2)
- **Clinics & Daycare:** 61 → **59**
- **Operational Beds:** 2,179 → **2,220** (+41)
- **Beds Recently Added:** 391 → **582**
- **Beds in Pipeline:** 360 → **400** (5 facilities)
- Franchise: 36 → **35**/117

### Key Changes from Q1
1. **EBITDA margin further expanded:** 45% → 48% (QoQ)
2. **Finance cost spiked:** ₹166 L → ₹435 L (+162% QoQ) — first sign of borrowing
3. **Govt Panchkarma declined further:** ₹15.51 Cr → ₹8.77 Cr (now only 5% of revenue)
4. **New MD:** Acharya Manish Ji now referenced as Managing Director (was Manish Grover in Aug)
5. **Salesforce partnership announced:** Digital transformation / AI-driven patient engagement
6. **New product launches:** Dr. BP Care DS, Dr. Kidney Care DS, Dr. Madhu Care DS, Dr. Liver DS, Dr. Sukoon DS
7. **Pipeline products shifted:** From 10 specific SKUs (Aug) to 6 categories (Plant Based Protein, Gyno Syrup, Joint Pain range)
8. **ARPB:** ₹8,287 → **₹8,324**/day/bed
9. **Research papers:** Grew from 17 to significantly more (2/4 section added)

### Market Stats (Nov 6, 2025)
- CMP: ₹785.20; Mcap: ₹9,720 Cr; 52W H/L: ₹850/₹280
- Shareholding: Prom 63.61%, Public 29.80%, FII 6.59%

### Messaging Shifts
- Revenue growth guidance: Described as "one of the fastest growing healthcare enterprises"
- "Freedom from 2D: Diseases & Drugs" tagline continues
- Strategic focus on Private Business Segment reiterated
- International expansion flags: USA, Australia, Canada, Pakistan, UAE, Bangladesh now shown on geographic map

---

## 3. PPT_Feb2026 (Q3FY26 — February 2026)

### Key Financial Metrics (Q3FY26)
| Metric | Q3FY25 | Q2FY26 | Q3FY26 | QoQ | YoY |
|--------|--------|--------|--------|-----|-----|
| Revenue (₹ Cr) | 115.69 | 189.85 | 221.66 | +17% | +92% |
| EBITDA (₹ Cr) | 29.61 | 92.06 | 100.80 | +9% | +240% |
| EBITDA Margin | 26% | 48% | 45% | | |
| PAT (₹ Cr) | 13.21 | 58.78 | 66.73 | +14% | +405% |
| PAT Margin | 11% | 31% | 30% | | |
| EPS (₹) | 1.06 | 4.73 | 5.37 | +14% | +407% |

**Revenue Mix Q3FY26:** Medicine ₹121.74 Cr (55%), Private Panchkarma ₹91.81 Cr (41%), Govt Panchkarma ₹8.12 Cr (4%)

**9MFY26 Revenue:** 78% YoY growth; **EBITDA margin: 46%** (vs 29% in FY25)

### Operating Metrics (Q3FY26)
| Metric | Q3FY25 | Q2FY26 | Q3FY26 | QoQ | YoY |
|--------|--------|--------|--------|-----|-----|
| IPD Volumes | 6,133 | 9,614 | 11,313 | +18% | +84% |
| OPD Volumes (Lakh) | 0.83 | 1.40 | 1.57 | +12% | +89% |
| Day Care Volumes | 7,946 | 17,154 | 18,977 | +11% | +139% |
| OPD+COD+VC (Lakh) | 1.25 | 2.59 | 4.34 | +68% | +247% |
| Video-Call Consultations | 19,479 | 56,347 | 61,135 | +8% | +214% |

### Center Count & Capacity (Changes from Nov 2025)
- **Total Beds:** New metric — **2,800** total, **2,290** operational
- **Operational Beds:** 2,220 → **2,290** (+70)
- **Beds Recently Added:** 582 → **510** (reset/recalculated)
- **Beds in Pipeline:** 400 → **475** (across 6 facilities, vs 5 previously)
- Hospitals: 58 (unchanged); Clinics/Daycare: 59 (unchanged)
- NABH accredited: 46 → **49**; Pipeline: 5 → **3**

### Key Changes from Q2
1. **EBITDA margin dipped:** 48% → 45% (first sequential decline in margins)
2. **Operating expenses jumped:** ₹7,370 L → ₹9,671 L (+31% QoQ)
3. **Finance cost moderated:** ₹435 L → ₹310 L (-29% QoQ)
4. **H1 Revenue Mix shifted:** Products overtook Services in 9MFY26: Products ₹298 Cr (51%) vs Services ₹288 Cr (49%)
5. **Jeena Sikho Health Card announced:** Trial phase, referral benefits, diagnostic discounts
6. **HIIMS branding introduced:** Sub-brand "HUMS (Hospitals & Institute of Integrated Medical Sciences)"
7. **New MD title:** Acharya Manish Ji, Managing Director
8. **ARPB:** ₹8,337/day/bed
9. **Doctors:** 541→**575**; Support staff: 711→**750**
10. **Newer facilities highlighted:** Panvel (Mumbai) — 230 beds, operational Oct 2025

### Market Stats (Feb 6, 2026)
- CMP: ₹712.50; Mcap: ₹8,856 Cr; 52W H/L: ₹850/₹280
- Shareholding: Prom 63.62%, Public 29.96%, FII+DII 6.42%

### Messaging Shifts
- First appearance of "Empowering Holistic Health & Wellness" alongside traditional tagline
- Strong "volume-led growth" narrative
- International flags (USA, Australia, Canada, Pakistan, UAE, Bangladesh) now explicitly on geographic slide
- Management commentary now delivered by Acharya Manish Ji as MD

---

## 4. PPT_May2026 (Q4FY26 / FY26 Annual — May 2026)

### Key Financial Metrics (Q4FY26)
| Metric | Q4FY25 | Q3FY26 | Q4FY26 | QoQ | YoY |
|--------|--------|--------|--------|-----|-----|
| Revenue (₹ Cr) | 139.25 | 221.66 | 215.55 | -3% | +55% |
| EBITDA (₹ Cr) | 45.77 | 100.80 | 77.98 | -23% | +70% |
| EBITDA Margin | 33% | 45% | 36% | | |
| PAT (₹ Cr) | 25.34 | 66.73 | 45.35 | -32% | +79% |
| PAT Margin | 18% | 30% | 21% | | |
| EPS (₹) | 10.19 | 5.37 | 3.65 | -32% | -64% |

**Revenue Mix Q4FY26:** Medicine ₹117.98 Cr (55%), Private Panchkarma ₹93.80 Cr (43%), Govt Panchkarma ₹3.76 Cr (2%)

### Full Year FY26 Annual Performance (CRITICAL)
| Metric | FY25 | FY26 | YoY |
|--------|------|------|-----|
| Revenue (₹ Cr) | 469.07 | **801.35** | +71% |
| EBITDA (₹ Cr) | 140.60 | **349.63** | +148% |
| EBITDA Margin | 30% | **44%** | +1400 bps |
| PAT (₹ Cr) | 79.94 | **222.18** | +178% |
| PAT Margin | 17% | **27%** | +1000 bps |
| EPS (₹) | 6.43 | 17.87 | +178% |

**FY26 Segment Revenue:** Services ₹386.6 Cr (48%), Products ₹415.6 Cr (52%)

### Key FY26 Annual Financials (₹ Lakhs)
| Particulars | FY22 | FY23 | FY24 | FY25 | FY26 |
|-------------|------|------|------|------|------|
| Revenue | 14,645 | 20,390 | 32,441 | 46,907 | **80,135** |
| EBITDA | 1,812 | 4,608 | 9,299 | 14,060 | **34,963** |
| EBITDA% | 12% | 23% | 29% | 30% | **44%** |
| PAT | 1,127 | 3,374 | 6,921 | 7,994 | **22,218** |
| PAT% | 8% | 16% | 21% | 17% | **27%** |
| Finance Cost | 114 | 70 | 41 | 1,065 | 1,283 |
| Depreciation | 331 | 313 | 510 | 2,911 | 4,758 |

**3Y CAGR (FY23-26): 58%** (up from 47% FY22-25)

### Balance Sheet Evolution (₹ Lakhs)
| Particulars | FY24 | FY25 | FY26 |
|-------------|------|------|------|
| Total Equity | 19,225 | 25,634 | 46,740 |
| Non-Current Liab. | 88 | 8,925 | 10,231 |
| Total Assets | 22,053 | 41,895 | 67,312 |
| PPE | 6,683 | 9,234 | 11,701 |
| Trade Receivables | 4,119 | 8,496 | 6,993 |
| Cash | 6,201 | 2,298 | 1,516 |
| Inventories | 350 | 1,155 | 2,017 |

**Cash Flow (₹ Lakhs):** FY26 OCF ₹26,199; Investing (₹21,109); Financing (₹5,873)

### Operating Metrics (FY24-FY26)
| Metric | FY24 | FY25 | FY26 |
|--------|------|------|------|
| Operational Beds | 1,277 | 1,600 | 2,300 |
| Beds Occupied | 490 | 850 | 1,288 |
| Occupancy % | 38% | 53% | 56% |
| ARPB (₹) | 7,900 | 8,200 | 8,300 |
| IPD Volumes | 13,159 | 24,578 | 40,454 |
| OPD Volumes (Lakh) | 2.52 | 3.37 | 5.70 |
| Medicine Orders (Lakh) | 2.09 | 4.43 | 11.83 |
| Services Rev (₹ Cr) | 138.7 | 253.8 | 386.6 |
| Products Rev (₹ Cr) | 185.9 | 215.3 | 415.6 |
| Govt Rev (₹ Cr) / % | 52.0/16% | 117.8/25% | 36.0/4% |
| Active Centres | 111 | 115 | 119 |

### Center Count & Capacity
- **61 hospitals** (+3), **58 clinics/daycare** (-1); Total: **119**
- **Total beds: 2,861**, Operational: 2,300
- Recently added: 561; Pipeline: 445 (5 facilities)
- Franchise: 33/119
- NABH accredited: 50; Pipeline: 3
- Geographic: UP +1 hospital (12), Bihar +1 hospital (2), Punjab +1 hospital (4)

### Key Changes from Q3
1. **First sequential revenue decline:** -3% QoQ (₹221.66 Cr → ₹215.55 Cr)
2. **Major margin compression in Q4:** EBITDA margin 45%→36% (one-off provisions: ₹7 Cr labour code, ₹5 Cr ECL, ₹9 Cr Ind AS adjustments)
3. **ROCE declined:** 71% → **46%** (3Y avg) — recalibrated with new asset base
4. **Govt Panel nearly collapsed:** ₹8.12 Cr (4%) → ₹3.76 Cr (2%); FY26 full year: 4% of revenue vs 25% in FY25
5. **Trade Receivables improved:** ₹8,496 L → ₹6,993 L (first decline since scaling began)
6. **Health Card launched:** "Jeena Sikho Health Card" in trial; Swadeshi Health Card with referral/cashback
7. **New Q4 product launches:** Swaranfalum Amrit (3 flavors), Fat Burner, Nutri Roz protein, Pre-Workout Shot
8. **Consultations surged:** FY26 OPD+VOPD: 227,127 (vs 102,556 in FY25)
9. **OPD+COD+VC (cumulative):** 14.10 Lakh (vs 5.46 L in FY25) — 158% jump
10. **Research papers:** "More than 170+" (massive increase from prior ~20-30)
11. **Dividend:** Board recommends ₹4.50/share final dividend for FY26

### Market Stats (May 29, 2026)
- CMP: ₹614.95; Mcap: ₹7,756 Cr; 52W H/L: ₹850/₹400.25
- Stock down significantly from Nov peak (₹785→₹615, -22%)
- Shareholding: Prom 63.62%, Public 29.75%, FII+DII 6.63%

---

## 5. PPT_Jun2026 (Q4FY26 / FY26 Annual — June 2026)

**Substantially identical to May 2026 PPT** but restructured: Annual Financial Highlights (5Y Income Statement, Balance Sheet, Cash Flow) presented **before** Q4FY26 quarterly details. Same FY26 and Q4FY26 data.

### Notable Differences from May 2026
1. **Slide order reorganized:** Annual highlights first, then Q4 quarterly
2. **FY25/FY26 columns noted as projections/guidance** in annual slides (green highlights)
3. **Swadeshi Health Card** detailed with full program description (referral bonuses, cashback, "Chandan Diagnostics" partnership)
4. **Management Commentary** provides explicit breakdown of one-off provisions:
   - Employee-related provisions: ~₹7 Cr
   - One-time ECL provision: ~₹5 Cr
   - Ind AS transition adjustments: ~₹9 Cr
5. **EBITDA margin attribution:** FY26 full-year 44% driven by "operating leverage, improved asset utilization, and scalability"

---

## Cross-Quarter Evolution Tracker

### Revenue Growth (₹ Cr)
| Quarter | Revenue | QoQ | YoY |
|---------|---------|-----|-----|
| Q1FY26 | 174.29 | +25% | +74% |
| Q2FY26 | 189.85 | +9% | +66% |
| Q3FY26 | 221.66 | +17% | +92% |
| Q4FY26 | 215.55 | -3% | +55% |

### EBITDA Margin Trend
| Quarter | Margin |
|---------|--------|
| Q1FY26 | 45% |
| Q2FY26 | 48% |
| Q3FY26 | 45% |
| Q4FY26 | 36% |

### PAT Margin Trend
| Quarter | Margin |
|---------|--------|
| Q1FY26 | 29% |
| Q2FY26 | 31% |
| Q3FY26 | 30% |
| Q4FY26 | 21% |

### Revenue Mix Shift (% of Total)
| Segment | Q1FY26 | Q2FY26 | Q3FY26 | Q4FY26 |
|---------|--------|--------|--------|--------|
| Medicine | 46% | 50% | 55% | 55% |
| Private Panchkarma | 45% | 45% | 41% | 43% |
| Government Panchkarma | 9% | 5% | 4% | 2% |

### Govt Panel Revenue Collapse
| Period | Govt Rev (₹ Cr) | % of Total |
|--------|----------------|------------|
| FY25 | 117.8 | 25% |
| Q1FY26 | 15.51 | 9% |
| Q2FY26 | 8.77 | 5% |
| Q3FY26 | 8.12 | 4% |
| Q4FY26 | 3.76 | 2% |
| **FY26 Full** | **36.0** | **4%** |

### Capacity Build-Up
| Metric | Aug '25 | Nov '25 | Feb '26 | May/Jun '26 |
|--------|---------|---------|---------|-------------|
| Hospitals | 55 | 58 | 58 | 61 |
| Clinics/Daycare | 61 | 59 | 59 | 58 |
| Total Centres | 116 | 117 | 117 | 119 |
| Operational Beds | 2,179 | 2,220 | 2,290 | 2,300 |
| Total Beds | N/R | N/R | 2,800 | 2,861 |
| Beds in Pipeline | 360 | 400 | 475 | 445 |
| Pipeline Facilities | 5 | 5 | 6 | 5 |
| Franchise | 36 | 35 | 35 | 33 |

### ARPB Evolution
| Period | ARPB (₹/day) |
|--------|-------------|
| FY23 | 6,100 |
| FY24 | 7,900 |
| FY25 | 8,200 |
| Aug '25 | 8,287 |
| Nov '25 | 8,324 |
| Feb '26 | 8,337 |
| May/Jun '26 | 8,300 |

### Patient Volumes (Quarterly IPD)
| Quarter | IPD Volumes | QoQ |
|---------|-------------|-----|
| Q4FY25 | 6,415 | |
| Q1FY26 | 8,616 | +34% |
| Q2FY26 | 9,614 | +12% |
| Q3FY26 | 11,313 | +18% |
| Q4FY26 | 10,911 | -4% |

### Video-Call Consultations
| Quarter | Consultations | QoQ |
|---------|---------------|-----|
| Q4FY25 | 34,451 | |
| Q1FY26 | 41,789 | +21% |
| Q2FY26 | 56,347 | +35% |
| Q3FY26 | 61,135 | +8% |
| Q4FY26 | 67,856 | +11% |

### Key Metric Revisions
| Item | Aug '25 | Jun '26 | Change |
|------|---------|---------|--------|
| 3Y CAGR | 47% (FY22-25) | 58% (FY23-26) | Rebased |
| 3Y Avg ROCE | 71% | 46% | Dropped 25pp |
| Doctors | 532 | 592 | +60 |
| Support Staff | 650 | 779 | +129 |
| NABH Accreditations | 45+3 | 50+3 | +5 |
| Research Papers | ~17 | 170+ | 10x |
| CMP | ₹654 | ₹615 | -6% |
| Mcap | ₹8,129 Cr | ₹7,756 Cr | -4.6% |

### Major Strategy/Messaging Changes Across Quarters
1. **H1 to H2 Pivot:** Products revenue overtook Services (52% vs 48% in FY26)
2. **Government Panel virtual exit:** From 25% of revenue (FY25) to 4% (FY26) — deliberate strategic pullback
3. **Health Card initiative:** Introduced in Q3, launched in Q4 as loyalty/referral tool
4. **HIIMS branding:** New sub-brand introduced in Q3; not present in Aug/Nov
5. **Salesforce partnership:** Announced Q2 for digital transformation
6. **Management transition:** Manish Grover (MD in Aug) → Acharya Manish Ji (MD from Nov onward)
7. **Massive margin expansion FY25→FY26:** EBITDA margins from 30% to 44% (management ascribes to operating leverage)
8. **ROCE recalibration:** 71% to 46% reflects heavy asset build
9. **Finance cost surge:** From ₹41 L (FY24) to ₹1,283 L (FY26) — debt funding expansion
10. **Q4 margin compression warning:** One-off provisions worth ~₹21 Cr in Q4FY26
11. **"Way Forward" unchanged** across all 5 PPTs: Same 7 strategic pillars every quarter
</task_result>
</task>
```

---

## Assistant (Build · DeepSeek V4 Pro · 115.1s)

_Thinking:_

Great comprehensive PPT analysis. Now let me get the transcripts analyzed.

Now let me read all transcripts:

**Tool: task**

**Input:**
```json
{
  "description": "Read transcript txt files",
  "prompt": "Read the following 4 transcript text files for Jeena Sikho Lifecare. These are concall transcripts. Read ALL of them chronologically (oldest first):\n\n1. \"/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Aug2025.txt\"\n2. \"/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Nov2025.txt\"\n3. \"/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Feb2026.txt\"\n4. \"/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Jun2026.txt\"\n\nFor each transcript, extract and return:\n1. Management commentary on business performance, strategy, outlook\n2. All forward guidance provided (revenue, margin, capex, expansion targets)\n3. Key Q&A exchanges — especially analyst questions that reveal risks, skepticism, or management's responses to challenges\n4. Capex plans, debt levels, fund raise plans\n5. Competitive landscape discussion\n6. Any red flags: inconsistencies, evasive answers, changes in tone\n7. Specific revenue/EBITDA/PAT targets for future years\n8. Center/bed expansion plans\n9. Product/service mix discussion\n10. Government revenue discussion\n11. Any cost/margin outlook\n\nTrack how answers evolve across the 4 transcripts. Look for any promises made in earlier transcripts that are walked back later. Return comprehensive data.",
  "subagent_type": "general"
}
```

**Output:**
```
<task id="ses_0cc70ac95ffepjoF9B7f3ft5U6" state="completed">
<task_result>
Below is the comprehensive analysis across all 4 transcripts:

---

# JEENA SIKHO LIFECARE - Comprehensive Concall Analysis (Aug 2025 – Jun 2026)

## 1. MANAGEMENT COMMENTARY ON BUSINESS PERFORMANCE, STRATEGY, OUTLOOK

### Aug 2025 (Q1 FY26)
- Revenue INR174 Cr (+74% YoY), EBITDA INR79 Cr (+220% YoY, 45% margin), PAT INR51 Cr (+218% YoY)
- 2180 operational beds → 2570 total capacity. Services 54%, Products 46% of revenue
- Strategy: College tie-ups for capital-light expansion, OTC product launch, tech/AI enablement
- Tone: Extremely bullish, offering free product samples to investors

### Nov 2025 (Q2 FY26)
- Revenue INR190 Cr (+66% YoY, +9% QoQ), EBITDA INR92 Cr (+129% YoY, 48% margin), PAT INR59 Cr (+121% YoY)
- Bed target of 2,800 achieved in 6 months (vs full-year promise). Occupancy steady at 57%
- Grant Thornton signed as statutory auditor. Chandan Diagnostic tie-up announced. Franchise model (50 new hospitals) planned
- Q3 flagged as "weak quarter" due to Diwali/winter

### Feb 2026 (Q3 FY26)
- Revenue INR221.7 Cr (+92% YoY, +17% QoQ), EBITDA INR100.8 Cr (240% YoY, 45% margin), PAT INR66.7 Cr (+405% YoY)
- Occupancy 58% despite "worst quarter for healthcare." Entero partnership finalized. 2nd OTC product launched.
- Deliberately did NOT increase operational beds in Q3 to protect margins (expenses avoided)
- New "Super Specialty Clinic Day Care Centers" chain announced. Forvis Mazars appointed internal auditor

### Jun 2026 (Q4 FY26 / Full Year)
- FY26 Full Year: Revenue INR801 Cr (+71% YoY), EBITDA INR349 Cr (+149% YoY, 44% margin), PAT INR222 Cr (+177% YoY, 28% margin)
- Q4 standalone: Revenue INR216 Cr (+55% YoY), EBITDA INR78 Cr (36% margin), PAT INR45 Cr
- **Major one-off provisions of ~INR21 Cr in Q4**: Labour code changes, ESOP provision, lease adjustments under Indian AS (driven by GT), ECL provision INR5 Cr, loyalty points INR1.25 Cr
- Blames Q4 softness on "Iran-America war panic" → advance-booking patients deferred visits. Entero partnership didn't start as planned (Entero wanted to expense-share)
- New narrative: "Preventive" not "Curative" - positioning company as a paradigm shift. New products for pregnancy planning

---

## 2. FORWARD GUIDANCE (REVENUE, MARGIN, PAT, EXPANSION)

| Metric | Aug 2025 | Nov 2025 | Feb 2026 | Jun 2026 |
|--------|----------|----------|----------|----------|
| **FY26 Revenue** | INR700 Cr (hospital+clinic only, OTC excluded) | INR650-700 Cr (same) | Implied INR780 Cr (run-rate) | Actual INR801 Cr |
| **PAT Margin Target** | 20-25% "healthy margin" | 20-25% | 20-25% | FY26 Actual 28% |
| **OTC Revenue Target** | INR500 Cr in 1.5-2 yrs | INR300-500 Cr (no timeframe given) | INR500 Cr in 2 years; INR300 Cr from one product | Not updated; Entero model stalled |
| **PAT Target** | ~INR140 Cr (mentioned by analyst, not denied) | ~INR125-130 Cr implied | ~INR225 Cr+ (for FY26, "work out yourself") | **FY26 Actual: INR222 Cr. FY27: "Minimum INR300 Cr PAT"** |
| **Long-term Profit Target** | None | None | **INR1,000 Cr profit (4-5x from here, 3-5 yrs)** | **PAT 4-5x in 3-5 years** |
| **Long-term Revenue** | None | None | None | **INR3,000 Cr revenue in 3-5 years** |
| **Beds - FY26** | 2,850-3,000 by Mar 2026 | 3,000 by year-end | 2,800 ready, 2,290 ops | 2,300 ops; 3,000-3,500 by Mar 2027 |
| **Beds - Long-term** | 7,000-10,000 in 3-5 years | 7,000-10,000 in 3-5 years | 7,000-10,000 in 3-5 years | 7,000-10,000 in 3-5 years |
| **EBITDA Margin Target** | No guidance (45% actual) | 48% actual | 45% actual | 44% FY26 Actual; Q4 dipped to 36% |

### Key Evolution in Guidance:
- **FY26 Revenue**: Promised INR700 Cr → delivered INR801 Cr. OTC contribution not separately disclosed.
- **FY27 PAT guidance**: First explicit "minimum INR300 Cr PAT" given in Jun 2026 (vs INR222 Cr FY26 actual). This implies ~35% PAT growth on a base with ~INR21 Cr of one-offs in Q4.
- **Long-term targets** escalated from none in Aug 2025 → INR1,000 Cr profit (Feb 2026) → INR3,000 Cr revenue (Jun 2026).
- **PAT margin guidance consistently 20-25%** through all 4 calls, but FY26 delivered 28%.

---

## 3. KEY Q&A EXCHANGES (RISKS, SKEPTICISM, MANAGEMENT RESPONSE)

### Aug 2025:
- **Divya Agarwal (Ficom)** pressed on government receivables: INR92 Cr from govt in prior quarter. Management admitted reducing govt business to 8% vs 25%+ earlier. Received INR25 Cr of old dues. Remaining ~INR70 Cr still outstanding.
- **Nilabja Dey** asked about CEO/COO hiring (promised in 2024 call) - COO promoted internally, CEO still being searched. Asked about tax rate. Cut off by moderator.
- **Neeraj Agarwal** noted opex decreased despite bed addition — management cited cost control committee, bulk negotiations.

### Nov 2025:
- **Ashok Parekh** challenged the decision to curtail government business, arguing other big hospitals run on CGHS/EMpanelment and JSLL was losing opportunity. **Manish Grover's revealing response**: "Your investment community doesn't let us live — if I do this, you raise questions. If I do that, you raise questions."
- **Raunak Duggar** pointed out college tie-up count stagnant at 3 (same as Q1), asking why less attention. Management cited govt NOC formalities, trust/NGO restrictions, and wanting to prove model first.
- **Chirag Shah** pressed on Chandan investment commitment — revealed they hadn't paid a single rupee yet despite announced tie-up.

### Feb 2026:
- **Shubhanu (Three Head Capital)** flagged that operational beds only increased by 60 from Q1 to Q2 (2179→2220), and occupancy remains very low (58%). Called out the inconsistency between "focus on occupancy" and low bed addition. Management's explanation: deliberately avoided adding beds in Q3 weak quarter.
- **Chirag Shah** pressed on one-offs — management segmented but answers were vague.

### Jun 2026:
- **Akshay** flagged sequential decline in Q4 OPD/IPD/daycare volumes. **Manish Grover's response**: "It happened because of Trump, sir" (Iran-America war scare). Then blamed booking recognition change under GT (advances no longer booked until bill generation).
- **Chirag Shah / Deepak Poddar** pressed hard on the INR21 Cr one-off bifurcation — CFO admitted INR19-20 Cr one-time, INR2 Cr recurring. But later admitted lease impact "will gradually decrease each quarter" (i.e., not purely one-time).
- **Praveen Kumar** asked what can be expected for FY27 — got "minimum INR300 Cr PAT" but no revenue guidance.
- **Entero deal admission**: "The tie-up was done, but the business model didn't start because Entero was asking us to bear the expenses." (Jun 2026) — a significant walk-back from the Feb 2026 enthusiasm.

---

## 4. CAPEX, DEBT, FUND RAISE PLANS

| Item | Aug 2025 | Nov 2025 | Feb 2026 | Jun 2026 |
|------|----------|----------|----------|----------|
| **Capex per Bed** | INR3-4 Lakh (own); INR1-1.5 Lakh (college model) | INR3-4 Lakh | INR3-4 Lakh | INR3-4 Lakh |
| **Debt** | None mentioned | None mentioned | None mentioned | "Absolutely no debt on the balance sheet" |
| **Cash/Investments** | — | INR10 Cr in Chandan (not yet paid) | "Money kept aside for high-level acquisition" | — |
| **Own Manufacturing** | "Next year I will buy a large manufacturing unit" | Not mentioned | "This year I will make manufacturing my own" | Not re-mentioned |
| **Fund Raise** | None planned | None | None — "We have capital now, why franchise?" | None |

### Observations:
- The own-manufacturing promise was made in Aug 2025 ("next year") and Feb 2026 ("this year"), but not mentioned in Jun 2026.
- College-tie-up model was supposed to reduce capex to INR1-1.5 Lakh/bed but stalled at 3 colleges.
- Cash position appears strong (INR222 Cr PAT, no debt) but Q4 showed provisioning hits.
- Chandan investment of INR10 Cr finally paid by Feb 2026 ("just gave them the money now").

---

## 5. COMPETITIVE LANDSCAPE

- **Aug 2025**: No specific competitor named. "Allopathy has 19 lakh beds, I have 2,200 — I'm 0.00%!" Positioned as "preventive" vs everyone else who is "curative."
- **Nov 2025**: Claims "no other player in Ayurveda who has undergone clinical trials and launched products."
- **Feb 2026**: "We don't have any competition with anyone" — blue ocean strategy. Entero deal positioned as exclusive Ayurveda partnership with 1.25 lakh pharmacies.
- **Jun 2026**: Manish says: "10-15 companies like mine should be listed so a separate market is created." Requests investors not to see the company "quarter-on-quarter" but as "forehead of India."
- **Competitive risks unaddressed**: Apollo entering Ayurveda (asked in Aug 2025 — Manish said they'd sell products to Apollo if asked). No discussion of Patanjali, Dabur, or any large Ayurveda players as threats. No competitive moat articulated beyond "first mover in clinical trials."

---

## 6. RED FLAGS & CONCERNS

### Inconsistencies / Walk-backs:
1. **Entero Deal (MAJOR)**: Announced with fanfare in Nov 2025 ("will make an exclusive agreement"), finalized in Feb 2026 ("agreement signed last week"). By Jun 2026: "business model didn't start because Entero was asking us to bear the expenses." This was a significant promise walked back.

2. **OTC Product Launch Timeline**: Aug 2025 said 6-7 products by Mar 2026, 15-20 next year. Feb 2026 said 16 products "by Dec 2026." Jun 2026 reality: only 1 product >3 months old in OTC. 9 total launched but all within 3 months. BP/sugar/kidney pills "supposed to be launched in February" — delayed to June/July.

3. **College Tie-ups Stalled**: Aug 2025 said 16 colleges approached, "ready to work with us." By Nov 2025 — "stopped them so first we can practically run 2-3 efficiently." Feb 2026 — only 1 operational out of 3. Jun 2026 — "I have details of seven colleges that I can take whenever I want" (contradicts earlier concern about NGO/trust restrictions).

4. **"Weak Quarter" Narrative**: Q3 called weak (Diwali/winter) yet delivered record INR221 Cr. Q4 called weak (war panic) yet full year delivered INR801 Cr. Pattern: lower expectations and then beat. But Q4 PAT (INR45 Cr) was significantly below run-rate after adjusting one-offs.

5. **Revenue per Bed Metric Change**: Jun 2026 abruptly shifted from ARPOB (INR8,337) to a new metric (INR4,650 per bed assuming 100% occupancy). When asked if it'd return to INR8,500+: "Sir, you do the calculation work." This makes comparisons harder.

6. **Occupancy Stagnation**: 57% → 57% → 58% over three quarters. Despite claims of "80% on old beds," aggregate occupancy consistently low. Management's "deliberately didn't add operational beds" doesn't explain why occupancy isn't rising on existing beds.

7. **Evasion on Numbers**: Repeatedly says "I don't know calculations" or "I don't pay attention to numbers" when pressed on guidance. Directs questions to CFO or asks analysts to "calculate yourself." In Jun 2026, admits "I don't know ROCE and all that."

8. **Government Receivables**: From INR92 Cr in prior quarter to ~INR70 Cr by Aug 2025. Q4 FY26 had INR5 Cr ECL provision (suggesting some govt receivables written off). Full year govt revenue dropped from INR118 Cr (FY25) to INR36 Cr (FY26) — an INR82 Cr reduction framed as "strategic."

9. **Auditor Changes**: Aug 2025 confusingly discussed Walker Chandiok, Grant Thornton, EY all in one Q&A. Grant Thornton finalized as statutory auditor in Q2. Forvis Mazars added as internal auditor by Q3. Original auditor (Deepak K Garg) still internal auditor until change.

10. **Q4 One-off Provisions**: INR21 Cr in one-offs is material relative to INR45 Cr Q4 PAT. The bifurcation of one-time vs recurring changed during the call itself. Leasehold impact described as both "one-time" and "will gradually decrease."

---

## 7. SPECIFIC REVENUE/EBITDA/PAT TARGETS

| Target | When Given | Amount |
|--------|-----------|--------|
| FY26 Revenue | Aug 2025 | INR700 Cr (ex-OTC) |
| FY26 Actual | Jun 2026 | INR801 Cr |
| FY26 EBITDA | Implied Aug 2025 | ~INR175 Cr (at 25% margin) |
| FY26 Actual EBITDA | Jun 2026 | INR349 Cr (44% margin) |
| FY26 PAT | Implied Aug 2025 | INR140 Cr |
| FY26 Actual PAT | Jun 2026 | INR222 Cr (28% margin) |
| FY27 PAT (minimum) | Jun 2026 | INR300 Cr |
| OTC Revenue (1.5-2 yrs) | Aug 2025 | INR500 Cr |
| Long-term PAT | Feb 2026 / Jun 2026 | INR1,000 Cr (4-5x, 3-5 yrs) |
| Long-term Revenue | Jun 2026 | INR3,000 Cr (3-5 yrs) |

---

## 8. CENTER/BED EXPANSION

| Metric | Aug 2025 | Nov 2025 | Feb 2026 | Jun 2026 |
|--------|----------|----------|----------|----------|
| **Total Beds** | 2,570 | 2,802 | ~2,800 | 2,300 ops + 445 deploying |
| **Operational Beds** | 2,180 | 2,220 | 2,290 | ~2,300 |
| **Hospitals** | 55 | 58 | — | 58 |
| **Clinics/Daycare** | — | 59 + 35 franchises | — | 59 + 35 franchises |
| **NABH** | 45 | 46 (+5 pipeline) | — | 49 (+3 pipeline) |
| **New geographies** | Chennai, BLR, HYD, Assam | Guwahati, Kolkata, Kazakhstan | Dubai, Abu Dhabi, Kazakhstan, Nepal | Lucknow, Ahmedabad, Patna, Pune |
| **Wellness Centers** | None | "Premium center in 2-4 months" | VVIP upgrade of 28 rooms in Meerut | Manali ultra-luxury (108 rooms, July); Panchkula (June) |

### Expansion Model Evolution:
- **Aug 2025**: College tie-up as primary expansion vehicle (INR1-1.5 Lakh/bed, rent + revenue share)
- **Nov 2025**: Franchise model (50 new hospitals FOCO); college model slowed
- **Feb 2026**: Franchise model walked back → "why divide margin? we have capital." 5-10 own super-specialty first
- **Jun 2026**: "I can increase 2,000 beds whenever I want" — but earlier constraints (NOC, hiring, NABH) acknowledged

---

## 9. PRODUCT/SERVICE MIX

| Period | Services (Healthcare) | Products (Medicine) | Government |
|--------|----------------------|--------------------|------------|
| Q1 FY26 | 54% | 46% | ~8% (INR15 Cr) |
| Q2 FY26 | 50% | 50% | ~3% |
| Q3 FY26 | ~45% | ~55% | ~4% (INR8 Cr/quarter) |
| Q4 FY26 | 48% | 52% | Minimal |
| FY26 Full Year | ~48% | 52% (INR416 Cr) | INR36 Cr (vs INR118 Cr FY25) |
| Target for INR3,000 Cr | ~50% | ~50% | — |

Product business: 330+ SKUs, Gross margin >85%, third-party manufacturing, sold via e-com + OTC pharmacy

---

## 10. GOVERNMENT REVENUE DISCUSSION (TRACKING THE PIVOT)

| Call | Government Revenue | Receivables | Management Stance |
|------|-------------------|-------------|-------------------|
| Aug 2025 | ~8% of quarterly (INR15 Cr), down from INR28 Cr in Q4 FY25 | ~INR70 Cr outstanding (down from INR92 Cr). INR25 Cr recovered. | "Wrote letter to govt — fix payment or we stop." Waiting for "new portal." Bihar and Maharashtra now passing Ayurveda bills. |
| Nov 2025 | ~3% of business | Not disclosed (payment cycle 4-6 months) | "No point raising outstanding in books." CAPF portal still not ready. "Will start again when money comes on time." |
| Feb 2026 | INR8 Cr/qtr (from INR118 Cr full year FY25) | "Recovered INR20-21 Cr in last few months" | "There are problems upon problems." Don't want govt business "until portal is fully settled." |
| Jun 2026 | INR36 Cr full year (vs INR118 Cr FY25) | INR5 Cr ECL provision booked | "I immediately shifted business model." UP launched UPSS scheme (cashless Ayurveda). Ayushman Bharat draft at INR8,800-9,400/day. "I can increase 2,000 beds whenever I want" when govt portal fixed. |

### Evolution:
- **Clear strategic pivot** from government-heavy (INR118 Cr in FY25) to private-dominant (INR36 Cr FY26 govt). This was forced by payment delays, not proactive strategy.
- Manish expressed frustration: "This investment community doesn't let us live" (Nov 2025) when challenged on the withdrawal.
- By Jun 2026, narrative reframed as "efficient management taking immediate decision."
- **Ayushman Bharat theme**: Mentioned in Nov 2025 ("government meeting done"), Feb 2026 ("government promised in budget"), Jun 2026 ("first draft reached ministry, 1-2 months away"). Has been a recurring "any day now" catalyst across calls.

---

## 11. COST/MARGIN OUTLOOK

| Item | Aug 2025 | Nov 2025 | Feb 2026 | Jun 2026 |
|------|----------|----------|----------|----------|
| **Gross Margin** | 85%+ | 85%+ (restated; was 91% pre-Ind AS) | 89% | 89% (FY26) / 88% (Q4) |
| **EBITDA Margin** | 45% | 48% | 45% | 44% (FY26) / 36% (Q4) |
| **PAT Margin** | 29% | 31% | 30% | 28% (FY26) |
| **PAT Margin Target** | 20-25% | 20-25% | 20-25% | 20-25% |
| **Manpower cost** | Not disclosed | Not disclosed | Not disclosed | 19% of revenue (FY26) vs 21% (FY25) |
| **Ad spend** | Reduced from prior quarter | Not disclosed | Not disclosed | INR66 Cr (FY26) vs INR58 Cr (FY25) — only 14% increase on 71% revenue growth |
| **Direct cost (products)** | 15% (medicines), 9% (consumption) | Maintained | — | 11% (FY26), down from 12% (FY25) |
| **OTC margin** | 20% PAT (after 45% trade discounts) | 18-22% PAT | 20-25% | — |
| **Govt rate** | INR8,000/day | INR8,000/day | — | INR8,800-9,400/day (Ayushman draft) |
| **Insurance rate** | — | — | — | INR8,800-9,200/day |

### Margin Sustainability Concerns:
- Q4 EBITDA margin dropped to 36% (was 45-48% in prior 3 quarters). Ex-one-offs, ~46% adjusted.
- Ad spend barely grew (+14%) while revenue grew 71% — suggests existing brand pull, but also raises question: can this persist as new products launch?
- Manish's repeated insistence on "20-25% is healthy" while delivering 28-31% creates a "beat" narrative, but Q4 showed underlying margin compression even without one-offs.
- Operating leverage story: Manpower from 21%→19%, Rent from 7%→6%, Other opex from 15%→9%. This is genuine efficiency improvement.

---

## CROSS-TRANSCRIPT TRACKING: PROMISES MADE → WALKED BACK

| Promise | When Made | Status |
|---------|-----------|--------|
| OTC INR500 Cr in 1.5-2 years | Aug 2025 | Too early; 1 product only >3 months old |
| 6-7 OTC products by Mar 2026 | Aug 2025 | Only 1 launched >3 months; "delayed due to Iran war" |
| BP/Sugar/Kidney pills launched | Feb 2026 ("this month") | Pushed to Jun/Jul 2026 |
| Ex-Entero exclusive Ayurveda partnership | Nov 2025 / Feb 2026 | "Business model didn't start" (Jun 2026) |
| 50 franchise hospitals | Nov 2025 | Walked back Feb 2026 ("why divide margin?") |
| College tie-up expansion (16 colleges approached) | Aug 2025 | Stalled at 3; "deliberately delayed" |
| Own manufacturing unit | Aug 2025 / Feb 2026 | Not re-mentioned Jun 2026 |
| CEO hiring | 2024 call / Aug 2025 | Still searching Jun 2026 |
| Dubai 2 hospitals | Aug 2025 | Became "2 daycare centers" by Nov 2025. 4 "being built" Feb 2026. |
| Ayushman Bharat inclusion | Mentioned every call | "Any day now" across all 4 calls |
| 2,850-3,000 beds by Mar 2026 | Aug 2025 | Achieved total beds, but ops only 2,290 |
| 3,000-3,500 ops beds by Mar 2027 | Jun 2026 | Pending |

---

## SUMMARY: KEY INVESTMENT CONSIDERATIONS

**Strengths**: Genuinely strong revenue growth (71% YoY to INR801 Cr). 28% PAT margin. Zero debt. Capital-light model. Rising health insurance adoption (4% → 26% of sales). High gross margins (89%). Growing patient volumes across all segments.

**Concerns**: 
1. Multiple guidance walk-backs (Entero, OTC product timeline, franchise model, own manufacturing)
2. Government receivables legacy (INR70 Cr+ pending, ECL provision booked)
3. Low and stagnant aggregate occupancy (57-58%)
4. Q4 showed sequential weakness (even adjusting one-offs, revenue declined from INR222 Cr Q3 to INR216 Cr Q4)
5. Management's reluctance to engage with specific numbers ("I don't know calculations")
6. Recurring "external event" excuses (war, Diwali, winter, Trump)
7. Auditor transition clean-up revealing provisioning gaps
8. Long-term targets (INR1,000 Cr PAT, INR3,000 Cr revenue) are highly ambitious and rely on unproven OTC scale-up and bed expansion that has consistently under-delivered vs promises

The core hospital/healthcare services business appears real and profitable. The OTC/products narrative remains largely aspirational. The key question is whether the FY27 INR300 Cr PAT target is achievable without the Entero distribution push that was central to the OTC thesis — and whether Ayushman Bharat actually materializes this time.
</task_result>
</task>
```

---

## Assistant (Build · DeepSeek V4 Pro · 88.8s)

_Thinking:_

Excellent! Now I have comprehensive data from all three sources:
1. Screener data (financials)
2. PPT analysis (strategy, metrics, evolution)
3. Transcript analysis (management commentary, Q&A, red flags, guidance)

Now I need to write a detailed verdict.md. Let me synthesize all this information into a comprehensive analysis. Let me write the verdict now.

All sources analyzed. Now writing the comprehensive verdict:

**Tool: write**

**Input:**
```json
{
  "filePath": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/5-July-2026/verdict.md",
  "content": "\n# Jeena Sikho Lifecare — Verdict\n\n**Date:** July 5, 2026\n\n**Market Snapshot:** CMP ₹576 | Mcap ₹7,160 Cr | P/E 32.2x | P/B 15.3x | ROE 60% | ROCE 71% | Promoter Holding 63.6%\n\n---\n\n## 1. Company Overview\n\n**Business Model:** Jeena Sikho Lifecare operates a dual-vertical Ayurveda healthcare company:\n- **Services (48% FY26 revenue: ₹387 Cr):** Ayurveda hospitals + clinics via hub-and-spoke model. Treatments span kidney disease, liver, diabetes, arthritis, and more. 61 hospitals + 58 clinics across 23 states.\n- **Products (52% FY26 revenue: ₹416 Cr):** Ayurvedic medicines sold via company centres, tele-calling, and early-stage OTC pharma. 330+ SKUs, gross margins ~89%, third-party manufactured.\n\n**Core Moats (claimed):**\n- **Capital light:** ₹3-4 lakh/bed capex vs ₹50 lakh–1 Cr for allopathy hospitals; payback <6 months\n- **Operating leverage:** High fixed-cost base, break-even at ~35% occupancy, margins expand with utilization\n- **Clinical research:** 170+ published papers — rare for Ayurveda; NABH accreditation (50 hospitals, ~9% share of NABH Panchkarma/AYUSH)\n- **First-mover advantage** in clinically-validated Ayurveda at scale; no listed Ayurveda hospital chain comparable\n\n**Reality check on moats:** The capital-light advantage is real. But \"170+ research papers\" appeared suddenly as a number across presentations (from ~17 in Aug 2025 to \"170+\" by May 2026). Low barriers to entry exist — any hospital chain could open Ayurveda wings. The real moat is the brand (HIIMS/Jeevan Shakti/Acharya Manish Ji), not the structural economics.\n\n---\n\n## 2. Financial Analysis\n\n### 2.1 Revenue Growth (Extraordinary)\n\n| Year | Revenue (₹ Cr) | YoY Growth |\n|------|---------------|------------|\n| FY21 | 136 | |\n| FY22 | 146 | +7% |\n| FY23 | 204 | +40% |\n| FY24 | 324 | +59% |\n| FY25 | 469 | +45% |\n| **FY26** | **801** | **+71%** |\n\n3Y CAGR: 58%. 5Y CAGR: 43%. TTM growth: 71% — revenue accelerated into FY26.\n\nQuarterly trajectory in FY26: ₹174 Cr → ₹190 Cr → ₹222 Cr → **₹216 Cr** (Q4 sequential decline of -3%).\n\n### 2.2 Profitability (Structural Improvement)\n\n| Metric | FY22 | FY23 | FY24 | FY25 | FY26 |\n|--------|------|------|------|------|------|\n| EBITDA Margin | 12% | 23% | 29% | 30% | **44%** |\n| PAT Margin | 8% | 16% | 21% | 17% | **28%** |\n| ROE | — | — | 49% | 46% | **60%** |\n| ROCE | — | 53% | 58% | 50% | **71%** |\n\nMargins have structurally expanded as operating leverage kicked in. FY26 EBITDA margin of 44% is exceptional. However, Q4 FY26 margin dipped to 36% — management cites ₹21 Cr of one-off provisions (labour code changes, Ind AS adjustments, ECL provision, loyalty points). Adjusted Q4 margin ~46% — in line with prior quarters.\n\n**Key margin drivers:** Employee cost dropped from 21% to 19% of revenue; rent from 7% to 6%; other opex from 15% to 9%. Ad spend grew only 14% despite 71% revenue growth — implying strong brand pull.\n\n### 2.3 Balance Sheet\n\n| Item | FY24 | FY25 | FY26 | Change |\n|------|------|------|------|--------|\n| Net Worth (₹ Cr) | 192 | 273 | **468** | +71% |\n| Borrowings (₹ Cr) | 1 | 11 | **127** | +1,155% |\n| Fixed Assets (₹ Cr) | 67 | 153 | **307** | +101% |\n| Debt/Equity | 0.01 | 0.04 | **0.27** | |\n| Cash (₹ Cr) | 62 | 23 | **15** | |\n\n**Key concern:** Borrowings surged from ₹11 Cr to ₹127 Cr. While D/E is still modest at 0.27x, the trajectory is aggressive. Fixed assets doubled to ₹307 Cr — substantial capacity build. Cash has dwindled to ₹15 Cr. Management claims \"no debt on balance sheet\" (Jun 2026 concall), but screener reports ₹127 Cr of borrowings. This needs reconciliation.\n\n### 2.4 Cash Flow\n\n| Item (₹ Cr) | FY23 | FY24 | FY25 | FY26 |\n|-------------|------|------|------|------|\n| OCF | 17 | 37 | 69 | **262** |\n| Investing | (57) | (18) | (70) | **(211)** |\n| Free Cash Flow | (13) | 23 | (40) | **231** |\n| CFO to Operating Profit | 55% | 66% | 81% | **96%** |\n\nFY26 FCF turned strongly positive at ₹231 Cr — a dramatic improvement. CFO conversion at 96% of operating profit is strong. But FY25 was deeply negative FCF (-₹40 Cr), and the FY26 investing outflow of ₹211 Cr shows the expansion is consuming significant capital.\n\n### 2.5 Working Capital\n\n| Metric (Days) | FY22 | FY23 | FY24 | FY25 | FY26 |\n|---------------|------|------|------|------|------|\n| Debtor Days | 22 | 40 | 46 | 76 | 32 |\n| Inventory Days | 136 | 87 | 121 | 135 | 80 |\n| Working Capital Days | -11 | 29 | 58 | 55 | 54 |\n| Cash Conversion Cycle | 49 | -2 | 92 | 100 | 26 |\n\nWorking capital improved dramatically in FY26. Debtor days halved from 76 to 32 — a result of the deliberate pivot away from government business (where payment cycles were 4-6 months) toward private pay (faster collections). CCC dropped from 100 to 26 days.\n\n---\n\n## 3. Quarterly Progression & Evolution\n\n### 3.1 Revenue Mix Transformation\n\n| Segment | FY25 | Q1FY26 | Q2FY26 | Q3FY26 | Q4FY26 | FY26 |\n|---------|------|--------|--------|--------|--------|------|\n| Services (Private) | 45% | 45% | 45% | 41% | 43% | ~48% |\n| Products (Medicine) | 46% | 46% | 50% | 55% | 55% | 52% |\n| Government Panel | **25%** | **9%** | **5%** | **4%** | **2%** | **4%** |\n\nGovernment revenue collapsed from ₹118 Cr (FY25) to ₹36 Cr (FY26) — an ₹82 Cr gap. This was the single biggest structural change in FY26. The pivot was forced by government payment delays (receivables peaked at ₹92 Cr), framed as \"strategic\" by management. The ₹82 Cr revenue was more than replaced by private business growth.\n\n### 3.2 Margin Trajectory (Quarterly)\n\n| Quarter | EBITDA% | PAT% | Notes |\n|---------|---------|------|-------|\n| Q1FY26 | 45% | 29% | Peak operating leverage, seasonal strength |\n| Q2FY26 | 48% | 31% | Best quarter; margin expanded further |\n| Q3FY26 | 45% | 30% | \"Weak quarter for healthcare\" per mgmt but still 45% |\n| Q4FY26 | 36% | 21% | ₹21 Cr one-offs; adjusted ~46%/27% |\n\n### 3.3 Volume Growth (Sequential)\n\n| Quarter | IPD | OPD (Lakh) | Day Care | OPD+COD+VC |\n|---------|-----|------------|----------|------------|\n| Q1FY26 | 8,616 | 1.24 | 14,828 | 2.07 Lakh |\n| Q2FY26 | 9,614 | 1.40 | 17,154 | 2.59 Lakh |\n| Q3FY26 | 11,313 | 1.57 | 18,977 | 4.34 Lakh |\n| Q4FY26 | **10,911** | 1.49 | 17,132 | **3.59 Lakh** |\n\nQ4 showed sequential volume decline across all metrics. Management blames \"Iran-America war panic\" causing advance-booked patients to defer visits and Grant Thornton's booking changes (advances no longer recognized until bill generation).\n\n### 3.4 Capacity Build\n\n| Metric | Aug'25 | Nov'25 | Feb'26 | May'26 |\n|--------|--------|--------|--------|--------|\n| Operational Beds | 2,179 | 2,220 | 2,290 | 2,300 |\n| Total Beds | 2,570 | 2,802 | 2,800 | 2,861 |\n| Hospitals | 55 | 58 | 58 | 61 |\n| Occupancy | ~53% | 57% | 58% | 56% |\n\nOccupancy stagnated between 57-58% for three consecutive quarters despite bed additions. This is a concern — if occupancy isn't rising, the operating leverage narrative weakens on marginal beds.\n\n### 3.5 ARPB Stagnation\n\nARPB (Average Revenue Per Bed per Day) has been flat at ₹8,200-8,337 across FY26 quarters. In Jun 2026, management abruptly introduced a new metric (₹4,650/bed assuming 100% occupancy), making historical comparison difficult. When pressed on why ARPOB isn't growing, management deflected.\n\n---\n\n## 4. Strategy & Growth\n\n### 4.1 Capacity Expansion\n- **FY26:** 2,300 operational beds → target 3,000-3,500 by March 2027\n- **Long-term vision:** 7,000-10,000 beds in 3-5 years\n- New hospitals in Ahmedabad, Patna, Pune, Lucknow; Manali ultra-luxury wellness centre (108 rooms, opening July 2026)\n\n### 4.2 OTC Pharma Products (unproven)\n\nThe OTC narrative has evolved but delivery is far behind promises:\n\n| Commitment | When Made | Status (Jun 2026) |\n|------------|-----------|-------------------|\n| INR 500 Cr revenue in 1.5-2 yrs | Aug 2025 | Too early to assess |\n| 6-7 products by Mar 2026 | Aug 2025 | 1 product >3 months old |\n| BP/Sugar/Kidney pills | Feb 2026 (\"this month\") | Pushed to Jun/Jul |\n| Entero distribution partnership | Nov 2025 / Feb 2026 | \"Business model didn't start\" |\n\nThe Entero walk-back is significant. The Entero deal (1.25 lakh pharmacies) was central to the OTC distribution thesis and was announced with confidence in Nov/Feb calls. By Jun 2026, management admitted Entero asked them to bear expenses and the deal stalled.\n\n### 4.3 Other Growth Initiatives\n\n- **Health Card** (Jeena Sikho Swadeshi Health Card): Launched Q4 — referral bonuses, cashback, Chandan Diagnostics tie-up for discounts. Early stage.\n- **College tie-up model:** Promised capital-light expansion (₹1-1.5 lakh/bed). 16 colleges approached in Aug 2025. Stalled at 1-3 operational by Jun 2026. Management cited NGO/trust restrictions, government NOC delays.\n- **Franchise model (FOCO):** 50 hospitals announced in Nov 2025. Walked back in Feb 2026 (\"why divide margin? We have capital.\").\n- **Own manufacturing:** Announced Aug 2025 (\"next year I will buy a large manufacturing unit\"), repeated Feb 2026. Not mentioned in Jun 2026.\n- **International:** Dubai plans scaled down from \"2 hospitals\" (Aug) to \"2 daycare centers\" (Nov) to \"4 being built\" (Feb). Nepal, Kazakhstan, Abu Dhabi also mentioned.\n- **Ayushman Bharat inclusion:** Mentioned every single concall as \"any day now.\" Draft at ₹8,800-9,400/day reached ministry. No inclusion yet.\n\n### 4.4 CEO/Professional Management\nCEO hiring was promised in 2024, still searching by Jun 2026. COO promoted internally. Manish Grover (Acharya Manish Ji) is MD and the face of the company — founder-led, deeply dependent on him.\n\n---\n\n## 5. Management Quality\n\n### 5.1 Strengths\n- **Founder conviction:** Manish Grover is the driving force. He's built a ₹800 Cr company from scratch in Ayurveda — a rare achievement.\n- **Execution:** Revenue CAGR of 58% over 3 years speaks for itself. FY26 revenue of ₹801 Cr beat the ₹700 Cr guidance.\n- **Willingness to pivot:** Moved decisively away from government business when payments stalled — a hard but correct decision.\n\n### 5.2 Red Flags\n- **Repeated walk-backs:** Entero deal, OTC product timelines, franchise model, college tie-ups, own manufacturing. Too many commitments made with confidence and then abandoned or delayed without clear acknowledgment.\n- **\"I don't know calculations\":** Manish repeatedly deflects analyst questions on numbers, saying \"I don't pay attention to numbers\" and directing to CFO. For a public company MD, this is unusual.\n- **External blame pattern:** \"Weak Q3\" (Diwali/winter), \"Weak Q4\" (Iran-America war panic), product launch delays (war), Entero deal failure (Entero wanted us to pay). A pattern of attributing shortfalls to uncontrollable events.\n- **Aggressive guidance:** INR 1,000 Cr PAT in 3-5 years implies 4.5x growth from ₹222 Cr. INR 3,000 Cr revenue in 3-5 years implies 3.75x from ₹801 Cr. These are not conservative targets.\n- **Government receivables legacy:** ₹92 Cr peak receivables from government — never fully explained how much was lost vs recovered.\n- **Cash dwindling:** ₹62 Cr (FY24) → ₹23 Cr (FY25) → ₹15 Cr (FY26). With ₹127 Cr borrowings, the balance sheet has changed character significantly in one year.\n\n### 5.3 Auditor Changes\nGrant Thornton replaced as statutory auditor in Q2 FY26. Forvis Mazars added as internal auditor. Deepak K Garg removed as internal auditor. Auditor transitions can be benign, but in the context of other red flags, it warrants monitoring.\n\n---\n\n## 6. Risks\n\n### 6.1 Business Risks\n- **Low barriers to entry:** Any hospital chain (Apollo, Max, Fortis) can set up Ayurveda wings. No structural moat beyond brand and first-mover status.\n- **Insurance adoption risk:** 4% → 26% of sales from insurance is positive, but insurance companies may reduce rates or place caps on Ayurveda treatments as the category grows.\n- **Concentration risk:** Dependent on kidney/liver treatment reputation. Any adverse medical outcome or regulatory crackdown on claims could impact brand.\n- **Geography concentration:** UP (12 hospitals), Rajasthan (10), Haryana (6) — heavy north India concentration.\n\n### 6.2 Financial Risks\n- **Surging borrowings:** ₹127 Cr debt (from ₹1 Cr in FY24) with ₹15 Cr cash. D/E 0.27x is manageable, but trajectory matters (doubled in one year).\n- **FCF sustainability:** FY26 FCF was ₹231 Cr, but FY25 was -₹40 Cr. The ₹211 Cr investing outflow implies heavy capex commitment that may outstrip OCF in weaker years.\n- **One-off provisioning:** ₹21 Cr in Q4 alone. If these recur (management admitted lease impact \"will gradually decrease\" — i.e., not purely one-time), margins may compress.\n\n### 6.3 Execution Risks\n- **OTC products unproven:** 9 products launched but only 1 has been on market >3 months. Entero distribution deal collapsed. Revenue from OTC is negligible vs the INR 500 Cr target.\n- **Capacity absorption:** 2,300 operational beds at 56% occupancy. Adding 1,200+ more beds (target 3,500) without diluting occupancy is unproven.\n- **Talent availability:** Can they hire enough Ayurveda doctors, therapists, and support staff for 3,500+ beds? Manish acknowledged this constraint in concalls.\n\n### 6.4 Regulatory / External Risks\n- **Government payment risk:** INR 70 Cr+ recoverable from government — already booked INR 5 Cr ECL provision. More write-offs possible.\n- **Ayushman Bharat risks:** Even if included, reimbursement rates may be lower than private rates, compressing margins on that segment.\n\n---\n\n## 7. Valuation Context\n\n### 7.1 Current Multiples\n\n| Metric | Value |\n|--------|-------|\n| P/E (TTM) | 32.2x |\n| P/B | 15.3x |\n| EV/EBITDA | 20.0x |\n| Market Cap / FCF | 31.0x |\n\n### 7.2 Peer Comparison\n\nJeena Sikho is the ONLY profitable company in its screener.in peer group (wellness/leisure services). Kaya Ltd (EV/EBITDA -44x) and Lloyds Luxuries (EV/EBITDA 135x) are loss-making. This makes traditional peer P/E comparison meaningless.\n\n### 7.3 Growth-Adjusted Valuation\n\nAt P/E 32.2x with 3Y EPS CAGR of 88%: PEG ratio = 0.37 — appears cheap on a growth-adjusted basis. But this rests entirely on sustaining growth rates that are already showing signs of deceleration (QoQ revenue decline in Q4, occupancy stagnation).\n\n### 7.4 Scenario Analysis\n\n**Bull case (₹1,000 Cr PAT by FY29):**\n- Revenue: ₹3,000 Cr (3.75x from FY26, ~39% CAGR)\n- PAT margin: ~30-33%\n- At P/E 25-30x: Mcap ₹25,000-30,000 Cr (~3.5-4x from current ₹7,160 Cr)\n- Requires OTC products to contribute ₹500 Cr+, beds to reach 7,000+, occupancy to improve to 65%+\n\n**Base case (₹600 Cr PAT by FY29):**\n- Revenue: ₹2,000 Cr (~26% CAGR)\n- PAT margin: 28-30%\n- At P/E 22-25x: Mcap ₹13,200-15,000 Cr (~1.8-2.1x)\n- Requires occupancy improvement to 60%+, modest OTC contribution\n\n**Bear case (₹350 Cr PAT by FY29):**\n- Revenue: ₹1,500 Cr (~17% CAGR)\n- PAT margin: 22-25% (margin compression from competition/costs)\n- At P/E 15-20x: Mcap ₹5,250-7,000 Cr (-2% to -26% from current)\n- Requirements: No OTC breakthrough, occupancy stuck at 55-58%, government receivables write-offs\n\n---\n\n## 8. Key Monitorables for FY27\n\n1. **FY27 PAT:** Can they deliver the \"minimum ₹300 Cr\" PAT target? This implies ~35% growth on an adjusted base (after stripping one-offs). Q1FY27 will be the first test.\n\n2. **Occupancy rate:** Must cross 60%+ on the expanded bed base. If it stays at 56-58% as they add 1,000+ more beds, the operating leverage thesis breaks.\n\n3. **OTC product traction:** Need to see at least 2-3 products with meaningful revenue (>₹50 Cr each). Entero deal needs resolution — either revived or replaced with an alternative distribution channel.\n\n4. **Auditor sign-off:** First full-year audit under Grant Thornton. Watch for any qualifications, provisions, or adjustments.\n\n5. **Government receivable resolution:** Remaining ₹70 Cr+ from government panels — how much is recovered vs written off.\n\n6. **Debt trajectory:** Borrowings at ₹127 Cr and rising. Need to see debt stabilize or reduce as a percentage of net worth.\n\n7. **Ayushman Bharat inclusion:** If the \"any day now\" actually happens, it could be a significant volume catalyst (management claims ability to add 2,000 beds immediately).\n\n8. **Q1FY27 seasonal pattern:** Q1 has historically been the strongest quarter. If Q1FY27 doesn't show sequential growth over Q3FY26 levels (₹222 Cr), the growth momentum may be stalling.\n\n---\n\n## 9. Conclusion\n\nJeena Sikho is a genuinely high-growth, high-return business in a niche space — clinically-validated Ayurveda healthcare at scale. The financials are exceptional: 71% revenue growth, 44% EBITDA margins, 60% ROE, 71% ROCE, and positive FCF of ₹231 Cr. No listed peer exists with comparable scale and profitability in Ayurveda.\n\nHowever, there are meaningful concerns:\n\n1. **The guidance walk-back pattern.** Entero, OTC product timelines, franchise model, college tie-ups, own manufacturing — too many commitments have been abandoned or delayed without clear accountability.\n\n2. **Q4 sequential weakness warrants caution.** Even after adjusting one-offs, revenue declined QoQ and volumes dropped across all operating metrics. If Q1FY27 doesn't rebound, the growth narrative is at risk.\n\n3. **Management communication style.** The tendency to deflect quantitative questions (\"I don't know calculations\"), attribute shortfalls to external events, and escalate guidance without delivery track record on earlier promises is a concern for minority shareholders.\n\n4. **Balance sheet transformation.** The move from debt-free (₹1 Cr borrowings FY24) to ₹127 Cr debt with ₹15 Cr cash is a material shift that hasn't been well-explained.\n\n5. **OTC thesis is unproven.** The product business within the hospital ecosystem (416 Cr in FY26) is real and profitable. But the ₹500 Cr OTC pharma revenue target relies on a distribution model that has already failed once (Entero).\n\nAt P/E 32.2x, the stock prices in significant growth but is not exorbitant for a business with 28% FY26 PAT margins and 58% 3Y revenue CAGR. However, the combination of aggressive long-term guidance, repeated walk-backs, and Q4FY26 sequential weakness suggests the next 1-2 quarters are critical.\n\n**Verdict: WATCH CLOSELY — POSITIVE BIAS BUT AWAIT Q1FY27 CONFIRMATION.** The core hospital/services business is real, highly profitable, and growing. But the company has over-promised and under-delivered on every growth initiative outside the core. Wait for Q1FY27 numbers to confirm that FY26 Q4 was indeed a one-off blip, and that the ₹300 Cr PAT target for FY27 is on track, before committing capital.\n"
}
```

**Output:**
```
Wrote file successfully.
```

---

## Assistant (Build · DeepSeek V4 Pro · 4.4s)

_Thinking:_

The verdict has been written. Let me update the todo list and provide a summary to the user.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Step 1: Download documents (PPTs & transcripts) from screener",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Step 2: Analyze PPTs with vision model",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Step 3: Read all sources and write verdict.md",
      "priority": "high",
      "status": "completed"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Step 1: Download documents (PPTs & transcripts) from screener",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Step 2: Analyze PPTs with vision model",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Step 3: Read all sources and write verdict.md",
    "status": "completed",
    "priority": "high"
  }
]
```

---

## Assistant (Build · DeepSeek V4 Pro · 5.6s)

Analysis complete. **verdict.md** written to `JEENA_SIKHO_LIFECARE/5-July-2026/verdict.md`.

**TL;DR verdict: WATCH CLOSELY — POSITIVE BIAS BUT AWAIT Q1FY27 CONFIRMATION.**

**The good:** Exceptional financials — ₹801 Cr revenue (+71% YoY), 44% EBITDA margin, 60% ROE, ₹231 Cr FCF. No listed Ayurveda peer at this scale. Core hospital/services business is real and profitable.

**The concerning:** Multiple guidance walk-backs (Entero deal collapsed, OTC products delayed, franchise model abandoned). Q4 FY26 showed sequential revenue decline and volume drops despite management downplaying it. Borrowings surged from ₹1 Cr to ₹127 Cr in one year. INR 1,000 Cr PAT target in 3-5 years is aggressive given track record of missing non-core promises.

**Key trigger:** Q1FY27 numbers — need to see rebound above Q3FY26 levels (₹222 Cr revenue) to confirm Q4 was a one-off.

---

## User

/rename JEENA_SIKHO_LIFECARE

---

## Assistant (Build · DeepSeek V4 Pro · 2.8s)

---

## User

okay let's discuss the business in simple words. 
what are some of the interesting pivots that the company has taken over the years, and are they successfull in delivering their past guidance? 

---

## Assistant (Build · DeepSeek V4 Pro · 24.4s)

_Thinking:_

The user wants me to discuss the business in simple terms, focusing on:

1. Interesting pivots the company has taken over the years
2. Whether they've been successful in delivering past guidance

I already have all the data from the previous analysis - the PPTs, transcripts, and financial data. Let me synthesize this into a clear, simple discussion without needing to read files again.

Let me think about the key pivots from the data I already have:

1. **From small to scaled**: Revenue grew from ₹146 Cr (FY22) to ₹801 Cr (FY26)
2. **Government to Private pivot**: Govt revenue went from 25% of total (₹118 Cr in FY25) to 4% (₹36 Cr in FY26) - forced by payment delays
3. **Services-led to Products-led**: Products revenue jumped from ₹215 Cr (FY25) to ₹416 Cr (FY26), overtaking services
4. **Pure hospital to OTC pharma ambition**: Launched 9 OTC products
5. **Own expansion to franchise/college model (abandoned)**: Announced 50 franchise hospitals, then walked it back
6. **Entero distribution deal (failed)**: Big partnership announced, then "business model didn't start"
7. **International expansion**: Dubai plans scaled down from hospitals to daycare centers
8. **Health Card / loyalty program**

On guidance delivery:
- FY26 revenue: Guided ₹700 Cr, delivered ₹801 Cr (beat)
- FY26 PAT: Implied ~₹140 Cr, delivered ₹222 Cr (massively beat)
- But on non-core initiatives, they've consistently overpromised and underdelivered

Let me write this up simply.

## Jeena Sikho Lifecare — Business in Simple Terms

### What They Do

You run hospitals and clinics that treat chronic diseases (kidney, liver, diabetes, arthritis) using Ayurveda — not allopathy. You also sell your own line of Ayurvedic medicines. Think of it like a hospital chain meets pharma company, but all in the Ayurveda space.

Revenue FY26: ₹801 Cr (Services 48%, Products 52%). Profit: ₹222 Cr. No listed peer exists at this scale in Ayurveda.

---

### The Major Pivots

**1. Government → Private Pay (Q4 FY25 to Q1 FY26)**

This was the biggest pivot, and not by choice. They used to get 25% of revenue (₹118 Cr) from government health panels. But the government stopped paying on time — receivables piled up to ₹92 Cr. Manish wrote a letter saying "fix payments or we stop," and then actually stopped. Govt revenue collapsed to ₹36 Cr (4%).

**Verdict: Successful.** They replaced the ₹82 Cr gap with private business growth. Cash conversion actually improved (debtor days halved from 76 to 32) because private patients pay upfront. This was the right call executed well.

**2. Hospital Operator → Pharma Distributor Ambition (Aug 2025 → ongoing)**

They sell medicines within their own hospitals (₹416 Cr in FY26, 52% of revenue). That works. But they announced a plan to sell Ayurvedic drugs through third-party pharmacies — the Entero tie-up (1.25 lakh pharmacy outlets) — with a target of ₹500 Cr in OTC revenue.

**Verdict: Failed so far.** Entero deal collapsed — Entero wanted JSLL to bear expenses, JSLL refused. Only 1 of the promised 6-7 OTC products is more than 3 months old. The ₹500 Cr target looks aspirational.

**3. Own Expansion → Franchise Model → Back to Own (Aug → Feb 2026)**

Nov 2025 concall: "We're launching 50 franchise hospitals." Feb 2026 concall: "Why divide margin? We have capital now." Brand-new strategy announced and killed within 3 months.

**Verdict: Incoherent strategic planning.** This is a red flag — you don't announce 50 franchise hospitals and walk it back in 90 days without a good explanation.

**4. Small Hospitals → Ultra-Luxury Wellness (Jun 2026)**

They're building a 108-room luxury wellness centre in Manali (opening July 2026). This is a completely different customer segment — wealthy lifestyle/wellness tourists, not chronic disease patients. Untested.

---

### Guidance Track Record

| What They Said | When | Reality |
|---|---|---|
| FY26 revenue: ₹700 Cr | Aug 2025 | **Beat: ₹801 Cr** |
| FY26 PAT: ~₹140 Cr implied | Aug 2025 | **Massive beat: ₹222 Cr** |
| 6-7 OTC products by Mar 2026 | Aug 2025 | **Miss: 1 product >3 months old** |
| Entero pharmacy partnership | Nov 2025 | **Failed: deal didn't start** |
| "Next year I will buy a large manufacturing unit" | Aug 2025 | **Not mentioned 12 months later** |
| 50 franchise hospitals | Nov 2025 | **Walked back by Feb 2026** |
| "I have 16 colleges ready to work with us" | Aug 2025 | **1-3 operational, rest stalled** |
| 2,850-3,000 ops beds by Mar 2026 | Aug 2025 | **Partial: 2,800 total beds but only 2,300 operational** |
| CEO hire | 2024 promise | **Still searching Jun 2026** |

**Pattern**: On core financial targets (revenue, profit), they've actually beaten guidance. On growth initiatives outside the core hospital business, they consistently overpromise and underdeliver.

---

### Bottom Line

The core business is a genuine success story — you can't fake 71% revenue growth and 44% EBITDA margins on ₹801 Cr. The hospital model works, and the pivot away from government business was disciplined.

But every "next big thing" they've announced — OTC drugs, franchise expansion, college tie-ups, manufacturing, international — has either stalled, failed, or been walked back. The FY27 target of ₹300 Cr PAT (+35%) can be met from the core hospital business alone if they execute. The ₹1,000 Cr/₹3,000 Cr long-term vision depends on growth initiatives that haven't worked yet.

---

## User

what's the revenue splits across their different businesses. mention upcoming business segments also (with estimated guidance). 
and tell me margins of each different business segments. 

---

## Assistant (Build · DeepSeek V4 Pro · 41.3s)

_Thinking:_

The user wants to know the revenue splits across different business segments and margins for each. Let me look at what I already have from the analysis.

From the PPT and screener data:

**Services (Healthcare)**:
- FY25: ₹254 Cr (54% of revenue)
- FY26: ₹387 Cr (48% of revenue)
- Within Services: Private Panchkarma, Government Panchkarma

**Products (Medicine)**:
- FY25: ₹215 Cr (46% of revenue)  
- FY26: ₹416 Cr (52% of revenue)
- Within Products: Sold through company centres, tele-calling, e-com, and early OTC

**Government Panel**:
- FY25: ₹118 Cr (25% of total revenue)
- FY26: ₹36 Cr (4% of total revenue) — collapsed

Margins were discussed in the concall transcript:
- Products (Medicine): Gross margin ~89% (was 91% pre-Ind AS)
- Services: Need to look at what was mentioned
- OTC: 20% PAT margin (after 45% trade discounts)
- Government vs Private: Private Panchkarma has better margins

Let me also think about what guidance was given for upcoming segments:
- OTC Pharma: ₹500 Cr in 1.5-2 years (Aug 2025), later framed as ₹300-500 Cr
- Long-term: ₹3,000 Cr revenue in 3-5 years (Jun 2026), split ~50/50 services/products
- Insurance within services: 4% → 26% of sales
- Health Card: Early stage
- International: UAE, Kazakhstan, Nepal - no revenue guidance given
- Wellness/Luxury: Manali centre - no guidance

Let me also check if there's more detail I should pull from the sources. Let me re-read the key sections about margins from the transcript analysis.

From transcript analysis:
- Products: Gross margin 85%+ (89% in FY26). Third-party manufactured. 
- Services: Direct costs for services are 9% (consumption)
- OTC: PAT margin 18-22% (Nov 2025), 20-25% (Feb 2026), "20% PAT" (Aug 2025, after 45% trade discounts)
- Govt rate: ₹8,000/day per bed
- Insurance rate: ₹8,800-9,200/day
- Overall company EBITDA margin: 44% (FY26)
- Direct cost: 11% of revenue (FY26), down from 12% (FY25)
- Manpower: 19% of revenue
- Rent: 6%
- Other opex: 9%
- Ad spend: ₹66 Cr (FY26), ~8% of revenue

Let me present this clearly. But the user is asking for more detail than I have readily available in the summary. Let me look at the actual PPT files to get exact segment margin details if available.

Actually, I have quite comprehensive data already. Let me look at what margins were specifically mentioned:

From PPT data:
- Products: ~85-89% gross margins, outsourced manufacturing
- Government Panchkarma: Government reimburses at ~₹8,000/day
- Private Panchkarma: Better margins than government

From Transcript:
- Products gross margin: 89% FY26 (was 91% pre-Ind AS)
- Direct material cost (products): 15% of medicine revenue in Aug, 11% overall in FY26
- Services direct cost: 9% (consumption)

I think I have enough to give a good answer. Let me structure this clearly.

Key segments:
1. **Private Panchkarma (Services)** - ₹387 Cr FY26 (48%)
2. **Medicine/Products** - ₹416 Cr FY26 (52%)
   - a) In-house (sold at own centres, tele-calling) - bulk of products
   - b) OTC Pharma (early stage) - negligible currently
3. **Government Panchkarma** - ₹36 Cr FY26 (4%) — declining

Upcoming:
4. OTC Pharma - ₹500 Cr target
5. Insurance - growing within Private Panchkarma
6. Health Card - too early
7. International - too early
8. Ultra-luxury wellness - Manali, Panchkula

Let me present this clearly.

## Jeena Sikho — Revenue Splits & Margins

### Current Business Segments (FY26: ₹801 Cr)

#### 1. Private Panchkarma Services — ₹351 Cr (44%)

Ayurveda hospital stays, daycare, OPD consultations. Patients pay out of pocket or via insurance.

| Metric | Value |
|---|---|
| Gross margin | ~91% (only 9% direct consumption cost) |
| Realization | ₹8,300/bed/day (ARPB) |
| Payback (new 100-bed facility) | <6 months |
| Insurance penetration | 4% → 26% of service sales in FY26 |

The money-making engine. Highly profitable, cash-upfront, operating leverage kicks in at ~35% occupancy.

#### 2. Medicine/Products — ₹416 Cr (52%)

Ayurvedic medicines (330+ SKUs) sold through own centres, tele-calling, and early-stage e-commerce. Third-party manufactured — they don't make it themselves.

| Metric | Value |
|---|---|
| Gross margin | **89%** (FY26; was 91% pre-Ind AS) |
| Direct cost | ~11% of product revenue |
| Manufacturing | Fully outsourced |

This is effectively "retail" margin on someone else's manufacturing. The product gets prescribed at their own hospitals and patients continue buying on auto-refill.

#### 3. Government Panchkarma — ₹36 Cr (4%)

Treating government panel patients at fixed rates.

| Metric | Value |
|---|---|
| Realization | ~₹8,000/bed/day |
| Payment cycle | 4-6 months (when they paid at all) |
| Gross margin | Lower than private (govt rate is fixed, costs same) |
| FY25 comparison | Was ₹118 Cr (25% of revenue) — collapsed 70% |

Deliberately wound down. ₹70 Cr+ still stuck in receivables, ₹5 Cr already provisioned as doubtful.

---

### Segment Margin Summary

| Segment | Revenue (FY26) | Gross Margin | Key Cost |
|---|---|---|---|
| Private Panchkarma | ₹351 Cr (44%) | ~91% | 9% consumables |
| Medicine/Products | ₹416 Cr (52%) | ~89% | 11% third-party manufacturing |
| Govt Panchkarma | ₹36 Cr (4%) | Lower than private | Same costs, fixed govt rates |

**Overall EBITDA margin: 44%** built on: manpower 19%, rent 6%, other opex 9%, ad spend 8%, depreciation 6%, finance 1.6%.

---

### Upcoming Business Segments

#### 1. OTC Pharma — Target: ₹500 Cr (no timeline anymore)

Selling Ayurvedic drugs through third-party pharmacies (not just their own hospitals).

| What | Detail |
|---|---|
| Target | ₹500 Cr in 1.5-2 years (Aug 2025 promise) |
| Status | **9 products launched, only 1 >3 months old** |
| PAT margin target | **18-25%** (after 45% trade discount to pharmacies) |
| Key enabler (failed) | Entero tie-up with 1.25 lakh pharmacies — collapsed |
| Current revenue | Negligible / not separately disclosed |

The big "next growth engine" on paper. But the distribution deal that was supposed to make it work has already failed once. Without a pharmacy distribution partner, these products stay confined to their own hospital ecosystem — which is the ₹416 Cr they already have.

#### 2. Insurance-Paid Services — Growing within Private Panchkarma

| What | Detail |
|---|---|
| Current share | 26% of service revenue (up from 4%) |
| Realization | ₹8,800-9,200/day (higher than govt rate) |
| Growth driver | More insurers adding Ayurveda coverage |

This is growing organically as more insurance companies reimburse Ayurveda. It's essentially the same service delivered to a different payer — same margins, better than government.

#### 3. Ayushman Bharat (Government Scheme) — Target: "2,000 beds overnight"

| What | Detail |
|---|---|
| Status | Draft at ₹8,800-9,400/day; "any day now" across 4 concalls |
| Potential | Management claims they can deploy 2,000 additional beds immediately |
| Risk | If it mirrors the old govt panel (payment delays), it's more trouble than it's worth |

Has been dangled as a catalyst for 12+ months. No inclusion yet.

#### 4. International — UAE, Kazakhstan, Nepal

| What | Detail |
|---|---|
| Status | Dubai: scaled down from "2 hospitals" → "2 daycare centres" → "4 being built" |
| Revenue guidance | None given |
| Margins | Unknown — entirely different regulatory/operating environment |

Meaningful revenue unlikely in the next 2 years. More of a narrative element.

#### 5. Ultra-Luxury Wellness — Manali (July 2026), Panchkula

| What | Detail |
|---|---|
| Manali | 108-room luxury wellness resort |
| Target customer | Wealthy lifestyle/wellness tourists |
| Revenue guidance | None given |
| Margins | Likely high (luxury pricing) but unknown occupancy dynamics |

This is a pivot into lifestyle hospitality, not chronic disease treatment. Completely new customer segment.

#### 6. Health Card (Jeena Sikho Swadeshi Health Card)

| What | Detail |
|---|---|
| Status | Launched Q4 FY26 |
| Model | Referral bonuses, cashback, diagnostic discounts via Chandan Diagnostics tie-up |
| Revenue | Nil currently — loyalty/referral tool, not a direct revenue line |

A loyalty program dressed up as a "health card." Potentially useful for patient stickiness but not a revenue segment.

---

### The Real Picture

The entire ₹801 Cr comes from two things: treating patients in their own hospitals, and selling them medicines. That's it. Everything else is aspiration.

The long-term vision (₹3,000 Cr revenue, ₹1,000 Cr PAT) requires OTC pharma to contribute ₹500 Cr+, international to become real, and Ayushman Bharat to actually happen. At this point, only the core hospital + medicine business has been proven.

---

## User

Interesting point. 
let

---

## Assistant (Plan · DeepSeek V4 Pro · 1.8s)

---

## User

Interesting points. 
what reason did management give for entero tie-up collapsing. 

---

## Assistant (Plan · DeepSeek V4 Pro · 9.0s)

_Thinking:_

The user wants to know what reason management gave for the Enteero tie-up collapsing. Let me look at the transcript data I already have from the task agent's analysis. I recall from the transcript analysis:

"Entero deal admission: "The tie-up was done, but the business model didn't start because Entero was asking us to bear the expenses." (Jun 2026) — a significant walk-back from the Feb 2026 enthusiasm."

Let me read the actual transcript to get the exact quote and context.

Let me pull the exact management quote from the Jun 2026 transcript.

**Tool: grep**

**Input:**
```json
{
  "pattern": "Entero|entero",
  "include": "Transcript_Jun2026.txt",
  "path": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall"
}
```

**Output:**
```
Found 3 matches
/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Jun2026.txt:
  Line 333: but last time we spoke, you said the tie-up with Entero was done and our medicines would be 

  Line 337: Sir, actually, the tie-up with Entero was done, but the business model didn't start because Entero 

  Line 1030: engagement with Satkartar, Chandan, and then Entero? Any latest data you want to share with 

```

**Tool: grep**

**Input:**
```json
{
  "pattern": "Entero|entero",
  "include": "Transcript_Feb2026.txt",
  "path": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall"
}
```

**Output:**
```
Found 10 matches
/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Feb2026.txt:
  Line 487: an exclusive agreement with a B2B distributor, with Entero, for Ayurveda, so what about 

  Line 490: We finalized the agreement with Entero last week. 

  Line 496: people like Entero; Entero has a 10% share of all medical stores in India, and we have become 

  Line 514: Yes. Yes, I was asking about Entero first. 

  Line 733: join with Entero, that number will straightaway reach 1 lakh, goods will start being sent to 

  Line 734: Entero in the next 15 days or so. 

  Line 738: So they have 1.25 lakh stores -- the reason it took so long with Entero was because our rate 

  Line 1056: thing, deal with Entero. Our job is not to open stores, not to retail. Our job is to sell medicine 

  Line 1391: Good, congratulations. This is the Entero partnership, right? 

  Line 1393: Thank you. I'll tell the name. Entero. 1.25 Lakh distributor network is theirs. And in India total 

```

**Tool: grep**

**Input:**
```json
{
  "pattern": "Entero|entero",
  "include": "Transcript_Nov2025.txt",
  "path": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall"
}
```

**Output:**
```
Found 2 matches
/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Nov2025.txt:
  Line 1198: Entero. Entero is a listed company. They have one lakh pharmacies in India. Entero is a tech-

  Line 1204: by Entero. The acquisition cost to bring customer, we will transfer it to Entero. 

```

---

## Assistant (Plan · DeepSeek V4 Pro · 4.3s)

_Thinking:_

Let me read the exact quotes from the Jun 2026 and Feb 2026 transcripts to get the full context.

**Tool: read**

**Input:**
```json
{
  "filePath": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Jun2026.txt",
  "offset": 330,
  "limit": 50
}
```

**Output:**
```
<path>/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Jun2026.txt</path>
<type>file</type>
<content>
330: Akshay: 
331: Right, sir. And sir, the second thing is that our medicine sales in the last quarter were INR121 
332: crores, and this quarter they are INR118 crores, meaning a decline of INR3 crores. It's not much, 
333: but last time we spoke, you said the tie-up with Entero was done and our medicines would be 
334: available in medical stores. So, what can we expect now? Will sales growth start from this 
335: quarter in the products business? 
336: Manish Grover: 
337: Sir, actually, the tie-up with Entero was done, but the business model didn't start because Entero 
338: was asking us to bear the expenses. So, we have now increased our presence in newspapers, 
339: social media, and TV. We have also launched new products this month – 2 products in May. 
340:  
341: You will 100% see the impact of that in the next 2 to 4 months. The commitments we made in 
342: previous con calls about future numbers and profits remain as they are; we have no problem of 
343: any kind. In such a large business with an INR800 crores turnover, seeing INR2 crores to INR4 
344: crores up or down quarter-on-quarter doesn't matter to us. We are long-distance runners; we 
345: have to go further. We see INR3000 crores in sales in the next 3 to 5 years, so why would we 
346: focus on INR2 crores to INR4 crores? 
347: Akshay: 
348: Okay, understood. 
349: Manish Grover:  
350: What happens quarter-on-quarter is that when our auditors changed and GT came in, previously 
351: when we closed the financial year quarter, we used to book our advances as well. But GT said 
352: in our practices that you should only book the patient once the bill is generated and they leave. 
353:  
354: Otherwise, my fourth quarter is INR6 crores higher than the third quarter in terms of collections. 
355: But that sale was booked in the third quarter because the fourth quarter advance was booked 
356: then. In the fourth quarter, this practice was stopped. Otherwise, my fourth quarter would also 
357: have been INR9 crores higher. 
358:  
359: Even now, as of May 31st, I have an INR8 crores advance, but that is now carried forward to 
360: June because we don't book advances anymore. Sir, when we bring in a large auditor, we have 
361: to change our practices as they guide. 
362:  
363:  
364: Jeena Sikho Lifecare Limited
365:  
366:  
367: June 02, 2026 
368:  
369: Page 7 of 23 
370:  
371: Akshay: 
372: Okay. And sir last question. 
373: Moderator: 
374: I'm sorry to interrupt, Akshay. You may please rejoin the queue for more questions. 
375: Akshay: 
376: Okay, thank you. 
377: Moderator: 
378: Thank you. We will take our next question from the line of Ankur from Genuity Capital. Please 
379: go ahead. Ankur your line is unmuted you may please go ahead with your question. 

(Showing lines 330-379 of 1257. Use offset=380 to continue.)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Feb2026.txt",
  "offset": 485,
  "limit": 60
}
```

**Output:**
```
<path>/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Feb2026.txt</path>
<type>file</type>
<content>
485: Akhilesh Rawat: 
486: My second question is actually—you mentioned in the last quarter that we were going to make 
487: an exclusive agreement with a B2B distributor, with Entero, for Ayurveda, so what about 
488: that... 
489: Manish Grover: 
490: We finalized the agreement with Entero last week. 
491: Akhilesh Rawat: 
492: What impact are you seeing from that on our revenue? Like... 
493: Manish Grover: 
494: Sir, I'll give you a figure: there are 9 lakh medical stores in India, 9 lakh chemists. And I want 
495: to enter the OTC market. Now, how do I reach those 9 lakh chemists? So I contracted with 
496: people like Entero; Entero has a 10% share of all medical stores in India, and we have become 
497: their exclusive Ayurveda partner. 
498:  
499: This means if they need anything in Ayurveda now, they will demand it from us, and we will 
500: develop the product for them. Yes. Like BP pills, diabetes pills, besides that, medicines for 
501: depression and anxiety—we will provide all that to them. We have already started giving them 
502: the Stomach-Liver-Spleen Purification Kit. 
503:  
504: And this month, we'll launch our first product for nutritional deficiency in India, called 'Nutri-
505: Roz', right in this month of February, and that will be our second OTC product. After that, 
506: products will come in quick succession because once our network is created, as sales increase, 
507: I will bring the third, fourth, and fifth products. 
508: Akhilesh Rawat: 
509: So currently we have only given them the Stomach-Liver-Spleen Purification Kit. 
510: Manish Grover: 
511: Right now there is one in OTC; we have 300 products in total, which sell both online and 
512: offline. 
513: Akhilesh Rawat: 
514: Yes. Yes, I was asking about Entero first. 
515: Manish Grover: 
516: At the medical store, only the 'Stomach-Liver-Spleen Purification Kit' is available, and I also 
517: said you all can call or message the number and I will have it sent to you. 
518: Akhilesh Rawat: 
519: Yes, yes. Yes. sir, I had one final question, a final question—like now regarding our -- as we 
520: saw that this quarter we achieved a very good EBITDA margin, you gave a guidance last time 
521: that we are targeting around 20% to 25%, so are you still sticking with that guidance or would 
522: you like to improve it a bit? 
523:  
524:  
525: Jeena Sikho Lifecare Limited
526:  
527:  
528: February 09, 2026 
529:  
530: Page 10 of 28 
531:  
532: Manish Grover: 
533: That is our margin; that is what should be maintained, and if it comes in higher, it's God's 
534: grace. Yes sir, thank you sir, thanks. We will put full effort into maintaining it. And we've 
535: been showing it to you for three quarters now, sir. 
536: Moderator: 
537: Thank you. We have the next question from the line of Shubhanu from Three Head Capital. 
538: Please go ahead. 
539: Shubhanu: 
540: Sir, you said that in Q3 we didn't increase operational beds due to weak season. But from Q1 
541: to Q2 also we only increased operational beds by 60. Like from 2179 beds to 2220 beds in Q2. 
542: And that's why our operational occupancy is also very low. And in the last call, you said you 
543: would focus a lot on increasing occupancy. How do we see occupancy at the end of this year? 
544: Manish Grover: 

(Showing lines 485-544 of 1535. Use offset=545 to continue.)
</content>
```

---

## Assistant (Plan · DeepSeek V4 Pro · 10.2s)

_Thinking:_

Now I have the full context. Here's the summary of what management said about the Entero collapse:

In Feb 2026: "We finalized the agreement with Entero last week... Entero has a 10% share of all medical stores in India, and we have become their exclusive Ayurveda partner... goods will start being sent to Entero in the next 15 days or so."

In Jun 2026: "Sir, actually, the tie-up with Entero was done, but the business model didn't start because Entero was asking us to bear the expenses."

That's the full picture. Management gave one reason: Entero wanted JSLL to bear the expenses, and JSLL refused. The question is what "expenses" means — likely trade discounts, marketing spend, or shelf-space costs that JSLL wasn't willing to pay. Instead they're going direct via newspapers, social media, and TV advertising.

The exact reason, in Manish Grover's own words from the Jun 2026 concall:

> *"Sir, actually, the tie-up with Entero was done, but the business model didn't start because Entero was asking us to bear the expenses."*

That's it. One line. No elaboration on what "expenses" meant — likely trade margins, shelf-space fees, or marketing costs that Entero wanted JSLL to cover.

**The context makes it worse.** Just 3 months earlier (Feb 2026 concall), he was saying:

> *"We finalized the agreement with Entero last week... Entero has a 10% share of all medical stores in India, and we have become their exclusive Ayurveda partner... goods will start being sent to Entero in the next 15 days."*

So the narrative went from "agreement signed, goods shipping in 15 days" to "business model didn't start, they wanted us to pay" with zero acknowledgment that the earlier statement was misleading. His alternative plan? Direct-to-consumer ads in newspapers, social media, and TV — a fundamentally different distribution strategy.

This is one of the clearer red flags. Either the deal was never properly finalized (and he overstated it in Feb), or the economics didn't work and he walked away — but in either case, the OTC thesis hinged on this distribution partner and he hasn't articulated a credible replacement.

---

## User

did management give any reason for recent march-2026 quarter numbers? was the result in line with expectation or not? 

---

## Assistant (Plan · DeepSeek V4 Pro · 24.5s)

_Thinking:_

The user is asking two questions about the Q4 FY26 (March 2026 quarter) results:

1. What reasons did management give for the numbers?
2. Were the results in line with expectations?

Let me go back to the data I already have from the transcripts and PPTs. Let me gather the Q4 context:

From the PPT analysis:
- Q4FY26 revenue: ₹215.55 Cr (down -3% QoQ from ₹221.66 Cr)
- Q4FY26 EBITDA: ₹77.98 Cr (down -23% QoQ, margin 36%)
- Q4FY26 PAT: ₹45.35 Cr (down -32% QoQ, margin 21%)
- Management cited one-off provisions worth ~₹21 Cr (labour code ₹7 Cr, ECL ₹5 Cr, Ind AS adjustments ₹9 Cr)
- Also cited "Iran-America war panic" causing advance-booked patients to defer visits
- Grant Thornton booking changes (advances no longer booked until bill generation)

From the transcript analysis:
- Manish Grover gave multiple reasons:
  1. "Iran-America war panic" — advance-booked patients deferred visits
  2. Grant Thornton auditor changes — advances previously booked at quarter-end, now only booked upon bill generation. Claims Q4 would have been ₹9 Cr higher without this change
  3. One-off provisions: ₹19-20 Cr one-time, ₹2 Cr recurring
  4. Entero tie-up didn't start (impact on products business)

Were they in line with expectations? 
- Management had given PAT guidance of 20-25% margins consistently. Q4 came in at 21% PAT margin. On the surface, within guidance.
- But the EBITDA margin of 36% was a sharp drop from 45-48% in prior quarters. Even adjusted for one-offs (~46%), it was slightly lower than Q2's 48%.
- Revenue was ₹215.55 Cr — they had been on a trajectory of ₹174 → ₹190 → ₹222, so a QoQ decline of -3% was a miss vs trend.
- The "Iran-America war" excuse is questionable — did other healthcare companies report similar impact?
- Management seemed to be managing expectations downward with "Q3 is a weak quarter" narrative before Q3, and "war panic" narrative for Q4.

Let me also check if there's anything in the transcript that specifically discusses whether analysts were surprised or not.

Management gave **four separate reasons** for the Q4FY26 (March 2026) softness. Here's what they said:

---

### The 4 Reasons Given

**1. Iran-America War Panic**

Manish Grover's exact words: *"It happened because of Trump, sir."* He claimed advance-booked patients deferred visits due to geopolitical uncertainty. When pressed on QoQ volume decline across IPD, OPD, and daycare, this was his primary explanation.

**2. Auditor Booking Change (Grant Thornton)**

Previously, JSLL used to book advances as revenue at quarter-end when patients pre-paid. Grant Thornton stopped this practice — revenue now only recognized when the bill is generated at checkout. He claimed Q4 would have been ₹6-9 Cr higher without this change:

> *"Otherwise, my fourth quarter is ₹6 crores higher than the third quarter in terms of collections... In the fourth quarter, this practice was stopped. Otherwise, my fourth quarter would also have been ₹9 crores higher."*

**3. One-Off Provisions (~₹21 Cr)**

| Provision | Amount | Nature |
|-----------|--------|--------|
| Labour code changes | ~₹7 Cr | Employee-related |
| ECL (Expected Credit Loss) | ~₹5 Cr | Govt receivables write-off |
| Ind AS adjustments (lease etc.) | ~₹9 Cr | GT-driven accounting changes |

The CFO initially said ₹19-20 Cr was one-time, ₹2 Cr recurring. But later in the same call admitted the lease impact *"will gradually decrease each quarter"* — meaning not purely one-off.

**4. Entero Deal Didn't Start**

Products revenue fell ₹3 Cr QoQ (₹122 Cr → ₹118 Cr). When asked why the promised pharmacy push didn't materialize, he admitted Entero collapsed.

---

### Was the Result in Line with Expectations?

**No — it was a miss.** Here's why:

| Metric | Trend (Q1-Q3) | Q4 Expectation | Q4 Actual | Miss? |
|---|---|---|---|---|
| Revenue | ₹174 → ₹190 → ₹222 Cr | ₹230+ Cr (if trend held) | **₹216 Cr (-3% QoQ)** | Yes |
| EBITDA Margin | 45% → 48% → 45% | 44-46% | **36%** | Yes |
| PAT | ₹51 → ₹59 → ₹67 Cr | ₹70+ Cr | **₹45 Cr (-32% QoQ)** | Yes |
| IPD Volumes | 8.6K → 9.6K → 11.3K | 12K+ | **10.9K (-4% QoQ)** | Yes |
| OPD+COD+VC | 2.1L → 2.6L → 4.3L | 4.5L+ | **3.6L (-17% QoQ)** | Yes |

**Every single operating metric declined sequentially** — revenue, margins, IPD, OPD, daycare, video consultations. Even if you generously add back all ₹21 Cr of "one-offs" and the ₹9 Cr of advance booking changes, revenue would have been ~₹225-230 Cr — still barely flat vs Q3's ₹222 Cr, not the sequential growth investors expected.

Management's PAT margin guidance was 20-25%, and Q4 delivered 21% on the surface — just barely within range. But that was only because the denominator shrank.

**The telling part**: In the Jun 2026 concall, Manish brushed off the ₹3-4 Cr product revenue decline saying *"seeing ₹2-4 Cr up or down quarter-on-quarter doesn't matter to us — we see ₹3,000 Cr in 3-5 years."* That's a CEO dodging a legitimate question about sequential momentum with a long-term aspiration.

---

## User

is it worth paying 14.9 P/B and 33 P/E for the company? 

---

## Assistant (Plan · DeepSeek V4 Pro · 38.1s)

_Thinking:_

The user is asking whether the valuation (14.9x P/B, 33x P/E) is justified for Jeena Sikho Lifecare. Let me think through this carefully based on what we already know from the analysis.

Key data points:
- P/E: 32.2x (TTM), roughly 33x as user says
- P/B: 15.3x (TTM), user says 14.9x (slightly different timing perhaps)
- ROE: 60% (FY26)
- ROCE: 71% (FY26)
- 3Y PAT CAGR: 88%
- EPS: ₹17.87 (FY26)
- Book Value: ₹37.6/share
- FY26 PAT: ₹222 Cr
- FY27 PAT guidance: ₹300 Cr (minimum)
- Mcap: ₹7,160 Cr
- 5Y Sales CAGR: 42.6%
- Debt/Equity: 0.27
- Stock down from 52H ₹850 to ₹576 (-32%)

Let me think about whether 33x P/E and ~15x P/B make sense.

P/E of 33x:
- FY27 forward P/E = 7,160/300 = 23.9x (if they hit minimum ₹300 Cr PAT)
- PEG ratio (FY27 forward): 23.9/35% growth = 0.68 — reasonable
- Indian healthcare/hospitals typically trade at 40-60x P/E (Apollo, Max, etc.) but those are allopathy chains with institutional trust
- For a 58% 3Y revenue CAGR business, 33x trailing isn't crazy

P/B of 15x:
- If ROE sustains at 50%+, 15x P/B implies you're paying 15x book to get 50%+ annual return on that book
- In theory, a business generating 50% ROE sustainably can justify very high P/B
- But P/B of 15x implies the market believes current ROE of 60% is sustainable indefinitely — which is a very aggressive assumption

Key question: Is 60% ROE sustainable?
- Competitors (Kaya, Lloyds) are loss-making — so no pricing pressure yet
- But barriers to entry are low. Apollo or any hospital chain can set up Ayurveda wings
- If competition enters, margins compress, ROE drops
- Even if ROE drops to 30%, 15x P/B would be wildly expensive

Now let me think about what comparable companies trade at and what growth is already priced in.

At 33x trailing P/E with ₹17.87 EPS:
- Market is pricing in ~15-20% PAT CAGR for next 3-5 years (rule of thumb: PEG ~1-1.5 for quality)
- If growth decelerates to 20%, stock would rerate to 20-25x → ~₹357-447 (down 22-38%)
- If growth stays at 35%+, stock is reasonably priced

The key risk is multiple compression if:
1. Growth decelerates (Q4 already showed -3% QoQ)
2. ROE drops as asset base grows and margins normalize
3. Any corporate governance concern flares up

Let me think about what I want to say. The user wants a clear yes/no-ish assessment.

My view: At 33x trailing P/E, the stock isn't cheap, but it's not egregiously expensive for the growth profile IF you believe growth sustains. The 15x P/B is the more concerning number — it implies ROE of 60% is the new normal, which is unlikely as the business matures and adds more capital-intensive assets (fixed assets doubled to ₹307 Cr, borrowings to ₹127 Cr).

The FY27 forward P/E of ~24x (on ₹300 Cr PAT) is more palatable. But there's execution risk around that ₹300 Cr target given the Q4 miss and the OTC walk-backs.

I should present both sides and let the user decide.

A nuanced question. Let me break it down:

---

## The Math

| Metric | Value |
|---|---|
| Trailing P/E (FY26 PAT ₹222 Cr) | **32.2x** |
| Forward P/E (FY27 min ₹300 Cr PAT) | **23.9x** |
| P/B (BV ₹37.6) | **15.3x** |
| FY27 Implied PEG (at 35% PAT growth) | **0.68** |

At 33x trailing, you're buying into two things: the growth doesn't stop, and the margins don't mean-revert.

---

## The Case for "Yes"

**1. Forward P/E is actually moderate.** If they hit ₹300 Cr PAT (their own minimum guidance), you're paying 24x — reasonable for 35% growth. PEG of 0.68 is below 1.0.

**2. No real peer exists.** Kaya and Lloyds Luxuries are loss-making. You can't comp this to Apollo (40-50x P/E, but allopathy, institutionalized, 40-year track record). Jeena Sikho is the only profitable scaled Ayurveda play — scarcity premium is real.

**3. ROE of 60% math.** If this business genuinely returns 50%+ on equity sustainably, a 15x P/B is theoretically fair. The market is saying: "we believe this compounding machine keeps going."

**4. FY26 performance was a beat.** ₹801 Cr revenue vs ₹700 Cr guided. ₹222 Cr PAT vs ~₹140 Cr implied. They've beaten their own numbers on what matters most.

---

## The Case for "No"

**1. 15x P/B assumes 60% ROE is permanent.** It won't be. Fixed assets doubled to ₹307 Cr this year. Borrowings went from ₹1 Cr to ₹127 Cr. As they add beds, ROE naturally compresses — more capital employed, same or lower margins. If ROE settles at 35-40% (still excellent), the P/B should be 8-10x, not 15x. That's a 35-50% de-rating risk even with no earnings decline.

**2. Q4 FY26 broke the momentum.** Revenue declined QoQ. Every volume metric dropped. PAT fell 32%. Management stacked up 4 different excuses (Trump, auditor changes, ₹21 Cr one-offs, Entero). Even adjusting for all of them, Q4 was flat vs Q3 — not growing. One bad quarter doesn't make a trend, but at 33x P/E you can't afford many more.

**3. Stock's already told you something.** From ₹850 (52W high) to ₹576 — that's a 32% drop. The market already started pricing in the Q4 disappointment and the Entero walk-back. The question is whether ₹576 is the bottom or a resting point on the way down.

**4. Growth is decelerating.** Q1FY26: +25% QoQ. Q2: +9%. Q3: +17%. Q4: -3%. Trailing growth rates are backward-looking. Forward, even ₹300 Cr PAT for FY27 is only +35% — a sharp slowdown from FY26's +144% PAT growth. Markets pay up for acceleration, not deceleration.

---

## The Critical Question

**Is FY27 ₹300 Cr PAT achievable?**

| Path to ₹300 Cr | Required |
|---|---|
| Revenue at current 28% PAT margin | ~₹1,070 Cr (+34% YoY) |
| Revenue at 25% PAT margin | ~₹1,200 Cr (+50% YoY) |
| Revenue at 22% PAT margin (guidance floor) | ~₹1,360 Cr (+70% YoY) |

Q4FY26 annualized revenue run-rate was ₹862 Cr (₹216 Cr × 4). To hit ₹1,070 Cr in FY27, they need to average ₹268 Cr/quarter — a 24% jump from Q4's ₹216 Cr. With Entero dead, OTC products barely launched, and no new growth engine beyond organic bed additions, that's a big ask.

---

## Bottom Line

At 33x trailing P/E, you're paying full price for a business with a proven core but a habit of overpromising on everything outside it. The forward multiple of 24x is more reasonable IF they deliver ₹300 Cr PAT — but Q4 FY26 doesn't give confidence that's a lock.

The real risk isn't earnings. It's **multiple compression**. If growth decelerates to 20-25%, this stock could easily go to 20-22x P/E — which on ₹222 Cr PAT gives you ~₹360/share (-37%). The P/B of 15x amplifies this — it doesn't take much ROE compression for the stock to get cut in half even if earnings hold.

**Worth it if:** You believe Q4 was genuinely a one-off, FY27 ₹300 Cr is achievable, and the business can compound PAT at 30%+ for 3+ years.

**Not worth it if:** You see the pattern of walk-backs, the Q4 volume decline, and the deceleration as early warning signs of a growth company maturing faster than the multiple prices in.

---

## User

What should be the right price to buy for good risk-reward tradeoff 

---

## Assistant (Plan · DeepSeek V4 Pro · 4.1s)

_Thinking:_

The

---

## User

What should be the right price to buy for good risk-reward tradeoff 
do some calculation analysis and let me know 

---

## Assistant (Plan · DeepSeek V4 Pro · 45.9s)

_Thinking:_

The user wants me to calculate the right entry price for a good risk-reward tradeoff. I should do a proper valuation analysis using multiple approaches. Let me think through this carefully.

I have all the data I need from the earlier analysis. Let me do the calculations mentally and present them.

Key data points:
- FY26 Revenue: ₹801 Cr
- FY26 PAT: ₹222 Cr
- FY26 EPS: ₹17.87
- Book Value: ₹37.6 per share (or ₹468 Cr / (25/2) shares)
- Current P/E: 32.2x
- Current P/B: 15.3x
- CMP: ₹576
- Shares outstanding: 25 Cr (face value ₹2, so 25 Cr / 2 = 12.5 Cr shares? Wait, let me recalculate)

Actually, EPS is ₹17.87. Market cap is ₹7,160 Cr. So shares = 7160/576 = ~12.43 Cr shares. PAT ₹222 Cr / 12.43 Cr shares = ₹17.86 EPS. That matches.

Book value per share = ₹37.6. So total book value = 37.6 * 12.43 = ~₹468 Cr. That matches the screener data.

Let me do the analysis now.

Approaches:
1. DCF / Earnings-based valuation
2. P/E multiple approach with different scenarios
3. P/B approach given the ROE
4. Technical / sentiment approach (the stock already corrected 32% from highs)

Let me think about scenarios:

**Bear Case (₹350 Cr PAT by FY29, 3 years out):**
- Revenue: ~₹1,500 Cr
- PAT margin: 23%
- PAT: ~₹350 Cr
- EPS: ~₹28
- If market gives 15-18x (deceleration, trust issues): ₹420-505/share
- Today's value at 12% discount: ~₹315-380/share

**Base Case (₹500-600 Cr PAT by FY29):**
- Revenue: ~₹2,000 Cr
- PAT margin: 25-28%
- PAT: ~₹560 Cr
- EPS: ~₹45
- If market gives 20-25x: ₹900-1,125/share
- Today's value at 12% discount: ~₹640-800/share

**Bull Case (₹1,000 Cr PAT by FY29):**
- Revenue: ₹3,000 Cr
- PAT margin: 30-33%
- PAT: ₹1,000 Cr
- EPS: ~₹80
- If market gives 25-30x: ₹2,000-2,400/share
- Today's value at 12% discount: ~₹1,420-1,700/share

Probability-weighted:
- Bear 25% × ₹350 = ₹88
- Base 50% × ₹720 = ₹360
- Bull 25% × ₹1,560 = ₹390
- Weighted fair value: ~₹838/share

For 2:1 risk-reward (2x upside vs downside):
- Entry at 67% of fair value = ~₹560/share

Now let me also think about what P/E multiple the market would give at each price.

At ₹576 (current), trailing P/E is 32x. But let me think about what P/E is "fair" for different growth rates.

Sustainable growth rates:
- Next 3 years: 25-35% PAT CAGR
- Next 5 years: 20-25% (natural deceleration)

A company with 25% growth and 50%+ ROE deserves 20-25x P/E in a normal market.
A company with 35% growth and 60% ROE deserves 25-30x.

Right now at 32x, you're paying for 35%+ growth with high confidence. 

For entry, I'd want a margin of safety:
- 22-24x FY26 earnings: ₹393-429
- 18-20x FY27 estimated earnings (₹24 EPS est): ₹432-480
- 14-17x FY27 estimated earnings (conservative): ₹336-408

Let me also consider the recent price action:
- 52W High: ₹850
- 52W Low: ₹492
- Current: ₹576 (32% from high, 17% above low)

Let me structure this well. I'll compute the fair value range and then the entry price with adequate margin of safety.

I think the right approach is:
1. Compute FY27/FY28 earnings estimates under different scenarios
2. Apply appropriate multiples based on each scenario
3. Discount back to present
4. Apply margin of safety

Let me also compute what P/B is implied at different price levels based on growing book value.

Actually, let me just present this cleanly. The user wants me to calculate and present entry prices. Since I'm in read-only/plan mode, I should just present the analysis.

Good question. Let me run the numbers properly across multiple valuation approaches.

---

## The Setup

| Data Point | Value |
|---|---|
| Shares outstanding | ~12.43 Cr (Mcap ₹7,160 / ₹576 CMP) |
| FY26 EPS | ₹17.87 |
| FY26 Book Value/Share | ₹37.6 |
| FY26 PAT | ₹222 Cr |
| FY27 PAT (mgmt floor) | ₹300 Cr (+35%) |
| 52W Range | ₹850 (high) / ₹492 (low) |
| Current | ₹576 |

---

## Approach 1: Scenario-Based Earnings Model (FY29, 3 Years Out)

| Scenario | FY29 PAT (₹ Cr) | FY29 EPS (₹) | Terminal P/E | FY29 Price (₹) | PV @12% (₹) | Probability |
|---|---|---|---|---|---|---|
| **Bear** — growth stalls at 15% CAGR, margin compression to 22% | ~340 | 27 | 15x | 405 | **288** | 20% |
| **Base** — 25% CAGR, PAT margin 26% | ~560 | 45 | 22x | 990 | **705** | 55% |
| **Bull** — 35% CAGR, 30% PAT margin, OTC contributes | ~950 | 76 | 26x | 1,976 | **1,406** | 25% |

**Probability-weighted fair value: ~₹797/share** → 28% upside from ₹576.

---

## Approach 2: Forward P/E Method (FY27)

The market will reprice based on FY27 execution. Here's what different P/E multiples imply:

| FY27 PAT Scenario | EPS (₹) | P/E 20x | P/E 22x | P/E 25x | P/E 28x | P/E 32x |
|---|---|---|---|---|---|---|
| ₹250 Cr (miss) | 20.1 | 402 | 442 | 503 | 563 | — |
| ₹300 Cr (floor) | 24.1 | 483 | 531 | **603** | 676 | 772 |
| ₹350 Cr (beat) | 28.2 | 563 | 619 | 704 | 788 | 901 |

**Key insight:** If they hit ₹300 Cr PAT and the market awards 25x (reasonable for 35% growth), you get ₹603 — only +4.7% from ₹576. The upside at current price is thin unless either A) they beat ₹300 Cr, or B) multiples stay elevated at 28-32x.

---

## Approach 3: PEG-Based Fair P/E

A simple rule: fair P/E ≈ growth rate for high-quality compounders.

| 3-Year PAT CAGR Assumption | Fair P/E | Implied FY26 Price (₹) | Implied FY27 Price (₹) |
|---|---|---|---|
| 40% (aggressive) | 40x | 715 | 964 |
| 35% (mgmt guidance) | 35x | 625 | 844 |
| 30% (moderate) | 30x | 536 | 723 |
| 25% (conservative) | 25x | 447 | 603 |
| 20% (disappointment) | 20x | 357 | 482 |

At ₹576, the market is pricing in roughly **32% 3-year PAT CAGR**. That's the embedded expectation.

---

## Approach 4: P/B × ROE Framework

Sustainable P/B should roughly equal sustainable ROE divided by cost of equity.

| Sustainable ROE | Fair P/B | Fair Price (₹) |
|---|---|---|
| 60% (current, unlikely to sustain) | 5.0x | 188 |
| 50% | 4.2x | 158 |
| 40% | 3.3x | 124 |
| 30% | 2.5x | 94 |

Wait — this approach breaks down because BV is growing fast. BV will be ~₹60 in FY27, ~₹80 in FY28. Applying a reasonable 6-8x P/B on FY27 BV gives ₹360-480. But the current 15.3x P/B is pricing in 3-4 years of compounding — you're paying today for a book value that hasn't been built yet.

---

## Approach 5: Technical / Correction Levels

Stock has already corrected 32% from the ₹850 peak. Key levels:

| Level | Price | From Peak | Context |
|---|---|---|---|
| 52W High | ₹850 | 0% | Nov 2025 euphoria |
| 61.8% Fib | ₹630 | -26% | First support zone |
| Current | **₹576** | **-32%** | Post-Q4 selloff |
| 50% retracement | ₹549 | -35% | Psychological level |
| 52W Low | ₹492 | -42% | Panic bottom |

At ₹576, the stock is in no-man's land — not cheap enough for deep value, not high enough for momentum. The 50% retracement at ₹549 is a more natural support, and the 52W low at ₹492 is the "world is ending" price.

---

## Synthesis: The Right Entry Zones

### Zone 1: ₹490–530 — "Good Risk-Reward" 

| What you're buying | Detail |
|---|---|
| Trailing P/E | 27-30x |
| Forward P/E (₹300 Cr PAT) | 20-23x |
| PEG (35% growth) | 0.60-0.66 |
| Upside to fair value (₹797) | +50 to +63% |

At ₹500, even if they miss FY27 (₹250 Cr PAT) and trade at 20x, you're at ₹402 — only -20%. But if they hit ₹300 Cr at 25x, you get ₹603 — +21%. And the bull case gets you to ₹1,400. Risk-reward is asymmetric in your favor here.

### Zone 2: ₹400–460 — "Compelling"

| What you're buying | Detail |
|---|---|
| Trailing P/E | 22-26x |
| Forward P/E | 17-20x |
| Downside protection | Even a miss trades at 18-20x, giving ~₹360-400 (-20% max) |

This is where you buy if Q1FY27 disappoints and the market panics. You're paying for the core hospital business alone, with OTC/international/Ayushman as free options.

### Zone 3: Below ₹380 — "Steal"

Only happens in a crisis — regulatory crackdown, promoter controversy, major earnings miss. At these levels you're buying a ₹800 Cr revenue, 28% PAT margin business at liquidation multiples.

---

## So What's the Answer?

| Price | P/E (FY26) | Risk-Reward |
|---|---|---|
| **₹576 (Current)** | 32.2x | Decent, but thin margin of safety. Q1FY27 execution critical. |
| **₹500-530** | 28-30x | **Good entry.** 2:1 upside/downside if FY27 hits. |
| **₹450-490** | 25-27x | **Compelling.** Near 52W low, pricing in meaningful disappointment. |
| **<₹400** | <22x | Buy aggressively — market is mispricing the core business. |

**My take:** Current price ₹576 isn't terrible — forward P/E of 24x on ₹300 Cr is reasonable. But the risk-reward is only marginally positive because you need perfect execution. The sweet spot is **₹490-530** — that's where you get a ~30% discount to fair value, downside is cushioned (market has already panic-tested ₹492), and the forward P/E of 20x on ₹300 Cr FY27 PAT is well below the 24-25x a 35% grower deserves.

The stock has already visited ₹492 once. If Q1FY27 numbers are soft or FY27 guidance is cut, it likely revisits that level. That's the entry point worth waiting for.

---

## User

for longer-term, let's say 10 year horizon does it matter ? 

---

## Assistant (Plan · DeepSeek V4 Pro · 44.4s)

_Thinking:_

The user is asking a great question: on a 10-year horizon, does the exact entry price really matter? This is the classic "time in the market vs timing the market" debate applied to a single stock. Let me think through this carefully.

For a company like Jeena Sikho, the answer depends on what the business looks like in 10 years. If they even modestly succeed, the entry price difference between ₹500 and ₹576 is noise. But if they fail, both prices are terrible.

Let me do the math:

Scenario 1: They succeed - ₹3,000 Cr revenue, 25% PAT margin = ₹750 Cr PAT. At P/E 22x = ₹16,500 Cr mcap. That's ₹1,327/share.
- Bought at ₹576: CAGR = 8.7% over 10 years. Hmm, that's actually not great.
- Bought at ₹500: CAGR = 10.2%. Still not amazing.
- Wait, let me re-check. ₹1,327/₹576 = 2.30x over 10 years = 8.7% CAGR. That's underwhelming.

Actually wait, ₹3,000 Cr could be 3-5 years per management, not 10 years. Let me think about 10 years out.

If they hit ₹3,000 Cr in 5 years and then grow 15% for the next 5 years, that's ₹6,000 Cr revenue. At 25% PAT = ₹1,500 Cr. At 20x = ₹30,000 Cr mcap = ₹2,413/share.
- Bought at ₹576: CAGR = 15.4%. Good.
- Bought at ₹500: CAGR = 17.0%. Slightly better.

If they become a ₹10,000 Cr company (like a Max Healthcare but for Ayurveda):
- Revenue ₹10,000 Cr, PAT 22% = ₹2,200 Cr, P/E 22x = ₹48,400 Cr = ₹3,893/share
- Bought at ₹576: CAGR = 21.1%
- Bought at ₹500: CAGR = 22.8%

The difference between buying at ₹500 vs ₹576 over 10 years is roughly 1-2% CAGR. Significant but not life-changing.

BUT - and this is the key point - this all assumes the company survives and thrives for 10 years. Let me think about the risks more carefully:

What could kill the 10-year thesis:
1. Regulatory crackdown on Ayurveda claims
2. Competition from large hospital chains entering Ayurveda
3. Founder risk (Manish is the entire brand)
4. Government payment issues never fully resolved
5. OTC products fail and growth stalls

The real question is: is Jeena Sikho a compounder that will exist and thrive in 10 years, or is it a high-growth anomaly that mean-reverts?

Let me think about what the business could reasonably look like in 10 years.

Actually, let me think about this more carefully. The ₹3,000 Cr revenue target is for 3-5 years from now (so FY29-FY31). In 10 years (FY36), they'd need to be well beyond that.

Let me think about what a 10-year old Ayurveda hospital chain looks like. The addressable market is genuinely large - India's healthcare spending is growing, Ayurveda acceptance is increasing, lifestyle diseases are exploding. But the question is whether Jeena Sikho specifically captures this.

Key considerations for 10 years:
1. Brand moat: Acharya Manish Ji / HIIMS brand getting stronger or fading?
2. Competition: Will Apollo, Fortis, Max enter Ayurveda seriously?
3. Regulation: Will there be stricter clinical evidence requirements?
4. Succession: Manish is ~50 now. Who runs it when he's 60?
5. Insurance: Will insurance penetration keep growing for Ayurveda?
6. Ayushman Bharat: A massive catalyst if included, a nothingburger if not.

For a 10-year horizon, the entry price matters LESS but it doesn't NOT matter. The key question shifts from "what's the right price" to "will this company still exist and be growing in 10 years?"

Let me present this analysis clearly.

With a 10-year lens, the entry price debate shrinks significantly — but **not** to zero. Let me show you why.

---

## The Math: Price Matters Less, Survival Matters More

Let's assume the business works out. Three 10-year scenarios:

| Scenario | 10Y Revenue | PAT Margin | PAT (₹ Cr) | P/E | Mcap (₹ Cr) | Share Price (₹) |
|---|---|---|---|---|---|---|
| Modest success | ₹5,000 Cr | 22% | 1,100 | 20x | 22,000 | 1,770 |
| Base case | ₹8,000 Cr | 25% | 2,000 | 22x | 44,000 | 3,539 |
| Home run | ₹15,000 Cr | 28% | 4,200 | 25x | 1,05,000 | 8,446 |

Now plug in different entry prices:

| Buy Price | CAGR to ₹1,770 (Modest) | CAGR to ₹3,539 (Base) | CAGR to ₹8,446 (Home Run) |
|---|---|---|---|
| **₹576 (current)** | **11.9%** | **19.9%** | **30.8%** |
| ₹500 (ideal entry) | 13.5% | 21.6% | 32.8% |
| ₹400 (steal) | 16.0% | 24.3% | 35.9% |

The difference between buying at ₹400 vs ₹576 over 10 years shrinks to ~4-5% CAGR. Meaningful, yes. But the binary call — *does the business survive and compound?* — matters far more. Buying a dud at ₹400 still returns zero. Buying the right compounder at ₹576 still delivers 20%+ CAGR.

---

## But Here's the Real Question: Can This Business Compound for 10 Years?

This is where the analysis shifts from valuation to durability. Let's stack the evidence:

### What Needs to Be True for a 10-Year Compounder

| Factor | Status | Confidence |
|---|---|---|
| Large addressable market | India's chronic disease burden is massive, Ayurveda acceptance growing | High |
| Sustainable moat | Currently: brand (HIIMS/Acharya Manish). Structural: capital-light model, no patent cliffs | **Medium** |
| Founder dependency | Everything runs through Manish. No professional CEO. Brand = person | **Low** |
| Competitive insulation | No moat against Apollo opening an Ayurveda wing. "First mover" is not a moat | **Low** |
| Regulatory safety | Ayurveda claims on kidney/liver reversal could face clinical scrutiny | **Uncertain** |
| Capital allocation discipline | Franchise announced and killed in 90 days. Entero promised and walked back | **Low** |
| Earnings visibility | Proving grounds: FY26 beat. But OTC, international, wellness all unproven | **Medium** |

---

## The 10-Year Bear Case (Realistic)

You wake up in 2036. Apollo, Fortis, and 3 other chains now have large Ayurveda divisions — they undercut on price, offer integrated allopathy+Ayurveda, and have brand trust. Jeena Sikho's differentiation ("we were first") has faded. Manish Grover is 60, still running everything, no succession. Government never fixed payments — the old ₹70 Cr was written off. OTC products never broke out without a pharmacy partner. Growth settles at 10-12%. Stock trades at 15-18x. You get **₹500-600** — flat after 10 years.

Probability: maybe 20-25%.

---

## The 10-Year Bull Case (Plausible)

Ayurveda becomes mainstream. Insurance covers it routinely. Jeena Sikho is the "Apollo of Ayurveda" — synonymous with the category. They have 15,000 beds, ₹400 Cr+ in OTC products, revenue crosses ₹15,000 Cr. Manish has stepped back, professional CEO runs operations. The brand compounder narrative is intact. Stock does 25%+ CAGR.

Probability: maybe 15-20%.

---

## The 10-Year Base Case (Most Likely)

The core hospital + medicine business keeps growing at 18-22%. They add beds steadily. Margins hold at 22-25% PAT. OTC contributes modestly (₹100-200 Cr). International remains tiny. Stock does 15-18% CAGR over a decade — a solid but not spectacular compounder. ₹3,500-5,000 per share. You 6-8x your money.

Probability: maybe 55-60%.

---

## What a 10-Year Investor Should Actually Care About

Ranked by importance:

**1. Moats that compound.** The ₹3-4 lakh/bed capex advantage is a real structural moat — it means they can grow faster with less capital than an allopathy chain. That edge persists regardless of competition. Brand (HIIMS, Acharya Manish) is currently strong but unproven under competitive pressure.

**2. Founder risk resolution.** If Manish Grover is still the sole face, sole decision-maker, and sole brand in 5 years, the stock will always carry a discount. The single biggest long-term catalyst is a professional CEO, a credible board, and systems that don't need him.

**3. The product business getting real.** If OTC products ever contribute ₹500 Cr+ at 20%+ PAT margins, the earnings become far more predictable (recurring pharmacy refills vs hospital footfall). This is the difference between a 15% compounder and a 25% one.

**4. Competitive response.** Watch Apollo AyurVAID, any Fortis/Max Ayurveda moves. The moat has never been tested.

---

## So Does Entry Price Matter for 10 Years?

**Yes, but less than you think.** At ₹576, you're paying 32x for something that could 5-10x in a decade. The difference vs buying at ₹500 is ~1-2% CAGR — noticeable but not the thing that makes or breaks the investment.

What makes or breaks it: *Does this company become the definitive Ayurveda healthcare brand in India, or does it get commoditized as competition enters?*

**Current price is fine for a 10-year hold IF you answer "yes" to that question with conviction.** If you're uncertain, waiting for ₹500 gives you the same upside with a bit more margin of safety — but the real work isn't timing, it's conviction on the moat.

---

## User

what's the geogrophical distribution of hospitals of JSLL 

---

## Assistant (Plan · DeepSeek V4 Pro · 6.3s)

_Thinking:_

The user wants to know the geographical distribution of JSLL's hospitals. Let me check the PPT markdown files and transcripts for this information.

**Tool: grep**

**Input:**
```json
{
  "include": "PPT_*.md",
  "path": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation",
  "pattern": "Uttar|Rajasthan|Haryana|Punjab|Gujarat|Bihar|Maharashtra|Delhi|state|centre|hospital|presence"
}
```

**Output:**
```
Found 100 matches (more matches available)
/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Jun2026.md:
  Line 357:     *   **61:** Operational hospitals

  Line 390:     *   **FY21:** Surpassed 50 operational centres.

  Line 398: *   **2013:** Established first ayurveda health care centre in Chandigarh; holistic health care services added to the fold.

  Line 399: *   **2018:** Developed the "Shuddhi Project" to setup dedicated ayurveda health care centres.

  Line 400: *   **2020:** Inaugurated Derabassi centre – Jeena Sikho Panchakarma Hospital.

  Line 402: *   **2023:** Opened centres in Lucknow, Jaipur, Navi Mumbai, and 20 other small-mid centres across the country.

  Line 477: *   **Operational Model:** Hubs and spokes model (hospitals & clinics).

  Line 485: *   **Sales Channels:** Generated through company health care centres, tele-calling centre, and e-commerce.

  Line 495: *   **Product to Service:** Customers purchasing medicine/products are directed to visit health care centres for holistic treatment.

  Line 496: *   **Service to Product:** Patients visiting health care centres consume medicines for medium-to-long tenure post-treatment.

  Line 549: *   **Hub-and-Spoke Strategy:** Clinics and day-care facilities feed the sales funnel of hospitals in the vicinity.

  Line 550: *   **Volume Drivers:** OPD footfall from smaller units drives larger in-patient department (IPD) volumes in hospitals.

  Line 584: 1.  **Acquisition:** Proactive social media presence and national/regional media partnerships (TV, Radio, News Papers, Cinema).

  Line 585: 2.  **Lead Generation:** Health Care Camps (direct source of revenue and leads for hospitals).

  Line 661: *   **Payback Period of Investment:** <6 months (even lesser for smaller hospitals)

  Line 672: *   **Franchisee Network:** 33 franchisee-operated health care centres.

  Line 674:     *   *Control:* Ayurveda doctors and medical staff at franchise centres remain on JSLL’s payroll to ensure quality.

  Line 679:     *   **Geographies:** Direct settlement available for government employees in Uttar Pradesh, Bihar, Haryana, and Punjab.

  Line 680:     *   **Key Entities:** Empanelled with CGHS, CAPF, ECHS, and a wide range of public bodies including DDA, CBSE, CSIR, DERC, DHC, BIS, Narmada Control Authority, Haryana Govt Employee Panel, TRAI, CERC, NHAI, MMTC, IWAI, DFCIL, Air India, GAIL (India) Limited, GYPSA, MPPGCL, Navodaya, and Maruti Suzuki Limited.

  Line 689: *   **Patient Acquisition:** Relies heavily on word-of-mouth marketing ("best marketing tool") and a dedicated healthcare contact centre for customer support.

  Line 701: *   **Network Size:** 50 NABH accredited hospitals & clinics (Actual).

  Line 706: *   **Market Sizing:** India has an estimated ~1.9 million hospital beds (Source: CDDEP).

  Line 741: | Bihar | 2 | - | 9 |

  Line 744: | Delhi | 3 | 7 | 1 |

  Line 746: | Gujarat | 3 | 1 | 1 |

  Line 747: | Haryana | 6 | 1 | 5 |

  Line 752: | Maharashtra | 5 | 2 | 4 |

  Line 755: | Punjab | 4 | 5 | 1 |

  Line 756: | Rajasthan | 10 | - | - |

  Line 760: | Uttar Pradesh | 12 | 4 | 5 |

  Line 761: | Uttarakhand | 1 | - | 1 |

  Line 765: *   **New Markets:** Slide displays flags for the United States, Australia, Canada, UAE, and Bangladesh, indicating current or planned international presence.

  Line 774: This slide details the company's hospital infrastructure across four key locations, highlighting capacity (bed strength) and accreditation status.

  Line 778: | **Meerut** | Uttar Pradesh | Dec-2022 | 612 | NABH Accredited |

  Line 779: | **Lucknow** | Uttar Pradesh | Jun-2022 | 115 | NABH Accredited |

  Line 780: | **Derabassi** | Punjab (nearby Chandigarh) | Oct-2020 | 113 | NABH Accredited |

  Line 781: | **Navi Mumbai** | Maharashtra | Nov-2022 | 163 | NABH Accredited |

  Line 786: *   **Geographic Diversification:** The footprint covers Northern India (Uttar Pradesh, Punjab) and Western India (Maharashtra).

  Line 800: | **Panchkula, Haryana** | Since Aug-2024 | 70 | NABH Accredited |

  Line 806: *   **Geographic Diversification:** Facilities span Haryana, Gurugram (NCR), and Mumbai.

  Line 819: *   **Geography:** Data provided is specific to **Meerut Camp** in **Uttar Pradesh**.

  Line 825: | **Meerut Camp** | 27th to 29th March | Uttar Pradesh | 3 days | 115 | ~₹60 lakhs |

  Line 826: | **Meerut Camp** | 27th February to 1st March | Uttar Pradesh | 3 days | 118 | ~₹62 lakhs |

  Line 827: | **Meerut Camp** | 30th January to 1st February | Uttar Pradesh | 3 days | 95 | ~₹50 lakhs |

  Line 828: | **Meerut Camp** | 2nd to 4th January | Uttar Pradesh | 3 days | 103 | ~₹54 lakhs |

  Line 829: | **Meerut Camp** | 5th to 7th December | Uttar Pradesh | 3 days | 115 | ~₹61 lakhs |

  Line 830: | **Meerut Camp** | 25th to 28th December | Uttar Pradesh | 4 days | 61 | ~₹31 lakhs |

  Line 858: **Analysis Note:** This slide defines the company business model, indicating a mix of asset-heavy infrastructure (Hospitals), service hubs (Clinics/Camps), niche therapies (Panchakarma), and consumer retail products (Medical-kits, Diet Care). This suggests a diversified revenue mix beyond just inpatient hospitalization.

  Line 898:     *   Client support centres & e-com

  Line 899:     *   At health care centres

  Line 960: *   **Sales Support:** Facilitating sales leads for healthcare centres.

  Line 1029: | **02** | **Capacity Expansion** | Launch new centres & bed addition in existing centres. |


/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Feb2026.md:
  Line 137: *   **Growth Drivers:** Primarily driven by sustained volume expansion across business segments and strengthening pan-India presence.

  Line 142:     *   **New Channels:** Significant traction noted in **Day Care centres** and **Video-Call consultations**.

  Line 212: The company appears to be executing a strategic shift, reducing the count of smaller clinics/day cares while increasing the footprint of hospitals.

  Line 223: *   **Geographic Expansion (2023):** Opened centres in **Lucknow, Jaipur, and Navi Mumbai**, along with 20 other small-mid centres across the country.

  Line 227: *   **Infrastructure:** Developed the **Shuddhi Project** (2018) to set up dedicated ayurveda health care centres.

  Line 228: *   **Hospital Inauguration:** Inaugurated **Derabassi centre** (Jeena Sikho Panchakarma Hospital) in 2020.

  Line 348: *   **Referral Mechanics:** Clinics and day-care facilities act as a sales funnel, referring patients to nearby hospitals.

  Line 384: 1.  **Top of Funnel (Awareness/Leads):** Proactive social media presence, Client Support Centre marketing, and presence on National/Regional TV, Radio, Newspapers, and Cinema.

  Line 385: 2.  **Middle of Funnel (Engagement):** Health Care Camps (serving as a direct source of revenue and leads for hospitals).

  Line 398: *   **Media Partners:** Presence listed on logos including Livemint, Times Now, ABP News, NBT, Dainik Jagran, Punjabi Jagran, Amar Ujala, etc.

  Line 423: *   *Trend:* Explosive growth in IPD volumes, indicating highly effective conversion from lead sources (camps/consultations) to hospital admissions.

  Line 456: *   **Investment Payback Period:** <6 months. (Management notes this is often lesser for smaller hospitals).

  Line 468:     *   **State Empanelment:** Empanelled for treatment of government employees in Uttar Pradesh, Bihar, Haryana, and Punjab (direct settlement of medical bills as per state norms).

  Line 470:     *   **Additional Government Entities:** Listed as empanelled with DDA, CBSE, CSIR, DERC, DHC, BIS, Narmada Control Authority, Haryana Govt Employee Panel, TRAI, CERC, NHAI, MMTC, IWAI, DFCIL, Air India, GAIL (India) Limited, GYPSA, MPPGCL, Navodaya, Maruti Suzuki Limited, and leading private insurance companies.

  Line 490: *   **Franchise Centres:** 35 franchisee-operated healthcare centres.

  Line 493:     *   Doctors and medical staff at franchise centres are on JSLL’s (Jeena Sikho Lifecare Limited) payroll.

  Line 502: *   **Retention Strategy:** Patient-centric approach via dedicated healthcare contact centre and word-of-mouth marketing.

  Line 512: *   **Network Size:** 49 NABH accredited hospitals & clinics.

  Line 517: *   **Market Size:** India has an estimated ~1.9 million hospital beds (as per CDDEP).

  Line 541: *   **Total Facilities:** 58 Hospitals, 59 Clinics & daycare centres.

  Line 549: | Assam | 1 hospital |

  Line 550: | Bihar | 1 hospital | 10 franchise |

  Line 551: | Chandigarh | 1 hospital |

  Line 552: | Chhattisgarh | 2 hospital | 1 franchise |

  Line 553: | Delhi | 3 hospital | 7 clinic | 1 franchise |

  Line 554: | Goa | 1 hospital |

  Line 555: | Gujarat | 3 hospital | 1 clinic | 1 franchise |

  Line 556: | Haryana | 6 hospital | 1 clinic | 5 franchise |

  Line 558: | Jammu and Kashmir | 1 hospital |

  Line 559: | Jharkhand | 2 hospital | 1 franchise |

  Line 560: | Karnataka | 1 hospital |

  Line 561: | Maharashtra | 5 hospital | 1 clinic | 4 franchise |

  Line 562: | Madhya Pradesh | 2 hospital | 1 clinic | 1 franchise |

  Line 564: | Punjab | 3 hospital | 6 clinic | 1 franchise |

  Line 565: | Rajasthan | 10 hospital |

  Line 566: | Tamil Nadu | 1 hospital |

  Line 567: | Telangana | 1 hospital |

  Line 569: | Uttar Pradesh | 12 hospital | 3 clinic | 5 franchise |

  Line 570: | Uttarakhand | 1 hospital | 1 franchise |

  Line 571: | West Bengal | 1 hospital | 2 clinic | 1 franchise |

  Line 589: | **Meerut** | Uttar Pradesh | Dec-2022 | 612 Beds | NABH Accredited |

  Line 590: | **Lucknow** | Uttar Pradesh | Jun-2022 | 115 Beds | NABH Accredited |

  Line 591: | **Derabassi** | Punjab (nearby Chandigarh) | Oct-2020 | 113 Beds | NABH Accredited |

  Line 592: | **Navi Mumbai** | Maharashtra | Nov-2022 | 163 Beds | NABH Accredited |

  Line 604: | **Panchkula, Haryana** | Aug-2024 | 70 Beds | NABH Accredited |

  Line 610: *   **Strategic Footprint:** Operations are concentrated in the National Capital Region (Haryana/Delhi NCR) and expanding into Mumbai (Panvel).

  Line 624: The following table details specific camp instances in Uttar Pradesh, showing visitor volume and direct business generated (revenue).

  Line 664: - **Diversification:** The presence of services like "Obesity & Weight Loss," "Skincare," and "Eye Treatment" suggests a mix of medically essential services and elective/cosmetic-adjacent services, which could imply different margin profiles or growth drivers.


(Results truncated. Consider using a more specific path or pattern.)
```

**Tool: grep**

**Input:**
```json
{
  "include": "Transcript_*.txt",
  "path": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall",
  "pattern": "Uttar|Rajasthan|Haryana|Punjab|Gujarat|Maharashtra|Bihar|Delhi|states|geograph|presence|hospital.*in"
}
```

**Output:**
```
Found 100 matches (more matches available)
/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Feb2026.txt:
  Line 48: Place: Zirakpur, Punjab 

  Line 254: large hospitals spend just to acquire a patient, spending INR8,000, INR9,000 as patient 

  Line 261: open a 100-bed hospital, we open it in INR3 to INR4 crores. 

  Line 278: you gave Ravi sir's number. I spoke to him. I am currently a 3rd-year student at Delhi 

  Line 326: Diwali comes, winter comes, all hospitals remain weak. At that time, if I increased operational 

  Line 341: that we are starting new hospitals in UAE? 

  Line 402: India, until February, hospital business remains down. From March to September, hospital 

  Line 429: Franchises are only clinics. No hospital is a franchise, all are our own. We are slowly reducing 

  Line 566: hospitals, in how many years will those 50 franchise hospitals happen? 

  Line 568: Regarding the opening of new hospitals, we have just finalized the model. We have finalized a 

  Line 573: super-specialty hospitals. So super-specialty clinics—now they will be within cities. Our initial 

  Line 704: No, that's absolutely right, sir. Just looking at Vitamin D in Delhi-NCR, I think 80% of people 

  Line 728: So Acharya ji, in how many states is this available now -- meaning how many super stockists 

  Line 731: Currently, the product is in about 11 states and is available at approximately 2000 to 2500 

  Line 763: will now act as feeders for me to fill my hospitals. Now I am planning VVIP hospitals and we 

  Line 854: are the biggest clinic and hospital chain in India. 

  Line 884: Sir, I had told you that from March to September, beds fill up in hospital business. Now I will 

  Line 903: in every hospital. But in Ayurveda, health insurance is new, so people are taking time to 

  Line 1222: December, New Year celebration. If you check, the quarter of all hospitals remains weak, this 

  Line 1263: work. And I have kept Allopathy doctors in my hospitals. In emergency, they help. So I am in 

  Line 1266: But what is happening is, as hospitals are increasing, diseases are increasing. Because 

  Line 1314: dialysis came. So I came to your hospital, following you since then. And I found out this year 

  Line 1423: launch a product, anyone can open an Ayurveda hospital, but winning the customer's trust. We 

  Line 1445: And now we are bringing in a chain of super-specialty hospitals and clinics. We have done 

  Line 1447: products in OTC, and we have the hospitals. So we don't have to give anything to anyone; our 

  Line 1453: For example, day before yesterday, I gave a lecture at a Punjab University; so for all the 

  Line 1469: Bengali, Gujarati, Marathi, and all those patients. 


/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Jun2026.txt:
  Line 51: Place: Zirakpur, Punjab 

  Line 162: basis, including 58 hospitals and 59 daycare and clinical centers. Our centers are across 23 states 

  Line 163: and 100 cities. Large hospitals in big cities serve as hubs. Near Delhi and Meerut, we have about 

  Line 166: In Mumbai and Panvel, we have four hospitals, including 200+ beds in Panvel and 150+ beds in 

  Line 191: centers and hospitals. We have 59 clinics and daycare centers, client support centers, and 

  Line 224: the panels of the state governments of Uttar Pradesh, Bihar, Haryana, and Punjab, as well as the 

  Line 227: I have some good news, just four days ago, the Uttar Pradesh government launched its UPSS 

  Line 229: UP is India's largest state, and we have the most centers in Uttar Pradesh. 

  Line 232: like any other hospital in India. We are both preventive and curative. We are always committed 

  Line 338: was asking us to bear the expenses. So, we have now increased our presence in newspapers, 

  Line 448: employees in Uttar Pradesh. And UP is India's largest state, and I have the most centers in UP.  

  Line 630: made new hospitals into specialty hospitals. And now the new change we're going to start is 

  Line 697: hospitals became patients themselves, got admitted, purchased things there, gave cash and saw 

  Line 747: And I'm telling you again, all the big hospitals in India, whether Allopathy or Ayurveda, will 

  Line 749: so many scams in hospital billing that those hospitals then get blacklisted. 

  Line 877: in about 12 to 18 months and in small hospitals, it happens in even less than 6 months. So, when 

  Line 1059: for OPD. There were people from Gujarat, from Madhya Pradesh, from the South too. So, when 

  Line 1060: you have so much demand, why are you not opening more large hospitals like Meerut in other 

  Line 1075: very large hospital in Lucknow is going to be finalized this week. Work is going on for a large 

  Line 1076: hospital in Ahmedabad. We are looking for a new property in Patna. We have found a new 

  Line 1138: I can give you the data for the last quarter. In the last quarter's data, in our hospital business, if I 


/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Nov2025.txt:
  Line 47: Place: Zirakpur, Punjab 

  Line 139: occupancy. We have our reach in 23 states and 100 plus cities of the country and the customer 

  Line 140: traction which our newly opened hospitals have got is really encouraging. We are seeing 

  Line 150: market. Then we added clinics, we added hospitals, added daycare and now we are going to add 

  Line 194: in Delhi, Bihar, Gujarat and Maharashtra. And sales are increasing, product sale has increased 

  Line 262: I will use their cash back of their card. They were already in seven states and in a way their 34 

  Line 267: and because of which footfall will increase in my hospital, and it will increase greatly. And in 

  Line 269: five days. So, the footfall will increase in my hospital and clinic. And they are setting up full-

  Line 306: that time very aggressively I will pick up five to ten hospitals in India and I will admit patients 

  Line 307: in those hospitals. Because I have brought my government business to 3%. 

  Line 324: regarding this, all the private hospitals in big cities all are doing treatment. So, why are we 

  Line 336: All the big hospitals are running on RGHS and CGHS. There is no such big hospital that is not 

  Line 422: do not stay in the hospital at that time. Because no one can keep a patient tied up in our hospital. 

  Line 795: to go to the hospital? The Ayurvedic sutra says, “sarve roga api mandaginihi ajir maline kupit 

  Line 1027: to keep children of all languages. Assamese, Bengali, Punjabi, Marathi, Tamil, Telugu, Kannada. 

  Line 1070: investment. In Delhi, they bought a lab worth Rs. 4 crores to Rs. 5 crores just after our tie-up. 

  Line 1072: center. There are 19 centers in Delhi NCR. And their employees are sitting in all 19 centers. And 

  Line 1077: everything. And what is the biggest benefit? In Delhi, they are setting up cancer marker tests. 

  Line 1118: They have bought two labs in Delhi. One is of Rs 5 crores, Rs.6 crores and another one is of Rs 

  Line 1140: at least 50 new hospitals. And Jeena Sikho will open in a franchise model. I did not have to tell 

  Line 1147: new franchises. Which we will launch next month. So, we are planning 50 new hospitals in a 

  Line 1212: but you do not have much presence here. You just told us about a hospital in Kolkata in this 


/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/concall/Transcript_Aug2025.txt:
  Line 48: Place: Zirakpur, Punjab 

  Line 126: expansion of products and hospital, clinics and daycare footprint. We have seen an increase of 

  Line 136: spread to 100 plus cities and 23 states. And, the patient response from recently opened hospital 

  Line 333: I would like to tell you that the allopathy hospitals in India its market is of INR7 lakh crores. 

  Line 336: maintain this with my hospital and clinic business. 

  Line 383: in four different states so that we do not have to spend like I have to deliver in Punjab and 

  Line 384: Haryana. So I will get it made in Punjab, like if I have to deliver in UP, then it will be made in 

  Line 385: UP. If I have to deliver in Maharashtra and Gujarat, then the product will be made there.  

  Line 387: Maharashtra, we will write Marathi together on the box. In Gujarat, yesterday our Gujarat has 

  Line 391: So by doing this, in the next 15 to 30 days, we will launch this product in three states. And in 

  Line 392: the next 2 months, in about five to six states. We will launch this product. First, we will do one 

  Line 398: in OTC. The hospital details will come out in his box. The clinic details will come out. So that 

  Line 441: And our hospitals also increased from 50 to 55 in 2025. And our NABH was 41 in 2025. That 

  Line 445: have started getting hospitals without spending. 

  Line 446: For example, our Mohali hospital has started. The Saraswati group of college that we took in 

  Line 447: Kharar. And our second hospital that is being built in Vrindavan 150 beds that will also start 

  Line 459: second is Sanskriti University, Vrindavan. The third is a hospital of 100 beds in Aurangabad. 

  Line 562: hospital expenses will remain the same. As the bad occupancy increases, the benefit will also 

  Line 618: hospital in Dubai. It will be open till the next quarter. That's why you said. So can you tell 

  Line 621: Sir, we are not opening 2 hospitals. We are opening clinics. 2 have been opened there. But 

  Line 623: days. Clinic and hospital has been opened. 2 have been opened in Dubai, Abu Dhabi. And we 

  Line 628: in taking hospitals of the colleges. That you have avoided this medicine business. So what 

  Line 727: Madam, now we will plan all the colleges. We will not open our own hospitals. I told you in 

  Line 744: And the hospitals that we have tied up with, they have done minimum rent and revenue 

  Line 761: projects too. For example, we will bring a heart project in one hospital, we will bring a joint 

  Line 764: So we will make different hospitals specialized in different ways. If you have kidney disease, 

  Line 835: The Bihar government and the Maharashtra government, the Bihar and Maharashtra 

  Line 838: Earlier it was UP, then Punjab, -- earlier it was UP, Punjab, and what was it? Haryana. Now 

  Line 839: we have the letter from the Bihar government and the Maharashtra government has also started 

  Line 934: in Gujarat and Maharashtra. So, what will be left? 2-3 months will be left for this year. 


(Results truncated. Consider using a more specific path or pattern.)
```

---

## Assistant (Plan · DeepSeek V4 Pro · 4.0s)

_Thinking:_

Now let me get the detailed state-wise breakup from the PPT files, especially the hospital/clinic/franchise count per state.

**Tool: read**

**Input:**
```json
{
  "filePath": "/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Jun2026.md",
  "offset": 735,
  "limit": 40
}
```

**Output:**
```
<path>/Users/asheth/Documents/personal/equity_research/JEENA_SIKHO_LIFECARE/presentation/PPT_Jun2026.md</path>
<type>file</type>
<content>
735: *   **Pipeline (Facilities):** 5
736: 
737: **Geographical Asset Breakdown**
738: | State / Region | Hospitals | Clinics | Franchise |
739: | :--- | :---: | :---: | :---: |
740: | Assam | 1 | - | - |
741: | Bihar | 2 | - | 9 |
742: | Chandigarh | 1 | - | - |
743: | Chhattisgarh | 2 | - | 1 |
744: | Delhi | 3 | 7 | 1 |
745: | Goa | 1 | - | - |
746: | Gujarat | 3 | 1 | 1 |
747: | Haryana | 6 | 1 | 5 |
748: | Himachal Pradesh | - | 2 | - |
749: | Jammu and Kashmir | 1 | - | - |
750: | Jharkhand | 2 | - | 1 |
751: | Karnataka | 1 | - | - |
752: | Maharashtra | 5 | 2 | 4 |
753: | Madhya Pradesh | 2 | 1 | 1 |
754: | Odisha | - | - | 2 |
755: | Punjab | 4 | 5 | 1 |
756: | Rajasthan | 10 | - | - |
757: | Tamil Nadu | 1 | - | - |
758: | Telangana | 1 | - | - |
759: | Tripura | - | - | 1 |
760: | Uttar Pradesh | 12 | 4 | 5 |
761: | Uttarakhand | 1 | - | 1 |
762: | West Bengal | 2 | 2 | - |
763: 
764: **Strategic / International Expansion**
765: *   **New Markets:** Slide displays flags for the United States, Australia, Canada, UAE, and Bangladesh, indicating current or planned international presence.
766: 
767: ---
768: 
769: ## Page 38
770: 
771: **Slide Title: Key Health Care Facilities (Breadth of Operations)**
772: 
773: **Operational Footprint & Capacity Metrics**
774: This slide details the company's hospital infrastructure across four key locations, highlighting capacity (bed strength) and accreditation status.

(Showing lines 735-774 of 1073. Use offset=775 to continue.)
</content>
```

---

## Assistant (Plan · DeepSeek V4 Pro · 16.4s)

_Thinking:_

Now I have the full geographical breakdown from the PPT. Let me compile this into a clear summary.

Here's the geographical distribution of Jeena Sikho's facilities (from latest Jun 2026 PPT):

---

## State-Wise Facility Breakup (FY26)

| State | Hospitals | Clinics | Franchise | Total |
|---|---|---|---|---|
| **Uttar Pradesh** | **12** | 4 | 5 | **21** |
| **Rajasthan** | **10** | — | — | **10** |
| **Haryana** | 6 | 1 | 5 | 12 |
| **Maharashtra** | 5 | 2 | 4 | 11 |
| **Punjab** | 4 | 5 | 1 | 10 |
| Delhi | 3 | 7 | 1 | 11 |
| Gujarat | 3 | 1 | 1 | 5 |
| Bihar | 2 | — | 9 | 11 |
| Chhattisgarh | 2 | — | 1 | 3 |
| Jharkhand | 2 | — | 1 | 3 |
| Madhya Pradesh | 2 | 1 | 1 | 4 |
| West Bengal | 2 | 2 | — | 4 |
| Assam | 1 | — | — | 1 |
| Chandigarh | 1 | — | — | 1 |
| Goa | 1 | — | — | 1 |
| J&K | 1 | — | — | 1 |
| Karnataka | 1 | — | — | 1 |
| Tamil Nadu | 1 | — | — | 1 |
| Telangana | 1 | — | — | 1 |
| Uttarakhand | 1 | — | 1 | 2 |
| Himachal Pradesh | — | 2 | — | 2 |
| Odisha | — | — | 2 | 2 |
| Tripura | — | — | 1 | 1 |

**23 states, 100+ cities, 61 hospitals, 58 clinics, 33 franchise centres.**

---

## Key Concentration Patterns

### The Heartland Dominance
**North India (UP + Haryana + Rajasthan + Punjab + Delhi) = 64% of facilities.** 35 out of 61 hospitals are in these 5 states. This is where the brand is strongest — word of mouth, TV/radio campaigns in Hindi/Punjabi, and Acharya Manish's personal following are concentrated here.

### Key Flagship Hospitals

| Hospital | Location | Beds | Since |
|---|---|---|---|
| Meerut | Uttar Pradesh | **612** | Dec 2022 |
| Panvel | Maharashtra | 230 | Oct 2025 |
| Navi Mumbai | Maharashtra | 163 | Nov 2022 |
| Lucknow | Uttar Pradesh | 115 | Jun 2022 |
| Derabassi | Punjab (near Chandigarh) | 113 | Oct 2020 |
| Panchkula | Haryana | 70 | Aug 2024 |

### The Weak Spots
- **South India:** Only 1 hospital each in Karnataka, Tamil Nadu, Telangana — token presence. Total 3 hospitals south of Maharashtra. That's ~5% of the hospital network for a region with 20% of India's population and higher healthcare spending.
- **East India:** 1 hospital each in Assam, West Bengal (2). Odisha has only 2 franchise centres, no hospitals.

---

## What This Tells You

**1. The growth has been organic and regional, not national.** They've gone deep in the Hindi belt where Manish Grover's brand and media presence (Amar Ujala, Dainik Jagran, Punjabi Jagran, regional TV) works. Most patients travel from surrounding areas to flagships like Meerut.

**2. South India is the biggest unmet expansion opportunity — but also the hardest.** Brand awareness is near zero. Language is a barrier (they heavily use Hindi/Punjabi in marketing and camps). The 1 hospital each in Karnataka/Tamil Nadu/Telangana are experiments, not a real footprint.

**3. The franchise model is concentrated in Bihar and UP.** Bihar has 9 franchise centres but only 2 owned hospitals — suggesting they use franchises where they lack capital commitment or see lower per-patient economics.

**4. UP is the crown jewel.** 12 hospitals + 4 clinics + 5 franchises. Meerut alone has 612 beds (27% of total operational beds). The UP government just launched UPSS (cashless Ayurveda scheme) — Manish flagged this in the Jun 2026 concall as a major opportunity. If UP government business returns at better payment terms, the UP cluster becomes even more valuable.

**5. The "23 states, 100+ cities" headline overstates the depth.** Presence in 10+ states is just 1 hospital — symbolic. The real business is 5 north Indian states + Maharashtra pocket in Navi Mumbai/Panvel.

---

