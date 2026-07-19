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
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
JOURNAL = ROOT / "autopilot" / "journal.jsonl"


def now() -> datetime.datetime:
    return datetime.datetime.now().astimezone()


def read_events() -> list[dict]:
    if not JOURNAL.exists():
        return []
    events = []
    for line in JOURNAL.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass  # never let a corrupt line kill the loop
    return events


def cmd_append(event: str, pairs: list[str]) -> int:
    entry = {"ts": now().isoformat(timespec="seconds"), "event": event}
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
    JOURNAL.parent.mkdir(parents=True, exist_ok=True)
    with JOURNAL.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"journaled: {entry['event']} @ {entry['ts']}")
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

    st = {
        "now": t_now.isoformat(timespec="seconds"),
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
    a = ap.parse_args(argv)

    if a.cmd == "append":
        return cmd_append(a.event, a.pairs)

    st = derive_status()
    if a.json:
        print(json.dumps(st, indent=2))
        return 0
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
