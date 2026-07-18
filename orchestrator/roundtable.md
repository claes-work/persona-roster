# Roundtable — the council harness

How the orchestrator (a plain Claude Code session, or the `/council` command) turns a
problem into a synthesized, multi-persona answer.

> The full council described here is only ONE way to convene the roster. For the broader
> menu — ad-hoc teams, named preset groups, adversarial debates, and the skill layer that
> reaches them — see [`composition-modes.md`](composition-modes.md).

## Inputs
- **problem** — the question/decision, plus any project context (STATE.md + relevant
  decisions/learnings are loaded first — see [`knowledge-commit.md`](knowledge-commit.md)).
- **roster** — which clones sit at the table. Default: resolved by the router
  ([`router.md`](router.md) + `tools/route.py` — team, conditional seats, status
  gating); or an explicit pick like "Hormozi × Neil Patel" / `--team` / `--include`.

## Procedure

1. **Fan-out (independent takes).** Spawn ONE advisor agent per chosen clone,
   concurrently. Each is loaded ONLY with its own clone (system-prompt + read-only wiki).
   Prompt each with the *same* problem. No agent sees another's wiki or answer — this is
   the one-repo-one-person rule at runtime. Each returns: its take (in character) +
   `Sources:` (wiki paths).
2. **Cross-examine (standard for councils; skippable only at fast depth).** Give each
   persona the *others' takes as statements* (never their wikis) and ask it to
   critique/agree, in character, citing its own sources. This surfaces real disagreement
   instead of parallel monologue. At deep depth this becomes a structured debate
   (adversarial pairing — see [`composition-modes.md`](composition-modes.md) mode 4).
3. **Synthesize.** A single **moderator** agent (neutral curator, NOT a persona — see
   `moderator-prompt.md`) combines the takes into one recommendation with per-persona
   attribution and flagged disagreements — plus, for decisions, the Decision Record
   that gets persisted to `wiki/decisions/` (dissent preserved).

## Rules
- Personas exchange **statements, not knowledge bases.**
- Every persona claim stays **cited** to its own wiki; the moderator preserves attribution.
- A persona that lacks grounding **deflects in character** — the moderator marks that seat
  as "no strong basis" rather than inventing coverage.
- **Skip stubbed clones.** A clone whose `system-prompt.md` is uncompiled (`status:
  bootstrapped`) is noted as "seat reserved, not yet knowledgeable" and excluded from
  fan-out until it has a real persona.

## Advisor vs. operator at the table
The roundtable uses **advisor** (read-only) agents. When the outcome is "go do it in a
real project," hand the synthesized plan to the relevant **operator** agent, which works
inside that project with full tools. Council decides; operator executes.
