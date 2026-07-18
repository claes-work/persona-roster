# /add-clone — onboard a new persona into the roster

The strategy for growing the bench. Registers a new person end-to-end: repo → registry
→ agents → team seating → validation. The heavy knowledge work (ingest/synthesis) still
runs inside the clone's own repo — this command wires everything around it.

Usage: `/add-clone <Full Name>` (run inside the persona-roster repo)

## Steps

1. **Check the bench.** Is the person already in `roster.json` (clones or `planned`)?
   If a clone exists, report its state (`python tools/roster_status.py`) instead of
   duplicating. Also sanity-check fit: which team(s) would seat this person — a voice
   that duplicates an existing seat adds cost, not coverage (3–6 non-redundant seats).
2. **Create the repo** from `persona-clone-template` as its OWN GitHub repository
   (clones stay independent repos forever — never nested into the roster):
   - **Ownership rule:** create under the account you have repo-creation rights on.
     The roster owner (`github_owner` in roster.json, claes-work) creates under that
     account; a collaborator without those rights creates under their OWN account and
     registers it via the per-clone `github` field (step 3) so `clone_all.py` finds it.
   - Preferred: `gh repo create <owner>/<slug>-clone --template claes-work/persona-clone-template --public --clone`
     (template flag is set on GitHub since 2026-07-18). Fallback if gh/template is
     unavailable: `git clone` the template, delete `.git`, `git init`, commit,
     `gh repo create <owner>/<slug>-clone --source . --public --push`.
   - Place/junction it into `clones/<slug>-clone` (gitignored; contents never tracked
     by the umbrella).
3. **Register** in `roster.json`: slug, name, repo path, `domains`, `strong_for` /
   `weak_for` (routing metadata — ask the user 2-3 targeted questions if unclear),
   tier, `status: created`; add `"github": "<owner>/<slug>-clone"` when the repo lives
   outside the default `github_owner`. If the person was in `planned`, move the entry.
   **This registry entry is the distribution mechanism:** once roster.json is pushed,
   every other machine gets the new persona on its next `/setup` (clone_all pulls the
   repo, agents regenerate).
4. **Seat it** in `teams.json`: add the slug to fitting teams — as `default_members`
   only where the voice is clearly core, otherwise as `conditional_members` under a
   sensible tag. Propose the seating to the user before writing (this shapes every
   future council).
5. **Rebuild artifacts** — `python tools/gen_agents.py` + `python tools/install_global.py`.
6. **Validate** — `python tools/validate.py` must pass.
7. **Hand off to ingestion.** Tell the user the clone now holds a *reserved* seat and
   what makes it speak: in the clone repo run `/clone-setup <Full Name>`, then
   `/loop /ingest-loop` until the first synthesis pass compiles
   `persona/system-prompt.md` (that's the `active` threshold). Until then it can join
   councils only via explicit `--include` as a flagged experimental seat.
8. **Persist** — `setup |` log entry (who was added, seating, why), index.md if pages
   were added, STATE.md next actions; `python tools/validate.py --done` must pass.

## Promotion to active (later, when ingestion is done)

`python tools/roster_status.py` flags the moment a clone's repo has a compiled
system-prompt while the roster still lists it lower — then: set `status: active` in
roster.json, re-run steps 5–6, and announce the new council voice. `/setup` performs
this check on every run too.
