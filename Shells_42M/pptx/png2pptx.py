from pptx import Presentation
from pptx.util import Inches, Emu
from pathlib import Path
import sys
import re

SRC = Path("slides-export")
DST = "slides_pptx.pptx"
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

png_files = sorted(
    SRC.glob("*.png"),
    key=lambda p: int(re.search(r"(\d+)", p.stem).group(1))
    if re.search(r"(\d+)", p.stem)
    else 0,
)

if not png_files:
    print(f"No PNG files found in '{SRC}/'")
    sys.exit(1)

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H
blank_layout = prs.slide_layouts[6]

for png_path in png_files:
    slide = prs.slides.add_slide(blank_layout)
    pic = slide.shapes.add_picture(str(png_path), 0, 0, SLIDE_W, SLIDE_H)

prs.save(DST)
print(f"✓ Created {DST} with {len(png_files)} slides (PNG images)")
