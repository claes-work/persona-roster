"""Persona registry + environment loading for the standalone harness.

Resolves a persona slug (e.g. "hormozi") to its clone repo + system-prompt on
disk, reading the canonical `roster.json`. Dependency-light on purpose: no
SDKs, no dotenv package — just the stdlib so this package can be copied into any
project (2Key, a website backend, ...) and driven over an API key alone.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path

# harness/ lives at the roster repo root, so the roster root is our parent.
ROSTER_ROOT = Path(__file__).resolve().parent.parent
ROSTER_JSON = ROSTER_ROOT / "roster.json"


@dataclass(frozen=True)
class Persona:
    slug: str
    name: str
    repo: Path            # absolute, resolved clone repo root
    system_prompt: Path   # absolute path to persona/system-prompt.md
    domains: list[str]
    status: str

    def read_system_prompt(self) -> str:
        return self.system_prompt.read_text(encoding="utf-8")


def _load_env_file(path: Path) -> None:
    """Minimal .env loader (KEY=VALUE lines). Never overrides an existing env var."""
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def load_env() -> None:
    """Load harness/.env then roster-root/.env (first wins; env always wins)."""
    _load_env_file(Path(__file__).resolve().parent / ".env")
    _load_env_file(ROSTER_ROOT / ".env")


def _resolve_repo(rel_or_abs: str) -> Path:
    """roster.json stores clone repos as `clones/<name>` (a symlink on this
    machine). Resolve relative to the roster root and follow symlinks."""
    p = Path(rel_or_abs)
    if not p.is_absolute():
        p = ROSTER_ROOT / p
    return p.resolve()


def load_roster() -> dict[str, Persona]:
    data = json.loads(ROSTER_JSON.read_text(encoding="utf-8"))
    out: dict[str, Persona] = {}
    for c in data.get("clones", []):
        slug = c["slug"]
        repo = _resolve_repo(c["repo"])
        sysprompt = repo / c.get("system_prompt", "persona/system-prompt.md")
        out[slug] = Persona(
            slug=slug,
            name=c.get("name", slug),
            repo=repo,
            system_prompt=sysprompt,
            domains=c.get("domains", []),
            status=c.get("status", "unknown"),
        )
    return out


def get_persona(slug: str) -> Persona:
    roster = load_roster()
    if slug not in roster:
        raise KeyError(
            f"Unknown persona {slug!r}. Known: {', '.join(sorted(roster))}"
        )
    p = roster[slug]
    if not p.system_prompt.exists():
        raise FileNotFoundError(
            f"Persona {slug!r} has no compiled system-prompt at {p.system_prompt} "
            f"(status={p.status}). Only 'active' clones are queryable."
        )
    return p
