# ──────────────────────────────────────────────
# Makefile — Shells 42M
# Presentación Slidev: Bash, Zsh & Fish
# ──────────────────────────────────────────────
# Uso básico:
#   make dev    →  Ver presentación en vivo
#   make pdf    →  Exportar a PDF
#   make png    →  Exportar a PNG (para PPTX)
#   make build  →  Web estática
#   make sync   →  Traer última versión del slides.md raíz
#   make clean  →  Limpiar exportaciones
#   make pptx-marp            → marp-slides.md → PPTX editable
#   make pptx-marp-image      → marp-slides.md → PPTX imagen
# ──────────────────────────────────────────────

SLIDES ?= slides.md
ENTRY  ?= $(SLIDES)
MARP_SLIDES ?= marp-slides.md
MARP_PPTX  ?= slides_marp.pptx
CHROME_PATH ?= $(HOME)/.cache/ms-playwright/chromium-1223/chrome-linux64/chrome

.PHONY: help dev pdf png build sync clean dev-alt pdf-alt pptx-marp pptx-marp-image

help:
	@echo "╔══════════════════════════════════════╗"
	@echo "║  Shells 42M — Comandos disponibles   ║"
	@echo "╚══════════════════════════════════════╝"
	@echo ""
	@echo "  make dev      → slides.md en navegador"
	@echo "  make dev-alt  → slide.md (estilo PPTX terminal)"
	@echo "  make pdf      → Exportar slides.md a PDF"
	@echo "  make pdf-alt  → Exportar slide.md a PDF"
	@echo "  make png      → Exportar cada slide como PNG"
	@echo "  make build    → Web estática de slides.md"
	@echo "  make sync     → Copiar slides.md desde raíz"
	@echo "  make clean    → Limpiar exportaciones"
	@echo "  make pptx-marp       → marp-slides.md → PPTX (editable)"
	@echo "  make pptx-marp-image → marp-slides.md → PPTX (imagen)"
	@echo ""
	@echo "Ejemplos:"
	@echo "  make dev                  # slides.md original"
	@echo "  make dev-alt              # slide.md (nuevo)"
	@echo "  make pdf ENTRY=slide.md   # exportar slide.md"
	@echo "  make pptx-marp            # marp-slides.md a PPTX"
	@echo ""

dev:
	# Inicia servidor con slides.md
	pnpm dev

dev-alt:
	# Inicia servidor con slide.md (estilo PPTX terminal)
	pnpm exec slidev slide.md --open

pdf:
	# Exporta slides.md a PDF
	pnpm exec slidev export $(ENTRY)

pdf-alt:
	# Exporta slide.md a PDF
	pnpm exec slidev export slide.md

png:
	# Exporta cada slide como PNG
	pnpm exec slidev export --format png

build:
	# Genera web estática en dist/
	pnpm exec slidev build $(ENTRY)

sync:
	# Copia slides.md desde la raíz
	cp ../slides.md slides.md
	@echo "✔ Sincronizado desde ../slides.md"

pptx-marp:
	# Exporta marp-slides.md a PPTX editable (experimental)
	pnpm exec marp --pptx-editable $(MARP_SLIDES) -o slides_marp.pptx \
		--browser-path "$(CHROME_PATH)"
	@echo "✔ PPTX editable creado: slides_marp.pptx"

pptx-marp-image:
	# Exporta marp-slides.md a PPTX como imagen
	pnpm exec marp --pptx $(MARP_SLIDES) -o slides_marp_image.pptx \
		--browser-path "$(CHROME_PATH)"
	@echo "✔ PPTX imagen creado: slides_marp_image.pptx"

clean:
	# Elimina exportaciones previas
	rm -f slides-export.pdf slides-export-*.png
	@echo "🧹 Exportaciones eliminadas"
