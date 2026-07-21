#!/usr/bin/env python3
"""Update (git pull --ff-only) the roster repo and every clone repo (idempotent).

Companion to clone_all.py: that one CLONES missing repos, this one PULLS the ones
already present. Reads roster.json for the clone list, resolves each 'repo' relative
path (clones/<name>), and fast-forwards it plus the roster root itself.

Safe by design:
  - Never overwrites local work: uses --ff-only, so a diverged/dirty branch is reported
    and skipped, never force-updated.
  - Skips non-git and missing directories with a note instead of failing the whole run.
  - A single repo's failure does not abort the rest; the exit code reflects any failure.

Usage:
    python tools/pull_all.py                 # roster + all clones
    python tools/pull_all.py --clone chris-do # one clone only (by slug), no roster
    python tools/pull_all.py --no-roster     # all clones, skip the roster repo
"""
import argparse
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _git(repo: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True,
    )


def update(repo: pathlib.Path, label: str) -> bool:
    """Fast-forward one repo. Returns True on success (incl. already-current)."""
    if not (repo / ".git").exists():
        print(f"  skip   {label}: not a git repo ({repo})")
        return True  # not our repo to manage; not a failure

    dirty = bool(_git(repo, "status", "--porcelain").stdout.strip())
    # --no-rebase so a repo configured with pull.rebase=true still fast-forwards
    # instead of erroring on a dirty tree; --ff-only keeps it non-clobbering.
    res = _git(repo, "pull", "--no-rebase", "--ff-only")
    out = (res.stdout + res.stderr).strip()

    if res.returncode != 0:
        note = " [uncommitted changes present]" if dirty else ""
        first = out.splitlines()[0] if out else "unknown error"
        print(f"  FAIL   {label}: {first}{note}")
        return False

    if "Already up to date" in out or "up-to-date" in out:
        print(f"  ok     {label}: already current" + ("  [dirty]" if dirty else ""))
    else:
        summary = next((l for l in out.splitlines() if "|" in l or "files changed" in l or ".." in l), out.splitlines()[0] if out else "updated")
        print(f"  PULLED {label}: {summary.strip()}" + ("  [dirty]" if dirty else ""))
    return True


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--clone", help="update only this clone (slug); implies --no-roster")
    p.add_argument("--no-roster", action="store_true", help="skip the roster repo itself")
    a = p.parse_args(argv)

    data = json.loads((ROOT / "roster.json").read_text(encoding="utf-8"))
    clones = data.get("clones", [])
    ok = True

    print("Updating repos (git pull --ff-only):\n")

    if not a.no_roster and not a.clone:
        ok &= update(ROOT, "roster (persona-roster)")

    for c in clones:
        if a.clone and c["slug"] != a.clone:
            continue
        repo = ROOT / pathlib.PurePosixPath(c["repo"])
        ok &= update(repo, f"{c['slug']} ({c['repo']})")

    if a.clone and not any(c["slug"] == a.clone for c in clones):
        print(f"  ??     no clone with slug '{a.clone}' in roster.json")
        ok = False

    print("\nDone." if ok else "\nDone with errors (see FAIL lines above).")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
