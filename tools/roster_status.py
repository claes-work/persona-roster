#!/usr/bin/env python3
"""Readiness report: how far along is each clone REALLY?

Inspects every clone repo referenced in roster.json (ledger, synthesis state, compiled
system-prompt) and reports build progress next to the registered status — including
mismatches (e.g. roster says 'created' but the repo has a compiled system-prompt, or
vice versa). This is the tool behind "auf welchem Stand ist ein Klon?".

Usage:
  python tools/roster_status.py          # human-readable table
  python tools/roster_status.py --json   # machine-readable
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


def inspect_clone(c):
    repo = ROOT / c["repo"]
    info = {
        "slug": c["slug"], "name": c["name"], "status": c.get("status"),
        "capability": CAPABILITY.get(c.get("status"), "?"),
        "repo_present": repo.exists(),
        "sources_total": None, "sources_l2plus": None,
        "synthesis_passes": None, "prompt_version": None, "prompt_compiled": False,
        "mismatch": None,
    }
    if not repo.exists():
        return info

    ledger = repo / "pipeline" / "ledger.csv"
    if ledger.exists():
        try:
            with ledger.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            info["sources_total"] = len(rows)
            info["sources_l2plus"] = sum(1 for r in rows if r.get("status") in ("L2", "L3"))
        except Exception:
            pass

    synth = repo / "pipeline" / "synthesis-state.md"
    if synth.exists():
        text = synth.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"synthesis pass (\d+)", text)
        if m:
            info["synthesis_passes"] = int(m.group(1))

    prompt = repo / c.get("system_prompt", "persona/system-prompt.md")
    if prompt.exists():
        head = prompt.read_text(encoding="utf-8", errors="replace")[:4000]
        m = re.search(r"(?:Compiled v|\*\*Version: v)(\d+)", head)
        if m:
            info["prompt_version"] = int(m.group(1))
        # a real compiled prompt has substance; the template skeleton is tiny
        info["prompt_compiled"] = m is not None or prompt.stat().st_size > 10_000

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

    fmt = "{:<14} {:<13} {:>8} {:>7} {:>7} {:>7}  {}"
    print(fmt.format("slug", "status", "sources", "L2+", "synth", "prompt", "capability"))
    for i in report:
        print(fmt.format(
            i["slug"], i["status"] or "?",
            i["sources_total"] if i["sources_total"] is not None else ("-" if i["repo_present"] else "MISSING"),
            i["sources_l2plus"] if i["sources_l2plus"] is not None else "-",
            i["synthesis_passes"] if i["synthesis_passes"] is not None else "-",
            f"v{i['prompt_version']}" if i["prompt_version"] else ("yes" if i["prompt_compiled"] else "-"),
            i["capability"].split(":")[0],
        ))
        if i["mismatch"]:
            print(f"  !! {i['slug']}: {i['mismatch']}")
    if planned:
        print(f"planned (tier 2, no repo yet): {', '.join(planned)}")
    print("\nThreshold to 'active': first synthesis pass compiled persona/system-prompt.md "
          "(v1). Trust grows with L2+ sources and synthesis passes — for high-stakes "
          "councils prefer clones with multiple passes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
