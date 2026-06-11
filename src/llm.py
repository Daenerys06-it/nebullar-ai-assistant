"""LLM 提供方抽象层：按 .env 的 LLM_PROVIDER 选 Opus(公司网关) 或 DeepSeek(家里电脑)。

为什么要这层：
- 公司电脑走内网 Anthropic 网关连 Opus；家里电脑连不上网关，只能用 DeepSeek。
- 两家 SDK 调用方式不一样（见 complete），上层 agent.py / retrieve.py 不该到处写 if。
- 把"选谁 + 怎么调"收拢到这里，上层只管 load_client() 拿 client+model、complete() 拿文本。

切换方式：改 .env 里的 LLM_PROVIDER=opus 或 deepseek，代码一行不用动。
"""
import os
from dotenv import load_dotenv

load_dotenv()  # 把 .env 内容加载进环境变量

# 选哪个提供方：opus(默认，公司电脑) | deepseek(家里电脑)。统一转小写去空格，容错。
PROVIDER = os.getenv("LLM_PROVIDER", "opus").strip().lower()


def load_client():
    """按 LLM_PROVIDER 建客户端，返回 (client, model)。

    - opus    : 公司内网 Anthropic 网关。anthropic SDK 自动读 ANTHROPIC_BASE_URL/AUTH_TOKEN，
                所以 Anthropic() 不用传参。
    - deepseek: 家里用。DeepSeek 兼容 OpenAI 接口，用 OpenAI 类把 base_url 指过去。

    凭据都放 .env（被 gitignore），不写死代码，避免提交泄露。
    缺凭据时早报错，别等真正调用时才崩。
    """
    if PROVIDER == "opus":
        import anthropic  # 延迟导入：家里没装/不用 anthropic 时也不会报错
        if not os.getenv("ANTHROPIC_AUTH_TOKEN"):
            raise RuntimeError("LLM_PROVIDER=opus 但未找到 ANTHROPIC_AUTH_TOKEN，检查 .env")
        return anthropic.Anthropic(), "claude-opus-4-8"

    if PROVIDER == "deepseek":
        from openai import OpenAI  # 延迟导入：公司机器不用 deepseek 时不强依赖
        key = os.getenv("DEEPSEEK_API_KEY")
        if not key:
            raise RuntimeError("LLM_PROVIDER=deepseek 但未找到 DEEPSEEK_API_KEY，检查 .env")
        return OpenAI(api_key=key, base_url="https://api.deepseek.com"), "deepseek-chat"

    raise RuntimeError(f"未知 LLM_PROVIDER={PROVIDER!r}，应为 opus 或 deepseek")


def complete(client, model, system, user, max_tokens=4096):
    """统一的一次性补全调用，屏蔽两家 SDK 差异，返回纯文本字符串。

    两家差异：
    - Anthropic：system 单独传 system 参数，messages 只放 user；
                 返回在 resp.content（内容块列表），取 type=='text' 的块拼起来。
                 Opus 4.8 不支持 temperature（传了会 400），所以不传。
    - DeepSeek(OpenAI 风格)：system 塞进 messages 第一条；
                 返回在 resp.choices[0].message.content。temperature=0.3 让答案更稳。
    """
    if PROVIDER == "opus":
        resp = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return "".join(b.text for b in resp.content if b.type == "text")

    # deepseek / OpenAI 风格
    resp = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        temperature=0.3,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return resp.choices[0].message.content
