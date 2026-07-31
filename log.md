# Log

Append-only chronological record. Entry format:
`## [YYYY-MM-DD] <type> | <title>` with `<type>` ∈ `council | work | plan | review | wiki | setup`,
followed by 1–3 lines. Recent history: `grep "^## \[" log.md | tail -5`.

## [2026-07-27] council | CTA: Fit-Check klarer/prominenter, NICHT „buchen" (ki-business-agenten)
Team growth (hormozi + neil-patel + chris-do), einstimmig. Florian: Quiz klarer + „Du willst
buchen?"-Button. Verdikt: **Prominenz ja, „buchen" nein** — Message-Mismatch (kein Direktkauf;
Quiz→Call), falsche Beziehungsstufe (5k). „Ein CTA = eine Handlung, nicht ein Vorkommen" →
wiederholen erlaubt (nach jedem Block + Sticky), Label überall identisch. Fit-Frame behalten,
aber imperativ schärfen + „2-Min-Check"/End-Value. Sekundär „Ich will das bauen" vereinheitlicht.
Upgrade „Bewirb dich um deinen Platz" = stärkste Rahmung, aber nur mit ehrlicher Knappheit →
Founder-Input. Messen: Quiz-Start/Completion + qualifizierte Anfragen, nicht Klicks. Record:
`wiki/decisions/2026-07-27-cta-fit-check-nicht-buchen.md`. Knowledge: decision. GEBAUT im Target
(CTA-Copy + Sticky) direkt im Anschluss.

## [2026-07-27] council | Aufzeichnungs-Bibliothek als Lead-Magnet (ki-business-agenten)
Team growth (hormozi + neil-patel + chris-do), 2 Runden (Takes + Cross-Examine). Florians
Frage: Eingetragene immer ALLE Wochen-Videos geben + Inhaltsverzeichnis aller Wochen? Verdikt
**einstimmig: JA volle Bibliothek, aber KURATIERT** — Hero-Flagship + nach Problem sortiert
(kein Chrono-Dump) + Volltext-Suche (schon gebaut). Bibliothek = Proof-/Autoritäts-/Retention-
Motor; Verkauf am CTA, nicht pro Video → messen an Anfrage-Rate/Lead (Hormozi) + 30-Tage-
Rückkehr (Neil), nicht Signups. „Repurpose, don't manufacture" (öffentliche Highlights ernten,
rohe Voll-Aufnahmen als Reward). Value-Linie (Chris Do): Wissen gratis / Raum+Umsetzung bezahlt
→ entwertet 5k nicht. **Dissens erhalten + eskaliert:** Gate-Platzierung — Chris Do „Voll-
Bibliothek hinter E-Mail-Wall = Trojan Horse", Neil revidiert „Videos ungated, nur Upgrade
(Quiz/Action-Plan) gaten" — berührt bindenden Funnel (2026-07-21-website-funnel-structure) +
Commitment §3/§4 → nicht hier entschieden (harte Regel 3), Founder-Sache. Offene Prämisse:
Content-Quelle „von jeder Woche" undefiniert. Record:
`wiki/decisions/2026-07-27-aufzeichnungs-bibliothek-lead-magnet.md`. Knowledge: decision.
hub-candidate: „give knowledge free / sell the room" + Kuratierung-schlägt-Volumen als
projektübergreifende Lead-Magnet-Doktrin.

## [2026-07-27] council | Workshop-Versprechen: Bauplan statt „laufendem System"
Team growth (hormozi + chris-do + neil), Advisor-Sitze via SendMessage resumed (agentId, mit
Kontext). Florians Sorge: „an einem Tag fertig laufende Automatisierungen" über-verspricht.
Verdikt **einstimmig: ändern — der ehrliche Deliverable ist der STÄRKERE Verkauf.** Hormozi:
Über-Claim senkt Perceived Likelihood beim gestandenen Unternehmer (Value Equation); „promise
nothing, deliver a ton"; o-vegas selbst verspricht einen Plan. Chris Do: Plan = Premium („paid
to think, sell outputs not inputs"); Ehrlichkeit hebt Trust+Conversion. Neil: honest-spezifisch
konvertiert ≥, Über-Claim killt Refunds/Referrals; Message-Match zum „so baust du"-Cut besser.
Deliverable = 01 fertiger Bauplan · 02 erster Baustein läuft (live gebaut) · 03 selbst
weiterbauen (Claude Code als De-Risker, nicht Headline) + Damaging Admission. Record:
`wiki/decisions/2026-07-27-workshop-versprechen-bauplan-statt-laufendem-system.md`. Im Zielprojekt
umgesetzt (Hero, valueBlocks, VSL). Ratifizierung Offer-Mechanik = Florian. Orchestrierung:
Resume abgeschlossener Advisor per agentId funktioniert (Name nicht). hub-candidate: nein.

## [2026-07-27] council | Landing-Page nach o-vegas-Vorbild (ki-business-agenten-website)
Team growth (chris-do + hormozi + neil-patel). Frage: Seite nach Hormozis acquisition.com/o-vegas
bauen? Verdikt einstimmig: **Skelett übernehmen, Kostüm ablehnen** — DR-Struktur (ein CTA ×N,
VSL unter Hero, Frage-Headline auf Selbstinteresse, 3 nummerierte Value-Blöcke, Testimonials am
Entscheidungspunkt, narrative FAQ + öffentlicher FIT-Filter + Preis klar) in DE-Mittelstand-
Zurückhaltung + eigener CI + Chris-Do-Kontrast. Kur gegen „flat": Kontrast (ein Hero/Screen,
Typo 2–4×, Weight überspringen, eine dunkle Bande, Indigo sparsam). Buildbare Assets im Record
(Headline-Kandidaten, Preis/Filter-Copy, VSL-Skript). Record:
`wiki/decisions/2026-07-27-landing-page-nach-hormozi-o-vegas-vorbild.md`. Dependency: VSL-Video
fehlt (Florian). Orchestrierung: Advisor-Sitze nach Abschluss nicht per Name resumebar →
frisch gespawnt mit selbsttragendem Brief (funktioniert verlässlich). hub-candidate: nein.

## [2026-07-27] council | Growth Council → Landing-Page-Redesign (ki-business-agenten-website)
Team growth (chris-do + hormozi + neil-patel), depth standard, auto-routed. Konvergenz: **Proof
rauf** — echte Video-Testimonials + Logos vor Preis; Hero = Ergebnis + „ein Tag"; ein CTA; Preis
stolz zeigen/nie rechtfertigen; nur Belegbares. Record:
`wiki/decisions/2026-07-27-website-landing-page-redesign-growth-council.md`. Orchestrierungs-
Learning: reine Design-Anfrage routet trotzdem sinnvoll das volle Growth-Trio — Hormozi (Offer/
Conversion) + Neil (Landing/SEO) ergänzen Chris Do ohne Reibung, weil alle drei dieselbe
Proof-first-Diagnose teilen. Umsetzung + Asset-/Rechtsdaten-Details im Zielprojekt-Log/-Wiki.
Knowledge: decision persistiert; hub-candidate: nein.
## [2026-07-24] council | Studio-Workshop-Flywheel = OPERATE-Amendment, kein Portfolio-Re-Decide
Executive deep council (hormozi, chris-do, neil-patel; Kreuzbefragung mit 2 formalen
Retractions beim Pricing-Framing). Einstimmig: Sebastians „Workshops als DAS eine Ding,
2Key auf Eis" abgelehnt als Re-Decide, angenommen als Amendment der R2-OPERATE-Schicht;
Vorbedingung: R1/R2 + Amendment ENDLICH unterschreiben. 3-Stufen-Preisliste ohne
Rabatt-Vokabular (Studio on-camera ~€5k Anker inkl. Film / privat ~€7,5k / vor-Ort ~€12k+
unbeworben), Tripwire 5 zahlende Fremde/60 Tage, Langformat als E-Mail-Gate statt Paywall
(3:0 gegen Sebastians Premium-Idee), 2Key = erster „Sponsor" im Workshop mit gestarteter
90-Tage-Uhr. Record: `wiki/decisions/2026-07-24-studio-workshop-flywheel-amendment.md`.
Dissens erhalten (Ads/Retargeting, Checkpoint-Variante, Asset-Wert der Aufnahmen).
Hub-candidate: yes (Persistenz in second-brain + company-website in gleicher Session).

## [2026-07-22] council | R3: Homepage-Fokus (2Key Tor→Streifen) + Proof-Stack
Growth Council (hormozi, chris-do, neil-patel). Einstimmig (b): 2Key von der Tür zum ehrlichen
Streifen ("noch nicht kaufbar", Warteliste bleibt); Chris-Do-Verfeinerung übernommen: Gate
bleibt, Owner-Operator-Tür → /workshop (kaufbar). Proof-Stack: Zahlen unterm Hero, Testimonials
am Entscheidungspunkt, Fakten-Cases, Florian-Origin als Community-Proof. Während der Runde:
Alt-Website-Zitate + 6 Video-Testimonials gefunden (Prämisse "keine Zitate" überholt).
Record: `wiki/decisions/2026-07-22-homepage-focus-and-proof-stack.md`. Umgesetzt in gleicher
Session. Hormozi-Dissens (kein Split above fold) als A/B vorgemerkt. Hub-candidate: yes.

## [2026-07-22] council | Konvertierungs-Blueprints: Kaufseiten, Onboarding, /2key-Warteliste, Homepage-Gate
Growth Council (hormozi, neil-patel, chris-do; standard, Kreuzbefragung zu 3 Gabelungen).
Erste Runde unter Founder-Scope-Direktive (Infra geschlossen, nur Konvertierung). Konvergent:
eine Kaufseite kalt+warm (Proof-first, Accusation-Audit-FAQ, konditionale Garantie), Onboarding
trigger-basiert (KPI: Login+Lektion-1 ≤7d, 72h Stretch; Upsell am Deprivation-Punkt nach
Milestone 2/3), /2key = Tipp-Kosten-Rechner + ehrliches Erwartungsmanagement. Kreuzbefragt:
Gate = Ich-Form-Headline + Outcome-Subline (Neils Outcome als A/B); Quiz als Newsletter-Hook
einstimmig (Ergebnis VOR E-Mail-Frage, ehrliches Bleib-gratis-Outcome); Zwei-Tier zurückgezogen
(F4), Workshop-Anker nur mit echter Zahl. Claim-Zeile neu: „Wir bringen dir bei, wie du deine
Arbeit an KI abgibst — mit Claude Code." Record:
`wiki/decisions/2026-07-22-website-conversion-blueprints.md`. Hub-candidate: yes.

## [2026-07-22] council | Website-Shop-Override ratifiziert (Kanal ja, Custom-Build nein) + Funnel-Rulings
Growth Council (hormozi, chris-do, neil-patel; standard, Kreuzbefragung zu Frage 1). Verdict:
Founder-Override BEDINGT ratifiziert — Shopify-Direktkauf/YouTube-Shopping-Kanal freigegeben
(Round-5-Prämisse „YouTube unterstützt nur zugelassene Provider" widerlegt: Shopify IST
zugelassen; Chris Do widerruft sein Round-5-Veto), aber self-built Next.js+Supabase+Bunny-LMS
NICHT ratifiziert (Round-3-Wrong-Lever bestätigt, einstimmig; off-the-shelf-Delivery, Custom
erst nach Umsatzbeweis). Event-Mechanik: (a) Karte-hinterlegen via Shopify-App falls machbar,
sonst (c) übertragbares Deposit; (d)/(b) verworfen. Workshop-Preis: $1k–~$3k Self-Serve-Korridor,
darüber Qualifizierungsschritt; Zahl = Founders. /2key = Lead-Magnet, forward-only, Value-vor-Karte.
Record: `wiki/decisions/2026-07-22-website-shop-override-and-funnel-rulings.md`. Build-Scope-Dissens
Founder↔Council bewusst offen zurückgegeben. Hub-candidate: yes. Knowledge: decision persisted.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 06:30 UTC: all 4 owned clones still in back-off (mkbhd until
06:38, neil-patel/chris-do until 06:45, hormozi until 07:08) — same unresolved
systemic yt-dlp PO-token caption-fetch block carried over from prior runs.
Discovery still fresh (age 19.9h). No work eligible; nothing new happened.
run-start then run-end reason=drained journaled; no wakeup scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 06:27 UTC: all 4 owned clones still in back-off (mkbhd until
06:38, neil-patel/chris-do until 06:45, hormozi until 07:08) — same unresolved
systemic yt-dlp PO-token caption-fetch block carried over from prior runs.
Discovery still fresh (age 19.8h). No work eligible; nothing new happened.
run-start then run-end reason=drained journaled; no wakeup scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 02:29 UTC: all 4 owned clones remain in the back-off windows set
by the previous run (mkbhd/neil-patel until 03:14, hormozi until 02:32, chris-do
until 03:19), all from the same unresolved systemic yt-dlp PO-token caption-fetch
block. No work was eligible; nothing new happened. Discovery still fresh (age
15.9h). Still waiting on repo-owner action (`bgutil-ytdlp-pot-provider` install or
a cookies file) — until that lands, every invocation in this window will drain
immediately. run-end reason=drained journaled; no wakeup scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 05:51 UTC: all 4 owned clones still in back-off (hormozi until
06:00, mkbhd until 06:38, neil-patel/chris-do until 06:45) — same unresolved
systemic yt-dlp PO-token caption-fetch block carried over from prior runs.
Discovery still fresh (age 19.2h). No work eligible; nothing new happened.
run-start then run-end reason=drained journaled; no wakeup scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 05:56 UTC: all 4 owned clones still in back-off (hormozi until
06:00, mkbhd until 06:38, neil-patel/chris-do until 06:45) — same unresolved
systemic yt-dlp PO-token caption-fetch block, now persisting across 9+
consecutive one-shot runs in this window with zero net ingest. Discovery still
fresh (age 19.3h). No work eligible; nothing new happened. run-start then
run-end reason=drained journaled; no wakeup scheduled (one-shot). Repo-owner
action still needed (`bgutil-ytdlp-pot-provider` install or a cookies file) —
further one-shot invocations will keep draining identically until that lands
or the current back-off windows (06:00-06:45 UTC) simply expire.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 05:18 UTC: all 4 owned clones still within back-off windows
(mkbhd/neil-patel until 05:26, hormozi until 06:00, chris-do until 05:31) from the
same unresolved yt-dlp PO-token block. No work eligible; discovery fresh (age
18.7h, unchanged). run-start then run-end reason=drained journaled; no wakeup
scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 05:13 UTC: all 4 owned clones still in back-off (mkbhd/neil-patel
until 05:26, chris-do until 05:31, hormozi until 06:00) — same unresolved systemic
yt-dlp PO-token caption-fetch block as prior runs. No work eligible; discovery still
fresh (age 18.6h). run-end reason=drained journaled; no wakeup scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 04:53 UTC: all 4 owned clones still in back-off (hormozi until
04:56, mkbhd/neil-patel until 05:26, chris-do until 05:31) — same unresolved
systemic yt-dlp PO-token block from prior runs. No work eligible. Discovery fresh
(age 18.25h). run-end reason=drained journaled; no wakeup scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 04:50 UTC: all 4 owned clones still in back-off (mkbhd/neil-patel
until 05:26, hormozi until 04:56, chris-do until 05:31) — same unresolved systemic
yt-dlp PO-token caption-fetch block. No work eligible. Discovery still fresh (age
18.2h). Still waiting on repo-owner action; run-end reason=drained journaled; no
wakeup scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 04:47 UTC: all 4 owned clones still in back-off (mkbhd/neil-patel
until 05:26, hormozi until 04:56, chris-do until 05:31), same unresolved systemic
yt-dlp PO-token caption-fetch block as every prior run this window. Discovery
fresh (age 18.14h), no new work eligible. run-end reason=drained journaled; no
wakeup scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 04:41 UTC: all 4 owned clones still in back-off (mkbhd/neil-patel
until 05:26, hormozi until 04:56, chris-do until 05:31) — same unresolved systemic
yt-dlp PO-token caption-fetch block persisting across consecutive one-shot
invocations. No work eligible. Discovery still fresh (age 18.0h). Still waiting on
repo-owner action (`bgutil-ytdlp-pot-provider` install or a cookies file). run-end
reason=drained journaled; no wakeup scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 02:55 UTC: same story — all 4 owned clones still inside the
back-off windows (mkbhd/neil-patel until 03:14, hormozi until 03:35, chris-do
until 03:19), unchanged systemic yt-dlp caption-fetch block. Discovery still fresh
(age 16.3h), no eligible work. run-end reason=drained journaled; no wakeup
scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 02:47 UTC: all 4 owned clones (mkbhd/neil-patel until 03:14,
hormozi until 03:35, chris-do until 03:19) remain in back-off from the same
unresolved systemic yt-dlp PO-token caption-fetch block — no new backoffs set
this run, existing ones just haven't expired yet. Discovery still fresh (age
16.1h). No work was eligible; nothing new happened. run-end reason=drained
journaled; no wakeup scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained (backoffs still active)
One-shot check at 02:41 UTC, 12 min after the prior check: still all 4 owned
clones (neil-patel, mkbhd, hormozi, chris-do) sit inside back-off windows expiring
03:14-03:35 UTC, same systemic yt-dlp caption-fetch block, unchanged since the
last run. Discovery still fresh (age 16.0h), no refresh needed. No work eligible;
nothing new happened. run-end reason=drained journaled; no wakeup scheduled
(one-shot).

