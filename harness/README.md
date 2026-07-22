# harness/ — query personas with small, cheap, non-Anthropic models

A **standalone** proof-of-concept: ask a persona clone a question using a small
model (Gemini Flash / Mistral small / Groq Llama) over its API, **independent of
Claude Code and the Anthropic subscription**. Depends only on `httpx` — copy this
folder into any project (2Key, a website backend, …) and drive it with an API key.

## Why

The Claude Code advisor agent answers *as* a persona by (1) loading the compiled
`persona/system-prompt.md` and (2) grounding in the clone's wiki via Read/Grep/Glob.
None of that requires a frontier model. This harness reproduces exactly that loop
with a swappable small model, so we can measure — for real — **quality vs. speed
vs. cost** and decide what to embed elsewhere.

## Setup (one-time)

```bash
cp harness/.env.example harness/.env    # then paste ONE key (all have free tiers)
python -m pip install httpx             # already present in most envs
```

Keys: Gemini → https://aistudio.google.com/apikey · Mistral → https://console.mistral.ai
· Groq → https://console.groq.com/keys

## Ask

```bash
# agentic (default): model uses grep/read over the wiki and cites sources
python harness/persona_ask.py hormozi "How should I price a new offer?"

# direct: system-prompt only, single shot — the fast/cheap baseline
python harness/persona_ask.py hormozi "..." --mode direct

# pick a model + see the tool calls
python harness/persona_ask.py chris-do "How do I raise my rates?" \
  --model mistral-small --verbose
```

Personas = the `slug` in `roster.json` (only `active` clones with a compiled
system-prompt are queryable): `hormozi`, `chris-do`, `neil-patel`, `mkbhd`.

## Benchmark

```bash
python harness/bench.py hormozi \
  --models gemini-flash,mistral-small,groq-llama-70b --modes agentic,direct
```

Prints a per-(model, mode) table — avg latency, avg tokens, avg tool calls, total
est. cost — and writes every full answer to `harness/bench_answers.md` for manual
quality grading (a script can't judge whether it *sounds like Hormozi* and cites
correctly — you do that).

## How it maps to the Claude Code advisor

| Advisor agent | This harness |
|---|---|
| system = `persona/system-prompt.md` | `config.get_persona().read_system_prompt()` |
| tools = Read / Grep / Glob (repo-scoped) | `wiki_tools.WikiTools` (path-jailed to the clone) |
| "cite sources, deflect where silent" | appended `HARNESS_CONTRACT` |
| Opus/Sonnet | any `providers.MODELS` alias |

## Files

- `config.py` — resolve persona slug → clone repo + system-prompt (reads `roster.json`); `.env` loader
- `wiki_tools.py` — read-only, path-jailed grep/read/glob/list + provider-neutral tool schemas
- `providers.py` — Gemini + OpenAI-compatible (Mistral/Groq/OpenAI) clients over raw REST; model registry + prices
- `persona_ask.py` — the agentic loop (+ direct mode) and CLI; `ask()` is import-friendly
- `bench.py` — models × modes × questions matrix → summary table + answers file

## Limits / notes

- **Read-only.** The tools cannot write or escape the clone repo (path sandbox).
- Only queries **one** persona at a time — this is the single-advisor path, not a
  full moderated council (synthesis across personas stays a runtime concern).
- `providers.MODELS` prices are rough public list prices for the cost estimate —
  edit them; model IDs drift, so override with `--model provider/model@base_url`
  if an alias 404s.
