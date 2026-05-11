"""Parse extracted PDF text files into structured markdown by module."""
import re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")

# ── Financial SDK ──────────────────────────────────────────────
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
    "13_permissions": ("6. Access permission", None),
}

# ── Terminal Manager SDK ───────────────────────────────────────
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
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.split("\n")

    # Build section index: find line numbers for each section marker
    markers = {}
    for i, line in enumerate(lines):
        stripped = line.strip()
        for name, (start_marker, _) in sections.items():
            if start_marker in stripped and name not in markers:
                markers[name] = i
        for name, (_, end_marker) in sections.items():
            if end_marker and end_marker in stripped and f"{name}_end" not in markers:
                markers[f"{name}_end"] = i

    os.makedirs(out_dir, exist_ok=True)

    for name, (start_marker, end_marker) in sections.items():
        start_line = markers.get(name)
        end_line = markers.get(f"{name}_end")

        if start_line is None:
            print(f"  SKIP {name}: marker not found")
            continue
        if end_line is None:
            end_line = len(lines)

        content = []
        for i in range(start_line, end_line):
            line = lines[i].strip()
            # Clean up page numbers and garbled chars
            if re.match(r"^\d{1,3}$", line):  # standalone page numbers
                continue
            if line.startswith("\f"):  # form feed
                continue
            content.append(lines[i])

        # Write markdown
        md_path = os.path.join(out_dir, f"{name}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {title} - {name.replace('_', ' ').title()}\n\n")
            f.write("".join(content))

        print(f"  Wrote {md_path} ({len(content)} lines)")

    # Also save full text as single md (for complete reference)
    full_path = os.path.join(out_dir, "00_full_document.md")
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(f"# {title} - Complete Document\n\n")
        f.write(text)
    print(f"  Wrote {full_path}")


if __name__ == "__main__":
    print("Processing Financial SDK...")
    parse_sdk(
        os.path.join(DATA, "raw", "financial_sdk.txt"),
        FIN_SECTIONS,
        os.path.join(DATA, "processed", "financial_sdk"),
        "KOZEN Financial SDK",
    )

    print("\nProcessing Terminal Manager SDK...")
    parse_sdk(
        os.path.join(DATA, "raw", "terminal_manager_sdk.txt"),
        TM_SECTIONS,
        os.path.join(DATA, "processed", "terminal_manager_sdk"),
        "KOZEN Terminal Manager SDK",
    )

    print("\nDone!")