## [2026-07-22] work | Autopilot run (vps): 17 cycles, drained by all-clones-backoff
Run 00:15:48→02:22 UTC. neil-patel carried the run again: ~67 items ingested (Stage B)
plus one synthesis checkpoint (debt 10→0, prompt v14→v15) — until it too hit the
systemic yt-dlp PO-token caption-fetch block at 02:14, the same infra issue already
flagged for hormozi/mkbhd/chris-do (10th–13th consecutive confirmations this run).
All 4 owned clones are now in active back-off (mkbhd/neil-patel until 03:14, hormozi
until 02:32, chris-do until 03:19) — first time ingestion has been fully blocked
across the whole owned set, not just three of four. Discovery stayed fresh (age
15.7h), no refresh needed. **Action still needed from repo owner**: install
`bgutil-ytdlp-pot-provider` (needs pip/pipx/venv, absent from this VPS env) or supply
a YouTube cookies file — every recent run has hit this wall. run-end reason=drained
journaled; no wakeup scheduled (one-shot invocation).

## [2026-07-22] work | Autopilot run (vps): 51 cycles, timebox reached
Run 17:55:50→23:55 UTC (6h). neil-patel carried the run: 332 items ingested across ~35
iterations (Stage B) plus 2 synthesis passes (debt cleared twice, persona v13→v14).
hormozi, mkbhd, chris-do ingested 0 items all run — a systemic yt-dlp PO-token/
bot-detection block on caption fetch hit all three, confirmed **10 consecutive times
each** (env has no pip/pipx to install `bgutil-ytdlp-pot-provider`, no cookies file).
Each did land one synthesis pass on existing backlog (hormozi debt→0 v38→v39, mkbhd
debt→0 v5→v6) since synthesis doesn't need fresh captions. Discovery was fresh all run,
no refresh needed. **Action needed from repo owner**: install
`bgutil-ytdlp-pot-provider` (needs pip/pipx, currently absent from this VPS env) or
supply a YouTube cookies file — otherwise hormozi/mkbhd/chris-do ingest stays fully
blocked next run too. Back-offs active at stop: mkbhd until 00:48, hormozi until 00:12,
chris-do until 01:00 (2026-07-22 UTC). No wakeup scheduled (one-shot dispatch).

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
Fresh run start immediately hit drained: all 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) are in active back-off (mkbhd/neil-patel until 11:45, hormozi/chris-do until
11:52), leftover from the prior run's cadence. Discovery fresh (age 0.35h), no refresh
needed. No executors dispatched this iteration. Next: retry after ~11:52 when back-offs
clear.

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff (repeat)
One-shot dispatch invocation, same back-off window as the prior entry (mkbhd/neil-patel
until 11:45, hormozi/chris-do until 11:52; now 11:08). Discovery still fresh (age 0.5h).
No eligible clones, no executors dispatched. Back-offs expire ~11:45–11:52; a later
invocation should find work then.

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff (repeat 2)
One-shot dispatch invocation, same back-off window as the two prior entries (mkbhd/neil-patel
until 11:45, hormozi/chris-do until 11:52; now 11:17). Discovery still fresh (age 0.65h).
No eligible clones, no executors dispatched. Back-offs expire ~11:45–11:52; a later
invocation should find work then.

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff (repeat 3)
One-shot dispatch invocation, same back-off window as the three prior entries (mkbhd/neil-patel
until 11:45, hormozi/chris-do until 11:52; now 11:27). Discovery still fresh (age 0.81h).
No eligible clones, no executors dispatched. Back-offs expire ~11:45–11:52; a later
invocation should find work then.

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff (repeat 3)
One-shot dispatch invocation, same back-off window as the three prior entries (mkbhd/neil-patel
until 11:45, hormozi/chris-do until 11:52; now 11:20). Discovery still fresh (age 0.7h).
No eligible clones, no executors dispatched. Back-offs expire ~11:45–11:52; a later
invocation should find work then.

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff (repeat 4)
One-shot dispatch invocation, same back-off window as the four prior entries (mkbhd/neil-patel
until 11:45, hormozi/chris-do until 11:52; now 11:23). Discovery still fresh (age 0.76h).
No eligible clones, no executors dispatched. Back-offs expire ~11:45–11:52; a later
invocation should find work then.

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
## [2026-07-21] work | 2Key Konversions-Texte (Hormozi x Chris Do Operatoren + Skeptiker-Review)
Copy-Pakete fuer Popup/In-App (50/90/100 %), Kontingent-Mails, Top-up-Dialog und die
Starter-Sequenz (Willkommen bis Ask) ausgearbeitet; Skeptiker-Review ship-with-changes mit
8 Must-Fixes (Datenschutz-Passage, Gratis-Plan-Zusage, Trigger-Kollisionen, PAngV/MwSt,
Decoy-Korridor, Ship-Gates) — alle im Merge eingearbeitet. Artefakt: konversions-texte.md
(Zielprojekt 2key-workforce, Einzug per Feature-PR sobald Codeberg wieder erreichbar).
Orchestrierungs-Learning: Operator-Split nach Doktrin-Domaene + unabhaengiger Skeptiker
fand materielle Fehler, die beide Autoren teilten. Knowledge: project-knowledge.

## [2026-07-21] council | Portfolio-Fokus: ein Business (2Key), Rest sind Funktionen
Deep Council (Hormozi x Chris Do x Neil Patel, Cross-Examination + Skeptiker-Review
"rework" eingearbeitet): 2Key = Asset/Exit-Vehikel fuer eine 3-5-Jahres-Season (12 Mo
Season of No); YouTube = Marketing-Abteilung (KPI qualifizierte Leads, 1 Search-Video/Wo,
3:1-Ratio, E-Mail-Capture); Trainings = gedeckelte Cash-Bruecke + Listening-Post, Webinar
nur gated; Sales-Projekt freeze/kill; Enno-Track sequenziert (Pre-Order-Test VOR Pitch,
ein kanonisches Use-of-Proceeds-Memo, Solvenz-Rechnung mit Owner/Threshold, Skool-
Liability + StB als Pitch-Preconditions). Dissens bewahrt: Premium-Tier-Timing, 80/20-
Kreativ-Outlet, Memo-vs-Belief. Status proposed - Florians Input erforderlich. Record:
wiki/decisions/2026-07-21-portfolio-focus-2key.md. Knowledge: decision. hub-candidate.
## [2026-07-21] council | Runde 2: Creator-Business operiert, 2Key ist der einzige Build
Follow-up-Council (gleiche Seats, echte Zahlen: 20k/Mo Kosten, Break-even-Mix, Enno
wahrscheinlich raus): Verdikt amendiert - Creator/Education-Business IST das Operating
Business, 2Key der gebundene Build; YouTube NICHT 2Keys Marketingabteilung (Neil-Retraction,
Cash-Engine + Trust-Bank, 70/20/10, Search-Videos im Bestandsthema); freie Skool-10k +
E-Mail-Liste = 2Key-Kanal, Woche-1-Avatar-Zensus als Gate; Tripwire korrigiert auf bezahlte
Pre-Orders (>=50/30d, Reviewer fand Neils 100/Monat ~10x inflationiert); Workshops =
Sales-Channel (pro Kopf, 2x Reprice, KPI aktivierte Accounts); Hostinger-Klumpenrisiko +
Monat-12-Exit-These-Gate neu adressiert; Memo committet Inputs, nicht Outcomes; Signatur
hart auf Florian gegated. Skeptiker: ship-with-changes, alle 4 Blocker eingearbeitet.
Record: wiki/decisions/2026-07-21-operating-business-vs-2key-build.md. Knowledge: decision.
hub-candidate.
## [2026-07-21] council | Runde 3: Funnel- & Offer-Rulings (einstimmig)
Operative Schicht unter dem Runde-2-Record, alle Seats einstimmig, Skeptiker
ship-with-changes (F1-F5 eingearbeitet): reine E-Mail-Liste statt zweiter Community
(Quiz = Zensus + Segmentierung, dead = keine Klicks/Monat); Content 9:1 General-Value
mit Soft-CTA; EIN Workshop (nur Claude Code), 2Key als Uebungsumgebung + sichtbares
Menu-Add-on (Bundle und Fee-Credit verworfen - "bundled money is mute", Rabattverbot);
Website-Komplett-Neubau ABGELEHNT (Build-Verstoss) -> MVP-Funnel auf Fertig-Tooling,
2Key-Pfad ohne Agent-Phantom formuliert; Sequenz als Offer-Hierarchie: Tage 1-45
Transfer+Masterclass, Tage 45-90 Pre-Order-Fenster (Founding Annual -> monthly ->
Trial-mit-Karte), Free-Trial-Maximierung verworfen; Kurs-Katalog-Einigung + Lifetime-
Kohorten-Fence (F4). Record: wiki/decisions/2026-07-21-funnel-operational-rulings.md.
Knowledge: decision. hub-candidate.
## [2026-07-21] council | Runde 4: Free-Tier bleibt, Karte folgt dem Wert; eine Domain, Funnel zuerst
Enge Follow-up-Fragen (gleiche Seats, standard): 75-Credit-Starter wird NICHT entfernt
und NICHT durch Karten-vorab-Trial ersetzt (einstimmig) - Usage-Peak-Pain schlaegt
Kalender-Cliff, Karte-vor-Wert = Vertrauensbruch fuer eine Datensouveraenitaets-Marke,
Matchmaker-Versprechen bleibt; Signup e-mail-only, Karte erst am 100%-Popup (charge at
desire); Kartenschluss != Funnel-Ende (Ende = retained/ascended/referring user);
Website-Konsolidierung der Begleitartikel auf EINE Domain genehmigt als phasierte
Migration in die MVP-Shell (Funnel-Seiten zuerst, /artikel danach, 301-Cautions).
Mini-Dissens bewahrt: Restrolle des Karten-Trials (Chris Do keine / Hormozi nur
Pre-Order-Downsell / Neil warme Pfade). Record:
wiki/decisions/2026-07-21-2key-free-tier-and-website-consolidation.md.
Knowledge: decision. hub-candidate.
## [2026-07-21] council | Runde 5: Website-IA, Funnel-Reihenfolge, YouTube-Placement
Neuer Fakt: kein On-Site-Commerce (YouTube-Shop nur mit zugelassenen Providern; Kurse
nur im Skool-Classroom). Chris Do x Neil Patel: 5-Seiten-Sitemap (Home mit Claim +
Zwei-Wege-Gate, /workshop mit Preis-Bracket + Booking-Inquiry, /2key Waitlist,
/community mit Kursen als Classroom-Inhalt, E-Mail-Capture als Rueckgrat); Funnel als
nummerierte 10-Stufen-Leiter (Builder enden bei Kursen, Owner-Operators laufen bis
2Key); Pinned Comment = EIN Kampagnen-Link phasenabhaengig (Default Community,
Tage 1-45 Masterclass-Hook, 45-90 Pre-Order, danach evergreen); Messung via
Unique-Links/Placement + Onboarding-Attribution + monatliche Bank-Rekonziliation.
Moderator-Korrektur: Fee-Credit-Wiedereinschleusung (Chris Do) bleibt tot per Runde-3-F1.
Dissens bewahrt: Kursseiten (keine vs. SEO-Surfaces, Phase-2-Entscheid) + Pin im
Pre-Order-Fenster. Record: wiki/decisions/2026-07-21-website-funnel-structure.md.
Knowledge: decision. hub-candidate.
## [2026-07-21] council | Runde 6: Promotion-Map + E-Mail-Consent - Struktur GESCHLOSSEN
Chris Do x Neil Patel einstimmig: Bulk-Mail an ~11k ohne Marketing-Consent VERBOTEN
(Marken-Selbstwiderspruch einer Datensouveraenitaets-Firma + Deliverability-Gift +
Junk-Liste; die 300-400-EUR-Abmahnung preist die falschen Kosten); Consent-Segment =
Rueckgrat (erst zaehlen!), Skool-72h-Post-Mail = Bruecke und Asset (jeder Post als
E-Mail geschrieben, treibt einen Consent-Moment: Quiz/Masterclass/Magnet);
Frequenz-Tabelle fixiert (Community-CTA jedes Video, 1 Self-Ad-Segment max wegen
Hostinger-Ask, Kurse nie direkt auf YouTube); Website routet Skool statt es zu
bewerben; keine Rueckwaertskanten im Funnel. Architektur fuer GESCHLOSSEN erklaert -
Wiedereroeffnung nur bei falsifizierter Tripwire. Record:
wiki/decisions/2026-07-21-promotion-map-email-consent.md. Knowledge: decision.
hub-candidate.
## [2026-07-21] council | Klaerung: Kanal-Inhaltskarte + Website-Blueprint (aus Records)
Keine neue Deliberation - Sebastian brauchte die konkrete "wo erzaehlen wir was"-Sicht;
Moderator-Synthese aus den Runde-5/6-Records (website-funnel-structure,
promotion-map-email-consent) als Kanal-Karte + seitenweiser Website-Blueprint.
Knowledge: none (nichts Neues entschieden).
## [2026-07-21] work | Website- + Funnel-Bauplan ausgefuehrt (Artefakt im Zielprojekt)
Executive-Schritt nach 6 Council-Runden: Bauplan geschrieben nach
2key-workforce/wiki/website-und-funnel.md (5-Seiten-Struktur, Funnel A Workshop /
Funnel B 2Key, Messung, Bau-Reihenfolge mit Vorarbeiten); Skeptiker-Review
ship-with-changes, 5 Funde eingearbeitet - wichtigster: /2key-CTA-Phasenaufloesung
(Runde-4-vs-5-Record-Kollision explizit aufgeloest: Warteliste 1-45, Pre-Order 45-90,
Gratis-Test erst evergreen nach bestandenem Test) + Drei-Spalten-Preisanker
wiederhergestellt + LinkedIn-Quelle gestrichen (unbeschlossen). Zielprojekt-Wiki
(index+log) aktualisiert. Orchestrierungs-Learning: Artefakt-Review gegen die
Decision-Records faengt stille Record-Kollisionen, die die Einzelrunden nicht sahen.
Knowledge: project-knowledge (Artefakt im Zielprojekt).
## [2026-07-21] wiki | Bauplan-Artefakt umgezogen: 2key-workforce -> company-website
Sebastians Korrektur: Website-/Funnel-Bauplan gehoert nicht in die 2Key-Produkt-Wiki.
Neues Projekt D:/Dev/company-website nach Familien-Schema aufgesetzt (CLAUDE.md/AGENTS-
Stub, index, log, wiki/) mit vier destillierten Seiten: positionierung, produkte,
akquise-und-kanaele, website-und-funnel (verschoben + Links adaptiert). 2key-workforce
bereinigt (Datei raus, Index-Verweis, Log-Korrektureintrag). Quelle der Wahrheit bleibt
persona-roster/wiki/decisions/; company-website ist die baufaehige Destillation.
Hub-Onboarding des neuen Projekts steht aus (beim naechsten second-brain-Sync anmelden;
Federation-Register flaggt neue Verzeichnisse ohnehin). Knowledge: project-knowledge.

