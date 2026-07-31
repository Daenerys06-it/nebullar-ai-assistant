"""LLM provider switch: choose Kimi, GPT-5, or DeepSeek from .env.

Why this layer exists:
- Company computer uses Kimi (internal Anthropic-compatible gateway).
- GPT-5 via company gateway (when available).
- Home computer uses DeepSeek (external API).
- agent.py / retrieve.py should not care about SDK differences. They call load_client()
  and complete(); this file hides the provider-specific details.

Switching:
- LLM_PROVIDER=kimi      -> company Anthropic-compatible gateway (Kimi K2.5)
- LLM_PROVIDER=gpt5      -> company GPT-5 gateway (Anthropic-compatible)
- LLM_PROVIDER=deepseek  -> DeepSeek (home computer)
"""
import os
from dotenv import load_dotenv

load_dotenv()
PROVIDER = os.getenv("LLM_PROVIDER", "kimi").strip().lower()
FALLBACK_PROVIDER = os.getenv("LLM_FALLBACK_PROVIDER", "").strip().lower()


DEFAULT_MODELS = {
    "kimi": "kimi-k2.5",
    "gpt5": "gpt-5.5",  # OpenAI responses API
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
    if PROVIDER == "kimi":
        import anthropic

        key = os.getenv("KIMI_API_KEY")
        base_url = os.getenv("KIMI_BASE_URL")
        if not key:
            raise RuntimeError("LLM_PROVIDER=kimi but KIMI_API_KEY is missing. Check .env")
        if not base_url:
            raise RuntimeError("LLM_PROVIDER=kimi but KIMI_BASE_URL is missing. Check .env")
        return anthropic.Anthropic(base_url=base_url, api_key=key), _get_model("kimi")

    if PROVIDER == "gpt5":
        from openai import OpenAI

        token = os.getenv("GPT5_AUTH_TOKEN") or os.getenv("OPENAI_API_KEY")
        base_url = os.getenv("GPT5_BASE_URL") or os.getenv("OPENAI_BASE_URL")
        if not token:
            raise RuntimeError("LLM_PROVIDER=gpt5 but GPT5_AUTH_TOKEN/OPENAI_API_KEY is missing. Check .env")
        if not base_url:
            raise RuntimeError("LLM_PROVIDER=gpt5 but GPT5_BASE_URL/OPENAI_BASE_URL is missing. Check .env")
        # GPT-5.5 uses OpenAI responses API, not Anthropic
        return OpenAI(api_key=token, base_url=base_url), _get_model("gpt5")

    if PROVIDER == "deepseek":
        from openai import OpenAI

        key = os.getenv("DEEPSEEK_API_KEY")
        if not key:
            raise RuntimeError("LLM_PROVIDER=deepseek but DEEPSEEK_API_KEY is missing. Check .env")
        return OpenAI(api_key=key, base_url="https://api.deepseek.com"), _get_model("deepseek")

    raise RuntimeError("Unknown LLM_PROVIDER={!r}; use kimi, gpt5, or deepseek".format(PROVIDER))


def _build_client(provider: str):
    """Build a client/model pair for an explicit provider.

    This is used for fallback retries. load_client() stays as the public entry point
    for the primary provider selected by LLM_PROVIDER.
    """
    if provider == "kimi":
        import anthropic

        key = os.getenv("KIMI_API_KEY")
        base_url = os.getenv("KIMI_BASE_URL")
        if not key:
            raise RuntimeError("Fallback provider kimi selected but KIMI_API_KEY is missing")
        if not base_url:
            raise RuntimeError("Fallback provider kimi selected but KIMI_BASE_URL is missing")
        return anthropic.Anthropic(base_url=base_url, api_key=key), _get_model("kimi")

    if provider == "gpt5":
        from openai import OpenAI

        token = os.getenv("GPT5_AUTH_TOKEN") or os.getenv("OPENAI_API_KEY")
        base_url = os.getenv("GPT5_BASE_URL") or os.getenv("OPENAI_BASE_URL")
        if not token:
            raise RuntimeError("Fallback provider gpt5 selected but GPT5_AUTH_TOKEN/OPENAI_API_KEY is missing")
        if not base_url:
            raise RuntimeError("Fallback provider gpt5 selected but GPT5_BASE_URL/OPENAI_BASE_URL is missing")
        return OpenAI(api_key=token, base_url=base_url), _get_model("gpt5")

    if provider == "deepseek":
        from openai import OpenAI

        key = os.getenv("DEEPSEEK_API_KEY")
        if not key:
            raise RuntimeError("Fallback provider deepseek selected but DEEPSEEK_API_KEY is missing")
        return OpenAI(api_key=key, base_url="https://api.deepseek.com"), _get_model("deepseek")

    raise RuntimeError(f"Unknown fallback provider {provider!r}")


def _complete_with_provider(provider, client, model, system, user, max_tokens):
    """Provider-specific call implementation."""
    if provider == "kimi":
        resp = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        # Handle text blocks and thinking blocks (Kimi returns both)
        texts = []
        for b in resp.content:
            if b.type == "text":
                texts.append(b.text)
        return "".join(texts)

    if provider == "gpt5":
        # GPT-5.5 uses OpenAI responses API
        resp = client.responses.create(
            model=model,
            input=[{"role": "user", "content": user}],
            instructions=system,
        )
        # Extract text from response
        for item in resp.output:
            if item.type == "message" and item.content:
                for content in item.content:
                    if content.type == "output_text":
                        return content.text
        return ""

    # DeepSeek: OpenAI-style API.
    params = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    params["temperature"] = 0.3

    resp = client.chat.completions.create(**params)
    return resp.choices[0].message.content


def complete(client, model, system, user, max_tokens=4096):
    """Run one completion and return plain text.

    Kimi/GPT-5 use Anthropic messages endpoint. DeepSeek uses OpenAI chat.completions.
    We keep this difference here so upper layers stay simple.

    Optional fallback:
    - If LLM_FALLBACK_PROVIDER is set in .env, retry with that provider when the
      primary provider fails.
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
            raise primary_error
