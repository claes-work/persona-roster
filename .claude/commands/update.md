---
description: Update the whole roster — git pull --ff-only the roster repo AND every clone repo (idempotent, safe). Roster-repo command; NOT installed globally.
---

Update every repo in the roster: the orchestration repo itself plus all clones. This is
mechanical and safe — the script fast-forwards only, so nothing local is ever clobbered.

1. **Run**: `python tools/pull_all.py` ($ARGUMENTS may add `--clone <slug>` to update a
   single clone, or `--no-roster` to skip the roster repo).
2. **Read the summary** line by line:
   - `PULLED …` — repo advanced to new commits.
   - `ok … already current` — nothing to do (idempotent).
   - `… [dirty]` — repo has uncommitted changes; the pull still succeeded (ff-only), but
     flag it to the user so nothing local is forgotten.
   - `FAIL …` — usually a diverged branch or a pull that would overwrite local work.
     Report it; do NOT force anything. Let the user resolve, then re-run.
3. **No persistence, no done-gate.** This only syncs git state — it produces no artifact
   and writes nothing to the wiki, so skip the knowledge-commit procedure entirely.

Note: `clones/*` are junctions onto the sibling repos in `D:\Dev\*-clone`, so one pull
updates both views. Missing/not-yet-cloned repos are reported as `skip`; run
`python tools/clone_all.py` first to fetch those.
