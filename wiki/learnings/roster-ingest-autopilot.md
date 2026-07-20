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
- **2026-07-19 (run 1, supervised, user-ended at 0.48h of 2h):** 3 cycles, all
  hormozi Stage B (fresh uploads), 22 videos → L2. ~6–8 min/cycle wall clock,
  ~90–103k subagent tokens/cycle (≈293k total) + dispatcher overhead. Zero rate
  limits. Dispatcher-premise correction worked: cycle 2's executor verified the
  synthesis checkpoint was already drained and ran Stage B instead of the expected
  Stage S — "clone stage machine decides" holds.
- **Usage calibration:** Sebastian's prior observation: one clone's ingest
  loop can run 5–7h without exhausting the weekly limit (single-clone sessions,
  Opus 4.8). Record post-run data points here as
  `[date] timebox Xh, cycles N, observed usage Y%`.
  - **2026-07-19 (run 2, session /loop, 6h box, batch 8):** ended cleanly on
    timebox at 6.06h, 29 cycles (hormozi ×1 Stage B; neil-patel ×26 Stage B + ×2
    Stage S). 207 videos → L2, neil-patel built 0→207 L2 + system-prompt v2. Zero
    rate limits; one async subagent stalled mid-bookkeeping (cycle 19), recovered
    by resuming the same agent. **Attributable session cost (Claude Code meter):
    $210.99** — Opus 4.8: 4.3M input, 2.3M output, 114.8M cache-read, 11.6M
    cache-write; API wall ~8h57m (includes parallel subagents), session wall 6h25m.
    NOTE: subscription-limit % is NOT attributable to this run alone — Sebastian
    had other concurrent sessions running.
  - **Pre-run-3 limit snapshot (2026-07-19 ~17:55 CEST, before a planned ~15h box):**
    session gauge **50%** (resets 18:59 CEST); **week all-models 84%** (resets
    **2026-07-20 05:59 CEST** — this is the binding limit); week Fable 25%. Purpose:
    measure run-3 consumption by comparing against the Monday-06:00 reset. Because
    multiple sessions share the pool, treat this only as an upper-bound anchor, not a
    clean single-run delta. Cleanest single-run signal remains the Claude Code
    per-session $ meter above.
  - **2026-07-20 (run 3, session /loop, 15h box, parallel x2) — HIT THE WEEKLY LIMIT:**
    started 2026-07-19 18:20 at week-84%; the weekly all-models limit was reached
    **~03:54 CEST 2026-07-20** (resets 06:00). **~9.5h of parallel-x2 ingest** (2 clones
    per cycle) consumed the remaining ~16% weekly budget — but other concurrent sessions
    shared the pool, so treat as an **upper-bound anchor, not a clean single-run figure**.
    Work done in that window: 86 cycles (79 Stage B + 7 Stage S), ~600 videos → L2
    (neil-patel +326 to 533 / v6; mkbhd 0→274 / v3). Mid-run limit interruption was a
    non-event: both in-flight subagents died uncommitted; after the 06:00 reset, one
    `SendMessage`-resume recovered the single dirty clone and the run graceful-stopped
    cleanly — **idempotency held**. Rough scaling read: run 2 = 6h ×1-ingest ≈ $211/
    session-meter; run 3 ≈ 9.5h ×2-ingest ≈ ~3x that volume before the weekly wall from
    a 16%-remaining start.

## Effective rule

- Discovery refresh daily (stale_hours=24), newest-30 per channel; `--full`
  enumeration only targeted per clone.
- Time-box default 6h until ≥3 calibration data points exist; then set the time-box
  from the observed hours→usage curve to land at ~80% weekly usage.
- Treat rate-limit stalls as back-off (60 min), never as run failure.
