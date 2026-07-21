# Log

Append-only chronological record. Entry format:
`## [YYYY-MM-DD] <type> | <title>` with `<type>` ∈ `council | work | plan | review | wiki | setup`,
followed by 1–3 lines. Recent history: `grep "^## \[" log.md | tail -5`.

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
Fresh run start immediately hit drained: all 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) are in active back-off (mkbhd/neil-patel until 11:45, hormozi/chris-do until
11:52), leftover from the prior run's cadence. Discovery fresh (age 0.35h), no refresh
needed. No executors dispatched this iteration. Next: retry after ~11:52 when back-offs
clear.

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

## [2026-07-19] work | Autopilot run 1 (supervised): 3 cycles, 22 videos L2, user-ended at 0.48h
First supervised /loop /roster-loop run (timebox 2h, ended early by user). 3 cycles, all
hormozi Stage B freshness work: batches 276-278 -> 22 videos L2 (incl. same-day flagship
"Why AI won't make you rich in 2026" as L3-candidate), 1 dup, 1 unavailable; 8 fresh P1
remain on @MoreMozi; synthesis debt 4/10. Zero rate limits, zero errors; dispatcher
premise correction worked (cycle 2: subagent verified checkpoint already drained, ran B
not S). ~10 min/cycle, ~98k subagent tokens/cycle. Journal: autopilot/journal.jsonl.
Knowledge: first calibration data point pending user's observed-usage report.

## [2026-07-19] work | Parallel ingest + per-machine worker partition (roster-loop)
Made `/roster-loop` faster (single machine) and shareable (two accounts) with NO change
to how it's started. (1) Bounded fan-out: dispatcher works up to
`scheduling.max_parallel_clones` (default 2) *distinct* clones per iteration, one subagent
each in parallel. (2) Per-machine worker partition: `workers.assignments` maps worker→
clones; a machine sets identity once (`autopilot_journal.py set-worker <name>`), then only
works its clones and journals to a local gitignored `journal-<worker>.jsonl`; no identity =
all clones (unchanged). Enabling insight (verified): the clone is an independent git repo =
atomic unit of isolation; two units on the SAME clone is the one forbidden case (no
row-lock in the ledger). GaryVee already removed from `focus_order` earlier this session.
Files: autopilot.config.json, .gitignore, tools/autopilot_journal.py (+whoami/set-worker),
.claude/commands/roster-loop.md; +6 tests (38 green); validate clean.
Decision: `2026-07-19-parallel-ingest-and-workers` (amends `2026-07-19-ingest-scheduling-policy`).
Knowledge: decision recorded + old policy amended. Open: Florian one-time onboarding
(clone repos + collaborator write access); calibration of max_parallel_clones vs usage.

