---
type: decision
date: 2026-07-19
status: accepted
team: adhoc
seats: [claude, sebastian]
amends: 2026-07-19-ingest-scheduling-policy
review_trigger: revisit after the first two-machine run (Sebastian + Florian) and after the first single-machine run with max_parallel_clones>1 — calibration in wiki/learnings/roster-ingest-autopilot.md
---

# Parallel ingest + per-machine worker partition

**Decision.** The roster ingest autopilot (`/roster-loop`) may now work **more than one
clone at a time**, on one machine and across two machines, without changing how the user
starts it (still just `/loop /roster-loop`). This **amends** the "one work unit per
iteration / focus-until-active / parallel ingestion explicitly rejected" stance of
[[2026-07-19-ingest-scheduling-policy]]. Confidence: high on the mechanism (the clone is
already an independent git repo → the natural unit of isolation), medium on the parallelism
parameters (tunable in `autopilot.config.json`).

**Why the reversal.** The earlier policy rejected parallelism to protect the focus goal
(reach a third active council voice fastest) under a single account's token budget. Two
things changed: (1) Sebastian wants maximum ingest throughput and is willing to spend more
tokens concurrently; (2) a second operator (Florian) brings a **separate, largely unused
Claude quota** — capacity that is wasted unless work can be split. Throughput now outranks
strict serial focus.

## The enabling insight: the clone is the atomic unit of parallelism

Verified in the code (2026-07-19): each clone is its own git repo with its own
`pipeline/ledger.csv`, wiki, and remote. Two workers on **different** clones never touch
the same files → zero conflict. Two workers on the **same** clone collide badly: ledger
selection is "next N open rows" with **no row-level lock**, so they would double-ingest and
git-conflict on `ledger.csv` / `index.md` / `log.md`. Therefore: **parallelism is safe iff
each worker/session owns a disjoint set of clones; two units on one clone is the single
forbidden case.** Intra-clone parallelism (one subagent per video in Stage B) already
exists and is unchanged.

## Two mechanisms (both invisible in daily use)

1. **Bounded fan-out on one machine** (`scheduling.max_parallel_clones`, default 2). The
   single dispatcher picks up to N *distinct* eligible clones per iteration (freshness
   first, then `focus_order`) and spawns one subagent each in parallel. One journal writer
   (the dispatcher) → no locking needed. Raising N = more speed + more concurrent token
   burn; lowering to 1 = the old serial behavior.
2. **Per-machine worker partition** (`workers.assignments`). A machine sets its identity
   **once** (`python tools/autopilot_journal.py set-worker <name>`); thereafter it only
   ever works the clones assigned to that worker, and journals to a **local, gitignored**
   `autopilot/journal-<worker>.jsonl` (the ledgers, not the journal, are the source of
   truth for resume — so per-machine journals never need to merge). A machine with **no
   identity** ignores the map and works **all** clones → unchanged single-machine
   behavior. A named worker missing from a non-empty map owns **nothing** (safety: a
   mis-set identity can never silently duplicate another worker's clone).

Initial split (edit to rebalance): sebastian = neil-patel, networkchuck, hormozi;
florian = mkbhd, chris-do. `focus_order` remains the priority ordering *within* each
worker's owned set, so each machine still does freshness-first then focus.

## Cross-machine prerequisites (one-time)

- Florian clones the roster repo (`github.com/claes-work/persona-roster`) and the clone
  repos he owns (`tools/clone_all.py`), runs `tools/install_global.py` + `gen_agents.py`.
- **Florian needs GitHub write access (collaborator) to the clone repos he owns** — that
  is where ingest commits land. This is the only real coordination cost.
- yt-dlp throttling is keyed to IP/account, not git: two machines on **different**
  networks help; on the **same** IP they can hit YouTube's enumeration limit sooner (the
  existing 3-failure back-off rail handles it).

**Alternatives rejected.**
- *Multiple `/roster-loop` sessions on one machine*: they share one worker identity and
  would double-pick clones and collide on the single journal. Fan-out within ONE dispatcher
  gives the same speedup with a single writer — chosen instead.
- *Dynamic git-based claim/lease across machines*: real distributed-locking work (push
  races, TTL leases, stale-claim reclamation) for 6 clones. Static partition is far
  cheaper and the user explicitly wants low cognitive load.
- *Sharding a single clone across workers by channel*: still shares that clone's
  ledger/index/log → push conflicts. Keep the clone atomic across machines.
- *Committing per-worker journals*: append-only file, two machines → merge conflicts for no
  benefit. Gitignored + local; calibration evidence is promoted to the learnings wiki as
  before.

**Dissent.** none recorded. Noted risk (Claude): fan-out re-spreads effort across clones,
partially re-introducing the "thin focus" the prior policy avoided — accepted deliberately
because throughput + a second quota now outrank serial focus, and `focus_order` still
orders each worker's picks. Second risk: same-IP yt-dlp throttling under heavy fan-out —
mitigated by the back-off rail and a modest default (N=2).

**Assumptions.** Each clone stays an independent repo (isolation guarantee); Florian gets
collaborator write on his clones; the ledger remains the exact resume record so local
per-worker journals need no cross-machine merge.
