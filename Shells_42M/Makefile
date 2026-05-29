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
# ──────────────────────────────────────────────

SLIDES ?= slides.md
ENTRY  ?= $(SLIDES)

.PHONY: help dev pdf png build sync clean dev-alt pdf-alt

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
	@echo ""
	@echo "Ejemplos:"
	@echo "  make dev              # slides.md original"
	@echo "  make dev-alt          # slide.md (nuevo)"
	@echo "  make pdf ENTRY=slide.md  # exportar slide.md"
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

clean:
	# Elimina exportaciones previas
	rm -f slides-export.pdf slides-export-*.png
	@echo "🧹 Exportaciones eliminadas"
