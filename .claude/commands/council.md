# /council — run a roundtable of persona clones

Convene the active persona clones on a problem and return a synthesized, attributed
recommendation. Usage: `/council <problem, plus any project context>`.

## Steps
1. Read `roster.json`. Select clones with `status: active` (or the explicit subset the
   user named). Skip `bootstrapped`/`planned` — note them as reserved-but-not-ready.
2. Follow `orchestrator/roundtable.md`:
   - **Fan-out:** spawn ONE advisor per selected clone concurrently (the
     `<slug>-advisor` agents), each given the same problem. They answer in character,
     grounded and cited, seeing only their own repo.
   - **(Optional) cross-examine** for high-stakes decisions: feed each persona the
     others' *statements* (never their wikis) for in-character critique.
3. Run the **moderator** (`orchestrator/moderator-prompt.md`) — a neutral curator — to
   synthesize: verdict, agreements, attributed disagreements, per-persona contribution,
   gaps.
4. If the outcome is "do it," offer to hand the plan to the relevant **operator** agent
   to execute inside the target project.

## Rules
- Personas exchange statements, not knowledge bases. Citations preserved end-to-end.
- No fabrication; a persona without grounding deflects and the moderator marks the gap.
