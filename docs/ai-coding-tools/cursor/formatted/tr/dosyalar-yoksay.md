---
title: "Dosyaları yoksay"
source: "https://docs.cursor.com/tr/context/ignore-files"
language: "tr"
language_name: "Turkish"
---

# Dosyaları yoksay
Source: https://docs.cursor.com/tr/context/ignore-files

.cursorignore ve .cursorindexingignore ile dosya erişimini kontrol et

<div id="overview">
  ## Genel Bakış
</div>

Cursor, özelliklerini çalıştırmak için projenin kod tabanını okur ve indeksler. Kök dizindeki `.cursorignore` dosyasını kullanarak Cursor’un hangi dizin ve dosyalara erişebileceğini kontrol et.

Cursor, `.cursorignore` içinde listelenen dosyalara erişimi şuralardan engeller:

* Kod tabanı indeksleme
* [Tab](/tr/tab/overview), [Agent](/tr/agent/overview) ve [Inline Edit](/tr/inline-edit/overview) tarafından erişilebilen kod
* [@ sembol referansları](/tr/context/@-symbols/overview) aracılığıyla erişilebilen kod

<Warning>
  Agent tarafından başlatılan araç çağrıları — terminal ve MCP sunucuları gibi — `.cursorignore` kapsamındaki koda erişimi engelleyemez
</Warning>

<div id="why-ignore-files">
  ## Neden dosyaları yok sayasın?
</div>

**Güvenlik**: API anahtarlarına, kimlik bilgilerine ve sırlarına erişimi kısıtla. Cursor yok sayılan dosyaları engellese de, LLM’lerin öngörülemezliği nedeniyle tam koruma garanti edilemez.

**Performans**: Büyük kod tabanlarında veya monorepo’larda, daha hızlı indeksleme ve daha isabetli dosya keşfi için alakasız kısımları dışarıda tut.

<div id="global-ignore-files">
  ## Global ignore dosyaları
</div>

Her proje için ayrı ayrı yapılandırma yapmana gerek kalmadan, kullanıcı ayarlarında tüm projeler için ignore desenleri belirleyerek hassas dosyaları hariç tut.

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d5bb9e6b18ca466ec69ddd1b216320c9" alt="Global Cursor Ignore List" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/settings/global-ignore.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ce566e71f1fcac6a85942f9fbb741889 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=c833cf55c470463ce31ae936ee122971 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=a3c3f6c6b40a9e91487237f0cf37cbca 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=03284fab1ddfadb64346dc912ea97048 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=5bd5b338808979f9fa42faa7df69d39a 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=676448c72358de369a119b34a8dcf9c5 2500w" />
</Frame>

Varsayılan desenler şunlardır:

* Ortam dosyaları: `**/.env`, `**/.env.*`
* Kimlik bilgileri: `**/credentials.json`, `**/secrets.json`
* Anahtarlar: `**/*.key`, `**/*.pem`, `**/id_rsa`

<div id="configuring-cursorignore">
  ## `.cursorignore` yapılandırması
</div>

Kök dizininde, `.gitignore` sözdizimini kullanarak bir `.cursorignore` dosyası oluştur.

<div id="pattern-examples">
  ### Örnek kalıplar
</div>

```sh  theme={null}
config.json      # Belirli dosya
dist/           # Dizin
*.log           # Dosya uzantısı
**/logs         # İç içe dizinler
!app/           # Yoksayılandan çıkar (negasyon)
```

<div id="hierarchical-ignore">
  ### Hiyerarşik yok sayma
</div>

Üst dizinlerde `.cursorignore` dosyalarını aramak için `Cursor Settings` > `Features` > `Editor` > `Hierarchical Cursor Ignore` özelliğini etkinleştir.

**Notlar**: Yorumlar `#` ile başlar. Sonraki kalıplar önceki olanların üzerine yazar. Kalıplar dosyanın konumuna göredir.

<div id="limit-indexing-with-cursorindexingignore">
  ## `.cursorindexingignore` ile indekslemeyi sınırla
</div>

Yalnızca indekslemeden dosyaları hariç tutmak için `.cursorindexingignore` kullan. Bu dosyalar AI özellikleriyle erişilebilir kalır ama kod tabanı aramalarında görünmez.

<div id="files-ignored-by-default">
  ## Varsayılan olarak yok sayılan dosyalar
</div>

Cursor, `.gitignore` ve aşağıdaki varsayılan yok sayma listesindeki dosyaları otomatik olarak yok sayar. `.cursorignore` içinde `!` önekiyle geçersiz kılabilirsin.

<Accordion title="Varsayılan Yok Sayma Listesi">
  Yalnızca indeksleme için, `.gitignore`, `.cursorignore` ve `.cursorindexingignore` dosyalarındakilere ek olarak şu dosyalar da yok sayılır:

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
  ### Olumsuzlama deseni sınırlamaları
</div>

Olumsuzlama desenlerini (`!` ile başlayan) kullanırken, bir üst dizin `*` ile hariç tutulduysa bir dosyayı yeniden dahil edemezsin.

```sh  theme={null}

---

← Previous: [Kod Tabanı İndeksleme](./kod-taban-indeksleme.md) | [Index](./index.md) | Next: [Model Context Protocol (MCP)](./model-context-protocol-mcp.md) →