# Persona Roster — a council of cloned minds

An umbrella project that composes independent **persona clones** (each its own repo,
built from [`persona-clone-template`](../persona-clone-template)) into an **agent team**.
Ask a problem; each persona answers *as that person*, grounded in its own cited wiki; a
neutral moderator synthesizes the takes with per-persona attribution.

This folder **groups** the clones and holds the **orchestration layer**. It never merges
their knowledge — that is the whole point (see "Hard rules").

## Layout

```
persona-roster/
├── roster.json           canonical registry (machine-readable): every clone + its path/domains/status
├── clones/               the clones, grouped here (Windows junctions to their real repos;
│                         gitignored — each clone is its own repo, paths live in roster.json)
├── orchestrator/
│   ├── roundtable.md     the council harness: fan-out → (cross-examine) → synthesize
│   └── moderator-prompt.md   the neutral curator that combines the takes
├── .claude/
│   ├── agents/           auto-generated persona agents (advisor + operator per clone)
│   └── commands/council.md   /council <problem> — run a roundtable
└── tools/gen_agents.py   regenerates .claude/agents/* from roster.json + each clone's system-prompt
```

## Current roster

Primary tier has a repo each; secondary tier is planned (names in `roster.json`).

| Clone | Slug | Domains | Status |
|---|---|---|---|
| Alex Hormozi | `hormozi` | acquisition, offers, sales, pricing, scaling | **active** (system-prompt v35) |
| Chris Do | `chris-do` | branding, positioning, pricing creative work | bootstrapped (not compiled) |
| Neil Patel | `neil-patel` | SEO, digital marketing, content | created (run `/clone-setup`) |
| Marques Brownlee | `mkbhd` | tech review, production quality, creator business | created |
| Gary Vaynerchuk | `garyvee` | marketing, brand, attention | created |
| Chuck Keith | `networkchuck` | IT, networking, homelab | created |

Only **active** clones join a council; the rest hold a reserved seat until ingested.
Secondary tier (planned): Simon Sinek, Seth Godin, Ali Abdaal, Cal Newport, Derek Muller,
Cleo Abram, Linus Sebastian, Jeff Geerling, Theo Browne, Tim Ferriss.

## Two ways to use a clone

- **Advisor (read-only, council):** answers "how would X approach this?" grounded in
  X's wiki. Safe to fan out many at once. Tools: Read/Grep/Glob over its own repo.
- **Operator (embodied, works in your real projects):** gets full Claude Code tools
  (Edit/Write/Bash/WebSearch) **plus** X's system-prompt as a values/taste layer, and
  operates *inside* another project (e.g. `D:\Dev\youtube-engine`) the way X would
  prioritize. Persona = judgment; Claude Code = hands.

Both flavors are generated from the **same** source — each clone's
`persona/system-prompt.md` — so there is no hand-maintained duplication.

## Run a council

```
/council How should I structure and launch a new high-ticket offer?
```

or, in any Claude Code session, summon a single voice:

```
@hormozi-advisor  How would you price this?
@mkbhd-operator   Improve the thumbnail pipeline in youtube-engine.
```

## Add a clone to the roster

1. Build the clone in its own repo from `persona-clone-template` (`/clone-setup <Name>`,
   then `/loop /ingest-loop` until the first synthesis pass compiles a `system-prompt.md`).
2. Add an entry to `roster.json` (slug, name, path, domains, tier, status).
3. Junction it into `clones/` (existing repos) or create it there directly (new ones).
4. `python tools/gen_agents.py` → regenerates the advisor + operator agent files.

## Hard rules (carried from the clones)

- **One repo = one person.** Personas never read each other's wikis. They exchange
  *statements*, not knowledge bases — like real people in a meeting.
- **No merged super-brain.** Synthesis happens at runtime (the moderator), never in the
  data. Distinct, honest, cited perspectives are the entire value.
- **Citations all the way down.** Every claim traces to a dated wiki source, so
  disagreements between clones are *resolvable*, not noise.
- **No fabrication.** A clone that doesn't know deflects in character and the gap is
  logged in its own `wiki/gaps.md`.

See [`persona-clone-template/VISION.md`](../persona-clone-template/VISION.md) for the
staged plan this realizes (this project is Stage 2 + Stage 3).
