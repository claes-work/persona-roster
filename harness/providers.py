"""Provider-agnostic LLM clients over raw REST (httpx only).

Goal: prove the persona wiki can be queried by small, cheap, non-Anthropic
models with function calling — and stay embeddable in any project (no vendor
SDK). Two wire formats cover the interesting field:

  * Gemini            (generativelanguage.googleapis.com)   — Google format
  * OpenAI-compatible (Mistral, Groq, OpenAI, ...)          — /chat/completions

Every adapter takes a normalized conversation (list of turns) + the neutral
TOOL_SCHEMAS and returns a normalized Reply {text, tool_calls, usage}. The
agentic loop in persona_ask.py never sees provider differences.

Normalized turn shapes:
  {"role": "user", "text": str}
  {"role": "assistant", "text": str, "tool_calls": [{"id","name","args"}]}
  {"role": "tool", "tool_call_id": str, "name": str, "content": str}
"""
from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass, field

import httpx

HTTP_TIMEOUT = 120.0
MAX_RETRIES = 5          # on 429 rate-limit
MAX_BACKOFF_S = 45.0     # cap any single wait


def _post_json(url: str, headers: dict, body: dict, label: str) -> dict:
    """POST with automatic backoff on 429. Honors the server's advertised retry
    delay (Gemini RetryInfo.retryDelay / OpenAI Retry-After) when present.
    Non-429 4xx (e.g. 413 request-too-large) raise immediately — not retryable."""
    delay = 2.0
    for attempt in range(MAX_RETRIES + 1):
        r = httpx.post(url, headers=headers, json=body, timeout=HTTP_TIMEOUT)
        if r.status_code < 400:
            return r.json()
        if r.status_code == 429 and attempt < MAX_RETRIES:
            wait = _retry_delay(r) or delay
            time.sleep(min(wait, MAX_BACKOFF_S))
            delay *= 2
            continue
        raise RuntimeError(f"{label} {r.status_code}: {r.text[:500]}")
    raise RuntimeError(f"{label}: exhausted retries on 429")


def _retry_delay(r: httpx.Response) -> float:
    ra = r.headers.get("retry-after")
    if ra:
        try:
            return float(ra)
        except ValueError:
            pass
    m = re.search(r'"retryDelay":\s*"([0-9.]+)s"', r.text)
    return float(m.group(1)) + 0.5 if m else 0.0


@dataclass
class Reply:
    text: str
    tool_calls: list[dict] = field(default_factory=list)  # [{id,name,args}]
    usage: dict = field(default_factory=dict)             # {"in":int,"out":int}


# ---------------------------------------------------------------------------
# Model registry. price_in/price_out are USD per 1M tokens (rough public list
# prices — EDIT to taste; used only for the cost estimate). 0 => cost shown n/a.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class ModelSpec:
    provider: str      # "gemini" | "openai"
    model: str         # wire model id
    base_url: str = ""
    api_key_env: str = ""
    price_in: float = 0.0
    price_out: float = 0.0


MODELS: dict[str, ModelSpec] = {
    # --- Google Gemini (free tier available) ---
    # NB: bare-versioned ids (gemini-2.0-flash) can carry free-tier limit 0 or
    # 404 on newer keys; the "-latest" aliases are the reliable ones.
    "gemini-flash": ModelSpec("gemini", "gemini-flash-latest", api_key_env="GEMINI_API_KEY",
                              price_in=0.10, price_out=0.40),
    "gemini-flash-lite": ModelSpec("gemini", "gemini-flash-lite-latest", api_key_env="GEMINI_API_KEY",
                                   price_in=0.075, price_out=0.30),
    "gemini-2.0-flash": ModelSpec("gemini", "gemini-2.0-flash", api_key_env="GEMINI_API_KEY",
                                  price_in=0.10, price_out=0.40),
    # --- Mistral (free tier available) ---
    "mistral-small": ModelSpec("openai", "mistral-small-latest",
                               base_url="https://api.mistral.ai/v1",
                               api_key_env="MISTRAL_API_KEY", price_in=0.20, price_out=0.60),
    "mistral-nemo": ModelSpec("openai", "open-mistral-nemo",
                              base_url="https://api.mistral.ai/v1",
                              api_key_env="MISTRAL_API_KEY", price_in=0.15, price_out=0.15),
    # --- Groq (very fast; free tier) ---
    "groq-llama-70b": ModelSpec("openai", "llama-3.3-70b-versatile",
                                base_url="https://api.groq.com/openai/v1",
                                api_key_env="GROQ_API_KEY", price_in=0.59, price_out=0.79),
    "groq-llama-8b": ModelSpec("openai", "llama-3.1-8b-instant",
                               base_url="https://api.groq.com/openai/v1",
                               api_key_env="GROQ_API_KEY", price_in=0.05, price_out=0.08),
}


def resolve_spec(name: str) -> ModelSpec:
    """Accept a registry alias, or an explicit 'provider/model[@base_url]'."""
    if name in MODELS:
        return MODELS[name]
    if "/" in name:
        provider, _, rest = name.partition("/")
        model, _, base = rest.partition("@")
        env = "GEMINI_API_KEY" if provider == "gemini" else \
              "MISTRAL_API_KEY" if "mistral" in base else \
              "GROQ_API_KEY" if "groq" in base else "OPENAI_API_KEY"
        return ModelSpec(provider, model, base_url=base, api_key_env=env)
    raise KeyError(f"Unknown model {name!r}. Known: {', '.join(MODELS)} "
                   f"(or 'provider/model@base_url').")


