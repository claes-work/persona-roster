---
type: learning
topic: roster-ingest-autopilot
updated: 2026-07-19
---

# Roster ingest autopilot — what actually works (cadence, batches, budget)

Operational learnings for `/roster-loop` + `tools/refresh_sources.py`. Policy:
[[../decisions/2026-07-19-ingest-scheduling-policy]]. Journal (raw evidence):
`autopilot/journal.jsonl`.

## Persona view

n/a — this is infrastructure; no persona claims ingest-scheduling expertise.

## Own evidence

- **2026-07-19 (first live discovery refresh, 4 enumerated clones, newest-30/channel):**
  hormozi +32 video/+61 short (6 days since last enumeration — ~5/day long-form
  across 5 channels), neil-patel +4/+12, mkbhd +2/0, chris-do +0 (5 days, weekly
  cadence channel). Runtime ~4 min total, dominated by per-video metadata fill.
  Same-day re-run: +0 everywhere — idempotency confirmed. The fresh-upload→P1
  promotion put the same-day Hormozi video ("Why AI won't make you rich in 2026",
  2026-07-19) at the head of the ingest queue.
- **Usage calibration:** none yet. Sebastian's prior observation: one clone's ingest
  loop can run 5–7h without exhausting the weekly limit (single-clone sessions,
  Opus 4.8). Record post-run data points here as
  `[date] timebox Xh, cycles N, observed usage Y%`.

## Effective rule

- Discovery refresh daily (stale_hours=24), newest-30 per channel; `--full`
  enumeration only targeted per clone.
- Time-box default 6h until ≥3 calibration data points exist; then set the time-box
  from the observed hours→usage curve to land at ~80% weekly usage.
- Treat rate-limit stalls as back-off (60 min), never as run failure.
