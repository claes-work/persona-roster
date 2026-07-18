# /plan — create a persistent, resumable plan

For work too large for one `/work` pass. Produces a plan FILE (`plans/<id>.md`), not a
chat answer — `/run-plan` executes it package by package across sessions.

Usage: `/plan <goal, plus context>`
Overrides: `--team <id>` · `--include <slugs>` · `--exclude <slugs>` · `--depth standard|deep`

## Steps

1. **Read before work** — `orchestrator/knowledge-commit.md` §Read-before-work
   (STATE.md, decisions in force, relevant learnings; existing plans in `plans/` — if
   one already covers this goal, extend it instead of creating a duplicate).
2. **Route** — `orchestrator/router.md` + `python tools/route.py --intent plan ...`.
   For risky/irreversible goals (depth deep) run the council first (`/council` flow)
   and seed the plan from its decision record.
3. **Draft the plan** — `plans/YYYY-MM-DD-<slug>.md` in the format of
   `plans/README.md`: goal, success criteria, context (linked decisions/learnings),
   assumptions/open questions, work packages with owners (operator/seat) and
   dependencies, review steps, documentation targets. Status: `draft`.
4. **Skeptical pass** — the skeptical-reviewer role attacks the plan (assumptions,
   sequencing, missing packages); fix must-fix findings.
5. **Approve** — present the plan summary; on user OK set `status: approved`
   (or `active` if execution starts immediately with `/run-plan`).
6. **Persist (mandatory)** — index.md entry for the plan, `plan |` log entry, STATE.md
   (active work / next actions); `python tools/validate.py --done` must pass.
