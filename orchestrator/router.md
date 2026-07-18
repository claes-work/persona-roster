# Router — from task to team, members, and depth

How a skill turns a free-form user request into a routed unit of work. The split follows
the pipeline philosophy of the clone repos: **the LLM does the judgment (classification),
Python does the mechanical/stateful half (`tools/route.py` — deterministic, testable).**

## Step 1 — Classify the task (LLM judgment)

Read the request (plus loaded context, see `knowledge-commit.md` §Read-before-work) and
fill this descriptor. Be minimal — tags you can't justify, leave out.

```yaml
task:
  domains: [youtube, title, thumbnail]   # kebab-case topic tags; match teams.json vocabulary where possible
  intent: decide | execute | plan | review | research
  artifact: what should exist afterwards (decision-record, titles, newsletter, code-change, plan, report ...)
  risk: low | medium | high              # cost of being wrong
  reversible: true | false               # can it be cheaply undone/iterated?
  complexity: low | medium | high
  novelty: low | medium | high           # have we done this before? (check wiki/learnings/)
  tags: [seo, positioning]               # conditional-member triggers (teams.json conditional_members keys)
```

## Step 2 — Resolve team + seats (deterministic)

```bash
python tools/route.py --domains youtube,title --tags seo --risk low --reversible \
    [--team youtube] [--include garyvee] [--exclude networkchuck] [--depth fast] \
    [--intent execute] [--complexity medium]
```

`route.py` applies, in order:

1. **Explicit `--team`** override, else **domain match** against `teams.json` (team whose
   `domains` overlap the task's domains most), else **fallback** (see below).
2. **Default members + conditional members** whose tag matched.
3. **`--include` / `--exclude`** overrides (validated against roster.json).
4. **Status gating** — only `status: active` clones are seated; everyone else is listed
   under `reserved_seats` (reported, never fanned out — the existing skip-stubs rule).
5. **Depth** — explicit `--depth`, else risk/reversibility/complexity rules
   (see `pipelines.md`), else the team's `default_depth`.
6. Output: JSON with `team`, `seated` (advisors to spawn), `reserved_seats`, `roles`,
   `review` (independent reviewers), `depth`, and `rationale` lines for observability.

## Fallback (unknown domain)

No team matches → route.py builds an **ad-hoc team**: clones whose roster
`domains`/`strong_for` overlap the task domains. Still nothing → `seated` is empty and
`fallback: "no-grounded-voice"` is set; the skill then proceeds **without persona
fan-out** (plain Claude + skeptical-reviewer for review) and says so — an ungrounded
persona take is worse than none (deflect-over-fabricate, roster edition).

## Router principles

- **Not everyone talks about everything.** A database migration does not need GaryVee.
  3–6 non-redundant voices beat headcount (see memory: council value = non-redundant
  domain coverage).
- **Own evidence first.** If `wiki/learnings/` has an `effective_rule` on the question,
  it is loaded into every seat's brief and outranks persona defaults.
- **Observability.** Every routed run reports: chosen pipeline, team, seats + why,
  reserved seats, reviewers, and which wiki pages were read. Keep it to a few lines.
- **Overrides are overrides.** `--team/--include/--exclude/--depth` are the public knobs;
  everything else is automatic. Don't grow a parameter zoo.
