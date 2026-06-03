#!/usr/bin/env python3
"""
png2pptx_text.py — Crea PPTX desde slides-export/ PNGs

Modos:
  image-only  PNG a pantalla completa (por defecto)
  invisible   PNG + texto de slides.md en color #1a1a1a (buscable en Google Slides)
  visible     PNG + texto OCR en blanco + corrección con slides.md
"""

import re
import sys
from pathlib import Path

SRC_PNG = Path("slides-export")
SRC_MD   = Path("slides.md")
DST      = "slides_text.pptx"

SLIDE_W  = 13.333
SLIDE_H  = 7.5

MODE = (sys.argv[1] if len(sys.argv) > 1 else "image-only").strip().lower()
VALID = {"image-only", "invisible", "visible"}
if MODE not in VALID:
    print(f"Usage: python3 pptx/png2pptx_text.py [{'|'.join(sorted(VALID))}]")
    sys.exit(1)


# ────────── slides.md parser ──────────

def parse_slides_md(path: Path) -> list[str]:
    """Devuelve lista de contenido markdown por slide (sin frontmatter)."""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    n = len(lines)

    slides: list[str] = []
    buf: list[str] = []
    mode = "global-fm"

    i = 0
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped == "---":
            if mode == "global-fm":
                mode = "content"
                i += 1
                while i < n and lines[i].strip() != "---":
                    i += 1
                continue

            if mode == "fm":
                mode = "content"
                i += 1
                continue

            if mode == "content":
                if buf:
                    slides.append("\n".join(buf).strip())
                    buf = []

                j = i + 1
                is_yaml = False
                while j < n:
                    peek = lines[j].strip()
                    if peek and not peek.startswith("#"):
                        if re.match(r"^[\w-]+:", peek) or peek == "---":
                            is_yaml = True
                        break
                    j += 1

                mode = "fm" if is_yaml else "content"
                i += 1
                continue
        else:
            if mode == "content":
                buf.append(line)

        i += 1

    if buf:
        slides.append("\n".join(buf).strip())

    return slides


def extract_plain_text(md: str) -> str:
    """Extrae texto plano legible de un bloque markdown."""
    lines = md.split("\n")
    parts: list[str] = []
    in_code = False
    in_html_comment = False

    for line in lines:
        s = line.strip()

        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if not s:
            continue
        if s.startswith("<!--"):
            if "-->" in s:
                continue
            in_html_comment = True
            continue
        if in_html_comment:
            if "-->" in s:
                in_html_comment = False
            continue
        if s == "---":
            continue

        t = s
        t = re.sub(r"<carbon:[^/]+/>", "", t)
        t = re.sub(r"<[^>]+>", "", t)
        t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
        t = re.sub(r"__([^_]+)__", r"\1", t)
        t = re.sub(r"!\[.*?\]\(.*?\)", "", t)
        t = re.sub(r"`([^`]+)`", r"\1", t)
        t = re.sub(r"^[#]+\s*", "", t)
        t = re.sub(r"^-\s+", "", t)
        t = re.sub(r"^\d+\.\s+", "", t)
        t = re.sub(r"^::\w+::$", "", t)
        t = t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        t = t.strip()

        if len(t) > 1:
            parts.append(t)

    return "\n".join(parts)


# ────────── main ──────────

def main():
    if not SRC_PNG.is_dir():
        print(f"✗ Directory '{SRC_PNG}/' not found")
        sys.exit(1)

    png_files = sorted(
        SRC_PNG.glob("*.png"),
        key=lambda p: int(m.group(1)) if (m := re.search(r"(\d+)", p.stem)) else 0,
    )
    if not png_files:
        print(f"✗ No PNG files in '{SRC_PNG}/'")
        sys.exit(1)

    # slides.md → texto plano por slide
    md_texts: list[str] = []
    if SRC_MD.exists():
        raw = parse_slides_md(SRC_MD)
        md_texts = [extract_plain_text(s) for s in raw]
        print(f"✓ Parsed {len(raw)} slides from {SRC_MD}")

    # OCR (solo visible)
    reader = None
    if MODE == "visible":
        import easyocr
        reader = easyocr.Reader(["en"], gpu=False, verbose=False)
        print("✓ OCR ready")

    # PPTX
    from pptx import Presentation
    from pptx.util import Inches, Emu, Pt
    from pptx.dml.color import RGBColor

    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W)
    prs.slide_height = Inches(SLIDE_H)
    blank = prs.slide_layouts[6]

    for i, png_path in enumerate(png_files):
        sn = i + 1
        print(f"  Slide {sn}/{len(png_files)} ...", end=" ", flush=True)
        slide = prs.slides.add_slide(blank)

        # PNG a pantalla completa
        slide.shapes.add_picture(str(png_path), 0, 0, Inches(SLIDE_W), Inches(SLIDE_H))

        # ── mode: image-only ──
        if MODE == "image-only":
            print("✓")
            continue

        # ── mode: invisible ──
        if MODE == "invisible":
            txt = md_texts[i] if i < len(md_texts) else ""
            if txt:
                txbox = slide.shapes.add_textbox(Emu(91440), Emu(91440), Inches(12), Inches(6.5))
                tf = txbox.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = txt
                p.font.size = Pt(8)
                p.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
            print("✓")
            continue

        # ── mode: visible (OCR) ──
        from PIL import Image
        import numpy as np
        import difflib

        img = Image.open(png_path)
        w, h = img.size
        results = reader.readtext(np.array(img))
        md_lines = md_texts[i].split("\n") if i < len(md_texts) else []

        for bbox, ocr_text, conf in results:
            text = ocr_text.strip()
            if not text or conf < 0.25:
                continue

            x1, y1 = bbox[0]
            x2, y2 = bbox[2]
            bw = x2 - x1
            bh = y2 - y1
            if bw < 10 or bh < 6:
                continue

            ex = int(x1 / w * SLIDE_W * 914400)
            ey = int(y1 / h * SLIDE_H * 914400)
            ew = int(bw / w * SLIDE_W * 914400)
            eh = int(bh / h * SLIDE_H * 914400)

            # corregir con slides.md (mejor coincidencia)
            final = text
            best_ratio = 0.0
            best_line = ""
            for line in md_lines:
                l = line.strip()
                if not l:
                    continue
                ratio = difflib.SequenceMatcher(None, text.lower(), l.lower()).ratio()
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_line = l
            if best_ratio > 0.45:
                final = best_line

            txbox = slide.shapes.add_textbox(Emu(ex), Emu(ey), Emu(ew), Emu(eh))
            tf = txbox.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = final
            p.font.size = Pt(11)
            p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        print("✓")

    prs.save(DST)
    print(f"\n✔ Created '{DST}' with {len(png_files)} slides (mode: {MODE})")


if __name__ == "__main__":
    main()
