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

## [2026-07-18] work | Cross-project: video plan for the roster created in youtube-engine
First real cross-project use of the OS conventions: planned-video folder
../youtube-engine/videos/geplant/2026-07-18-persona-klone-council/ (status/inventory/
drehplan-v0/title-hypotheses/checklist) following youtube-engine's own templates.
Artifact knowledge lives THERE (incl. docs/log.md entry); roster note: STATE next actions
now include producing the video once >=4 clones are active. Knowledge: this entry.

## [2026-07-18] work | Cross-project: 5 Titelvarianten Infrastruktur-Video (youtube-engine)

Erster echter /work-Lauf end-to-end: standard-Pipeline, Team youtube, Seats Hormozi +
Chris Do (--include), Review skeptical + evidence. Artefakt im Zielprojekt:
`youtube-engine/videos/wip/2026-07-11-infrastruktur-hinter-ki-automatisierung/titel-hypothesen.md`
(+ Hypothesen-Zeilen in dessen `docs/concepts/titel-formeln.md`, Log-Eintrag dort).
Orchestrierungs-Learning: `wiki/learnings/work-pipeline-standard.md` (Seats konvergierten;
Funktions-Reviewer lieferten die Hälfte der Must-fixes). Knowledge: learning + Log beidseitig.

## [2026-07-18] work | Persona-grounded packaging skills built in youtube-engine
Live advisor consultations (hormozi v35, chris-do v7) produced a cited packaging
"constitution" (youtube-engine docs/concepts/packaging-prinzipien.md); 8 skills + a
thumbnail-gen script now use it, with live routing via this roster's route.py so future
active clones auto-join (no hardcoded persona names in any skill). Pattern worth
keeping: cache persona doctrine in the target project, consult live only where it pays
(titles). Both clones honestly flagged knowledge gaps - deflect rule held in practice.
Next: after first /packaging run on a real video, retro the constitution against results.

## [2026-07-18] work | Cross-project: Thumbnail-Konzepte Infrastruktur-Video + V3-Titel-Widerlegung (youtube-engine)

Zweiter /work-Lauf (standard, youtube-Team, Hormozi + Chris Do, beide Reviewer):
3 Thumbnail-Konzepte in `youtube-engine/.../thumbnail-prompts.md` (Council-Dissens
Beweis-Zahl vs. Neugier wurde zur A/B-Test-Dimension). Evidence Reviewer widerlegte per
Drehbericht + Video-Frames den beschlossenen Titel V3 (Take 7 fehlt im Material) —
Orchestrator-Briefing-Fehler: Titel-Review lief nur gegen Plan-Dokumente. Learning-Seite
`wiki/learnings/work-pipeline-standard.md` aktualisiert (effective_rule: Reviewer auf
IST-Artefakte briefen). Knowledge: learning aktualisiert + Logs beidseitig.

## [2026-07-19] plan | Roster ingest autopilot planned (freshness, scheduling, loop, budget)
User requirement (voice note): keep all personas current automatically — new-video
discovery, an explicit cross-clone ingest plan instead of gut feeling, one roster-level
loop ("nudge once daily"), later cron/server, budget-aware (~80% of weekly usage).
Current-state analysis of clone machinery done (ledger stages, Stage-A-only discovery
gap, roster_status lacks freshness metrics). Plan object created:
`plans/2026-07-19-roster-ingest-autopilot.md` (WP1 status metrics → WP2 discovery
refresh → WP3 scheduling policy → WP4 /roster-loop → WP5 budget guard → WP6 cron).
Knowledge: plan + STATE update; open question logged on programmatic usage measurement.

## [2026-07-19] work | Roster ingest autopilot built (WP1-WP5) + first live discovery refresh
Plan `2026-07-19-roster-ingest-autopilot` executed in one pass: roster_status.py now
reports backlog/freshness/synthesis-debt/maturity-target per clone (+ regex fix: chris-do
synthesis passes were invisible); tools/refresh_sources.py + /refresh-sources pull new
videos into clone ledgers (idempotent, fresh uploads -> P1 "fresh-upload"); scheduling
policy accepted as decision `2026-07-19-ingest-scheduling-policy` (freshness first,
focus-until-active, time-boxed budget); /roster-loop dispatcher + autopilot.config.json +
autopilot/journal.jsonl + tools/autopilot_journal.py; 15 new tests (32 green).
Live verification: hormozi +32 video/+61 short (same-day upload "Why AI won't make you
rich in 2026" -> P1), neil-patel +4/+12, mkbhd +2, re-run +0; clone commits pushed.
Knowledge: decision + learning page + plan progress + STATE updated. Open: WP6 cron.
