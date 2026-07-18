---
type: decision
date: 2026-07-18
status: accepted
team: adhoc
seats: [claude, sebastian]
review_trigger: revisit the experimental-seat rules after the first council that used one
---

# Clone maturity policy: when a persona may sit at the table

**Decision.** Council capability is graded by clone build state, with one hard
threshold and one explicit escape hatch. Confidence: high.

| Status | Council capability |
|---|---|
| `active` | Full: default council seat (advisor) + operator authority. |
| `bootstrapped` / `created` | **Experimental seat, only via explicit `--include`** — advisory only, grounded strictly in whatever wiki dossiers the repo already has, flagged low-confidence in the synthesis; never default-seated, never operator authority. |
| `planned` / `deprecated` | None (reported as reserved/retired). |

**The `active` threshold stays:** first synthesis pass compiled
`persona/system-prompt.md` (v1). Trust above the threshold is graded, not binary —
for high-stakes (deep) councils prefer clones with multiple synthesis passes;
`tools/roster_status.py` makes the real build state (sources, L2+ count, passes,
prompt version) visible and flags roster/repo mismatches.

**Context.** Sebastian's question 2026-07-18: most clones are half-built; what happens
if the system is used NOW? Binary active/skip was safe but wasted partially-built
knowledge (a bootstrapped clone has cited research dossiers); silently seating
half-built clones would violate deflect-over-fabricate.

**Reasoning.** The escape hatch is explicit-only: default routing must stay honest
(reserved seats), but a user who consciously asks for a half-built voice gets it with
its true confidence label — the moderator treats experimental takes as low-confidence
input, and the evidence reviewer audits them like any other claim.

**Dissent.** none.

**Assumptions.** Dossier-grounded answers from uncompiled clones are useful when
labeled; the v1-compile threshold remains the right bar for default seating.

**Rejected alternatives.** (a) Numeric maturity score with auto-seating above a source
count — false precision, the compile step IS the meaningful gate; (b) seating
bootstrapped clones by default with a warning — erodes the deflect-over-fabricate
invariant.

**Risks / next experiment.** Experimental seats might still over-claim → the seat
prompt pins them to dossier citations; first real use reviews this (see
review_trigger). Immediate win recorded: roster_status.py detected Chris Do already
compiled (v7, 378 L2 sources) → promoted to `active` the same day.

**Affected.** tools/route.py (experimental_seats), tools/roster_status.py (new),
roster.json (chris-do → active), .claude/commands/{setup,add-clone}.md (new),
docs/agent-system-guide.md, AGENTS.md, README.md.
