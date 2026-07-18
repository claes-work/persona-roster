#!/usr/bin/env python3
"""Validate the roster's configuration and wiki health.

Modes:
  python tools/validate.py            # configs + wiki structure (default)
  python tools/validate.py --wiki     # + deeper wiki lint (links, frontmatter, formats)
  python tools/validate.py --done     # + done-gate: today's log entry must exist
                                      #   (skills run this before reporting completion)

Exit 0 = clean (warnings allowed), 1 = errors found, 2 = broken setup.
"""
import argparse
import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATUSES = {"active", "bootstrapped", "created", "planned", "deprecated"}
DEPTHS = {"fast", "standard", "deep"}
DECISION_STATUSES = {"proposed", "accepted", "testing", "superseded"}
PLAN_STATUSES = {"draft", "approved", "active", "blocked", "review", "completed", "cancelled"}

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        err(f"{path.name}: missing")
    except json.JSONDecodeError as e:
        err(f"{path.name}: invalid JSON ({e})")
    return None


def frontmatter(path):
    """Parse simple 'key: value' YAML frontmatter; returns dict (empty if none)."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip()
    return fm


def check_roster(roster):
    slugs = set()
    for c in roster.get("clones", []):
        slug = c.get("slug", "<missing slug>")
        if slug in slugs:
            err(f"roster.json: duplicate slug {slug!r}")
        slugs.add(slug)
        for key in ("name", "repo", "domains", "tier", "status"):
            if key not in c:
                err(f"roster.json[{slug}]: missing key {key!r}")
        if c.get("status") not in STATUSES:
            err(f"roster.json[{slug}]: invalid status {c.get('status')!r} (valid: {sorted(STATUSES)})")
        if not c.get("domains"):
            err(f"roster.json[{slug}]: domains must be non-empty")
        if c.get("status") == "active" and not (ROOT / c.get("repo", "")).exists():
            warn(f"roster.json[{slug}]: active but repo path {c.get('repo')!r} not present on this machine (run tools/clone_all.py)")
    return slugs


def check_teams(teams, slugs):
    roles = teams.get("roles", {})
    for rid, r in roles.items():
        prompt = ROOT / r.get("prompt", "")
        if not r.get("prompt") or not prompt.exists():
            err(f"teams.json roles[{rid}]: prompt file {r.get('prompt')!r} not found")
    known = set(roles)
    for tid, t in teams.get("teams", {}).items():
        loc = f"teams.json[{tid}]"
        if not t.get("domains"):
            err(f"{loc}: domains must be non-empty")
        members = t.get("default_members", [])
        for slug in members:
            if slug not in slugs:
                err(f"{loc}: default member {slug!r} not in roster.json")
        for tag, extra in t.get("conditional_members", {}).items():
            for slug in extra:
                if slug not in slugs:
                    err(f"{loc}: conditional member {slug!r} ({tag}) not in roster.json")
        for role in t.get("roles", []):
            if role not in known:
                err(f"{loc}: role {role!r} not in roles registry")
        review = t.get("review", [])
        if not review:
            err(f"{loc}: review list must be non-empty (independent review is mandatory)")
        for r in review:
            if r not in known and r not in slugs:
                err(f"{loc}: reviewer {r!r} is neither a role nor a clone slug")
        if review and not [r for r in review if r not in members]:
            err(f"{loc}: no independent reviewer — every review seat is also a default member")
        if t.get("default_depth", "standard") not in DEPTHS:
            err(f"{loc}: invalid default_depth {t.get('default_depth')!r}")
        for stage, seats in t.get("stages", {}).items():
            for s in seats:
                if s not in slugs and s not in known:
                    err(f"{loc} stages[{stage}]: {s!r} is neither a clone nor a role")
        for mrole, slug in t.get("member_roles", {}).items():
            if slug not in slugs:
                err(f"{loc} member_roles[{mrole}]: {slug!r} not in roster.json")


def check_wiki_config(cfg):
    w = (cfg or {}).get("wiki", {})
    if not w.get("enabled"):
        warn("wiki.config.json: wiki disabled")
        return w
    for key in ("schema", "index", "log", "project_state"):
        p = ROOT / w.get(key, "")
        if not w.get(key) or not p.exists():
            err(f"wiki.config.json: {key} -> {w.get(key)!r} not found")
    for key in ("decisions", "learnings", "plans"):
        p = ROOT / w.get(key, "")
        if not w.get(key) or not p.is_dir():
            err(f"wiki.config.json: {key} dir -> {w.get(key)!r} not found")
    return w


def lint_wiki(w):
    log_path = ROOT / w.get("log", "log.md")
    if log_path.exists():
        pattern = re.compile(w.get("log_entry_regex", r"^## \[\d{4}-\d{2}-\d{2}\] \w+ \| .+"))
        for i, line in enumerate(log_path.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("## ") and not pattern.match(line):
                err(f"log.md:{i}: malformed entry heading: {line!r}")

    state = ROOT / w.get("project_state", "STATE.md")
    if state.exists():
        fm = frontmatter(state)
        if "last_updated" not in fm:
            err("STATE.md: frontmatter missing last_updated")

    index_path = ROOT / w.get("index", "index.md")
    index_text = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    for target in re.findall(r"\]\(([^)#]+)\)", index_text):
        if not target.startswith(("http://", "https://")) and not (ROOT / target).exists():
            err(f"index.md: broken link -> {target}")

    for sub, statuses, required in (
        ("decisions", DECISION_STATUSES, ("type", "date", "status")),
        ("plans", PLAN_STATUSES, ("type", "id", "status")),
    ):
        d = ROOT / w.get(sub, sub)
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name == "README.md":
                continue
            fm = frontmatter(f)
            for key in required:
                if key not in fm:
                    err(f"{f.relative_to(ROOT)}: frontmatter missing {key!r}")
            if fm.get("status") and fm["status"] not in statuses:
                err(f"{f.relative_to(ROOT)}: invalid status {fm['status']!r}")
            if sub == "decisions" and f.stem not in index_text:
                warn(f"{f.relative_to(ROOT)}: decision not referenced in index.md")

    learn = ROOT / w.get("learnings", "wiki/learnings")
    if learn.is_dir():
        for f in sorted(learn.glob("*.md")):
            if f.name != "README.md" and frontmatter(f).get("type") != "learning":
                warn(f"{f.relative_to(ROOT)}: frontmatter type should be 'learning'")


def check_done(w):
    """Done-gate: a log entry dated today must exist (knowledge commit ran)."""
    log_path = ROOT / w.get("log", "log.md")
    today = datetime.date.today().isoformat()
    text = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if f"## [{today}]" not in text:
        err(f"done-gate: no log.md entry dated {today} — run the knowledge commit "
            "(orchestrator/knowledge-commit.md) before reporting completion")


def main(argv=None):
    p = argparse.ArgumentParser(description="Validate roster configs and wiki health.")
    p.add_argument("--wiki", action="store_true", help="deeper wiki lint")
    p.add_argument("--done", action="store_true", help="done-gate check (today's log entry)")
    a = p.parse_args(argv)

    roster = load_json(ROOT / "roster.json")
    teams = load_json(ROOT / "teams.json")
    wcfg = load_json(ROOT / "wiki.config.json")
    if roster is None or teams is None or wcfg is None:
        for e in errors:
            print(f"ERROR   {e}")
        return 2

    slugs = check_roster(roster)
    check_teams(teams, slugs)
    w = check_wiki_config(wcfg)
    if a.wiki:
        lint_wiki(w)
    if a.done:
        check_done(w)

    for e in errors:
        print(f"ERROR   {e}")
    for wmsg in warnings:
        print(f"warning {wmsg}")
    if not errors and not warnings:
        print("OK — configs and wiki structure are clean")
    elif not errors:
        print(f"OK — {len(warnings)} warning(s), no errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
