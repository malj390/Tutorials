from pptx import Presentation
from pptx.util import Inches
import glob
import zipfile
from lxml import etree
from io import BytesIO
import os

NS_CT = "http://schemas.openxmlformats.org/package/2006/content-types"
NS_RELS = "http://schemas.openxmlformats.org/package/2006/relationships"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"

SLIDE_W = int(13.333 * 914400)
SLIDE_H = int(7.5 * 914400)

svg_files = sorted(glob.glob("slide-*.svg"))
if not svg_files:
    print("No SVG files found matching 'slide-*.svg'")
    exit(1)

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

for i, svg_path in enumerate(svg_files):
    slide_num = i + 1
    svg_name = os.path.basename(svg_path)
    rId = f"rIdImg{slide_num}"

    with open(svg_path, "rb") as f:
        entries[f"ppt/media/{svg_name}"] = f.read()

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
        print(f"Warning: could not find spTree in {slide_name}")
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
    entries[slide_name] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

with open("slides_simple.pptx", "wb") as f:
    with zipfile.ZipFile(f, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in entries.items():
            z.writestr(name, data)

print(f"Created slides_simple.pptx with {len(svg_files)} slides (SVG images only)")
