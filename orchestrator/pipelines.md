# Pipelines — fast / standard / deep

The three working depths every routed task runs through. Depth is chosen automatically
(rules below), overridable with `--depth fast|standard|deep`.

## Auto-selection rules (applied by tools/route.py)

- `risk: high` OR `reversible: false` → **deep**
- `risk: low` AND `complexity: low` → **fast**
- everything else → **standard**
- A team's `default_depth` applies only when the flags are absent.
- `/council` never goes below **standard** (a council IS deliberation); `/work` may use
  any depth; `/review` runs the review stage standalone.

## Fast path — small, reversible tasks

```
read-before-work (STATE.md + relevant learnings — minutes, not an audit)
→ execute (operator or plain session; single best-fit voice, no council)
→ short independent review (one reviewer from the team's review list)
→ knowledge commit (MANDATORY check; verdict may be "nothing durable" — see knowledge-commit.md)
```

Examples: rewrite a video description, draft subject lines, format a doc, fix a small bug.

## Standard path — relevant operative/creative work

```
read-before-work (STATE.md, index, relevant learnings + decisions)
→ mini-council: 2–4 seats, independent takes (fan-out, no cross-talk)
→ cross-examine: each seat gets the others' STATEMENTS, critiques/concurs, cited
→ moderator synthesis → Decision Brief (lightweight decision record)
→ execution (operator agent(s) or this session, per the brief)
→ independent review (review seats from teams.json; never only the creators)
→ revision (address must-fix findings)
→ knowledge commit (decision brief persisted, learnings updated, log + state)
```

Examples: plan a video, write a newsletter, design a landing page, shape a feature.

## Deep path — strategic, risky, hard-to-reverse

```
context audit (full read: STATE.md, decisions in force, learnings, /brain hub if relevant)
→ research (evidence gathering; /brain, clone wikis, web via /deep-research if needed)
→ full council: independent takes → structured debate (cross-examine is mandatory,
  may run adversarial pairing per composition-modes.md)
→ moderator synthesis → full Decision Record (dissent + review_trigger REQUIRED)
→ execution plan (/plan — persistent plan file in plans/)
→ staged execution (/run-plan, work package by work package)
→ specialized reviews (per teams.json review list + technical/evidence as applicable)
→ validation/tests where the artifact allows it
→ knowledge commit + retrospective (what did the council get right/wrong → learnings)
```

Examples: business model, pricing model, product architecture, brand positioning,
infrastructure migration.

## Council vs executive vs review (separation of powers)

- **Council** (advisors + moderator) analyzes, debates, decides → Decision Brief/Record.
  It does not execute.
- **Executive** (operator agents / this session with tools) executes on the basis of a
  goal, brief, or plan → artifacts.
- **Review** (role seats, minus anyone who created the artifact) independently checks →
  findings. The creator combination never green-lights its own work alone.
- The moderator stays neutral end-to-end. Persona names appear where attribution or
  dissent matters — no persona theatre in outputs.
