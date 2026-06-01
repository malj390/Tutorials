# # Solo SVG
# uv run --with python-pptx --with lxml python3 svg2pptx_simple.py

# # SVG + OCR
# uv run --with python-pptx --with lxml --with cairosvg --with easyocr --with pillow python3 svg2pptx_ocr.py


from pptx import Presentation
from pptx.util import Inches
import glob
import zipfile
from lxml import etree
from io import BytesIO
import os
import sys
import easyocr
import cairosvg
from PIL import Image
import numpy as np

NS_CT = "http://schemas.openxmlformats.org/package/2006/content-types"
NS_RELS = "http://schemas.openxmlformats.org/package/2006/relationships"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"

SLIDE_W = int(13.333 * 914400)
SLIDE_H = int(7.5 * 914400)


def make_text_box(text, x, y, w, h, font_pt, shape_id):
    sp = etree.SubElement(
        None, f"{{{NS_P}}}sp"
    ) if False else None
    sp = etree.Element(f"{{{NS_P}}}sp")

    nvSpPr = etree.SubElement(sp, f"{{{NS_P}}}nvSpPr")
    cNvPr = etree.SubElement(nvSpPr, f"{{{NS_P}}}cNvPr")
    cNvPr.set("id", str(shape_id))
    cNvPr.set("name", f"TextBox {shape_id}")
    cNvSpPr = etree.SubElement(nvSpPr, f"{{{NS_P}}}cNvSpPr")
    cNvSpPr.set("txBox", "1")
    etree.SubElement(nvSpPr, f"{{{NS_P}}}nvPr")

    spPr = etree.SubElement(sp, f"{{{NS_P}}}spPr")
    xfrm = etree.SubElement(spPr, f"{{{NS_A}}}xfrm")
    off = etree.SubElement(xfrm, f"{{{NS_A}}}off")
    off.set("x", str(x))
    off.set("y", str(y))
    ext = etree.SubElement(xfrm, f"{{{NS_A}}}ext")
    ext.set("cx", str(w))
    ext.set("cy", str(h))

    prstGeom = etree.SubElement(spPr, f"{{{NS_A}}}prstGeom")
    prstGeom.set("prst", "rect")
    etree.SubElement(prstGeom, f"{{{NS_A}}}avLst")

    etree.SubElement(spPr, f"{{{NS_A}}}noFill")
    ln = etree.SubElement(spPr, f"{{{NS_A}}}ln")
    etree.SubElement(ln, f"{{{NS_A}}}noFill")

    txBody = etree.SubElement(sp, f"{{{NS_P}}}txBody")
    bodyPr = etree.SubElement(txBody, f"{{{NS_A}}}bodyPr")
    bodyPr.set("wrap", "square")
    bodyPr.set("lIns", "0")
    bodyPr.set("tIns", "0")
    bodyPr.set("rIns", "0")
    bodyPr.set("bIns", "0")
    etree.SubElement(bodyPr, f"{{{NS_A}}}normAutofit")
    solidFill = etree.SubElement(txBody, f"{{{NS_A}}}solidFill")
    srgbClr = etree.SubElement(solidFill, f"{{{NS_A}}}srgbClr")
    srgbClr.set("val", "FFFFFF")

    p = etree.SubElement(txBody, f"{{{NS_A}}}p")
    r = etree.SubElement(p, f"{{{NS_A}}}r")
    rPr = etree.SubElement(r, f"{{{NS_A}}}rPr")
    rPr.set("lang", "en-US")
    rPr.set("sz", str(font_pt))
    rPr.set("dirty", "0")
    t = etree.SubElement(r, f"{{{NS_A}}}t")
    t.text = text

    return sp


svg_files = sorted(glob.glob("slide-*.svg"))
if not svg_files:
    print("No SVG files found matching 'slide-*.svg'")
    exit(1)

print(f"Found {len(svg_files)} SVG files")
print("Initializing EasyOCR reader (may download model on first run)...")
sys.stdout.flush()
reader = easyocr.Reader(["en"], gpu=False, verbose=False)
print("OCR reader ready")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
for _ in svg_files:
    prs.slides.add_slide(prs.slide_layouts[6])

