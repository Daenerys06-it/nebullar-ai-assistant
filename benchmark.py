"""性能测试脚本 - 定位响应时间瓶颈"""

import os
import sys
import time

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("LLM_PROVIDER", "kimi")

sys.path.insert(0, "src")

print("=" * 60)
print("Nebullar AI Assistant - 性能测试")
print("=" * 60)

# 1. 测试检索层（不含LLM）
print("\n[Test 1] 检索层性能（不含LLM）")
print("-" * 60)

from retrieve import search, vector_search, keyword_search, reciprocal_rank_fusion

query = "D0551怎么刷机"

# 向量检索
t0 = time.time()
vec_results = vector_search(query, top_k=20)
t1 = time.time()
print(f"  向量检索: {(t1-t0)*1000:.1f}ms, 返回 {len(vec_results)} 条")

# 关键词检索
t0 = time.time()
key_results = keyword_search(query, top_k=20)
t1 = time.time()
print(f"  BM25检索: {(t1-t0)*1000:.1f}ms, 返回 {len(key_results)} 条")

# RRF融合
t0 = time.time()
merged = reciprocal_rank_fusion(vec_results, key_results)
t1 = time.time()
print(f"  RRF融合:  {(t1-t0)*1000:.1f}ms, 合并后 {len(merged)} 条")

# 完整检索（含精排）
t0 = time.time()
final_results = search(query, top_k=5)
t1 = time.time()
print(f"  完整检索（含精排）: {(t1-t0)*1000:.1f}ms")

# 2. 测试案例检索
print("\n[Test 2] 案例检索性能")
print("-" * 60)

from memory import search_cases

t0 = time.time()
cases = search_cases("P18刷机超时", top_k=3)
t1 = time.time()
print(f"  案例检索: {(t1-t0)*1000:.1f}ms, 返回 {len(cases)} 条")

# 3. 测试LLM调用
print("\n[Test 3] LLM调用性能")
print("-" * 60)

from llm import create_client, complete

try:
    client, model = create_client("kimi")
    print(f"  使用模型: {model}")

    # 简单生成测试
    system = "你是技术助手，简短回答。"
    prompt = "D0551怎么刷机？简要步骤"

    print(f"  测试生成: '{prompt[:30]}...'")
    t0 = time.time()
    response = complete(client, model, system, prompt, max_tokens=200)
    t1 = time.time()

    print(f"  LLM生成时间: {t1-t0:.2f}s")
    print(f"  生成长度: {len(response)} 字符")
    print(f"  首token延迟: 约{t1-t0:.2f}s (非流式)")

except Exception as e:
    print(f"  [ERROR] LLM调用失败: {e}")

# 4. 模拟完整Agent流程
print("\n[Test 4] 模拟完整Agent流程")
print("-" * 60)

start = time.time()

# 4.1 意图分析（模拟）
t0 = time.time()
print("  1. 意图分析...", end=" ")
time.sleep(0.1)  # 模拟
print(f"{(time.time()-t0)*1000:.1f}ms")

# 4.2 检索
t0 = time.time()
print("  2. 文档检索...", end=" ")
results = search("D0551刷机", top_k=5)
print(f"{(time.time()-t0)*1000:.1f}ms")

# 4.3 案例检索
t0 = time.time()
print("  3. 案例检索...", end=" ")
cases = search_cases("D0551刷机", top_k=2)
print(f"{(time.time()-t0)*1000:.1f}ms")

# 4.4 LLM生成
t0 = time.time()
print("  4. LLM生成...", end=" ")
try:
    resp = complete(client, model, "你是FAE助手", "根据资料回答D0551刷机步骤", max_tokens=300)
    print(f"{(time.time()-t0)*1000:.1f}ms")
except:
    print("失败")

total = time.time() - start
print(f"\n  总计: {total:.2f}s")

print("\n" + "=" * 60)
print("性能分析建议:")
print("=" * 60)
print("""
正常应该看到:
  - 向量检索: <300ms
  - BM25检索: <200ms
  - RRF融合:  <50ms
  - 精排:      ~500ms
  - 案例检索: <100ms
  - LLM生成:  2-5s (取决于生成长度)
  - 总计:      3-8s

如果看到:
  - LLM生成 >10s: 可能是网关延迟或模型负载高
  - 检索 >2s: 可能是ChromaDB首次加载或缓存未命中
  - 总计 >30s: 检查是否有重复调用或阻塞操作
""")