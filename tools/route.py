#!/usr/bin/env python3
"""Deterministic half of the router (see orchestrator/router.md).

The LLM classifies a task (domains, tags, risk, reversibility, complexity, intent);
this script resolves that classification against roster.json + teams.json into a
routed unit of work: team, seated advisors (status-gated), reserved seats, roles,
independent reviewers, and pipeline depth. Pure and testable — no LLM judgment here.

Usage:
  python tools/route.py --domains youtube,title --tags seo --risk low --reversible
  python tools/route.py --team email --include garyvee --exclude neil-patel
  python tools/route.py --domains database,architecture --intent decide

Output: JSON on stdout. Exit 0 = routed; 2 = invalid input (unknown team/slug/value).
"""
import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEPTHS = ("fast", "standard", "deep")
RISKS = ("low", "medium", "high")
ACTIVE = "active"


def load_configs(root=ROOT):
    roster = json.loads((root / "roster.json").read_text(encoding="utf-8"))
    teams = json.loads((root / "teams.json").read_text(encoding="utf-8"))
    return roster, teams


def _clone_map(roster):
    return {c["slug"]: c for c in roster.get("clones", [])}


def select_team(teams, domains, explicit=None):
    """Return (team_id, team_dict, rationale). Highest domain overlap wins; ties break
    by declaration order in teams.json. None if nothing overlaps."""
    if explicit:
        if explicit not in teams["teams"]:
            raise ValueError(f"unknown team: {explicit!r} (known: {', '.join(teams['teams'])})")
        return explicit, teams["teams"][explicit], [f"team {explicit!r}: explicit --team override"]
    best, best_id, best_overlap = None, None, 0
    for tid, t in teams["teams"].items():
        overlap = len(set(t.get("domains", [])) & set(domains))
        if overlap > best_overlap:
            best, best_id, best_overlap = t, tid, overlap
    if best is None:
        return None, None, [f"no team matches domains {sorted(domains)} -> ad-hoc fallback"]
    return best_id, best, [
        f"team {best_id!r}: {best_overlap} domain overlap with {sorted(domains)}"
    ]


def adhoc_members(roster, domains):
    """Fallback: clones whose domains/strong_for overlap the task domains."""
    hits = []
    for c in roster.get("clones", []):
        overlap = (set(c.get("domains", [])) | set(c.get("strong_for", []))) & set(domains)
        if overlap:
            hits.append((c["slug"], sorted(overlap)))
    return hits


def pick_depth(explicit, risk, reversible, complexity, team, intent, rationale):
    if explicit:
        depth = explicit
        rationale.append(f"depth {depth!r}: explicit --depth override")
    elif risk or complexity or (reversible is not None):
        r = risk or "medium"
        cx = complexity or "medium"
        rev = True if reversible is None else reversible
        if r == "high" or not rev:
            depth = "deep"
            rationale.append(f"depth 'deep': risk={r}, reversible={rev}")
        elif r == "low" and cx == "low":
            depth = "fast"
            rationale.append("depth 'fast': low risk, low complexity, reversible")
        else:
            depth = "standard"
            rationale.append(f"depth 'standard': risk={r}, complexity={cx}")
    else:
        depth = (team or {}).get("default_depth", "standard")
        rationale.append(f"depth {depth!r}: team default (no risk flags given)")
    if intent == "decide" and depth == "fast":
        depth = "standard"
        rationale.append("depth bumped to 'standard': councils never run below standard")
    return depth


