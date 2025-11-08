---
title: "Ignorer des fichiers"
source: "https://docs.cursor.com/fr/context/ignore-files"
language: "fr"
language_name: "French"
---

# Ignorer des fichiers
Source: https://docs.cursor.com/fr/context/ignore-files

Gérer l’accès aux fichiers avec .cursorignore et .cursorindexingignore

<div id="overview">
  ## Vue d’ensemble
</div>

Cursor lit et indexe le code de ton projet pour alimenter ses fonctionnalités. Contrôle les répertoires et fichiers auxquels Cursor peut accéder avec un fichier `.cursorignore` à la racine de ton projet.

Cursor bloque l’accès aux fichiers listés dans `.cursorignore` pour :

* L’indexation du codebase
* Le code accessible via [Tab](/fr/tab/overview), [Agent](/fr/agent/overview) et [Inline Edit](/fr/inline-edit/overview)
* Le code accessible via les [références avec le symbole @](/fr/context/@-symbols/overview)

<Warning>
  Les appels d’outils lancés par Agent, comme le terminal et les serveurs MCP, ne peuvent pas bloquer
  l’accès au code régi par `.cursorignore`
</Warning>

<div id="why-ignore-files">
  ## Pourquoi ignorer des fichiers ?
</div>

**Sécurité** : Restreins l’accès aux clés d’API, identifiants et secrets. Même si Cursor bloque les fichiers ignorés, une protection totale n’est pas garantie à cause de l’imprévisibilité des LLM.

**Performance** : Dans de grandes bases de code ou des monorepos, exclue les parties non pertinentes pour un indexage plus rapide et une découverte de fichiers plus précise.

<div id="global-ignore-files">
  ## Fichiers d’ignore globaux
</div>

Définis des patterns d’exclusion pour tous les projets dans tes paramètres utilisateur afin d’écarter les fichiers sensibles sans configurer chaque projet individuellement.

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d5bb9e6b18ca466ec69ddd1b216320c9" alt="Liste d’ignore globale de Cursor" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/settings/global-ignore.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ce566e71f1fcac6a85942f9fbb741889 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=c833cf55c470463ce31ae936ee122971 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=a3c3f6c6b40a9e91487237f0cf37cbca 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=03284fab1ddfadb64346dc912ea97048 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=5bd5b338808979f9fa42faa7df69d39a 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=676448c72358de369a119b34a8dcf9c5 2500w" />
</Frame>

Les patterns par défaut incluent :

* Fichiers d’environnement : `**/.env`, `**/.env.*`
* Identifiants : `**/credentials.json`, `**/secrets.json`
* Clés : `**/*.key`, `**/*.pem`, `**/id_rsa`

<div id="configuring-cursorignore">
  ## Configurer `.cursorignore`
</div>

Crée un fichier `.cursorignore` à la racine de ton projet en utilisant la syntaxe de `.gitignore`.

<div id="pattern-examples">
  ### Exemples de modèles
</div>

```sh  theme={null}
config.json      # Fichier spécifique
dist/           # Répertoire
*.log           # Extension de fichier
**/logs         # Répertoires imbriqués
!app/           # Annuler l’ignorance (négation)
```

<div id="hierarchical-ignore">
  ### Ignorer hiérarchique
</div>

Active `Cursor Settings` > `Features` > `Editor` > `Hierarchical Cursor Ignore` pour rechercher des fichiers `.cursorignore` dans les répertoires parents.

**Notes** : Les commentaires commencent par `#`. Les règles définies plus tard écrasent les précédentes. Les règles sont relatives à l’emplacement du fichier.

<div id="limit-indexing-with-cursorindexingignore">
  ## Limiter l’indexation avec `.cursorindexingignore`
</div>

Utilise `.cursorindexingignore` pour exclure des fichiers de l’indexation uniquement. Ces fichiers restent accessibles aux fonctionnalités d’IA, mais n’apparaîtront pas dans les recherches du codebase.

<div id="files-ignored-by-default">
  ## Fichiers ignorés par défaut
</div>

Cursor ignore automatiquement les fichiers listés dans `.gitignore` ainsi que la liste d’exclusion par défaut ci-dessous. Tu peux les rétablir avec le préfixe `!` dans `.cursorignore`.

<Accordion title="Liste d’exclusion par défaut">
  Uniquement pour l’indexation, ces fichiers sont ignorés en plus de ceux présents dans ton `.gitignore`, `.cursorignore` et `.cursorindexingignore` :

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
  ### Limitations des motifs de négation
</div>

Quand tu utilises des motifs de négation (préfixés par `!`), tu ne peux pas réinclure un fichier si un répertoire parent est exclu via \*.

```sh  theme={null}

---

← Previous: [Indexation de la base de code](./indexation-de-la-base-de-code.md) | [Index](./index.md) | Next: [Model Context Protocol (MCP)](./model-context-protocol-mcp.md) →