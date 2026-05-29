---
theme: seriph
background: https://images.unsplash.com/photo-1629654297299-c8506221ca97?q=80&w=1920&auto=format&fit=crop
class: text-center
highlighter: shiki
lineNumbers: true
drawings:
  persist: false
transition: slide-left
title: Shell Showdown
---

# Shell Showdown
### Bash, Zsh & Fish: Eficiencia en la Terminal

<div class="text-sm opacity-50">Tutorial para 42 Málaga</div>

---
layout: section
---
# 01. Introducción

<div class="text-xl font-medium tracking-wide mt-2">
  <span class="text-green-400">Bash</span> 
  <span class="text-gray-500 text-lg">vs</span> 
  <span class="text-teal-400">Zsh</span> 
  <span class="text-gray-500 text-lg">vs</span> 
  <span class="text-blue-400">Fish</span>
</div>

---
layout: default
---

# Ecosistema de Shells
Análisis comparativo de características

<div class="grid grid-cols-3 gap-6 mt-8 font-mono">

  <div class="p-5 rounded-xl border border-green-500/20 bg-green-950/10 flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 text-green-400 font-bold text-lg mb-4 border-b border-green-500/20 pb-2">
        <carbon:terminal /> Bash
      </div>
      <ul class="space-y-4 text-sm font-sans text-gray-300">
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Año de lanzamiento</strong> 1989</li>
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Compatibilidad POSIX</strong> 100% Estándar</li>
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Filosofía de Sintaxis</strong> Clásica y estricta</li>
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Experiencia Inicial</strong> Espartana</li>
      </ul>
    </div>
    <div class="mt-4 pt-2 border-t border-white/5 text-xs text-gray-500 font-mono">Plugins: Limitados</div>
  </div>

  <div class="p-5 rounded-xl border border-teal-500/20 bg-teal-950/10 flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 text-teal-400 font-bold text-lg mb-4 border-b border-teal-500/20 pb-2">
        <carbon:settings-adjust /> Zsh
      </div>
      <ul class="space-y-4 text-sm font-sans text-gray-300">
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Año de lanzamiento</strong> 1990</li>
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Compatibilidad POSIX</strong> 99% (Superconjunto)</li>
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Filosofía de Sintaxis</strong> Clásica mejorada</li>
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Experiencia Inicial</strong> Espartana</li>
      </ul>
    </div>
    <div class="mt-4 pt-2 border-t border-white/5 text-xs text-teal-400/70 font-mono">Plugins: Oh My Zsh (Extenso)</div>
  </div>

  <div class="p-5 rounded-xl border border-blue-500/30 bg-blue-950/20 flex flex-col justify-between shadow-lg shadow-blue-950/50">
    <div>
      <div class="flex items-center gap-2 text-blue-400 font-bold text-lg mb-4 border-b border-blue-500/30 pb-2">
        <carbon:fish /> Fish Shell
      </div>
      <ul class="space-y-4 text-sm font-sans text-gray-300">
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Año de lanzamiento</strong> 2005</li>
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Compatibilidad POSIX</strong> 0% (Diseño propio)</li>
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Filosofía de Sintaxis</strong> Moderna (Humana)</li>
        <li><strong class="text-xs uppercase font-mono text-gray-500 block">Experiencia Inicial</strong> Completa e Inteligente</li>
      </ul>
    </div>
    <div class="mt-4 pt-2 border-t border-blue-500/20 text-xs text-blue-400 font-mono">Plugins: Fisher (Ligero/Nativo)</div>
  </div>

</div>

---
layout: three-cols
class: p-8
---

# Ventajas

::left::
<!-- VENTAJAS BASH -->
<div class="text-emerald-400 font-mono font-bold text-lg border-b border-emerald-500/20 pb-1 mb-3">
  <carbon:terminal /> Bash
</div>
<ul class="space-y-2 text-[11px] font-sans text-gray-300 list-none p-0 pr-2">
  <li><span class="text-emerald-400 mr-1">✓</span> <strong class="text-emerald-300">Portabilidad absoluta:</strong><br>Linux, macOS, WSL, servidores, contenedores.</li>
  <li><span class="text-emerald-400 mr-1">✓</span> <strong class="text-emerald-300">Documentación infinita:</strong><br>todo problema ya fue resuelto en internet.</li>
  <li><span class="text-emerald-400 mr-1">✓</span> <strong class="text-emerald-300">Estándar:</strong><br>El rey en CI/CD, Dockerfiles y scripts de instalación.</li>
  <li><span class="text-emerald-400 mr-1">✓</span> <strong class="text-emerald-300">Ligero:</strong><br>Sin dependencias externas y ultra rápido en arranque.</li>
  <li><span class="text-emerald-400 mr-1">✓</span> <strong class="text-emerald-300">Compatibilidad total:</strong><br>Scripts de hace décadas siguen funcionando.</li>
