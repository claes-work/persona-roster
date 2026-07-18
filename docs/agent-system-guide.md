# Agent system guide — how to use the roster

The practical manual for the persona-roster agent operating system. You state a goal;
the system picks who thinks about it, how deeply, who executes, who reviews, and what
gets remembered. You never manage personas, pipelines, or the wiki by hand.

## 1. What the system is

- **Personas (clones)** — independent repos, one real person each, with a cited wiki
  and a compiled system-prompt. Registered in `roster.json`. The roster is the *bench*.
- **Functional roles** — non-persona control seats (skeptical/evidence/editorial/
  technical reviewer, customer advocate, moderator). Prompts in `orchestrator/roles/`.
- **Teams** — curated, declarative lineups of personas + roles per problem area
  (`teams.json`). A council seats 3–6 non-redundant voices, never the whole bench.
- **Router** — classifies your task and resolves team, seats, reviewers, and depth
  (`orchestrator/router.md` + `tools/route.py`). Automatic by default.
- **Council** — independent takes → cross-examination → neutral synthesis → decision
  record. Councils decide; they don't execute.
- **Executive** — operator agents (persona judgment + full tools) do the real work
  inside real projects.
- **Review** — independent seats check the output; the creators never green-light
  their own work alone.
- **Wiki persistence** — the AI maintains the project memory (`index.md`, `log.md`,
  `STATE.md`, `wiki/decisions/`, `wiki/learnings/`, `plans/`) automatically after every
  relevant workflow. You never have to say "merk dir das".

## 2. Quick start

```text
/council Soll mein Produkt einen kostenlosen Tarif bekommen?
/work    Erstelle 5 Titel und 3 Thumbnail-Konzepte für mein Video über Agent Harnesses.
/plan    Entwickle die neue Claude-Code-Masterclass.
/run-plan plans/2026-07-20-masterclass.md
/review  Prüfe die neue Landingpage in ../website-form.
/wiki    status
```

Ask in any language; the system's files stay English.

### Prerequisites & access rights

| You want to… | You need |
|---|---|
| **Use** the system (councils, /work, all clones) | `git`, Python 3, Claude Code. The clone repos are public on GitHub → cloning needs **no** rights or tokens. |
| **Push ingest/synthesis work** to a clone | Collaborator (write) access on THAT clone repo — the owner adds you. Never run two ingest loops on the same clone from two machines. |
| **Add a new persona** (`/add-clone`) | `gh` CLI authenticated + repo-creation rights on some account. No rights on `claes-work`? Create the clone repo under your OWN account — the per-clone `github` field in roster.json points `clone_all.py` there, so everyone else still gets it automatically. |
| **Change the roster itself** (roster.json, teams.json) | Write access to `persona-roster` — the registry is the single shared source of truth; pushing it is how new personas/teams reach every machine. |

Disk note: the clone repos carry big wikis (Hormozi alone: ~2,000 source pages); the
first `/setup` download takes a while. Raw transcripts are gitignored and not fetched.

### New machine / new collaborator: `/setup`

Clone the repo, open it in Claude Code, run **`/setup`** — that's the whole onboarding.
It pulls the clone repos, generates the machine-local agents, installs the global
commands, validates everything, and shows the readiness report. Idempotent: re-running
detects the existing install and switches to refresh-and-report mode. (Manual
equivalent: `clone_all.py` → `gen_agents.py` → `install_global.py`, see README.)

### Use from any project (the normal case)

You mostly work INSIDE your projects (youtube-engine, client repos, …), not in the
roster. `/setup` (above) installs everything user-globally; to refresh only the global
shims:

```bash
python tools/install_global.py     # from the roster root
```

This installs machine-local shims into `~/.claude/` (same build-artifact philosophy as
`gen_agents.py`): all six commands plus every `<slug>-advisor`/`<slug>-operator` agent
become available in every Claude Code session. Invoked from another project:

