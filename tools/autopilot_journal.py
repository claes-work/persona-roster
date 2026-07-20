#!/usr/bin/env python3
"""Journal + derived state for the roster ingest autopilot (/roster-loop).

The journal (autopilot/journal.jsonl, append-only, committed) is the autopilot's
operational memory: when a run started and with what time-box, what each cycle did,
when discovery last ran, which clones are backing off after rate limits. `status`
derives everything the loop needs for its stop/stale checks in one call — the loop
never parses the jsonl itself.

Events (free-form key=value pairs are allowed on top):
  run-start   timebox_h=6 batch=8     — a /roster-loop run began
  cycle       clone=x stage=B n=8 ... — one executed work unit
  discovery   new=12 fresh=3          — a refresh_sources run
  backoff     clone=x minutes=60      — rate-limit back-off for one clone
  limit       note=...                — an API/usage limit was hit (observability)
  run-end     reason=timebox|drained|user  — the run finished
  usage       observed_pct=34 note=…  — user-reported usage after a run (calibration)

Usage:
  python tools/autopilot_journal.py append <event> [key=value ...]
  python tools/autopilot_journal.py status [--json]
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
JOURNAL = ROOT / "autopilot" / "journal.jsonl"
WORKER_FILE = ROOT / "autopilot" / "worker"


def now() -> datetime.datetime:
    return datetime.datetime.now().astimezone()


def resolve_worker() -> str | None:
    """This machine's worker identity, or None for the unpartitioned default.

    Order: ROSTER_WORKER env (escape hatch) → autopilot/worker file → None.
    None = single-machine default: the committed journal, and ALL clones eligible
    (so a machine that never opts in behaves exactly as before this feature).
    """
    env = os.environ.get("ROSTER_WORKER", "").strip()
    if env:
        return env
    if WORKER_FILE.exists():
        return WORKER_FILE.read_text(encoding="utf-8").strip() or None
    return None


def journal_path() -> pathlib.Path:
    """Per-worker journal when an identity is set (gitignored, local — two machines
    never collide on it); otherwise the committed default journal. The default path
    is the module global so the test-suite can point it at a temp file."""
    w = resolve_worker()
    return ROOT / "autopilot" / f"journal-{w}.jsonl" if w else JOURNAL


def owned_clones(worker: str | None, cfg: dict) -> list[str] | None:
    """Clone slugs this worker may work. None = not partitioned = all clones.
    A named worker missing from a NON-empty assignments map owns nothing — a safety
    default so a mis-set identity can never silently duplicate another worker's clone.
    """
    assignments = cfg.get("workers", {}).get("assignments", {})
    if not worker or not assignments:
        return None
    return assignments.get(worker, [])


def read_events(path: pathlib.Path | None = None) -> list[dict]:
    path = path or journal_path()
    if not path.exists():
        return []
    events = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass  # never let a corrupt line kill the loop
    return events


def cmd_append(event: str, pairs: list[str]) -> int:
    worker = resolve_worker()
    entry = {"ts": now().isoformat(timespec="seconds"), "event": event}
    if worker:
        entry["worker"] = worker
    for p in pairs:
        if "=" not in p:
            print(f"ignoring malformed pair {p!r} (want key=value)", file=sys.stderr)
            continue
        k, v = p.split("=", 1)
        try:
            entry[k] = int(v)
        except ValueError:
            try:
                entry[k] = float(v)
            except ValueError:
                entry[k] = v
    path = journal_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    who = f" [{worker}]" if worker else ""
    print(f"journaled{who}: {entry['event']} @ {entry['ts']}")
    return 0


def parse_ts(s: str) -> datetime.datetime | None:
    try:
        return datetime.datetime.fromisoformat(s)
    except (ValueError, TypeError):
        return None


def derive_status() -> dict:
    events = read_events()
    t_now = now()
    cfg_path = ROOT / "autopilot.config.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8")) if cfg_path.exists() else {}
    worker = resolve_worker()

    st = {
        "now": t_now.isoformat(timespec="seconds"),
        "worker": worker,                            # this machine's identity (null = default)
        "owned_clones": owned_clones(worker, cfg),   # slugs this worker may work (null = all)
        "max_parallel_clones": cfg.get("scheduling", {}).get("max_parallel_clones", 1),
        "run": None,             # active run (started, no run-end after it)
        "last_discovery": None,  # ts + age_h
        "backoffs": [],          # active clone back-offs
        "cycles_this_run": 0,
        "last_run_end": None,
    }

    run_start, run_end = None, None
    for e in events:
        if e["event"] == "run-start":
            run_start, run_end = e, None
        elif e["event"] == "run-end":
            run_end = e

    if run_end:
        st["last_run_end"] = {"ts": run_end.get("ts"), "reason": run_end.get("reason")}
    if run_start and not run_end:
        started = parse_ts(run_start.get("ts", ""))
        timebox = run_start.get("timebox_h", cfg.get("timebox_hours_default", 6))
        elapsed_h = round((t_now - started).total_seconds() / 3600, 2) if started else None
        st["run"] = {
            "started": run_start.get("ts"),
            "timebox_h": timebox,
            "elapsed_h": elapsed_h,
            "over_timebox": elapsed_h is not None and elapsed_h >= float(timebox),
        }
        start_ts = run_start.get("ts", "")
        st["cycles_this_run"] = sum(
            1 for e in events if e["event"] == "cycle" and e.get("ts", "") >= start_ts)

    for e in events:
        if e["event"] == "discovery":
            st["last_discovery"] = e.get("ts")
    if st["last_discovery"]:
        t = parse_ts(st["last_discovery"])
        age_h = round((t_now - t).total_seconds() / 3600, 2) if t else None
        stale_h = cfg.get("discovery", {}).get("stale_hours", 24)
        st["last_discovery"] = {"ts": st["last_discovery"], "age_h": age_h,
                                "stale": age_h is None or age_h >= stale_h}
    else:
        st["last_discovery"] = {"ts": None, "age_h": None, "stale": True}

    backoffs = {}
    for e in events:
        if e["event"] == "backoff" and e.get("clone"):
            t = parse_ts(e.get("ts", ""))
            minutes = e.get("minutes", cfg.get("scheduling", {}).get("backoff_minutes", 60))
            if t:
                backoffs[e["clone"]] = t + datetime.timedelta(minutes=float(minutes))
    st["backoffs"] = [
        {"clone": c, "until": u.isoformat(timespec="seconds")}
        for c, u in backoffs.items() if u > t_now
    ]
    return st


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_append = sub.add_parser("append", help="append one journal event")
    p_append.add_argument("event")
    p_append.add_argument("pairs", nargs="*", metavar="key=value")
    p_status = sub.add_parser("status", help="derived state for the loop")
    p_status.add_argument("--json", action="store_true")
    sub.add_parser("whoami", help="show this machine's worker identity + owned clones")
    p_set = sub.add_parser("set-worker", help="set this machine's worker identity (one-time)")
    p_set.add_argument("name", help="worker name, e.g. sebastian or florian (empty string clears it)")
    a = ap.parse_args(argv)

    if a.cmd == "append":
        return cmd_append(a.event, a.pairs)

    if a.cmd == "set-worker":
        name = a.name.strip()
        if name:
            WORKER_FILE.parent.mkdir(parents=True, exist_ok=True)
            WORKER_FILE.write_text(name + "\n", encoding="utf-8")
            print(f"worker identity set to {name!r} (autopilot/worker). "
                  f"Now just run /loop /roster-loop as usual.")
        elif WORKER_FILE.exists():
            WORKER_FILE.unlink()
            print("worker identity cleared — this machine falls back to the default (all clones).")
        else:
            print("no worker identity was set.")
        return 0

    if a.cmd == "whoami":
        cfg_path = ROOT / "autopilot.config.json"
        cfg = json.loads(cfg_path.read_text(encoding="utf-8")) if cfg_path.exists() else {}
        w = resolve_worker()
        owned = owned_clones(w, cfg)
        print(f"worker: {w or '(default — no identity set)'}")
        if owned is None:
            print("owned clones: all clones")
        elif owned:
            print(f"owned clones: {', '.join(owned)}")
        else:
            print(f"owned clones: NONE — '{w}' is not in autopilot.config.json workers.assignments; "
                  "add it (or clear the identity) or this machine will do nothing")
        print(f"journal: {journal_path().relative_to(ROOT)}")
        return 0

    st = derive_status()
    if a.json:
        print(json.dumps(st, indent=2))
        return 0
    if st["worker"]:
        owned = st["owned_clones"]
        owned_txt = ("all clones" if owned is None
                     else ", ".join(owned) if owned
                     else "NOTHING — not in workers.assignments")
        print(f"worker: {st['worker']} (owns: {owned_txt})")
    if st["run"]:
        r = st["run"]
        flag = "  << TIMEBOX REACHED — stop the run" if r["over_timebox"] else ""
        print(f"run: started {r['started']}, {r['elapsed_h']}h of {r['timebox_h']}h "
              f"time-box, {st['cycles_this_run']} cycle(s){flag}")
    else:
        lre = st["last_run_end"]
        print("run: none active" + (f" (last ended {lre['ts']}, reason={lre.get('reason')})" if lre else ""))
    d = st["last_discovery"]
    print(f"discovery: last {d['ts'] or 'never'}"
          + (f" ({d['age_h']}h ago)" if d["age_h"] is not None else "")
          + ("  << STALE — run refresh_sources" if d["stale"] else ""))
    if st["backoffs"]:
        for b in st["backoffs"]:
            print(f"backoff: {b['clone']} until {b['until']}")
    else:
        print("backoff: none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