</ul>

::middle::
<!-- VENTAJAS ZSH -->
<div class="text-teal-400 font-mono font-bold text-lg border-b border-teal-500/20 pb-1 mb-3">
  <carbon:settings-adjust /> Zsh
</div>
<ul class="space-y-2 text-[11px] font-sans text-gray-300 list-none p-0 px-1">
  <li><span class="text-teal-400 mr-1">✓</span> <strong class="text-teal-300">Compatibilidad total:</strong><br>Los scripts de Bash funcionan sin cambios.</li>
  <li><span class="text-teal-400 mr-1">✓</span> <strong class="text-teal-300">Oh My Zsh:</strong><br>El mayor ecosistema de plugins y temas de la comunidad.</li>
  <li><span class="text-teal-400 mr-1">✓</span> <strong class="text-teal-300">Personalizable:</strong><br>Puedes redefinir cualquier comportamiento interno.</li>
  <li><span class="text-teal-400 mr-1">✓</span> <strong class="text-teal-300">Nativo en Apple:</strong><br>Es la Shell por defecto en macOS actualmente.</li>
  <li><span class="text-teal-400 mr-1">✓</span> <strong class="text-teal-300">Mejor autocompletado:</strong><br>Supera a Bash ampliamente.</li>
  <li><span class="text-teal-400 mr-1">✓</span> <strong class="text-teal-300">Arrays flexibles:</strong><br>Manipulación limpia sin requerir <code>${array[@]}</code>.</li>
</ul>

::right::
<!-- VENTAJAS FISH -->
<div class="text-blue-400 font-mono font-bold text-lg border-b border-blue-500/20 pb-1 mb-3">
  <carbon:fish /> Fish
</div>
<ul class="space-y-2 text-[11px] font-sans text-gray-300 list-none p-0 pl-2">
  <li><span class="text-blue-400 mr-1">✓</span> <strong class="text-blue-300">Autocompletado nativo:</strong><br>Lee páginas <code>man</code> y sugiere comandos en gris.</li>
  <li><span class="text-blue-400 mr-1">✓</span> <strong class="text-blue-300">Sintaxis limpia:</strong><br>Adiós a <code>do/done/fi</code>, todo termina con <code>end</code>.</li>
  <li><span class="text-blue-400 mr-1">✓</span> <strong class="text-blue-300"><code>argparse</code> integrado:</strong><br>Procesa banderas avanzadas en una sola línea.</li>
  <li><span class="text-blue-400 mr-1">✓</span> <strong class="text-blue-300">Listas nativas:</strong><br>Manejo de arrays real sin comillas de protección.</li>
  <li><span class="text-blue-400 mr-1">✓</span> <strong class="text-blue-300"><code>funcsave</code>:</strong><br>Guardado instantáneo de funciones desde la terminal.</li>
  <li><span class="text-blue-400 mr-1">✓</span> <strong class="text-blue-300">Rápido y robusto:</strong><br>Diseñado desde cero y escrito en C++.</li>
</ul>

---
layout: three-cols
class: p-8
---

# Desventajas

::left::
<!-- DESVENTAJAS BASH -->
<div class="text-emerald-400 font-mono font-bold text-lg border-b border-emerald-500/20 pb-1 mb-3">
  <carbon:terminal /> Bash
</div>
<ul class="space-y-2 text-[11px] font-sans text-gray-300 list-none p-0 pr-2">
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-emerald-300">Sintaxis arcaica:</strong><br>Un espacio en blanco mal puesto rompe el script por completo.</li>
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-emerald-300">Espacios en rutas:</strong><br>Olvidar las comillas dobles desarma los argumentos.</li>
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-emerald-300">Parseo tedioso:</strong><br>Requiere bucles <code>while + case + shift</code> para banderas simples.</li>
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-emerald-300">Autocompletado básico:</strong><br>Por defecto viene limitado a comandos y archivos locales.</li>
</ul>