- **Artifacts + artifact knowledge** land in the project you're in, following ITS
  conventions (its CLAUDE.md, wiki, docs/log).
- **Decisions and orchestration learnings** land in the roster wiki (the shared brain
  about how councils/teams work).
- Re-run the installer after changing `roster.json`, `teams.json`, or command
  procedures; `--uninstall` removes everything it created. Foreign files in `~/.claude`
  are never touched (marker check).
- If a project defines its own command with the same name (e.g. a local `/review`),
  the project-local one applies there — use the roster from that project via the
  agents (`@hormozi-advisor`) or rename locally.

## 3. Which command when?

| You want… | Use |
|---|---|
| a decision or recommendation | `/council` |
| a finished artifact from a goal | `/work` |
| a bigger, multi-step effort structured first | `/plan` |
| to continue an existing plan | `/run-plan` |
| an independent check of something that exists | `/review` |
| wiki health check / query / manual capture | `/wiki` (maintenance only — normal persistence is automatic) |
| one persona's take, no synthesis | `@<slug>-advisor` (e.g. `@hormozi-advisor`) |
| one persona working in a project | `@<slug>-operator` |

## 4. Public parameters (the only knobs)

Everything else is automatic; these override the router:

- `--team <id>` — force a team: `executive · growth · content · youtube · email ·
  product · engineering · research`. Example: `/work --team email "Betreffzeilen für den Launch"`.
- `--include <slugs>` — add seats: `/council --include garyvee,chris-do "..."`.
- `--exclude <slugs>` — remove seats: `/work --exclude networkchuck "..."`.
- `--depth fast|standard|deep` — force pipeline depth: `/work --depth fast "Beschreibung umformulieren"`.

Default behavior without flags: domain match picks the team, conditional seats join on
matching tags, risk/reversibility picks the depth, only `status: active` clones are
seated (others are reported as reserved).

## 5. Teams

Defined in `teams.json` (edit there; workflows need no change):

| Team | For | Default seats | Conditional |
|---|---|---|---|
| executive | big, hard-to-reverse business decisions | Hormozi, Chris Do | Neil Patel (seo/traffic), GaryVee (attention/brand), MKBHD (product/credibility) |
| growth | marketing, acquisition, funnel, SEO | Hormozi, Neil Patel, GaryVee | Chris Do (positioning/branding) |
| content | content, storytelling, editorial | MKBHD, GaryVee | NetworkChuck (tech-education), Chris Do, Neil Patel |
| youtube | video packaging: title, thumbnail, hook, retention | MKBHD, NetworkChuck, Hormozi | GaryVee, Chris Do, Neil Patel |
| email | newsletters, subject lines, sequences | Hormozi, Chris Do, Neil Patel | GaryVee (attention/storytelling) |
| product | product, UX, features | MKBHD, Hormozi (+ customer advocate) | NetworkChuck, Chris Do |
| engineering | architecture, code, infra, security | (role-driven: technical + skeptical reviewer) | NetworkChuck (infra/networking/homelab) |
| research | evidence gathering & fact-checks | (role-driven: evidence reviewer) | Neil Patel |

Every team has independent review seats. Note: seats belonging to not-yet-ingested
clones are honestly reported as "reserved" (currently speaking: Hormozi, Chris Do) —
see §9 for the maturity levels and the `--include` escape hatch.

## 6. Personas and roles

**Personas** (see `roster.json` for `strong_for` / `weak_for` details): Hormozi
(offers/pricing/scaling — not for architecture or design), Chris Do (positioning/brand
language/value pricing — not for SEO), Neil Patel (SEO/traffic/conversion), MKBHD
(audience perspective/credibility/packaging), GaryVee (attention/distribution/
repurposing), NetworkChuck (tech-education/infrastructure — not a business strategist;
reserve/specialist seat).

