# /work — routed execution: from goal to reviewed artifact

The central executing entry point. The user states a goal; the system classifies it,
picks team/depth automatically, deliberates only as much as the task warrants,
executes, gets independent review, and persists what was learned.

Usage: `/work <goal / task, plus any context>`
Overrides: `--team <id>` · `--include <slugs>` · `--exclude <slugs>` · `--depth fast|standard|deep`

## Steps

1. **Read before work** — `orchestrator/knowledge-commit.md` §Read-before-work. If the
   task targets ANOTHER project (e.g. youtube-engine), also load THAT project's
   CLAUDE.md/AGENTS.md + state/log per its conventions.
2. **Route** — classify per `orchestrator/router.md` (domains, intent, artifact, risk,
   reversibility, complexity, tags), then `python tools/route.py ...` with any
   overrides. Report the routing in 2–4 lines (pipeline, team, seats + why, reviewers).
3. **Run the pipeline** per `orchestrator/pipelines.md` at the chosen depth:
   - **fast:** execute directly (best-fit operator/session voice) → one independent
     reviewer → knowledge commit.
   - **standard:** mini-council (2–4 seats, independent takes → cross-examine) →
     Decision Brief → execute → independent review (team's review seats) → revise
     must-fix findings → knowledge commit.
   - **deep:** do not improvise a big execution inside /work — run the council
     (`/council` flow) and then create a plan (`/plan`); /work executes single work
     packages via `/run-plan`.
4. **Execution rules** — council decides, executive executes: operators
   (`<slug>-operator`) work inside the real target project; artifacts land where the
   target project expects them, never inside clone repos.
5. **Review** — reviewers were not the creators; each reviewer role uses its prompt
   under `orchestrator/roles/`. Must-fix findings get addressed before "done".
6. **Persist (mandatory)** — commit-after-work checklist
   (`orchestrator/knowledge-commit.md`): decision brief (standard+), learnings when
   something reusable emerged, STATE.md, `work |` log entry (with `Knowledge: none`
   verdict when trivial), index for new pages; artifact knowledge goes to the TARGET
   project's wiki when working cross-project. Then `python tools/validate.py --done`
   must pass.

## Observability

Always tell the user, briefly: chosen pipeline + team, seats and why, which wiki pages
were read, what was changed/created, review verdicts, what was persisted where.
