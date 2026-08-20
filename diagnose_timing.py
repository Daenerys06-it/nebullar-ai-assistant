"""诊断Agent各环节耗时"""
import os
import sys
import time

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("LLM_PROVIDER", "kimi")

sys.path.insert(0, "src")

from retrieve import (
    preload_all_models, search, expand_query_rules,
    vector_search, keyword_search, reciprocal_rank_fusion, rerank
)
from memory import search_cases, preload_models

# 预加载
print("[1] 预加载模型...")
t0 = time.time()
preload_models()
preload_all_models()
print(f"    预加载: {time.time()-t0:.2f}s")

# 测试查询
query = "D0551怎么刷机"

print(f"\n[2] 查询扩展...")
t0 = time.time()
queries = expand_query_rules(query)
print(f"    扩展耗时: {time.time()-t0:.4f}s")
print(f"    扩展为 {len(queries)} 个query: {queries}")

print(f"\n[3] 逐个query检索（这就是瓶颈！）...")
all_vec = []
all_key = []
for i, q in enumerate(queries):
    print(f"    Query {i+1}: '{q[:30]}...'")

    t0 = time.time()
    v = vector_search(q, top_k=10)
    t1 = time.time()
    print(f"      向量检索: {t1-t0:.2f}s")
    all_vec.append((q, v, t1-t0))

    t0 = time.time()
    k = keyword_search(q, top_k=10)
    t1 = time.time()
    print(f"      BM25检索: {t1-t0:.2f}s")
    all_key.append((q, k, t1-t0))

print(f"\n[4] RRF融合...")
t0 = time.time()
for q, v, _ in all_vec:
    for qq, k, _ in all_key:
        if q == qq:
            merged = reciprocal_rank_fusion(v, k)
            break
print(f"    RRF耗时: {time.time()-t0:.4f}s")

print(f"\n[5] 完整search()调用...")
t0 = time.time()
results = search(query, top_k=5)
print(f"    总耗时: {time.time()-t0:.2f}s")

print(f"\n[6] 案例检索...")
t0 = time.time()
cases = search_cases(query, top_k=3)
print(f"    案例检索: {time.time()-t0:.2f}s")

print("\n" + "="*60)
print("诊断结论:")
print("="*60)
total_search = sum(t for _, _, t in all_vec) + sum(t for _, _, t in all_key)
print(f"5个query × (向量+BM25) = {total_search:.2f}s 串行检索")
print(f"这就是127秒的元凶！")
print()
print("优化方案:")
print("1. 限制扩展数量: max 3个变体")
print("2. 并行检索: 用async/线程池同时跑多个query")
print("3. 首次查询不扩展，用户确认后再深度检索")