buf = BytesIO()
prs.save(buf)

in_zip = zipfile.ZipFile(buf)
entries = {}

for item in in_zip.infolist():
    name = item.filename
    data = in_zip.read(name)

    if name == "[Content_Types].xml":
        root = etree.fromstring(data)
        default = etree.SubElement(root, f"{{{NS_CT}}}Default")
        default.set("Extension", "svg")
        default.set("ContentType", "image/svg+xml")
        data = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

    entries[name] = data

in_zip.close()

next_text_id = 200

for i, svg_path in enumerate(svg_files):
    slide_num = i + 1
    svg_name = os.path.basename(svg_path)
    rId = f"rIdImg{slide_num}"
    print(f"Processing slide {slide_num}/{len(svg_files)}...")
    sys.stdout.flush()

    with open(svg_path, "rb") as f:
        svg_data = f.read()

    entries[f"ppt/media/{svg_name}"] = svg_data

    rels_name = f"ppt/slides/_rels/slide{slide_num}.xml.rels"
    root = etree.fromstring(entries[rels_name])
    rel = etree.SubElement(root, f"{{{NS_RELS}}}Relationship")
    rel.set("Id", rId)
    rel.set("Type", f"{NS_R}/image")
    rel.set("Target", f"../media/{svg_name}")
    entries[rels_name] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

    slide_name = f"ppt/slides/slide{slide_num}.xml"
    root = etree.fromstring(entries[slide_name])
    spTree = root.find(f"{{{NS_P}}}cSld/{{{NS_P}}}spTree")
    if spTree is None:
        print(f"  Warning: could not find spTree in {slide_name}")
        continue

    pic = etree.fromstring(
        f'<p:pic xmlns:p="{NS_P}" xmlns:a="{NS_A}" xmlns:r="{NS_R}">'
        f'<p:nvPicPr><p:cNvPr id="{100 + slide_num}" name="Picture {slide_num}" descr="{svg_name}"/>'
        f'<p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>'
        f'<p:blipFill><a:blip r:embed="{rId}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>'
        f'<p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{SLIDE_W}" cy="{SLIDE_H}"/></a:xfrm>'
        f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>'
    )
    spTree.append(pic)

    # OCR
    try:
        png_data = cairosvg.svg2png(bytestring=svg_data, scale=3.0) # scale 2.0
        img = Image.open(BytesIO(png_data))
        img_array = np.array(img)
        img_w, img_h = img.size
    except Exception as e:
        print(f"  Warning: could not render SVG for OCR: {e}")
        entries[slide_name] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
        continue

    try:
        results = reader.readtext(img_array)
    except Exception as e:
        print(f"  Warning: OCR failed for {svg_name}: {e}")
        entries[slide_name] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
        continue

    for bbox, text, confidence in results:
        text = text.strip()
        if not text or confidence < 0.1: # 0.3
            continue

        x1, y1 = bbox[0]
        x2, y2 = bbox[2]
        box_w = x2 - x1
        box_h = y2 - y1

        if box_w < 10 or box_h < 6:
            continue

        emu_x = int(x1 / img_w * SLIDE_W)
        emu_y = int(y1 / img_h * SLIDE_H)
        emu_w = int(box_w / img_w * SLIDE_W)
        emu_h = int(box_h / img_h * SLIDE_H)

        font_pt = max(8, int(box_h * 432 / img_h))
        font_sz = font_pt * 100

        txbox = make_text_box(text, emu_x, emu_y, emu_w, emu_h, font_sz, next_text_id)
        spTree.append(txbox)
        next_text_id += 1

    entries[slide_name] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

print(f"Writing slides.pptx with {len(svg_files)} slides...")
sys.stdout.flush()

with open("slides.pptx", "wb") as f:
    with zipfile.ZipFile(f, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in entries.items():
            z.writestr(name, data)

print(f"Done — created slides.pptx with {len(svg_files)} slides (vector SVGs + OCR text)")