## [2026-07-19] wiki | Index-coverage check in validate.py (drift guard)
Extended `tools/validate.py --wiki`: new `check_index_coverage()` warns for any page in
wiki/decisions, wiki/learnings, or plans/ that is referenced neither in index.md nor in
its directory's README.md (sub-index pattern). Replaces the narrower decisions-only
check. Rationale: the curated index IS our retrieval layer ("read before work, targeted
via index") — an unreferenced page is invisible to navigation; this guards index
freshness instead of building a separate software index (assessed same session: file +
content index already exist natively via index.md/topics/wiki.config.json; a generated
retrieval index would add staleness/silent-miss risk for ~no speed gain — bottleneck is
synthesis, not search). Verified: clean run on current wiki; negative test (unreferenced
learning) triggers the warning. Warning-level, non-blocking.

## [2026-07-19] work | Autopilot run 2 (session /loop): 29 cycles, 207 videos L2, neil-patel built to persona v2
Time-boxed roster-ingest autopilot, 6h box, batch 8, ended cleanly on timebox
(11:49→17:53, elapsed 6.06h). **29 cycles**: hormozi ×1 (Stage B), neil-patel ×28
(26 Stage B ingest + 2 Stage S synthesis). Zero rate-limit hits across the whole run;
one background subagent stalled mid-bookkeeping (cycle 19) and was recovered by resuming
the same agent to finish its own ledger/index/log/commit — no work lost, no duplicate
ingest.

Freshness-first fired once (hormozi @MoreMozi fresh-upload P1 tail, 8→0), then
focus-until-active drove neil-patel from a bootstrapped-but-unstarted clone (0 L2) to a
grounded persona: **0 → 207 L2 sources**, both long-form P1 eras drained (@neilpatel +
@MarketingSchoolPod, attribution-gated for co-host Eric Siu — disguised
guest-interview / Perpetual-Traffic-crossover / multi-presenter episodes detected and
quarantined), **2 synthesis passes** (8 topic hubs + persona beliefs/voice/biography),
and **system-prompt compiled v1→v2** from all 135 P1-era sources (`/neilpatel` now
loadable). neil-patel then continued into its P2 backlog (1,823 → 1,751 open).

Follow-ups for a human: (1) consider flipping neil-patel roster status `created → active`
now that a v2 persona exists; (2) calibration — report observed usage via
`autopilot_journal.py append usage observed_pct=<n>`; (3) process note captured for the
autopilot learnings: the dispatcher must verify commit state (git log + ledger) rather
than trust a subagent's completion summary, since async subagents can stall mid-unit.

## [2026-07-20] work | Autopilot run 3 (session /loop, 15h box, parallel x2): 86 cycles, ~600 videos L2, hit weekly limit
Time-boxed roster-ingest autopilot, 15h box, batch 8, **parallel x2** (bounded-parallelism
policy: up to max_parallel_clones=2 distinct clones per iteration). Started 2026-07-19
18:20; **hit the weekly API subscription limit ~03:54 (resets 06:00)**, both in-flight
cycle-46 subagents terminated mid-work; resumed after the 06:00 reset to recover the one
uncommitted unit (mkbhd), then graceful-stopped at the 15h box. **86 cycles** (neil-patel
45, mkbhd 41): 79 Stage B ingest + 7 Stage S synthesis. 1 backoff (mkbhd 429s early),
1 recorded weekly-limit event.

Output: **neil-patel 207 → 533 L2** (+326; 2017-2019 P2 tactical era + both P1 eras from
run 2), **6 synthesis passes, system-prompt v3 → v6**; **mkbhd 0 → 274 L2** (built from
scratch: @Waveform + @mkbhd 2009-2025 P1 complete, @AutoFocus EV, into 2009 origin P2),
**3 synthesis passes, system-prompt v0 → v3 (/mkbhd now loadable)**; plus 1 hormozi
fresh-upload batch at the start. Attribution gating held throughout (Eric Siu / Waveform
co-hosts / interview guests Musk/Gates/Zuckerberg/Obama/Cook/Pichai/Neistat / AutoFocus
co-host Miles all quarantined out of persona). A subagent surfaced and a later one fixed
a real clone-side driver bug (FLAG_RE matched "429" inside view counts, silently hiding
the Humane AI Pin review) — the autopilot self-repaired.

Both clones ended at synthesis-DUE (debt 10/10) — the 7th (neil-patel) and 4th (mkbhd)
passes are pending and will run first on the next /roster-loop (idempotent, nothing lost).

**Calibration (headline result):** from an 84%-consumed weekly limit at start (plus other
concurrent sessions), the remaining ~16% weekly budget sustained **~9.5h of parallel-x2
ingest** before the wall. Not a clean single-run figure (concurrent sessions confound it);
the per-session $ meter remains the cleaner signal. Evidence in
wiki/learnings/roster-ingest-autopilot.md.

**Process learnings confirmed:** (1) async single subagents reliably stall mid-bookkeeping;
the "write pages yourself sequentially, no background sub-agents" brief eliminated it.
(2) The dispatcher must verify commit state (git log + tree) rather than trust a completion
summary — caught 3 stalls + 2 limit-interruptions this session. (3) Weekly-limit mid-run
needs no special handling: idempotent resume after reset recovered cleanly.

## [2026-07-20] council | Skool premium community: exit, not revival (sunset vs. structured transfer)

Executive Council, deep depth, seats Hormozi × Chris Do (full adversarial round; both
amended, neither switched). Convergent core: end the half-alive state now; never another
rev-share operator; annual members made 100% whole; Masterclass carved out, kept, and
productized via YouTube; hard 60-day window for a real ownership transfer to a successor,
else 90-day honorable sunset. Open fork (dissent preserved): Hormozi = seller-financed
10–20% fixed-term earn-out + staged face transfer + reversion; Chris Do = clean asset/
license sale for cash or fixed note, no performance royalty, no face transfer. Record:
wiki/decisions/2026-07-20-skool-premium-community-exit.md. Second-brain context (Marco
Hanczuch precedent, 2026-07-06 focus decision) was decisive as own evidence in both
briefs. Knowledge: decision record; hub-candidate (business decision for Sebastian's
GmbH — hub should pull on next sync). Orchestration learning: cross-exam produced real
convergence (both seats adopted pieces of the other's plan) — debate mode worked without
a judge variant at 2 seats.

## [2026-07-20] work | Pitchdeck für die Community-Übergabe (Artefakt zum Council 2026-07-20)

Visuelles HTML-Pitchdeck (10 Slides, Brand-CI: Indigo #3B2EF0, Instrument Sans) für das
Übernahme-Gespräch mit Alexander, abgeleitet aus
wiki/decisions/2026-07-20-skool-premium-community-exit.md — beide Deal-Wege (Earn-out /
Clean Buy) als Verhandlungsbasis, rote Linien (Jahreszahler, Masterclass-IP), 60-Tage-
Fahrplan, 90-Tage-Gesichts-Transfer. Artefakt:
https://claude.ai/code/artifact/da96dcac-2f6e-48c2-ae52-351a7586339c (Quelle im
Session-Scratchpad; Zahlen vor Versand prüfen: Jahreszahler-Bestand fehlt noch).
Knowledge: none (Artefakt-Pointer only).

## [2026-07-20] work | 2Key-Investor-Pitch-Deck (Enno Miedl/Bleispitz) — executive council + dual review

/work standard (--include chris-do, target: 2key-workforce). Seats Hormozi + Chris Do (konvergent:
Confirmation-Deck, Mitarbeiter-Frame, Accusation-Audit-Namensfolie, Proof-vor-Promise, MESO).
Artefakte im Zielprojekt: pitch/investor-deck-bleispitz.html (14 Folien, offline-faehig, 2Key-Brand)
+ pitch/gespraechsleitfaden.md (Anker/harte Linien/BATNA). Review: Evidence "mixed" (7 Must-fixes,
alle eingearbeitet), Skeptical "ship-with-changes" (Vehikel/IP-Luecke, Anker-neben-Untergrenze ->
Option C auf 8 %; alle Top-Risiken mitigiert). Decision: wiki/decisions/2026-07-20-2key-investor-pitch-deck.md.
Knowledge: Orchestrierungs-Learning im Decision-Record (Doppel-Review fand disjunkte materielle Fehler).
Artefakt-Wissen im Zielprojekt (wiki/investment-und-exit.md + dessen log). hub-candidate: Exit-/Deal-Kontext
liegt bereits im Hub (gespraech-florian-2key-investment).

## [2026-07-20] council | 2Key-Deal-Struktur: Ein Lead-Szenario statt MESO-Menue

Runde 2 zum Investor-Pitch (Frage Sebastian: welche Option ist die beste + wie bewertet man
guten Gewissens?). Seats Hormozi + Chris Do verwarfen unabhaengig ihre eigenen
Standard-Doktrinen fuer diesen Kaeufertyp: Lead = Direktbeteiligung 150k/10% (Preis fix,
Ticket flexibel), Fallback verdeckt = Wandeldarlehen 1,5M Cap/20%, Option B gestrichen
(Dienstvertrag statt Cap-Rabatt fuer Ennos Frau). Paralleler Recherche-Agent lieferte
Bewertungsmethodik + DE-Marktzahlen (Pre-Seed-Median 3,7M) -> 1,35M pre = unterer Rand des
vertretbaren Korridors. Decision: wiki/decisions/2026-07-20-2key-deal-struktur.md (proposed,
wartet auf Gruender-Bestaetigung). Artefakt: 2key-workforce/pitch/deal-szenario.md.
Knowledge: Seats-verwerfen-eigene-Doktrin als Konvergenz-Signal (im Decision-Record).

## [2026-07-20] council | 2Key-Werbebudget: 25k ist Test-Budget, nicht Wachstums-Budget (einstimmig, 3 Fixes)

Growth Council (Hormozi + Chris Do via positioning-Tag; Reserve: neil-patel, garyvee — Paid-Ads-
Benchmark-Luecke explizit ausgewiesen). Fan-out + Cross-Examine. Einstimmig: 25k = Lern-Budget
(Rule of 100, ~68 EUR/Tag), Skalierung = CFA-Loop statt Budgetzeile. Hormozi fand Gate-Widerspruch
(3:1 erlaubt 56 EUR CAC vs. 30d-Payback erlaubt 13,50) -> Fix Jahres-Vorauszahlung; Chris Do
korrigierte die Verpackung (Founding-Member/Value-Add statt Discount) und setzte durch: Loaded-CAC
(222 vs. 170) ins Deck drucken, Marketer-Scorecard zweistufig (Monate 1-6 Audience-Conversion,
nicht CAC-only). Dissens bewahrt (karmic-equity-Gewichtung; financing- vs. self-funding-Framing =
Payback-abhaengig). Decision: wiki/decisions/2026-07-20-2key-werbebudget-25k.md. Artefakt-Folgen
im Zielprojekt notiert (deal-szenario.md), Deck-Umsetzung folgt mit naechster Deck-Iteration.

## [2026-07-20] council | 2Key-Zielgruppe: EIN Avatar (Owner-Operator) statt B2C/B2B-Binaerfrage (deep)

Executive Council deep (Hormozi + Chris Do + Skeptical-Reviewer). Beide Seats konvergent:
Avatar = deutschsprachiger Owner-Operator (kauft wie Konsument, expandiert wie Firma); kein
B2B-Vertrieb Jahr 1 (Kapazitaetsmathe: 15-18 Founder-Logos unmoeglich bei 4 Tagen/Woche);
Piloten produktisiert per Ausnahme. Kreuzbefragung durch Skeptiker-Attacke ersetzt (Konvergenz
= Groupthink-Risiko) — Verdikt ship-with-changes mit 4 Treffern: Avatar-Praemisse ungetestet
(Pre-Order-Test >=50 in 30d definiert), Expansion ohne Produktmechanismus (Upside statt These
+ 6-Mo-Zeitlimit), Enno nicht als Pilot #1 auf die Folie (Verquickungsrisiko), Marken-Gate vor
Annual-Prepay. Offener Zielkonflikt Exit-Kurs vs. MRR-Gates an Gruender eskaliert. Decision:
wiki/decisions/2026-07-20-2key-zielgruppe-owner-operator.md. Learning: bei Seat-Konvergenz ist
der Skeptical-Review wichtiger, nicht ueberfluessig (im Record).

## [2026-07-20] work | 2Key-Deck Final-Review (v4->v5) + Gruender-Briefing

/work review (executive, standard). Beide Advisor lasen erstmals das ECHTE Artefakt (HTML) statt
Zusammenfassungen — deutlich schaerfere Findings: Hormozi fand Margen-Zahlenkollision, gedruckten
TODO-Marker, fehlendes IP-/Vesting-/Miss-Szenario und forderte die Reichweiten-Zusage als
Vertragszeile; Chris Do fand Fake-Zitat-Styling (Kostuem-Zitat ohne Kunden = Ehrlichkeits-Leck),
Doppel-Verwendung desselben Assets (Reichweite als Gegenleistung UND Einsatz), gedruckte
Schmerzgrenze (~15 %) und setzte Angebot-als-Schlussfolie durch (nie am Verkauf vorbeireden).
Alle 10 Must-Fixes in v5 umgesetzt (16 Folien); zusaetzlich gruender-briefing.md (Begriffe/
Zahlen/Ablauf/Einwaende) als Lernunterlage. Knowledge: Advisors auf ECHTEN Artefakten reviewen
lassen (Read-Zugriff) schlaegt Prompt-Zusammenfassungen deutlich — als Muster uebernehmen.

## [2026-07-20] setup | Fresh-machine install + neil-patel promoted to active
Ran /setup on a clean checkout: pulled all 6 clones, generated 12 machine-local
agents, installed user-global shims, validate clean. roster_status flagged neil-patel
(compiled system-prompt v6, 6 synth passes) as status-mismatched; promoted created→active
in roster.json (user-approved), re-ran gen_agents + install_global. Councils now have 3
voices: hormozi, chris-do, neil-patel. Note: python missing on this machine — used
python3 throughout. Knowledge: neil-patel active (config change recorded here + STATE.md).

## [2026-07-21] work | Autopilot run 2: 22 cycles across 4 clones (timebox 6h)
Roster-loop autopilot, time-boxed 6h (defaults), user-supervised via `/loop /roster-loop`.
Machine unblock at start: installed `yt-dlp` (missing on fresh machine, needed by discovery
+ ingest) and resolved a `git push` 403 wall (user granted `ki-business-agenten` write
access to `claes-work/*`). Then 22 clone-side cycles, all committed+pushed, zero rate limits:
- **hormozi** B×7 + S×1 → synthesis pass 30, system-prompt **v37→v38**; L2 2262→2307, P2 216.
- **neil-patel** B×3 + P×1 + S×1 → synthesis pass 7 + persona refresh, **v6→v8**; L2 533→557.
- **mkbhd** B×4 + S×1 → synthesis pass 4, **v3→v4**; L2 274→301.
- **chris-do** B×4 → L2 704→736, P2 358, debt 6.
Discovery refresh once (50 new rows, 14 fresh-upload P1 promoted → all drained bench-wide).
Focus-until-active exhausted: garyvee/networkchuck are `STATUS: UNINITIALIZED` (need the
interactive `/clone-setup` bootstrap — not autopilot-eligible).
Knowledge (open items for user):
- **mkbhd earned `active`** (compiled system-prompt v4) but roster.json still says `created`
  — a candidate 4th council voice; promotion deferred to user (governance decision).
- Hygiene: hormozi youtube-index footer vs ledger-L2 count drift (~10, accumulating) → lint pass.
  chris-do `ledger_set.py` writes CRLF vs LF history → add `.gitattributes`/LF-normalize.
- Calibration: report observed usage via `python3 tools/autopilot_journal.py append usage observed_pct=<n>`
  (evidence → wiki/learnings/roster-ingest-autopilot.md). Note: this machine has `python3` only, no `python`.

## [2026-07-21] work | Autopilot run 3: 5 cycles — halted on subagent spawn cap
Roster-loop autopilot, resumed morning of 2026-07-21 (timebox 6h). 5 deepening cycles,
all Stage B, all committed+pushed, zero rate limits, before the run hit a hard session
limit (not a timebox stop):
- **neil-patel** B×2 → L2 565→573, P2 653.
- **chris-do** B×1 → L2 744, P2 350, debt 7.
- **mkbhd** B×1 → L2 309, P2 1369.
- **hormozi** B×1 → L2 2315, P2 208.
**Halt cause:** subagent spawn cap **200/200** reached for the session — the dispatcher
spawns one general-purpose executor per cycle, and that budget (setup + run 2's 22 cycles
+ their nested per-file writers + run 3) is exhausted. Cannot spawn further executors.
**Remedy:** raise `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` or start a fresh session, then
`/loop /roster-loop`. Everything is idempotent — the next run resumes exactly from the
ledgers. Still-open items unchanged: mkbhd active-promotion (compiled v4) pending user
decision; garyvee/networkchuck need interactive `/clone-setup` bootstrap.

## [2026-07-21] work | Autopilot run 4: 6 cycles — user-stopped
Roster-loop autopilot, fresh session (timebox 6h, batch 8, `max_parallel_clones` 2),
started 10:12, stopped 10:49 on user request (`reason=user-stop`) — well inside the box.
Discovery was 16h old (not stale), so no refresh; worker identity unset → all clones
eligible; focus order picked the same disjoint pair every iteration.
- **neil-patel** B×3 → L2 581 → 589 → **597**; `@neilpatel` 2019-12 → 2020-01 solo-tactical
  drain. Open P1 0, P2 629. Synthesis debt 5 → **8/10**.
- **mkbhd** B×3 → L2 317 → 325 → **333**; `@mkbhd` 2009 origin tail (May 14 → Jun 17).
  Open P1 0, P2 1345. Synthesis debt 5 → **8/10**.
Zero rate limits, zero yt-dlp failures, zero back-offs; every batch committed+pushed by
the clone itself (`6f67315`, `bab2cb1`, `8f5a75b`, `741f5b8`, `24ff166`, `78a84c3`).
**Validated fix:** the collapse-nested-spawning rule held — 6 executors total for 6 cycles
(vs. the ~200 that capped run 3). Spawn budget is a non-issue at this rate.
**Next run picks up at:** both clones 2 batches from their Stage S checkpoint — the next
`/loop /roster-loop` will trigger synthesis on each. Unchanged open items: garyvee /
networkchuck still need interactive `/clone-setup` bootstrap (0 sources, status `created`).
Calibration: report observed usage via
`python3 tools/autopilot_journal.py append usage observed_pct=<n>`.

## [2026-07-21] council | 2Key Pricing & Conversion-Funnel (Hormozi x Chris Do, standard)
Keine Preissenkung trotz fehlendem Agent; Agent-Phantom raus aus Max; Kaufstrecke an den
Peak-Pain-Moment (Top-up + Ein-Klick im Popup); Gespart-Zeit-Zaehler; Verbrauchs-Trigger als
Educate-Sequenz; Jahresabo nur als verdientes Founding-Angebot mit 30-Tage-Garantie. Dissens
dokumentiert (Credit-Verfall, Auto-Renewal-Default). Record:
wiki/decisions/2026-07-21-2key-pricing-conversion-funnel.md. Artefakt im Zielprojekt:
2key-workforce wiki/konversions-strategie.md (per Feature-PR). Knowledge: decision.

## [2026-07-21] work | Autopilot run (vps) — 4 cycles, drained by YouTube bot-check block
Worker `vps` (owned: neil-patel, mkbhd, hormozi, chris-do). Discovery refreshed at run
start: 32 new rows, 0 fresh-promoted. All 4 owned clones then hit yt-dlp caption-fetch
failures (`8/8 caption fetches failed - YouTube bot-check block`) on their next cycle —
0 items ingested, no ledger change — and were each put into a 60-min back-off
(mkbhd/neil-patel until 11:45 UTC, hormozi/chris-do until 11:52 UTC). With all owned
clones in back-off and none at their fresh/focus target, the eligible set was empty this
iteration: stopped `reason=drained` per policy rather than spin. No new synthesis/persona
debt work happened this iteration. Next `/loop /roster-loop` will retry once back-offs
expire; if the bot-check block persists across workers/clones it may indicate a
broader YouTube-side rate-limit rather than per-clone noise — worth a look if it recurs.
Calibration: report observed usage via
`python3 tools/autopilot_journal.py append usage observed_pct=<n>`.

## [2026-07-21] work | Autopilot run (vps) — 0 cycles, drained by all-clones-backoff (recheck)
Fresh run immediately hit drained again: all 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still in the active back-off from the prior run (mkbhd/neil-patel until 11:45,
hormozi/chris-do until 11:52 UTC), triggered by the earlier YouTube bot-check block.
Discovery fresh (age 0.39h), no refresh needed, no executors dispatched. Next
`/loop /roster-loop` after ~11:52 UTC should find work again once back-offs clear.

## [2026-07-21] work | Autopilot run (vps) — 0 cycles, drained by all-clones-backoff (third check)
Same story a third time at 11:05 UTC: all 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) remain in back-off from the earlier YouTube bot-check block (mkbhd/neil-patel
until 11:45, hormozi/chris-do until 11:52 UTC). Discovery fresh (age 0.45h), no refresh
needed, no executors dispatched. This is a one-shot invocation (no wakeup scheduled);
whoever runs `/loop /roster-loop` next should retry after ~11:52 UTC.
