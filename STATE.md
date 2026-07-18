---
type: state
last_updated: 2026-07-18
---

# Project state

Snapshot for fast session resume. Maintained automatically by the knowledge-commit
procedure — details live in the wiki/log, this page only points.

## What this project is

Umbrella orchestrator ("agent operating system") over independent persona-clone repos:
roster registry → teams/roles → router → fast/standard/deep pipelines → mandatory wiki
persistence. See `AGENTS.md`.

## Current focus

- Grow the clone bench: **Hormozi (v35) and Chris Do (v7) are `active`** — councils have
  two real voices. Neil Patel & MKBHD are enumerated but not ingested (0 L2); GaryVee,
  NetworkChuck only scaffolded. Check anytime: `python tools/roster_status.py`.
- Exercise the new skill layer (`/work`, `/council`, `/plan`) on real problems and feed
  `wiki/learnings/`.

## Active decisions

- Roster = bench, council = curated 3–6 non-redundant seats (2026-07-14).
- Flexible composition modes over one fixed council; skills choose the mode (2026-07-14).
- YouTube "what-performs" analytics layer deferred — foundation first (2026-07-14).
- Agent-OS architecture: teams.json + route.py + mandatory knowledge commit
  (2026-07-18, see `wiki/decisions/2026-07-18-agent-os-architecture.md`).
- Clone maturity policy: graded capability, experimental seats via `--include`
  (2026-07-18, see `wiki/decisions/2026-07-18-clone-maturity-policy.md`).

## Open questions

- Which composition mode wins for which problem type — resolve empirically once ≥3
  clones are active (`orchestrator/composition-modes.md`).
- Debate mode: does it need a judge-variant of the moderator prompt? (likely yes).

## Next actions

- Continue Chris Do ingestion (more synthesis passes deepen the v7 prompt).
- Ingest Neil Patel & MKBHD (enumerated, `/clone-setup` + ingest loop pending), then
  GaryVee/NetworkChuck.
- Run a first real `/work` task end-to-end (e.g. from youtube-engine) and record the
  learning; retro the routing per the architecture decision's review trigger.

## Blocked

- Councils beyond two voices blocked on clone ingestion (Neil Patel, MKBHD, GaryVee,
  NetworkChuck not compiled yet).
