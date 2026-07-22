# Index

Catalog of this repo's knowledge and configuration pages. Updated by the
knowledge-commit procedure whenever pages are added or change meaning.

## Governance & procedures

- [AGENTS.md](AGENTS.md) — operating schema (canonical rules; CLAUDE.md imports it)
- [STATE.md](STATE.md) — project state snapshot for session resume
- [orchestrator/router.md](orchestrator/router.md) — task classification → team/depth routing
- [orchestrator/pipelines.md](orchestrator/pipelines.md) — fast/standard/deep working depths
- [orchestrator/roundtable.md](orchestrator/roundtable.md) — council harness (fan-out → cross-examine → synthesis)
- [orchestrator/composition-modes.md](orchestrator/composition-modes.md) — the menu of convening modes
- [orchestrator/knowledge-commit.md](orchestrator/knowledge-commit.md) — mandatory read-before / commit-after memory procedure

## Roles

- [orchestrator/moderator-prompt.md](orchestrator/moderator-prompt.md) — neutral synthesis + decision record
- [orchestrator/roles/skeptical-reviewer.md](orchestrator/roles/skeptical-reviewer.md) — assumption/risk attack
- [orchestrator/roles/evidence-reviewer.md](orchestrator/roles/evidence-reviewer.md) — claim grounding audit
- [orchestrator/roles/editorial-reviewer.md](orchestrator/roles/editorial-reviewer.md) — clarity/structure/tone review
- [orchestrator/roles/technical-reviewer.md](orchestrator/roles/technical-reviewer.md) — correctness/complexity/security review
- [orchestrator/roles/customer-advocate.md](orchestrator/roles/customer-advocate.md) — recipient's-eye review

## Configuration

- [roster.json](roster.json) — clone registry (the bench)
- [teams.json](teams.json) — teams + functional-role registry
- [wiki.config.json](wiki.config.json) — machine-readable wiki layout pointer
- [autopilot.config.json](autopilot.config.json) — ingest-autopilot parameters (time-box, discovery cadence, focus order)
- [autopilot/](autopilot/README.md) — autopilot operational journal (not wiki content)

## Wiki

