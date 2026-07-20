#!/usr/bin/env python3
"""Tests for the roster ingest autopilot building blocks:
roster_status metrics, refresh_sources parsing/promotion, autopilot_journal state.

Run:  python -m unittest discover tools/tests
"""
import datetime
import os
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import autopilot_journal  # noqa: E402
import refresh_sources  # noqa: E402
import roster_status  # noqa: E402


def row(**kw):
    base = {"id": "yt-x", "type": "video", "title": "t", "channel_or_publisher": "@c",
            "url": "u", "published": "2026-01-01", "discovered": "2026-07-01",
            "status": "L0-discovered", "priority": "2", "domains": "", "notes": ""}
    base.update(kw)
    return base


class LedgerMetrics(unittest.TestCase):
    def test_open_counts_by_priority_and_type(self):
        rows = [
            row(id="a", priority="1"),
            row(id="b", priority="2"),
            row(id="c", priority="3"),
            row(id="d", type="short", priority="3"),
            row(id="e", status="L2"),                      # not open
            row(id="f", notes="no-captions"),              # flagged -> not open
            row(id="g", status="skipped"),                 # not open
        ]
        m = roster_status.ledger_metrics(rows)
        self.assertEqual((m["open_p1"], m["open_p2"], m["open_p3"]), (1, 1, 1))
        self.assertEqual(m["open_shorts"], 1)
        self.assertEqual(m["sources_l2plus"], 1)
        self.assertEqual(m["sources_total"], 7)

    def test_fresh_and_last_discovered(self):
        rows = [
            row(id="a", notes="views=5 fresh-upload", discovered="2026-07-19"),
            row(id="b", discovered="2026-07-01"),
            row(id="c", discovered="not-a-date"),
        ]
        m = roster_status.ledger_metrics(rows)
        self.assertEqual(m["fresh_open"], 1)
        self.assertEqual(m["last_discovered"], "2026-07-19")

    def test_synthesis_debt_counts_ingest_since_last_synthesis(self):
        with tempfile.TemporaryDirectory() as d:
            repo = pathlib.Path(d)
            (repo / "log.md").write_text(
                "## [2026-07-01] ingest | batch 1\n"
                "## [2026-07-02] lint | synthesis pass 3\n"
                "## [2026-07-03] ingest | batch 2\n"
                "## [2026-07-04] ingest | batch 3\n",
                encoding="utf-8")
            self.assertEqual(roster_status.synthesis_debt(repo), 2)


class ChannelParsing(unittest.TestCase):
    SUBJECT = (
        "## Content universe\n"
        "### YouTube channels (TARGET = enumerated into the ledger)\n"
        "1. @thefutur `UC-b3c` — 1,177 long-form (2.81M subs) — TARGET\n"
        "2. @TheFuturAcademy `UCqH` — tutorials, low persona value — TARGET\n"
        "   (catalog-only tier; only Chris-featuring items get ingested)\n"
        "3. @SomeOther `UCx` — fan channel, do not ingest\n"
        "- Excluded: @thefuturishere is a legacy vanity URL.\n"
        "### Other platforms (Phase 4)\n"
        "1. @thechrisdo on Instagram — TARGET-looking but wrong section\n")

    LOOP = (
        "### Target channels (the full universe)\n"
        "Live per-channel progress is in the ledger. The channel universe:\n"
        "1. @AlexHormozi    UCUyDOdBWhC1MCxEjC46d-zw\n"
        "2. @MoreMozi       UCrvchO1h6lWZAuGaa1LqX9Q — continuation\n"
        "   spans two lines\n"
        "Excluded (do not ingest): @mozimedia (empty), fan channels.\n"
        "## Stage S — Synthesis\n")

    def test_subject_targets_only(self):
        self.assertEqual(refresh_sources.parse_subject_channels(self.SUBJECT),
                         ["@thefutur", "@TheFuturAcademy"])

    def test_ingest_loop_stops_at_excluded(self):
        self.assertEqual(refresh_sources.parse_ingest_loop_channels(self.LOOP),
                         ["@AlexHormozi", "@MoreMozi"])


class StagingAndFreshness(unittest.TestCase):
    def test_staging_rows_classify_shorts_and_quote_titles(self):
        lines = ['abc123;A "quoted" title;2026-07-18;45;100',
                 "def456;Long video;NA;600;NA",
                 "bad-line-without-fields"]
        rows = refresh_sources.staging_rows(lines, "2026-07-19")
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["type"], "short")
        self.assertEqual(rows[0]["title"], "A 'quoted' title")
        self.assertEqual(rows[0]["notes"], "views=100")
        self.assertEqual(rows[1]["type"], "video")
        self.assertEqual(rows[1]["published"], "NA")
        self.assertEqual(rows[1]["status"], "L0-discovered")

    def test_is_fresh_window(self):
        today = datetime.date(2026, 7, 19)
        self.assertTrue(refresh_sources.is_fresh("2026-07-19", today, 14))
        self.assertTrue(refresh_sources.is_fresh("2026-07-05", today, 14))
        self.assertFalse(refresh_sources.is_fresh("2026-07-04", today, 14))
        self.assertFalse(refresh_sources.is_fresh("NA", today, 14))
        self.assertFalse(refresh_sources.is_fresh("", today, 14))


