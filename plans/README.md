# Plans

Persistent, resumable work objects — not chat output. Created by `/plan`, executed
package-by-package by `/run-plan`, updated in place. One file per plan:
`<id>.md` where `<id>` = `YYYY-MM-DD-<slug>`.

## Format

```markdown
---
type: plan
id: YYYY-MM-DD-<slug>
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: draft | approved | active | blocked | review | completed | cancelled
team: <teams.json id or "adhoc">
seats: [...]
---

# <Title>

**Goal.** What done looks like.
**Success criteria.** Measurable/checkable conditions.
**Context.** Constraints, decisions in force (link wiki/decisions/), relevant learnings.
**Assumptions / open questions.**

## Work packages
- [ ] WP1 — <deliverable> (owner: <seat/operator>, depends: —)
- [ ] WP2 — <deliverable> (owner: ..., depends: WP1)
...

## Review steps
Which reviewers check what, at which point.

## Progress log
- [YYYY-MM-DD] WP1 done: <one line>. Next: WP2.

## Documentation targets
What gets persisted where when this plan completes (decisions, learnings, state).
```

Rules: `/run-plan` picks the next unblocked unchecked package, executes, reviews,
ticks it, appends to Progress log, updates `updated:`/`status:`, and runs the
knowledge commit. Plans are never silently rewritten — history stays in the file.