- [wiki/decisions/](wiki/decisions/README.md) — decision records (append-only, dissent preserved)
  - [2026-07-18-agent-os-architecture](wiki/decisions/2026-07-18-agent-os-architecture.md) — the agent-OS upgrade decisions
  - [2026-07-18-clone-maturity-policy](wiki/decisions/2026-07-18-clone-maturity-policy.md) — graded council capability per clone build state; experimental seats via --include
  - [2026-07-19-ingest-scheduling-policy](wiki/decisions/2026-07-19-ingest-scheduling-policy.md) — autopilot scheduling: freshness first, focus-until-active, maturity target, time-boxed budget (amended below)
  - [2026-07-19-parallel-ingest-and-workers](wiki/decisions/2026-07-19-parallel-ingest-and-workers.md) — bounded fan-out (max_parallel_clones) + per-machine worker partition (workers.assignments) for two-account load-sharing
  - [2026-07-20-skool-premium-community-exit](wiki/decisions/2026-07-20-skool-premium-community-exit.md) — first real deep council (Hormozi × Chris Do): exit the premium Skool community; 60-day transfer window, else honorable sunset; earn-out-vs-clean-sale fork preserved as dissent
  - [2026-07-20-2key-investor-pitch-deck](wiki/decisions/2026-07-20-2key-investor-pitch-deck.md) — /work standard (Hormozi × Chris Do + dual review): confirmation-deck strategy, MESO options (C at 8%), accusation-audit name slide, vehicle/IP answer mandatory
  - [2026-07-20-2key-deal-struktur](wiki/decisions/2026-07-20-2key-deal-struktur.md) — council round 2: ONE lead scenario (priced 150k/10%) + hidden convertible fallback, option B killed (services never in cap table), valuation stack from market research
  - [2026-07-20-2key-werbebudget-25k](wiki/decisions/2026-07-20-2key-werbebudget-25k.md) — growth council: 25k ads = test budget (Rule of 100), scaling = CFA loop; gate contradiction found (3:1 vs 30d payback) -> annual-prepay founding-member fix; two-stage marketer scorecard; print loaded CAC
  - [2026-07-20-2key-zielgruppe-owner-operator](wiki/decisions/2026-07-20-2key-zielgruppe-owner-operator.md) — deep council: ONE avatar (German owner-operator, buys like consumer/expands like business), no B2B sales motion year 1, pilots productized+investor-separated, pre-order avatar test, trademark gate before prepay
  - [2026-07-22-homepage-focus-and-proof-stack](wiki/decisions/2026-07-22-homepage-focus-and-proof-stack.md) — growth council R3 (unanimous): 2Key demoted from door to honest strip ("earn the masthead"), owner-operator door now routes to /workshop (buyable); proof stack: numbers bar under hero, testimonials at decision point, fact-cases (no invented uplifts), Florian-origin as community proof; old-website testimonial texts + 6 videos recovered mid-round
  - [2026-07-22-website-conversion-blueprints](wiki/decisions/2026-07-22-website-conversion-blueprints.md) — growth council (cross-examined, under founder scope-directive): course sales-page blueprint (one page cold+warm, proof-first, conditional guarantee, workshop-as-anchor only with real number — two-tier withdrawn per F4), trigger-based onboarding (KPI login+lesson-1 ≤7d, upsell at deprivation point post-milestone-2/3), /2key waitlist = typing-cost calculator + honest expectation mail, homepage gate = Ich-Form headline + outcome subline (outcome variant as A/B), quiz as newsletter hook (result before email ask, honest stay-free outcome), new claim line
  - [2026-07-22-website-shop-override-and-funnel-rulings](wiki/decisions/2026-07-22-website-shop-override-and-funnel-rulings.md) — growth council (Hormozi × Chris Do × Neil, cross-examined): Founder-Override CONDITIONALLY ratified — Shopify direct-purchase/YouTube-Shopping channel APPROVED (round-5 "approved-providers" premise refuted; Chris Do reverses his round-5 no-on-site-commerce vote), but self-built Next.js+Supabase+Bunny course-LMS NOT ratified (round-3 wrong-lever upheld unanimously; off-the-shelf delivery, custom only after revenue proof); event mechanic (a) card-on-file via Shopify app else (c) transferable deposit, (d)/(b) rejected; workshop $1k–~$3k self-serve band then qualification step (number = Founders); /2key = lead-magnet, forward-only, value-before-card; build-scope Founder↔Council dissent left open
  - [2026-07-21-2key-pricing-conversion-funnel](wiki/decisions/2026-07-21-2key-pricing-conversion-funnel.md) — executive council: keep prices (raise at agent launch), remove agent phantom from Max, one-click purchase at peak-pain popup, saved-time counter, usage-triggered educate emails, annual only as earned founding offer; dissent preserved (credit expiry, auto-renewal default)
  - [2026-07-21-portfolio-focus-2key](wiki/decisions/2026-07-21-portfolio-focus-2key.md) — deep council (Hormozi × Chris Do × Neil Patel + skeptical review): one business (2Key, 3–5-yr season), YouTube = marketing dept, trainings = capped bridge, sales project freeze/kill, Enno track sequenced behind pre-order test + solvency math; dissent: premium-tier timing, 80/20 outlet, memo-vs-belief (partially superseded by round 2 below)
  - [2026-07-21-operating-business-vs-2key-build](wiki/decisions/2026-07-21-operating-business-vs-2key-build.md) — round 2 with real numbers: creator business OPERATES, 2Key is the only BUILD; YouTube framing retracted (cash engine + trust bank), free Skool 10k + email = 2Key channel gated on week-1 avatar census; paid pre-order tripwire (≥50/30d) restored over inflated trial number; workshops → 2Key sales channel; Hostinger concentration + month-12 exit-thesis gate; signature hard-gated on Florian
  - [2026-07-21-funnel-operational-rulings](wiki/decisions/2026-07-21-funnel-operational-rulings.md) — round 3 (unanimous): pure email list over second community, 9:1 content mix, ONE Claude-Code workshop with 2Key inside + visible menu add-on (bundle/fee-credit killed), website rebuild denied → MVP funnel, offer-hierarchy sequencing (days 1–45 transfer+masterclass, 45–90 pre-order window), free-trial maximization rejected
  - [2026-07-21-2key-free-tier-and-website-consolidation](wiki/decisions/2026-07-21-2key-free-tier-and-website-consolidation.md) — round 4 (unanimous core): 75-credit Starter stays, no card-upfront trial as default (card at the 100% peak-pain popup, charged at desire), card-entry = middle of funnel not end; article/mini-site consolidation onto one domain approved as phased migration (funnel pages first, /artikel + mapped 301s second); card-trial residual role preserved as minor dissent
  - [2026-07-21-website-funnel-structure](wiki/decisions/2026-07-21-website-funnel-structure.md) — round 5 (Chris Do × Neil): no on-site commerce; 5-page site map (claim + two-door gate, /workshop with published price bracket, /2key waitlist, /community carries the courses), 10-step numbered funnel ladder, phase-dependent pinned comment (community default), unique-link measurement + bank reconciliation; fee-credit revival blocked by moderator; course-page fork deferred to phase 2
  - [2026-07-21-promotion-map-email-consent](wiki/decisions/2026-07-21-promotion-map-email-consent.md) — round 6 (unanimous): no-consent bulk email BANNED (brand + deliverability, not just the Abmahnung); consent list = spine, Skool 72h post-email = consent-harvesting bridge; frequency table per surface (1 self-ad segment/video max, courses never direct on YouTube); no backward funnel edges; architecture declared CLOSED — reopens only on falsified tripwire
- [wiki/learnings/](wiki/learnings/README.md) — operative learnings; persona view vs own evidence vs effective rule
  - [work-pipeline-standard](wiki/learnings/work-pipeline-standard.md) — first real /work runs: seat convergence as signal, functional reviewers earn their keep
  - [roster-ingest-autopilot](wiki/learnings/roster-ingest-autopilot.md) — autopilot cadence/batch/budget evidence (usage calibration accumulates here)
- [plans/](plans/README.md) — persistent, resumable plan objects
  - [2026-07-19-roster-ingest-autopilot](plans/2026-07-19-roster-ingest-autopilot.md) — discovery refresh + cross-clone scheduling + roster-level loop + budget guard + cron path

## Docs

- [docs/agent-system-guide.md](docs/agent-system-guide.md) — user manual for the whole system
- [docs/architecture-report.md](docs/architecture-report.md) — 2026-07-18 analysis, Soll-Ist mapping, migration record
- [README.md](README.md) — project overview + setup
