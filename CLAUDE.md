# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

A memorial web application ([shootingvictims.us](https://shootingvictims.us)) that displays the names of gun violence victims with respect and solemnity. All data changes must honor that intent — this is a memorial, not a database demo.

## Commands

```bash
npm install        # Install dependencies
npm run dev        # Local dev server
npm run build      # Production build (outputs to dist/)
npm run preview    # Preview production build locally
```

```bash
python victims.py add "First" "Middle" "Last" <age> "YYYY-MM-DD"   # Add victim (middle name optional, pass "" to omit)
python victims.py list                                               # List all victims
python victims.py remove "First" "Middle" "Last" <age> "YYYY-MM-DD" # Remove by exact match
```

Run `victims.py` from the project root — it expects `src/assets/victims.json` relative to CWD.

## Architecture

Two independent layers that share only `src/assets/victims.json`:

**Vue 3 frontend** (`src/`) — no router, no store, no build-time data fetching. `victims.json` is imported statically at build time via Vite. The app opens with a full-screen "Rest in peace" fade sequence (~5 s), then transitions to the victim list. `App.vue` owns the sequence logic and renders `Victim.vue` once per entry. There is no backend; everything is a static site deployed to S3 + CloudFront.

**Python data tool** (`victims.py`) — a standalone CLI (`VictimsManager` class) that reads, validates, deduplicates, sorts, and writes `victims.json`. It does not interact with the frontend at build time; changes take effect on the next `npm run build`.

## Data Format

`src/assets/victims.json` is an array sorted most-recent-first by `dateOfDeath`. The `age` field is stored but not rendered in the UI. Always use `victims.py` to mutate the file — it enforces duplicate checking, date validation, and re-sorting.

```json
[
  {
    "firstname": "Jane",
    "middlename": "",
    "lastname": "Doe",
    "age": 30,
    "dateOfDeath": "2023-06-20"
  }
]
```

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the app and syncs `dist/` to S3, then invalidates the CloudFront cache. There is no staging environment — `main` is production.
