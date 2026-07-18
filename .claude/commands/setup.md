# /setup — one-command onboarding for this machine (idempotent)

Sets up the whole agent OS on a fresh machine (e.g. Florian after `git clone`) — or,
when already installed, refreshes and reports instead. Safe to run any number of times;
every underlying step is idempotent.

Usage: `/setup` (run inside the persona-roster repo)

## Steps

1. **Detect state first.** Check: does `clones/` have the clone repos? does
   `.claude/agents/` exist? do `~/.claude/commands/council.md` etc. carry our GENERATED
   marker? Then say clearly which case applies: **fresh install** / **partial** /
   **already installed → refresh mode**.
2. **Pull the clone repos** — `python tools/clone_all.py` (skips existing ones; on
   refresh, additionally offer `git pull` per existing clone to update them).
   Note: clone repos can be large (raw sources are gitignored, but wikis are big) —
   tell the user this step may take a while on first run.
3. **Generate machine-local agents** — `python tools/gen_agents.py` (12 advisor/
   operator files with THIS machine's absolute paths; gitignored build artifact).
4. **Install user-globally** — `python tools/install_global.py` (commands + agents into
   `~/.claude/`, marker-guarded). Report any SKIPPED foreign files.
5. **Validate** — `python tools/validate.py` must pass; fix or report what doesn't.
6. **Readiness report** — `python tools/roster_status.py`: show which clones are
   `active` (council-ready), which are experimental/thin, and any status mismatches
   between roster.json and the actual repos. If a mismatch says a clone earned
   `active` (compiled system-prompt), offer to update roster.json and re-run steps 3–4.
7. **Wrap up.** Tell the user: which commands now work from any project
   (`/work /council /plan /run-plan /review /wiki`), how many voices councils
   currently have, and the next best step (usually: continue ingesting the next clone —
   see `docs/agent-system-guide.md` §9). Append a `setup |` log entry
   (`orchestrator/knowledge-commit.md`) — on pure re-runs with zero changes, note
   `Knowledge: none` and skip the log entry entirely.

## Collaboration guardrails (from README)

- Never run two ingest/synthesis loops on the SAME clone from two machines — split the
  roster between people.
- Pushing ingest work to a clone repo needs collaborator access on that repo.
- `USER.md`-style machine differences don't exist here; everything machine-specific is
  generated, never committed.
