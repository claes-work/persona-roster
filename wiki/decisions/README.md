# Decision records

One file per decision: `YYYY-MM-DD-<slug>.md`. Written automatically by the
knowledge-commit step of `/council`, `/work` (standard/deep), and `/plan`. Never
deleted — superseded by a newer record that links back. Dissent is part of the record,
not noise to clean up.

## Format

```markdown
---
type: decision
date: YYYY-MM-DD
status: proposed | accepted | testing | superseded
team: <teams.json id or "adhoc">
seats: [hormozi, skeptical-reviewer, ...]
review_trigger: <condition or date for re-examination, if any>
supersedes: <older record, if any>
---

# <Decision title>

**Decision.** What was decided, 1–3 sentences. Confidence: low | medium | high.

**Context.** Why this came up; constraints that shaped it.

**Reasoning.** The load-bearing arguments (attributed where attribution matters).

**Dissent.** Minority positions, verbatim in spirit, with whose seat and why. `none` if
genuinely unanimous.

**Assumptions.** What must hold for this to be right.

**Rejected alternatives.** What was considered and why it lost.

**Risks / next experiment.** Top risks; the cheapest validation step.

**Affected.** Files, projects, or plans this touches.
```