**Roles** (`orchestrator/roles/`): skeptical-reviewer (attacks assumptions/risks),
evidence-reviewer (audits claim grounding; enforces "own evidence > persona opinion"),
editorial-reviewer (clarity/structure/tone), technical-reviewer (correctness/
complexity/security), customer-advocate (recipient's experience), moderator (neutral
synthesis + decision record — never a persona).

## 7. How work flows (depths)

Details: `orchestrator/pipelines.md`.

- **fast** — small & reversible: execute → one independent reviewer → knowledge commit.
- **standard** — normal creative/operative work: mini-council (independent takes →
  cross-examine) → decision brief → execute → independent review → revise → commit.
- **deep** — strategic/risky/irreversible: context audit → research → full council with
  structured debate → decision record → plan → staged execution → specialized reviews →
  validation → retrospective.

Council output always separates: verdict, agreements, **attributed disagreements**
(dissent is preserved, never averaged away), per-seat contribution, gaps. No persona
theatre — names appear where attribution matters.

## 8. The automatic wiki (what you never have to do)

The AI reads before working (STATE.md → index → relevant decisions/learnings) and
commits after working (`orchestrator/knowledge-commit.md`). Enforced: a workflow only
counts as done when `python tools/validate.py --done` passes (a dated log entry from
the knowledge commit exists). Trivial tasks legitimately record `Knowledge: none`.

Where things land:

| What | Where |
|---|---|
| Decisions (incl. dissent, rejected alternatives) | `wiki/decisions/YYYY-MM-DD-<slug>.md` |
| Operative learnings, playbooks, own-evidence rules | `wiki/learnings/<topic>.md` |
| Current project state (resume point for new sessions) | `STATE.md` |
| Chronological history | `log.md` (append-only) |
| Navigation | `index.md` |
| Plans | `plans/<id>.md` |

**Own evidence beats persona opinion:** learnings pages track *persona view* vs *own
evidence* vs *effective rule*; councils load effective rules into every seat's brief.

**Project vs global knowledge:** roster knowledge stays here. Insights useful across
projects get flagged `hub-candidate` in the log; the second-brain hub pulls them via
its own sync — nothing is ever written into the hub directly. When operators work in
another project, artifact knowledge goes into THAT project's wiki per its conventions.

Manual maintenance when you want it: `/wiki status`, `/wiki lint`, `/wiki query "..."`,
`/wiki repair`, `/wiki capture <note>`.

## 9. Adding a new persona

Run **`/add-clone <Full Name>`** in the roster repo — it handles the wiring end-to-end:
fit-check against the bench (non-redundant coverage), repo creation from
`persona-clone-template`, registration in `roster.json` (domains + `strong_for`/
`weak_for`), team seating proposal for `teams.json`, agent regeneration + global
install, validation, and the hand-off instructions for ingestion.

The knowledge work then runs in the clone's own repo: `/clone-setup <Full Name>`, then
`/loop /ingest-loop` until the first synthesis pass compiles
`persona/system-prompt.md`. `/setup` (or `tools/roster_status.py`) detects the moment a
clone earns promotion and offers the `active` flip. The tier-2 wishlist (Sinek, Godin,
Abdaal, Newport, …) already sits in `roster.json` under `planned`.

### Clone maturity: who may sit at the table

(Policy: `wiki/decisions/2026-07-18-clone-maturity-policy.md`)

| Build state | Council capability |
|---|---|
| `active` (system-prompt compiled) | Full: default seat + operator authority. Trust grows with synthesis passes — prefer multi-pass clones for deep councils. |
| `bootstrapped` / `created` | **Experimental seat, only if you say `--include <slug>`** — advisory only, answers strictly from its existing wiki dossiers, flagged low-confidence in the synthesis. Never default-seated. |
| `planned` | Name on the wishlist, nothing to convene. |

