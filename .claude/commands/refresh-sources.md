---
description: Discovery refresh — pull newly published videos into every clone's ledger (idempotent; fresh uploads get P1). Roster-repo command; the /roster-loop runs this automatically when discovery is stale.
---

Refresh the video backlog of every eligible clone. This is mechanical — the script
does the work; you orient, run, verify, journal.

1. **Orient**: `python tools/autopilot_journal.py status` (when discovery last ran) and
   `python tools/roster_status.py` (current backlog per clone).
2. **Run**: `python tools/refresh_sources.py --commit` ($ARGUMENTS may add
   `--clone <slug>` or `--full`; `--full` also enumerates channels that have ZERO
   ledger rows — that is the clone's Stage A and can take a long while on big
   channels, so only do it deliberately or when the loop's focus policy calls for it).
3. **Verify**: the summary must show per-channel modes and no `!!` errors. New rows
   land as `L0-discovered`; long-form published within the fresh window becomes
   priority 1 with a `fresh-upload` note (`python tools/roster_status.py` shows them
   as `** fresh upload(s) open`). Re-runs are idempotent (+0 everywhere).
4. **Journal**: `python tools/autopilot_journal.py append discovery new=<total_new> fresh=<total_fresh>`.
5. **Persist (standalone runs only — inside /roster-loop the loop's own reporting
   covers this)**: append one roster `log.md` entry
   (`## [YYYY-MM-DD] work | Discovery refresh: +N rows, M fresh-upload`) and run
   `python tools/validate.py --done`. Clone-side ledger commits are already handled
   by `--commit` (commit message is the audit trail; no clone log entries — those
   are reserved for ingest batches, whose count drives the synthesis debt).

Rate-limit rule (from the clone loops): if yt-dlp returns nothing for several
channels in a row, assume throttling — journal a `backoff` event and stop the
refresh gracefully instead of hammering.