::middle::
<!-- DESVENTAJAS ZSH -->
<div class="text-teal-400 font-mono font-bold text-lg border-b border-teal-500/10 pb-1 mb-3">
  <carbon:settings-adjust /> Zsh
</div>
<ul class="space-y-2 text-[11px] font-sans text-gray-300 list-none p-0 px-1">
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-teal-300">Requiere configuración:</strong><br>Sin plugins externos, es visualmente tan gris como Bash.</li>
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-teal-300">Lentitud:</strong><br>Cargar Oh My Zsh con muchos temas puede ralentizar el arranque.</li>
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-teal-300">Sintaxis heredada:</strong><br>Mantiene la lógica pesada de usar <code>fi</code>, <code>done</code> y <code>[[ ]]</code>.</li>
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-teal-300">Inconsistencias:</strong><br>Algunas funciones nativas de Bash no se comportan igual aquí.</li>
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-teal-300">Dependencias pesadas:</strong><br>Oh My Zsh puede convertirse en un monstruo difícil de auditar.</li>
</ul>

::right::
<!-- DESVENTAJAS FISH -->
<div class="text-blue-400 font-mono font-bold text-lg border-b border-blue-500/20 pb-1 mb-3">
  <carbon:fish /> Fish
</div>
<ul class="space-y-2 text-[11px] font-sans text-gray-300 list-none p-0 pl-2">
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-blue-300">Incompatibilidad POSIX:</strong><br>Los scripts de Bash tradicionales no funcionarán nativamente.</li>
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-blue-300">Ausencia en servidores:</strong><br>Rara vez viene instalado por defecto en servidores de producción.</li>
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-blue-300">Ecosistema menor:</strong><br>Tiene menos recursos listos para usar que Oh My Zsh.</li>
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-blue-300">Herramientas CLI externas:</strong><br>A veces requieren envoltorios como <code>bass</code> o traducción manual.</li>
  <li><span class="text-rose-400 mr-1">✗</span> <strong class="text-blue-300">Curva de aprendizaje:</strong><br>Su sintaxis diferente puede chocar a usuarios veteranos de Bash/Zsh.</li>
</ul>
---
layout: two-cols-title
---

# Variables y Condicionales

::left::

# <span class="text-teal-400">Bash/Zsh</span>
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

::right::

# <span class="text-blue-400">Fish</span>
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
- Variables globales con `set -gx`, locales con `set -l`

---
layout: two-cols-title
---

# Arrays y Bucles

::left::
# <span class="text-teal-400">Bash/Zsh</span>

```bash
extensiones=(js py ts)

for ext in "${extensiones[@]}"; do
    echo "Procesando: $ext"
done
```

Sintaxis pesada: `${array[@]}`, `do`/`done`

::right::
# <span class="text-blue-400">Fish</span>
```fish
set extensiones js py ts

for ext in $extensiones
    echo "Procesando: $ext"
end
```

- Las listas son nativas: `$extensiones` ya es una lista
- Sin `${array[@]}`, sin `do`/`done`

---
layout: two-cols-title
---

# Brace Expansion & Argumentos

::left::
# <span class="text-teal-400">Bash/Zsh</span>
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

::right::
# <span class="text-blue-400">Fish</span>
```fish
# Parseo de argumentos en una línea
function ejemplo_args
    argparse 'o/output=' 'e/ext=+' -- $argv
    echo "Salida: $_flag_output"
    echo "Extensiones: $_flag_ext"
end

# Brace expansion (desde Fish 3.0)
mkdir test{1..4}
mkdir -p proyecto/{js,css}/{src,dist}
```


---
layout: section
---

# 05. Comparativa Directa

---
layout: section
---

# Variables

