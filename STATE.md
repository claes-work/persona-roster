---
type: state
last_updated: 2026-07-20
---

# Project state

Snapshot for fast session resume. Maintained automatically by the knowledge-commit
procedure — details live in the wiki/log, this page only points.

## What this project is

Umbrella orchestrator ("agent operating system") over independent persona-clone repos:
roster registry → teams/roles → router → fast/standard/deep pipelines → mandatory wiki
persistence. See `AGENTS.md`.

## Current focus

- Grow the clone bench: **Hormozi (v37), Chris Do (v12), Neil Patel (v6) are `active`** —
  councils have three real voices (neil-patel promoted 2026-07-20). MKBHD ingested but no
  compiled prompt yet (274 L2, P2 deep); GaryVee & NetworkChuck only scaffolded (0 L2).
  Check anytime: `python tools/roster_status.py`.
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
- Ingest scheduling policy: freshness first → focus-until-active (neil-patel → mkbhd
  → networkchuck → hormozi/chris-do; GaryVee removed from focus_order 2026-07-19 —
  Sebastian may resume him manually later); maturity target = P1+P2 drained + debt 0 +
  compiled prompt; budget time-boxed with user calibration (2026-07-19, see
  `wiki/decisions/2026-07-19-ingest-scheduling-policy.md`).
- Parallel ingest + worker partition: `/roster-loop` works up to `max_parallel_clones`
  distinct clones per iteration and can split clones across two machines via
  `workers.assignments` (each machine `set-worker` once); no identity = all clones.
  Start command unchanged (2026-07-19, see
  `wiki/decisions/2026-07-19-parallel-ingest-and-workers.md`).

## Open questions

- How to measure subscription usage programmatically for the roster loop's budget guard
  (no official API; candidates: time-boxing, ccusage/OTel token counts, rate-limit
  errors as back-off signal) — see `plans/2026-07-19-roster-ingest-autopilot.md`.
- Which composition mode wins for which problem type — resolve empirically once ≥3
  clones are active (`orchestrator/composition-modes.md`).
- Debate mode: does it need a judge-variant of the moderator prompt? (likely yes).
- Best `max_parallel_clones` value vs token/usage burn and same-IP yt-dlp throttling —
  calibrate on the first fan-out run (default 2).
- Florian two-machine onboarding: needs the roster + his clone repos locally AND
  GitHub collaborator write on those clone repos (only real coordination cost).

## Next actions

- **Autopilot built (WP1–WP5 done 2026-07-19)** — daily nudge: `/loop /roster-loop`
  (time-boxed dispatcher; discovery refresh + focus-until-active ingest via clone
  loops). First supervised run pending (WP4 review step: `/loop /roster-loop 2`),
  then report observed usage for calibration
  (`python tools/autopilot_journal.py append usage observed_pct=<n>`). WP6
  (headless cron local → server) still open: `plans/2026-07-19-roster-ingest-autopilot.md`.
- Clone ingestion now runs THROUGH the autopilot (policy order: neil-patel → mkbhd →
  networkchuck, then deepening hormozi/chris-do; fresh uploads first; GaryVee excluded
  until Sebastian opts him back in). Now parallel-capable per machine + across two.
- ~~Run a first real `/work` task end-to-end~~ **done 2026-07-18** (youtube-engine
  Titelvarianten; learning: `wiki/learnings/work-pipeline-standard.md`). Follow-up: nach
  Livegang des Videos die Titel-Performance messen (48h/7d/28d) und die Learning-Seite
  um Ergebnis-Evidenz ergänzen; Routing-Retro per Architektur-Review-Trigger steht aus.
- Produce the YouTube video about this system once ≥4 clones are active — fully
  pre-planned in `../youtube-engine/videos/geplant/2026-07-18-persona-klone-council/`
  (content inventory, drehplan v0, title hypotheses; update the numbers before filming).

## Blocked

- Councils beyond three voices blocked on clone ingestion (MKBHD has L2 but no compiled
  prompt yet; GaryVee, NetworkChuck not compiled yet).
