---
description: Roster ingest autopilot — ONE nudge keeps the whole bench fresh and growing. Time-boxed dispatcher over the clones' own ingest loops. Run via "/loop /roster-loop [timebox_hours] [batch_size]".
---

You are the roster AUTOPILOT DISPATCHER. Policy:
`wiki/decisions/2026-07-19-ingest-scheduling-policy.md` (freshness first, then
focus-until-active). One work unit per iteration, keep going across wakeups until the
time-box is reached or the bench is drained. **Do not recommend stopping early.**
`$ARGUMENTS`: first number = time-box in hours, second = batch size (defaults from
`autopilot.config.json`).

## 0. Orient (every iteration)

1. `python tools/autopilot_journal.py status --json` — active run, elapsed vs
   time-box, discovery staleness, active back-offs.
2. `python tools/roster_status.py --json` — backlog, fresh uploads, maturity per clone.
3. Read `autopilot.config.json` (focus_order, freshness_first, batch/backoff defaults).
4. **No active run in the journal?** This is a fresh run: append
   `python tools/autopilot_journal.py append run-start timebox_h=<H> batch=<N>`.

## 1. Stop check (before any work)

If the journal status shows `over_timebox: true` → **graceful stop**:
`append run-end reason=timebox`, then write ONE roster `log.md` entry
(`## [YYYY-MM-DD] work | Autopilot run: <cycles> cycles — <summary from journal>`),
run `python tools/validate.py --done`, report the run summary (cycles per clone,
stages, new discoveries, back-offs), remind the user to report observed usage
(`python tools/autopilot_journal.py append usage observed_pct=<n>` — calibration
evidence goes to `wiki/learnings/roster-ingest-autopilot.md`), and **do not schedule
another wakeup**. Same procedure with `reason=drained` when step 3 finds no work.

## 2. Discovery refresh (when stale)

If journal status shows discovery `stale: true`:
`python tools/refresh_sources.py --commit --json`, then
`append discovery new=<total new rows> fresh=<fresh promoted>`. If the refresh
reports enumeration-empty errors on several channels, treat it as throttling:
`append backoff clone=discovery minutes=60` and continue with step 3 (ingest still
works — captions come from different endpoints than enumeration).
This counts as this iteration's work only if it found new rows AND took long;
otherwise continue to step 3 in the same iteration.

## 3. Pick ONE work unit (first matching rule wins)

Eligibility: skip clones in active back-off (journal) and clones whose
`maturity_target_reached` is true (their P3/shorts tail is optional — only worked
when nothing else is eligible).

1. **Freshness first** (config `freshness_first`): an `active`-status clone has
   `fresh_open > 0` → ingest one batch there (the fresh rows are P1 on their
   channel; tell the executor which channel holds them).
2. **Focus build-out**: first clone in config `focus_order` that is eligible and has
   work:
   - `sources_total == 0` but channels are known (SUBJECT.md) → this iteration's
     unit is targeted Stage A:
     `python tools/refresh_sources.py --clone <slug> --full --commit` (long — one
     unit; journal it as `cycle clone=<slug> stage=A`).
   - open P1/P2 (or synthesis debt / persona staleness — the clone's own stage
     machine decides) → one clone-loop iteration (step 4).
3. **Nothing eligible** → stop per step 1 with `reason=drained` (report WHICH clones
   are blocked and why — e.g. "garyvee: bootstrap pending", "all at maturity target").

## 4. Execute the unit (one subagent, clone-side rules govern)

Spawn ONE general-purpose subagent. Brief (fill in the placeholders):

> Work inside the clone repo at `<absolute clone path>`. Read its CLAUDE.md /
> AGENTS.md and `.claude/commands/ingest-loop.md`, then execute EXACTLY ONE
> iteration of that loop's stage machine (its "first matching rule wins" selection —
> including Stage S synthesis or Stage P persona refresh when they are due), batch
> size <N>. <If freshness routing chose this clone: "Prefer channel <handle> — it
> has open fresh-upload P1 rows.">
> Complete ALL of the clone's own bookkeeping for the stage (ledger, source pages,
> youtube-index, log entry with Synthesis notes, commit, push) exactly per its
> rules. Do NOT schedule wakeups, do NOT start loops, do NOT touch the roster repo.
> Safety rail: 3 consecutive yt-dlp failures → assume rate-limiting, finish the
> bookkeeping for what succeeded and stop.
> Return a compact report: stage run, channel, items processed
> (ingested/skipped/no-captions/dup), open P1/P2 after, synthesis debt, whether you
> hit rate limits, any errors.

The clone repos are the authority on HOW to ingest (hard rule 1: statements, not
wikis — the roster never writes clone wiki content itself; the subagent works under
the clone's own rules).

## 5. Journal + reschedule (every iteration)

1. `append cycle clone=<slug> stage=<S|P|A|B|C|D> n=<items> note=<one-liner>`.
2. Subagent reported rate limiting → `append backoff clone=<slug> minutes=60`
   (next iterations work another clone; the back-off expires on its own).
   Subagent failed outright → same back-off + note; never retry the identical unit
   in a tight loop.
3. Report one line: what ran, counts, what the next iteration will do.
4. Schedule the next wakeup (delaySeconds ~90) with this same `/loop /roster-loop`
   prompt — UNLESS step 1 stopped the run.

## Safety rails (non-negotiable)

- Every clone-side change is committed+pushed by the executing subagent per the
  clone's own rules; an interruption loses at most one unit.
- The roster loop NEVER writes clone wiki/persona content — it dispatches; clones
  self-govern (their loop docs are harness-neutral by design).
- An unexpectedly long gap between wakeups (API usage limit hit mid-run) needs no
  special handling: everything is idempotent — on the next wakeup the stop check
  and journal pick up where things stand. If the harness surfaces an explicit
  usage-limit error, `append limit note=<what it said>` before continuing/stopping
  so calibration data accumulates.
- Discovery full-enumeration (`--full`) only ever targeted (step 3.2), never for
  the whole bench in one iteration.
