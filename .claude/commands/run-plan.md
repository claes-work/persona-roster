# /run-plan — resume and execute an existing plan

Continues a persistent plan exactly where it stands — never re-invents it.

Usage: `/run-plan <plans/<id>.md | plan id | empty: pick the single active plan>`

## Steps

1. **Load state** — STATE.md, then the plan file: status, progress log, unchecked work
   packages, linked decisions. If status is `blocked`, report the blocker and stop
   unless the user unblocks. If no plan matches, list `plans/` and ask.
2. **Pick the next package** — the first unchecked work package whose dependencies are
   done. Confirm scope in one line; set plan `status: active`.
3. **Execute** — route the package like a `/work` task at the package's natural depth
   (usually fast/standard); operators work in the target project. One package per
   iteration — don't drain the whole plan in one pass unless the user asks.
4. **Review** — per the plan's review steps (independent reviewer, must-fix loop).
5. **Update the plan** — tick the package, append to Progress log
   (`[YYYY-MM-DD] WPn done: ... Next: ...`), bump `updated:`; set `status: review` or
   `completed` when the last package closes (then verify success criteria explicitly).
6. **Persist (mandatory)** — knowledge-commit checklist: learnings from the package,
   STATE.md next actions, `plan |` log entry; on completion write the closing decision/
   learning records named under the plan's documentation targets.
   `python tools/validate.py --done` must pass.
7. **Report** — package result, review verdict, plan progress (n/m), next package.