class JournalState(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._orig = autopilot_journal.JOURNAL
        autopilot_journal.JOURNAL = pathlib.Path(self._tmp.name) / "journal.jsonl"

    def tearDown(self):
        autopilot_journal.JOURNAL = self._orig
        self._tmp.cleanup()

    def test_no_journal_means_stale_discovery_no_run(self):
        st = autopilot_journal.derive_status()
        self.assertIsNone(st["run"])
        self.assertTrue(st["last_discovery"]["stale"])
        self.assertEqual(st["backoffs"], [])

    def test_run_over_timebox_and_cycles(self):
        old = (autopilot_journal.now() - datetime.timedelta(hours=7)).isoformat(timespec="seconds")
        recent = autopilot_journal.now().isoformat(timespec="seconds")
        autopilot_journal.JOURNAL.parent.mkdir(exist_ok=True)
        autopilot_journal.JOURNAL.write_text(
            f'{{"ts": "{old}", "event": "run-start", "timebox_h": 6}}\n'
            f'{{"ts": "{recent}", "event": "cycle", "clone": "hormozi", "stage": "B"}}\n'
            f'{{"ts": "{recent}", "event": "discovery", "new": 3}}\n',
            encoding="utf-8")
        st = autopilot_journal.derive_status()
        self.assertTrue(st["run"]["over_timebox"])
        self.assertEqual(st["cycles_this_run"], 1)
        self.assertFalse(st["last_discovery"]["stale"])

    def test_run_end_closes_run_and_backoff_expires(self):
        t = autopilot_journal.now().isoformat(timespec="seconds")
        expired = (autopilot_journal.now() - datetime.timedelta(hours=2)).isoformat(timespec="seconds")
        autopilot_journal.JOURNAL.parent.mkdir(exist_ok=True)
        autopilot_journal.JOURNAL.write_text(
            f'{{"ts": "{t}", "event": "run-start", "timebox_h": 6}}\n'
            f'{{"ts": "{t}", "event": "run-end", "reason": "timebox"}}\n'
            f'{{"ts": "{expired}", "event": "backoff", "clone": "mkbhd", "minutes": 60}}\n'
            f'{{"ts": "{t}", "event": "backoff", "clone": "hormozi", "minutes": 60}}\n'
            "corrupt line that must not crash the parser\n",
            encoding="utf-8")
        st = autopilot_journal.derive_status()
        self.assertIsNone(st["run"])
        self.assertEqual(st["last_run_end"]["reason"], "timebox")
        self.assertEqual([b["clone"] for b in st["backoffs"]], ["hormozi"])


class WorkerPartition(unittest.TestCase):
    CFG = {"workers": {"assignments": {"a": ["x", "y"], "b": ["z"]}},
           "scheduling": {"max_parallel_clones": 3}}

    def test_owned_none_without_worker(self):
        # unpartitioned default -> all clones (represented as None)
        self.assertIsNone(autopilot_journal.owned_clones(None, self.CFG))

    def test_owned_none_without_assignments(self):
        self.assertIsNone(autopilot_journal.owned_clones("a", {}))

    def test_owned_list_for_assigned_worker(self):
        self.assertEqual(autopilot_journal.owned_clones("a", self.CFG), ["x", "y"])

    def test_owned_empty_for_unassigned_named_worker(self):
        # safety: a named worker missing from a non-empty map owns NOTHING, never all
        self.assertEqual(autopilot_journal.owned_clones("ghost", self.CFG), [])

    def test_env_override_sets_worker_and_journal(self):
        old = os.environ.get("ROSTER_WORKER")
        os.environ["ROSTER_WORKER"] = "florian"
        try:
            self.assertEqual(autopilot_journal.resolve_worker(), "florian")
            self.assertEqual(autopilot_journal.journal_path().name, "journal-florian.jsonl")
        finally:
            os.environ.pop("ROSTER_WORKER", None)
            if old is not None:
                os.environ["ROSTER_WORKER"] = old

    def test_journal_path_defaults_to_global_without_worker(self):
        old = os.environ.pop("ROSTER_WORKER", None)
        try:
            self.assertIsNone(autopilot_journal.resolve_worker())
            self.assertEqual(autopilot_journal.journal_path(), autopilot_journal.JOURNAL)
        finally:
            if old is not None:
                os.environ["ROSTER_WORKER"] = old


if __name__ == "__main__":
    unittest.main()
