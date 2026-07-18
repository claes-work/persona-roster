# Composition modes — how clones get convened

_Design direction, not yet built. Captured 2026-07-14 from a brainstorm. The point of
this file: **the fixed, always-same-core council is only ONE way to use the roster.** Once
each clone is a well-built, standalone unit, the real value is the many ways they can be
composed. Decide concretely which modes to implement once the clones exist and we can
test what actually produces the best output._

## The premise

The atomic unit is the **individual, well-built clone** (one repo, one person, its own
cited wiki + system-prompt). Everything below is orchestration *on top of* those units.
Because the units are independent, they recombine freely — that flexibility is the
product, more than any single fixed lineup. So: **don't over-fixate on one permanent
council with the same core members.** Keep the clones sharp and standalone; let the
convening be situational.

## Modes (a menu, not a hierarchy)

1. **Full council (default).** Every `status: active` clone takes a seat; fan-out →
   optional cross-examine → moderator synthesis. Today's `/council` behaviour
   (see [`roundtable.md`](roundtable.md)). Best for broad, cross-domain problems.

2. **Ad-hoc team.** The user names the clones for a specific problem
   ("let Hormozi × Neil Patel work this"). Already supported by the roundtable's explicit
   roster pick. Best when the user already knows whose lens fits.

3. **Preset groups (named, reusable lineups).** Curated subsets saved by use-case, so the
   user invokes a lens instead of remembering who's in it. Draft presets grounded in the
   current roster:
   - **Business** — Hormozi + Chris Do + Neil Patel (offers/sales/scaling + brand/positioning + SEO/traffic).
   - **YouTube / Creator** — MKBHD + GaryVee + NetworkChuck + Neil Patel (production craft + attention + tech-education niche + SEO). Aimed at Sebastian's own channel problems.
   - (more emerge as the roster grows; a preset is just a named list of slugs.)

4. **Debate / adversarial.** Two clones argue *opposite* positions (or the same brief from
   rival philosophies) and the moderator judges the exchange rather than blending it.
   - **Contrast pairing** — two *different* thinkers on one call: e.g. GaryVee vs Hormozi on
     "spend on brand now vs. direct-response now." Surfaces the real trade-off instead of a
     mushy average.
   - **Same-lane pairing** — two *similar* clones to expose fine-grained divergence within a
     domain (where do two marketers actually disagree?).
   - Mechanically this is the roundtable's optional cross-examine step, promoted to the main
     event and given an explicit "argue against" prompt.

5. **1:1 consult.** A single advisor for a single lens (already possible via
   `@<slug>-advisor`). The lightest mode; no synthesis needed.

6. **Operator hand-off.** Any of the above decides; the relevant **operator** agent then
   executes inside the real project. Council decides, operator does. (Already in
   `roundtable.md`.)

## The skill layer (the UX for all of this)

The intended direction: **skills are how the user reaches these modes.** You do your normal
work / ask a question, and depending on the skill invoked you either get a straight answer,
convene the full council, pull up a preset group, or start a debate. The mode is chosen by
the skill, not hand-wired each time. Sketch:
- `/council <problem>` — full council (exists today).
- `/council <preset> <problem>` or dedicated preset skills — a named group.
- a debate skill — `<clone-a> vs <clone-b> <problem>` → adversarial mode.
- ad-hoc — name the slugs inline.

## Invariants (hold in EVERY mode)

These do not change no matter how clones are grouped:
- **One repo = one person.** Clones exchange *statements*, never each other's wikis.
- **Citations preserved.** Every persona claim stays traced to its own wiki; the moderator
  keeps attribution.
- **Deflect over fabricate.** A clone without grounding says so; the moderator marks the
  seat "no strong basis" rather than inventing coverage.
- **Skip stubs.** Uncompiled personas (`status: bootstrapped`) hold a reserved seat, out of
  fan-out until they have a real system-prompt.

## Open questions (resolve empirically, later)

- Which mode yields the best output for which problem type? Unknown until we run real cases.
  Full council vs. a tight preset vs. a debate may each win in different situations.
- How many voices is too many before synthesis gets muddy? (See the roster's memory
  `council-composition-philosophy`: value = non-redundant coverage, not headcount.)
- ~~Should presets live in `roster.json` (machine-readable) or as their own skills?~~
  RESOLVED 2026-07-18: presets grew into full **teams** (`teams.json` — members,
  conditional members, roles, review seats, stages), read by the skills and
  `tools/route.py`. Roster.json stays a pure clone registry.
- Does debate mode need a different moderator prompt (judge, not blender)? Likely yes.

## Status

Updated 2026-07-18 — largely realized by the agent-OS upgrade (see
`wiki/decisions/2026-07-18-agent-os-architecture.md`):
- Mode 1/3 (full council / preset groups) → `/council` + router + `teams.json`.
- Mode 2 (ad-hoc) → `--include/--exclude` overrides + router fallback team.
- Mode 5 (1:1) → unchanged (`@<slug>-advisor`).
- Mode 6 (operator hand-off) → formalized in `pipelines.md` (council decides,
  executive executes, review checks).
- Mode 4 (debate) → partially: deep-depth cross-examine runs adversarial pairing; a
  dedicated judge-moderator variant is still open (see question above).
Which mode wins for which problem type remains to be tested empirically once ≥3 clones
are active.
