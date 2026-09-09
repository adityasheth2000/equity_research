---
name: screener-navigator
description: Use whenever the user wants to navigate screener.in via agent-browser or download documents. Covers login, full-page screenshots, tab navigation, and document downloads (PPTs, transcripts, annual reports). Trigger on "navigate screener", "screener login", "download screener docs", "take screener screenshot", "screener screenshot".
allowed-tools: Bash(agent-browser:*), Bash(source .opencode/skills/screener-navigator/.env:*), Bash(python .opencode/skills/screener-navigator/*)
---

# Screener Navigator

Two capabilities:
1. **Browser automation** — navigate screener.in via agent-browser (login, screenshots, tab navigation)
2. **Document downloads** — fetch PPTs, transcripts, and annual reports via `download_docs.py`

## Prerequisites

- `agent-browser` CLI installed (`npm i -g agent-browser && agent-browser install`)
- Repo-level `.venv` with `requests`, `beautifulsoup4`, `PyMuPDF` installed
- Credentials in `.opencode/skills/screener-navigator/.env`

---

## Part 1: Browser Navigation (agent-browser)

### Open Company Page & Login

```bash
source .opencode/skills/screener-navigator/.env
agent-browser open "https://www.screener.in/company/{TICKER}/consolidated/"
agent-browser wait --load networkidle

# Login (click "LOGIN" link in top nav)
agent-browser snapshot -i
agent-browser click @eX                    # link "LOGIN" (top-right nav)
agent-browser wait --load networkidle
agent-browser snapshot -i
agent-browser fill @eX "$SCREENER_EMAIL"   # textbox "Email"
agent-browser fill @eY "$SCREENER_PASSWORD" # textbox "Password"
agent-browser click @eZ                    # button "LOGIN"
# NOTE: successful login redirects to https://www.screener.in/dash/ (NOT back to /company/)
agent-browser wait --url "**/dash/**"
agent-browser wait --load networkidle

# Verify login — top nav now shows account button (e.g. "NIVESTINDIA"), not "LOGIN"
# Re-open the company page:
agent-browser open "https://www.screener.in/company/{TICKER}/consolidated/"
agent-browser wait --load networkidle
```

**Login details:**
- Login page shows `heading "Welcome back!"`, `textbox "Email"`, `textbox "Password"`, `button "LOGIN"`.
- After login, screener.in redirects to the **dashboard** (`https://www.screener.in/dash/`), not back to the company page. Wait for `**/dash/**`, then re-open the company URL.
- Verify by checking the top nav shows the account name (e.g. `button "NIVESTINDIA"`) instead of `link "LOGIN"`.

### Full-Page Screenshot

```bash
agent-browser screenshot --full {TICKER}/tmp/screener_full.png
```

### Navigate Sections

Use `agent-browser snapshot -i` to see interactive elements. Scroll down to find sections:

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
| **Annual Reports** | `heading "Annual reports"` |
| **Credit Ratings** | `heading "Credit ratings"` |
| **Concalls** | `heading "Concalls"` |

### Close Browser

```bash
agent-browser close
```

---

## Part 2: Document Downloads (download_docs.py)

```bash
source .venv/bin/activate

python .opencode/skills/screener-navigator/download_docs.py \
  --url "https://www.screener.in/company/{TICKER}/consolidated/" \
  --max 5
```

Downloads the 5 most recent investor presentations to `{TICKER}/presentation/`, concall transcripts to `{TICKER}/concall/`, and the 2 most recent annual reports to `{TICKER}/annual_reports/`. Transcript PDFs are auto-converted to `.txt` via PyMuPDF. Idempotent — skips existing files.

Options:
- `--max N` — max recent concall entries to download (default 5)
- `--max-annual-reports N` — max annual reports to download (default 2)
- `--skip-annual-reports` — skip annual report downloads
- `--skip-transcript-text` — skip transcript → text conversion

### Output Structure

```
TICKER/
├── presentation/                       # PPT PDFs
├── concall/                            # Transcript PDFs + .txt
├── annual_reports/                     # Annual report PDFs from BSE
└── tmp/                                # Intermediate (gitignored)
    └── screener_full.png
```

### Important Notes

- Always `source .opencode/skills/screener-navigator/.env` before using credentials.
- Re-snapshot after every navigation (refs become stale).
- Use `wait --load networkidle` after tab switches or form submissions.
- The screenshot flag is `--full` (not `--fullpage`).
- Avoid hardcoding credentials; always use `$SCREENER_EMAIL` / `$SCREENER_PASSWORD`.