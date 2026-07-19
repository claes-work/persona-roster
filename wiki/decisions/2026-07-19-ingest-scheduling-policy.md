---
type: decision
date: 2026-07-19
status: accepted
team: adhoc
seats: [claude, sebastian]
review_trigger: revisit after the first 3 unattended /roster-loop runs (calibration data in wiki/learnings/roster-ingest-autopilot.md)
---

# Ingest scheduling policy: freshness first, then focus-until-active

**Decision.** The roster ingest autopilot (`/roster-loop`) schedules cross-clone work
by three rules, in order. Confidence: high on the rules, medium on the parameters
(they live in `autopilot.config.json` and are expected to be tuned).

1. **Freshness first.** Newly published videos of `active` clones are ingested before
   any build-out work — a stale flagship clone is worse than a slow build-out.
   Discovery refresh (`tools/refresh_sources.py`) runs when >24h stale; recent
   uploads (≤14 days) are promoted to P1 with a `fresh-upload` note.
2. **Focus-until-active.** Build-out effort goes to ONE clone at a time until it
   crosses the `active` threshold (first compiled synthesis pass —
   [[2026-07-18-clone-maturity-policy]]), in this order: **neil-patel → mkbhd →
   garyvee → networkchuck**, then deepening hormozi/chris-do. Rationale: councils are
   blocked on a third voice; one more `active` clone beats marginal depth anywhere
   else. Parallel "fight on all fronts" ingestion is explicitly rejected.
3. **Maturity target = "done enough", not "everything".** A clone is at target when
   open P1+P2 long-form = 0 AND synthesis debt = 0 AND the system-prompt is compiled.
   The P3/long-tail and shorts are optional depth, worked only when nothing else is
   eligible. "100% of the ledger" is NOT a goal (Hormozi alone has ~8.5k open L0
   rows — that tail is an option pool, not debt).

**Execution model.** The roster dispatches; clones self-govern. One work unit per
loop iteration = one iteration of the target clone's OWN ingest-loop stage machine
(including its Stage S synthesis and Stage P persona refresh when due), executed by a
subagent under the clone's rules. Synthesis runs unattended — this is the status quo
of the per-clone loops (29 passes on Hormozi ran this way); periodic spot-checks of
synthesis quality are the mitigation, not attended checkpoints.

**Budget model: time-boxed, user-calibrated.** There is no reliable programmatic API
for subscription usage %. The loop therefore runs against a time-box (default 6h,
config/argument), journals every unit (`autopilot/journal.jsonl`), and the user
reports observed usage after runs; the mapping "hours → usage %" accumulates as own
evidence in [[../learnings/roster-ingest-autopilot]] until the time-box can be set to
hit ~80% weekly usage deliberately. Rate limits are a back-off-and-resume signal
(rolling session window), never treated as "budget spent".

**Context.** Sebastian's requirement (2026-07-19, voice note): personas must stay
current automatically; ingest effort needs a plan instead of gut feeling; one daily
nudge should keep everything moving; later cron/server. Plan:
`plans/2026-07-19-roster-ingest-autopilot.md`.

**Alternatives rejected.**
- *Round-robin across all clones*: spreads effort thin, delays the third active
  council voice — the actual bottleneck.
- *Percentage-of-ledger completion targets*: punishes clones with huge back catalogs;
  the P1/P2 + synthesis-debt target measures usable maturity instead.
- *Token-metered budget (ccusage/OTel)*: measurement exists but maps unreliably to
  the subscription limit; time-boxing + user calibration is simpler and converges.

**Dissent.** none recorded; noted risk (Claude): unattended synthesis quality drift —
mitigated by spot-checks and the review_trigger above.

**Assumptions.** Clone ingest-loop docs remain harness-neutral enough for a fresh
subagent to execute one unit faithfully; yt-dlp enumeration once per day stays under
YouTube throttling thresholds.
