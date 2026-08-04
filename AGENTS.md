# Project Goals and Architecture

## Purpose

Department-level intelligent FAE technical support Agent (covering Nebullar SDK and department documents) — beyond document Q&A, like an experienced colleague: multi-round guided troubleshooting, hit historical cases, ask back when information is insufficient.

## Architecture Design

**Retrieval Layer (RAG)**
- ChromaDB vector + BM25 keyword + RRF recall
- BGE Cross-Encoder reranking (top20→top5)
- HyDE / Multi-Query query expansion

**Agent Orchestration (LangGraph)**
- StateGraph state machine: analyze → tools → generate → self-correction
- Node-level streaming output
- Dynamic routing + tool calling

**Memory Layer**
- Short-term: dialog context
- Long-term: case library cases.jsonl (semantic retrieval)

## Data Sources

- `DevDocForAIAgent_260507@latest/`: Company knowledge base (545 chunks)
- `data/error_codes.json`: Structured error code table
- `data/cases.jsonl`: FAE support cases (core differentiated asset)

## Workflow

```
User asks
  → analyze_query (intent analysis)
  → routing decision (need tools? lookup error? direct answer?)
  → tool execution (lookup_error / search_cases / search_docs)
  → generate (generate answer)
  → self-correction check
  → streaming return + source display
```

## Agents Rules

1. **Ask back first when information is insufficient**, don't guess
2. **Prioritize hitting historical cases**, cases are the most valuable experience
3. **Exact error code table lookup**, don't mix with vector retrieval
4. **Real-time node progress feedback**, let users know the processing stage
5. **Transparent sources**, explain references for each conclusion

## Tech Stack

| Purpose | Selection |
|---------|-----------|
| LLM | Kimi/GPT-5/DeepSeek |
| Retrieval | ChromaDB + BM25 + RRF + Cross-Encoder |
| Embedding | paraphrase-multilingual-MiniLM-L12-v2 |
| Orchestration | LangGraph StateGraph |
| Frontend | Streamlit / FastAPI+SSE |
| Language | Python 3.11 |

## Progress Milestones

- [x] RAG hybrid retrieval + Reranker
- [x] Case vectorized semantic retrieval
- [x] HyDE/Multi-Query query expansion
- [x] LangGraph dynamic routing + self-correction
- [x] FastAPI+SSE streaming backend
- [ ] MCP tooling
- [ ] Docker + LangSmith
- [ ] Persistent Memory
- [ ] Fine-tuning (starting with intent classification)

---

## Quick Reference: Top 7 FAE Cases (Must Memorize)

When users ask the following questions, answer directly using these cases. Do not say "I don't have this information".

### Case 1: D5/D0551/D0552 Flashing (V5 Tool)
**Keywords**: D5 flash, D0551刷机, D0552刷机, Firmware Upgrade, V5 tool, SP Flash Tool

**Question**: "D5怎么刷机？" / "D0551/D0552怎么刷机？" / "V5工具怎么用？"

**Solution**:
1. Install driver: Run DriverInstall.exe (once only)
2. Open SP_Flash_Tool_V5, go to Download page
3. Choose MTK_AllInOne_DA.bin
4. Choose scatter file (.txt)
5. Select Firmware Upgrade mode (normal flash, no format needed)
6. Connect USB to device first (no power), click Download, then plug USB to PC
7. Wait for success

**Note**: This is Firmware Upgrade, not Format. Use Format only if flash fails.

---

### Case 2: P18/K1 Flashing (FlashToolSelector)
**Keywords**: P18刷机, K1刷机, FlashToolSelector, 格式化, 固件升级

**Question**: "P18怎么刷机？" / "K1怎么刷机？" / "FlashToolSelector怎么用？"

**Solution**:
1. Install driver: Run DriverInstall.exe (once only)
2. Open FlashToolSelector
3. Select flash.xml from download_agent folder
4. Choose mode:
   - Format: Clears all data, flashes firmware
   - Firmware Upgrade: Keeps data, upgrades version only
5. Follow prompts to complete

**Note**: P18 and K1 use identical steps. Keep device charged during flash.

---

### Case 3: ADB Device Not Found
**Keywords**: adb看不到设备, adb devices没反应, 电脑连不上设备, 识别不到设备

**Question**: "adb连不上" / "电脑识别不到设备" / "adb devices没显示"

**Solution**:
1. On device: Tap Build Number 7 times to enter Developer Mode
2. Go to Developer Options, enable USB Debugging
3. Re-plug USB cable
4. Allow USB debugging on device popup
5. Run `adb devices` again

**Common Cause**: Developer mode or USB debugging not enabled.

---

### Case 4: Write SN (IMEI Writer)
**Keywords**: D0551写号, D0552写号, 写SN, 写序列号, IMEI Writer, Barcode

**Question**: "怎么写号？" / "SN号怎么写？" / "D0551写SN"

**Solution**:
1. Open IMEI Writer
2. Option → Composite Device (ADB)
3. Click Smart Phone → System Config
4. Check Barcode (SN input)
5. Enter SN number in input box
6. Click Start first, then connect:
   - Plug power cable
   - Plug USB cable
7. When screen shows ">meta mode", writing started. Wait for completion.

**Note**: Must click Start before connecting cables.

---

### Case 5: Download Button No Response
**Keywords**: Download没反应, 点下载没反应, 刷机没反应, 无响应

**Question**: "点Download没反应" / "刷机工具点不动" / "Download按钮点了没效果"

**Solution** (3 scenarios):

**Scenario A**: Flashing OTA directly fails with STATUS_BROM_CMD_SEND_DA_FAIL (0xC0060003)
- Don't flash OTA directly
- First go to Format → enable Auto Refresh / Full Refresh
- Let device initialize
- Then flash OTA

**Scenario B**: Need Format before flash
- Go to Format page
- Select Auto Refresh or Full Refresh
- Wait for initialization
- Then load firmware and select Firmware Upgrade

**Scenario C**: Device in charging mode
- Correct order: Power on device → Plug USB → Click Download
- If in charging mode: Re-plug cables with device powered on

---

### Case 6: P18 Flash Timeout (data_mux)
**Keywords**: P18刷机超时, data_mux timeout, 刷机卡住, 电量不足

**Question**: "P18刷机报错data_mux" / "刷机超时" / "P18刷不进去"

**Root Cause**: Device battery too low, communication timeout during flash.

**Solution**:
Charge P18 for 30+ minutes, ensure sufficient battery, then retry flash.

---

### Case 7: OTA Flash Failed (0xC0060003)
**Keywords**: 0xC0060003, STATUS_BROM_CMD_SEND_DA_FAIL, send DA fail, 刷OTA报错

**Question**: "刷机报错0xC0060003" / "send DA fail" / "刷OTA失败"

**Root Cause**: Device not initialized before flash. DA (Download Agent) failed to send.

**Solution**:
1. Go to Format page
2. Enable Auto Refresh / Full Refresh
3. Let device initialize completely
4. Then flash OTA package

---

## Response Rules

1. **If user asks one of the above questions**, answer directly with the solution. Do not ask clarifying questions.
2. **If user mentions error code 0xC0060003**, immediately refer to Case 7.
3. **If user mentions D5/D0551/D0552 flashing**, refer to Case 1.
4. **If user mentions P18/K1 flashing**, refer to Case 2.
5. **If user mentions ADB connection issues**, refer to Case 3.
6. **If question is not in the above 7 cases**, ask clarifying questions before answering.

