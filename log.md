# Log

Append-only chronological record. Entry format:
`## [YYYY-MM-DD] <type> | <title>` with `<type>` ∈ `council | work | plan | review | wiki | setup`,
followed by 1–3 lines. Recent history: `grep "^## \[" log.md | tail -5`.

## [2026-07-18] setup | Agent-OS upgrade: teams, router, pipelines, mandatory wiki persistence
Analyzed roster/template/hormozi-clone/second-brain; built the orchestration layer per the
2026-07-18 master brief: teams.json (+5 role prompts), tools/route.py + validate.py (+19 tests),
/work /plan /run-plan /review /wiki beside extended /council, roster wiki scaffold
(STATE/index/log/decisions/learnings/plans), AGENTS.md/CLAUDE.md, docs. Decision:
[[wiki/decisions/2026-07-18-agent-os-architecture]]. Knowledge: decision + this entry.
Next: ingest Chris Do → first multi-voice council.

## [2026-07-18] setup | Global install: agent OS usable from any project
Added tools/install_global.py: generates machine-local shims into ~/.claude (all six
commands + 12 persona agents; marker-guarded, --uninstall supported). gen_agents.py
refactored to expose generate(out_dir). Cross-project rule: artifacts to the target
project per its conventions, decisions/orchestration learnings to the roster wiki.
Knowledge: this entry + guide/README updates. Next: use /work from youtube-engine for real.

## [2026-07-18] setup | Onboarding skills, maturity policy, Chris Do promoted to active
Added /setup (idempotent machine onboarding) + /add-clone (persona onboarding strategy),
tools/roster_status.py (clone readiness + mismatch detection), experimental seats in
route.py (non-active clones joinable ONLY via explicit --include, flagged low-confidence;
policy: [[wiki/decisions/2026-07-18-clone-maturity-policy]]). roster_status immediately
found Chris Do compiled (v7, 378 L2) -> status active; agents regenerated + reinstalled.
Councils now have TWO voices (Hormozi v35, Chris Do v7). Tests 22/22. Next: ingest Neil Patel/MKBHD.

## [2026-07-18] setup | Multi-owner clone hosting + install prerequisites documented
clone_all.py now honors a per-clone "github" field (owner/name or URL) so collaborators
can host new personas under their own accounts; /add-clone documents the ownership rule,
the registry-as-distribution mechanism, and a template-flag-free fallback for repo
creation. Guide gained a prerequisites/access-rights matrix. Found: GitHub template repo
lacks the --template flag (gh repo edit claes-work/persona-clone-template --template
would enable the preferred creation path). Knowledge: this entry.

## [2026-07-18] setup | README rewritten for non-technical onboarding; template flag set
README now leads with plain-language what/why, 3-step get-started (/setup), everyday-use
table, bench table with build status, /add-clone story, collaborator rights matrix;
manual steps folded into a details block. GitHub: persona-clone-template marked as
template repo -> gh repo create --template path in /add-clone now works. Knowledge: this entry.
