---
title: "Dateien ignorieren"
source: "https://docs.cursor.com/de/context/ignore-files"
language: "de"
language_name: "German"
---

# Dateien ignorieren
Source: https://docs.cursor.com/de/context/ignore-files

Datei­zugriff mit .cursorignore und .cursorindexingignore steuern

<div id="overview">
  ## Überblick
</div>

Cursor liest und indexiert den Code deines Projekts, um seine Funktionen bereitzustellen. Steuere, auf welche Verzeichnisse und Dateien Cursor zugreifen kann, indem du eine `.cursorignore`-Datei im Root-Verzeichnis verwendest.

Cursor blockiert den Zugriff auf in `.cursorignore` aufgeführte Dateien für:

* Codebase-Indexierung
* Code, auf den [Tab](/de/tab/overview), [Agent](/de/agent/overview) und [Inline Edit](/de/inline-edit/overview) zugreifen können
* Code, der über [@-Symbol-Referenzen](/de/context/@-symbols/overview) zugänglich ist

<Warning>
  Vom Agent initiierte Tool-Aufrufe, z. B. Terminal und MCP-Server, können
  den Zugriff auf Code, der durch `.cursorignore` gesteuert wird, nicht blockieren
</Warning>

<div id="why-ignore-files">
  ## Warum Dateien ignorieren?
</div>

**Sicherheit**: Den Zugriff auf API-Schlüssel, Zugangsdaten und Secrets einschränken. Cursor blockiert ignorierte Dateien, aber vollständiger Schutz ist wegen der Unvorhersehbarkeit von LLMs nicht garantiert.

**Performance**: In großen Codebases oder Monorepos irrelevante Bereiche ausschließen, um schneller zu indexieren und Dateien genauer zu finden.

<div id="global-ignore-files">
  ## Globale Ignore-Dateien
</div>

Leg in den Benutzereinstellungen Ignore-Muster für alle Projekte fest, um sensible Dateien ohne projektweise Konfiguration auszuschließen.

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d5bb9e6b18ca466ec69ddd1b216320c9" alt="Globale Cursor Ignore-Liste" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/settings/global-ignore.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ce566e71f1fcac6a85942f9fbb741889 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=c833cf55c470463ce31ae936ee122971 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=a3c3f6c6b40a9e91487237f0cf37cbca 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=03284fab1ddfadb64346dc912ea97048 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=5bd5b338808979f9fa42faa7df69d39a 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=676448c72358de369a119b34a8dcf9c5 2500w" />
</Frame>

Standardmuster sind:

* Umgebungsdateien: `**/.env`, `**/.env.*`
* Zugangsdaten: `**/credentials.json`, `**/secrets.json`
* Schlüssel: `**/*.key`, `**/*.pem`, `**/id_rsa`

<div id="configuring-cursorignore">
  ## Konfigurieren von `.cursorignore`
</div>

Erstell in deinem Root-Verzeichnis eine `.cursorignore`-Datei mit der `.gitignore`-Syntax.

<div id="pattern-examples">
  ### Beispielmuster
</div>

```sh  theme={null}
config.json      # Konkrete Datei
dist/           # Verzeichnis
*.log           # Dateiendung
**/logs         # Verschachtelte Verzeichnisse
!app/           # Von der Ignorierliste ausnehmen (Negation)
```

<div id="hierarchical-ignore">
  ### Hierarchisches Ignorieren
</div>

Aktiviere `Cursor Settings` > `Features` > `Editor` > `Hierarchical Cursor Ignore`, um in übergeordneten Verzeichnissen nach `.cursorignore`-Dateien zu suchen.

**Hinweise**: Kommentare beginnen mit `#`. Spätere Muster überschreiben frühere. Muster sind relativ zum Speicherort der Datei.

<div id="limit-indexing-with-cursorindexingignore">
  ## Indizierung mit `.cursorindexingignore` begrenzen
</div>

Verwende `.cursorindexingignore`, um Dateien ausschließlich von der Indizierung auszunehmen. Diese Dateien bleiben für AI‑Features zugänglich, werden aber nicht in Codebase‑Suchen angezeigt.

<div id="files-ignored-by-default">
  ## Standardmäßig ignorierte Dateien
</div>

Cursor ignoriert automatisch Dateien in `.gitignore` sowie in der unten aufgeführten Standard-Ignorierliste. Du kannst das mit dem Präfix `!` in `.cursorignore` überschreiben.

<Accordion title="Standard-Ignorierliste">
  Nur für das Indexing werden diese Dateien zusätzlich zu den Dateien in deiner `.gitignore`, `.cursorignore` und `.cursorindexingignore` ignoriert:

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
  ### Einschränkungen von Negationsmustern
</div>

Wenn du Negationsmuster verwendest (mit `!` vorangestellt), kannst du eine Datei nicht erneut einbeziehen, wenn ein übergeordnetes Verzeichnis per \* ausgeschlossen wurde.

```sh  theme={null}

---

← Previous: [Codebase-Indexierung](./codebase-indexierung.md) | [Index](./index.md) | Next: [Model Context Protocol (MCP)](./model-context-protocol-mcp.md) →