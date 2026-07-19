#!/usr/bin/env python3
"""Discovery refresh: pull newly published videos into every clone's ledger.

For each clone in roster.json (status active/bootstrapped/created, repo + ledger
present) this enumerates the newest N items of every TARGET channel (yt-dlp
flat-playlist, /videos + /shorts tabs), merges them into the clone's own
pipeline/ledger.csv via the clone's merge_staging.py (dedup by id — existing rows
always win, so re-running is idempotent and safe), backfills upload date + views for
the NEW rows only, and promotes recent uploads (published within --fresh-days) of
long-form videos to priority 1 with a `fresh-upload` note so the ingest loop picks
them up next.

Channel lists are resolved per clone, first match wins:
  1. pipeline/channels.json         — optional explicit override
                                      {"channels": [{"handle": "@x"}, ...]}
  2. SUBJECT.md                     — "### YouTube channels" numbered entries
                                      containing the word TARGET (newer clones)
  3. .claude/commands/ingest-loop.md — "### Target channels" numbered entries
                                      before the "Excluded" line (older clones)

Channels with ZERO ledger rows are skipped by default (initial enumeration is the
clone's Stage A); pass --full to run the full Stage-A flow for them (full
enumeration + the clone's backfill_metadata.py --top N).

This script only touches pipeline/ledger.csv (mechanical, same format as the clone
tools). It writes no wiki/log content — the roster autopilot journals refreshes on
the roster side; --commit records the ledger change in each clone repo per the
clone convention (every change ends in a pushed commit).

Usage:
  python tools/refresh_sources.py                    # all eligible clones
  python tools/refresh_sources.py --clone hormozi    # one clone
  python tools/refresh_sources.py --commit           # + git commit/push per clone
  python tools/refresh_sources.py --full             # + Stage A for empty channels
  python tools/refresh_sources.py --json             # machine-readable summary
"""
from __future__ import annotations

import argparse
import csv
import datetime
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COLS = [
    "id", "type", "title", "channel_or_publisher", "url", "published",
    "discovered", "status", "priority", "domains", "notes",
]
ELIGIBLE_STATUSES = {"active", "bootstrapped", "created"}
HANDLE_RE = re.compile(r"@[A-Za-z0-9_.-]+")
SHORT_MAX_SECONDS = 62  # mirrors fetch_channel.ps1


def load_config() -> dict:
    cfg = ROOT / "autopilot.config.json"
    d = json.loads(cfg.read_text(encoding="utf-8")) if cfg.exists() else {}
    disc = d.get("discovery", {})
    return {
        "playlist_end": disc.get("playlist_end", 30),
        "fresh_days": disc.get("fresh_days", 14),
        "top_promote": disc.get("top_promote", 50),
    }


# --------------------------------------------------------------- channel resolution
def numbered_entries(lines: list[str]) -> list[str]:
    """Group a section's numbered-list entries (continuation lines included)."""
    entries, current = [], None
    for line in lines:
        if re.match(r"^\s*\d+\.\s", line):
            if current:
                entries.append(current)
            current = line
        elif current is not None and (line.startswith((" ", "\t")) and line.strip()):
            current += " " + line.strip()
        else:
            if current:
                entries.append(current)
                current = None
    if current:
        entries.append(current)
    return entries


def section_lines(text: str, heading_re: str) -> list[str]:
    out, inside = [], False
    for line in text.splitlines():
        if re.match(heading_re, line):
            inside = True
            continue
        if inside and re.match(r"^#{2,3} ", line):
            break
        if inside:
            out.append(line)
    return out


def parse_subject_channels(text: str) -> list[str]:
    """SUBJECT.md: '### YouTube channels' numbered entries marked TARGET."""
    lines = section_lines(text, r"^### YouTube channels")
    handles = []
    for entry in numbered_entries(lines):
        if "TARGET" not in entry:
            continue
        m = HANDLE_RE.search(entry)
        if m:
            handles.append(m.group(0))
    return handles


def parse_ingest_loop_channels(text: str) -> list[str]:
    """ingest-loop.md: '### Target channels' numbered entries before 'Excluded'."""
    lines = section_lines(text, r"^### Target channels")
    kept = []
    for line in lines:
        if line.strip().lower().startswith("excluded"):
            break
        kept.append(line)
    handles = []
    for entry in numbered_entries(kept):
        m = HANDLE_RE.search(entry)
        if m:
            handles.append(m.group(0))
    return handles


def resolve_channels(repo: pathlib.Path) -> tuple[list[str], str]:
    override = repo / "pipeline" / "channels.json"
    if override.exists():
        d = json.loads(override.read_text(encoding="utf-8"))
        return [c["handle"] for c in d.get("channels", [])], "channels.json"
    subject = repo / "SUBJECT.md"
    if subject.exists():
        handles = parse_subject_channels(subject.read_text(encoding="utf-8", errors="replace"))
        if handles:
            return handles, "SUBJECT.md"
    loop = repo / ".claude" / "commands" / "ingest-loop.md"
    if loop.exists():
        handles = parse_ingest_loop_channels(loop.read_text(encoding="utf-8", errors="replace"))
        if handles:
            return handles, "ingest-loop.md"
    return [], "none"


