---
name: tavily-research
description: Deep AI-powered research with citations via `tvly research`. Use when the user wants comprehensive multi-source analysis, market reports, or needs synthesis with citations. Takes ~30s. For quick lookups, use `tvly search` instead.
allowed-tools: Bash(tvly *)
---

# Tavily Research

Always use `--model mini` — fast (~30s), sufficient for our use case.

## Quick start

```bash
tvly research "query" --model mini            # basic (~30s)
tvly research "query" --model mini --stream   # stream results in real-time
tvly research "query" --model mini -o out.md  # save to file
tvly research "query" --model mini --json     # structured JSON output
```

## Options

- `--model` — `mini`, `pro`, or `auto` (default). Always use `mini`.
- `--stream` — stream results in real-time
- `--no-wait` — return request_id immediately (async)
- `--citation-format` — `numbered`, `mla`, `apa`, `chicago`
- `--timeout` — max wait seconds (default: 600)
- `-o, --output` — save output to file
- `--json` — structured JSON output

## Prerequisites

Check `tvly --status`. Install via `curl -fsSL https://cli.tavily.com/install.sh | bash` if missing.
