"""Parse extracted PDF text files into structured markdown by module."""
import re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")

# ── Financial SDK 模块切割表 ──────────────────────────────────────
# key=输出文件名, value=(原文起始标题, 原文结束标题)
# 原理：在 PDF 导出的 txt 里找到这些标题对应的行号，切出中间内容
FIN_SECTIONS = {
    "01_overview": ("2. Overview", "3. API Interface Introduction"),
    "02_scanner_basic": ("3.2 Scanner Operation module", "3.3 Card Reader Operation module"),
    "03_cardreader": ("3.3 Card Reader Operation module", "3.4 EMV Operation module"),
    "04_emv": ("3.4 EMV Operation module", "3.5 General Operation function"),
    "05_general": ("3.5 General Operation function", "3.6 PINPAD Operation module"),
    "06_pinpad": ("3.6 PINPAD Operation module", "3.7 Printing Operation module"),
    "07_printer": ("3.7 Printing Operation module", "3.8 Security module"),
    "08_security": ("3.8 Security module", "3.9 ECR module"),
    "09_ecr": ("3.9 ECR module", "3.10 Scanner module"),
    "10_scanner_advanced": ("3.10 Scanner module", "4. Error Code Definition"),
    "11_error_codes": ("4. Error Code Definition", "5. Entity Class Definition"),
    "12_entities": ("5. Entity Class Definition", "6. Access permission"),
    "13_permissions": ("6. Access permission", None),  # None = 直接取到文件末尾
}

# ── Terminal Manager SDK 模块切割表 ───────────────────────────────
TM_SECTIONS = {
    "01_overview": ("2. Overview", "3. API Interface Introduction"),
    "02_certification": ("3.2 Certification module", "3.3 Device information module"),
    "03_device_info": ("3.3 Device information module", "3.4 Device module"),
    "04_device": ("3.4 Device module", "3.5 Location module"),
    "05_location": ("3.5 Location module", "3.6 Network Management module"),
    "06_network": ("3.6 Network Management module", "3.7 Resource Management module"),
    "07_resource": ("3.7 Resource Management module", "4. Error Code Definition"),
    "08_error_codes": ("4. Error Code Definition", "5. Entity Class Definition"),
    "09_entities": ("5. Entity Class Definition", "6. Access permission"),
    "10_permissions": ("6. Access permission", None),
}


def parse_sdk(txt_path, sections, out_dir, title):
    # 第一步：读取整个 txt 文件，按行拆分
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.split("\n")

    # 第二步：建立标记索引 —— 找到每个模块起止标题在第几行
    # 遍历每一行，如果行内容匹配到某个模块的开始/结束标题，就记录行号
    markers = {}
    for i, line in enumerate(lines):
        stripped = line.strip()
        # 找起始标记
        for name, (start_marker, _) in sections.items():
            if start_marker in stripped and name not in markers:
                markers[name] = i
        # 找结束标记（即下一个模块的起始标题）
        for name, (_, end_marker) in sections.items():
            if end_marker and end_marker in stripped and f"{name}_end" not in markers:
                markers[f"{name}_end"] = i

    os.makedirs(out_dir, exist_ok=True)

    # 第三步：根据标记索引切出每个模块的内容，写入单独 md
    for name, (start_marker, end_marker) in sections.items():
        start_line = markers.get(name)
        end_line = markers.get(f"{name}_end")

        if start_line is None:
            print(f"  SKIP {name}: marker not found")
            continue
        if end_line is None:
            end_line = len(lines)  # 最后一个模块取到文件末尾

        # 逐行读取，过滤掉页码数字和换页符
        content = []
        for i in range(start_line, end_line):
            line = lines[i].strip()
            if re.match(r"^\d{1,3}$", line):  # 独立数字行（PDF页码残留），跳过
                continue
            if line.startswith("\f"):  # 换页符（form feed），跳过
                continue
            content.append(lines[i])

        md_path = os.path.join(out_dir, f"{name}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {title} - {name.replace('_', ' ').title()}\n\n")
            f.write("".join(content))

        print(f"  Wrote {md_path} ({len(content)} lines)")

    # 额外输出一份完整文档，方便查阅对照
    full_path = os.path.join(out_dir, "00_full_document.md")
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(f"# {title} - Complete Document\n\n")
        f.write(text)
    print(f"  Wrote {full_path}")


if __name__ == "__main__":
    # 一份 PDF → 一份 txt → 按模块切成 13 个 md
    print("Processing Financial SDK...")
    parse_sdk(
        os.path.join(DATA, "raw", "financial_sdk.txt"),
        FIN_SECTIONS,
        os.path.join(DATA, "processed", "financial_sdk"),
        "Nebullar Financial SDK",
    )

    # 同理，Terminal Manager SDK 切成 10 个 md
    print("\nProcessing Terminal Manager SDK...")
    parse_sdk(
        os.path.join(DATA, "raw", "terminal_manager_sdk.txt"),
        TM_SECTIONS,
        os.path.join(DATA, "processed", "terminal_manager_sdk"),
        "Nebullar Terminal Manager SDK",
    )

    print("\nDone!")
