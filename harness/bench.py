"""Benchmark: run a set of questions across models × modes for one persona.

    python harness/bench.py hormozi
    python harness/bench.py hormozi --models gemini-flash,mistral-small,groq-llama-70b --modes agentic,direct

Prints a per-(model,mode) summary (avg latency, avg tokens, total est. cost,
avg tool calls) and writes every full answer to a markdown file so you can grade
quality by hand — the one thing a script can't score for you.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

from config import load_env
from persona_ask import ask

HERE = Path(__file__).resolve().parent


def load_questions(path: str | None) -> list[str]:
    p = Path(path) if path else HERE / "questions.sample.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    return data["questions"] if isinstance(data, dict) else data


def main() -> None:
    load_env()
    ap = argparse.ArgumentParser(description="Benchmark small models against a persona wiki.")
    ap.add_argument("persona", help="clone slug, e.g. hormozi")
    ap.add_argument("--models", default="gemini-flash",
                    help="comma-separated registry aliases")
    ap.add_argument("--modes", default="agentic,direct",
                    help="comma-separated: agentic,direct")
    ap.add_argument("--questions", help="path to a questions .json (list or {questions:[...]})")
    ap.add_argument("--out", default=str(HERE / "bench_answers.md"))
    a = ap.parse_args()

    models = [m.strip() for m in a.models.split(",") if m.strip()]
    modes = [m.strip() for m in a.modes.split(",") if m.strip()]
    questions = load_questions(a.questions)

    runs: list[dict] = []
    md: list[str] = [f"# Bench — {a.persona}\n"]
    total = len(models) * len(modes) * len(questions)
    n = 0
    for model in models:
        for mode in modes:
            for q in questions:
                n += 1
                print(f"[{n}/{total}] {model} · {mode} · {q[:60]}...", file=sys.stderr)
                try:
                    r = ask(a.persona, q, model=model, mode=mode)
                except Exception as e:
                    print(f"    FAILED: {e}", file=sys.stderr)
                    continue
                runs.append(r)
                md.append(f"## [{model} · {mode}] {q}\n\n{r['answer']}\n\n"
                          f"*{r['latency_s']}s · {r['tokens_in']}→{r['tokens_out']} tok · "
                          f"{r['tool_calls']} tool calls · "
                          f"est. ${r['cost_usd']:.5f}*\n")

    Path(a.out).write_text("\n".join(md), encoding="utf-8")

    # --- summary table ---
    print("\n" + "=" * 78)
    print(f"{'model':<20}{'mode':<9}{'n':>3}{'avg s':>8}{'avg in':>9}"
          f"{'avg out':>9}{'avg tools':>11}{'total $':>10}")
    print("-" * 78)
    for model in models:
        for mode in modes:
            g = [r for r in runs if r["model"] == model and r["mode"] == mode]
            if not g:
                continue
            avg_lat = statistics.mean(r["latency_s"] for r in g)
            avg_in = statistics.mean(r["tokens_in"] for r in g)
            avg_out = statistics.mean(r["tokens_out"] for r in g)
            avg_tools = statistics.mean(r["tool_calls"] for r in g)
            tot_cost = sum(r["cost_usd"] for r in g)
            priced = any(r["priced"] for r in g)
            cost_s = f"${tot_cost:.4f}" if priced else "n/a"
            print(f"{model:<20}{mode:<9}{len(g):>3}{avg_lat:>8.2f}{avg_in:>9.0f}"
                  f"{avg_out:>9.0f}{avg_tools:>11.1f}{cost_s:>10}")
    print("=" * 78)
    print(f"\nFull answers written to {a.out} — grade quality there.")


if __name__ == "__main__":
    main()
