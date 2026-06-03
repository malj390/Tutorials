#!/usr/bin/env python3
"""
slides2pptx.py — Parsea slides.md y genera PPTX estructurado (no solo imágenes)
Modos:
  with-bg  (default) Estructura editable + PNG de fondo
  no-bg             Solo estructura editable, sin PNG
"""

import re
import sys
from pathlib import Path
from html.parser import HTMLParser

SRC_PNG = Path("slides-export")
SRC_MD   = Path("slides.md")
DST      = "slides_structured.pptx"

SLIDE_W  = 13.333
SLIDE_H  = 7.5

MODE = (sys.argv[1] if len(sys.argv) > 1 else "with-bg").strip().lower()
VALID = {"with-bg", "no-bg"}
if MODE not in VALID:
    print(f"Usage: python3 pptx/slides2pptx.py [{'|'.join(sorted(VALID))}]")
    sys.exit(1)


# ────────── slides.md parser (reused from png2pptx_text.py) ──────────

def parse_slides_md(path: Path) -> list[dict]:
    """Devuelve lista de {frontmatter: str, content: str} por slide.
    Maneja correctamente slides con y sin frontmatter."""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    n = len(lines)

    slides: list[dict] = []
    buf: list[str] = []
    mode = "global-fm"  # global-fm | content | fm
    current_fm: list[str] = []

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
                # i is now at the closing --- of global frontmatter
                continue

            if mode == "fm":
                # end of frontmatter → switch to content
                mode = "content"
                i += 1
                continue

            if mode == "content":
                # end of current slide content
                if buf:
                    slides.append({
                        "frontmatter": "\n".join(current_fm),
                        "content": "\n".join(buf),
                    })
                    buf = []
                    current_fm = []

                # peek ahead to see if next non-empty line looks like YAML
                j = i + 1
                is_yaml = False
                while j < n:
                    peek = lines[j].strip()
                    if peek and not peek.startswith("#"):
                        if re.match(r"^[\w-]+:", peek) or peek == "---":
                            is_yaml = True
                        break
                    j += 1

                if is_yaml:
                    mode = "fm"
                # else: stays in content mode (next slide starts immediately)
                i += 1
                continue

        else:
            if mode == "fm":
                current_fm.append(line)
            elif mode == "content":
                buf.append(line)
            # global-fm: skip

        i += 1

    # last slide
    if buf:
        slides.append({
            "frontmatter": "\n".join(current_fm),
            "content": "\n".join(buf),
        })

    return slides


def parse_layout(fm: str) -> str:
    m = re.search(r"layout:\s*(\S+)", fm)
    return m.group(1) if m else "default"


# ────────── content parser ──────────

class Elem:
    def __init__(self, type_: str, **kw):
        self.type = type_
        self.data = kw


def parse_content(text: str) -> list[Elem]:
    """Convierte markdown de un slide a lista de Elem."""
    elems: list[Elem] = []
    lines = text.split("\n")
    i = 0
    n = len(lines)

    while i < n:
        raw = lines[i]
        s = raw.strip()

        # skip empty
        if not s:
            i += 1
            continue

        # skip separators
        if s == "---":
            i += 1
            continue

        # column markers
        if s in ("::left::", "::middle::", "::right::", "::left:: ::middle:: ::right::"):
            elems.append(Elem("column_start", marker=s))
            i += 1
            continue

        # image
        m = re.match(r'<img\s+src="([^"]+)"', s, re.IGNORECASE)
        if m:
            elems.append(Elem("image", src=m.group(1)))
            i += 1
            continue

        # code block
        if s.startswith("```"):
            fence = s[3:].strip()
            code_lines: list[str] = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            elems.append(Elem("code", content="\n".join(code_lines), lang=fence))
            continue

        # v-click (just skip the tag, process content inside normally)
        if s.startswith("<v-click") or s == "</v-click>":
            i += 1
            continue

        # heading
        hm = re.match(r"^(#{1,3})\s+(.+)$", s)
        if hm:
            level = len(hm.group(1))
            elems.append(Elem("heading", text=strip_inline(hm.group(2)), level=level))
            i += 1
            continue

        # bullet list
        if re.match(r"^-\s+", s) or re.match(r"^\*\s+", s):
            items: list[str] = []
            while i < n:
                ls = lines[i].strip()
                lm = re.match(r"^[-*]\s+(.+)$", ls)
                if not lm:
                    break
                items.append(strip_inline(lm.group(1)))
                i += 1
            elems.append(Elem("list", items=items))
            continue

        # numbered list
        if re.match(r"^\d+\.\s+", s):
            items_num: list[str] = []
            while i < n:
                ls = lines[i].strip()
                lm = re.match(r"^\d+\.\s+(.+)$", ls)
                if not lm:
                    break
                items_num.append(strip_inline(lm.group(1)))
                i += 1
            elems.append(Elem("list", items=items_num, numbered=True))
            continue

        # markdown table
        if s.startswith("|") and s.endswith("|") and "|" in s[1:-1]:
            # check if next line is separator
            if i + 1 < n and re.match(r"^[\s|:-]+$", lines[i + 1]):
                rows: list[list[str]] = []
                while i < n and lines[i].strip().startswith("|"):
                    ls = lines[i].strip()
                    if re.match(r"^[\s|:-]+$", ls) and not re.search(r"[a-zA-Z]", ls):
                        i += 1
                        continue
                    cells = [strip_inline(c.strip()) for c in ls.split("|")[1:-1]]
                    rows.append(cells)
                    i += 1
                if rows:
                    elems.append(Elem("table", rows=rows))
                continue

        # HTML table (complex, handle separately)
        if s.lower().startswith("<table"):
            table_data = extract_html_table(lines, i)
            if table_data:
                elems.append(Elem("table", rows=table_data))
                i += len(table_data) + 3  # approximate skip
                continue

        # HTML div / span: extract text
        plain = strip_html(s)
        if plain and len(plain) > 1:
            elems.append(Elem("text", text=plain))
            i += 1
            continue

        # plain text fallback
        if len(s) > 1:
            elems.append(Elem("text", text=strip_inline(s)))
        i += 1

    return elems


