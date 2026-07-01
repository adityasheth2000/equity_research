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
└── SHANTIGOLD/
    └── 1-July-2026/          # Dated analysis folder
        ├── verdict.md        # Final analysis summary
        ├── monte_carlo.py    # Monte Carlo simulation source
        ├── monte_carlo_data.json    # Raw simulation data
        ├── monte_carlo_results.json # Summary statistics
        ├── chart_*.png       # Distribution charts
        ├── Transcript_*.pdf  # Concall transcripts (3 quarters)
        ├── Transcript_*.txt  # Extracted text from transcripts
        ├── PPT_*.pdf         # Investor presentations (3 quarters)
        └── PPT_*.txt         # Extracted text from PPTs
```
