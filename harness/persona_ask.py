"""Ask a persona a question with a small, cheap, non-Anthropic model.

    python harness/persona_ask.py hormozi "How should I price a new offer?"
    python harness/persona_ask.py hormozi "..." --model mistral-small --mode agentic

Two modes:
  * direct  — system-prompt only, single shot. Fastest/cheapest baseline. Tests
              the thesis "the compiled persona alone answers most questions."
  * agentic — same, plus the wiki tools (grep/read/glob/list). The model
              retrieves and cites, mirroring the Claude Code advisor agent.

This module is import-friendly: bench.py calls ask() directly.
"""
from __future__ import annotations

import argparse
import sys
import time

# Persona answers contain Unicode (em-dashes, smart quotes, arrows); the Windows
# console defaults to cp1252 and would crash on print(). Force UTF-8 output.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

from config import get_persona, load_env
from providers import make_provider, resolve_spec
from wiki_tools import TOOL_SCHEMAS, WikiTools, dispatch

MAX_ITERS_DEFAULT = 12

# Appended to the persona's own system-prompt to give the harness its operating
# contract (mirrors the advisor agent's "How you answer / Hard rules").
HARNESS_CONTRACT = """

---
## Operating instructions (harness)

You are answering as yourself, in first person, in character.

- You have read-only tools over YOUR OWN wiki: `grep`, `read_file`, `glob`, `list_dir`.
  Use them to ground concrete claims. A good path: `grep` for the concept →
  `read_file` the best hit → cite it.
- Stay in your lane (your documented domains). Where your wiki is silent, say so
  in character — deflect, never fabricate.
- Keep the answer tight and useful. End with a `Sources:` line listing the wiki
  paths you actually read (omit if you used no tools).
"""

DIRECT_CONTRACT = """

---
## Operating instructions (harness — direct mode)

Answer as yourself, first person, in character, from what you already know above.
Stay in your documented lane; if you're unsure, say so in character rather than
inventing specifics. Keep it tight and useful.
"""


def ask(persona_slug: str, question: str, model: str = "gemini-flash",
        mode: str = "agentic", max_iters: int = MAX_ITERS_DEFAULT,
        verbose: bool = False) -> dict:
    persona = get_persona(persona_slug)
    provider = make_provider(model)
    spec = resolve_spec(model)

    system = persona.read_system_prompt()
    system += HARNESS_CONTRACT if mode == "agentic" else DIRECT_CONTRACT
    tools = WikiTools(persona.repo)
    tool_schemas = TOOL_SCHEMAS if mode == "agentic" else None

    history: list[dict] = [{"role": "user", "text": question}]
    tok_in = tok_out = tool_calls = iterations = 0
    trace: list[str] = []
    answer = ""

    t0 = time.perf_counter()
    for iterations in range(1, max_iters + 1):
        reply = provider.complete(system, history, tool_schemas)
        tok_in += reply.usage.get("in", 0)
        tok_out += reply.usage.get("out", 0)

        if reply.tool_calls:
            history.append({"role": "assistant", "text": reply.text,
                            "tool_calls": reply.tool_calls})
            for tc in reply.tool_calls:
                tool_calls += 1
                result = dispatch(tools, tc["name"], tc["args"])
                line = f"  → {tc['name']}({_fmt_args(tc['args'])}) [{len(result)} chars]"
                trace.append(line)
                if verbose:
                    print(line, file=sys.stderr)
                history.append({"role": "tool", "tool_call_id": tc["id"],
                                "name": tc["name"], "content": result})
            continue

        answer = reply.text
        break
    else:
        answer = answer or "[harness: hit max iterations without a final answer]"
    elapsed = time.perf_counter() - t0

    cost = (tok_in / 1e6) * spec.price_in + (tok_out / 1e6) * spec.price_out
    return {
        "persona": persona.name,
        "model": model,
        "mode": mode,
        "question": question,
        "answer": answer,
        "latency_s": round(elapsed, 2),
        "tokens_in": tok_in,
        "tokens_out": tok_out,
        "tool_calls": tool_calls,
        "iterations": iterations,
        "cost_usd": round(cost, 6),
        "priced": spec.price_in > 0 or spec.price_out > 0,
        "trace": trace,
    }


def _fmt_args(args: dict) -> str:
    return ", ".join(f"{k}={v!r}" for k, v in (args or {}).items())[:120]


def _print_result(r: dict) -> None:
    print(f"\n\033[1m{r['persona']}\033[0m  ·  {r['model']}  ·  {r['mode']}\n")
    print(r["answer"])
    cost = f"${r['cost_usd']:.5f}" if r["priced"] else "n/a"
    print(f"\n\033[2m— {r['latency_s']}s · {r['tokens_in']}→{r['tokens_out']} tok · "
          f"{r['tool_calls']} tool calls · {r['iterations']} iters · est. cost {cost}\033[0m")


def main() -> None:
    load_env()
    ap = argparse.ArgumentParser(description="Ask a persona via a small non-Anthropic model.")
    ap.add_argument("persona", help="clone slug, e.g. hormozi / chris-do / neil-patel")
    ap.add_argument("question", nargs="+", help="the question")
    ap.add_argument("--model", default="gemini-flash",
                    help="registry alias or 'provider/model@base_url' (see providers.MODELS)")
    ap.add_argument("--mode", choices=["agentic", "direct"], default="agentic")
    ap.add_argument("--max-iters", type=int, default=MAX_ITERS_DEFAULT)
    ap.add_argument("--verbose", action="store_true", help="print tool calls to stderr")
    ap.add_argument("--json", action="store_true", help="emit the raw result dict as JSON")
    a = ap.parse_args()

    try:
        r = ask(a.persona, " ".join(a.question), model=a.model, mode=a.mode,
                max_iters=a.max_iters, verbose=a.verbose)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    if a.json:
        import json
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        _print_result(r)


if __name__ == "__main__":
    main()