def strip_inline(text: str) -> str:
    """Limpia inline formatting: bold, code, icons."""
    t = text
    t = re.sub(r"<carbon:[^/]+/>", "", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"__([^_]+)__", r"\1", t)
    t = re.sub(r"`([^`]+)`", r"\1", t)
    t = re.sub(r"!\[.*?\]\(.*?\)", "", t)
    t = t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    t = re.sub(r"\s+", " ", t).strip()
    return t


def strip_html(text: str) -> str:
    t = re.sub(r"<[^>]+>", "", text)
    t = t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    t = re.sub(r"\s+", " ", t).strip()
    return t


def extract_html_table(lines: list[str], start: int) -> list[list[str]] | None:
    """Extrae tabla HTML como lista de filas (lista de celdas)."""
    class TableParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.rows: list[list[str]] = []
            self._row: list[str] = []
            self._cell = ""
            self._in_cell = False

        def handle_starttag(self, tag, attrs):
            if tag in ("th", "td"):
                self._cell = ""
                self._in_cell = True

        def handle_endtag(self, tag):
            if tag in ("th", "td"):
                self._row.append(strip_inline(self._cell.strip()))
                self._in_cell = False
            elif tag == "tr":
                if self._row:
                    self.rows.append(self._row)
                    self._row = []

        def handle_data(self, data):
            if self._in_cell:
                self._cell += data

    buf = ""
    i = start
    depth = 0
    while i < len(lines):
        buf += lines[i] + "\n"
        depth += lines[i].count("<table")
        depth -= lines[i].count("</table")
        if depth == 0 and "</table" in lines[i]:
            break
        i += 1

    parser = TableParser()
    parser.feed(buf)
    return parser.rows if parser.rows else None


# ────────── PPTX renderers ──────────

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN


def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W)
    prs.slide_height = Inches(SLIDE_H)
    return prs


def add_title(slide, text, x, y, w, h, size=28, align=PP_ALIGN.LEFT, color=RGBColor(0xFF, 0xFF, 0xFF)):
    tx = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tx.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.bold = True
    p.font.color.rgb = color
    p.alignment = align
    return tx


def add_body_text(slide, text, x, y, w, h, size=14, color=RGBColor(0xCC, 0xCC, 0xCC), align=PP_ALIGN.LEFT):
    tx = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tx.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.alignment = align
    return tx


def add_list_block(slide, items, x, y, w, h, size=13, color=RGBColor(0xCC, 0xCC, 0xCC), numbered=False):
    if not items:
        return
    tx = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tx.text_frame
    tf.word_wrap = True

    for idx, item in enumerate(items):
        if idx == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()

        prefix = f"{idx + 1}. " if numbered else "• "
        p.text = prefix + item
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.space_after = Pt(3)


