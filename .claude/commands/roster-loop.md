---
description: Roster ingest autopilot — ONE nudge keeps the whole bench fresh and growing. Time-boxed dispatcher over the clones' own ingest loops. Run via "/loop /roster-loop [timebox_hours] [batch_size]".
---

You are the roster AUTOPILOT DISPATCHER. Policy:
`wiki/decisions/2026-07-19-ingest-scheduling-policy.md` (freshness first, then
focus-until-active) as amended by
`wiki/decisions/2026-07-19-parallel-ingest-and-workers.md` (bounded parallelism +
per-machine worker partition). Keep going across wakeups until the time-box is
reached or the bench is drained. **Do not recommend stopping early.**
`$ARGUMENTS`: first number = time-box in hours, second = batch size (defaults from
`autopilot.config.json`).

**Worker & parallelism (both invisible to the user — the command is still just
`/loop /roster-loop`):**
- **Eligible clones = this machine's `owned_clones`** from the status JSON. `null`
  means "not partitioned → all clones" (a single machine that never set an identity —
  unchanged behavior). A second machine (e.g. Florian's) sets its identity once with
  `python tools/autopilot_journal.py set-worker <name>`; from then on it only ever
  works its assigned clones, so two accounts on disjoint clones never duplicate or
  git-conflict. **Never work a clone outside `owned_clones`.**
- **Per iteration, work up to `max_parallel_clones` DISJOINT eligible clones at once**
  (one subagent each, in parallel). This is the speed/throughput lever; the journal is
  a single writer (the dispatcher), so no locking is needed. Two subagents on the SAME
  clone is the one forbidden case (they'd collide on that clone's ledger) — always
  pick distinct clones.

## 0. Orient (every iteration)

1. `python tools/autopilot_journal.py status --json` — active run, elapsed vs
   time-box, discovery staleness, active back-offs, **plus `worker`, `owned_clones`
   (null = all), `max_parallel_clones`**. Everything below treats "eligible clones" as
   `owned_clones` (or all clones when it is null).
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

If journal status shows discovery `stale: true`: refresh discovery for the eligible
clones only. If `owned_clones` is null, run the whole bench once:
`python tools/refresh_sources.py --commit --json`. If partitioned, run it once per
owned clone: `python tools/refresh_sources.py --clone <slug> --commit --json` for each
(a worker must never refresh a clone it does not own — that clone's owner does it).
Then `append discovery new=<total new rows> fresh=<fresh promoted>`. If the refresh
reports enumeration-empty errors on several channels, treat it as throttling:
`append backoff clone=discovery minutes=60` and continue with step 3 (ingest still
works — captions come from different endpoints than enumeration).
This counts as this iteration's work only if it found new rows AND took long;
otherwise continue to step 3 in the same iteration.

## 3. Pick the work units (up to `max_parallel_clones` DISTINCT clones)

Build a set of DISTINCT clones to work this iteration, at most `max_parallel_clones`.
Restrict to eligible clones only: within `owned_clones` (or all clones when null),
skip clones in active back-off (journal) and clones whose `maturity_target_reached`
is true (their P3/shorts tail is optional — only worked when nothing else is
eligible). Fill the set by applying these rules in order; each clone appears at most
once (never two units on the same clone):

1. **Freshness first** (config `freshness_first`): every eligible `active`-status
   clone with `fresh_open > 0` → a batch there (its fresh rows are P1 on their
   channel; tell each executor which channel holds them).
2. **Focus build-out**: walk config `focus_order` and add each eligible clone with
   work until the set is full:
   - `sources_total == 0` but channels are known (SUBJECT.md) → that clone's unit is
     targeted Stage A:
     `python tools/refresh_sources.py --clone <slug> --full --commit` (long — counts
     as one unit; journal it as `cycle clone=<slug> stage=A`).
   - open P1/P2 (or synthesis debt / persona staleness — the clone's own stage
     machine decides) → one clone-loop iteration (step 4).
3. **Set still empty → nothing eligible** → stop per step 1 with `reason=drained`
   (report WHICH clones are blocked and why — e.g. "garyvee: not in this worker's
   assignment", "all owned clones at maturity target").

If fewer than `max_parallel_clones` clones are eligible, just work the ones that are —
do not pad the set or touch a clone twice.

## 4. Execute the units (one subagent PER picked clone, in parallel)

Spawn one general-purpose subagent per clone in the set — **all in a single message
(multiple tool calls) so they run concurrently**. Each works a DIFFERENT clone repo,
so there is no shared-file contention between them. This is ONE level of nesting; the
executor must not add a second one (see the write-directly rule in the brief). Same
brief for each (fill in the placeholders):

> Work inside the clone repo at `<absolute clone path>`. Read its CLAUDE.md /
> AGENTS.md and `.claude/commands/ingest-loop.md`, then execute EXACTLY ONE
> iteration of that loop's stage machine (its "first matching rule wins" selection —
> including Stage S synthesis or Stage P persona refresh when they are due), batch
> size <N>. <If freshness routing chose this clone: "Prefer channel <handle> — it
> has open fresh-upload P1 rows.">
> **Write every source page YOURSELF, sequentially — do NOT spawn a subagent per
> video.** You are already a subagent under a session-wide spawn budget
> (`CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`, default 200); a second nesting level
> multiplies as batch × clones × iterations and is exactly what exhausted that budget
> mid-run before. The clone's Stage B describes per-video subagents for STANDALONE
> runs — collapse that one level when dispatched here and read/write each transcript
> one after another.
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

1. After ALL subagents in the set return, `append cycle clone=<slug>
   stage=<S|P|A|B|C|D> n=<items> note=<one-liner>` **once per clone worked** (the
   journal is single-writer — you, the dispatcher — so these appends are safe and
   never race).
2. Any subagent that reported rate limiting → `append backoff clone=<slug> minutes=60`
   for that clone (later iterations skip it; the back-off expires on its own).
   A subagent that failed outright → same back-off + note; never retry the identical
   unit in a tight loop. Other clones in the set are unaffected.
3. Report one line: which clones ran, counts each, what the next iteration will do.
4. Schedule the next wakeup (delaySeconds ~90) with this same `/loop /roster-loop`
   prompt — UNLESS step 1 stopped the run.

## Safety rails (non-negotiable)

- Every clone-side change is committed+pushed by the executing subagent per the
  clone's own rules; an interruption loses at most one unit per in-flight clone
  (each clone commits independently).
- The roster loop NEVER writes clone wiki/persona content — it dispatches; clones
  self-govern (their loop docs are harness-neutral by design).
- An unexpectedly long gap between wakeups (API usage limit hit mid-run) needs no
  special handling: everything is idempotent — on the next wakeup the stop check
  and journal pick up where things stand. If the harness surfaces an explicit
  usage-limit error, `append limit note=<what it said>` before continuing/stopping
  so calibration data accumulates.
- Discovery full-enumeration (`--full`) only ever targeted (step 3.2), never for
  the whole bench in one iteration.
- **Subagent spawn budget is CUMULATIVE per session, not concurrent.**
  `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` (default 200; recommended to raise to ~1000
  for overnight runs via `.claude/settings.json` `env`, or an exported shell var)
  counts every subagent ever spawned across ALL wakeups of a single `/loop` run and
  never decrements — terminated agents do not free a slot. With
  the write-directly rule above the growth is ~`max_parallel_clones` per iteration, so a
  long night stays well under budget. If a run still ends with `run-end
  reason=subagent-cap`, don't treat it as an error: everything is idempotent — start a
  fresh session and `/loop /roster-loop` resumes exactly from the ledgers (a new session
  resets the counter). `append limit note=<what it said>` first so calibration data
  accumulates.
