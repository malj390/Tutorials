#!/usr/bin/env fish

# ──────────────────────────────────────────────
# export-pptx.fish
# Exporta slides.md → PNG (modo oscuro) → PPTX
#
# Uso:
#   ./export-pptx.fish                    # solo PNG como imagen
#   ./export-pptx.fish invisible          # PNG + texto invisible (Ctrl+F)
#   ./export-pptx.fish visible            # PNG + texto OCR visible blanco
#   ./export-pptx.fish structured         # PPTX estructurado + PNG fondo (default)
#   ./export-pptx.fish no-bg              # PPTX estructurado sin PNG
#   ./export-pptx.fish marp              # marp-slides.md → PPTX editable
#   ./export-pptx.fish marp-image        # marp-slides.md → PPTX imagen
#   ./export-pptx.fish help               # esta ayuda
# ──────────────────────────────────────────────

set SELF_DIR (dirname (status filename))
cd $SELF_DIR

# ── Argumento ──
set mode structured
if test (count $argv) -ge 1
    set mode $argv[1]
end

switch $mode
    case help --help -h
        echo "Uso: ./export-pptx.fish [mode]"
        echo ""
        echo "Modos rápidos (imagen):"
        echo "  image-only  (alias: default) PNG como imagen, sin texto"
        echo "  invisible   PNG + texto de slides.md invisible (buscable Ctrl+F)"
        echo "  visible     PNG + texto OCR visible blanco"
        echo ""
        echo "Modos estructurados (desde slides.md):"
        echo "  structured  (alias: with-bg, default) PPTX con estructura editable + PNG fondo"
        echo "  no-bg       Solo estructura editable, sin PNG fondo"
        echo ""
        echo "Modos Marp (desde marp-slides.md):"
        echo "  marp        PPTX editable (experimental, requiere LibreOffice)"
        echo "  marp-image  PPTX como imagen (todas las diapositivas renderizadas)"
        echo ""
        echo "Ejemplos:"
        echo "  ./export-pptx.fish"
        echo "  ./export-pptx.fish invisible"
        echo "  ./export-pptx.fish visible"
        echo "  ./export-pptx.fish structured"
        echo "  ./export-pptx.fish no-bg"
        echo "  ./export-pptx.fish marp"
        echo "  ./export-pptx.fish marp-image"
        exit 0
    case image-only default
        set mode image-only
    case invisible visible structured with-bg no-bg
        # válido
    case marp marp-image
        # válido
    case '*'
        echo "✗ Modo desconocido: '$mode'"
        echo "  Usa: ./export-pptx.fish help"
        exit 1
end

set CHROME_PATH "$HOME/.cache/ms-playwright/chromium-1223/chrome-linux64/chrome"

# ── Paso 1 (Slidev): Exportar PNGs ──
if test "$mode" != no-bg; and test "$mode" != marp; and test "$mode" != marp-image
    echo "── Paso 1: Exportar slides como PNG (modo oscuro) ──"
    pnpm exec slidev export --format png --dark

    if test $status -ne 0
        echo "✗ Error en la exportación a PNG"
        exit 1
    end
    echo ""
end

# ── Paso 2: Generar PPTX ──
echo "── Paso 2: Generar PPTX (mode: $mode) ──"

switch $mode
    case image-only
        uv run --with python-pptx python3 pptx/png2pptx_text.py image-only
        set outfile slides_text.pptx

    case invisible
        uv run --with python-pptx python3 pptx/png2pptx_text.py invisible
        set outfile slides_text.pptx

    case visible
        uv run --with python-pptx --with easyocr --with pillow python3 pptx/png2pptx_text.py visible
        set outfile slides_text.pptx

    case structured with-bg
        uv run --with python-pptx python3 pptx/slides2pptx.py with-bg
        set outfile slides_structured.pptx

    case no-bg
        uv run --with python-pptx python3 pptx/slides2pptx.py no-bg
        set outfile slides_structured.pptx

    case marp
        pnpm exec marp --pptx-editable marp-slides.md -o slides_marp.pptx --browser-path "$CHROME_PATH"
        set outfile slides_marp.pptx

    case marp-image
        pnpm exec marp --pptx marp-slides.md -o slides_marp_image.pptx --browser-path "$CHROME_PATH"
        set outfile slides_marp_image.pptx
end

if test $status -ne 0
    echo "✗ Error al generar PPTX"
    exit 1
end

echo ""
echo "✔ Listo — Importa '$outfile' en Google Slides"
