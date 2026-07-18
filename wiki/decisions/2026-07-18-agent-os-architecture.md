---
type: decision
date: 2026-07-18
status: accepted
team: adhoc
seats: [claude, sebastian]
review_trigger: after the first 3 real /work or /council runs, retro whether routing + depth defaults fit
---

# Agent-OS architecture: teams.json + route.py + mandatory knowledge commit

**Decision.** Extend the roster into a reusable agent operating system as an ADDITIVE
layer: declarative `teams.json` (teams + functional roles), deterministic
`tools/route.py` for team/depth resolution (LLM classifies, Python resolves), five new
entry points (`/work`, `/plan`, `/run-plan`, `/review`, `/wiki`) beside the extended
`/council`, and a roster-level LLM wiki (`index.md`, `log.md`, `STATE.md`,
`wiki/decisions/`, `wiki/learnings/`, `plans/`) whose maintenance is enforced by a
done-gate (`validate.py --done`). Confidence: high for the structure, medium for the
concrete team lineups (untested until more clones are active).

**Context.** Master brief 2026-07-18 ("agent operating system"): councils, executive
work, review, and mandatory knowledge persistence over the existing clone roster.
Existing assets: mature clone layer (provenance, lifecycle, auto-persistence), thin
roster layer, second-brain hub with federation.

**Reasoning.**
- Judgment/mechanics split copies the proven clone-pipeline philosophy (agent judges,
  Python drives state) — makes routing observable and testable.
- Teams/roles as config (not skills) keeps workflows stable while lineups evolve.
- Roster statuses keep their established names (`active` etc.); a rename to
  draft/experimental/validated would churn README, roster.json, and generated agents
  for aesthetics only.
- Persona depth (strong_for/weak_for only) stays out of the roster; clones remain the
  single source of persona truth (gen_agents.py contract).
- No new global knowledge base: second-brain federation already covers it
  (`hub-candidate` flag + hub-side sync).

**Dissent.** none (single-curator decision; flagged for retro via review_trigger).

**Assumptions.** (a) 3–6 non-redundant seats beat headcount (memory 2026-07-14);
(b) the done-gate (today's log entry) is enough enforcement without hooks; (c) domain
keyword overlap is a good-enough team selector until real usage says otherwise.

**Rejected alternatives.**
- Presets as a block inside roster.json (composition-modes open question) — teams carry
  roles/stages/review and outgrew a preset list; own file keeps the registry clean.
- A `.claude/skills/` tree — the repo's established convention is `.claude/commands/`.
- Stop-hooks forcing persistence — too noisy; gate lives in each skill's DoD instead.

**Risks / next experiment.** Routing quality unproven → run 3 real tasks through
`/work` and retro the routing rationale lines; teams.json lineups may need tuning once
Chris Do & Neil Patel go active.

**Affected.** roster.json (additive fields), new: teams.json, wiki.config.json,
AGENTS.md/CLAUDE.md, STATE.md, index.md, log.md, orchestrator/{router,pipelines,
knowledge-commit}.md, orchestrator/roles/*, tools/{route,validate}.py, tools/tests/,
.claude/commands/{work,plan,run-plan,review,wiki}.md, docs/*; extended: /council,
moderator-prompt.md, roundtable.md, README.md.