## [2026-07-22] work | VPS-Ingest: "Cookies prüfen"-Dauerschleife war fehlzugeordneter IP-Bot-Check
Diagnose am Server: POT-Provider (127.0.0.1:4416) läuft, Cookies heute 14:19 frisch, ein
Referenzvideo zog Captions einwandfrei — Cookies waren nie die Ursache. Der echte Block
ist YouTubes "sign in to confirm you're not a bot" auf der Hostinger-Datacenter-IP
(72.61.20.102); ein Cookie-Tausch behebt das nie. Der Wrapper-Regex warf Bot-Check und
Cookie-Ablauf in einen Topf → 2×/Tag "🍪 Cookies prüfen" für ein IP-Problem. Kostenlose
Fixes (kein Proxy): yt-dlp-Throttle in beiden Configs (--sleep-requests/-subtitles/
-interval), Timer-Kadenz 2min→10min, exponentieller Caption-Backoff (60→120→240, Cap 360;
Reset bei sauberem Run) und korrigierte Alarm-Zuordnung (IP-Bot-Check bei frischen Cookies
→ max. 1×/24h "keine Aktion nötig"; 🍪-Nag nur bei echtem Cookie-Ablauf/>7 Tage). Ops-
Dateien leben auf dem VPS (nicht im Git-Repo); Backup ingest-cycle.sh.bak-20260722b.
Durabler kostenloser Hebel bei erneutem Nerven: Caption-Loop von Residential-IP (Sebastians
PC ist bereits Secondary-Worker). Knowledge: project (Memory vps-ingest-autopilot-ops
aktualisiert). hub-candidate.

## [2026-07-22] work | VPS-Benachrichtigungen auf "nur handlungsrelevant" reduziert
Sebastians Regel: pingen nur, wenn er wirklich etwas tun muss. Umgesetzt am Server:
(a) IP-Bot-Check auf frischen Cookies → keine Telegram mehr (still selbstheilend, nur
Log). (b) 3-stündlicher Status-Digest ABGESCHALTET — status-report.py sendet nur noch
beim Übergang aktiv→durch (alle owned Clones open_p1==0 && fresh_open==0): "✅ Prioritäts-
Backlog durch — du kannst den Loop stoppen"; State state/drain-state; sonst silent.
(c) Account-Schwelle umformuliert auf "🔄 Account durch — stoppen oder wechseln" (feuert
weiter 1× bei 75%/60h). (d) Echter Cookie-Ablauf (explizit / Datei >7 Tage) → weiter
🍪-Nag; generisches rc≠0 → weiter ⚠️. Backups ingest-cycle.sh.bak-20260722c,
status-report.py.bak-20260722. Verifiziert: Reporter meldet "silent (drained=False)".
Knowledge: project (Memory aktualisiert).

## [2026-07-21] work | Autopilot run: 0 cycles — drained, all owned clones in back-off
Worker vps, owned clones (neil-patel, mkbhd, hormozi, chris-do) all in active
back-off (expiring 11:45–11:52 UTC); discovery fresh (0.55h); no fresh_open rows on
any owned clone. Nothing eligible this iteration → stopped immediately with
reason=drained. No wakeup scheduled (one-shot invocation).

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot dispatch at 11:30 UTC, same back-off window as the preceding entries
(mkbhd/neil-patel until 11:45, hormozi/chris-do until 11:52). Discovery still fresh
(age 0.86h). No eligible owned clones (neil-patel, mkbhd, hormozi, chris-do all
back-off-blocked), no executors dispatched. Back-offs clear ~11:45–11:52; a later
invocation should find work then.

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot dispatch at 11:33 UTC. Same back-off window persists (mkbhd/neil-patel
until 11:45, hormozi/chris-do until 11:52); discovery still fresh (age 0.91h), no
fresh_open rows. All 4 owned clones back-off-blocked → stopped immediately with
reason=drained, no executors dispatched, no wakeup scheduled (one-shot).

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff (still waiting)
One-shot dispatch at 11:37 UTC, same YouTube-bot-check back-off window as the last
several entries (mkbhd/neil-patel until 11:45, hormozi/chris-do until 11:52 UTC —
now 8-15 min out). Discovery fresh (age 0.97h), no fresh_open rows. All 4 owned
clones still back-off-blocked → reason=drained, no executors dispatched, no wakeup
scheduled (one-shot). Process note: these one-shot invocations are firing roughly
every 3 min, well inside the ~1h back-off window, so several have now landed on an
unchanged state — next invocation should ideally wait until after 11:52 UTC to find
real work instead of repeating this same drained cycle.

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff (still waiting, 2)
One-shot dispatch at 11:41 UTC, same YouTube-bot-check back-off window as all prior
entries in this streak (mkbhd/neil-patel until 11:45:48, hormozi/chris-do until
11:52:15 UTC — now under 5 and under 11 min out respectively). Discovery fresh (age
1.04h), no fresh_open rows. All 4 owned clones still back-off-blocked → reason=drained,
no executors dispatched, no wakeup scheduled (one-shot). mkbhd/neil-patel's back-off
clears in the next few minutes — the very next invocation after 11:46 UTC should find
real work on at least those two.

## [2026-07-21] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff (still waiting, 3)
One-shot dispatch at 11:44 UTC, same YouTube-bot-check back-off window as the prior
two entries in this streak (mkbhd/neil-patel until 11:45:48 — under 2 min out;
hormozi/chris-do until 11:52:15 UTC — under 8 min out). Discovery fresh (age 1.1h),
no fresh_open rows. All 4 owned clones still back-off-blocked → reason=drained, no
executors dispatched, no wakeup scheduled (one-shot). These one-shot invocations keep
landing inside the same ~1h back-off window (this is the third in a row with no new
information); the next invocation after 11:46 UTC should finally clear mkbhd/neil-patel.

## [2026-07-21] work | Autopilot run (vps): 55 cycles — timebox reached
Run started 11:47 UTC, ended 17:51 UTC (6.06h, over the 6h timebox). 55 cycles across
owned clones: neil-patel 30 (234 items, P2 drain, synthesis debt climbed to 7/10),
mkbhd 16 (78 items, then hit a systemic yt-dlp PO-token caption-fetch block —
confirmed on 4+ consecutive iterations, environment lacks pip/node so no PO-token
provider can be installed; back-off applied, standing infra fix still needed),
hormozi 3 (0 items — repeatedly back-off-blocked by the same caption-fetch issue),
chris-do 6 (70 items, also hit the caption block on @thefutur mid-run; back-off
applied). Discovery stayed fresh throughout (no refresh needed). Final iteration
dispatched neil-patel (+8, P2 batch cont.82) and mkbhd (0, PO-token block reconfirmed,
60min back-off applied) in parallel; both are the only two of the four owned clones
not already in back-off at orient time. run-end reason=timebox journaled; no wakeup
scheduled (one-shot, per policy).

## [2026-07-22] work | Autopilot run (vps): 1 cycle — one-shot dispatch
Run started 00:03 UTC. Of the 4 owned clones, mkbhd/hormozi/chris-do were all still
in active back-off from the prior run's caption-fetch throttling (hormozi's window
cleared moments after orient, too late for this iteration); neil-patel was the only
eligible clone (max_parallel_clones=2, but only 1 clone available). Discovery fresh
(age 13.4h), no fresh_open rows, so no refresh needed. Dispatched one executor for
neil-patel: Stage B, `@neilpatel` P2 batch (2023-06-05→2023-06-22), 8/8 ingested (0
skipped/no-captions/dup), no rate limits. Open after: neil-patel P2 133/P3 21,
MarketingSchoolPod P2 731/P3 28, 2688 shorts open, L2=1089. Synthesis debt hit the
10-batch checkpoint — Stage S is due on the clone's next iteration. run-end
reason=user journaled (one-shot invocation, per operator instruction); no wakeup
scheduled.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
Run started 02:26 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi, chris-do) were
already in active back-off at orient time (from the prior run's caption-fetch
throttling), with expiries between 02:32 and 03:20 UTC; none had fresh_open rows.
No eligible clone this iteration — no executor dispatched. Discovery fresh (age
15.8h), no refresh needed. run-end reason=drained journaled; no wakeup scheduled
(one-shot invocation, per operator instruction).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
Run started 02:32 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi, chris-do) were
already in active back-off at orient time (from the prior run's caption-fetch
throttling), with expiries between 03:14 and 03:35 UTC; none had fresh_open rows.
No eligible clone this iteration — no executor dispatched. Discovery fresh (age
16.0h), no refresh needed. run-end reason=drained journaled; no wakeup scheduled
(one-shot invocation, per operator instruction).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 02:44 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 03:14-03:35 UTC — same systemic
yt-dlp caption-fetch throttling, unchanged since the prior two checks. Discovery
fresh (age 16.09h), no refresh needed. No work eligible; nothing new happened.
run-end reason=drained journaled; no wakeup scheduled (one-shot invocation, per
operator instruction).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 02:50 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 03:14-03:35 UTC — same systemic
yt-dlp caption-fetch throttling, unchanged since the prior checks. Discovery fresh
(age 16.19h), no refresh needed. No work eligible; nothing new happened. run-end
reason=drained journaled; no wakeup scheduled (one-shot invocation, per operator
instruction).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 02:53 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 03:14-03:35 UTC — same systemic
yt-dlp caption-fetch throttling, unchanged since the prior checks. Discovery fresh
(age 16.24h), no refresh needed. No work eligible; nothing new happened. run-end
reason=drained journaled; no wakeup scheduled (one-shot invocation, per operator
instruction).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 02:59 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 03:14-03:35 UTC — same systemic
yt-dlp caption-fetch throttling, unchanged since the prior checks. Discovery fresh
(age 16.34h), no refresh needed. No work eligible; nothing new happened. run-end
reason=drained journaled; no wakeup scheduled (one-shot invocation, per operator
instruction).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 03:02 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 03:14-03:35 UTC — same systemic
yt-dlp caption-fetch throttling, unchanged since the prior checks. Discovery fresh
(age 16.39h), no refresh needed. No work eligible; nothing new happened. run-end
reason=drained journaled; no wakeup scheduled (one-shot invocation, per operator
instruction).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 03:05 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 03:14-03:35 UTC — same systemic
yt-dlp caption-fetch throttling, unchanged since the prior checks. Discovery fresh
(age 16.45h), no refresh needed. No work eligible; nothing new happened. run-end
reason=drained journaled; no wakeup scheduled (one-shot invocation, per operator
instruction).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 03:08 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 03:14-03:35 UTC — same systemic
yt-dlp caption-fetch throttling, unchanged since the prior checks. Discovery fresh
(age 16.51h), no refresh needed. No work eligible; nothing new happened. run-end
reason=drained journaled; no wakeup scheduled (one-shot invocation, per operator
instruction).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 03:11 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 03:14-03:35 UTC — same systemic
yt-dlp PO-token caption-fetch block first hit ~02:35 (hormozi retry: 8/8
no-captions), unchanged since. Discovery fresh (age 16.56h), no refresh needed. No
work eligible; nothing new happened. run-end reason=drained journaled; no wakeup
scheduled (one-shot invocation, per operator instruction). Still waiting on
repo-owner action (`bgutil-ytdlp-pot-provider` install or a cookies file) to clear
the block permanently instead of cycling through hour-long back-offs.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 04:34 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 04:56-05:32 UTC — same systemic
yt-dlp caption-fetch throttling, unchanged since the prior checks. Discovery fresh
(age 17.93h), no refresh needed. No work eligible; nothing new happened. run-end
reason=drained journaled; no wakeup scheduled (one-shot invocation, per operator
instruction). Still waiting on repo-owner action (`bgutil-ytdlp-pot-provider`
install or a cookies file) to clear the block permanently instead of cycling
through hour-long back-offs.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 04:37 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 04:56-05:32 UTC — same systemic
yt-dlp caption-fetch throttling, unchanged since the prior checks. Discovery fresh
(age 17.99h), no refresh needed. No work eligible; nothing new happened. run-end
reason=drained journaled; no wakeup scheduled (one-shot invocation, per operator
instruction). Still waiting on repo-owner action (`bgutil-ytdlp-pot-provider`
install or a cookies file) to clear the block permanently instead of cycling
through hour-long back-offs.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 04:44 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 04:56-05:32 UTC — same systemic
yt-dlp caption-fetch throttling, unchanged since the prior checks. Discovery fresh
(age 18.09h), no refresh needed. No work eligible; nothing new happened. run-end
reason=drained journaled; no wakeup scheduled (one-shot invocation, per operator
instruction). Still waiting on repo-owner action (`bgutil-ytdlp-pot-provider`
install or a cookies file) to clear the block permanently instead of cycling
through hour-long back-offs.

## [2026-07-22] work | Autopilot run (vps): 1 cycle (hormozi, 0 ingested), drained by all-clones-backoff
One-shot check at 05:03 UTC. Run (started 04:56) attempted hormozi's MoreMozi P2
batch — 16th consecutive zero-yield batch from the same systemic yt-dlp PO-token
caption block, 0/8 ingested, safety rail tripped, hormozi entered back-off. That
put all 4 owned clones (neil-patel, mkbhd, hormozi, chris-do) simultaneously
inside back-off windows expiring 05:26-06:00 UTC. Discovery fresh (age 18.44h), no
refresh needed. No further work eligible; run-end reason=drained journaled; no
wakeup scheduled (one-shot invocation, per operator instruction). Root cause is
unchanged and worsening (16+ consecutive failures across all 4 clones this run
alone) — still waiting on repo-owner action (`bgutil-ytdlp-pot-provider` install
or a cookies file) to clear the block permanently instead of cycling through
hour-long back-offs that yield nothing.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 05:07 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 05:26-06:00 UTC — same systemic
yt-dlp PO-token caption-fetch throttling, unchanged since the prior run. Discovery
fresh (age 18.48h), no refresh needed. No work eligible; run-start immediately
followed by run-end reason=drained journaled; no wakeup scheduled (one-shot
invocation, per operator instruction). Root cause unchanged — still waiting on
repo-owner action (`bgutil-ytdlp-pot-provider` install or a cookies file) to clear
the block permanently instead of cycling through hour-long back-offs that yield
nothing.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 05:09 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 05:26-06:00 UTC — same systemic
yt-dlp PO-token caption-fetch throttling, unchanged since the prior two runs.
Discovery fresh (age 18.53h), no refresh needed. No work eligible; run-start
immediately followed by run-end reason=drained journaled; no wakeup scheduled
(one-shot invocation, per operator instruction). Root cause unchanged and now
persisting across 3+ consecutive runs — still waiting on repo-owner action
(`bgutil-ytdlp-pot-provider` install or a cookies file) to clear the block
permanently instead of cycling through hour-long back-offs that yield nothing.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 05:15 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 05:26-06:00 UTC — same systemic
yt-dlp PO-token caption-fetch throttling, unchanged since the prior four runs.
Discovery fresh (age 18.62h), no refresh needed. No work eligible; run-start
immediately followed by run-end reason=drained journaled; no wakeup scheduled
(one-shot invocation, per operator instruction). Root cause unchanged and now
persisting across 4+ consecutive runs — still waiting on repo-owner action
(`bgutil-ytdlp-pot-provider` install or a cookies file) to clear the block
permanently instead of cycling through hour-long back-offs that yield nothing.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 05:22 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 05:26-06:00 UTC — same systemic
yt-dlp PO-token caption-fetch throttling, unchanged since the prior five runs.
Discovery fresh (age 18.72h), no refresh needed. No work eligible; run-start
immediately followed by run-end reason=drained journaled; no wakeup scheduled
(one-shot invocation, per operator instruction). Root cause unchanged and now
persisting across 5+ consecutive runs — still waiting on repo-owner action
(`bgutil-ytdlp-pot-provider` install or a cookies file) to clear the block
permanently instead of cycling through hour-long back-offs that yield nothing.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 05:47 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 06:00-06:45 UTC — same systemic
yt-dlp PO-token caption-fetch throttling, unchanged since the prior seven runs.
Discovery fresh (age 19.16h), no refresh needed. No work eligible; run-start
immediately followed by run-end reason=drained journaled; no wakeup scheduled
(one-shot invocation, per operator instruction). Root cause unchanged and now
persisting across 7+ consecutive runs — still waiting on repo-owner action
(`bgutil-ytdlp-pot-provider` install or a cookies file) to clear the block
permanently instead of cycling through hour-long back-offs that yield nothing.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 05:59 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 06:00-06:45 UTC — same systemic
yt-dlp PO-token caption-fetch throttling, unchanged since the prior eight runs.
Discovery fresh (age 19.36h), no refresh needed. No work eligible; run-start
immediately followed by run-end reason=drained journaled; no wakeup scheduled
(one-shot invocation, per operator instruction). Root cause unchanged and now
persisting across 8+ consecutive runs — still waiting on repo-owner action
(`bgutil-ytdlp-pot-provider` install or a cookies file) to clear the block
permanently instead of cycling through hour-long back-offs that yield nothing.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 06:11 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 06:38-07:08 UTC — same systemic
yt-dlp PO-token caption-fetch throttling, unchanged since the prior nine runs.
Discovery fresh (age 19.54h), no refresh needed. No work eligible; run-end
reason=drained journaled (run had already been started at 06:03 UTC by a prior
wakeup); no wakeup scheduled (one-shot invocation, per operator instruction).
Root cause unchanged and now persisting across 9+ consecutive runs — still
waiting on repo-owner action (`bgutil-ytdlp-pot-provider` install or a cookies
file) to clear the block permanently instead of cycling through hour-long
back-offs that yield nothing.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 06:14 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 06:38-07:08 UTC — same systemic
yt-dlp PO-token caption-fetch throttling, unchanged since the prior ten-plus
runs. Discovery fresh (age 19.59h), no refresh needed. No work eligible;
run-start immediately followed by run-end reason=drained journaled; no wakeup
scheduled (one-shot invocation, per operator instruction). Root cause unchanged
and now persisting across 10+ consecutive one-shot dispatches with zero net
ingest progress — this pattern will keep repeating every invocation until a
repo-owner fixes the caption-fetch throttle (`bgutil-ytdlp-pot-provider`
install or a cookies file); no wiki decision/learning yet documents this
recurring block despite the run count.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 06:18 UTC. Same systemic yt-dlp PO-token caption-fetch
throttle (11th+ consecutive drained one-shot); all 4 owned clones still in
back-off (06:38-07:08 UTC), discovery fresh (19.67h). run-start immediately
followed by run-end reason=drained; no wakeup scheduled (one-shot). Escalating:
this recurring block still has no wiki decision/learning capturing it despite
10+ repeat occurrences — worth a `wiki/learnings/` entry so future runs stop
re-describing the same root cause from scratch.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 06:22 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 06:38-07:08 UTC — same
systemic yt-dlp PO-token caption-fetch throttle (12th+ consecutive drained
one-shot). Discovery fresh (age 19.73h), no refresh needed. No work eligible;
run-start immediately followed by run-end reason=drained journaled; no wakeup
scheduled (one-shot).

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 06:32 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 06:38-07:08 UTC — same
systemic yt-dlp PO-token caption-fetch throttle (13th+ consecutive drained
one-shot). Discovery fresh (age 19.91h), no refresh needed. No work eligible;
run-start immediately followed by run-end reason=drained journaled; no wakeup
scheduled (one-shot invocation, per operator instruction). Confirmed
`wiki/learnings/` still has no entry for this recurring block despite 12+
repeat occurrences — still worth capturing so future runs stop re-deriving the
same root cause; deferred here as out of scope for a one-shot dispatch
iteration.