# --------------------------------------------------------------------- yt-dlp layer
def ytdlp_flat(url: str, limit: int | None) -> list[str]:
    """Flat-playlist print lines 'id;title;date;duration;views' (newest first)."""
    cmd = ["yt-dlp", "--encoding", "utf-8", "--flat-playlist", "--no-warnings",
           "--ignore-errors",
           "--print", "%(id)s;%(title)s;%(upload_date>%Y-%m-%d|NA)s;%(duration|0)s;%(view_count|0)s"]
    if limit:
        cmd += ["--playlist-end", str(limit)]
    cmd.append(url)
    out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    lines = [ln for ln in (out.stdout or "").splitlines() if ln.strip()]
    if out.returncode != 0 and not lines:
        return []  # tab missing (e.g. no /shorts) or transient failure — caller reports
    return lines


def staging_rows(lines: list[str], today: str) -> list[dict]:
    rows = []
    for ln in lines:
        p = ln.split(";", 4)
        if len(p) < 5 or not p[0]:
            continue
        try:
            dur = int(p[3])
        except ValueError:
            dur = 0
        rows.append({
            "id": f"yt-{p[0]}",
            "type": "short" if 0 < dur <= SHORT_MAX_SECONDS else "video",
            "title": p[1].replace('"', "'"),
            "channel_or_publisher": "",  # merge_staging stamps the handle
            "url": f"https://www.youtube.com/watch?v={p[0]}",
            "published": p[2],
            "discovered": today,
            "status": "L0-discovered",
            "priority": "3",
            "domains": "",
            "notes": f"views={p[4]}" if p[4].isdigit() else "",
        })
    return rows


def fetch_meta(urls: list[str]) -> dict[str, tuple[str, str]]:
    """id -> (published YYYY-MM-DD|'', views|'') via per-video extraction."""
    if not urls:
        return {}
    cmd = ["yt-dlp", "--skip-download", "--no-warnings", "--ignore-errors", "--no-update",
           "--print", "%(id)s\t%(upload_date)s\t%(view_count)s", *urls]
    out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    meta = {}
    for line in (out.stdout or "").splitlines():
        parts = line.split("\t")
        if len(parts) == 3:
            vid, date, views = parts
            pub = f"{date[0:4]}-{date[4:6]}-{date[6:8]}" if re.fullmatch(r"\d{8}", date) else ""
            meta[vid] = (pub, views if views.isdigit() else "")
    return meta


# --------------------------------------------------------------------- ledger layer
def read_ledger(path: pathlib.Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_ledger(path: pathlib.Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in COLS})


def is_fresh(published: str, today: datetime.date, fresh_days: int) -> bool:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", published or ""):
        return False
    d = datetime.date.fromisoformat(published)
    return (today - d).days <= fresh_days


