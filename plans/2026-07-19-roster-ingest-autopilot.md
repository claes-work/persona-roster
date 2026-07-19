---
type: plan
id: 2026-07-19-roster-ingest-autopilot
created: 2026-07-19
updated: 2026-07-19
status: active
team: adhoc
seats: [operator]
---

# Roster ingest autopilot — keep all personas fresh and growing without gut-feeling

**Goal.** Replace "fight on all fronts by gut feeling" with a roster-level system that
(1) discovers newly published videos per persona automatically, (2) decides *where* to
ingest next according to an explicit policy, (3) runs as a single daily-nudged loop that
drives the existing per-clone ingest machinery, and (4) respects a usage budget so it can
eventually run unattended (local cron first, server later).

**Success criteria.**
- One command (`/roster-loop` or equivalent) advances the whole bench: discovery refresh
  + ingest batches + synthesis checkpoints, no per-clone babysitting.
- `python tools/roster_status.py` shows freshness per clone (open backlog L0, last
  discovery date, open P1/P2) — "where do we stand" answered by one command.
- New videos from active personas (e.g., a fresh Hormozi upload) land in the ledger
  within ~24h of the next loop run, prioritized appropriately.
- The loop stops itself on budget/time threshold or rate limit and resumes cleanly.
- Zero changes to the clone architecture's hard rules (one repo = one person; ledger is
  the source of truth; every batch ends in a pushed commit).

**Context.**
- Clone-side machinery already exists and works: `pipeline/ledger.csv` as source of
  truth, `/ingest-loop` (self-scheduling, stages A–D), `tools/INGEST.md` with a
  harness-neutral opener, `tools/fetch_channel.ps1` → `merge_staging.py` (dedup by id,
  so re-enumeration is idempotent) → `backfill_metadata.py`. Proven 5–7h unattended runs
  on a single clone.
- Gap 1 — discovery: channel enumeration is manual (Stage A only fires when a channel
  has *zero* rows). No re-poll for newly published videos.
- Gap 2 — scheduling: no cross-clone policy. STATE.md priorities exist (Neil Patel &
  MKBHD next) but nothing consumes them.
- Gap 3 — visibility: `roster_status.py` measures depth (L2+, synthesis passes, prompt
  version) but not freshness/backlog.
- Gap 4 — budget: no programmatic view of subscription usage; user calibrates by eye.
- Decisions in force: clone maturity policy
  (`wiki/decisions/2026-07-18-clone-maturity-policy.md`) — `active` threshold = first
  synthesis pass compiled; agent-OS architecture
  (`wiki/decisions/2026-07-18-agent-os-architecture.md`).

**Assumptions / open questions.**
- "100% per persona" needs a definition. Proposal: *maturity target* = all P1+P2
  long-form at L2 + synthesis debt zero + prompt recompiled — NOT all ledger rows
  (Hormozi alone has ~8.5k L0 rows; the P3 tail is optional depth, not debt).
- Exact %-of-weekly-usage is not cleanly scriptable from inside a session (no official
  API for subscription limits). Proxies: time-boxing (known-good 5–7h), token counts
  from local transcripts (`ccusage` / OTel), and treating rate-limit errors as a
  back-off-and-resume signal, not a failure. Open: verify what `claude /usage`-class
  data is accessible headless on the current CLI version.
- Yesterday's limit message was most likely the rolling session window (resets within
  hours), not the weekly cap — loop design must distinguish "back off until reset"
  from "weekly budget spent".
- Quality: L2 ingest is templated and safe to run unattended; synthesis passes are
  judgement-heavy. Start with synthesis checkpoints flagged-but-attended; loosen after a
  few spot-checked unattended passes.
- Discovery frequency: once per day per channel is plenty; more risks yt-dlp throttling
  for zero benefit.

## Work packages