<div class="mt-4 overflow-hidden rounded-xl border border-white border-opacity-10 bg-slate-900 bg-opacity-40 shadow-xl font-mono text-xs">
  <table class="w-full text-left border-collapse">
    <thead>
      <tr class="bg-slate-800/50 border-b border-white/10">
        <th class="p-3 font-bold text-gray-400 uppercase tracking-wider text-[11px]">Concepto</th>
        <th class="p-3 font-bold text-teal-400 uppercase tracking-wider text-[11px]">Bash / Zsh</th>
        <th class="p-3 font-bold text-blue-400 uppercase tracking-wider text-[11px]">Fish</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-white/5 text-gray-300">
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Declarar</td>
        <td class="p-3"><code>var="x"</code></td>
        <td class="p-3 text-emerald-400"><code>set var "x"</code></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Local</td>
        <td class="p-3"><code>local var="x"</code></td>
        <td class="p-3 text-emerald-400"><code>set -l var "x"</code></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Global</td>
        <td class="p-3"><code>export VAR=x</code></td>
        <td class="p-3 text-emerald-400"><code>set -gx VAR x</code></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Espacios en <code>=</code></td>
        <td class="p-3"><span class="px-1.5 py-0.5 bg-red-500/10 text-red-400 rounded text-[10px]">❌ Prohibido</span></td>
        <td class="p-3"><span class="px-1.5 py-0.5 bg-green-500/10 text-green-400 rounded text-[10px]">✅ No aplica</span></td>
      </tr>
    </tbody>
  </table>
</div>

---
layout: section
---

# Condicionales

<div class="mt-4 overflow-hidden rounded-xl border border-white border-opacity-10 bg-slate-900 bg-opacity-40 shadow-xl font-mono text-xs">
  <table class="w-full text-left border-collapse">
    <thead>
      <tr class="bg-slate-800/50 border-b border-white/10">
        <th class="p-3 font-bold text-gray-400 uppercase tracking-wider text-[11px]">Concepto</th>
        <th class="p-3 font-bold text-teal-400 uppercase tracking-wider text-[11px]">Bash / Zsh</th>
        <th class="p-3 font-bold text-blue-400 uppercase tracking-wider text-[11px]">Fish</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-white/5 text-gray-300">
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">If</td>
        <td class="p-3"><code>if [ "$a" = "b" ]</code></td>
        <td class="p-3 text-emerald-400"><code>if test $a = "b"</code></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">And</td>
        <td class="p-3"><code>&&</code> <span class="text-gray-500 font-sans text-[11px]">en [ ]</span></td>
        <td class="p-3 text-emerald-400"><code>; and</code></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Or</td>
        <td class="p-3"><code>||</code> <span class="text-gray-500 font-sans text-[11px]">en [ ]</span></td>
        <td class="p-3 text-emerald-400"><code>; or</code></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Cierre</td>
        <td class="p-3 text-gray-400"><code>fi</code></td>
        <td class="p-3 text-cyan-400 font-bold"><code>end</code></td>
      </tr>
    </tbody>
  </table>
</div>

---
layout: section
---

# Arrays / Listas

