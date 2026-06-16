"""Small regression evals for the Nebullar Agent.

These tests focus on deterministic behavior and mock the LLM call where needed.
They are meant to catch regressions in routing, tools, and structured metadata.
"""

import os
import sys
import unittest
from unittest.mock import patch


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

import agent  # noqa: E402
from memory import search_cases  # noqa: E402


class AgentEvalTest(unittest.TestCase):
    def test_lookup_error_70004(self):
        hit = agent.lookup_error("-70004")

        self.assertIsNotNone(hit)
        self.assertEqual(hit["meaning"], "APDU Error")
        self.assertEqual(hit["category"], "cardreader")

    def test_vague_card_question_clarifies_first(self):
        result = agent.ask_structured("刷卡无反应怎么办")

        self.assertTrue(result["needs_clarification"])
        self.assertIn("analyze_query", result["tools_used"])
        self.assertIn("是哪种卡", result["answer"])
        self.assertEqual(result["sources"], [])

    def test_adb_case_is_retrievable(self):
        hits = search_cases("adb devices 查不到设备怎么办")

        self.assertGreaterEqual(len(hits), 1)
        self.assertIn("开发者模式", hits[0]["root_cause"])
        self.assertIn("debugging", hits[0]["solution"].lower())

    def test_structured_answer_contains_tools_and_sources(self):
        fake_docs = [
            {
                "content": "APDU Error means the APDU exchange failed. Check card power-on and APDU command.",
                "module": "financial_cardreader",
                "product": "financial",
                "rrf_score": 0.03,
            }
        ]

        with patch.object(agent, "search", return_value=fake_docs), patch.object(
            agent,
            "complete",
            return_value="结论：-70004 是 APDU Error，先检查卡片上电和 APDU 指令。",
        ):
            result = agent.ask_structured("刷卡返回 -70004 怎么排查？")

        self.assertFalse(result["needs_clarification"])
        self.assertIn("lookup_error", result["tools_used"])
        self.assertIn("search_docs", result["tools_used"])
        self.assertEqual(result["error"]["meaning"], "APDU Error")
        self.assertEqual(result["sources"][0]["module"], "financial_cardreader")
        self.assertIn("APDU Error", result["answer"])


if __name__ == "__main__":
    unittest.main()