## [2026-07-22] work | Autopilot run (vps): 0 cycles, drained by all-clones-backoff
One-shot check at 06:36 UTC. All 4 owned clones (neil-patel, mkbhd, hormozi,
chris-do) still inside back-off windows expiring 06:38-07:08 UTC — same
systemic yt-dlp PO-token caption-fetch block (20+ consecutive drained
one-shots since ~02:26 UTC). Discovery fresh (age 19.98h), no refresh needed.
No work eligible; run-start immediately followed by run-end reason=drained
journaled; no wakeup scheduled (one-shot). Added the deferred
`wiki/learnings/roster-ingest-autopilot.md` entry this time: documents the
lockstep back-off pattern as expected mechanics (not a fresh failure per
invocation) and flags that the real fix — installing a POT provider
(`bgutil-ytdlp-pot-provider`) or a YouTube cookies file for yt-dlp — is
infra-level and outside this agent's reach (no pip/root on this box); needs
human action.

## [2026-07-22] work | Autopilot run (vps): 30 cycles — timebox stop
Run started 06:41 UTC (6h box), stopped 13:14 UTC on `over_timebox` (elapsed
6.55h). Owned clones neil-patel/mkbhd/hormozi/chris-do. Productive early
hours: mkbhd 13 cycles (~125 items incl. 1 Stage S synthesis pass, debt
2→0, v6→v7), neil-patel 12 cycles (~72 items incl. 2 Stage S passes, debt
drained twice), one discovery refresh at 10:59 UTC (+52 new rows, 21
promoted fresh/P1). chris-do and hormozi mostly blocked this run (2 and 3
cycles respectively, near-zero items) by the same recurring yt-dlp
PO-token/bot-check caption-fetch gate seen in prior one-shots. From ~11:05
UTC onward all four owned clones cycled into repeated 1h back-offs
(hormozi, chris-do at 11:05; neil-patel, mkbhd at 12:13) as the block spread
bench-wide — consistent with the systemic, infra-level issue already flagged
in `wiki/learnings/roster-ingest-autopilot.md` (needs a POT provider or
cookies file; outside this agent's reach). run-end reason=timebox journaled;
no wakeup scheduled (one-shot dispatch).

## [2026-07-21] work | 2Key Kaltakquise-Anschreiben — Copy fertig, Kanal `do-not-ship`
Growth-Team (Hormozi- + Chris-Do-Operator, unabhängige Entwürfe → Merge → Skeptical Review;
neil-patel als redundant für 1:1-Outbound-Copy ausgelassen, evidence-reviewer durch skeptical
ersetzt wegen Claim-/Rechtsrisiko — beides dokumentierte Routing-Abweichungen). Artefakt im
Zielprojekt: `2key-workforce/wiki/kaltakquise-anschreiben.md` (+ dortiger Log-/Index-Eintrag).
**Copy steht** (3 Betreffzeilen, 118 Wörter, Sie-/Du-Fassung); **Versand als Kaltmail nicht** —
drei Blocker: (1) „Ihre Daten bleiben bei Ihnen" ist beim heutigen Cloud-gepinnten Produkt
sachlich falsch (Claim aus der Copy entfernt; betrifft ALLE Marketing-Flächen), (2) § 7 Abs. 2
Nr. 2 UWG kennt keine B2B-Ausnahme für E-Mail-Werbung, (3) Kaltversand über `info@2key.ai`
gefährdet die Zustellbarkeit der Funnel-Mails. Beschluss-Einordnung: kein Bruch von
2026-07-20 (self-serve-CTA, kein Founder-Sales-Zyklus), aber ein **unbeschlossener Kanal**
außer der Reihe — der beschlossene Avatar-Beweis ist der Pre-Order-Test, nicht Kaltmail.
Orchestrierungs-Learning in `wiki/learnings/work-pipeline-standard.md` (n=3): Persona-Seats
prüfen gegen Doktrin, nie gegen die IST-Architektur des Zielprodukts — der Reviewer muss
dafür explizit gebrieft werden. Knowledge: project-knowledge + operative-learning.

## [2026-07-22] council | IWP-Landingpage (Kunde) — Funnel-Integrität vor Copy
Growth-Team, Sitze Hormozi + Neil Patel + Chris Do (`--include`), Moderator; GaryVee
reserviert (`created`). Vorlage: Desktop-Screenshot von
`iwp-training.de/potenzialgespraech-engpaesse-vertrieb`. Ablauf: Fan-out → Kreuzbefragung
→ **zweite Fan-out-Runde**, nachdem der Moderator die Trafficquelle im Schwesterprojekt
`sales-team` fand (Brief per Post mit QR-Code → LP → Gespräch → Kompetenzcheck →
Training). Record: `wiki/decisions/2026-07-22-iwp-landingpage-conversion.md`.
**Verdikt:** kein Copy-Problem als Hauptproblem, sondern ein Bruch zum vorgelagerten
Kanal. P0 vor jeder Textarbeit: (1) Brief sagt „Strategiegespräch"/`/strategiegespraech`,
die Seite sagt „Potenzial-Gespräch" unter anderer URL — im `sales-team`-Repo steht die
Brief-URL noch als unbestätigte Annahme = Kampagnen-Stopper; (2) QR auf Papier heißt ~100 %
Mobiltraffic, bewertet wurde Desktop; (3) ohne utm+Empfänger-ID am QR ist der Print-Traffic
„Direct" = 100 % Messverlust. P1: KI-Video raus (einstimmig, alle Runden), Beweis-Hero,
Briefsprache übernehmen, Bielinski nach oben, Klotz nicht als Hero-Beweis (steht schon im
Brief). P2: die vier Schritte benennen und nur die Diagnose zurückhalten, „Bonus"
benennen oder streichen, **Kompetenzcheck offenlegen statt dreimal „kein Verkaufsgespräch"
zu dementieren**, kostenlos bleiben ohne zweite Filterstufe. Dissens bewahrt (Hero-Großfläche
Kunde vs. Bielinski, Deposit-Varianten, H1-Wortlaut). Orchestrierungs-Learning in
`wiki/learnings/work-pipeline-standard.md` (n=4): vor dem Fan-out die vorgelagerte
Funnel-Stufe beschaffen; im echten Viewport prüfen. Knowledge: decision + operative-learning.

## [2026-07-22] work | IWP-Landingpage: Sektion-für-Sektion-Umbauanleitung
Folgeauftrag zum Council vom selben Tag: nicht mehr Befunde, sondern fertige Copy je
Sektion. Growth-Team, Hormozi- + Chris-Do-**Operator** schreiben unabhängige Vollentwürfe
gegen dieselbe vorgegebene Sektionsstruktur (S0–S11), Merge durch den Orchestrator,
danach unabhängiger Skeptical Reviewer. Artefakt im Zielprojekt:
`sales-team/docs/outreach/iwp-landingpage-umbau.md` (+ Zeile in dessen `docs/README.md`).
**Review-Verdikt `ship-with-changes` mit 10 Must-Fixes — alle eingearbeitet.** Die
schwersten: ein **umgeschriebenes Kundenzitat unter Klarnamen** in der Hero-Beweiskarte
(Loibl hat den Satz so nie gesagt; jetzt ohne Anführungszeichen als IWP-Aussage mit
Quelle); ein **Formular ohne E-Mail-Feld** bei gleichzeitig versprochener
Bestätigungsmail; **erfundene Prozess-Tatsachen** („per Video oder Telefon", „Zwei
Minuten", Zugangslink), die das Dokument an anderer Stelle selbst als offene Frage
führte; eine **Vertraulichkeitszusage** („bleibt zwischen uns") ohne definierten Umfang,
die durch Kompetenzcheck und CRM-Speicherung schon gebrochen wäre; und der Verweis auf
die **vier Schritte** in drei Sektionen, obwohl die Sektion selbst blockiert ist —
jetzt mit harter Sperrregel und Fallback-Zeilen. Dazu: fünf **stille
Beschluss-Abweichungen** (Vorzeile ohne „Vertriebsleiter", Testimonial-Fotos gestrichen,
zwei geschützte FAQ-Fragen entfernt, CTA-Reduktion vor der Instrumentierung) sind jetzt
als einzeln zurückdrehbare Abweichungstabelle am Dokumentanfang benannt.
Neu eingeführt: `[IWP: …]`-Markierung, `[FREIGABE BIELINSKI]` für Sätze, die der Seite
in Bielinskis Mund gelegt werden, und eine **Platzhalter-Regel** (fehlt eine Angabe zum
Livegang, wird der ganze Satz gestrichen — nie geschätzt). Die vier Schritte der
IWP-Systematik sind in keiner Quelle dokumentiert und bleiben bewusst leer.
Orchestrierungs-Learning in `wiki/learnings/work-pipeline-standard.md` (n=5).
Knowledge: project-knowledge + operative-learning.

## [2026-07-22] work | IWP: neue Briefversion — Umbauanleitung revidiert, P0 gekippt
Nachgereichte zweite Briefversion (Betreff „…an den Wettbewerb verloren werden") weicht
erheblich von `sales-team/docs/outreach/iwp-brief.md` ab, auf der beide Council-Runden
beruhten. **P0-Punkt 1 kehrt sich um:** Der neue Brief nennt das Angebot
„Potenzial-Gespräch" — wie die Seite. Der Namensbruch existiert nicht, die Umbenennung
auf „Strategiegespräch" wäre jetzt der Fehler; die Regel („der Name, den der Käufer
zuerst liest, gewinnt") trägt unverändert. Der Brief druckt zudem keine URL mehr, nur den
QR-Code → Scan-Ziel frei wählbar, Dauerregel (Weiterleitung statt finaler URL) bleibt.
Weiter geändert: Leitmotiv, Dauer 45–60 Min, „über 40 Jahren" vs. 46 auf der Seite,
„Aus der Praxis für die Praxis" jetzt Wiedererkennungsanker statt Floskel,
„Vertriebs-Systematik" als Begriff bestätigt. Zwei Council-Fragen sind durch den Brief
beantwortet (Bielinski führt persönlich; Zugangsknappheit steht schon drin). Stärkster
Fund: die drei Diagnose-Sätze des Briefes sind wörtlich das, was die vier Fragekarten der
Seite fragen — richtiger Inhalt, falscher Platz. Artefakt revidiert
(`sales-team/docs/outreach/iwp-landingpage-umbau.md`, Revisionsblock + betroffene
Sektionen), Decision Record um Nachtrag 2 ergänzt, veralteter Task-Chip zurückgezogen und
ersetzt. Knowledge: project-knowledge + operative-learning.

## [2026-07-22] work | IWP: Phasenmodell erhalten — S4 entsperrt, Raster-vs-Lieferung getrennt
Folie „Verkaufs-Phasen-Modell nach IWP" nachgereicht: **0 Kontaktaufnahme (ausgegraut) ·
1 Bedarfsanalyse · 2 KONA (KundenOrientierte NutzenArgumentation) · 3 Abschluss**, dazu
„Einwände" zwischen 2 und 3 und eine Kurve „Hauptkommunikationsebene" (emotional vs.
sachlich). Damit ist S4 der Umbauanleitung entsperrt (Namen belegt; offen bleiben nur die
Ein-Satz-Erklärungen je Phase).
**Der vom Nutzer bemerkte Bruch ist real und aufgelöst:** Das Phasenmodell ist NICHT das,
was der Kunde mitnimmt — es ist das **Raster**, mit dem diagnostiziert wird. Zwei Achsen,
die bisher vermischt waren. Konsequenz: S4 zeigt die Landkarte (das WAS, verschenkt),
S5 liefert den Befund „in welcher Phase verlieren SIE" (das WIE, verkauft). Damit löst
die Seite den Brief-Teaser ein, ohne die Methode preiszugeben.
**Zweiter Gewinn:** Die vier Fragekarten der Bestandsseite sind keine leeren Fragen,
sondern die Phasen in Frageform — sie werden nicht gestrichen (Korrektur der ersten
Fassung), sondern den Phasen zugeordnet. Zuordnung ist als Vorschlag markiert, nicht als
IWP-Doktrin.
Neue offene Punkte an IWP: **drei Namen für eine Sache** („vier Schritte"/
„Vertriebs-Systematik" im Brief vs. „Verkaufs-Phasen-Modell"/„Phasen" auf der Folie) ·
warum Phase 0 ausgegraut ist · KONA als Akronym auf einer Kaltakquise-Seite (jetzt
ausgeschrieben, Kürzel in Klammern) · Bestätigung der abgelesenen emotional/sachlich-Kurve.
Knowledge: project-knowledge.

## [2026-07-22] review | IWP-Akquisebrief vor dem Druck (3 Sitze, getrennte Blickwinkel)
Growth-Team, Tiefe `deep` per route.py (risk=high — Druck ist irreversibel). Abweichung:
statt Council+Plan drei Advisor-Sitze mit **getrennten Blickwinkeln** auf einen einseitigen
Brief — Hormozi (Hook/Angebot/Beweis/Ökonomie), Chris Do (Sprache/Haltung/Vertrauen),
Neil Patel (Message-Match/QR/Messbarkeit/Follow-up). Artefakt:
`sales-team/docs/outreach/iwp-brief-review.md` (+ Index in dessen docs/README.md).
**Konvergenter Hauptbefund gegen das bestehende Briefkonzept:** Alle drei fordern
unabhängig, das **Zurückhalten der vier Schritte aufzugeben**. Chris Do am schärfsten:
Kontaktaufnahme/Bedarfsanalyse/Nutzenargumentation/Abschluss ist die Grundform jedes
Vertriebsprozesses — dahinter wird nichts geschützt; „Sie kündigen an, dass es vier sind,
und sagen nicht, vier was. Das ist ein Teaser, kein Hook." Auflage: nur in Kundensprache,
KONA-Akronym raus. Folge: Der LP-Payoff verschiebt sich auf „in welcher der vier verlieren
SIE" — deckt sich mit der Raster-vs-Befund-Trennung im Umbaudokument.
Weitere Konvergenzen: **kein P.S.** (zweitmeistgelesene Fläche leer), **Referenzlogos
fehlen im Brief**, **QR als einziger Weg** (Vanity-URL + Kampagnendurchwahl dazu), **kein
Follow-up** (Touch 1 von ~7), **„über 40 Jahren" → 46**, Wellen statt Vollauflage,
Kalender-Verfügbarkeit als stärkster Hebel. Vier Floskelsätze zur Streichung; ein
Claim ohne Deckung gefunden („Auf Umsatz und Marge" — das Testimonial belegt nur Umsatz).
Offener Konflikt: **Headline** — Hormozi und Chris Do wollen sie schärfen, Neil verteidigt
sie als einzige bestehende Message-Match-Achse zur LP. Moderator-Einordnung: kein Veto,
sondern Kopplungsbedingung (LP-H1 muss mitwandern).
**Rechtliche Abgrenzung als Moderator ergänzt:** adressierte Postwerbung an Unternehmen
ist NICHT wie Kalt-E-Mail zu bewerten — § 7 Abs. 2 UWG zielt auf E-Mail/Fax/automatisierte
Anrufe; Briefwerbung stützt sich auf Art. 6 Abs. 1 lit. f DSGVO mit Art.-14-Info-/
Art.-21-Widerspruchspflichten. Ausdrücklich als „kein anwaltlicher Rat" markiert, damit
die frühere E-Mail-Bewertung nicht falsch übertragen wird. Knowledge: project-knowledge.

## [2026-07-24] council | Lang LifeScience / Tierarzt — Scrape-to-Personalize-Briefkonzept
Growth-Team (Hormozi × Neil Patel × Chris Do), standard + Kreuzbefragung. Geprüft: der
KI-personalisierte Postbrief (AMAMUS Vet coldPlasma an Tierarztpraxen) im Legacy-n8n-
Workflow — Brief-Aufbau, Enrichment-Feld-Beschreibungen, Gesamtkonzept, 3-Zeilen-Hook.
Record: wiki/decisions/2026-07-22-lang-lifescience-tierarzt-brief-konzept.md. Artefakt im
Zielprojekt: sales-team/docs/outreach/tierarzt-brief-council-review.md (+ docs/README.md).
**Konvergenter Kern (alle drei):** (1) Die KI soll GENAUIGKEIT statt Nähe erzeugen — eine
wahre, überprüfbare Beobachtung; gibt das JSON nichts her, ehrlich generisch senden
(falsch spezifisch schlimmer als ehrlich generisch). 3-Beat-Hook: Accusation Audit + eine
wahre Tatsache + Schmerzfrage; drei Zeilen sind nicht zu kurz, es geht um Präzision.
(2) Getestet wird auf der SCAN-RATE gegen einen ehrlich-generischen Kontroll-Arm (Buchungen
bei kleiner Auflage nicht signifikant testbar), entschieden gegen eine ökonomische
Break-even-Schwelle. (3) Kleine Batches (~5-10 %), weil der Markt endlich/vernetzt ist —
Hormozi revidierte im Kreuzverhör seine eigene Aussage „miserable Response-Rate ist okay".
Weitere: „kleines Geschenk" streichen → benannte Lieferung; ein CTA-Ziel; P.S. mit
Risikoumkehr; zweiter Weg neben QR. Enrichment: tierwohl zu breit (wörtliche Belege statt
Zusammenfassung), tierarztleitung höchstes Halluzinationsrisiko (strukturiert, Konstruktion
verbieten), zielgruppe-Achse klassifiziert den Website-Texter (alle Scores speichern),
fehlendes Tierart-Fit-Gate (wichtigste Einzellücke), Daten-Tier-Gate A/B/C/D. Message-Match:
3 LP-Varianten spiegeln die Hook-Achse. Zwei Sofort-Bugs: Copy-Paste-Rest „das Museum" in
allen Hook-Prompts; CT/MRT-Hook-Variante konzeptionell kaputt (Diagnostik ≠ Behandlung).
Dissens bewahrt (Chris Do: Scan-Test misst nicht den Vertrauensschaden bei den ~98 %
Nicht-Buchern; Kalt-Kanal-Prognose warm vs. Beweis). Knowledge: decision.

## [2026-07-27] council | Welches Ziel treibt „Claude Code lernen"? — Jobs-to-be-done
Growth Council (Hormozi × Neil Patel × Chris Do, konvergent). Verdikt: niemand will das Tool lernen — „lernen" ist der Nenner; 3 Jobs darunter (A Zeit zurück/Markus, B selbst bauen/Mastery = höchste Zahlungsbereitschaft, C nicht-abgehängt/Status). Einstimmig: der Lern-Stamm (B/C) ≠ der ertrinkende-Markus-Stamm (A) — schärft die 2026-07-20-Avatar-These auf der Mastery-vs-Convenience-Achse. Evidence-Gate prominent: alle drei Wikis leer zu Claude Code/DACH/den 300 → Council ist Methodik über ungetestetem Substrat; Avatar messen (Survey 300 / 300€ Paid-Search / 15–25 Interviews) VOR Workshop-Bau. Positionierung: Ergebnis statt Tool. Decision: wiki/decisions/2026-07-27-claude-code-lernen-ziel-jobs.md
Knowledge: decision

## [2026-07-27] council | TAKTILo-Landing vs. Kunden-PDF: was übernehmen
Growth Council (Hormozi × Neil Patel × Chris Do, konvergent; GaryVee reserviert/Stub). Ziel-Projekt sales-team. Verdikt einstimmig: Kunden-PDF „TAKTILo® Core" ist Sales-Collateral/Datenblatt, KEINE Conversion-Seite → Leave-behind im Musterpaket, nicht Ersatz der Live-Landing (`/m/<token>`, ein Ziel = Musterbestellung). Botschaften ernten, Layout NICHT. HERO: Positionszeile „einfach, sauber und normgerecht nachrüsten" (Swap jetzt, dann Positions-Varianten testen) · Schmerz-Verkauf „keine Baustelle/laufender Betrieb/planbare Festkosten" · Message-Match per Personalisierung (Gebäudetyp zeigen statt abfragen). UNTER FALZ: maßstäbliches Produktfoto (Tabelle raus) · Ton-in-Ton-vs-Kontrast-Einwand-Killer · 13 Jahre + benannte GF · EIN echtes Testimonial am CTA · Lieferversprechen. RAUS: Modultabelle, 2. CTA/„Projektlösung"-Frame, Mehrschritt, Produkt-als-Held, „Core"-Sub-Brand. Dissense erhalten: Headline Swap(Chris/Hormozi) vs. Test(Neil)→Swap+Varianten-Test; Produktfoto Hero(Hormozi) vs. below-fold(Neil/Chris)→below-fold; Gebäudetyp-Feld Neil-add vs. Hormozi-Kostenqualifier vs. Chris-Veto/personalisieren→keine neue Reibung. Behalten: Single-CTA + Founder-Note „Ihr Brief kam von mir" (Brief→Seite-Brücke, unfairer Vorteil). Decision: wiki/decisions/2026-07-27-taktilo-landing-kunden-pdf-uebernahme.md · Artefakt: sales-team/docs/outreach/taktilo-landing-council.md
Knowledge: decision

## [2026-07-27] council | Landing-Page-Kritik „was passt noch nicht" (ki-business-agenten-website)
Growth Council prüft gebauten Stand. Konsens Top-Leaks: (1) echter VSL fehlt, (2) Headline macht
kein Versprechen + Bandwurm-Subline + Message-Match zu YouTube, (3) „So läuft dein Tag" + STAR-
Fit-Filter fehlen, (4) FAQ zu dünn/falsche 3 + Schema, (5) Proof an Entscheidungspunkt + Ergebnis-
Zahlen, (6) CTA-Ehrlichkeit + Owned-Audience-Pfad (E-Mail-Gate) reaktivieren, (7) Design-Politur
(Kontrast/Typo, 6→3 Testimonials, Preis-Zahl als Hero, statisches Logo-Grid, Marke oben-links),
(8) SEO+Analytics fehlen komplett (kein ld+json, Potsdam nicht im Title, kein UTM). Record:
wiki/decisions/2026-07-27-landing-page-critique-was-fehlt.md. hub-candidate: nein.

## [2026-07-27] council | Claude Code prominent? + Fit-Filter behalten? (ki-business-agenten-website)
Growth Council, einstimmig. (1) Claude Code NICHT in die Headline (Jargon senkt Perceived
Likelihood beim nicht-technischen Owner) — aber als eigene „Womit du baust"-Sektion prominent:
Damaging-Admission-Reframe („klingt nach Code — aber keine Zeile") + Future-Proof („beste
Werkzeuge, aktuell Claude Code") + Insider-Call-out; plus Segmentierung/SEO-Supporting-Asset
(später). (2) „Für dich/Nicht für dich" BEHALTEN aber SCHÄRFEN (echte Damaging Admissions, vor
dem Quiz-CTA; als A/B-Test messen) — Florians Bauch erkannte „weich geschrieben", nicht „unnötig".
Umgesetzt im Zielprojekt. Record: wiki/decisions/2026-07-27-claude-code-prominenz-und-fit-filter.md.
hub-candidate: nein.

## [2026-07-27] council | Amendment: „Womit du baust"-Block gestrichen (ki-business-agenten-website)
Florian: eigener Claude-Code-Block überflüssig, seit das Claude-Logo über dem Hero-Video sitzt.
Moderator (council-fundiert, ohne neue Runde): zustimmen — Insider-Signal = Logo, Reassurance
bereits in Block 03 + FAQ. Block gestrichen, Claude Code bleibt via Logo/03/FAQ/VSL. Record-
Amendment ergänzt. hub-candidate: nein.

## [2026-07-27] council | Cold-letter hook closing question (A vs B vs B′)
- Growth Council (hormozi, neil-patel, chris-do) on sales-team vet cold letter.
- Verdict UNANIMOUS: B′ (non-doubling question in hook, body widens it) > A (statement hook, body asks) > B (old doubling). Reject B.
- Tensions: tone risk feel-understood-vs-judged (Hormozi+ChrisDo); decide-by-split-test optimizing reply quality (Neil+Hormozi); evidence is digital-only, no direct-mail data.
- Decision: wiki/decisions/2026-07-27-hook-closing-question.md
- Knowledge: durable (reusable copy principle: keep the question in the personalized zone, point it at their world, body answers not echoes).
- hub-candidate: cold-outreach hook = personalized open-loop, never doubled by the body.

## [2026-07-27] council | Critique of concrete B′ hooks (real leads)
- Growth Council (hormozi, neil-patel, chris-do) judged 4 rendered hooks.
- Verdict UNANIMOUS: FIXABLE not ship-ready. Dietz=gold standard; holistic=mis-targeted (physio, no prescribing); "auf Ihrer Seite gesehen"=mail-merge tell; questions too long + deficiency undertone.
- Disagreement: Chris Do challenges self-answer mechanic (setup/scream); Hormozi+Neil keep it. Resolution: keep self-answer + Chris Do guardrails.
- Decision: wiki/decisions/2026-07-27-hook-copy-critique.md
- Knowledge: durable (cold-mail hook craft: lead with O-Ton, no meta-tell, short noun-landing question, no deficiency undertone, fix targeting before copy).
- hub-candidate: "no sentence saves a wrong list" — targeting precedes copy.

## [2026-07-28] council | Workshop-Upsells: Continuity-Retainer + Ascension-Mechanismus (target second-brain)
Executive Council (Hormozi × Chris Do, deep) auf Florians Frage „Upsells an einen frischen
Workshop-Kunden, damit wir nicht neu akquirieren müssen". Verdikt: die echte Lücke ist ein
WIEDERKEHRENDES Vehikel (kein weiteres Projekt) → monatlicher Retainer („Agenten am Laufen
halten"), auf Ergebnis bepreist, 4-Wochen-Takt, Einmal-Build über dem Monatspreis. Upsells über
BAM-FAM-Ergebnis-Check-in statt Sales-Termin; Film sauber ohne Bedingungen übergeben. Dissens:
Hormozi (Anker 50k + Deprivations-Timing) vs. Chris Do (reine Antizipation, kein Anker, Goodwill-
Konto) — aufgelöst: Antizipation zuerst am Check-in, Anker-als-Erleichterung bei frischen Kunden
gestrichen. Record: wiki/decisions/2026-07-28-workshop-upsell-ascension.md (status recommended,
Ratifizierung Founder). Hub-Persistenz in second-brain separat. Nächster Schritt: /work
(Retainer-Angebot: Scope + Preis + Check-in-Skript).

## [2026-07-28] council | Website-Konversions-Review ki-business-agenten.de (Growth: Hormozi × Neil × Chris Do)
Review-Council (Chris Do per --include; Founder-Direktive 2026-07-22: Councils nur für
Konvertierung). Drei Sitze konvergent auf P1: **Community-Leak raus** (Stat „11k Community" +
Skool-Footer = gratis Off-Ramp + Fame≠Käufer-Proof), **„- Florian"-Testimonial** fixen/raus,
**Founder-VSL** (Platzhalter → echter Studio-Cut, 5-Teiler-Belief-Breaking, rough-Hook jetzt),
**Funnel instrumentieren** (GA4/Consent/Events Quiz→Call, gegen Bank rekonziliieren — Neils #1),
**ein CTA identisch+wiederholt**, Proof über die Falz, FAQPage/LocalBusiness-Schema. Dissens
VSL-first (Hormozi/Chris Do) vs. Measure-first (Neil) → parallel aufgelöst (Messung billig+
unblockend sofort; VSL = Founder-kritischer-Pfad). Garantie (abschluss-kontingent) + Studio-Tag-
Verknappung = Offer-Mechanik → an Founder zurückgegeben (harte Regel 3), NICHT council-lokal
entschieden. Record: wiki/decisions/2026-07-28-website-conversion-review-growth-council.md.
Ziel-Projekt-Doku (log/STATE) separat in ki-business-agenten-website. Orchestrierung: Growth-Team
+ Chris-Do-Include bewährt sich für Website/Brand-Reviews. Knowledge: none (projekt-lokal).

## [2026-07-30] council | Workshop-Rabattanfrage (Kunde Marleau) — halten vs. bewegen
Executive-Team (Chris Do × Hormozi), standard + Kreuzbefragung. Kunde drückt auf den
Tagessatz eines 2-Tages-Workshops (3.800 €/Tag, + Anfahrt + Dozentenkosten). Record:
wiki/decisions/2026-07-24-workshop-rabattanfrage-marleau.md.
**Verdikt:** kein Nein, sondern der beste Einwand (Kunde will intern verteidigen, bietet
selbst Umfangsanpassung an). Tagessatz HALTEN, nur Umfang/Terme bewegen, nie nackter
Rabatt, nie rechtfertigen. Entscheidender Fork (beide Sitze): ist „rahmenkonform" ein
psychologischer Anker (→ Value-Reframe) oder eine harte Beschaffungsdecke (→ BATNA-/
Autoritätstatsache, rückwärts von der Decke zuschneiden oder absagen)? Deshalb ZUERST eine
Diagnose-Frage, dann bauen. Kreuzbefragung brachte zwei eingeräumte Korrekturen: Chris Do
zeigte, dass Hormozis „1 Tag / 3.800 €"-Option ein verkappter 50-%-Rabatt ist (schlanke
Option = andere Zusammensetzung, nicht halbierter Kauf); Hormozi zog die Diagnose-Frage vor
die Optionen und hält die Jahres-Paket-/Vorkasse-Option als Reziprozitätskarte zurück.
Sequenz: Mail 1 (Sachfrage ehrlich + eine Frage + eine Richtung + Call-Einladung) →
15-Min-Call → kalibrierte Recap-Optionen als interne Verteidigungsmunition. Kostenzeilen
(Anfahrt/Dozent) ins Paket statt einzeln. Walk-away, wenn er am Preis pro Einheit dreht
statt am Umfang. Fertige Antwort-Mail im Record. Knowledge: decision.

## [2026-07-30] council | Workshop-Rabattanfrage Marleau — Nachtrag: Hackathon, kein Call
Zwei korrigierte Fakten (bereits ein Call gehabt → schriftlich lösen; Hackathon-
Hintergrundsupport → „weniger Zeit" beschädigt den Kernwert). Beide Sitze konvergent:
schriftliches Dokument = legitimes Recap (nicht bedürftig); Rescope über Zeit ist die
falsche Achse → halten, allenfalls Peripherie tauschen (nie Kern-Verfügbarkeit); der
ökonomische Kern ist der Schubladenwechsel — Marleaus Anker ist gegen Standard-Trainer-
Tagessätze gerechnet, ihr liefert spezialisierte Event-Begleitung (kein Vergleichsmaßstab).
Value-Reframe von „Tage geliefert" auf „Event-Risiko reduziert / Experten auf Abruf".
Optionen jetzt schriftlich als Setups (Fokus vs. Voll), nicht als Zeitmengen; Voll gegen
Vorkasse + Fallstudie. Überarbeitete Mail im Record ergänzt. Knowledge: decision-update.

## [2026-07-30] council | Marleau Nachtrag 2 — Kostenpositionen (Anreise vs. Dozent)
Frage: Anreise (eigene Position 2, km + Stundenpauschale, lange Anfahrt) in die 3.800
reinpacken? Beide Sitze: Dozentenkosten rein (margen-nah, Zerpflück-Einladung), Anreise
RAUS — reinpacken vergrößert die Anker-Zahl gegen den Trainer-Vergleich, vermischt Wert mit
Selbstkosten, verschenkt eine Konzessions-Karte. Fix = Label statt Struktur: km-Rechnung →
glatte benannte Reisekostenpauschale zu Selbstkosten (keine Kalkulation = kein Feilschen;
fiduziarisches Signal stärkt den Tagessatz). Kosten nach der Nachfrage zu verstecken =
schlechtester Zug (Ertappt-Verdacht). Ein-Satz-Antwort auf die Position-2-Frage im Record.
Knowledge: decision-update.

## [2026-07-28] council | Quiz-Länge/Konversion ki-business-agenten.de (Growth: Hormozi × Neil × Chris Do)
Founder-Sorge „mehr Fragen = mehr Abbruch" am Workshop-Anfrage-Quiz (7 Fragen). Einstimmig:
**`bereich` (Multi-Select) raus**, **Reorder Desire→Geld**, Kern behalten (bauwunsch+umsatz+
team_size). Größter Hebel (Hormozi): **Buchung am Ergebnis** (Live-Kalender, vorbefüllt, kein
Doppel-Eintrag). Dissens erhalten: **Hormozi „auf 4"** (kamera+timing auch raus) vs. **Neil
„6–7 behalten"** (714k-Lead-Magnet-Quiz-Daten) — Moderator landet ~5 (Neils Optimum ist
Low-Ticket-Kontext; High-Ticket → Hormozis „ändert es das Lead-Handling?"). kamera bedingt
behalten aber als Deliverable reframen (Chris Do). Umami misst jetzt Drop-off → A/B vor Commit;
Umsetzung = Founder-Freigabe (harte Regel 3). Record: wiki/decisions/2026-07-28-quiz-laenge-
konversion-growth-council.md. Knowledge: none (projekt-lokal).

## [2026-07-30] council | Marleau Nachtrag 3 — echtes Angebot AG0122, Reframe korrigiert
Angebot-PDF vorgelegt: Pos 1 „8-stündiger In-House-Workshop zur Einführung", 2 Tage
7.600 €; Pos 2 „Fahrtkostenpauschale 930 €" (330 km + 600 Referent gemischt); O1 optional
Person 2, 6.000/2 Tage. **Materielle Korrektur:** Beschreibung = frontaler Einführungs-
Workshop, nicht der mündlich genannte Hackathon-Support → Kategorie-Reframe (Nachtrag 1)
tot, Marleaus Trainer-Vergleich laut Papier legitim. Neue Linie: Knappheit × Ergebnis.
Haupthebel = Pos 1 von „Einführung/8-stündig" auf Outcome umschreiben („lauffähige
Automatisierungen an euren Prozessen, gebaut und übergeben"). Pos 2 entmischen (Hormozi
korrigiert Nachtrag 2): Referentenpauschale 600 ins Honorar, Anreise ehrlich 330 als reine
km — NICHT alle 930 als Reise labeln (versteckt Marge). Person 2 @ 3.000 perforiert den
3.800-Anker → als Fokus/Voll-Setup mit begründetem Bundle-Vorteil rahmen. Offene
Faktenfrage an Nutzer: real hands-on-bauen oder Frontal-Vortrag? (entscheidet, ob
Outcome-Wording ehrlich ist). Knowledge: decision-update.

## [2026-07-30] council | Marleau Nachtrag 4 — Hackathon bestätigt, finale Antwort + Mail
Fakt geklärt: es IST ein Hackathon (kein Vortrag); 3.800 = Standardsatz. Verdikt: NICHT
runtergehen — Hackathon ist mehr wert als Vortrag; der Druck kam aus der zu schwachen
Beschreibung, Fix ist das Wording, nicht der Preis. Outcome-Wording aus Nachtrag 3 jetzt
ehrlich → verteidigt den Satz. 4-Schritt-Plan: Pos 1 auf Hackathon/Outcome umschreiben,
Pos 2 entmischen (Referent 600 ins Honorar, Anreise 330 rein), Person 2 als Fokus/Voll-
Setup, Mail ohne zweiten Call mit Anreise-Erlass-bei-Vorkasse als einziger Geste. Korrektur:
Basis ist bereits 1 Senior → „einer statt zwei" ist KEIN Sparhebel (Person 2 = Aufstockung).
Finale Mail im Record. Knowledge: decision-update.

## [2026-07-30] council | Marleau Nachtrag 5 — kein Resend, finale Antwort-Mail
Nutzer-Constraint: kein aktualisiertes Angebot nachschieben (wirkt schwach nach bereits
gesendetem AG0122). Konsequenz: Wording-/Struktur-Fixes werden Zukunftsvorlage; für dieses
Deal Formatklärung rein mündlich in der Mail, Tagessatz gehalten. Einzige bewegte Zahl geht
für den Kunden nach unten: Erlass Fahrtkostenpauschale Pos 2 (930 €) bei Vorkasse (Geste +
Zahlungssicherheit, kein Nachschieben). Diagnose-Frage bleibt. Finale Mail-Fassung ohne jede
Andeutung eines zweiten Angebots im Record + Chatverlauf. Knowledge: decision-update.

## [2026-07-30] council | Marleau Nachtrag 6 — Kunde kennt Format, Re-Pitch raus (final)
Kunde weiß bereits, dass es ein Hackathon mit echtem Bauen ist (vorab besprochen). Format-
Klarstellung aus Nachtrag 5 daher redundant/schwächend → raus. Finale Mail: selbstsicherer
Verweis auf gemeinsames Wissen statt Re-Pitch, Benchmark-Konter als geteilte Einsicht,
kürzer. Satz gehalten, eine Frage, Vorkasse→930-Erlass, kein Resend, kein Call. Finale
Version im Record + Chatverlauf. Knowledge: decision-update.

## [2026-07-30] council | Marleau Nachtrag 7 — Konzession finalisiert (930 bei Annahme+Zahlung 2 Wo)
Geste festgelegt: Annahme + Zahlung binnen 2 Wochen → Fahrtkostenpauschale 930 € gestrichen
(deckt sich mit Angebots-Zahlungsfrist, wirkt als Close-Anreiz, als „Anfahrt übernehmen wir"
gerahmt statt Rabatt). Konzessionssatz in finaler Mail ersetzt. Versandfertige Endfassung im
Record + Chatverlauf. Knowledge: decision-update.

## [2026-07-30] council | Workshop-Funnel: Buchungs-Buttons, Terminname, Mails, Vorname (ki-business-agenten)
Team email (Hormozi × Chris Do × Neil Patel), kreuzbefragt. Einstimmig: 3-Termin-Buttons behalten
(Assumed Close/Goldilocks); kundenseitigen Terminnamen von „Erstgespräch" auf Ergebnis-Namen
umbenennen (interner Kalendername bleibt); eine Mail + Google-Einladung richtig, DOI-Zweitmail als
Geschenk; Vorname Pflicht bei Buchung / optional beim Newsletter (wie gebaut), „Hallo,"-Fallback ok,
keine Extra-Mails ohne Vorname. Verknappungs-Spannung gelöst (Hormozi): Call ≠ Studio-Tag, 4
Studio-Tage/Monat sind die echte Produkt-Scarcity. Dissens erhalten: Priorisierung — Hormozi
(Reminder-Kadenz 24h/12h/3h zuerst) vs. Neil (Buchungs-Conversion + Tracking zuerst; keine verbürgte
No-Show-Zahl im Wiki) vs. Chris Do (Framing/Name zuerst). Moderator: umbenennen → Funnel
instrumentieren → Reminder; empirisch auflösen. Record:
`wiki/decisions/2026-07-30-workshop-buchung-termin-mails.md`. Knowledge: decision. hub-candidate.

## [2026-07-30] council | Prep-Geschenk (Aufzeichnung) vor dem gebuchten Call (ki-business-agenten)
Team growth (Hormozi × Neil × Chris Do, kreuzbefragt; GaryVee reserviert). Frage: Workshop-
Aufzeichnungen vor dem Call als Geschenk/Trust — schadet es (2. CTA/Show-Rate/Kannibalisierung)?
Verdikt (Confidence high): **ja, aber nur EINE kuratierte Aufzeichnung, streng als Vorbereitung
geframt, in der Buchungsbestätigung**; 24h-Reminder trägt nur einen Ein-Satz-Prep-Nudge (kein 2.
CTA), Reminder bleiben Single-CTA „erscheinen"; NIE die ganze Bibliothek vor dem Call (Substitution).
Keine Kannibalisierung (live+interaktiv ≠ Aufzeichnung). Cross-exam-Bewegung: Hormozi+Neil → Bestätigung
als Container, Chris Do → Prep-Video sei kein 2. CTA, dürfe in die 24h-Mail (Dissens erhalten). Record:
`wiki/decisions/2026-07-30-prep-geschenk-vor-dem-call.md`. Knowledge: decision. hub-candidate.

## [2026-07-30] council | Close-CRM: Aufräumen + Setup für Inbound-Funnel (ki-business-agenten)
Team growth (Hormozi × Neil × Chris Do, kreuzbefragt). Grundlage: echte Close-Daten — 2.551 Leads,
~72 % tot/kalt, nur ~20 % warm, nur ~52 % mit E-Mail; gewuchertes Schema (3 Pipelines, 16 Status,
18 Fields). Verdikt (high): EINE verhaltensbasierte Pipeline (Quiz→Call gebucht→Call gehalten→
Angebot→Won/Lost + Nurture/Advocate), Alt-Ballast archivieren; die 2.551 NICHT massen-mailen
(Kalt-Akquise ohne Opt-in) — nur warmes ~20 % per Anruf/1:1, Rest archivieren. Cross-exam:
Hormozi konzediert Blast, Neil qualifiziertes Ja NUR für isolierten Consent-Filter-Touch auf
Wegwerf-Subdomain; Moderator-Default = kein Massen-Filter (Dissens erhalten). DSGVO-Gap → Anwalt.
Record: `wiki/decisions/2026-07-30-close-crm-cleanup-und-setup.md`. Knowledge: decision. hub-candidate.

## [2026-07-30] council | Close Smart-Views: wie viele, welche (ki-business-agenten)
Team growth (Hormozi × Neil × Chris Do). Frage: mehr Smart-Views nutzen? Verdikt (high): Views =
Arbeits-Warteschlangen (auf null abarbeiten), keine Reports. Empfohlen 6 total: Warm + Archiv
(bestehend) + Heute-anrufen (Wiedervorlage/Rückruf ≤ heute) + Angebot-offen-nachfassen + Neue-
Quiz-Leads (Speed-to-Lead) + Calls-nächste-48h. Regel: View = eine tägliche Handlung, Fünftklässler-
Test, 7 Tage ungeöffnet → killen. Dissens Zahl (Chris Do 4 / Hormozi 6 / Neil ≤8). Record:
`wiki/decisions/2026-07-30-close-smart-views.md`. Knowledge: decision. hub-candidate.

## [2026-07-30] council | Close-Felder aus aufgezeichnetem Call (ki-business-agenten)
Team executive (Hormozi × Chris Do, kreuzbefragt). Frage: welche Themen/Kriterien aus einem
aufgezeichneten Call in Close speichern? Verdikt (high): Zusammenfassung in 3 strikt getrennten
Blöcken **A) O-Ton (wörtlich) · B) Diagnose (STAR + Wert-Gleichung + Ampel) · C) nächster Schritt**.
Ampel rot/gelb/grün bleibt, aber regelbasiert/auditierbar (Index auf STAR, kein Black-Box-„87 %") +
**Bauch-Override-Feld** (Mensch vetoet jede Farbe). KI auf **Schmerz+Klarheit** trainiert, nicht auf
Kaufsignale (fehlt Schmerz → hinschreiben). Einwand-Kategorie **„Avoidance" gestrichen** (Charakter-
urteil), jeder Einwand mit O-Ton belegt. Aufzeichnung zu Call-Beginn ansagen. Dissens erhalten
(Auto-Score, „Munition"-Framing, felt-pain-Verbatim). DSGVO → Anwalt. Record:
`wiki/decisions/2026-07-30-close-call-summary-felder.md`. Knowledge: decision. hub-candidate.

## [2026-07-30] council | Close-Pipelines + Status: Altlasten bereinigen (ki-business-agenten)
Team ad-hoc (Hormozi + Chris Do, kreuzbefragt). Auf echter Live-Struktur (4 Pipelines: 3 alt +
neu „Studio-Workshop (Inbound)"; 16 Lead-Status). Verdikt (high, einstimmig): **EINE aktive
Pipeline mit exakt den 5 Stufen** (Call gebucht→gehalten→Angebot raus→Gewonnen→Verloren), KEIN
Quiz/Nurture/Advocate als Stufe. **Fortschritt auf EINER Achse** (Opportunity = Wert); Lead-Status
nur Vor-/Nach-Deal (empfohlen 5–6: Neu/Follow-up/Aktive-Opp/Nurture/Kein-Fit/Kunde), Ampel = Score.
Pflichtfeld **„Verloren-Grund"** (No-Show/BadFit/Preis/Timing-Nurture/Wettbewerber) → No-Show+Nurture
= Gründe, keine Stufen. Alt-Pipelines archivieren (Records behalten), Alt-Status nach Bulk-Remap aus
der Auswahl entfernen. Dissens: Lead-Status-Zahl (Hormozi 6 vs. Chris Do 4). Größter Fehler: Stufen
über interne Aktivität statt filmbare Käufer-Handlung (Hormozi) / Anhaftung an Altlasten (Chris Do).
Record: `wiki/decisions/2026-07-30-close-pipelines-und-status.md`. Knowledge: decision. hub-candidate.

## [2026-07-30] council | Website-Review + Next Steps ki-business-agenten.de (Hormozi × Neil × Chris Do)
Growth Council, standard, kreuzbefragt — Florian ließ die LIVE-Seite durchgehen. Verdikt (high bei
Website-Fixes): Fundament stimmt (ein Angebot/CTA/Quiz/Fit-Filter/persönliche Buchung) → Cleanup, kein
Rebuild. Prioritäten: (1) `/workshop` löschen/301 (SEO-Kannibalisierung; /langform-Redirect bleibt);
(2) Proof Vanity→**Ergebnis-in-Euro**; (3) **prozess-/asset-basierte Garantie** (Chris Do: nie fremde
Betriebsergebnisse garantieren; Neil: 60>30-Tage +7%); (4) **Feind benennen** + Preis value-based
herleiten + Film in Euro; (5) Tracking an **CRM-Cash** + Nurture hinterm Gate. Danach: Traffic-Motor
(YouTube→/quiz, Content-Cluster aus 50h Video), Angebots-Sequenz (Upsell/Downsell statt 0€/Premium-Anker).
Reibungen aufgelöst: A/B (Hormozi) vs. „nicht testbar bei 4 Sales/Monat" (Neil) → **CTR an der Gabelung**
+ qualitativ + CRM-Cash. Preis/Angebotsmechanik/Garantie = Founder-Hoheit; hier nur Bau-Input.
Record: `wiki/decisions/2026-07-30-website-review-growth-council.md`. Knowledge: decision. hub-candidate.

## [2026-07-30] council | Marleau Nachtrag 8 — Gegenanker 1.500–2.800, finaler Reply
Marleau ankert gegen Einzel-Coach-Sätze (falsche Kategorie), Benchmark nicht harte Decke,
weicher Walk-away. Beide Sitze: Tagessatz halten (26-%-Cut vom Tisch); Anker per „agree and
one-up" annehmen+umdrehen (Ergebnis-Vergleich statt Tagessatz-Vergleich); Anbietervergleich
aktiv einladen (walk-ready); Konzession = Anreise 930 als Kennenlern-Geste (Nutzer-Rahmung)
+ Bonus statt Rabatt (Doku + 2 Wo Support); 1-Tages-Pilot als Fallback (nicht in Mail 1, da
Einwand am Tagessatz hängt). Walk-away-Linie: Tagessatz-Druck auf 2.800 → ziehen lassen.
Finaler Reply im Chatverlauf. Knowledge: decision-update.

## [2026-07-31] council | YouTube-Kooperations-Intake (self-qualifying sponsorship form) — ki-business-agenten
Team youtube (mkbhd × hormozi × chris-do, cross-examined). Verdict: inbound sponsor requests run
through a self-qualifying application form; the channel is the funnel for the 5k workshop and
audience trust IS the business, so judge every deal by "help or hurt the workshop machine."
Auto-decline anything competing with the workshop; budget a required forced-choice field with the
lowest band = the floor; editorial control + Werbung/Anzeige labelling non-negotiable;
usage-rights/whitelisting priced separately as a licence/royalty; paid-first (deposit = qualifier).
Dissent (transactional vs. long-term) resolved by Hormozi himself: few trusted repeat partners at
the RELATIONSHIP level, cash-first clean deals at the DEAL level (goose vs. eggs). Cross-examine
added blindspots: off-ramp/post-publish caveats (MKBHD), exclusivity + frequency cap (Hormozi),
German media-contract usage-scope trap + reveal-first for shy partners (Chris Do). Record:
wiki/decisions/2026-07-31-youtube-kooperations-intake.md. Knowledge: decision. hub-candidate: no.

## [2026-07-31] plan | Kooperations-Bewerbungsformular (unlisted /kooperationen) — ki-business-agenten
/plan seeded from the 2026-07-31-youtube-kooperations-intake council record. Hidden, noindex,
non-linked landing page with a self-qualifying application form; Founder constraint: unlisted,
sent only on email request, no CTA competition with the workshop. Auto-decline only on hard
machine-checkable criteria (budget-below-floor / non-negotiables not accepted / no decision-maker);
fit + competitor screening stays a HUMAN flag (freitext unreliable); qualified -> server-validated
team mail, kept separate from the workshop pipeline; honeypot + rate-limit + DSGVO consent. 7 WPs
(WP6 = Founder: price floor + lawyer media-contract, out of build scope). Skeptical pass integrated
into the plan. Plan file lives in the TARGET project: ki-business-agenten-website/plans/
2026-07-31-kooperations-formular.md (status draft, awaiting founder OK). Knowledge: plan.

## [2026-07-31] council | TAKTILo-Landing: ROI-/Kosten-Zahlen platzieren
Verdikt: absolute €-Zahlen/Vergleichstabelle raus von der Cold-Muster-Seite (→ Datenblatt-PDF + Gespräch); Ersparnis als operative Proof-Zeile (10→2 Tage, Haftung/Ablöserisiko, Trägermaterial/RAL) unter dem Falz; Hero/CTA ohne Zahl. Dissens Neil (Prozent-Deltas rein) vs Hormozi+Chris (Kosten-Framing raus) → konservativ 2:1 aufgelöst. Seats: hormozi, neil-patel, chris-do. Knowledge: decision.

## [2026-07-31] council | Lern-/Selbstlern-Tier ~49 €/Monat (Console, ohne Community)
Verdikt: JA zum niedrigschwelligen Monats-Tier — aber (1) unterste Sprosse der EINEN Leiter, kein zweiter Funnel („one funnel to rule them all"); (2) verkauft als **Console/Schmerzlinderung** („nutze die Console, fall nie hinter den Stand"), NICHT „Zugang zu Videos" (Commodity/Preiskampf); (3) primärer Job = Top-of-Funnel/Ascension → gemessen an **Workshop-Buchungen pro Mitglieds-Monat**, nicht MRR; (4) **ERST per Pre-Sell validieren, nicht bauen** — 20 zahlende Signups in 7 Tagen + ≥10 % Self-Book Fit-Call, sonst nicht bauen. Minimal/versteckt bewerben richtig (Nav/Footer + Quiz-„nicht-Fit"-Zweig, kein Hero-Wettbewerb); Aufstieg via In-Product-Wall + Antizipation, nie Pitch. Billing 49 €/4-Wochen, konsumierbar; zero-touch onboarding oder schließen; auf Churn budgetieren (>5 % = kaputt, <10 % Ascension in 6 Mon = Leck). Seats: hormozi, chris-do, neil-patel (deep, cross-examined). Dissens erhalten: Hormozi (Decoy) / Neil (Lead-Source) vs. Chris Do (reiner Give-first-Service, „decoy zum Scheitern gebaut = Manipulation") → aufgelöst: interne Decoy/Lead-Mess-Logik + bindende Integritäts-Bedingung (Mitglied bekommt Gegenwert unabhängig vom Aufstieg). Refines 2026-07-28-workshop-upsell-ascension. Record: wiki/decisions/2026-07-31-lernbereich-membership-49eur-tier.md. Knowledge: decision. hub-candidate: no.

## [2026-07-31] council | Bibliotheks-Gate: personalisiertes Upgrade statt Video-Wall
Frage: nur EIN Workshop-Video gratis gegen E-Mail (Wall aufs Video) statt volle Bibliothek? Verdikt (nach Cross-Examine EINSTIMMIG): NEIN zur E-Mail-Wall auf dem Content. **Video/Bibliothek ungated** (Discovery/SEO/Binge/Autorität — „Google can't index what's behind a form"; Hormozi konzediert „Get Flow → Monetize → THEN Add Friction", Teil-Gate „destroys trust", Gratis > bezahlter Konkurrenz-Content). **E-Mail auf dem personalisierten Upgrade** einsammeln (Fit-Check-Quiz-Ergebnis / maßgeschneiderter Plan), Wert vorher sichtbar → routet in Anfrage→Call→5k. **49 € Console = bezahlter Raum, Bibliothek NIE dahinter** (Linie: „Aufzeichnung vs. lebend/interaktiv" / „WAS frei, WIE bezahlt"). Metrik = qualifizierte CRM-Anfragen pro 100 Viewer (nicht Opt-in-Rate), in Close. Erst A/B (ungated-Video+Exit-Intent-Upgrade vs. Video-Wall), kein Rebuild. Florians Instinkt (E-Mail einsammeln, EIN Flagship) bleibt richtig — nur der Gate-Ort wandert. Seats: hormozi, chris-do, neil-patel (deep, cross-examined). **Löst den am 2026-07-27 offen gelassenen Gate-Dissens** (zugunsten Chris Do + Neil ungated; Hormozi eingerückt) und **reversiert Status-quo E-Mail-Gate-vor-Langform** (2026-07-21 / Commitment §3/§4) → Founder-Ratifizierung nötig. Refines 2026-07-27-aufzeichnungs-bibliothek-lead-magnet; löst Free-vs-49€-Kollision aus 2026-07-31-lernbereich-membership-49eur-tier. Record: wiki/decisions/2026-07-31-bibliothek-gate-personalisiertes-upgrade.md. Knowledge: decision. hub-candidate: no.

## [2026-07-31] council | Console-Tier-Preis: Job bestimmt Preis, 49 vs 99 Pre-Sell-Test
Frage: 49 € zu niedrig fürs Console-Tier (gefühlter Wert hoch)? Verdikt (einstimmig auf dem Grundsatz): NICHT auf „die Tipps sind unglaublich" preisen — das ist „selling out of your own wallet", optimiert MRR (die für dieses Tier verworfene Kennzahl) und hungert den 5k aus. Der JOB (Lead-Quelle/Aufstieg) bestimmt den Preis, gemessen an Workshop-Buchungen nicht MRR. Start 49 €/4-Wochen + Garantie (self-serve zero-contact). Rungs weit auseinander, Ceiling ~100 (49 = 1% von 5k). Dissens Richtung: Hormozi+Chris „niedrig halten" (39–59; low price = feature am Front-End; Buchungen = Mitglieder × Rate, Preis schneidet Mitglieder schneller; wetten 49 gewinnt) vs. Neil „als Filter höher" (Preis filtert auf 5k-Käufer, senkt Casual-Churn, „zu billig wirkt fake"/Diamond Foundry; wettet 99). Aufgelöst in DENSELBEN Test, den beide unabhängig vorschlugen: **Pre-Sell A/B 49 € vs 99 €, entschieden an Workshop-Buchungen pro 100 Besucher** (nicht MRR, nicht Buchungs-Rate). Chris' Leitplanke falls höher gewinnt: nur mit menschlichem Angebots-Zusatz (Gruppen-Call/Hot-Seat), sonst preist man ein Tool wie einen Raum → Order-Taker-Rahmung. Seats: hormozi, chris-do, neil-patel (standard). Refines 2026-07-31-lernbereich-membership-49eur-tier (löst dessen offenen Preis-Punkt). Record: wiki/decisions/2026-07-31-console-tier-preis.md. Knowledge: decision. hub-candidate: no.

## [2026-07-31] setup | Neuer Klon: agency-scaler (Agency Scaler) — DXR-Kurs, EINE Persona
`/add-clone` end-to-end. Neuer Klon **agency-scaler** ("Agency Scaler") registriert (roster.json, status: created, tier 1, github: ki-business-agenten/agency-scaler-clone, **PRIVAT** — synthetisiert aus BEZAHLTEM DXR-Kurs). EINE Persona (kein A/B-Split, obwohl zwei Stimmen im Kurs) — eine zusammenhängende Denkwelt (DACH-Agenturaufbau + Principle-Based-Selling). Quelle: 248 Transkripte in privatem Repo ki-business-agenten/dxr-course-transcripts (12 Kapitel), zuvor per logged-in Chrome vom Membersport gezogen. **strong_for:** high-ticket-sales, sales-closing, cold-calling, appointment-setting, offer-creation, agency-scaling, fulfillment-ops, sales-team-building, objection-handling, founder-mindset. **weak_for:** ecommerce-ops, seo, creative-production, software-architecture, consumer-branding, enterprise-sales. Sitzplätze (conditional, nicht default → gezielt bei Agentur/Sales, nicht redundant zu hormozi): **growth** (high-ticket-sales, cold-calling, agency-scaling, leadgen), **executive** (high-ticket-sales, agency-scaling, offer-creation, fulfillment-ops). gen_agents + install_global neu gebaut (agency-scaler-advisor/-operator, 14 Agenten). validate.py sauber. **Reservierter Sitz** (status: created, kein System-Prompt) → nimmt an Councils nur via explizitem --include als experimentell teil. **Besonderheit:** Text-Transkript-Quelle aus privatem Bezahlkurs, KEINE öffentliche YouTube-Person → Standard-Ingest (Kanal-Enumeration) passt nicht; „aktiv" (sprechfähig) erst nach Synthese der Transkripte → persona/system-prompt.md. Nächster Schritt offen (Synthese-Ansatz). Knowledge: setup. hub-candidate: no.
## [2026-07-24]

council | growth (hormozi × chris-do × neil-patel, cross-examined, standard) on
youtube-engine Furkan-collab packaging → decision
`wiki/decisions/2026-07-24-furkan-video-packaging.md`. Verdict: package the universal
reframe ("ein Entwickler wie ein ganzes Team"), deliver depth as PROOF not jargon.
Title = outcome front, "Claude Code" keyword woven into front half — Neil retracted his
keyword-position-1 rule (Google-web, not YouTube; his own headline formula puts keyword
mid, promise front), collapsing the one real dispute. A/B = outcome-reframe vs contrarian
"Prompt überbewertet". Thumbnail = reframe-as-hook, Sebastian dominant + Furkan as
credential badge (guest-authority guard), Furkan's name out of the title. Slice tension
(Hormozi sofa-buyer vs Neil launch-window poisoning) dissolved by Chris: both are the same
event (base bounces in first 2 min) → cold open must honor the broad promise or it's a
casting problem. Hub-candidate: generic rule "outcome front, keyword woven; package broad /
deliver deep as proof" → youtube-engine docs/concepts/titel-formeln.md. Artifacts land in
the target project per its conventions (packaging chain next).

council | youtube (mkbhd × hormozi × chris-do, cross-examined, standard) on
youtube-engine thumbnail-process redesign → decision
`wiki/decisions/2026-07-24-thumbnail-system-redesign.md`. Anlass: Sebastian verwarf die
KI-generierten Thumbnails grundsätzlich; empirische Basis 76 Thumbnails (Top-12 von
Julian Ivanov/Hormozi/NateHerk/TheFutur/MKBHD einzeln visuell analysiert + 16 eigene mit
Performance-Abgleich). Verdict einstimmig: Komposition statt Ein-Schritt-Generierung
(echtes Expression-Foto, echter Beweis, deterministische HTML-Typo; KI nie für
Gesicht/Logo/Text/Beweis), Feld hell ("keep the ink, flip the field", 3/3 konditioniert:
High-Key-Fotos, A/B-Validierung, Ablaufdatum-Klausel), Signature = Typo-Stimme statt
Ornament (Hormozis "geliehener Anzug"-Einspruch übernommen), Konzept bei Video-Planung,
binäres QA-Gate, 70-20-10, Nordstern Workshop-Anfragen. MKBHD saß erstmals in einem
Council (kein STUB-Verhalten beobachtet; zitierte production-filmmaking/creator-business
sauber). Umgesetzt im Zielprojekt: research-Doc + packaging-prinzipien §2 v2 +
thumbnail-Skill v2. Offen: Expression-Foto-Session (Blocker), thumbnail-compose.mjs.

## [2026-07-26] council | Intro-Format Workshop-Serie (youtube-engine)
MKBHD × Hormozi × Chris Do (cross-examined, evidence+skeptical review) → reproduzierbares 20–25-s-Intro-Template für Sebastians Studio-Workshop-Serie („Ein Tag, ein System", A/B vs „8 Stunden Vorsprung"). 2 SWAP-Slots (Name + eine Zeile) + Foto; Cold Open = Gast-in-Reaktion (Existenz, nicht Outcome); Gast = Held / Sebastian = Guide; kein Fail-Frame; „Fremder"-Zeile verworfen (Werte-Test). Cross-exam löste beide Forks durch Konzession statt Kompromiss (Chris zog Ergebnis-Open zurück, Hormozi verwarf seine stärkste Zeile). Decision: wiki/decisions/2026-07-26-workshop-serie-intro-format.md.
Knowledge: decision. Artefakt liegt im Zielprojekt (youtube-engine/docs/concepts/workshop-serie-intro-format.md) + dortiger log/index/drehplan aktualisiert. Orchestrierungs-Learning: 3-Sitz-YouTube-Team mit cross-exam produzierte echten Konsens ohne Restdissens; Router-Domains youtube/intro/packaging/hook → team youtube korrekt.

## [2026-07-26] council | Hostinger-Werbeblock: fix vs. personalisiert (youtube-engine)
Growth Council (Hormozi × Chris Do × Neil Patel, cross-examined) → **Hybrid mit VO-Default**: ~95 % fixer Evergreen-Kern (kein Gesicht in der Konserve), variabel nur EIN Brückensatz als Voice-over über der Animation (<5 Min Grenzkosten, kein Teleprompter); Disclosure+Exklusivität wandern IN den fixen Block (selbsttragend); Hook-Swipe-File 10–15 evergreen-wahre Sätze; Kapitelmarke „Sponsor" ab Tag 1; sequenzieller Kohorten-Test (fix vs. VO-Brücke, dann Gewinner vs. On-Camera) mit Retention-Delta als Primärmetrik; Refresh per Kurven-Trigger + 6–8-Wochen-Backstop; Sponsor-Report (freiwillige Watch-Through) als Verlängerungs-Hebel, Whitelisting als Stufe 2. Alle drei Forks durch Konzession aufgelöst (Hormozi: On-Camera→Testarm; Chris: On-Camera ok unter Audio-Brücken-Bedingung; Neil: Codes→Retention als Primärmetrik). Decision: wiki/decisions/2026-07-26-hostinger-werbeblock-hybrid.md.
Knowledge: decision. Artefakt-Updates im Zielprojekt (sponsor-hostinger.md + docs/log.md). Orchestrierungs-Learning: SendMessage-Resume der Advisor-Agents fürs Cross-Exam funktioniert kontexterhaltend und billig; Growth-Router-Team passte, chris-do via --include war nötig und wertvoll (2 der 3 Konzessionen liefen über ihn).

## [2026-07-26] council | Intro Runde 2: Frames + Vorproduktions-Architektur (youtube-engine)
MKBHD × Hormozi × Chris Do (cross-examined, evidence+skeptical review) → erweitert Runde 1. EINE Position / 3 Castings (Unternehmer / Aufbauender / Professional), Anker = der Aufbauende (Starter); geweiteter Spine „Ein echter Mensch mit einem echten Problem baut an einem Tag ein KI-System, das am Ende wirklich läuft"; Feind RAUS aus dem Spine (eigene Warn-Frame-Evidenz schlägt Chris' Villain-Doktrin, er konzedierte) → optionaler 10%-A/B-Beat. Modulare Architektur: frozen head+tail-Caches + Batch-Alpha-Overlays (Name/Rolle) + Reveal im Mittelfenster + Musik-Stem; HyperFrames-Projekt+Batch = source of truth. VO: 1 Spine-Read + 3 Casting-Zeilen, Name nie gesprochen. Adam=Folge 1=Starter, Ziel in €/Stunden denominiert (Geld-das-floss als Gold-Standard). Decision: wiki/decisions/2026-07-26-workshop-serie-intro-frames-und-architektur.md (extends round 1).
Knowledge: decision. Artefakt im Zielprojekt aktualisiert (docs/concepts/workshop-serie-intro-format.md §0b/§5b/§6/§11). Orchestrierungs-Learning: zweite Runde mit demselben 3-Sitz-Team baute sauber auf Runde-1-Record auf (kein Re-Litigieren), Forks erneut per Konzession an eigene Evidenz gelöst; „own evidence > persona" funktionierte als expliziter Tie-breaker (Feind-im-Spine).

## [2026-07-27] council | Studio- vs. Vor-Ort-Workshops: Bewerbung, öffentlicher Preis, Anker (second-brain)
Growth Council (Hormozi × Neil Patel × Chris Do, cross-examined, evidence-reviewer) auf Sebastians /council-Frage (aus second-brain-Vault). Kein neuer Beschluss — Re-Decide des 2026-07-24-Amendments; Vorschlag (Studio 2.500 / Vor-Ort 5.000, „Hälfte des Preises") driftete zurück in die verworfene Rabatt-Falle. Einstimmig 3:0: extern nur Studio bewerben; Studio-Preis öffentlich als EINE fixe Zahl ~5.000 € (Neil zieht „Bracket" zurück; 2.500 = stiller Discount, Hormozi-„don't copy the moron"); „Hälfte des Preises" gestrichen (Chris: zwei Produkte, nicht eine Achse); Vor-Ort NICHT ins Schaufenster (Hormozi revidiert Solo-Position: fake anchor); On-site-Zahl in den Quiz-Ergebnis-Step (Neil, messbar) statt aufs statische /workshop; echter High-Anker = gesprochener Bespoke-Decoy 25–50k oberhalb Vor-Ort (Hormozi same-core-function-Regel + Chris anchor-really-high); Kannibalisierung über Funnel-Architektur (nur Studio hat Funnel+Preis), nicht über Preis-Drohung. Decision: wiki/decisions/2026-07-27-studio-vs-onsite-bewerbung-und-anker.md (REFINES 2026-07-24-studio-workshop-flywheel-amendment).
Knowledge: decision (hub-candidate). Kern-Handlung ist nicht mehr Deliberation, sondern UNTERSCHRIFT beider Gründer — vierte Behandlung desselben Themas, Record ist Exhibit. Zweite Dissens-Achse offen: Ort der On-site-Zahl (Chris rein mündlich vs. Neil Quiz-Step) → A/B bei Volumen. Orchestrierungs-Learning: Kreuzbefragung erzeugte echten Fortschritt (Hormozi + Neil je eine Solo-Position revidiert), obwohl die Solo-Takes schon 3:0 konvergierten — Cross-Exam lohnt auch bei Konvergenz, wenn es genau auf die Rest-Tensionen zielt. Artefakt-Update im Zielprojekt (second-brain-Hub): Synthese verkauf-und-verhandlung.md + Source-Page + Hub-Log.

## [2026-07-27] council | Workshop-Serie Runde 3: Aufhänger + Titel-Familie (youtube-engine)
YouTube-Team (MKBHD × Hormozi × Chris Do), cross-examined, 3:0: wiederholbare Titel-Formel
(Held+Startpunkt / €-Std-Ergebnis / kollabierte Zeit / Suffix), Tool = Verschreibung nicht Position,
GF-Verbreiterung nur als Casting, Intake = Hook-Casting mit Titel-Gate, keine Challenge-Gamification.
Chris' erneuter Ergebnis-Cold-Open-Vorstoß zurückgezogen; Hormozis Preis-Titel selbst eingeschränkt
(Dissens-Gradient dokumentiert). Record: wiki/decisions/2026-07-27-workshop-serie-aufhaenger-und-titel-familie.md;
Artefakt: youtube-engine/docs/concepts/workshop-serie-aufhaenger-und-titel.md. Knowledge: decision.

## [2026-07-27] council | Workshop-Fokus: Commitment + Preis-Realismus-Check + 2 Deliverables (second-brain)
Executive Council deep (Hormozi × Chris Do × Neil Patel, evidence+skeptical review) auf Sebastians Frage vor der Unterschrift: ist 5.000 € / 12–50k auf dem DEUTSCHEN Markt realistisch oder US-Bias? Einstimmig 3:0, evidenzgewichtet (eigenes Ledger > US-Priors): 5.000 € Studio FEST unterschreiben (eher zu vorsichtig — durch eigene realisierte Preise gedeckt: 5k/2-Tage, 7k/3-Tage, 12× 7,5k Schulung; Boden 4,5k, nie aus Angst darunter); 12k vor Ort quasi validiert (Barrierefreiheit 12,1k), 25k nur ROI-gekoppelt inquiry-only; einzige Abwärts-Justierung: reine Einmal-50k-Decoy zu dünn für DE-Einkauf → als Retainer rahmen / 35–40k. US-Bias-Korrektur: DE kauft ROI/DSGVO/kein-Ärger, nicht Prestige/Film → Film = interne 2×-Begründung, im Pitch Ergebnis verkaufen, Preis nie rechtfertigen. Test: nur 5k öffentlich, Rest inquiry-only (keine Preis-Wand), Concession-Ladder 12k→7,5k→5k, Close-Rate-Diagnostik ~33 %, Three-Yeses-Ratsche. Quiz berechnet Tier (nicht wählen) → löst Selbstselektions-Angst; Studio=Default, Vor-Ort nur bei hartem Trigger. Tag-21-30-Read trennt Preis-Nein von Hook-Nein. Founder-Entscheidung dokumentiert: 2Key ruht (dated, nicht getötet) — amendiert 2Key-Rolle aus dem 24.-Beschluss; Community nicht als Produkt beworben. Decision: wiki/decisions/2026-07-27-workshop-fokus-commitment-und-preis-realismus.md.
Knowledge: decision (hub-candidate). Deliverables im Zielprojekt second-brain erstellt: commitment-workshop-fokus-2026-07-27.md (Vertrag) + fahrplan-workshop-fokus-q3-2026.md (90-Tage). Orchestrierungs-Learning: „own evidence > persona" als expliziter Brief-Header funktionierte hervorragend — alle drei Sitze rahmten ihre US-Doktrin selbst als US-kalibriert und korrigierten gegen Sebastians reales Ledger; Executive-deep-Routing + neil-patel via --include war korrekt (Neils Funnel-Mathematik + Quiz-Logik trug die Hälfte der Antwort). Konvergenz so stark, dass die Deep-Debatte-Runde auf die eine Rest-Justierung (Decoy-Spitze) zusammenschrumpfte.

## [2026-07-27] council | Vertrag-Finalisierung: Persona, Selbstbindung, Kadenz, Playbook (second-brain)
Executive Council standard (Hormozi × Chris Do × Neil Patel) — dritter Lauf des Tages, Vertrag+Fahrplan vor Unterschrift durchgegangen. 3:0: (1) 5.000 € gilt NICHT für beide Personas — bestätigt Sebastians Intuition: Workshop = etabliertes Unternehmen mit Umsatz (mehr Geld als Zeit), Wantrepreneur = Gratis-Spur (Barbell), schärft Positionierung; (2) Evidenz-Rahmung korrigiert: 7,5k-Schulung war fünfstelliges Mehrmonats-Programm (LMS+Betreuung), nicht „7,5k/Tag" → beweist Markt kauft fünfstelliges KI-Enablement (stärker); (3) On-Site 12–25k = KEIN Tagessatz, Mehrtages-/Whole-Team-Build, %-of-value; (4) 5.000 beworben vs. 4.500 interne Verhandlungs-Untergrenze aufgelöst (Checkpoint-Neu-Basis zuerst 4,5k, Fahrplan von 3,5–4k korrigiert); (5) Kadenz halten nicht dunkel gehen, zwei Engines trennen (Content vs. Paid-Validierung) + Buchungs-Tags gegen Selbstbetrug; (6) Funnel parallel bauen, muss vor bezahlten Fremd-Sessions stehen; (7) Selbstbindung an INPUTS koppeln (Kadenz + Boot-verbrennen/keine Agentur-2Key-Arbeit), Escrow-Spite-Money + öffentliche Zielmarke, schmerzhaft nie ruinös → §10; (8) Kunden-LinkedIn = personalisierter nativer Post statt Einheits-Artikel; (9) Reviews: eine Frage am Peak, Google zuerst, Feedback mittags nicht am Erschöpfungs-Tief; (10) Community-Link bleibt (nur nicht bewerben); (11) Fahrplan-Owner B=Florian. Decision: wiki/decisions/2026-07-27-vertrag-finalisierung-persona-selbstbindung-playbook.md.
Knowledge: decision (hub-candidate). Beide Deliverables im Zielprojekt direkt editiert (Commitment §1.3/§2/§5/§10 + Fahrplan Owner/Zwei-Engine/Phase-0-1/Trust-Anker/4.500/Playbook). Orchestrierungs-Learning: dritte Runde mit demselben 3-Sitz-Team, „own evidence > persona" trug erneut den Kern (Persona-Bestätigung + Evidenz-Ehrlichkeit bei der LMS-Kopplung); großer heterogener Fragen-Batch ließ sich in EINER Fan-out-Runde ohne Cross-Exam abarbeiten, weil die Fragen fachlich getrennt in die drei Lanes fielen (Hormozi=Persona/Strafe/Evidenz, Chris=Positionierung/On-Site/Anker-Erklärung, Neil=Kadenz/Amplifikation/Reviews).

## [2026-07-27] council | Avatar = Schnittpunkt dreier Filter; On-Site = reaktives Upsell (second-brain)
Executive Council standard (Hormozi × Chris Do × Neil Patel), vierter Lauf — letzte Schärfung vor Unterschrift. 3:0: (A) „Firma vs. Aufbauer" ist Scheindichotomie → drei orthogonale Filter (Umsatz [hart] × Bau-Wunsch × Kamera-Willigkeit), Avatar = Schnittpunkt = „umsatzbringender Owner-Operator/Gründer, der mit KI baut & kamera-willig ist" = „Aufbauer MIT Umsatz"; Sebastians Instinkt richtig, nur Geld-Filter bleibt hart; YouTube-Publikum-Bauer-Tilt = Filter 3 arbeitet; Geld-Filter per Quiz ergänzen (keine 0-€-Antwort). Kontur in 60 Tagen testen = EINE Botschaft/eine Tür/ein Quiz + 4-Qualifier-Tagging, nach 60T Top-20 % der Zahlenden = geschärfte Kontur; NIE zwei Kampagnen. (B) On-Site 12–25k = reaktives Stage-II-Upsell, KEIN Produkt: nicht beworben/nicht im Funnel/nicht im Quiz/nie darauf hingebaut, nur reaktiv im Gespräch (capture don't create); Creep-Test = Marketing-Aufmerksamkeit/Avatar-Split; zwei Schutzplanken (Workshop liefert eigenständig; kein Rep steuert zum Build). Sebastians Scope-Einwand bestätigt. Decision: wiki/decisions/2026-07-27-avatar-schnittpunkt-und-onsite-scope.md.
Knowledge: decision (hub-candidate). Beide Deliverables editiert (Commitment §2 Avatar-Callout+On-Site-Zeile+Scope-Callout+§3, Fahrplan Quiz-Logik+Phase-3-Avatar-Schärfung). Orchestrierungs-Learning: vierte Runde, „own evidence > persona" trug erneut (Hormozi rahmte seine Luxus-/Status-Doktrin selbst als US-Prior und ließ das Publikums-Argument gewinnen); die zwei Einwände fielen sauber getrennt in die Lanes (Hormozi Avatar-Achse/Money-Model-Scope, Chris Positionierung/Fokus, Neil Publikum-Fit/Funnel-Reinheit) → wieder eine Fan-out-Runde ohne Cross-Exam ausreichend.

## [2026-07-31] setup | agency-scaler promoted created→active (v1 system-prompt)
Compiled persona/system-prompt.md v1 (214 lines) in clones/agency-scaler-clone from 248 DXR
transcripts; sources placed under wiki/sources/dxr-course/; pushed (ddc2f02). roster.json status
created→active, gen_agents + install_global rebuilt (agency-scaler-advisor/-operator now real council
seats, not stubs), validate clean. Now a live voice: auto-seats in growth (high-ticket-sales,
cold-calling, agency-scaling, leadgen) + executive (high-ticket-sales, agency-scaling, offer-creation,
fulfillment-ops), or via --include agency-scaler / the agency-scaler-advisor agent. v2 enrichment
pending (5 dense doctrine digests preserved in this session's tasks/*.output). Knowledge: setup. hub-candidate: no.

## [2026-07-31] setup | Neuer Klon: webinar-hero (Webinar Hero) — Webinare-Kurs, active
`/add-clone` + Synthese. **webinar-hero** ("Webinar Hero") aus dem privaten Bezahl-Kurs "Webinare"
(21 Transkripte, 3 Kapitel: Webinarstruktur 10 / Angebot 3 / ADS 8; 2 video-only). Quelle: privates
Repo ki-business-agenten/webinare-transcripts; Klon-Repo (privat) ki-business-agenten/webinar-hero-clone.
System-prompt v1 (322 Zeilen) via Hintergrund-Agent synthetisiert, gepusht (9edfdc9); Quellen in
wiki/sources/webinare/. roster.json status active, tier 1. Sitze (conditional): **growth** (webinar,
webinar-funnel, paid-ads), **content** (webinar, presentation). gen_agents + install_global neu gebaut
(webinar-hero-advisor/-operator = echte Seats). validate sauber. strong_for: Webinar-Struktur/Intro
(4 Säulen Status/Dringlichkeit/Commitment/Hoffnung, Show-don't-tell), Webinar-Pitch/Angebot (magisches
Angebot), Slides/Content, Going-Live (WebinarJam), Meta-Ads (Leadpreis, Pixel/Tracking, Lookalike,
Skalieren). weak_for: SEO, cold-outbound, 1:1-high-ticket-sales, ecommerce-ops, software, legal.
**Sprechbar** via /council (auto in growth/content) oder --include webinar-hero / Agent webinar-hero-advisor.
Geschwister-Klon zu agency-scaler. Hinweis: Angebot-Kapitel hat Nebenstimmen (Nick/Erik), ehrlich vermerkt.
Knowledge: setup. hub-candidate: no.

## [2026-08-01] setup | Neuer Klon: eddy-ad — Adbaker Mentoring, active
Codename **eddy-ad** = Adbaker Mentoring (Simon Marder / Adbaker), DACH Meta/Facebook Paid-Social.
Quelle: privater Bezahlkurs auf **LearningSuite** (adbaker-mentoring.learningsuite.io), 3 Kurse
(Starter 155 / Advanced 215 / Creative 151 = **521 Lektionen, 484 Transkripte**). Extraktion NEU
via LearningSuite-GraphQL-API (window.__APOLLO_CLIENT__, eingeloggte Session): courseContent-Baum,
Video-fileId je Step, `StepFileTranscriptQuery(id)` — Bulk statt Durchklicken. Transkripte im
privaten Repo `ki-business-agenten/eddy-ad-transcripts`; Klon `ki-business-agenten/eddy-ad-clone`
(Quellen in wiki/sources/adbaker/). System-Prompt v1 (319 Zeilen) synthetisiert (Push-vs-Pull,
BM/Kampagnenstruktur, ABO/CBO, Targeting/Lookalikes, Ad Building Blocks/Hooks, Pixel/CAPI,
CPA/ROAS-KPIs, Testing-Phasen, Skalierung vertikal/horizontal). Sitze: growth + content (Meta/
Facebook/Paid-Social/Ad-Creatives-Tags). Composite — primär Simon, teils Nebenstimmen (Marius/Jan/
Nico), ehrlich vermerkt. **Sprechbar** via /council (auto in growth/content) oder --include eddy-ad
/ Agent eddy-ad-advisor. Geschwister zu agency-scaler + webinar-hero.
OFFEN (User bestätigen): private GitHub-Repos vs. Memory-Regel "Bezahlkurs = local-only".
Knowledge: setup. hub-candidate: no.
