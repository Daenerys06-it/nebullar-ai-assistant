"""验证 ChromaDB 全局复用 + Reranker 缓存优化效果"""
import os
import sys
import time

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("LLM_PROVIDER", "kimi")

sys.path.insert(0, "src")

print("=" * 60)
print("优化验证：ChromaDB复用 + Reranker缓存")
print("=" * 60)

from retrieve import (
    preload_all_models, search, vector_search, keyword_search,
    get_cache_stats, clear_search_cache
)

# 1. 先预加载（模拟app启动时）
print("\n[Step 1] 预加载模型...")
t0 = time.time()
preload_all_models()
print(f"预加载耗时: {time.time()-t0:.2f}s")

# 2. 第一次查询（冷）
print("\n[Step 2] 第一次查询（冷）...")
query = "D0551怎么刷机"
t0 = time.time()
results1 = search(query, top_k=5)
t1 = time.time()
print(f"第一次查询耗时: {t1-t0:.2f}s")
print(f"返回结果: {len(results1)} 条")
print(f"缓存状态: {get_cache_stats()}")

# 3. 第二次查询（热）- 相同query
print("\n[Step 3] 第二次查询（相同query，应该全缓存命中）...")
t0 = time.time()
results2 = search(query, top_k=5)
t1 = time.time()
print(f"第二次查询耗时: {t1-t0:.2f}s")
print(f"缓存状态: {get_cache_stats()}")

# 4. 第三次查询 - 不同query但相似（测试扩展查询）
print("\n[Step 4] 第三次查询（不同query：'P18刷不进去'）...")
t0 = time.time()
results3 = search("P18刷不进去", top_k=5)
t1 = time.time()
print(f"第三次查询耗时: {t1-t0:.2f}s")
print(f"缓存状态: {get_cache_stats()}")

# 5. 第四次查询 - 重复第三次
print("\n[Step 5] 第四次查询（重复'P18刷不进去'，应该缓存命中）...")
t0 = time.time()
results4 = search("P18刷不进去", top_k=5)
t1 = time.time()
print(f"第四次查询耗时: {t1-t0:.2f}s")
print(f"缓存状态: {get_cache_stats()}")

print("\n" + "=" * 60)
print("总结:")
print("=" * 60)
print("""
优化前问题:
- ChromaDB每次新建client: 10s+
- Reranker无缓存: 每次重新精排 ~15s

优化后预期:
- 预加载后，单次查询应在 0.5-2s 内
- 缓存命中时，应在 50ms 内

如果第二次/第四次查询耗时 < 1s，说明优化成功！
""")