"""智能文档切分策略：结构感知 + 语义切分 + 元数据增强"""

import re
from typing import Iterator
from dataclasses import dataclass


@dataclass
class Chunk:
    """文档块，包含内容和丰富的元数据"""
    content: str
    source: str  # 来源文件
    product: str  # 产品名
    module: str  # 模块名
    headers: list[str]  # 标题层级 [H1, H2, H3...]
    chunk_type: str  # 类型: text, code, table
    start_line: int  # 在原文中的起始行
    end_line: int  # 在原文中的结束行


class MarkdownChunker:
    """Markdown文档智能切分器

    策略：
    1. 按标题层级识别文档结构
    2. 保护代码块、表格的完整性
    3. 在结构块内部按语义长度二次切分
    4. 附加丰富的元数据（标题层级、类型标记）
    """

    def __init__(
        self,
        chunk_size: int = 512,
        chunk_overlap: int = 50,
        max_code_lines: int = 100,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.max_code_lines = max_code_lines

        # 正则：识别Markdown元素
        self.header_pattern = re.compile(r'^(#{1,6})\s+(.+)$')
        self.code_fence_pattern = re.compile(r'^```(\w*)')
        self.table_row_pattern = re.compile(r'^\|.*\|$')

    def _identify_block_type(self, lines: list[str]) -> str:
        """识别文本块类型"""
        content = '\n'.join(lines).strip()

        # 检查是否是代码块
        if content.startswith('```') and content.endswith('```'):
            return 'code'

        # 检查是否是表格（多行管道符格式）
        table_lines = [l for l in lines if l.strip().startswith('|')]
        if len(table_lines) >= 2 and len(table_lines) / len(lines) > 0.5:
            return 'table'

        return 'text'

    def _extract_headers(self, text: str) -> list[str]:
        """提取文档中的所有标题层级"""
        headers = []
        for line in text.split('\n'):
            match = self.header_pattern.match(line.strip())
            if match:
                level = len(match.group(1))
                title = match.group(2).strip()
                # 确保列表长度等于标题层级
                while len(headers) < level - 1:
                    headers.append('')
                headers = headers[:level-1] + [title]
        return headers

    def _get_current_headers(self, lines: list[str], line_idx: int) -> list[str]:
        """获取指定行号处的当前标题上下文"""
        headers = []
        for i, line in enumerate(lines[:line_idx+1]):
            match = self.header_pattern.match(line.strip())
            if match:
                level = len(match.group(1))
                title = match.group(2).strip()
                while len(headers) < level - 1:
                    headers.append('')
                headers = headers[:level-1] + [title]
        return headers

    def _is_header_line(self, line: str) -> bool:
        """判断是否是标题行"""
        return bool(self.header_pattern.match(line.strip()))

    def _is_code_fence(self, line: str) -> tuple[bool, str]:
        """判断是否是代码块标记，返回(是否匹配, 语言)"""
        match = self.code_fence_pattern.match(line.strip())
        if match:
            return True, match.group(1)
        return False, ''

    def _split_by_structure(self, text: str) -> Iterator[tuple[list[str], dict]]:
        """第一级：按文档结构切分

        返回: (行列表, 元数据字典)
        """
        lines = text.split('\n')
        current_block: list[str] = []
        current_meta = {'type': 'text', 'start_line': 0}
        in_code_block = False
        code_lang = ''

        for i, line in enumerate(lines):
            # 检测代码块边界
            is_fence, lang = self._is_code_fence(line)
            if is_fence:
                if not in_code_block:
                    # 代码块开始，先结束当前文本块
                    if current_block:
                        yield current_block, current_meta
                        current_block = []
                    in_code_block = True
                    code_lang = lang
                    current_meta = {
                        'type': 'code',
                        'start_line': i,
                        'code_lang': code_lang
                    }
                    current_block.append(line)
                else:
                    # 代码块结束
                    current_block.append(line)
                    yield current_block, current_meta
                    current_block = []
                    in_code_block = False
                    code_lang = ''
                    current_meta = {'type': 'text', 'start_line': i + 1}
                continue

            # 在代码块内，整段保留
            if in_code_block:
                current_block.append(line)
                # 防止代码块过长
                if len(current_block) > self.max_code_lines:
                    yield current_block, current_meta
                    current_block = []
                    in_code_block = False
                    current_meta = {'type': 'text', 'start_line': i + 1}
                continue

            # 检测标题（结构边界）
            if self._is_header_line(line) and current_block:
                # 遇到新标题，结束当前块
                yield current_block, current_meta
                current_block = [line]
                current_meta = {'type': 'text', 'start_line': i}
                continue

            # 普通文本行
            current_block.append(line)

        # 处理最后一块
        if current_block:
            yield current_block, current_meta

    def _split_semantic(
        self,
        lines: list[str],
        meta: dict,
        headers: list[str],
        source: str,
        product: str,
        module: str
    ) -> Iterator[Chunk]:
        """第二级：在结构块内部按语义长度切分"""

        content = '\n'.join(lines).strip()
        if not content:
            return

        # 代码块和短文本不二次切分
        block_type = meta.get('type', 'text')
        if block_type == 'code' or len(content) <= self.chunk_size:
            yield Chunk(
                content=content,
                source=source,
                product=product,
                module=module,
                headers=headers,
                chunk_type=block_type,
                start_line=meta['start_line'],
                end_line=meta['start_line'] + len(lines)
            )
            return

        # 文本块按段落/句子切分
        paragraphs = content.split('\n\n')
        current_chunk: list[str] = []
        current_len = 0
        chunk_start_line = meta['start_line']
        line_counter = meta['start_line']

        for para in paragraphs:
            para_lines = para.split('\n')
            para_len = len(para)

            # 如果当前段落加上已有内容超长了，先输出当前块
            if current_chunk and current_len + para_len > self.chunk_size:
                yield Chunk(
                    content='\n\n'.join(current_chunk).strip(),
                    source=source,
                    product=product,
                    module=module,
                    headers=headers,
                    chunk_type='text',
                    start_line=chunk_start_line,
                    end_line=line_counter
                )
                # 保留overlap（最后一段或最后50字符）
                overlap_text = current_chunk[-1][-self.chunk_overlap:] if current_chunk else ''
                current_chunk = [overlap_text] if overlap_text else []
                current_len = len(overlap_text)
                chunk_start_line = line_counter

            current_chunk.append(para)
            current_len += para_len + 2  # +2 for '\n\n'
            line_counter += len(para_lines)

        # 输出最后一块
        if current_chunk:
            yield Chunk(
                content='\n\n'.join(current_chunk).strip(),
                source=source,
                product=product,
                module=module,
                headers=headers,
                chunk_type='text',
                start_line=chunk_start_line,
                end_line=meta['start_line'] + len(lines)
            )

    def chunk_document(
        self,
        text: str,
        source: str,
        product: str,
        module: str
    ) -> list[Chunk]:
        """主入口：切分单个文档"""
        chunks: list[Chunk] = []

        for block_lines, meta in self._split_by_structure(text):
            if not block_lines:
                continue

            # 获取该块开始位置的标题上下文
            headers = self._get_current_headers(text.split('\n'), meta['start_line'])

            # 在结构块内部做语义切分
            for chunk in self._split_semantic(
                block_lines, meta, headers, source, product, module
            ):
                chunks.append(chunk)

        return chunks

    def chunk_with_enhanced_metadata(self, chunk: Chunk) -> dict:
        """将Chunk转换为带增强元数据的字典（用于存入向量库）"""
        # 构建标题路径
        header_path = ' > '.join(h for h in chunk.headers if h) or 'Root'

        # 构建增强内容（标题前缀 + 原文）
        enhanced_content = chunk.content
        if chunk.headers:
            # 在内容前加上标题上下文，帮助检索
            header_context = ' | '.join(h for h in chunk.headers if h)
            enhanced_content = f"[{header_context}]\n{chunk.content}"

        # ChromaDB 不支持空列表作为metadata值，需要转换
        headers_for_meta = chunk.headers if chunk.headers else ['']

        return {
            'content': enhanced_content,  # 增强后的内容用于embedding
            'original_content': chunk.content,  # 原始内容
            'metadata': {
                'source': chunk.source,
                'product': chunk.product,
                'module': chunk.module,
                'headers': headers_for_meta,
                'header_path': header_path,
                'chunk_type': chunk.chunk_type,
                'start_line': chunk.start_line,
                'end_line': chunk.end_line,
            }
        }


class RecursiveFallbackChunker:
    """降级切分器：当Markdown结构识别失败时使用

    保留原有的RecursiveCharacterTextSplitter行为，
    但添加基础的元数据支持。
    """

    def __init__(self, chunk_size: int = 800, chunk_overlap: int = 80):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        # 分隔符优先级：段落 > 句子 > 单词 > 字符
        self.separators = ["\n\n", "\n", ". ", "  ", " ", ""]

    def chunk_document(
        self,
        text: str,
        source: str,
        product: str,
        module: str
    ) -> list[Chunk]:
        """使用递归字符切分"""
        chunks = []
        start = 0
        line_num = 0

        while start < len(text):
            # 找到合适的切分点
            end = start + self.chunk_size
            if end >= len(text):
                chunk_text = text[start:]
            else:
                # 寻找最佳切分位置
                chunk_text = text[start:end]
                for sep in self.separators:
                    last_sep = chunk_text.rfind(sep, self.chunk_size - self.chunk_overlap)
                    if last_sep != -1:
                        chunk_text = chunk_text[:last_sep + len(sep)]
                        break

            lines = chunk_text.split('\n')
            chunks.append(Chunk(
                content=chunk_text.strip(),
                source=source,
                product=product,
                module=module,
                headers=[''],  # 降级切分器无法提取标题，用 [''] 避免 ChromaDB 报错
                chunk_type='text',
                start_line=line_num,
                end_line=line_num + len(lines)
            ))

            # 计算下一起始位置（考虑overlap）
            advance = len(chunk_text)
            if advance <= self.chunk_overlap:
                advance = len(chunk_text)  # 防止死循环
            start += advance - self.chunk_overlap if end < len(text) else advance
            line_num += len(lines)

        return chunks


def create_chunker(strategy: str = "markdown", **kwargs) -> MarkdownChunker | RecursiveFallbackChunker:
    """工厂函数：创建切分器"""
    if strategy == "markdown":
        return MarkdownChunker(**kwargs)
    elif strategy == "recursive":
        return RecursiveFallbackChunker(**kwargs)
    else:
        raise ValueError(f"Unknown chunking strategy: {strategy}")