def add_code_block(slide, code, x, y, w, h, size=9):
    tx = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tx.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = code
    p.font.size = Pt(size)
    p.font.name = "Courier New"
    p.font.color.rgb = RGBColor(0xE0, 0xE0, 0xE0)
    return tx


def add_table(slide, rows, x, y, w, h, font_size=11):
    """Crea tabla nativa PPTX a partir de rows (lista de listas)."""
    if not rows:
        return
    nrows = len(rows)
    ncols = max(len(r) for r in rows)
    if ncols == 0:
        return

    table_shape = slide.shapes.add_table(nrows, ncols, Inches(x), Inches(y), Inches(w), Inches(h))
    table = table_shape.table

    for r_idx, row in enumerate(rows):
        for c_idx, cell_text in enumerate(row):
            if c_idx >= ncols:
                break
            cell = table.cell(r_idx, c_idx)
            cell.text = cell_text
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(font_size)
                p.font.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)

    return table_shape


def add_png_background(slide, png_path):
    """Añade PNG a pantalla completa como imagen."""
    if png_path and png_path.exists():
        slide.shapes.add_picture(str(png_path), 0, 0, Inches(SLIDE_W), Inches(SLIDE_H))


# ────────── layout renderers ──────────

def render_section(slide, elems, png_path):
    add_png_background(slide, png_path) if MODE == "with-bg" else None
    title_text = ""
    subtitle_text = ""

    for e in elems:
        if e.type == "heading" and e.data["level"] == 1:
            title_text = e.data["text"]
        elif e.type == "heading" and e.data["level"] == 2:
            title_text = e.data["text"]
        elif e.type == "heading" and e.data["level"] == 3:
            subtitle_text = e.data["text"]
        elif e.type == "text" and not title_text:
            title_text = e.data["text"]
        elif e.type == "text" and not subtitle_text:
            subtitle_text = e.data["text"]

    if title_text:
        add_title(slide, title_text, 1.5, 2.8, 10.3, 1.2, size=36, align=PP_ALIGN.CENTER)
    if subtitle_text:
        add_body_text(slide, subtitle_text, 1.5, 4.0, 10.3, 0.8, size=18, align=PP_ALIGN.CENTER, color=RGBColor(0xAA, 0xAA, 0xAA))


def render_default(slide, elems, png_path):
    add_png_background(slide, png_path) if MODE == "with-bg" else None
    y = 0.4

    for e in elems:
        if e.type == "heading":
            sz = {1: 28, 2: 22, 3: 18}.get(e.data["level"], 16)
            add_title(slide, e.data["text"], 0.8, y, 11.7, 0.7, size=sz)
            y += 0.8
        elif e.type == "text":
            add_body_text(slide, e.data["text"], 0.8, y, 11.7, 0.5, size=14)
            y += 0.45
        elif e.type == "list":
            add_list_block(slide, e.data["items"], 0.8, y, 11.7, 0.4 * len(e.data["items"]), size=13)
            y += 0.35 * len(e.data["items"])
        elif e.type == "code":
            lines = e.data["content"].count("\n") + 1
            h = max(0.5, lines * 0.22)
            add_code_block(slide, e.data["content"], 0.8, y, 11.7, h)
            y += h + 0.15
        elif e.type == "table":
            add_table(slide, e.data["rows"], 0.8, y, 11.7, 3.5, font_size=10)
            y += 3.8
        elif e.type == "image":
            # skip remote images in this context
            pass


