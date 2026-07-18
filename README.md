# Persona Roster — your council of cloned minds

Imagine asking Alex Hormozi, Chris Do, and Marques Brownlee to sit down together and
work through YOUR problem — each answering the way they really think, backed by
receipts from everything they've published. That's this project: a **team of AI
advisors modeled on real people**, each built from their actual books, videos, and
interviews, with every claim traceable to a source.

You ask one question. The right advisors discuss it (they genuinely disagree
sometimes), a neutral moderator sums it up, and the decision is saved so future
sessions remember it. You can also send an advisor to **work inside your projects** —
writing, researching, editing — applying that person's documented judgment.

```
/council Should my product get a free tier?
/work    Create 5 titles and 3 thumbnail concepts for this video.
```

## What you need

- [Claude Code](https://claude.com/claude-code) (the AI does everything through it)
- `git` and Python 3 installed
- **No GitHub account or special access needed just to use it** — the knowledge repos
  are public.

## Get started (one time, ~10 minutes)

```bash
git clone https://github.com/claes-work/persona-roster.git
cd persona-roster
```

Open the folder in Claude Code and type:

```
/setup
```

That's it. `/setup` downloads the persona knowledge bases, wires up all commands and
agents on your machine, checks everything, and tells you exactly who is ready to talk.
(First run downloads a lot — the knowledge bases are big. Safe to re-run anytime: it
refreshes instead of reinstalling.)

## Everyday use — from ANY of your projects

After `/setup`, these work in every Claude Code session on your machine, not just in
this folder:

| You want… | Type |
|---|---|
| a decision or recommendation | `/council <question>` |
| a finished piece of work | `/work <goal>` |
| a big effort broken into steps | `/plan <goal>`, then `/run-plan` |
| an independent check of something | `/review <what>` |
| one specific voice, no committee | `@hormozi-advisor <question>` |

The system automatically picks who should be involved and how deep to go. If you want
control: `--team youtube`, `--include garyvee`, `--exclude networkchuck`,
`--depth fast|standard|deep`. Everything is explained in the
**[full manual → docs/agent-system-guide.md](docs/agent-system-guide.md)**.

Everything important is remembered automatically: decisions (with dissent), lessons
learned, project state. You never have to say "write that down."

## Who's on the bench

| Advisor | Knows about | Status |
|---|---|---|
| **Alex Hormozi** | offers, pricing, sales, scaling | ✅ active (v35, ~1,760 videos + books) |
| **Chris Do** | branding, positioning, pricing creative work | ✅ active (v7, 378 videos, growing) |
| Neil Patel | SEO, digital marketing, content | 🚧 sources cataloged, not ingested |
| Marques Brownlee | tech review, production, creator business | 🚧 sources cataloged, not ingested |
| Gary Vaynerchuk | marketing, brand, attention | 🚧 scaffold only |
| Chuck Keith (NetworkChuck) | IT, networking, homelab | 🚧 scaffold only |

Only ✅ advisors speak in councils by default — a half-built clone would just make
things up, and this system never fakes knowledge. Check the live state anytime with
`python tools/roster_status.py` (or `/setup`, which flags advisors that earned
promotion). Wishlist (planned): Simon Sinek, Seth Godin, Ali Abdaal, Cal Newport,
Derek Muller, Cleo Abram, Linus Sebastian, Jeff Geerling, Theo Browne, Tim Ferriss.

## Add a new persona

In this folder, type:

```
/add-clone <Full Name>
```

It creates the person's own knowledge repository from the
[template](https://github.com/claes-work/persona-clone-template), registers them,
proposes which teams they should sit on, and hands you the one command that starts the
knowledge build (`/clone-setup`, then an autonomous ingest loop — this part takes days,
it's reading their life's work). Until the build compiles, the seat is "reserved":
visible, honest about not being ready, joinable only if you explicitly ask
(`--include`, flagged low-confidence).

When you push the updated `roster.json`, everyone else gets the new persona
automatically on their next `/setup` — the registry is the distribution mechanism.

## How it actually works (the short version)

- **One repo = one person.** Every advisor is its own independent GitHub repository
  with its own cited wiki. They exchange *statements* in a council, never each other's
  knowledge — like real people in a meeting. No merged super-brain, ever.
- **Bench vs council.** The roster may grow forever; a council seats only the 3–6
  voices that actually fit the problem (`teams.json` + an automatic router).
- **Council decides, operators execute, reviewers check** — and at least one reviewer
  was never involved in creating the work.
- **The system keeps its own memory** (`wiki/decisions/`, `wiki/learnings/`,
  `STATE.md`, `log.md`) and learns: your OWN results eventually outrank what the
  personas recommend.
- Deep dives: [docs/agent-system-guide.md](docs/agent-system-guide.md) (manual) ·
  [AGENTS.md](AGENTS.md) (operating rules) ·
  [docs/architecture-report.md](docs/architecture-report.md) (how this was built) ·
  [persona-clone-template/VISION.md](../persona-clone-template/VISION.md) (the vision).

## For collaborators

| You want to… | You need |
|---|---|
| use everything | nothing beyond `/setup` (repos are public) |
| push ingest/synthesis work on a clone | write access to THAT clone repo (owner adds you) |
| add a persona under your own GitHub account | create the repo there; register it with `"github": "your-account/name-clone"` in roster.json — everyone still gets it via `/setup` |
| change the shared roster/teams | write access to this repo |

Two hard rules when working in parallel: **never run two ingest loops on the same
clone at once** (split the roster between you), and machine-specific files are never
committed (agents & global commands are regenerated per machine — that's why `/setup`
exists).

## Layout

```
persona-roster/
├── roster.json           WHO exists: every clone + domains + build status (+ optional github origin)
├── teams.json            WHO sits together: teams, roles, reviewers, routing vocabulary
├── STATE.md · index.md · log.md · wiki/   the system's own memory (auto-maintained)
├── plans/                persistent multi-step plans (/plan → /run-plan)
├── orchestrator/         the procedures: router, pipelines, roundtable, roles, knowledge-commit
├── clones/               the persona repos (downloaded here; each stays its own git repo)
├── .claude/commands/     /setup /add-clone /council /work /plan /run-plan /review /wiki
├── .claude/agents/       generated advisor+operator agents (machine-local, gitignored)
├── docs/                 the manual + architecture report
└── tools/                setup & routing machinery (clone_all, gen_agents, install_global,
                          route, validate, roster_status, tests/)
```

## Hard rules (carried from the clones)

- **One repo = one person.** Personas never read each other's wikis.
- **No merged super-brain.** Synthesis happens at runtime (the moderator), never in the data.
- **Citations all the way down.** Every claim traces to a dated wiki source.
- **No fabrication.** A clone that doesn't know deflects in character; the gap is logged.

<details>
<summary><b>Manual setup</b> (if you'd rather not use /setup)</summary>

```bash
python3 tools/clone_all.py        # pull every clone repo into clones/ (idempotent)
#   fork owner instead: PERSONA_ROSTER_OWNER=<gh-user> python3 tools/clone_all.py
python3 tools/gen_agents.py       # generate machine-local persona agents (gitignored)
python3 tools/install_global.py   # install commands+agents user-globally (~/.claude)
python3 tools/roster_status.py    # see who is council-ready
python3 tools/validate.py         # sanity-check configs and wiki
```
</details>
