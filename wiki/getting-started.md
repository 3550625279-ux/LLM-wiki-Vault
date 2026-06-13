---
type: meta
title: "Getting Started"
updated: 2026-06-13
tags:
  - meta
  - onboarding
status: evergreen
---

# Getting Started

## Three Steps

### 1. Drop a source

Put any document into `raw/`:
- PDFs, markdown files, transcripts, articles, URLs

### 2. Ingest it

```
ingest [filename]
```

Claude reads the source, creates wiki pages under `wiki/`, cross-references everything, and updates the index.

### 3. Ask questions

```
what do you know about [topic]?
```

Claude reads the wiki and gives you a synthesized answer citing specific pages.

---

## Key Commands

| You say | Claude does |
|---------|-------------|
| `ingest [file]` | Creates wiki pages from a source |
| `what do you know about X?` | Queries the wiki, cites pages |
| `/save` | Files this conversation as a wiki note |
| `/autoresearch [topic]` | Searches the web, ingests results |
| `lint the wiki` | Health check |
| `update hot cache` | Refreshes session context |
