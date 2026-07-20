# Index

Catalog of this repo's knowledge and configuration pages. Updated by the
knowledge-commit procedure whenever pages are added or change meaning.

## Governance & procedures

- [AGENTS.md](AGENTS.md) — operating schema (canonical rules; CLAUDE.md imports it)
- [STATE.md](STATE.md) — project state snapshot for session resume
- [orchestrator/router.md](orchestrator/router.md) — task classification → team/depth routing
- [orchestrator/pipelines.md](orchestrator/pipelines.md) — fast/standard/deep working depths
- [orchestrator/roundtable.md](orchestrator/roundtable.md) — council harness (fan-out → cross-examine → synthesis)
- [orchestrator/composition-modes.md](orchestrator/composition-modes.md) — the menu of convening modes
- [orchestrator/knowledge-commit.md](orchestrator/knowledge-commit.md) — mandatory read-before / commit-after memory procedure

## Roles

- [orchestrator/moderator-prompt.md](orchestrator/moderator-prompt.md) — neutral synthesis + decision record
- [orchestrator/roles/skeptical-reviewer.md](orchestrator/roles/skeptical-reviewer.md) — assumption/risk attack
- [orchestrator/roles/evidence-reviewer.md](orchestrator/roles/evidence-reviewer.md) — claim grounding audit
- [orchestrator/roles/editorial-reviewer.md](orchestrator/roles/editorial-reviewer.md) — clarity/structure/tone review
- [orchestrator/roles/technical-reviewer.md](orchestrator/roles/technical-reviewer.md) — correctness/complexity/security review
- [orchestrator/roles/customer-advocate.md](orchestrator/roles/customer-advocate.md) — recipient's-eye review

## Configuration

- [roster.json](roster.json) — clone registry (the bench)
- [teams.json](teams.json) — teams + functional-role registry
- [wiki.config.json](wiki.config.json) — machine-readable wiki layout pointer
- [autopilot.config.json](autopilot.config.json) — ingest-autopilot parameters (time-box, discovery cadence, focus order)
- [autopilot/](autopilot/README.md) — autopilot operational journal (not wiki content)

## Wiki

- [wiki/decisions/](wiki/decisions/README.md) — decision records (append-only, dissent preserved)
  - [2026-07-18-agent-os-architecture](wiki/decisions/2026-07-18-agent-os-architecture.md) — the agent-OS upgrade decisions
  - [2026-07-18-clone-maturity-policy](wiki/decisions/2026-07-18-clone-maturity-policy.md) — graded council capability per clone build state; experimental seats via --include
  - [2026-07-19-ingest-scheduling-policy](wiki/decisions/2026-07-19-ingest-scheduling-policy.md) — autopilot scheduling: freshness first, focus-until-active, maturity target, time-boxed budget (amended below)
  - [2026-07-19-parallel-ingest-and-workers](wiki/decisions/2026-07-19-parallel-ingest-and-workers.md) — bounded fan-out (max_parallel_clones) + per-machine worker partition (workers.assignments) for two-account load-sharing
  - [2026-07-20-skool-premium-community-exit](wiki/decisions/2026-07-20-skool-premium-community-exit.md) — first real deep council (Hormozi × Chris Do): exit the premium Skool community; 60-day transfer window, else honorable sunset; earn-out-vs-clean-sale fork preserved as dissent
  - [2026-07-20-2key-investor-pitch-deck](wiki/decisions/2026-07-20-2key-investor-pitch-deck.md) — /work standard (Hormozi × Chris Do + dual review): confirmation-deck strategy, MESO options (C at 8%), accusation-audit name slide, vehicle/IP answer mandatory
  - [2026-07-20-2key-deal-struktur](wiki/decisions/2026-07-20-2key-deal-struktur.md) — council round 2: ONE lead scenario (priced 150k/10%) + hidden convertible fallback, option B killed (services never in cap table), valuation stack from market research
  - [2026-07-20-2key-werbebudget-25k](wiki/decisions/2026-07-20-2key-werbebudget-25k.md) — growth council: 25k ads = test budget (Rule of 100), scaling = CFA loop; gate contradiction found (3:1 vs 30d payback) -> annual-prepay founding-member fix; two-stage marketer scorecard; print loaded CAC
  - [2026-07-20-2key-zielgruppe-owner-operator](wiki/decisions/2026-07-20-2key-zielgruppe-owner-operator.md) — deep council: ONE avatar (German owner-operator, buys like consumer/expands like business), no B2B sales motion year 1, pilots productized+investor-separated, pre-order avatar test, trademark gate before prepay
- [wiki/learnings/](wiki/learnings/README.md) — operative learnings; persona view vs own evidence vs effective rule
  - [work-pipeline-standard](wiki/learnings/work-pipeline-standard.md) — first real /work runs: seat convergence as signal, functional reviewers earn their keep
  - [roster-ingest-autopilot](wiki/learnings/roster-ingest-autopilot.md) — autopilot cadence/batch/budget evidence (usage calibration accumulates here)
- [plans/](plans/README.md) — persistent, resumable plan objects
  - [2026-07-19-roster-ingest-autopilot](plans/2026-07-19-roster-ingest-autopilot.md) — discovery refresh + cross-clone scheduling + roster-level loop + budget guard + cron path

## Docs

- [docs/agent-system-guide.md](docs/agent-system-guide.md) — user manual for the whole system
- [docs/architecture-report.md](docs/architecture-report.md) — 2026-07-18 analysis, Soll-Ist mapping, migration record
- [README.md](README.md) — project overview + setup
