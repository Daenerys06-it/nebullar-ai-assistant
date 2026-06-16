"""Long-term support cases.

第一版先做轻量 JSONL 检索：
- cases.jsonl 保存 FAE 支持案例
- search_cases(query) 按关键词命中相关案例

后续如果案例量变大，再把 cases 也做向量化或接入 ChromaDB。
"""

from __future__ import annotations

import json
import os
import re
from functools import lru_cache


_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES_PATH = os.path.join(_BASE, "data", "cases.jsonl")


CASE_FIELDS = [
    "symptom",
    "root_cause",
    "solution",
    "module",
    "product",
    "tags",
]


ALIASES = {
    "adb": ["adb", "adb devices"],
    "device": ["设备", "device", "终端", "机器"],
    "not_found": ["查不到", "看不到", "识别不到", "没有设备", "连不上", "无法识别", "not found", "unauthorized"],
    "debugging": ["debug", "debugging", "usb debugging", "usb调试", "调试", "开发者模式", "开发者选项"],
}


@lru_cache(maxsize=1)
def load_cases() -> list[dict]:
    """Load cases from data/cases.jsonl.

    每行一个 JSON。空行跳过；坏行直接跳过，避免一个手写案例破坏整个 Agent。
    """
    if not os.path.exists(CASES_PATH):
        return []

    cases = []
    with open(CASES_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                case = json.loads(line)
            except json.JSONDecodeError:
                continue

            if case.get("symptom") or case.get("solution"):
                cases.append(case)

    return cases


def _case_text(case: dict) -> str:
    parts = []
    for field in CASE_FIELDS:
        value = case.get(field, "")
        if isinstance(value, list):
            parts.extend(str(item) for item in value)
        else:
            parts.append(str(value))
    return " ".join(parts).lower()


def _query_terms(query: str) -> set[str]:
    text = query.lower()
    terms = set(re.findall(r"[a-zA-Z0-9_+-]+|[\u4e00-\u9fff]{2,}", text))

    for aliases in ALIASES.values():
        if any(alias.lower() in text for alias in aliases):
            terms.update(alias.lower() for alias in aliases)

    return {term for term in terms if term.strip()}


def _score_case(query: str, case: dict) -> int:
    text = _case_text(case)
    terms = _query_terms(query)
    score = 0

    for term in terms:
        if term in text:
            score += 2 if len(term) >= 3 else 1

    query_lower = query.lower()
    # ADB 连接类问题的强特征组合：同时提到 adb/设备/识别问题时，提高案例优先级。
    if any(k in query_lower for k in ["adb", "电脑", "usb"]) and any(
        k in query_lower for k in ["查不到", "看不到", "识别不到", "没有设备", "连不上", "device"]
    ):
        if "adb" in text and ("开发者模式" in text or "debugging" in text):
            score += 8

    return score


def search_cases(query: str, top_k: int = 3) -> list[dict]:
    """Search support cases by query and return the best matches."""
    scored = []
    for case in load_cases():
        score = _score_case(query, case)
        if score > 0:
            scored.append((score, case))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [case for _, case in scored[:top_k]]


def build_cases_context(cases: list[dict]) -> str:
    """Render matched cases into prompt context."""
    if not cases:
        return ""

    parts = ["【历史支持案例（来自 FAE cases.jsonl，可作为排查经验参考）】"]
    for i, case in enumerate(cases, 1):
        tags = ", ".join(case.get("tags", []))
        parts.append(
            f"[案例{i}] {case.get('module', 'unknown')}\n"
            f"现象: {case.get('symptom', '')}\n"
            f"原因: {case.get('root_cause', '')}\n"
            f"处理: {case.get('solution', '')}\n"
            f"标签: {tags}\n"
        )

    return "\n".join(parts) + "\n"
