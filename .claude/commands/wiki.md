# /wiki — wiki maintenance & diagnosis (NOT needed for normal persistence)

Normal knowledge capture is AUTOMATIC (`orchestrator/knowledge-commit.md`, enforced by
the done-gate in every skill). This command exists only for maintenance, diagnosis, and
manual special cases.

Usage: `/wiki <status | lint | query "<question>" | repair | capture <note>>`

## Subcommands

- **status** — run `python tools/validate.py` and summarize: config health, STATE.md
  freshness, last log entries (`grep "^## \[" log.md | tail -5`), open decisions
  (status `proposed`/`testing`), active plans, learnings count.
- **lint** — run `python tools/validate.py --wiki`, then a judgment pass: contradictions
  between decisions/learnings, decisions past their `review_trigger`, orphan pages,
  stale STATE.md claims, log entries flagged `hub-candidate` not yet synced by the hub.
  Report findings, propose fixes, apply approved ones, log `wiki | lint`.
- **query "<question>"** — answer from the roster wiki (index → targeted pages), cited
  with paths. For cross-project knowledge use `/brain` (second-brain hub) instead.
- **repair** — fix mechanical damage found by lint (broken index links, malformed
  frontmatter/log headings) without changing meaning; log `wiki | repair`.
- **capture <note>** — manual escape hatch: run the commit-after-work checklist on the
  given note/insight and file it (learning/decision/state/log as applicable). This is
  for out-of-band insights the user wants kept — routed workflows persist on their own.

Every subcommand that changed files appends a `wiki |` log entry.
