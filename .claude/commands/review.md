# /review — independent review of an existing artifact

Checks work WITHOUT having created it. Picks the right reviewer mix for the artifact
type and returns concrete, prioritized findings.

Usage: `/review <what to review — file(s), URL, pasted text, or a project path + description>`
Overrides: `--team <id>` · `--include <slugs>` · `--exclude <slugs>` · `--depth fast|standard`

## Steps

1. **Read before work** — STATE.md + the decisions/learnings that constrain this
   artifact (a review against the wrong effective rule is noise); then the artifact
   itself, fully.
2. **Route** — classify the artifact (`orchestrator/router.md`), then
   `python tools/route.py --intent review ...`. Reviewer mix = the team's `review`
   seats + persona seats whose lane the artifact touches. Never seat a reviewer that
   created the artifact in this session.
3. **Fan out reviewers** — concurrently, each with its role prompt
   (`orchestrator/roles/*.md`) or persona advisor, each returning its own verdict +
   findings. Fast depth = one best-fit reviewer.
4. **Merge** — one consolidated report: overall verdict
   (`ship | ship-with-changes | rework`), findings ordered by severity with concrete
   fixes, conflicts between reviewers attributed (not averaged away), what's already
   good.
5. **Persist (mandatory)** — `review |` log entry (verdict + must-fix count; `Knowledge:
   none` when nothing durable); recurring finding-patterns go to `wiki/learnings/`;
   `python tools/validate.py --done` must pass. Fixing the findings is a follow-up
   `/work` (or the user), not part of the review.