<div class="mt-4 overflow-hidden rounded-xl border border-white border-opacity-10 bg-slate-900 bg-opacity-40 shadow-xl font-mono text-xs">
  <table class="w-full text-left border-collapse">
    <thead>
      <tr class="bg-slate-800/50 border-b border-white/10">
        <th class="p-3 font-bold text-gray-400 uppercase tracking-wider text-[11px]">Concepto</th>
        <th class="p-3 font-bold text-teal-400 uppercase tracking-wider text-[11px]">Bash / Zsh</th>
        <th class="p-3 font-bold text-blue-400 uppercase tracking-wider text-[11px]">Fish</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-white/5 text-gray-300">
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Declarar</td>
        <td class="p-3"><code>arr=(a b)</code></td>
        <td class="p-3 text-emerald-400"><code>set arr a b</code></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Acceder</td>
        <td class="p-3"><code>"${arr[0]}"</code> <span class="text-gray-500 font-sans text-[10px]">(Base 0)</span></td>
        <td class="p-3 text-emerald-400"><code>$arr[1]</code> <span class="text-blue-400 font-sans text-[10px]">(Base 1)</span></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Todos</td>
        <td class="p-3"><code>"${arr[@]}"</code></td>
        <td class="p-3 text-emerald-400"><code>$arr</code></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Longitud</td>
        <td class="p-3"><code>${#arr[@]}</code></td>
        <td class="p-3 text-emerald-400"><code>count $arr</code></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Añadir</td>
        <td class="p-3"><code>arr+=("x")</code></td>
        <td class="p-3 text-emerald-400"><code>set -a arr "x"</code></td>
      </tr>
    </tbody>
  </table>
</div>

---
layout: section
---

# Bucles

<div class="mt-4 overflow-hidden rounded-xl border border-white border-opacity-10 bg-slate-900 bg-opacity-40 shadow-xl font-mono text-xs">
  <table class="w-full text-left border-collapse">
    <thead>
      <tr class="bg-slate-800/50 border-b border-white/10">
        <th class="p-3 font-bold text-gray-400 uppercase tracking-wider text-[11px]">Concepto</th>
        <th class="p-3 font-bold text-teal-400 uppercase tracking-wider text-[11px]">Bash / Zsh</th>
        <th class="p-3 font-bold text-blue-400 uppercase tracking-wider text-[11px]">Fish</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-white/5 text-gray-300">
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">For rango</td>
        <td class="p-3"><code>{1..5}</code> <span class="text-gray-500 font-sans text-[11px]">+ do/done</span></td>
        <td class="p-3 text-emerald-400"><code>(seq 1 5)</code> <span class="text-gray-500 font-sans text-[11px]">+ end</span></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">For lista</td>
        <td class="p-3"><code>"${arr[@]}"</code> <span class="text-gray-500 font-sans text-[11px]">+ do/done</span></td>
        <td class="p-3 text-emerald-400"><code>$arr</code> <span class="text-gray-500 font-sans text-[11px]">+ end</span></td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans font-semibold text-white">Cierre</td>
        <td class="p-3 text-gray-400"><code>done</code></td>
        <td class="p-3 text-cyan-400 font-bold"><code>end</code></td>
      </tr>
    </tbody>
  </table>
</div>
---
layout: section
---

# 06. Compatibilidad y Ecosistema

---
layout: two-cols-title
---

# El problema POSIX

::left::

```bash
# Esto funciona en Bash/Zsh pero NO en Fish
export GOOGLE_CLOUD_PROJECT="mi-proyecto"
source /ruta/init.sh
```

::right::

```fish
# Equivalente en Fish
set -gx GOOGLE_CLOUD_PROJECT "mi-proyecto"
bass source /ruta/init.sh
```

---

# Plugins Fisher esenciales

<div class="mt-4 overflow-hidden rounded-xl border border-white border-opacity-10 bg-slate-900 bg-opacity-40 shadow-xl font-mono text-xs">
  <table class="w-full text-left border-collapse">
    <thead>
      <tr class="bg-slate-800/50 border-b border-white/10">
        <th class="p-3 font-bold text-gray-400 uppercase tracking-wider text-[11px]">Plugin</th>
        <th class="p-3 font-bold text-teal-400 uppercase tracking-wider text-[11px]">Función</th>
        <th class="p-3 font-bold text-blue-400 uppercase tracking-wider text-[11px]">Descripción</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-white/5 text-gray-300">
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 text-teal-400"><code>edc/bass</code></td>
        <td class="p-3 font-sans text-white">Ejecuta scripts Bash en Fish</td>
        <td class="p-3">Permite usar herramientas CLI diseñadas para Bash</td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 text-teal-400"><code>jorgebucaran/nvm.fish</code></td>
        <td class="p-3 font-sans text-white">NVM nativo ultra-rápido</td>
        <td class="p-3">Gestión de versiones Node.js sin ralentizar el shell</td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 text-teal-400"><code>patrickf1/fzf.fish</code></td>
        <td class="p-3 font-sans text-white">Buscador difuso (Ctrl+R visual)</td>
        <td class="p-3">Reemplazo moderno para <code>history</code> con vista previa de comandos</td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 text-teal-400"><code>jethrokuan/z</code></td>
        <td class="p-3 font-sans text-white">Salto a carpetas frecuentes</td>
        <td class="p-3">Navegación rápida basada en uso reciente</td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 text-teal-400"><code>IlanCosman/tide</code></td>
        <td class="p-3 font-sans text-white">Prompt asíncrono moderno</td>
        <td class="p-3">Prompt personalizable con información de Git, tiempo, etc.</td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 text-teal-400"><code>franciscolourenco/done</code></td>
        <td class="p-3 font-sans text-white">Notificación de comandos largos</td>
        <td class="p-3">Notifica al terminar comandos que tardan más de 10 segundos</td>
      </tr>
    </tbody>
  </table>
</div>

---
layout: two-cols-title
---

# Instalación rápida de plugins

::left::

## <span class="text-blue-400">For Fish (Fisher)</span>
```fish
fisher install edc/bass
fisher install patrickf1/fzf.fish
```
::right::

## <span class="text-teal-400">For Zsh (Oh My Zsh)</span>

```zsh
# En ~/.zshrc
plugins=(git fzf)
source $ZSH/oh-my-zsh.sh
```

---

# fzf: Buscador difuso

<div class="h-96 flex justify-center">
  <img src="https://raw.githubusercontent.com/junegunn/i/master/fzf-preview.png" class="h-full object-contain" />
</div>

---

# eza: ls mejorado

<div class="h-96 flex justify-center">
  <img src="https://github.com/eza-community/eza/raw/main/docs/images/screenshots.png" class="h-full object-contain" />
</div>



---
layout: section
---

# Ejemplos del Día a Día (Fish)

---

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

## Uso
```bash
$>gcpush "Actualización de README"
$>git log --oneline
14538a (HEAD -> main, origin/main, origin/HEAD) Actualización de README
```

O sin mensaje:
```bash
$>gcpush
$>git log --oneline
14538a (HEAD -> main, origin/main, origin/HEAD) 12 MAY 26 13:17
```


---

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


<pre class="bg-[#1e1e1e] p-4 rounded-md text-sm font-mono mt-4 border border-gray-700 max-h-80 overflow-y-auto w-full relative">
<span class="text-[#f5f543] font-bold">ft_printf</span>
Already up to date.

<span class="text-[#f5f543] font-bold">repo_not_sync</span>
Updating 42c9b8a..d1e2f3a
Fast-forward
 README.md | 2 <span class="text-green-400">+</span><span class="text-red-400">-</span>
 1 file changed, <span class="text-green-400">1 insertion(+)</span>, <span class="text-red-400">1 deletion(-)</span>

</pre>


---

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

## Uso

```fish
memo "Titulo de la entrada o comando" "ls -l"
```


---

# memoshow
```fish
function memoshow
    cat "$FISH_TOOLS_ROOT/memo.md"
end

funcsave memoshow
```

## Uso

```fish
$>memoshow
# Titulo de la entrada o comando
`ls -l`

# Comando anterior
`cat README.md`

# Comando de hace 1 mes
`git log --oneline`
```

---
layout: two-cols-title
---

# statussearch

Estado Git de múltiples repositorios:

::left::

<div style="--slidev-code-font-size: 0.47rem; --slidev-code-line-height: 1.15;">

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
            echo "📥 $parent (Pendiente de PULL - Hay cambios en GitHub)"
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

</div>

::right::

```fish
$>find . -name ".git" -type d
./repo1/.git
./repo2/.git
./repo3/.git
```
- `fetch --quiet ` para no saturar la salida
- `status --porcelain` para detectar cambios locales
- `status -sb` para ver si estamos behind/ahead del remoto.

---

# statussearch: Salida de ejemplo

<pre class="bg-[#1e1e1e] p-4 rounded-md text-sm font-mono mt-4 border border-gray-700 w-full relative">
<span class="text-gray-400">✔ ./000_42Repos/Current/Minishell-dev</span>

<span class="text-[#f5f543] font-bold">🚧 ./000_42Repos/Current/42Malaga (Cambios locales)</span>
 <span class="text-red-400">M</span> Presentacion_Bash_Fish/Shells_42M/slides.md

<span class="text-pink-400 font-bold">📥 ./repo_inventado/README_tutorial (Pendiente de PULL)</span>
</pre>

---

# list_declarations

Escanea archivos C extrayendo firmas de funciones:

```fish
function list_declarations
    if test (count $argv) -eq 0
        echo "Usage: list_declarations file1.c file2.c ..."; return 1
    end

    for file in $argv
        set -l regex '^'                           # Inicio de línea
        set regex "$regex""[ \t]*(static[ \t]+)?"  # Opcional "static" al inicio
        set regex "$regex""[a-zA-Z_][a-zA-Z0-9_]*" # Tipo de retorno (int, void, char*, etc.)
        set regex "$regex""([ \t]|\*)+"            # Espacios o asteriscos entre tipo y nombre
        set regex "$regex""[a-zA-Z_][a-zA-Z0-9_]*" # Nombre de la función
        set regex "$regex""[ \t]*\("               # Espacios opcionales antes del paréntesis de apertura

        # Ejecutamos pasando la regex limpia
        set -l output (command awk "/$regex/ { print \$0 \";\" }" $file | tr -d '\r')
        
        echo "// $file N:"(count $output)
        string join \n $output
    end
end
```
---

<div class="text-xs uppercase font-mono text-gray-400 tracking-wider border-b border-white/10 pb-1 mb-3">Uso</div>

```bash
$>list_declarations parser.c
// parser.c N:5
int	ft_isdigit(int c);
void	skip_spaces(const char *nptr, int *i);
void	parse_sign(const char *str, int *i, int *sign);
int	ft_atoi_strict(const char *str, int *out);
int	check_args(int argc, char **argv);
```

<div class="mt-6"></div>

<div class="text-xs uppercase font-mono text-gray-400 tracking-wider border-b border-white/10 pb-1 mb-3">Pregunta: ¿Podemos generalizar para todo un proyecto?</div>

```text
src/
├── main.c
├── parser.c
└── utils.c
```

<v-click>

```fish
function list_decl_bulk
    for i in *.c 
        list_declarations $i
    end
end
```
</v-click>

---

<div class="text-xs uppercase font-mono text-gray-400 tracking-wider border-b border-white/10 pb-1 mb-3">Pregunta: ¿Podemos generalizar para todo un proyecto?</div>

```text
src/
├── main.c
├── parser/
│   ├── parser.c
│   ├── parser_utils.c
│   └── lvalidation.c 
└── rendering/
```

<v-click>

```fish
function list_decl_bulk
	for i in **/*.c
		list_declarations $i
	end
end
```

</v-click>

<v-click>

```fish
function list_decl_bulk
	for i in (find . -name "*.c")
		list_declarations $i
	end
end
```

</v-click>

<v-click>

```fish
function list_decl_bulk
	find . -name "*.c" -exec list_declarations {} \;
end
```
</v-click>

---
layout: section
---

# 08. Fish Tools Loader

---

# Organización modular

Todas las funciones anteriores se agrupan en un repositorio estructurado:

```
fish_tools/
├── init.fish          # Motor de carga
├── groups/
│   ├── 42tools/         # list_declarations.fish
│   ├── gt/            # gcpush, pulleverything, statussearch
│   ├── utils/         # memo, memoshow
```

```fish
# init.fish — Motor de carga automática
set -gx FISH_TOOLS_ROOT (dirname (status filename))

for group_dir in $FISH_TOOLS_ROOT/groups/*/
    for func_file in $group_dir*.fish
        source $func_file
    end
end

echo "fish_tools: " (count $FISH_TOOLS_ROOT/groups/*/*.fish) "funciones cargadas"
```

---

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
layout: section
---

# 09. Conclusión

---
layout: default
---

# ¿Cuál elegir?

<div class="mt-4 overflow-hidden rounded-xl border border-white border-opacity-10 bg-slate-900 bg-opacity-40 shadow-xl font-mono text-xs">
  <table class="w-full text-left border-collapse">
    <thead>
      <tr class="bg-slate-800/50 border-b border-white/10">
        <th class="p-3 font-bold text-gray-400 uppercase tracking-wider text-[11px]">Contexto</th>
        <th class="p-3 font-bold text-teal-400 uppercase tracking-wider text-[11px]">Recomendación</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-white/5 text-gray-300">
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans text-white">Servidores / CI/CD / Docker</td>
        <td class="p-3 font-bold text-teal-400">Bash</td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans text-white">Compartir herramientas en equipo</td>
        <td class="p-3 font-bold text-teal-400">Bash</td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans text-white">macOS (sin configurar nada)</td>
        <td class="p-3 font-bold text-teal-400">Zsh</td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans text-white">Personalización total</td>
        <td class="p-3 font-bold text-teal-400">Zsh + Oh My Zsh</td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans text-white">Productividad local diaria</td>
        <td class="p-3 font-bold text-blue-400">Fish</td>
      </tr>
      <tr class="hover:bg-white/5 transition-colors">
        <td class="p-3 font-sans text-white">"Que funcione desde el minuto uno"</td>
        <td class="p-3 font-bold text-blue-400">Fish</td>
      </tr>
    </tbody>
  </table>
</div>

---
layout: center
class: text-center
---


<div class="pt-8">
  <!-- font-mono le da el toque C/Terminal. text-7xl lo hace enorme -->
  <!-- bg-gradient-to-r crea un degradado que se aplica al texto -->
  <span class="font-mono text-7xl font-extrabold tracking-wider bg-gradient-to-r from-green-400 to-blue-500 bg-clip-text text-transparent opacity-90 drop-shadow-lg">
    ¡Gracias!
  </span>
</div>

# mlermo-j

<div class="mt-4 text-sm opacity-40 font-mono">
  42 Málaga · Shells
</div>