def write_staging(path: pathlib.Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow(r)


# ------------------------------------------------------------------- per-clone flow
def refresh_clone(c: dict, cfg: dict, full: bool, commit: bool) -> dict:
    repo = (ROOT / c["repo"]).resolve()
    result = {"slug": c["slug"], "eligible": True, "channels": [], "new_video": 0,
              "new_short": 0, "fresh_promoted": 0, "skipped_reason": None, "errors": []}

    ledger_path = repo / "pipeline" / "ledger.csv"
    if not repo.exists() or not ledger_path.exists():
        result.update(eligible=False, skipped_reason="repo or ledger missing")
        return result
    handles, source = resolve_channels(repo)
    if not handles:
        result.update(eligible=False,
                      skipped_reason="no channel list found (bootstrap /clone-setup pending)")
        return result
    result["channel_source"] = source

    today = datetime.date.today()
    today_s = today.isoformat()
    before_ids = {r["id"] for r in read_ledger(ledger_path)}
    norm = lambda h: h.lstrip("@").lower()
    per_channel_rows = {norm(r.get("channel_or_publisher", "")) for r in read_ledger(ledger_path)}

    for handle in handles:
        ch = {"handle": handle, "mode": None, "new": 0, "note": None}
        result["channels"].append(ch)
        has_rows = norm(handle) in per_channel_rows
        if not has_rows and not full:
            ch.update(mode="skipped", note="0 ledger rows — initial enumeration is Stage A (use --full)")
            continue
        limit = None if not has_rows else cfg["playlist_end"]
        ch["mode"] = "full" if limit is None else f"newest-{limit}"

        vids = ytdlp_flat(f"https://www.youtube.com/{handle}/videos", limit)
        shorts = ytdlp_flat(f"https://www.youtube.com/{handle}/shorts", limit)
        if not vids and not shorts:
            ch["note"] = "yt-dlp returned nothing (tab missing, throttled, or offline)"
            result["errors"].append(f"{handle}: enumeration empty")
            continue

        slug = norm(handle)
        v_path = repo / "pipeline" / f"staging-refresh-{slug}-videos.csv"
        s_path = repo / "pipeline" / f"staging-refresh-{slug}-shorts.csv"
        write_staging(v_path, staging_rows(vids, today_s))
        write_staging(s_path, staging_rows(shorts, today_s))
        merge = subprocess.run(
            [sys.executable, str(repo / "tools" / "merge_staging.py"),
             "--channel", handle, "--videos", str(v_path), "--shorts", str(s_path)],
            capture_output=True, text=True, encoding="utf-8", errors="replace")
        v_path.unlink(missing_ok=True)
        s_path.unlink(missing_ok=True)
        if merge.returncode != 0:
            ch["note"] = "merge_staging failed"
            result["errors"].append(f"{handle}: merge_staging: {merge.stderr.strip()[:200]}")
            continue

        if limit is None:  # Stage-A flow for a previously empty channel
            bf = subprocess.run(
                [sys.executable, str(repo / "tools" / "backfill_metadata.py"),
                 "--channel", handle, "--top", str(cfg["top_promote"])],
                capture_output=True, text=True, encoding="utf-8", errors="replace")
            if bf.returncode != 0:
                result["errors"].append(f"{handle}: backfill_metadata: {bf.stderr.strip()[:200]}")

    # New rows across all channels: fill metadata, promote fresh long-form uploads.
    rows = read_ledger(ledger_path)
    new_rows = [r for r in rows if r["id"] not in before_ids]
    need_meta = [r for r in new_rows if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r.get("published") or "")]
    meta = {}
    for i in range(0, len(need_meta), 40):
        meta.update(fetch_meta([r["url"] for r in need_meta[i:i + 40]]))
    changed = bool(new_rows)
    for r in new_rows:
        vid = r["id"].removeprefix("yt-")
        if vid in meta:
            pub, views = meta[vid]
            if pub:
                r["published"] = pub
            if views:
                r["notes"] = f"views={views}"
        if r["type"] == "video":
            result["new_video"] += 1
            if is_fresh(r.get("published", ""), today, cfg["fresh_days"]):
                r["priority"] = "1"
                r["notes"] = (r.get("notes", "") + " fresh-upload").strip()
                result["fresh_promoted"] += 1
        else:
            result["new_short"] += 1
    if changed:
        write_ledger(ledger_path, rows)

    if commit and changed:
        msg = (f"ledger: discovery refresh (+{result['new_video']} video, "
               f"+{result['new_short']} short; {result['fresh_promoted']} fresh-upload P1) "
               "via roster autopilot")
        subprocess.run(["git", "-C", str(repo), "add", "pipeline/ledger.csv"],
                       capture_output=True, text=True)
        cm = subprocess.run(["git", "-C", str(repo), "commit", "-m", msg],
                            capture_output=True, text=True)
        if cm.returncode == 0:
            push = subprocess.run(["git", "-C", str(repo), "push"],
                                  capture_output=True, text=True)
            if push.returncode != 0:
                result["errors"].append("git push failed (commit is local)")
        else:
            result["errors"].append(f"git commit failed: {cm.stderr.strip()[:200]}")
    return result


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--clone", help="only this roster slug")
    ap.add_argument("--full", action="store_true",
                    help="also enumerate channels with zero ledger rows (Stage-A flow)")
    ap.add_argument("--commit", action="store_true",
                    help="git commit+push the ledger change in each clone repo")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    cfg = load_config()
    roster = json.loads((ROOT / "roster.json").read_text(encoding="utf-8"))
    clones = [c for c in roster.get("clones", [])
              if c.get("status") in ELIGIBLE_STATUSES
              and (not a.clone or c["slug"] == a.clone)]
    if a.clone and not clones:
        print(f"unknown or ineligible clone {a.clone!r}", file=sys.stderr)
        return 2

    results = [refresh_clone(c, cfg, a.full, a.commit) for c in clones]

    if a.json:
        print(json.dumps({"date": datetime.date.today().isoformat(),
                          "results": results}, indent=2))
    else:
        for r in results:
            if not r["eligible"]:
                print(f"{r['slug']:<14} skipped: {r['skipped_reason']}")
                continue
            print(f"{r['slug']:<14} +{r['new_video']} video, +{r['new_short']} short, "
                  f"{r['fresh_promoted']} fresh-upload -> P1  "
                  f"[{r.get('channel_source')}: {len(r['channels'])} channel(s)]")
            for ch in r["channels"]:
                note = f" — {ch['note']}" if ch.get("note") else ""
                print(f"    {ch['handle']:<20} {ch['mode']}{note}")
            for e in r["errors"]:
                print(f"    !! {e}")
    return 1 if any(r["errors"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
