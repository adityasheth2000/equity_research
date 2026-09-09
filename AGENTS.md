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
│       └── screener-navigator/   # Screener.in document downloads
│           ├── SKILL.md          # Skill documentation
│           └── download_docs.py  # Downloads PPTs + transcripts → TICKER/presentation/, TICKER/concall/
└── TICKER/
    ├── presentation/             # PPTs (shared across dates)
    │   ├── PPT_May2026.pdf
    │   └── ...
    ├── concall/                  # Transcripts PDFs + .txt (shared across dates)
    │   ├── Transcript_May2026.pdf
    │   ├── Transcript_May2026.txt
    │   └── ...
    ├── credit_ratings/           # Rating reports (shared across dates)
    ├── tmp/                      # Intermediate artifacts (gitignored)
    └── dated-folder/             # e.g., 27-august-2026
        ├── screener_full.png     # Screener.in snapshot
        └── verdict.md            # Final analysis summary
```

## Workflow

Since modern LLMs support direct PDF reading, the analysis pipeline is simplified:

1. **Download documents** using the `screener-navigator` skill — fetches PPTs and transcripts from Screener.in into `TICKER/presentation/` and `TICKER/concall/`
2. **Read PDFs directly** — use the read tool on downloaded PDFs for direct model interpretation (no intermediate extraction scripts needed)
3. **Capture screener data** — take a full-page screenshot of the Screener.in company page to `TICKER/tmp/screener_full.png` for financial data reference
4. **Synthesize** findings into a verdict.md in a dated folder

Skills provide specialized instructions and workflows for specific tasks.
Use the skill tool to load a skill when a task matches its description.