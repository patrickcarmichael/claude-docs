---
title: "Ignorar archivos"
source: "https://docs.cursor.com/es/context/ignore-files"
language: "es"
language_name: "Spanish"
---

# Ignorar archivos
Source: https://docs.cursor.com/es/context/ignore-files

Control del acceso a archivos con .cursorignore y .cursorindexingignore

<div id="overview">
  ## Descripción general
</div>

Cursor lee e indexa el código de tu proyecto para habilitar sus funciones. Controla a qué directorios y archivos puede acceder Cursor usando un archivo `.cursorignore` en tu directorio raíz.

Cursor bloquea el acceso a los archivos listados en `.cursorignore` para:

* Indexación del código base
* Código accesible por [Tab](/es/tab/overview), [Agent](/es/agent/overview) y [Inline Edit](/es/inline-edit/overview)
* Código accesible mediante [referencias con el símbolo @](/es/context/@-symbols/overview)

<Warning>
  Las llamadas a herramientas iniciadas por Agent, como la terminal y los servidores MCP, no pueden bloquear
  el acceso al código gobernado por `.cursorignore`
</Warning>

<div id="why-ignore-files">
  ## ¿Por qué ignorar archivos?
</div>

**Seguridad**: Restringe el acceso a claves de API, credenciales y secretos. Aunque Cursor bloquea los archivos ignorados, no se puede garantizar una protección total debido a la imprevisibilidad de los LLM.

**Rendimiento**: En bases de código grandes o monorepos, excluye partes irrelevantes para un indexado más rápido y una detección de archivos más precisa.

<div id="global-ignore-files">
  ## Archivos globales de ignore
</div>

Configura patrones de ignore para todos los proyectos en la configuración de usuario y así excluir archivos sensibles sin tener que configurar cada proyecto por separado.

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d5bb9e6b18ca466ec69ddd1b216320c9" alt="Lista global de ignore de Cursor" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/settings/global-ignore.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ce566e71f1fcac6a85942f9fbb741889 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=c833cf55c470463ce31ae936ee122971 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=a3c3f6c6b40a9e91487237f0cf37cbca 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=03284fab1ddfadb64346dc912ea97048 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=5bd5b338808979f9fa42faa7df69d39a 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=676448c72358de369a119b34a8dcf9c5 2500w" />
</Frame>

Los patrones predeterminados incluyen:

* Archivos de entorno: `**/.env`, `**/.env.*`
* Credenciales: `**/credentials.json`, `**/secrets.json`
* Claves: `**/*.key`, `**/*.pem`, `**/id_rsa`

<div id="configuring-cursorignore">
  ## Configurar `.cursorignore`
</div>

Crea un archivo `.cursorignore` en tu directorio raíz usando la sintaxis de `.gitignore`.

<div id="pattern-examples">
  ### Ejemplos de patrones
</div>

```sh  theme={null}
config.json      # Archivo específico
dist/           # Directorio
*.log           # Extensión de archivo
**/logs         # Directorios anidados
!app/           # Quitar de la lista de ignorados (negación)
```

<div id="hierarchical-ignore">
  ### Ignorar jerárquico
</div>

Activa `Cursor Settings` > `Features` > `Editor` > `Hierarchical Cursor Ignore` para buscar en los directorios superiores archivos `.cursorignore`.

**Notas**: Los comentarios empiezan con `#`. Los patrones posteriores reemplazan a los anteriores. Los patrones son relativos a la ubicación del archivo.

<div id="limit-indexing-with-cursorindexingignore">
  ## Limita la indexación con `.cursorindexingignore`
</div>

Usa `.cursorindexingignore` para excluir archivos únicamente de la indexación. Estos archivos siguen estando disponibles para las funciones de IA, pero no aparecerán en las búsquedas del código.

<div id="files-ignored-by-default">
  ## Archivos ignorados de forma predeterminada
</div>

Cursor ignora automáticamente los archivos de `.gitignore` y la lista de ignorados predeterminada de abajo. Podés anular esto con el prefijo `!` en `.cursorignore`.

<Accordion title="Lista de ignorados predeterminada">
  Solo para indexación, estos archivos se ignoran además de los que estén en tu `.gitignore`, `.cursorignore` y `.cursorindexingignore`:

  ```sh  theme={null}
  package-lock.json
  pnpm-lock.yaml
  yarn.lock
  composer.lock
  Gemfile.lock
  bun.lockb
  .env*
  .git/
  .svn/
  .hg/
  *.lock
  *.bak
  *.tmp
  *.bin
  *.exe
  *.dll
  *.so
  *.lockb
  *.qwoff
  *.isl
  *.csv
  *.pdf
  *.doc
  *.doc
  *.xls
  *.xlsx
  *.ppt
  *.pptx
  *.odt
  *.ods
  *.odp
  *.odg
  *.odf
  *.sxw
  *.sxc
  *.sxi
  *.sxd
  *.sdc
  *.jpg
  *.jpeg
  *.png
  *.gif
  *.bmp
  *.tif
  *.mp3
  *.wav
  *.wma
  *.ogg
  *.flac
  *.aac
  *.mp4
  *.mov
  *.wmv
  *.flv
  *.avi
  *.zip
  *.tar
  *.gz
  *.7z
  *.rar
  *.tgz
  *.dmg
  *.iso
  *.cue
  *.mdf
  *.mds
  *.vcd
  *.toast
  *.img
  *.apk
  *.msi
  *.cab
  *.tar.gz
  *.tar.xz
  *.tar.bz2
  *.tar.lzma
  *.tar.Z
  *.tar.sz
  *.lzma
  *.ttf
  *.otf
  *.pak
  *.woff
  *.woff2
  *.eot
  *.webp
  *.vsix
  *.rmeta
  *.rlib
  *.parquet
  *.svg
  .egg-info/
  .venv/
  node_modules/
  __pycache__/
  .next/
  .nuxt/
  .cache/
  .sass-cache/
  .gradle/
  .DS_Store/
  .ipynb_checkpoints/
  .pytest_cache/
  .mypy_cache/
  .tox/
  .git/
  .hg/
  .svn/
  .bzr/
  .lock-wscript/
  .Python/
  .jupyter/
  .history/
  .yarn/
  .yarn-cache/
  .eslintcache/
  .parcel-cache/
  .cache-loader/
  .nyc_output/
  .node_repl_history/
  .pnp.js/
  .pnp/
  ```
</Accordion>

<div id="negation-pattern-limitations">
  ### Limitaciones de los patrones de negación
</div>

Al usar patrones de negación (con el prefijo `!`), no podés volver a incluir un archivo si un directorio padre está excluido mediante `*`.

```sh  theme={null}

---

← Previous: [Indexación del codebase](./indexacin-del-codebase.md) | [Index](./index.md) | Next: [Protocolo de Contexto del Modelo (MCP)](./protocolo-de-contexto-del-modelo-mcp.md) →