# Persona Roster — operating schema

Harness-neutral operating rules for this repo (same pattern as the clone repos:
`AGENTS.md` is canonical, `CLAUDE.md` is a stub importing it). This repo is the
**orchestration layer** over independent persona clones — the agent operating system:
personas (clones) → functional roles → teams → router → pipelines → mandatory wiki
persistence.

## Map

| Layer | Files |
|---|---|
| Registry | `roster.json` (clones: slug/domains/strong_for/weak_for/status/tier) |
| Teams + roles | `teams.json` (declarative; validated by `tools/validate.py`) |
| Role prompts | `orchestrator/moderator-prompt.md`, `orchestrator/roles/*.md` |
| Procedures | `orchestrator/router.md` · `pipelines.md` · `roundtable.md` · `knowledge-commit.md` · `composition-modes.md` |
| Entry points | `.claude/commands/`: `/council` `/work` `/plan` `/run-plan` `/review` `/wiki` (installed user-globally) · `/setup` `/add-clone` `/refresh-sources` `/roster-loop` (roster-repo only) |
| Wiki (roster memory) | `index.md` · `log.md` · `STATE.md` · `wiki/decisions/` · `wiki/learnings/` · `plans/` |
| Autopilot | `/roster-loop` (time-boxed cross-clone ingest dispatcher, run via `/loop /roster-loop`) · `autopilot.config.json` (policy parameters) · `autopilot/journal.jsonl` (operational memory, via `tools/autopilot_journal.py`) · policy: `wiki/decisions/2026-07-19-ingest-scheduling-policy.md` |
| Tools | `tools/route.py` (routing) · `validate.py` (configs/wiki/done-gate) · `roster_status.py` (clone readiness, backlog/freshness, maturity target) · `refresh_sources.py` (discovery refresh: new videos → clone ledgers) · `autopilot_journal.py` · `gen_agents.py` · `install_global.py` (user-global shims → use from any project) · `clone_all.py` · `tools/tests/` |

## Hard rules (superset of the clone rules)

1. **One repo = one person.** Clones exchange statements, never wikis. No merged
   super-brain; synthesis happens at runtime (moderator), never in the data.
2. **Citations preserved end-to-end**; a clone without grounding deflects, the moderator
   marks the seat. Skip non-`active` clones (reserved seats).
3. **Council decides, executive executes, review checks independently.** At least one
   review seat was not involved in creation.
4. **Knowledge persistence is part of the definition of done** — every routed workflow
   ends with the `orchestrator/knowledge-commit.md` procedure and must pass
   `python tools/validate.py --done`. The user never triggers persistence manually.
5. **Read before work.** STATE.md + relevant decisions/learnings load before councils or
   execution (targeted via index, never the whole wiki).
6. **Own evidence outranks persona defaults.** `wiki/learnings/` effective rules go into
   every seat's brief; divergence from persona advice is noted, not hidden.
7. **No hub pollution.** Durable cross-project insights are flagged `hub-candidate` in
   the log; the second-brain hub PULLS them via its sync — never write there directly.
8. **Automatic selection is the default; parameters are overrides**
   (`--team/--include/--exclude/--depth` only).
9. **No persona theatre.** Argue with evidence and trade-offs; persona names appear for
   attribution and dissent.
10. **Language:** repo content in English (matching the clone family); converse with the
    user in their language.
11. `log.md` is **append-only**; decisions and dissent are never deleted, only
    superseded with a link.

## Wiki conventions (roster instance)

Machine-readable pointer file: `wiki.config.json`. Conventions follow the
second-brain/clone family: kebab-case filenames, YAML frontmatter, Obsidian wikilinks,
absolute dates, contradictions flagged visibly. `log.md` entry format:
`## [YYYY-MM-DD] <type> | <title>` with `<type>` ∈
`council | work | plan | review | wiki | setup`, greppable via `grep "^## \[" log.md`.

## Session start

Read `STATE.md` first (what's in focus, what's next). When resuming ongoing work, also
read the last few log entries. `python tools/validate.py` checks all configs.
