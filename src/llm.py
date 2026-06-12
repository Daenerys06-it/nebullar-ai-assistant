"""LLM provider switch: choose GPT-5, Opus gateway, or DeepSeek from .env.

Why this layer exists:
- Company computer can use either GPT-5 or the internal Anthropic-compatible Opus gateway.
- The company gateway can expose GPT-5 through an Anthropic-compatible endpoint.
- Home computer cannot reach the company gateway, so it uses DeepSeek.
- agent.py / retrieve.py should not care about SDK differences. They call load_client()
  and complete(); this file hides the provider-specific details.

Switching:
- LLM_PROVIDER=gpt5     -> Anthropic-compatible GPT-5 (good when developing from Codex/GPT-5)
- LLM_PROVIDER=opus     -> company Anthropic-compatible gateway Opus
- LLM_PROVIDER=deepseek -> DeepSeek (home computer)
"""
import os
from dotenv import load_dotenv

load_dotenv()
PROVIDER = os.getenv("LLM_PROVIDER", "opus").strip().lower()
FALLBACK_PROVIDER = os.getenv("LLM_FALLBACK_PROVIDER", "").strip().lower()


DEFAULT_MODELS = {
    "gpt5": "gpt-5",
    "opus": "claude-opus-4-8",
    "deepseek": "deepseek-chat",
}


def _get_model(provider: str) -> str:
    """Allow .env to override a model without touching code."""
    env_name = f"{provider.upper()}_MODEL"
    return os.getenv(env_name, DEFAULT_MODELS[provider]).strip()


def load_client():
    """Build the configured LLM client and return (client, model).

    Credentials stay in .env, which is gitignored.
    """
    if PROVIDER == "gpt5":
        import anthropic

        token = os.getenv("GPT5_AUTH_TOKEN") or os.getenv("OPENAI_API_KEY")
        base_url = os.getenv("GPT5_BASE_URL") or os.getenv("OPENAI_BASE_URL")
        if not token:
            raise RuntimeError("LLM_PROVIDER=gpt5 but GPT5_AUTH_TOKEN/OPENAI_API_KEY is missing. Check .env")
        if not base_url:
            raise RuntimeError("LLM_PROVIDER=gpt5 but GPT5_BASE_URL/OPENAI_BASE_URL is missing. Check .env")
        return anthropic.Anthropic(base_url=base_url, auth_token=token), _get_model("gpt5")

    if PROVIDER == "opus":
        import anthropic

        if not os.getenv("ANTHROPIC_AUTH_TOKEN"):
            raise RuntimeError("LLM_PROVIDER=opus but ANTHROPIC_AUTH_TOKEN is missing. Check .env")
        # anthropic SDK reads ANTHROPIC_BASE_URL and ANTHROPIC_AUTH_TOKEN automatically.
        return anthropic.Anthropic(), _get_model("opus")

    if PROVIDER == "deepseek":
        from openai import OpenAI

        key = os.getenv("DEEPSEEK_API_KEY")
        if not key:
            raise RuntimeError("LLM_PROVIDER=deepseek but DEEPSEEK_API_KEY is missing. Check .env")
        return OpenAI(api_key=key, base_url="https://api.deepseek.com"), _get_model("deepseek")

    raise RuntimeError("Unknown LLM_PROVIDER={!r}; use gpt5, opus, or deepseek".format(PROVIDER))


def _build_client(provider: str):
    """Build a client/model pair for an explicit provider.

    This is used for fallback retries. load_client() stays as the public entry point
    for the primary provider selected by LLM_PROVIDER.
    """
    if provider == "gpt5":
        import anthropic

        token = os.getenv("GPT5_AUTH_TOKEN") or os.getenv("OPENAI_API_KEY")
        base_url = os.getenv("GPT5_BASE_URL") or os.getenv("OPENAI_BASE_URL")
        if not token:
            raise RuntimeError("Fallback provider gpt5 selected but GPT5_AUTH_TOKEN/OPENAI_API_KEY is missing")
        if not base_url:
            raise RuntimeError("Fallback provider gpt5 selected but GPT5_BASE_URL/OPENAI_BASE_URL is missing")
        return anthropic.Anthropic(base_url=base_url, auth_token=token), _get_model("gpt5")

    if provider == "opus":
        import anthropic

        if not os.getenv("ANTHROPIC_AUTH_TOKEN"):
            raise RuntimeError("Fallback provider opus selected but ANTHROPIC_AUTH_TOKEN is missing")
        return anthropic.Anthropic(), _get_model("opus")

    if provider == "deepseek":
        from openai import OpenAI

        key = os.getenv("DEEPSEEK_API_KEY")
        if not key:
            raise RuntimeError("Fallback provider deepseek selected but DEEPSEEK_API_KEY is missing")
        return OpenAI(api_key=key, base_url="https://api.deepseek.com"), _get_model("deepseek")

    raise RuntimeError(f"Unknown fallback provider {provider!r}")


def _complete_with_provider(provider, client, model, system, user, max_tokens):
    """Provider-specific call implementation."""
    if provider in {"gpt5", "opus"}:
        resp = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return "".join(b.text for b in resp.content if b.type == "text")

    # GPT-5 / DeepSeek: OpenAI-style API.
    params = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    # DeepSeek accepts temperature; keep GPT-5 conservative and avoid provider-specific
    # sampling differences unless we explicitly need them later.
    if provider == "deepseek":
        params["temperature"] = 0.3

    resp = client.chat.completions.create(**params)
    return resp.choices[0].message.content


def complete(client, model, system, user, max_tokens=4096):
    """Run one completion and return plain text.

    Anthropic uses messages.create(system=...). GPT-5 and DeepSeek use the OpenAI-style
    chat.completions endpoint. We keep this difference here so upper layers stay simple.

    Optional fallback:
    - If LLM_FALLBACK_PROVIDER is set in .env, retry with that provider when the
      primary provider fails (for example company Opus gateway returns 503).
    """
    try:
        return _complete_with_provider(PROVIDER, client, model, system, user, max_tokens)
    except Exception as primary_error:
        if not FALLBACK_PROVIDER or FALLBACK_PROVIDER == PROVIDER:
            raise

        fallback_client, fallback_model = _build_client(FALLBACK_PROVIDER)
        try:
            answer = _complete_with_provider(
                FALLBACK_PROVIDER,
                fallback_client,
                fallback_model,
                system,
                user,
                max_tokens,
            )
            return f"（主模型 {PROVIDER}/{model} 调用失败，已自动切到 {FALLBACK_PROVIDER}/{fallback_model} 继续回答。）\n\n{answer}"
        except Exception:
            # Preserve the original provider error; it is usually the actionable one.
            raise primary_error
