---
title: "Mengabaikan file"
source: "https://docs.cursor.com/id/context/ignore-files"
language: "id"
language_name: "Indonesian"
---

# Mengabaikan file
Source: https://docs.cursor.com/id/context/ignore-files

Kendalikan akses file dengan .cursorignore dan .cursorindexingignore

<div id="overview">
  ## Gambaran Umum
</div>

Cursor membaca dan mengindeks codebase proyekmu untuk mendukung fitur-fiturnya. Atur direktori dan file mana yang boleh diakses Cursor pakai file `.cursorignore` di direktori root.

Cursor memblokir akses ke file yang tercantum di `.cursorignore` dari:

* Pengindeksan codebase
* Kode yang bisa diakses oleh [Tab](/id/tab/overview), [Agent](/id/agent/overview), dan [Inline Edit](/id/inline-edit/overview)
* Kode yang bisa diakses lewat [referensi simbol @](/id/context/@-symbols/overview)

<Warning>
  Panggilan tool yang dijalankan oleh Agent, seperti terminal dan server MCP, nggak bisa memblokir
  akses ke kode yang diatur oleh `.cursorignore`
</Warning>

<div id="why-ignore-files">
  ## Kenapa nge-ignore file?
</div>

**Keamanan**: Batasi akses ke API key, kredensial, dan secret. Meski Cursor ngeblokir file yang di-ignore, perlindungan penuh tetap nggak bisa dijamin karena ketidakpastian LLM.

**Performa**: Di codebase besar atau monorepo, exclude bagian yang nggak relevan biar indexing lebih cepat dan penemuan file lebih akurat.

<div id="global-ignore-files">
  ## Global ignore files
</div>

Atur pola ignore untuk semua project di user settings biar file sensitif otomatis dikecualikan tanpa perlu konfigurasi per project.

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d5bb9e6b18ca466ec69ddd1b216320c9" alt="Global Cursor Ignore List" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/settings/global-ignore.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ce566e71f1fcac6a85942f9fbb741889 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=c833cf55c470463ce31ae936ee122971 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=a3c3f6c6b40a9e91487237f0cf37cbca 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=03284fab1ddfadb64346dc912ea97048 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=5bd5b338808979f9fa42faa7df69d39a 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=676448c72358de369a119b34a8dcf9c5 2500w" />
</Frame>

Pola default mencakup:

* File environment: `**/.env`, `**/.env.*`
* Kredensial: `**/credentials.json`, `**/secrets.json`
* Kunci: `**/*.key`, `**/*.pem`, `**/id_rsa`

<div id="configuring-cursorignore">
  ## Mengonfigurasi `.cursorignore`
</div>

Buat file `.cursorignore` di direktori root kamu dengan sintaks `.gitignore`.

<div id="pattern-examples">
  ### Contoh pola
</div>

```sh  theme={null}
config.json      # File spesifik
dist/           # Direktori
*.log           # Ekstensi file
**/logs         # Direktori bertingkat
!app/           # Jangan diabaikan (negasi)
```

<div id="hierarchical-ignore">
  ### Pengabaian hierarkis
</div>

Aktifkan `Cursor Settings` > `Features` > `Editor` > `Hierarchical Cursor Ignore` untuk mencari file `.cursorignore` di direktori induk.

**Catatan**: Komentar diawali dengan `#`. Pola yang muncul belakangan akan menimpa yang lebih awal. Pola bersifat relatif terhadap lokasi file.

<div id="limit-indexing-with-cursorindexingignore">
  ## Batasi pengindeksan dengan `.cursorindexingignore`
</div>

Gunakan `.cursorindexingignore` untuk mengecualikan file hanya dari pengindeksan. File ini tetap bisa diakses oleh fitur AI, tapi nggak akan muncul di pencarian codebase.

<div id="files-ignored-by-default">
  ## File yang diabaikan secara default
</div>

Cursor otomatis mengabaikan file di `.gitignore` dan daftar abaikan default di bawah. Kamu bisa menimpanya dengan awalan `!` di `.cursorignore`.

<Accordion title="Daftar Abaikan Default">
  Hanya untuk pengindeksan, file-file berikut diabaikan selain yang ada di `.gitignore`, `.cursorignore`, dan `.cursorindexingignore` kamu:

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
  ### Batasan pola negasi
</div>

Saat pakai pola negasi (diawali `!`), lo nggak bisa menyertakan ulang file kalau direktori induknya dikecualikan pakai \*.

```sh  theme={null}

---

← Previous: [Pengindeksan Codebase](./pengindeksan-codebase.md) | [Index](./index.md) | Next: [Model Context Protocol (MCP)](./model-context-protocol-mcp.md) →