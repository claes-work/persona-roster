#!/usr/bin/env python3
"""Readiness report: how far along is each clone REALLY — and where should effort go?

Inspects every clone repo referenced in roster.json (ledger, synthesis state, compiled
system-prompt, log) and reports build progress next to the registered status —
including mismatches (e.g. roster says 'created' but the repo has a compiled
system-prompt, or vice versa). This is the tool behind "auf welchem Stand ist ein
Klon?" AND the sensor the roster ingest autopilot (/roster-loop) plans with.

Depth metrics:    sources, L2+, synthesis passes, prompt version.
Backlog metrics:  open long-form by priority (P1/P2/P3), open shorts, synthesis debt
                  (ingest batches since the last synthesis pass, from the clone log).
Freshness:        newest `discovered` date in the ledger, open `fresh-upload` rows
                  (recent uploads promoted by tools/refresh_sources.py).
Maturity target:  open P1+P2 == 0 AND synthesis debt == 0 AND compiled prompt
                  (wiki/decisions/2026-07-19-ingest-scheduling-policy.md — "done
                  enough"; the P3/shorts tail is optional depth, not debt).

Usage:
  python tools/roster_status.py          # human-readable table
  python tools/roster_status.py --json   # machine-readable (the autopilot reads this)
"""
import argparse
import csv
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Council capability per registered status (the maturity policy — see
# wiki/decisions/2026-07-18-clone-maturity-policy.md):
CAPABILITY = {
    "active": "full: default council seat (advisor) + operator",
    "bootstrapped": "experimental: seat only via explicit --include, dossier-grounded, advisory only",
    "created": "experimental (thin): seat only via explicit --include; usually still deflects",
    "planned": "none: name only, no repo",
    "deprecated": "none: retired",
}

# Mirrors the clone-side pipeline conventions (tools/ingest_batch.py in each clone):
OPEN_STATUSES = {"L0-discovered", "L1"}
FLAG_RE = re.compile(r"429|no-captions|unavailable|dup-of", re.IGNORECASE)


def ledger_metrics(rows):
    """Backlog + freshness metrics from ledger rows (clone-side semantics)."""
    m = {
        "sources_total": len(rows),
        "sources_l2plus": 0,
        "open_p1": 0, "open_p2": 0, "open_p3": 0, "open_shorts": 0,
        "fresh_open": 0,
        "last_discovered": None,
    }
    for r in rows:
        status = r.get("status", "")
        if status in ("L2", "L3"):
            m["sources_l2plus"] += 1
        disc = (r.get("discovered") or "").strip()
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", disc):
            if m["last_discovered"] is None or disc > m["last_discovered"]:
                m["last_discovered"] = disc
        if status not in OPEN_STATUSES or FLAG_RE.search(r.get("notes") or ""):
            continue
        if "fresh-upload" in (r.get("notes") or ""):
            m["fresh_open"] += 1
        if r.get("type") == "short":
            m["open_shorts"] += 1
        elif r.get("type") == "video":
            prio = r.get("priority", "")
            key = {"1": "open_p1", "2": "open_p2"}.get(prio, "open_p3")
            m[key] += 1
    return m


def synthesis_debt(repo):
    """Ingest-batch log entries since the last synthesis pass (clone-side semantics,
    mirrors ingest_batch.py batches_since_synthesis)."""
    log = repo / "log.md"
    if not log.exists():
        return None
    count = 0
    for line in log.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("## ["):
            low = line.lower()
            if "synthesis" in low:
                count = 0
            elif "ingest |" in low or "| ingest" in low:
                count += 1
    return count


def inspect_clone(c):
    repo = ROOT / c["repo"]
    info = {
        "slug": c["slug"], "name": c["name"], "status": c.get("status"),
        "capability": CAPABILITY.get(c.get("status"), "?"),
        "repo_present": repo.exists(),
        "sources_total": None, "sources_l2plus": None,
        "open_p1": None, "open_p2": None, "open_p3": None, "open_shorts": None,
        "fresh_open": None, "last_discovered": None, "synthesis_debt": None,
        "synthesis_passes": None, "prompt_version": None, "prompt_compiled": False,
        "maturity_target_reached": False,
        "mismatch": None,
    }
    if not repo.exists():
        return info

    ledger = repo / "pipeline" / "ledger.csv"
    if ledger.exists():
        try:
            with ledger.open(encoding="utf-8-sig", newline="") as f:
                rows = list(csv.DictReader(f))
            info.update(ledger_metrics(rows))
        except Exception:
            pass

    info["synthesis_debt"] = synthesis_debt(repo)

    synth = repo / "pipeline" / "synthesis-state.md"
    if synth.exists():
        text = synth.read_text(encoding="utf-8", errors="replace")
        # Formats vary across clones ("synthesis pass 29", "Synthesis pass 11 ran",
        # "pass 11 · system-prompt v12") — take the highest pass number found.
        passes = [int(n) for n in re.findall(r"\bpass (\d+)\b", text, re.IGNORECASE)]
        if passes:
            info["synthesis_passes"] = max(passes)

    prompt = repo / c.get("system_prompt", "persona/system-prompt.md")
    if prompt.exists():
        head = prompt.read_text(encoding="utf-8", errors="replace")[:4000]
        m = re.search(r"(?:Compiled v|\*\*Version: v)(\d+)", head)
        if m:
            info["prompt_version"] = int(m.group(1))
        # a real compiled prompt has substance; the template skeleton is tiny
        info["prompt_compiled"] = m is not None or prompt.stat().st_size > 10_000

    info["maturity_target_reached"] = bool(
        info["prompt_compiled"]
        and info["open_p1"] == 0 and info["open_p2"] == 0
        and (info["synthesis_debt"] or 0) == 0
    )

    compiled, status = info["prompt_compiled"], c.get("status")
    if compiled and status != "active":
        info["mismatch"] = f"repo has a compiled system-prompt but roster says {status!r} — consider status: active"
    elif not compiled and status == "active":
        info["mismatch"] = "roster says 'active' but no compiled system-prompt found — demote or re-sync the repo"
    return info


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)

    roster = json.loads((ROOT / "roster.json").read_text(encoding="utf-8"))
    report = [inspect_clone(c) for c in roster.get("clones", [])]
    planned = [x.get("name") for x in roster.get("planned", [])]

    if a.json:
        print(json.dumps({"clones": report, "planned": planned}, indent=2))
        return 0

    def num(v, missing="-"):
        return v if v is not None else missing

    fmt = "{:<13} {:<8} {:>7} {:>5} {:>5} {:>5} {:>6} {:>5} {:>5} {:>6} {:>10}  {}"
    print(fmt.format("slug", "status", "sources", "L2+", "P1", "P2",
                     "shorts", "debt", "synth", "prompt", "lastdisc", "capability"))
    for i in report:
        print(fmt.format(
            i["slug"], (i["status"] or "?")[:8],
            num(i["sources_total"], "-" if i["repo_present"] else "MISSING"),
            num(i["sources_l2plus"]),
            num(i["open_p1"]), num(i["open_p2"]), num(i["open_shorts"]),
            num(i["synthesis_debt"]), num(i["synthesis_passes"]),
            f"v{i['prompt_version']}" if i["prompt_version"] else ("yes" if i["prompt_compiled"] else "-"),
            i["last_discovered"] or "-",
            i["capability"].split(":")[0] + (" [target]" if i["maturity_target_reached"] else ""),
        ))
        if i["fresh_open"]:
            print(f"  ** {i['slug']}: {i['fresh_open']} fresh upload(s) open (promoted by discovery refresh)")
        if i["mismatch"]:
            print(f"  !! {i['slug']}: {i['mismatch']}")
    if planned:
        print(f"planned (tier 2, no repo yet): {', '.join(planned)}")
    print("\nP1/P2/shorts = OPEN backlog (unflagged rows); debt = ingest batches since last "
          "synthesis pass; lastdisc = newest ledger discovery date.\n"
          "Maturity [target] = P1+P2 drained + debt 0 + compiled prompt — the P3/shorts "
          "tail is optional depth. Threshold to 'active': first synthesis pass compiled "
          "persona/system-prompt.md (v1); for high-stakes councils prefer clones with "
          "multiple passes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
