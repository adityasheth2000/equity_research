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
│       ├── ppt-analyzer/         # Vision-based PPT extraction
│       │   ├── SKILL.md
│       │   └── ppt_analyzer.py
│       └── stock-analyzer/       # Document download & workflow
│           ├── SKILL.md
│           └── download_docs.py
└── COMPANY/
    ├── presentation/             # PPTs and vision-extracted .md (shared across dates)
    │   ├── PPT_May2026.pdf
    │   ├── PPT_May2026.md
    │   └── ...
    ├── concall/                  # Transcripts PDFs and .txt (shared across dates)
    │   ├── Transcript_May2026.pdf
    │   ├── Transcript_May2026.txt
    │   └── ...
    ├── tmp/                      # Intermediate artifacts (gitignored)
    └── dated-folder/             # e.g., 1-July-2026
        ├── screener.html         # Screener.in snapshot
        ├── screener_files/       # Screener.in assets
        └── verdict.md            # Final analysis summary
```

Skills provide specialized instructions and workflows for specific tasks.
Use the skill tool to load a skill when a task matches its description.
