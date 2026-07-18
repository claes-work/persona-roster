# Architecture report — agent operating system upgrade (2026-07-18)

Analysis of the existing persona-roster ecosystem against the "reusable agent operating
system" target architecture, the requirement mapping, and the migration plan that was
executed. Written before implementation; the "Result" notes were filled in after.

## A. What existed (Ist-Zustand)

### The ecosystem has three layers, two of which were already mature

**1. Clone layer (mature, per-person repos).** Each persona is its own repo built from
[`persona-clone-template`](../../persona-clone-template). A clone already provides:

- **Persona model:** `persona/system-prompt.md` (compiled build artifact, versioned —
  Hormozi is at v35), `biography.md` / `voice.md` / `beliefs.md` / `appearance.md`.
- **Provenance model:** 7 non-negotiable fidelity rules (every claim cited, verbatim vs
  paraphrase marked, opinions dated, contradictions flagged `> ⚠️ CONTRADICTION:`,
  no fabrication, speaker attribution, registry-verified vs self-reported).
- **Maturity lifecycle:** roster `status` (`active | bootstrapped | created | planned`) +
  per-source ingest tiers (L1/L2/L3) + system-prompt version + `wiki/gaps.md`.
- **Onboarding process:** `/clone-setup` → `/loop /ingest-loop` → synthesis checkpoints →
  persona-QA. Documented, semi-automated, interruption-safe (ledger + commit per unit).
- **Automatic persistence:** every ingest/synthesis unit updates `index.md`, appends to
  `log.md`, advances `pipeline/synthesis-state.md`, and commits. Persistence is already
  part of the clone loops' definition of done.

**2. Roster layer (this repo — thin before this upgrade).** `roster.json` registry,
`orchestrator/roundtable.md` (fan-out → optional cross-examine → moderator synthesis),
`orchestrator/moderator-prompt.md`, `/council` command, `tools/gen_agents.py` (generates
advisor + operator agents per clone; agents are a gitignored machine-local build artifact),
`tools/clone_all.py`. Design direction for flexible composition captured in
`orchestrator/composition-modes.md` (uncommitted brainstorm, preserved and now realized).

**3. Knowledge-hub layer (second-brain, mature).** `D:\Dev\second-brain` is the
cross-project LLM wiki hub (raw/wiki/index/log, frontmatter, wikilinks, callout flags).
Federation model: **projects keep their own wikis; the hub PULLS durable knowledge via
sync cursors; projects never write into the hub directly.** The altitude test decides
what gets promoted. Queryable from anywhere via the `/brain` skill + `second-brain`
subagent.

### What was missing (the gap this upgrade fills)

- No roster-level wiki, log, index, decisions, learnings, or project state — council
  results died in chat.
- No team/role configuration; only "all active clones" or ad-hoc picks.
- No functional roles besides the moderator (no independent reviewers).
- No router, no depth tiers, no `/work`, `/plan`, `/run-plan`, `/review` entry points.
- No plans as persistent objects.
- No validation tooling or tests at roster level.
- No CLAUDE.md/AGENTS.md governing this repo.
- No mechanism to weigh **own evidence** against persona recommendations (§19 of the
  target spec).

## B. Requirement mapping (Soll-Ist)

