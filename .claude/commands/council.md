# /council — convene a council on a decision or question

Convene the right persona clones + roles on a problem and return a synthesized,
attributed recommendation, persisted as a decision record.

Usage: `/council <problem, plus any project context>`
Overrides: `--team <id>` · `--include <slugs>` · `--exclude <slugs>` · `--depth standard|deep`
(auto-selection is the default; councils never run below standard).

## Steps

1. **Read before work** — `orchestrator/knowledge-commit.md` §Read-before-work
   (STATE.md, relevant decisions/learnings; effective rules go into every seat's brief).
2. **Route** — classify per `orchestrator/router.md`, then
   `python tools/route.py --domains ... --intent decide [overrides]`. Report team,
   seats, reserved seats, reviewers, depth in 2–4 lines. If the result says
   `no-grounded-voice`, say so and answer without persona fan-out (plain analysis +
   review roles) instead of simulating ungrounded personas.
3. **Fan-out (independent takes)** — per `orchestrator/roundtable.md`: one
   `<slug>-advisor` per seated clone, concurrently, same problem + the loaded
   effective rules; each seat sees only its own repo, answers cited.
4. **Cross-examine** — standard for every council: each seat gets the others'
   *statements* (never wikis) and critiques/concurs, cited. At `--depth deep`, run the
   full structured debate (adversarial pairing per
   `orchestrator/composition-modes.md` when two seats genuinely oppose).
5. **Synthesize** — the moderator (`orchestrator/moderator-prompt.md`): verdict,
   agreements, attributed disagreements, per-seat contribution, gaps — plus the
   **Decision Record** block.
6. **Persist (mandatory)** — write `wiki/decisions/YYYY-MM-DD-<slug>.md` (dissent
   preserved), update STATE.md active decisions if it changes project direction,
   append the `council |` log entry, update index.md; then run
   `python tools/validate.py --done` — the council is not finished until it passes.
7. **Hand-off** — if the outcome is "do it": offer `/work` (small) or `/plan` (large),
   seeded with the decision record.

## Rules

- Personas exchange statements, not knowledge bases. Citations preserved end-to-end.
- No fabrication; a seat without grounding deflects and the moderator marks the gap.
- Skip non-`active` clones (route.py reports them as reserved seats).
- No persona theatre: argue with evidence; names appear for attribution and dissent.
