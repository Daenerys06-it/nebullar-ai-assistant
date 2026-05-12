---
name: feedback_cases_workflow
description: User wants to dictate FAE cases conversationally and have me append to cases.jsonl
type: feedback
---

用户不想手动编辑 cases.jsonl，偏好对话式录入：在终端口述案例内容（产品、日期、现象、原因、解决方案、耗时），由我追加到 cases.jsonl 文件。

**Why**: 效率更高，FAE 日常工作已经够忙，手写 JSON 容易出错。

**How to apply**: 用户描述案例时，主动提取 structured fields，格式化为单行 JSON append 到 data/cases.jsonl。格式：
```json
{"product": "financial_sdk|terminal_manager_sdk", "module": "模块名", "date": "YYYY-MM-DD", "symptom": "客户描述", "root_cause": "根因", "solution": "解决方案", "time_cost_min": 数字, "tags": ["标签"]}
```