| Requirement (target spec §) | Verdict | Where / decision |
|---|---|---|
| Persona model: domains, strengths, limits, provenance, maturity (§5) | **Present, implemented differently** | Deep persona content lives in each clone repo (fidelity rules, dated beliefs, gaps.md) — richer than the YAML sketch. Roster adds routing metadata only: `strong_for` / `weak_for` per clone in `roster.json`. Status field = lifecycle (added `deprecated` as valid). |
| Source provenance (direct/repeated/plausible/simulated) (§5.2) | **Present (clone layer)** | Fidelity rules 1–7; verbatim vs paraphrase; ✅/📰/🗣️ confidence markers. Not duplicated at roster level. |
| Maturity lifecycle + advisory-only gating (§5.3) | **Present, different names** | `created→bootstrapped→active(→deprecated)` ≈ draft→experimental→active→deprecated. Gating: only `active` clones join fan-out (existing rule, now enforced by `tools/route.py`). |
| Persona onboarding process (§5.4) | **Fully present** | `/clone-setup` + ingest/synthesis loops + persona-QA in the template. Documented in the user guide. |
| Functional roles (§4.2) | **Was missing → added** | `orchestrator/roles/*.md` (skeptical-reviewer, evidence-reviewer, editorial-reviewer, technical-reviewer, customer-advocate). Moderator/synthesizer already existed (`moderator-prompt.md`). Wiki Maintainer / Decision Recorder deliberately NOT persona-like roles — they are the mandatory knowledge-commit procedure (`orchestrator/knowledge-commit.md`) run by the orchestrator itself. |
| Declarative teams (§4.3, §10) | **Was missing → added** | `teams.json`: default/conditional members, roles, stages, domains, review independence. Composition-modes' open question ("presets in roster.json or skills?") resolved: own file, read by skills and `tools/route.py`. |
| Dynamic router (§11) | **Was missing → added** | Judgment split: the LLM classifies the task (`orchestrator/router.md`); `tools/route.py` deterministically maps classification → team/members/depth with status gating, include/exclude, fallback. Testable. |
| Few top-level skills (§8) | **Partly → completed** | `/council` existed (extended); `/work`, `/plan`, `/run-plan`, `/review`, `/wiki` added under `.claude/commands/` (existing convention; no separate skills dir). |
| Simple overrides `--team/--include/--exclude/--depth` (§9) | **Added** | Parsed by all skills, resolved by `tools/route.py`. |
| Council phases: independent → critique → synthesis → decision (§7) | **Partly present → extended** | Fan-out + optional cross-examine + moderator existed. Now: cross-examine standard at standard/deep depth; moderator additionally emits a persistent Decision Record (dissent preserved). |
| Council vs executive vs review separation (§6) | **Present in principle → formalized** | "Council decides, operator executes" already a rule. Now: review stage must include a reviewer not involved in creation (validated in `tools/validate.py`). |
| Three pipeline depths (§12) | **Was missing → added** | `orchestrator/pipelines.md` (fast/standard/deep) + auto-selection rules + `--depth` override. |
| Mandatory wiki persistence, auto read-before / commit-after (§13) | **Was missing at roster level → added** | Roster gets its own LLM wiki (`index.md`, `log.md`, `wiki/decisions/`, `wiki/learnings/`, `STATE.md`) governed by new `AGENTS.md`. Every skill ends with the knowledge-commit checklist AND a hard gate: `python tools/validate.py --done`. |
| Per-project wiki configs (§13.2) | **Added, convention-first** | `wiki.config.json` describes THIS repo's wiki; when operators work inside another project, they follow that project's own conventions (CLAUDE.md/AGENTS.md, docs/log.md…), probed at runtime — no rigid structure forced. |
| Wiki lint (§13.8) | **Added (roster) / present (clones, hub)** | `python tools/validate.py --wiki` + `/wiki lint`. Clones and second-brain have their own lint operations already. |
| Global vs project knowledge, no pollution (§14) | **Present via second-brain federation — reused, not rebuilt** | Deliberately NOT re-implemented: durable insights go to the roster log/learnings; the second-brain hub pulls via its existing sync-cursor mechanism. Promotion candidates are just log/learnings entries flagged `hub-candidate`. |
| Project state & resume (§15) | **Added** | `STATE.md` (focus, active work, active decisions, open questions, next actions). |
| Plans as persistent objects (§16) | **Added** | `plans/<id>.md` with frontmatter (status lifecycle), work packages as checkboxes; `/run-plan` resumes. |
| Own evidence outweighs personas (§19) | **Added** | `wiki/learnings/` pages carry `persona_view` vs `own_evidence` vs `effective_rule` sections; router/context-load reads them before councils; rule codified in AGENTS.md. |
| Validation + tests (§21.3, §21.4) | **Added** | `tools/validate.py` (roster/teams/roles/wiki/plans/done-gate), `tools/test_route.py` (unittest: classification mapping, team selection, overrides, gating, fallback). |
| User documentation (§20) | **Added** | `docs/agent-system-guide.md`, linked from README. |
| No persona theatre (§21.6) | **Adopted** | Moderator/decision outputs argue by evidence; names appear only for attribution/dissent. Carried into all new role prompts. |

### Deliberately NOT adopted

- **A global knowledge base inside this repo** — the second-brain hub + federation
  already solves this better (altitude test, sync cursors, one hub only).
- **YAML persona schemas duplicating clone content** — would create a second source of
  truth; clones' system-prompts stay canonical (gen_agents.py already treats them so).
- **Renaming existing statuses to draft/experimental/validated** — existing lifecycle
  names are established across roster.json, README, and generated agents.
- **A separate `synthesizer` role file** — `moderator-prompt.md` already is exactly that.
- **Hooks forcing persistence on every session stop** — too noisy; the done-gate
  (`validate.py --done`) inside each skill's definition of done is the enforcement point.
- **Teams for domains with no grounded voice** (e.g. a "legal council") — teams only
  exist where the bench can actually staff them; engineering-council is role-heavy with
  conditional persona seats, honestly reflecting current coverage.

## C. Migration plan (executed)

Order: config → wiki layer → tools → skills → orchestrator docs → user docs → tests.
All changes additive; no existing file deleted or renamed; uncommitted user work
(`orchestrator/composition-modes.md`, roundtable pointer) preserved and built upon.
Backward compatibility: `/council <problem>` unchanged in its simplest form;
`gen_agents.py` unaffected (ignores new roster.json keys); README's documented flows
still work.

Known risks accepted: (a) LLM-side classification is not unit-testable — mitigated by
making the deterministic half (`route.py`) testable and the judgment half a short,
explicit procedure; (b) new statuses/fields in roster.json must stay in sync with
`validate.py` — validation is part of `/wiki status`.
