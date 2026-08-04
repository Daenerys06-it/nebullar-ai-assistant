"""测试新的Chunking策略和MCP工具"""

import os
import sys

# 设置离线模式
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE, "src"))

from chunking import create_chunker, MarkdownChunker


def test_chunking():
    """测试智能Chunking"""
    print("=" * 60)
    print("测试1: Markdown Chunking 策略")
    print("=" * 60)

    sample_doc = """# Nebullar Financial SDK

## 1. Overview
This SDK provides payment processing capabilities for financial terminals.

## 2. Scanner Operation

### 2.1 Initialize Scanner
To initialize the scanner, call the following API:

```java
Scanner scanner = new Scanner(context);
scanner.init();
```

Parameters:
- context: Application context
- callback: ScannerCallback instance

### 2.2 Start Scanning
Begin scanning with startScan() method.

## 3. Error Handling
Common error codes:
| Error Code | Description | Solution |
|------------|-------------|----------|
| ERR_TIMEOUT | Scan timeout | Check hardware |
| ERR_CANCELLED | User cancelled | Retry |

## 4. Advanced Topics
More content here...
"""

    chunker = create_chunker(strategy="markdown", chunk_size=300, chunk_overlap=30)
    chunks = chunker.chunk_document(
        text=sample_doc,
        source="test.md",
        product="financial_sdk",
        module="test"
    )

    print(f"\n生成 {len(chunks)} 个 chunks:\n")
    for i, chunk in enumerate(chunks, 1):
        print(f"--- Chunk {i} [{chunk.chunk_type}] ---")
        print(f"Headers: {' > '.join(h for h in chunk.headers if h)}")
        print(f"Lines: {chunk.start_line}-{chunk.end_line}")
        preview = chunk.content[:150].replace('\n', ' ')
        print(f"Content: {preview}...")
        print()

    return len(chunks)


def test_enhanced_metadata():
    """测试增强元数据"""
    print("=" * 60)
    print("测试2: 增强元数据")
    print("=" * 60)

    chunker = MarkdownChunker()
    chunk = chunker.chunk_document(
        text="# API Guide\n\n## Scanner\n\nInitialize with init()",
        source="api.md",
        product="test",
        module="guide"
    )[0]

    enhanced = chunker.chunk_with_enhanced_metadata(chunk)

    print("\n增强后的数据结构:")
    print(f"  content (用于embedding): {enhanced['content'][:80]}...")
    print(f"  metadata:")
    for k, v in enhanced['metadata'].items():
        print(f"    {k}: {v}")


def compare_chunking_strategies():
    """对比两种切分策略"""
    print("=" * 60)
    print("测试3: 策略对比")
    print("=" * 60)

    # 一个包含代码和段落的文档
    doc = """# 刷机指南

## 步骤1: 准备环境
首先安装驱动程序。

## 步骤2: 连接设备
使用USB线连接设备。

```bash
adb devices
```

## 步骤3: 执行刷机
运行刷机命令。

更多说明文字...
可以很长很长...
"""

    print("\nMarkdown策略:")
    md_chunker = create_chunker("markdown")
    md_chunks = md_chunker.chunk_document(doc, "test.md", "product", "module")
    print(f"  生成 {len(md_chunks)} chunks")
    for c in md_chunks:
        print(f"    - {c.chunk_type}: {len(c.content)} chars")

    print("\nRecursive策略:")
    rec_chunker = create_chunker("recursive", chunk_size=100, chunk_overlap=20)
    rec_chunks = rec_chunker.chunk_document(doc, "test.md", "product", "module")
    print(f"  生成 {len(rec_chunks)} chunks")
    for c in rec_chunks[:3]:  # 只显示前3个
        print(f"    - {c.chunk_type}: {len(c.content)} chars")


def test_ingest_preview():
    """预览 ingest.py 的效果"""
    print("=" * 60)
    print("测试4: 文档入库预览")
    print("=" * 60)

    # 模拟一个SDK文档
    sdk_doc = """# Scanner Module

## Overview
The Scanner module provides barcode scanning functionality.

## API Reference

### init()
Initialize the scanner.

Parameters:
- context: Context

Returns:
- boolean: success

### startScan()
Start scanning operation.

Code example:
```java
Scanner scanner = new Scanner(context);
scanner.init();
scanner.startScan();
```

## Error Codes
| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Error |
"""

    chunker = create_chunker("markdown", chunk_size=400)
    chunks = chunker.chunk_document(sdk_doc, "scanner.md", "financial_sdk", "scanner")

    print(f"\n模拟 financial_sdk/scanner.md 切分结果:")
    print(f"  总 chunks: {len(chunks)}")

    type_counts = {}
    for c in chunks:
        type_counts[c.chunk_type] = type_counts.get(c.chunk_type, 0) + 1
    print(f"  类型分布: {type_counts}")

    # 显示一个chunk的完整元数据
    if chunks:
        c = chunks[0]
        enhanced = chunker.chunk_with_enhanced_metadata(c)
        print(f"\n  示例 Chunk 元数据:")
        for k, v in enhanced['metadata'].items():
            print(f"    {k}: {v}")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Nebullar 智能 Chunking 测试")
    print("=" * 60 + "\n")

    try:
        test_chunking()
        test_enhanced_metadata()
        compare_chunking_strategies()
        test_ingest_preview()

        print("\n" + "=" * 60)
        print("✅ 所有测试通过!")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