- [x] WP1 — Freshness visibility: extend `tools/roster_status.py` with per-clone
  backlog metrics (L0-discovered count, open P1/P2, newest `discovered` date, synthesis
  debt) so status answers "where should effort go" (owner: operator, depends: —)
- [x] WP2 — Discovery refresh: roster-level skill (e.g. `/refresh-sources`) that, for
  every non-`planned` clone, re-enumerates channels newest-first (yt-dlp
  `--playlist-end N` fast mode) → `merge_staging.py` dedup → `backfill_metadata.py`;
  fresh uploads from active personas get priority promotion (owner: operator,
  depends: —)
- [x] WP3 — Scheduling policy as a decision record: focus-until-active for build-out
  (order per STATE.md: Neil Patel → MKBHD → GaryVee → NetworkChuck) + cheap freshness
  top-ups for already-active clones first in each run; define the per-clone maturity
  target ("done enough") (owner: operator + optional council, depends: WP1)
- [x] WP4 — `/roster-loop`: dispatcher loop in this repo. Per wakeup: (a) discovery
  refresh if stale >24h, (b) else one ingest batch in the focus clone — executed by a
  subagent pointed at the clone repo using the `tools/INGEST.md` harness-neutral
  opener, (c) synthesis checkpoint handling per WP3 policy, (d) stop conditions:
  budget/time reached, rate-limit back-off, or bench drained (owner: operator,
  depends: WP2, WP3)
- [x] WP5 — Budget guard: config (weekly time/token budget, e.g. "stop at ~80%"),
  per-run journal (batches done, tokens if measurable via ccusage), back-off-and-resume
  on rate limit vs. hard stop on weekly budget (owner: operator, depends: WP4)
- [ ] WP6 — Unattended operation: local first (Windows Task Scheduler or Claude Code
  cron running the loop headless once daily), server later (Linux + `claude -p` cron;
  roster is already machine-portable). Auth, git push credentials, yt-dlp cookies are
  the known risks to verify (owner: operator, depends: WP4, WP5)

## Review steps

- After WP2: run discovery refresh against Hormozi + Chris Do; verify the fresh Alex
  video (seen by user 2026-07-19) lands in the ledger with sensible priority and no
  duplicate rows.
- After WP4: one supervised full loop run (2–3h) across ≥2 clones; check clone-side
  done-gates held (ledger/index/log/commit per batch) before any unattended run.
- After WP6: first cron run reviewed next morning via log trails in roster + clones.

## Progress log

- [2026-07-19] Plan created from user's voice-note requirements; current-state analysis
  of clone ingest machinery done (ledger/stages/discovery/done-gate). Next: WP1.
- [2026-07-19] WP1–WP5 implemented in one pass (user approved plan verbatim, budget =
  time-boxing + user-reported calibration). Delivered: extended `roster_status.py`
  (backlog P1/P2/shorts, synthesis debt, fresh uploads, lastdisc, maturity target, and
  a regex fix — chris-do synthesis passes now detected), `tools/refresh_sources.py` +
  `/refresh-sources`, decision record `2026-07-19-ingest-scheduling-policy`,
  `/roster-loop` command, `autopilot.config.json` + `autopilot/journal.jsonl` +
  `tools/autopilot_journal.py`, learning page, 15 new unit tests (32 total green).
  WP2 review step PASSED live: hormozi +32 video/+61 short incl. the same-day video
  "Why AI won't make you rich in 2026" → P1 fresh-upload; re-run +0 (idempotent);
  neil-patel +4/+12, mkbhd +2; all clone ledger changes committed+pushed.
  Next: WP4 review step — first supervised `/loop /roster-loop 2` run, then WP6.

## Documentation targets

- WP3 → `wiki/decisions/` record (scheduling policy + maturity target definition).
- Loop learnings (what batch size / cadence / budget proxy actually works) →
  `wiki/learnings/roster-ingest-autopilot.md` with own-evidence sections.
- STATE.md: focus + next actions track this plan while active.