Check the real build state anytime: `python tools/roster_status.py` (sources ingested,
L2+ count, synthesis passes, prompt version, roster/repo mismatches — this is how
Chris Do's finished v7 prompt was spotted and promoted on 2026-07-18).

## 10. Adding a new team

Add a block to `teams.json`: `domains` (routing vocabulary), `default_members`,
`conditional_members` (tag → slugs), `roles`, `review` (at least one seat that is not a
default member — enforced), optional `stages`, `member_roles`, `default_depth`, `notes`.
Then `python tools/validate.py` and, if routing should prefer it, make sure its domains
don't collide with an existing team's. Test: `python tools/route.py --domains <...>`.
No workflow changes needed.

## 11. End-to-end examples

- **YouTube video** — `/work Plane und verpacke mein Video über Claude Code Agent
  Harnesses.` → youtube team, standard depth: learnings (what performs on YOUR channel)
  brief every seat → mini-council on promise/angle → decision brief → titles,
  thumbnails, hook, structure → skeptical + evidence review → commit (chosen direction
  + discarded angles land in decisions/learnings; later CTR/retention data feeds back
  into the same learnings page).
- **Newsletter** — `/work Erstelle den Launch-Newsletter für die Masterclass.` → email
  team (NOT the YouTube lineup), standard: offer/value (Hormozi seat) + language
  (Chris Do seat when active) → draft → editorial + evidence review → commit.
- **Product decision** — `/council Freemium-Tarif einführen?` → executive council,
  deep: research → independent takes → debate → decision record with dissent +
  review trigger → optional hand-off to `/plan`.
- **Software architecture** — `/work Entwirf das Schema für die Video-Datenbank.` →
  engineering council: role-driven (no marketer seats), technical review, decision
  record for the schema choice.
- **Landing page** — `/review Prüfe ../website-form gegen unsere Positionierung.` →
  reviewer mix: editorial + customer-advocate + evidence; consolidated verdict with
  must-fix list.
- **Research** — `/work Vergleiche die Preismodelle der Top-5-Konkurrenten.` → research
  team: evidence-first, `/brain` + web research, cited report; durable findings →
  learnings.
- **Multi-stage project** — `/plan Masterclass v2` → plan file → `/run-plan` across
  sessions, one work package at a time, plan file is the progress memory.

## 12. Troubleshooting

- **Wrong team picked** → say so + rerun with `--team`; if it recurs, add/adjust the
  team's `domains` in `teams.json` (that vocabulary IS the routing).
- **Too many voices** → `--exclude`, or trim the team's default members. Benchmark:
  3–6 non-redundant seats.
- **Council reads like parallel monologues** → cross-examine was skipped or seats were
  redundant; rerun at `--depth deep` or with a tighter lineup.
- **Knowledge wasn't persisted** → the done-gate was bypassed; run `/wiki capture
  <insight>` now, and check `python tools/validate.py --done` at the end of workflows.
- **Duplicate wiki pages / stale index** → `/wiki lint` then `/wiki repair`.
- **Plan not resumed** → `/run-plan` with the explicit `plans/<id>.md` path; check its
  `status:` (a `blocked` plan says why inside).
- **Persona asserts ungrounded claims** → evidence-reviewer flags them; a seat with no
  wiki coverage must deflect. If it didn't, that's a clone-quality issue — log a gap in
  the clone's `wiki/gaps.md` (persona-QA), not here.
- **Project knowledge marked hub-candidate wrongly** → it stays local anyway (the flag
  is only an offer to the hub's sync); remove the flag in the log entry's follow-up or
  note it in `/wiki lint`.
- **Seats all "reserved"** → the clones aren't ingested yet; that's honest. Ingest them
  (see §9) — the system refuses to fake voices it can't ground.

## 13. Observability

Every routed run reports: pipeline + depth, team, seats and why (route.py rationale),
reserved seats, reviewers, wiki pages read, artifacts changed, review verdicts, and
what was persisted where. If you want to see the raw routing:
`python tools/route.py --domains ... --tags ...`.
