---
marp: true
backgroundColor: "#0f172a"
color: "#e2e8f0"
description: Shell Showdown — Bash, Zsh & Fish
---

<style>
section {
  background: #0f172a;
  color: #e2e8f0;
  font-family: 'Courier New', 'Liberation Mono', monospace;
  padding: 48px;
}
h1 {
  color: #f8fafc;
  font-size: 2.2em;
  margin-bottom: 0.3em;
}
h2 {
  color: #94a3b8;
  font-size: 1.3em;
  border-bottom: 1px solid #1e293b;
  padding-bottom: 0.3em;
  margin-bottom: 0.5em;
}
h3 {
  color: #64748b;
  font-size: 1.1em;
  font-weight: normal;
}
h4 {
  color: #94a3b8;
  font-size: 1em;
  margin-bottom: 0.3em;
}
code {
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 4px;
  padding: 1px 5px;
  font-size: 0.85em;
}
pre {
  background: #1e293b !important;
  border: 1px solid #334155;
  border-radius: 8px;
  padding: 16px;
  line-height: 1.4;
}
pre code {
  background: none;
  border: none;
  padding: 0;
  font-size: 0.75em;
}
table {
  border-collapse: collapse;
  width: 100%;
  font-size: 0.65em;
}
th {
  background: #1e293b;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: 0.8em;
  padding: 10px 14px;
  border: 1px solid #334155;
}
td {
  padding: 10px 14px;
  border: 1px solid #1e293b;
}
tr:nth-child(even) td {
  background: rgba(30, 41, 59, 0.3);
}
a { color: #60a5fa; }
img {
  max-width: 100%;
  max-height: 65vh;
  object-fit: contain;
  display: block;
  margin: 0 auto;
}

.flex-three {
  display: flex;
  gap: 16px;
  margin-top: 16px;
}
.flex-three > div {
  flex: 1;
  min-width: 0;
}
.flex-two {
  display: flex;
  gap: 24px;
  margin-top: 16px;
}
.flex-two > div {
  flex: 1;
  min-width: 0;
}
.card {
  border-radius: 12px;
  padding: 16px;
  display: flex;
  flex-direction: column;
}
.card.bash {
  border: 1px solid rgba(52, 211, 153, 0.15);
  background: rgba(52, 211, 153, 0.05);
}
.card.zsh {
  border: 1px solid rgba(45, 212, 191, 0.15);
  background: rgba(45, 212, 191, 0.05);
}
.card.fish {
  border: 1px solid rgba(96, 165, 250, 0.2);
  background: rgba(96, 165, 250, 0.08);
}
.card-header {
  font-weight: bold;
  font-size: 1.1em;
  padding-bottom: 8px;
  margin-bottom: 10px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.card-header.bash { color: #34d399; }
.card-header.zsh { color: #2dd4bf; }
.card-header.fish { color: #60a5fa; }
.card-footer {
  margin-top: auto;
  padding-top: 8px;
  border-top: 1px solid rgba(255,255,255,0.05);
  font-size: 0.7em;
  color: #64748b;
}

.bash { color: #34d399; }
.zsh { color: #2dd4bf; }
.fish { color: #60a5fa; }

section.lead {
  text-align: center;
  padding-top: 15vh;
}
section.lead h1 {
  font-size: 3.5em;
  margin-bottom: 0.2em;
}
section.lead h3 {
  font-size: 1.5em;
  color: #94a3b8;
  font-weight: normal;
  margin-bottom: 1em;
}

section.section {
  text-align: center;
  padding-top: 15vh;
}
section.section h1 {
  font-size: 3em;
  color: #f8fafc;
}

ul {
  list-style: none;
  padding-left: 0;
}
li {
  margin-bottom: 0.4em;
  line-height: 1.45;
  font-size: 0.85em;
}

.text-sm { font-size: 0.7em; }
.text-xs { font-size: 0.6em; }
.text-muted { color: #64748b; }
.text-green { color: #34d399; }
.text-teal { color: #2dd4bf; }
.text-blue { color: #60a5fa; }
.text-rose { color: #fb7185; }
.text-cyan { color: #22d3ee; }
.text-white { color: #f8fafc; }
.text-yellow { color: #fbbf24; }
.text-center { text-align: center; }
.mt-1 { margin-top: 0.5em; }
.mt-2 { margin-top: 1em; }
.mt-4 { margin-top: 2em; }
.mb-1 { margin-bottom: 0.5em; }
</style>

<!--
╔══════════════════════════════════════════╗
║  SLIDE 1: TITLE                          ║
╚══════════════════════════════════════════╝
-->
<!-- _class: lead -->

# Shell Showdown
### Bash, Zsh & Fish: Eficiencia en la Terminal

<span class="text-sm text-muted">Tutorial para 42 Málaga</span>

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 2: SECTION — INTRODUCCIÓN        ║
╚══════════════════════════════════════════╝
-->
<!-- _class: section -->

# 01. Introducción

<span class="bash">Bash</span>
<span class="text-muted">vs</span>
<span class="zsh">Zsh</span>
<span class="text-muted">vs</span>
<span class="fish">Fish</span>

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 3: ECOSISTEMA (3-COL CARDS)      ║
╚══════════════════════════════════════════╝
-->

# Ecosistema de Shells
Análisis comparativo de características

<div class="flex-three">

<div class="card bash">
<div class="card-header bash">┌─ Bash ─┐</div>
<ul>
<li><span class="text-xs text-muted">Año de lanzamiento</span><br>1989</li>
<li><span class="text-xs text-muted">Compatibilidad POSIX</span><br>100% Estándar</li>
<li><span class="text-xs text-muted">Filosofía de Sintaxis</span><br>Clásica y estricta</li>
<li><span class="text-xs text-muted">Experiencia Inicial</span><br>Espartana</li>
</ul>
<div class="card-footer">Plugins: Limitados</div>
</div>

<div class="card zsh">
<div class="card-header zsh">┌─ Zsh ─┐</div>
<ul>
<li><span class="text-xs text-muted">Año de lanzamiento</span><br>1990</li>
<li><span class="text-xs text-muted">Compatibilidad POSIX</span><br>99% (Superconjunto)</li>
<li><span class="text-xs text-muted">Filosofía de Sintaxis</span><br>Clásica mejorada</li>
<li><span class="text-xs text-muted">Experiencia Inicial</span><br>Espartana</li>
</ul>
<div class="card-footer">Plugins: Oh My Zsh (Extenso)</div>
</div>

<div class="card fish">
<div class="card-header fish">┌─ Fish ─┐</div>
<ul>
<li><span class="text-xs text-muted">Año de lanzamiento</span><br>2005</li>
<li><span class="text-xs text-muted">Compatibilidad POSIX</span><br>0% (Diseño propio)</li>
<li><span class="text-xs text-muted">Filosofía de Sintaxis</span><br>Moderna (Humana)</li>
<li><span class="text-xs text-muted">Experiencia Inicial</span><br>Completa e Inteligente</li>
</ul>
<div class="card-footer">Plugins: Fisher (Ligero / Nativo)</div>
</div>

</div>

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 4: VENTAJAS (3-COL CARDS)        ║
╚══════════════════════════════════════════╝
-->

# Ventajas

<div class="flex-three">

<div class="card bash">
<div class="card-header bash">┌─ Bash ─┐</div>
<ul>
<li><span class="text-green">✓</span> <b>Portabilidad absoluta:</b><br>Linux, macOS, WSL, servidores, contenedores.</li>
<li><span class="text-green">✓</span> <b>Documentación infinita:</b><br>todo problema ya fue resuelto en internet.</li>
<li><span class="text-green">✓</span> <b>Estándar:</b><br>El rey en CI/CD, Dockerfiles y scripts de instalación.</li>
<li><span class="text-green">✓</span> <b>Ligero:</b><br>Sin dependencias externas y ultra rápido en arranque.</li>
<li><span class="text-green">✓</span> <b>Compatibilidad total:</b><br>Scripts de hace décadas siguen funcionando.</li>
</ul>
</div>

<div class="card zsh">
<div class="card-header zsh">┌─ Zsh ─┐</div>
<ul>
<li><span class="text-teal">✓</span> <b>Compatibilidad total:</b><br>Los scripts de Bash funcionan sin cambios.</li>
<li><span class="text-teal">✓</span> <b>Oh My Zsh:</b><br>El mayor ecosistema de plugins y temas de la comunidad.</li>
<li><span class="text-teal">✓</span> <b>Personalizable:</b><br>Puedes redefinir cualquier comportamiento interno.</li>
<li><span class="text-teal">✓</span> <b>Nativo en Apple:</b><br>Es la Shell por defecto en macOS actualmente.</li>
<li><span class="text-teal">✓</span> <b>Mejor autocompletado:</b><br>Supera a Bash ampliamente.</li>
<li><span class="text-teal">✓</span> <b>Arrays flexibles:</b><br>Manipulación limpia sin requerir <code>${array[@]}</code>.</li>
</ul>
</div>

<div class="card fish">
<div class="card-header fish">┌─ Fish ─┐</div>
<ul>
<li><span class="text-blue">✓</span> <b>Autocompletado nativo:</b><br>Lee páginas <code>man</code> y sugiere comandos en gris.</li>
<li><span class="text-blue">✓</span> <b>Sintaxis limpia:</b><br>Adiós a <code>do/done/fi</code>, todo termina con <code>end</code>.</li>
<li><span class="text-blue">✓</span> <b><code>argparse</code> integrado:</b><br>Procesa banderas avanzadas en una sola línea.</li>
<li><span class="text-blue">✓</span> <b>Listas nativas:</b><br>Manejo de arrays real sin comillas de protección.</li>
<li><span class="text-blue">✓</span> <b><code>funcsave</code>:</b><br>Guardado instantáneo de funciones desde la terminal.</li>
<li><span class="text-blue">✓</span> <b>Rápido y robusto:</b><br>Diseñado desde cero y escrito en C++.</li>
</ul>
</div>

</div>

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 5: DESVENTAJAS (3-COL CARDS)     ║
╚══════════════════════════════════════════╝
-->

# Desventajas

<div class="flex-three">

<div class="card bash">
<div class="card-header bash">┌─ Bash ─┐</div>
<ul>
<li><span class="text-rose">✗</span> <b>Sintaxis arcaica:</b><br>Un espacio en blanco mal puesto rompe el script.</li>
<li><span class="text-rose">✗</span> <b>Espacios en rutas:</b><br>Olvidar las comillas dobles desarma los argumentos.</li>
<li><span class="text-rose">✗</span> <b>Parseo tedioso:</b><br>Requiere bucles <code>while + case + shift</code> para banderas simples.</li>
<li><span class="text-rose">✗</span> <b>Autocompletado básico:</b><br>Por defecto viene limitado a comandos y archivos locales.</li>
</ul>
</div>

<div class="card zsh">
<div class="card-header zsh">┌─ Zsh ─┐</div>
<ul>
<li><span class="text-rose">✗</span> <b>Requiere configuración:</b><br>Sin plugins externos, es visualmente tan gris como Bash.</li>
<li><span class="text-rose">✗</span> <b>Lentitud:</b><br>Cargar Oh My Zsh con muchos temas puede ralentizar el arranque.</li>
<li><span class="text-rose">✗</span> <b>Sintaxis heredada:</b><br>Mantiene la lógica pesada de usar <code>fi</code>, <code>done</code> y <code>[[ ]]</code>.</li>
<li><span class="text-rose">✗</span> <b>Inconsistencias:</b><br>Algunas funciones nativas de Bash no se comportan igual aquí.</li>
<li><span class="text-rose">✗</span> <b>Dependencias pesadas:</b><br>Oh My Zsh puede convertirse en un monstruo difícil de auditar.</li>
</ul>
</div>

<div class="card fish">
<div class="card-header fish">┌─ Fish ─┐</div>
<ul>
<li><span class="text-rose">✗</span> <b>Incompatibilidad POSIX:</b><br>Los scripts de Bash tradicionales no funcionarán nativamente.</li>
<li><span class="text-rose">✗</span> <b>Ausencia en servidores:</b><br>Rara vez viene instalado por defecto en servidores de producción.</li>
<li><span class="text-rose">✗</span> <b>Ecosistema menor:</b><br>Tiene menos recursos listos para usar que Oh My Zsh.</li>
<li><span class="text-rose">✗</span> <b>Herramientas CLI externas:</b><br>A veces requieren envoltorios como <code>bass</code> o traducción manual.</li>
<li><span class="text-rose">✗</span> <b>Curva de aprendizaje:</b><br>Su sintaxis diferente puede chocar a usuarios veteranos de Bash/Zsh.</li>
</ul>
</div>

</div>

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 6: VARIABLES Y CONDICIONALES     ║
╚══════════════════════════════════════════╝
-->

# Variables y Condicionales

<div class="flex-two">

<div>

##### <span class="zsh">Bash / Zsh</span>

```bash
nombre="42Malaga"

if [ -d "$HOME/Downloads" ]; then
    echo "$nombre: carpeta existe"
fi
```

Reglas estrictas:
- Sin espacios alrededor del `=`
- Espacios **obligatorios** dentro de `[ ]`
- Las comillas dobles protegen espacios

</div>

<div>

##### <span class="fish">Fish</span>

```fish
set nombre "42Malaga"
set -l ruta_local "$HOME/Downloads"
set -gx VARIABLE_GLOBAL "exportada"

if test -d $HOME/Downloads
    echo "Carpeta existe"
end
```

Reglas más flexibles:
- `set` reemplaza al `=` — sin errores de espacios
- `test` sin corchetes, cierra con `end`
- Variables globales con `set -gx`
- Variables locales con `set -l`

</div>

</div>

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 7: ARRAYS Y BUCLES               ║
╚══════════════════════════════════════════╝
-->

# Arrays y Bucles

<div class="flex-two">

<div>

##### <span class="zsh">Bash / Zsh</span>

```bash
extensiones=(js py ts)

for ext in "${extensiones[@]}"; do
    echo "Procesando: $ext"
done
```

Sintaxis pesada: <code>${array[@]}</code>, <code>do</code> / <code>done</code>

</div>

<div>

##### <span class="fish">Fish</span>

```fish
set extensiones js py ts

for ext in $extensiones
    echo "Procesando: $ext"
end
```

- Las listas son nativas: <code>$extensiones</code> ya es una lista
- Sin <code>${array[@]}</code>, sin <code>do</code> / <code>done</code>

</div>

</div>

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 8: BRACE EXPANSION & ARGUMENTOS  ║
╚══════════════════════════════════════════╝
-->

# Brace Expansion & Argumentos

<div class="flex-two">

<div>

##### <span class="zsh">Bash / Zsh</span>

```bash
# Crear carpetas al vuelo
mkdir test{1..4}
mkdir -p proyecto/{js,css}/{src,dist}

# Parseo manual de argumentos
ejemplo_args() {
    local output=""
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -o|--output) output="$2"; shift 2 ;;
            *) echo "Error: $1"; return 1 ;;
        esac
    done
}
```

</div>

<div>

##### <span class="fish">Fish</span>

```fish
# Brace expansion (desde Fish 3.0)
mkdir test{1..4}
mkdir -p proyecto/{js,css}/{src,dist}

# Parseo de argumentos en una línea
function ejemplo_args
    argparse 'o/output=' 'e/ext=+' -- $argv
    echo "Salida: $_flag_output"
    echo "Extensiones: $_flag_ext"
end
```

</div>

</div>

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 9: SECTION — COMPARATIVA DIRECTA ║
╚══════════════════════════════════════════╝
-->
<!-- _class: section -->

# 05. Comparativa Directa

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 10: VARIABLES — TABLE            ║
╚══════════════════════════════════════════╝
-->

# Variables

| Concepto | Bash / Zsh | Fish |
|---|---|---|
| Declarar | `var="x"` | <span class="fish">`set var "x"`</span> |
| Local | `local var="x"` | <span class="fish">`set -l var "x"`</span> |
| Global | `export VAR=x` | <span class="fish">`set -gx VAR x`</span> |
| Espacios en `=` | <span class="text-rose">❌ Prohibido</span> | <span class="text-green">✅ No aplica</span> |

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 11: CONDICIONALES — TABLE        ║
╚══════════════════════════════════════════╝
-->

# Condicionales

| Concepto | Bash / Zsh | Fish |
|---|---|---|
| If | `if [ "$a" = "b" ]` | <span class="fish">`if test $a = "b"`</span> |
| And | `&&` | <span class="fish">`; and`</span> |
| Or | `\|\|` | <span class="fish">`; or`</span> |
| Cierre | `fi` | <span class="text-cyan">**`end`**</span> |

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 12: ARRAYS / LISTAS — TABLE      ║
╚══════════════════════════════════════════╝
-->

# Arrays / Listas

| Concepto | Bash / Zsh | Fish |
|---|---|---|
| Declarar | `arr=(a b)` | <span class="fish">`set arr a b`</span> |
| Acceder | `"${arr[0]}"` (Base 0) | <span class="fish">`$arr[1]` (Base 1)</span> |
| Todos | `"${arr[@]}"` | <span class="fish">`$arr`</span> |
| Longitud | `${#arr[@]}` | <span class="fish">`count $arr`</span> |
| Añadir | `arr+=("x")` | <span class="fish">`set -a arr "x"`</span> |

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 13: BUCLES — TABLE               ║
╚══════════════════════════════════════════╝
-->

# Bucles

| Concepto | Bash / Zsh | Fish |
|---|---|---|
| For rango | `{1..5}` + do/done | <span class="fish">`(seq 1 5)` + end</span> |
| For lista | `"${arr[@]}"` + do/done | <span class="fish">`$arr` + end</span> |
| Cierre | `done` | <span class="text-cyan">**`end`**</span> |

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 14: SECTION — COMPATIBILIDAD     ║
╚══════════════════════════════════════════╝
-->
<!-- _class: section -->

# 06. Compatibilidad y Ecosistema

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 15: EL PROBLEMA POSIX (2-COL)    ║
╚══════════════════════════════════════════╝
-->

# El problema POSIX

<div class="flex-two">

<div>

##### <span class="zsh">Bash / Zsh</span>

```bash
# Esto funciona en Bash/Zsh
# pero NO en Fish
export GOOGLE_CLOUD_PROJECT="mi-proyecto"
source /ruta/init.sh
```

</div>

<div>

##### <span class="fish">Fish</span>

```fish
# Equivalente en Fish
set -gx GOOGLE_CLOUD_PROJECT "mi-proyecto"
bass source /ruta/init.sh
```

</div>

</div>

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 16: PLUGINS FISHER ESENCIALES    ║
╚══════════════════════════════════════════╝
-->

# Plugins Fisher esenciales

| Plugin | Función | Descripción |
|---|---|---|
| `edc/bass` | Ejecuta scripts Bash en Fish | Permite usar herramientas CLI diseñadas para Bash |
| `jorgebucaran/nvm.fish` | NVM nativo ultra-rápido | Gestión de versiones Node.js sin ralentizar el shell |
| `patrickf1/fzf.fish` | Buscador difuso (Ctrl+R visual) | Reemplazo moderno para `history` con vista previa de comandos |
| `jethrokuan/z` | Salto a carpetas frecuentes | Navegación rápida basada en uso reciente |
| `IlanCosman/tide` | Prompt asíncrono moderno | Prompt personalizable con información de Git, tiempo, etc. |
| `franciscolourenco/done` | Notificación de comandos largos | Notifica al terminar comandos que tardan más de 10 segundos |

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 17: INSTALACIÓN RÁPIDA (2-COL)   ║
╚══════════════════════════════════════════╝
-->

# Instalación rápida de plugins

<div class="flex-two">

<div>

##### <span class="fish">Fish (Fisher)</span>

```fish
fisher install edc/bass
fisher install patrickf1/fzf.fish
```

</div>

<div>

##### <span class="zsh">Zsh (Oh My Zsh)</span>

```zsh
# En ~/.zshrc
plugins=(git fzf)
source $ZSH/oh-my-zsh.sh
```

</div>

</div>

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 18: FZF — BUSCADOR DIFUSO       ║
╚══════════════════════════════════════════╝
-->

# fzf: Buscador difuso

![fzf preview](https://raw.githubusercontent.com/junegunn/i/master/fzf-preview.png)

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 19: EZA — LS MEJORADO            ║
╚══════════════════════════════════════════╝
-->

# eza: ls mejorado

![eza screenshots](https://github.com/eza-community/eza/raw/main/docs/images/screenshots.png)

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 20: SECTION — EJEMPLOS DÍA A DÍA║
╚══════════════════════════════════════════╝
-->
<!-- _class: section -->

# Ejemplos del Día a Día (Fish)

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 21: GCPUSH                        ║
╚══════════════════════════════════════════╝
-->

# gcpush

```fish
function gcpush
    git add .
    if test (count $argv) -gt 0
        git commit -m "$argv[1]"
    else
        git commit -m (date "+%d %^b %y %H:%M")
    end
    git push
end

funcsave gcpush
```

**Uso:**
```bash
$> gcpush "Actualización de README"
$> git log --oneline
14538a (HEAD -> main, origin/main, origin/HEAD) Actualización de README
```

O sin mensaje:
```bash
$> gcpush
$> git log --oneline
14538a (HEAD -> main, origin/main, origin/HEAD) 12 MAY 26 13:17
```

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 22: PULLEVERYTHING               ║
╚══════════════════════════════════════════╝
-->

# pulleverything

```fish
function pulleverything
    for dir in */.git
        echo ""
        set_color --bold --underline yellow
        echo (dirname $dir)
        set_color normal
        git -C (dirname $dir) pull
    end
end

funcsave pulleverything
```

**Ejemplo de salida:**
```
ft_printf
Already up to date.

repo_not_sync
Updating 42c9b8a..d1e2f3a
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 23: MEMO                          ║
╚══════════════════════════════════════════╝
-->

# memo

```fish
function memo
    set -l memo_file "$FISH_TOOLS_ROOT/memo.md"
    if test (count $argv) -lt 2
        echo "Usage: memo \"Description\" \"Command\""
        return
    end
    set -l description $argv[1]
    set -l command_text $argv[2]
    if not test -f "$memo_file"
        echo "# Personal Command Memo" > "$memo_file"
    end
    echo -e "\n## $description\n\`\`\`bash\n$command_text\n\`\`\`" >> "$memo_file"
    echo "✅ Saved to: $memo_file"
end

funcsave memo
```

**Uso:**
```fish
memo "Titulo de la entrada o comando" "ls -l"
```

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 24: MEMOSHOW                      ║
╚══════════════════════════════════════════╝
-->

# memoshow

```fish
function memoshow
    cat "$FISH_TOOLS_ROOT/memo.md"
end

funcsave memoshow
```

**Uso:**
```fish
$> memoshow
# Titulo de la entrada o comando
`ls -l`

# Comando anterior
`cat README.md`

# Comando de hace 1 mes
`git log --oneline`
```

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 25: STATUSSEARCH                  ║
╚══════════════════════════════════════════╝
-->

# statussearch

Estado Git de múltiples repositorios:

```fish
function statussearch
    set -l repos (find . -name ".git" -type d)
    for repo in $repos
        set -l parent (dirname $repo)
        echo -n "Checking $parent... "
        git -C $parent fetch --quiet &
        wait
        echo -ne "\r\033[K"
        set -l dinfo (git -C $parent status --porcelain)
        set -l branch_info (git -C $parent status -sb)
        if test -n "$dinfo"
            set_color --bold yellow
            echo "🚧 $parent (Cambios locales)"
            set_color normal
            git -C $parent status -s
            echo ""
        else if string match -q "*behind*" "$branch_info"
            set_color --bold magenta
            echo "📥 $parent (Pendiente de PULL)"
            set_color normal
            echo ""
        else if string match -q "*ahead*" "$branch_info"
            set_color --bold cyan
            echo "🚀 $parent (Pendiente de PUSH)"
            set_color normal
            echo ""
        else
            set_color grey
            echo "✔ $parent"
            set_color normal
        end
    end
end
```

- <code>fetch --quiet</code> para no saturar la salida
- <code>status --porcelain</code> para detectar cambios locales
- <code>status -sb</code> para ver si estamos behind/ahead del remoto

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 26: STATUSSEARCH — SALIDA        ║
╚══════════════════════════════════════════╝
-->

# statussearch: Salida de ejemplo

```
✔ ./path/to/repo1-dev

🚧 ./path/to/repo2 (Cambios locales)
  M project/src/test.c

📥 ./path/to/repo3/README_tutorial (Pendiente de PULL)
```

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 27: LIST_DECLARATIONS            ║
╚══════════════════════════════════════════╝
-->

# list_declarations

Escanea archivos C extrayendo firmas de funciones:

```fish
function list_declarations
    if test (count $argv) -eq 0
        echo "Usage: list_declarations file1.c file2.c ..."; return 1
    end

    for file in $argv
        set -l regex '^'
        set regex "$regex""[ \t]*(static[ \t]+)?"
        set regex "$regex""[a-zA-Z_][a-zA-Z0-9_]*"
        set regex "$regex""([ \t]|\*)+"
        set regex "$regex""[a-zA-Z_][a-zA-Z0-9_]*"
        set regex "$regex""[ \t]*\("
        set -l output (command awk "/$regex/ { print \$0 \";\" }" $file | tr -d '\r')
        echo "// $file N:"(count $output)
        string join \n $output
    end
end
```

**Uso:**
```bash
$> list_declarations parser.c
// parser.c N:5
int	ft_isdigit(int c);
void	skip_spaces(const char *nptr, int *i);
void	parse_sign(const char *str, int *i, int *sign);
int	ft_atoi_strict(const char *str, int *out);
int	check_args(int argc, char **argv);
```

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 28: LIST_DECLARATIONS — BULK     ║
╚══════════════════════════════════════════╝
-->

# list_declarations: Generalización

**Pregunta: ¿Podemos generalizar para todo un proyecto?**

```
src/
├── main.c
├── parser/
│   ├── parser.c
│   ├── parser_utils.c
│   └── lvalidation.c
└── rendering/
```

**Opción 1** — Recursivo con asterisco (Fish nativo):

```fish
function list_decl_bulk
    for i in **/*.c
        list_declarations $i
    end
end
```

**Opción 2** — Con `find`:

```fish
function list_decl_bulk
    for i in (find . -name "*.c")
        list_declarations $i
    end
end
```

**Opción 3** — Con `find -exec`:

```fish
function list_decl_bulk
    find . -name "*.c" -exec list_declarations {} \;
end
```

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 29: SECTION — FISH TOOLS LOADER  ║
╚══════════════════════════════════════════╝
-->
<!-- _class: section -->

# 08. Fish Tools Loader

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 30: ORGANIZACIÓN MODULAR         ║
╚══════════════════════════════════════════╝
-->

# Organización modular

Todas las funciones anteriores se agrupan en un repositorio estructurado:

```
fish_tools/
├── init.fish          # Motor de carga
├── groups/
│   ├── 42tools/       # list_declarations.fish
│   ├── gt/            # gcpush, pulleverything, statussearch
│   └── utils/         # memo, memoshow
```

```fish
# init.fish — Motor de carga automática
set -gx FISH_TOOLS_ROOT (dirname (status filename))

for group_dir in $FISH_TOOLS_ROOT/groups/*/
    for func_file in $group_dir*.fish
        source $func_file
    end
end

echo "fish_tools: "(count $FISH_TOOLS_ROOT/groups/*/*.fish)" funciones cargadas"
```

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 31: SINCRONIZACIÓN VÍA GIT      ║
╚══════════════════════════════════════════╝
-->

# Sincronización vía Git

```fish
# En ~/.config/fish/config.fish
set -gx FISH_TOOLS_ROOT ~/path/to/fish_tools
source $FISH_TOOLS_ROOT/init.fish
```

**Ventajas:**
- Las funciones se cargan automáticamente por grupos temáticos
- El autocompletado con TAB funciona para todos los subcomandos
- Se sincroniza entre máquinas con `git pull` si se guarda en un repositorio
- Cada función es un archivo independiente → fácil de mantener

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 32: SECTION — CONCLUSIÓN         ║
╚══════════════════════════════════════════╝
-->
<!-- _class: section -->

# 09. Conclusión

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 33: ¿CUÁL ELEGIR?               ║
╚══════════════════════════════════════════╝
-->

# ¿Cuál elegir?

| Contexto | Recomendación |
|---|---|
| Servidores / CI/CD / Docker | **Bash** |
| Compartir herramientas en equipo | **Bash** |
| macOS (sin configurar nada) | **Zsh** |
| Personalización total | **Zsh + Oh My Zsh** |
| Productividad local diaria | **Fish** |
| "Que funcione desde el minuto uno" | **Fish** |

---

<!--
╔══════════════════════════════════════════╗
║  SLIDE 34: THANK YOU                     ║
╚══════════════════════════════════════════╝
-->
<!-- _class: lead -->

# <span class="gradient-text">¡Gracias!</span>

## mlermo-j

<span class="text-sm text-muted">42 Málaga · Shells</span>

<style scoped>
.gradient-text {
  font-size: 1.5em;
  background: linear-gradient(to right, #34d399, #60a5fa);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
</style>