# ---------------------------------------------------------------------------
def make_provider(name: str):
    spec = resolve_spec(name)
    key = os.environ.get(spec.api_key_env, "")
    if not key:
        raise RuntimeError(
            f"Missing API key: set {spec.api_key_env} (env or harness/.env) for model {name!r}.")
    if spec.provider == "gemini":
        return GeminiProvider(spec, key)
    return OpenAICompatProvider(spec, key)


# ---------------------------------------------------------------------------
class GeminiProvider:
    def __init__(self, spec: ModelSpec, api_key: str):
        self.spec, self.key = spec, api_key
        self.label = f"gemini:{spec.model}"

    def _contents(self, history: list[dict]) -> list[dict]:
        contents = []
        for t in history:
            if t["role"] == "user":
                contents.append({"role": "user", "parts": [{"text": t["text"]}]})
            elif t["role"] == "assistant":
                parts = []
                if t.get("text"):
                    parts.append({"text": t["text"]})
                for tc in t.get("tool_calls", []):
                    part = {"functionCall": {"name": tc["name"], "args": tc["args"]}}
                    # Gemini thinking models require the thought_signature from the
                    # original functionCall part to be echoed back verbatim.
                    if tc.get("_sig"):
                        part["thoughtSignature"] = tc["_sig"]
                    parts.append(part)
                contents.append({"role": "model", "parts": parts or [{"text": ""}]})
            elif t["role"] == "tool":
                contents.append({"role": "user", "parts": [{
                    "functionResponse": {"name": t["name"],
                                         "response": {"result": t["content"]}}}]})
        return contents

    def complete(self, system: str, history: list[dict], tools: list[dict]) -> Reply:
        body = {
            "system_instruction": {"parts": [{"text": system}]},
            "contents": self._contents(history),
            "generationConfig": {"temperature": 0.3, "maxOutputTokens": 2048},
        }
        if tools:
            body["tools"] = [{"function_declarations": tools}]
            body["tool_config"] = {"function_calling_config": {"mode": "AUTO"}}
        url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
               f"{self.spec.model}:generateContent")
        data = _post_json(url, {"x-goog-api-key": self.key}, body, f"Gemini/{self.spec.model}")
        cand = (data.get("candidates") or [{}])[0]
        parts = (cand.get("content") or {}).get("parts", []) or []
        text, calls = "", []
        for i, p in enumerate(parts):
            if "text" in p:
                text += p["text"]
            elif "functionCall" in p:
                fc = p["functionCall"]
                calls.append({"id": f"call_{i}", "name": fc["name"], "args": fc.get("args", {}),
                              "_sig": p.get("thoughtSignature")})
        um = data.get("usageMetadata", {})
        return Reply(text.strip(), calls,
                     {"in": um.get("promptTokenCount", 0), "out": um.get("candidatesTokenCount", 0)})


class OpenAICompatProvider:
    def __init__(self, spec: ModelSpec, api_key: str):
        self.spec, self.key = spec, api_key
        self.label = f"{spec.base_url.split('//')[-1].split('.')[1] if '.' in spec.base_url else 'openai'}:{spec.model}"

    def _messages(self, system: str, history: list[dict]) -> list[dict]:
        msgs = [{"role": "system", "content": system}]
        for t in history:
            if t["role"] == "user":
                msgs.append({"role": "user", "content": t["text"]})
            elif t["role"] == "assistant":
                m = {"role": "assistant", "content": t.get("text") or ""}
                if t.get("tool_calls"):
                    m["tool_calls"] = [{
                        "id": tc["id"], "type": "function",
                        "function": {"name": tc["name"], "arguments": json.dumps(tc["args"])},
                    } for tc in t["tool_calls"]]
                    m["content"] = t.get("text") or None
                msgs.append(m)
            elif t["role"] == "tool":
                msgs.append({"role": "tool", "tool_call_id": t["tool_call_id"],
                             "name": t["name"], "content": t["content"]})
        return msgs

    def complete(self, system: str, history: list[dict], tools: list[dict]) -> Reply:
        body = {
            "model": self.spec.model,
            "messages": self._messages(system, history),
            "temperature": 0.3,
            "max_tokens": 2048,
        }
        if tools:
            body["tools"] = [{"type": "function", "function": t} for t in tools]
            body["tool_choice"] = "auto"
        data = _post_json(f"{self.spec.base_url}/chat/completions",
                          {"Authorization": f"Bearer {self.key}"}, body, self.label)
        msg = (data.get("choices") or [{}])[0].get("message", {})
        text = msg.get("content") or ""
        calls = []
        for tc in msg.get("tool_calls") or []:
            fn = tc.get("function", {})
            try:
                args = json.loads(fn.get("arguments") or "{}")
            except json.JSONDecodeError:
                args = {}
            calls.append({"id": tc.get("id", f"call_{len(calls)}"), "name": fn.get("name"), "args": args})
        us = data.get("usage", {})
        return Reply(text.strip(), calls,
                     {"in": us.get("prompt_tokens", 0), "out": us.get("completion_tokens", 0)})