def route(roster, teams, domains=(), tags=(), team=None, include=(), exclude=(),
          depth=None, risk=None, reversible=None, complexity=None, intent=None):
    domains, tags = list(domains), list(tags)
    clones = _clone_map(roster)
    known_roles = set(teams.get("roles", {}))
    for slug in list(include) + list(exclude):
        if slug not in clones:
            raise ValueError(f"unknown clone slug: {slug!r} (known: {', '.join(clones)})")

    team_id, team_cfg, rationale = select_team(teams, domains, explicit=team)

    if team_cfg is not None:
        members = list(team_cfg.get("default_members", []))
        trigger_tags = set(tags) | set(domains)
        for tag, extra in team_cfg.get("conditional_members", {}).items():
            if tag in trigger_tags:
                for slug in extra:
                    if slug not in members:
                        members.append(slug)
                        rationale.append(f"seat {slug!r}: conditional on tag {tag!r}")
        roles = list(team_cfg.get("roles", ["moderator"]))
        review = list(team_cfg.get("review", ["skeptical-reviewer"]))
    else:
        team_id, team_cfg = "adhoc", {}
        hits = adhoc_members(roster, domains)
        members = [slug for slug, _ in hits]
        for slug, overlap in hits:
            rationale.append(f"seat {slug!r}: ad-hoc domain match {overlap}")
        roles = ["moderator"]
        review = ["skeptical-reviewer"]

    for slug in include:
        if slug not in members:
            members.append(slug)
            rationale.append(f"seat {slug!r}: explicit --include")
    for slug in exclude:
        if slug in members:
            members.remove(slug)
            rationale.append(f"seat {slug!r} removed: explicit --exclude")

    seated, experimental, reserved = [], [], []
    for slug in members:
        c = clones[slug]
        if c.get("status") == ACTIVE:
            seated.append({"slug": slug, "name": c["name"], "agent": f"{slug}-advisor"})
        elif slug in include and c.get("status") in ("bootstrapped", "created"):
            # Maturity policy: a not-yet-compiled clone NEVER joins by default routing,
            # but an explicit --include grants an EXPERIMENTAL seat — advisory only,
            # grounded strictly in whatever wiki dossiers its repo already has, flagged
            # low-confidence, never executive/operator authority.
            experimental.append({"slug": slug, "name": c["name"], "agent": f"{slug}-advisor",
                                 "status": c.get("status")})
            rationale.append(
                f"seat {slug!r}: EXPERIMENTAL (status {c.get('status')!r}, explicitly "
                "included) — dossier-grounded, low-confidence, advisory only"
            )
        else:
            reserved.append({"slug": slug, "name": c["name"], "status": c.get("status")})
    if not seated and not experimental:
        rationale.append(
            "fallback 'no-grounded-voice': no active clone fits — proceed without persona "
            "fan-out (plain session + review roles); do not simulate ungrounded personas"
        )

    depth = pick_depth(depth, risk, reversible, complexity, team_cfg, intent, rationale)

    result = {
        "team": team_id,
        "display_name": team_cfg.get("display_name", "Ad-hoc team"),
        "depth": depth,
        "seated": seated,
        "experimental_seats": experimental,
        "reserved_seats": reserved,
        "roles": [r for r in roles if r in known_roles],
        "review": review,
        "rationale": rationale,
    }
    if not seated and not experimental:
        result["fallback"] = "no-grounded-voice"
    for opt in ("member_roles", "stages", "notes"):
        if opt in team_cfg:
            result[opt] = team_cfg[opt]
    return result


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--domains", default="", help="comma-separated task domains")
    p.add_argument("--tags", default="", help="comma-separated conditional-member tags")
    p.add_argument("--team", help="explicit team override (teams.json id)")
    p.add_argument("--include", default="", help="comma-separated clone slugs to add")
    p.add_argument("--exclude", default="", help="comma-separated clone slugs to remove")
    p.add_argument("--depth", choices=DEPTHS, help="explicit pipeline depth override")
    p.add_argument("--risk", choices=RISKS)
    rev = p.add_mutually_exclusive_group()
    rev.add_argument("--reversible", dest="reversible", action="store_true", default=None)
    rev.add_argument("--irreversible", dest="reversible", action="store_false")
    p.add_argument("--complexity", choices=RISKS)
    p.add_argument("--intent", choices=("decide", "execute", "plan", "review", "research"))
    a = p.parse_args(argv)

    split = lambda s: [x.strip() for x in s.split(",") if x.strip()]
    if not a.team and not split(a.domains):
        p.error("--domains is required unless --team is given")
    try:
        roster, teams = load_configs()
        result = route(
            roster, teams, domains=split(a.domains), tags=split(a.tags), team=a.team,
            include=split(a.include), exclude=split(a.exclude), depth=a.depth,
            risk=a.risk, reversible=a.reversible, complexity=a.complexity, intent=a.intent,
        )
    except ValueError as e:
        print(f"route.py: {e}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
