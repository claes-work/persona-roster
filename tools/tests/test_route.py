#!/usr/bin/env python3
"""Tests for tools/route.py (+ config integrity via the real roster/teams files).

Run:  python -m unittest discover tools/tests
"""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import route  # noqa: E402

ROSTER, TEAMS = route.load_configs()


def seats(result):
    return [s["slug"] for s in result["seated"]]


def reserved(result):
    return [s["slug"] for s in result["reserved_seats"]]


class TeamSelection(unittest.TestCase):
    def test_youtube_domains_pick_youtube_team(self):
        r = route.route(ROSTER, TEAMS, domains=["youtube", "title", "thumbnail"])
        self.assertEqual(r["team"], "youtube")

    def test_email_domains_pick_email_team(self):
        r = route.route(ROSTER, TEAMS, domains=["newsletter", "email"])
        self.assertEqual(r["team"], "email")

    def test_explicit_team_override_wins(self):
        r = route.route(ROSTER, TEAMS, domains=["youtube"], team="growth")
        self.assertEqual(r["team"], "growth")

    def test_unknown_team_raises(self):
        with self.assertRaises(ValueError):
            route.route(ROSTER, TEAMS, domains=["x"], team="nope")

    def test_database_task_needs_no_marketers(self):
        r = route.route(ROSTER, TEAMS, domains=["architecture", "engineering"])
        self.assertEqual(r["team"], "engineering")
        self.assertNotIn("garyvee", seats(r) + reserved(r))
        self.assertNotIn("neil-patel", seats(r) + reserved(r))


class StatusGating(unittest.TestCase):
    def test_only_active_clones_are_seated(self):
        r = route.route(ROSTER, TEAMS, domains=["youtube"])
        active = {c["slug"] for c in ROSTER["clones"] if c["status"] == "active"}
        self.assertTrue(set(seats(r)) <= active)
        # mkbhd/networkchuck are not active yet -> reserved, not seated
        self.assertIn("mkbhd", reserved(r))

    def test_no_grounded_voice_fallback(self):
        r = route.route(ROSTER, TEAMS, domains=["research", "fact-check"])
        # research team has no default clone members -> empty seats, explicit fallback
        self.assertEqual(r["seated"], [])
        self.assertEqual(r.get("fallback"), "no-grounded-voice")


class Overrides(unittest.TestCase):
    def test_include_adds_seat(self):
        r = route.route(ROSTER, TEAMS, domains=["youtube"], include=["garyvee"])
        everywhere = seats(r) + reserved(r) + [s["slug"] for s in r["experimental_seats"]]
        self.assertIn("garyvee", everywhere)

    def test_exclude_removes_seat(self):
        r = route.route(ROSTER, TEAMS, domains=["youtube"], exclude=["networkchuck"])
        self.assertNotIn("networkchuck", seats(r) + reserved(r))

    def test_unknown_slug_raises(self):
        with self.assertRaises(ValueError):
            route.route(ROSTER, TEAMS, domains=["youtube"], include=["elon"])

    def test_conditional_member_joins_on_tag(self):
        base = route.route(ROSTER, TEAMS, domains=["youtube"])
        tagged = route.route(ROSTER, TEAMS, domains=["youtube"], tags=["seo"])
        self.assertNotIn("neil-patel", seats(base) + reserved(base))
        self.assertIn("neil-patel", seats(tagged) + reserved(tagged))


class ExperimentalSeats(unittest.TestCase):
    def test_included_nonactive_clone_gets_experimental_seat(self):
        r = route.route(ROSTER, TEAMS, domains=["youtube"], include=["mkbhd"])
        exp = [s["slug"] for s in r["experimental_seats"]]
        self.assertIn("mkbhd", exp)
        self.assertNotIn("mkbhd", seats(r))
        self.assertNotIn("mkbhd", reserved(r))

    def test_nonactive_default_member_stays_reserved(self):
        r = route.route(ROSTER, TEAMS, domains=["youtube"])
        self.assertIn("mkbhd", reserved(r))
        self.assertEqual(r["experimental_seats"], [])

    def test_experimental_only_council_is_not_no_grounded_voice(self):
        r = route.route(ROSTER, TEAMS, domains=["it", "networking"],
                        include=["networkchuck"])
        self.assertNotEqual(r.get("fallback"), "no-grounded-voice")
        self.assertEqual([s["slug"] for s in r["experimental_seats"]], ["networkchuck"])


class DepthSelection(unittest.TestCase):
    def test_explicit_depth_wins(self):
        r = route.route(ROSTER, TEAMS, domains=["youtube"], depth="deep", risk="low")
        self.assertEqual(r["depth"], "deep")

    def test_high_risk_is_deep(self):
        r = route.route(ROSTER, TEAMS, domains=["pricing"], risk="high")
        self.assertEqual(r["depth"], "deep")

    def test_irreversible_is_deep(self):
        r = route.route(ROSTER, TEAMS, domains=["youtube"], reversible=False)
        self.assertEqual(r["depth"], "deep")

    def test_low_risk_low_complexity_is_fast(self):
        r = route.route(ROSTER, TEAMS, domains=["youtube"], risk="low",
                        reversible=True, complexity="low")
        self.assertEqual(r["depth"], "fast")

    def test_council_floor_is_standard(self):
        r = route.route(ROSTER, TEAMS, domains=["youtube"], risk="low",
                        reversible=True, complexity="low", intent="decide")
        self.assertEqual(r["depth"], "standard")

    def test_team_default_depth_without_flags(self):
        r = route.route(ROSTER, TEAMS, domains=["business-strategy"])
        self.assertEqual(r["depth"], "deep")  # executive default


class ReviewIndependence(unittest.TestCase):
    def test_every_team_has_reviewers(self):
        for tid, t in TEAMS["teams"].items():
            self.assertTrue(t.get("review"), f"{tid} has no review seats")
            outside = [r for r in t["review"] if r not in t.get("default_members", [])]
            self.assertTrue(outside, f"{tid} has no independent reviewer")


class Fallback(unittest.TestCase):
    def test_unknown_domain_builds_adhoc_team(self):
        r = route.route(ROSTER, TEAMS, domains=["homelab"])
        self.assertEqual(r["team"], "adhoc")
        self.assertIn("networkchuck", seats(r) + reserved(r))
        self.assertIn("moderator", r["roles"])
        self.assertTrue(r["review"])


if __name__ == "__main__":
    unittest.main()