def render_columns(slide, elems, png_path, ncols=2):
    add_png_background(slide, png_path) if MODE == "with-bg" else None
    y_title = 0.3
    y_body = 1.3

    # Collect elements before first column marker as title area
    title_elems: list[Elem] = []
    col_elems: dict[str, list[Elem]] = {}
    current_col: str | None = None
    col_order: list[str] = []

    for e in elems:
        if e.type == "column_start":
            marker = e.data["marker"]
            if marker == "::left::":
                current_col = "left"
            elif marker == "::middle::":
                current_col = "middle"
            elif marker == "::right::":
                current_col = "right"
            if current_col and current_col not in col_order:
                col_order.append(current_col)
                col_elems[current_col] = []
            continue
        if current_col:
            col_elems.setdefault(current_col, []).append(e)
        else:
            title_elems.append(e)

    # Title
    for e in title_elems:
        if e.type == "heading":
            add_title(slide, e.data["text"], 0.8, y_title, 11.7, 0.7, size=26)
        elif e.type == "text":
            add_body_text(slide, e.data["text"], 0.8, y_title + 0.6, 11.7, 0.4, size=13, color=RGBColor(0xAA, 0xAA, 0xAA))

    # Columns
    col_widths = {"left": 4.0, "middle": 4.0, "right": 4.0}
    if ncols == 2:
        col_x = {"left": 0.5, "right": 6.8}
        col_widths = {"left": 6.0, "right": 6.0}
    else:
        col_x = {"left": 0.3, "middle": 4.6, "right": 8.9}
        col_widths = {"left": 4.1, "middle": 4.1, "right": 4.1}

    for col_name in col_order:
        cx = col_x.get(col_name, 0.5)
        cw = col_widths.get(col_name, 4.0)
        cy = y_body
        max_y = cy

        # Column header (if first element looks like a header)
        col_els = col_elems.get(col_name, [])
        for ce in col_els:
            if ce.type == "heading":
                add_title(slide, ce.data["text"], cx, cy, cw, 0.5, size=16)
                cy += 0.55
            elif ce.type == "list":
                add_list_block(slide, ce.data["items"], cx, cy, cw, 0.35 * len(ce.data["items"]), size=11)
                cy += 0.32 * len(ce.data["items"])
            elif ce.type == "code":
                lines_c = ce.data["content"].count("\n") + 1
                ch = max(0.4, lines_c * 0.18)
                add_code_block(slide, ce.data["content"], cx, cy, cw, ch, size=8)
                cy += ch + 0.1
            elif ce.type == "text":
                add_body_text(slide, ce.data["text"], cx, cy, cw, 0.4, size=11, color=RGBColor(0xBB, 0xBB, 0xBB))
                cy += 0.35
            elif ce.type == "list" and ce.data.get("numbered"):
                add_list_block(slide, ce.data["items"], cx, cy, cw, 0.3 * len(ce.data["items"]), size=11, numbered=True)
                cy += 0.28 * len(ce.data["items"])

            if cy > max_y:
                max_y = cy


def render_center(slide, elems, png_path):
    add_png_background(slide, png_path) if MODE == "with-bg" else None
    y = 1.5
    for e in elems:
        if e.type == "heading":
            add_title(slide, e.data["text"], 1.0, y, 11.3, 1.0, size=36, align=PP_ALIGN.CENTER)
            y += 1.0
        elif e.type == "text":
            add_body_text(slide, e.data["text"], 1.0, y, 11.3, 0.6, size=18, align=PP_ALIGN.CENTER)
            y += 0.6


# ────────── Main ──────────

def main():
    if not SRC_MD.exists():
        print(f"✗ '{SRC_MD}' not found"); sys.exit(1)

    slides = parse_slides_md(SRC_MD)
    print(f"✓ Parsed {len(slides)} slides from {SRC_MD}")

    # PNG files
    png_files: list[Path] = []
    if MODE == "with-bg":
        if not SRC_PNG.is_dir():
            print(f"✗ Directory '{SRC_PNG}/' not found — run export first")
            sys.exit(1)
        png_files = sorted(
            SRC_PNG.glob("*.png"),
            key=lambda p: int(m.group(1)) if (m := re.search(r"(\d+)", p.stem)) else 0,
        )
        if not png_files:
            print(f"✗ No PNG files in '{SRC_PNG}/' — run export first")
            sys.exit(1)

    prs = create_presentation()

    for i, slide_data in enumerate(slides):
        sn = i + 1
        print(f"  Slide {sn}/{len(slides)} ...", end=" ", flush=True)

        fm = slide_data["frontmatter"]
        content = slide_data["content"]
        layout = parse_layout(fm)

        # parse content elements
        elems = parse_content(content)

        # create slide
        slide = prs.slides.add_slide(prs.slide_layouts[6])

        png_path = png_files[i] if i < len(png_files) else None

        if layout == "section":
            render_section(slide, elems, png_path)
        elif layout == "default" or layout == "":
            render_default(slide, elems, png_path)
        elif layout == "two-cols-title":
            render_columns(slide, elems, png_path, ncols=2)
        elif layout == "three-cols":
            render_columns(slide, elems, png_path, ncols=3)
        elif layout == "center":
            render_center(slide, elems, png_path)
        else:
            # fallback: default render
            render_default(slide, elems, png_path)

        print("✓")

    prs.save(DST)
    print(f"\n✔ Created '{DST}' with {len(slides)} slides (mode: {MODE})")


if __name__ == "__main__":
    main()
