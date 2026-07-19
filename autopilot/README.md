# Autopilot — operational state of the roster ingest loop

Machine state for `/roster-loop` (see `.claude/commands/roster-loop.md` and the policy
in `wiki/decisions/2026-07-19-ingest-scheduling-policy.md`). Not wiki content — the
wiki records knowledge, this directory records loop operations.

- `journal.jsonl` — append-only event journal (run-start/cycle/discovery/backoff/
  limit/run-end/usage). Written ONLY via `python tools/autopilot_journal.py append …`;
  read ONLY via `… status [--json]`. Committed, so runs are auditable and the loop is
  machine-portable.
- Budget model: **time-boxed** (no reliable API for subscription usage %). The user
  reports observed usage after runs (`append usage observed_pct=… note=…`); the
  calibration evidence lives in `wiki/learnings/roster-ingest-autopilot.md`.
