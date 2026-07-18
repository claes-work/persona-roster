# Knowledge commit — the mandatory memory layer

The roster's wiki is maintained by the AI, not the user. **No relevant workflow is done
until this procedure ran** — the user never has to say "merk dir das". Skills enforce it
via the done-gate: `python tools/validate.py --done` must pass before a skill reports
completion.

## Read-before-work (start of every routed task)

Load, in this order, only what the task needs (index + targeted pages, never the whole
wiki):

1. `STATE.md` — what the project is, current focus, decisions in force, next actions.
2. `index.md` — locate relevant pages.
3. Relevant `wiki/decisions/` records — decisions in force that constrain this task.
4. Relevant `wiki/learnings/` pages — **own evidence outranks persona defaults**; any
   `effective_rule` on the topic goes into every seat's brief.
5. Last few `log.md` entries when resuming ongoing work
   (`grep "^## \[" log.md | tail -5`).
6. For cross-project or personal context: the second-brain hub via `/brain` (read-only).
7. When the task targets ANOTHER project (operator work): that project's own
   CLAUDE.md/AGENTS.md, wiki/log/state per ITS conventions.

## Commit-after-work (end of every routed task)

Answer the checklist, then write. A `none` verdict is legitimate for trivial tasks — but
the check itself is not skippable, and the log entry records the verdict.

**Checklist:** new facts? assumptions confirmed/refuted? decision taken (incl. rejected
alternatives + dissent)? reusable experience or rule? errors + what fixed them? artifacts
created/changed? open questions? project state changed? plan progress? insight
project-local or hub-worthy (altitude test)?

**Then write (only what applies):**

| What | Where |
|---|---|
| Decision (council/deep work) | `wiki/decisions/YYYY-MM-DD-<slug>.md` (format: `wiki/decisions/README.md`); dissent PRESERVED |
| Operative learning / reusable rule | `wiki/learnings/<topic>.md` — update `effective_rule` when own evidence justifies it |
| Progress on a plan | tick work packages + status in `plans/<id>.md` |
| Project state change | `STATE.md` (focus, active decisions, open questions, next actions, `last_updated`) |
| Always | one `log.md` entry: `## [YYYY-MM-DD] <type> | <title>` + 1–3 lines (types: `council | work | plan | review | wiki | setup`); include `Knowledge: none` when nothing durable emerged |
| New/renamed wiki pages | one-liner in `index.md` |

**Working in another project:** the artifact-related knowledge goes into THAT project's
wiki/log per its conventions; the roster only records orchestration learnings (what team
composition/pipeline worked). Never write into the second-brain hub — flag hub-worthy
insights with `hub-candidate` in the log entry; the hub pulls them on its next sync
(existing federation mechanism).

## Persistence classes (decide before writing)

`temporary` (chat-only, write nothing) · `project-knowledge` · `decision` ·
`operative-learning` · `playbook` (reusable procedure → learnings) · `open-question`
(STATE.md) · `hub-candidate` (stays local, flagged for second-brain sync).

## Own evidence > persona opinion (§ the learning loop)

A learnings page tracks three levels — keep them separate:

```markdown
## Persona view        <- what the clones recommend (cited to their wikis)
## Own evidence        <- what OUR runs/data actually showed (dated, with sample size)
## Effective rule      <- the rule currently in force for THIS project, derived from the above
```

When own evidence and persona view conflict, the effective rule follows the evidence and
notes the divergence. Councils load effective rules into every seat's brief.

## Anti-noise rules

- Trivial task + nothing durable → log line with `Knowledge: none`, nothing else. Never
  invent wiki content to satisfy the gate.
- `log.md` is append-only and terse; `index.md` is curated navigation, not a file dump.
- Never delete a decision or dissent; supersede with a new record that links the old one.
