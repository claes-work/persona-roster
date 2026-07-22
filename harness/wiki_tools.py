"""Read-only, path-jailed wiki tools handed to the small model.

These mirror the exact three tools the Claude Code advisor agent gets
(Read / Grep / Glob) plus a list_dir convenience, but implemented in pure
Python so the harness carries no dependency beyond the stdlib. Every path is
resolved and asserted to live *inside* the persona's clone repo — the model
can never read another persona's brain or anything else on disk.
"""
from __future__ import annotations

import fnmatch
import re
import shutil
import subprocess
from pathlib import Path

# Output caps keep tool results (and therefore token cost) bounded.
READ_MAX_CHARS = 12_000
GREP_MAX_MATCHES = 60
GLOB_MAX_RESULTS = 200
LIST_MAX_ENTRIES = 200


class WikiTools:
    """Filesystem tools scoped to a single clone repo root."""

    def __init__(self, repo_root: Path):
        self.root = repo_root.resolve()

    # --- path safety -----------------------------------------------------
    def _resolve(self, rel: str) -> Path:
        rel = (rel or "").strip().lstrip("/\\")
        target = (self.root / rel).resolve()
        if target != self.root and self.root not in target.parents:
            raise ValueError(f"path escapes repo sandbox: {rel!r}")
        return target

    def _rel(self, p: Path) -> str:
        return p.relative_to(self.root).as_posix()

    # --- tools -----------------------------------------------------------
    def read_file(self, path: str, start_line: int | None = None,
                  end_line: int | None = None) -> str:
        p = self._resolve(path)
        if not p.is_file():
            return f"ERROR: not a file: {path}"
        text = p.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        if start_line or end_line:
            s = max(1, start_line or 1)
            e = min(len(lines), end_line or len(lines))
            body = "\n".join(f"{i}\t{lines[i-1]}" for i in range(s, e + 1))
        else:
            body = text
        if len(body) > READ_MAX_CHARS:
            body = body[:READ_MAX_CHARS] + f"\n... [truncated at {READ_MAX_CHARS} chars — narrow with start_line/end_line]"
        return body

    def list_dir(self, path: str = "") -> str:
        p = self._resolve(path)
        if not p.is_dir():
            return f"ERROR: not a directory: {path}"
        entries = []
        for child in sorted(p.iterdir()):
            if child.name.startswith("."):
                continue
            entries.append(self._rel(child) + ("/" if child.is_dir() else ""))
            if len(entries) >= LIST_MAX_ENTRIES:
                entries.append(f"... [more than {LIST_MAX_ENTRIES} entries]")
                break
        return "\n".join(entries) or "(empty)"

    def glob(self, pattern: str) -> str:
        matches = [self._rel(p) for p in self.root.rglob("*")
                   if p.is_file() and fnmatch.fnmatch(self._rel(p), pattern)]
        matches.sort()
        head = matches[:GLOB_MAX_RESULTS]
        out = "\n".join(head)
        if len(matches) > GLOB_MAX_RESULTS:
            out += f"\n... [{len(matches) - GLOB_MAX_RESULTS} more; refine the pattern]"
        return out or f"(no files match {pattern!r})"

    def grep(self, pattern: str, path_glob: str = "**/*.md",
             max_results: int = GREP_MAX_MATCHES) -> str:
        max_results = min(int(max_results or GREP_MAX_MATCHES), GREP_MAX_MATCHES)
        rg = shutil.which("rg")
        if rg:
            return self._grep_rg(rg, pattern, path_glob, max_results)
        return self._grep_py(pattern, path_glob, max_results)

    def _grep_rg(self, rg: str, pattern: str, path_glob: str, max_results: int) -> str:
        try:
            proc = subprocess.run(
                [rg, "--line-number", "--no-heading", "--color=never",
                 "-g", path_glob, "-e", pattern, "."],
                cwd=self.root, capture_output=True, text=True, timeout=20,
            )
        except (subprocess.TimeoutExpired, OSError):
            return self._grep_py(pattern, path_glob, max_results)
        lines = [l for l in proc.stdout.splitlines() if l.strip()]
        if not lines:
            return f"(no matches for {pattern!r})"
        head = lines[:max_results]
        out = "\n".join(head)
        if len(lines) > max_results:
            out += f"\n... [{len(lines) - max_results} more matches; refine the pattern]"
        return out

    def _grep_py(self, pattern: str, path_glob: str, max_results: int) -> str:
        try:
            rx = re.compile(pattern, re.IGNORECASE)
        except re.error as e:
            return f"ERROR: bad regex: {e}"
        results: list[str] = []
        for f in self.root.rglob("*"):
            if not f.is_file() or not fnmatch.fnmatch(self._rel(f), path_glob):
                continue
            try:
                for n, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                    if rx.search(line):
                        results.append(f"{self._rel(f)}:{n}:{line.strip()[:200]}")
                        if len(results) >= max_results + 1:
                            break
            except OSError:
                continue
            if len(results) >= max_results + 1:
                break
        if not results:
            return f"(no matches for {pattern!r})"
        out = "\n".join(results[:max_results])
        if len(results) > max_results:
            out += f"\n... [more matches; refine the pattern]"
        return out


# ---------------------------------------------------------------------------
# Tool schema (provider-neutral). Adapters translate this into each API's
# function-declaration format.
# ---------------------------------------------------------------------------
TOOL_SCHEMAS = [
    {
        "name": "grep",
        "description": "Search the persona's wiki for a regex pattern. Returns file:line:text matches. Start here to locate grounding for a claim.",
        "parameters": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "description": "Regex, case-insensitive."},
                "path_glob": {"type": "string", "description": "Glob to restrict files, e.g. 'wiki/**/*.md'. Default '**/*.md'."},
            },
            "required": ["pattern"],
        },
    },
    {
        "name": "read_file",
        "description": "Read a file from the wiki (optionally a line range). Use after grep/glob to pull the actual passage to cite.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Repo-relative path, e.g. 'wiki/topics/business/money-model.md'."},
                "start_line": {"type": "integer"},
                "end_line": {"type": "integer"},
            },
            "required": ["path"],
        },
    },
    {
        "name": "glob",
        "description": "List wiki files matching a glob pattern, e.g. 'wiki/sources/2025-*.md'.",
        "parameters": {
            "type": "object",
            "properties": {"pattern": {"type": "string"}},
            "required": ["pattern"],
        },
    },
    {
        "name": "list_dir",
        "description": "List entries of a directory in the wiki. Empty path lists the repo root.",
        "parameters": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": [],
        },
    },
]


def dispatch(tools: WikiTools, name: str, args: dict) -> str:
    args = args or {}
    try:
        if name == "grep":
            return tools.grep(args.get("pattern", ""), args.get("path_glob", "**/*.md"))
        if name == "read_file":
            return tools.read_file(args.get("path", ""), args.get("start_line"), args.get("end_line"))
        if name == "glob":
            return tools.glob(args.get("pattern", "*"))
        if name == "list_dir":
            return tools.list_dir(args.get("path", ""))
        return f"ERROR: unknown tool {name!r}"
    except Exception as e:  # never let a tool crash the loop
        return f"ERROR: {type(e).__name__}: {e}"
