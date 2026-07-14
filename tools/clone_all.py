#!/usr/bin/env python3
"""Clone every roster clone repo from GitHub into clones/ (idempotent, cross-platform).

Reads roster.json, derives each GitHub repo name from its 'repo' path, and clones
https://github.com/<owner>/<name>.git into clones/<name>. Skips repos already present.

Owner resolution: $PERSONA_ROSTER_OWNER, else roster.json "github_owner", else claes-work.

Usage:
    python tools/clone_all.py
    PERSONA_ROSTER_OWNER=my-fork python tools/clone_all.py
"""
import json
import os
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> None:
    data = json.loads((ROOT / "roster.json").read_text(encoding="utf-8"))
    owner = os.environ.get("PERSONA_ROSTER_OWNER") or data.get("github_owner") or "claes-work"
    clones = ROOT / "clones"
    clones.mkdir(exist_ok=True)
    for c in data.get("clones", []):
        name = pathlib.PurePosixPath(c["repo"]).name  # basename, separator-agnostic
        dest = clones / name
        if (dest / ".git").exists():
            print(f"exists: {name}")
            continue
        url = f"https://github.com/{owner}/{name}.git"
        print(f"clone:  {url} -> clones/{name}")
        subprocess.run(["git", "clone", url, str(dest)], check=True)
    print("\nDone. Next: python tools/gen_agents.py")


if __name__ == "__main__":
    main()
