---
name: qmd-status
description: Query QMD (Quarto Markdown) memory backend status and statistics. Use when the user wants to check QMD index status, view indexed documents, or troubleshoot memory search issues.
---

# QMD Status Query

This skill queries the QMD memory backend status.

## Usage

Run the status script to get current QMD statistics:

```bash
~/.openclaw/skills/qmd-status/scripts/status.sh
```

## What it shows

- Index location and size
- Total indexed documents
- Vector embeddings count
- Collection details (memory-root, memory-alt, memory-dir)

## Manual queries

For advanced usage, run QMD commands directly:

```bash
export PATH="$HOME/.bun/bin:$PATH"

# Full status
qmd status

# List collections
qmd collection list

# Search memories
qmd search "keyword" -n 5

# Query with reranking (slower)
qmd query "search term" --json
```

## Troubleshooting

- If `qmd` not found: Check `~/.bun/bin` is in PATH
- If no collections: Run `qmd collection add` to index files
- If no vectors: Run `qmd embed` to generate embeddings
