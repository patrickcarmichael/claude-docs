---
title: "JetBrains"
source: "https://docs.cursor.com/id/guides/migration/jetbrains"
language: "id"
language_name: "Indonesian"
---

# JetBrains
Source: https://docs.cursor.com/id/guides/migration/jetbrains

Migrasi dari IDE JetBrains ke Cursor dengan alat yang sudah familier

Cursor menawarkan pengalaman ngoding modern bertenaga AI yang bisa menggantikan IDE JetBrains. Meski perpindahannya mungkin terasa berbeda di awal, fondasi Cursor yang berbasis VS Code menghadirkan fitur-fitur canggih dan opsi kustomisasi yang luas.

<div id="editor-components">
  ## Komponen Editor
</div>

<div id="extensions">
  ### Ekstensi
</div>

JetBrains IDE adalah alat yang keren, karena sudah dikonfigurasi sebelumnya untuk bahasa dan framework yang dituju.

Cursor berbeda — sebagai kanvas kosong sejak awal, kamu bisa menyesuaikannya sesuka hati, tanpa dibatasi oleh bahasa dan framework yang ditargetkan IDE.

Cursor punya akses ke ekosistem ekstensi yang luas, dan hampir semua fungsionalitas (bahkan lebih!) yang ditawarkan JetBrains IDE bisa direplikasi lewat ekstensi-ekstensi ini.

Lihat beberapa ekstensi populer berikut:

<CardGroup cols={4}>
  <Card title="Remote SSH" icon="network-wired" href="cursor:extension/anysphere.remote-ssh">
    Ekstensi SSH
  </Card>

  <Card title="Project Manager" icon="folder-tree" href="cursor:extension/alefragnani.project-manager">
    Kelola banyak proyek
  </Card>

  <Card title="GitLens" icon="git" href="cursor:extension/eamodio.gitlens">
    Integrasi Git yang lebih kaya
  </Card>

  <Card title="Local History" icon="clock-rotate-left" href="cursor:extension/xyz.local-history">
    Lacak perubahan file lokal
  </Card>

  <Card title="Error Lens" icon="bug" href="cursor:extension/usernamehw.errorlens">
    Sorotan error inline
  </Card>

  <Card title="ESLint" icon="code-compare" href="cursor:extension/dbaeumer.vscode-eslint">
    Linting kode
  </Card>

  <Card title="Prettier" icon="wand-magic-sparkles" href="cursor:extension/esbenp.prettier-vscode">
    Pemformatan kode
  </Card>

  <Card title="Todo Tree" icon="folder-tree" href="cursor:extension/Gruntfuggly.todo-tree">
    Lacak TODO dan FIXME
  </Card>
</CardGroup>

<div id="keyboard-shortcuts">
  ### Pintasan Keyboard
</div>

Cursor punya manajer pintasan keyboard bawaan yang memungkinkan kamu memetakan pintasan favorit ke aksi-aksi.

Dengan ekstensi ini, kamu bisa membawa hampir semua pintasan JetBrains IDE langsung ke Cursor!
Pastikan baca dokumentasi ekstensi untuk tahu cara mengonfigurasinya sesuai selera:

<Card title="IntelliJ IDEA Keybindings" icon="keyboard" href="cursor:extension/k--kato.intellij-idea-keybindings">
  Instal ekstensi ini untuk membawa pintasan keyboard JetBrains IDE ke Cursor.
</Card>

<Note>
  Pintasan umum yang berbeda:

  * Find Action: ⌘/Ctrl+Shift+P  (vs. ⌘/Ctrl+Shift+A)
  * Quick Fix: ⌘/Ctrl+.  (vs. Alt+Enter)
  * Go to File: ⌘/Ctrl+P  (vs. ⌘/Ctrl+Shift+N)
</Note>

<div id="themes">
  ### Tema
</div>

Reka ulang tampilan dan nuansa JetBrains IDE favorit kamu di Cursor dengan tema komunitas ini.

Pilih Darcula Theme standar, atau pilih tema yang cocok dengan penyorotan sintaks alat JetBrains kamu.

<CardGroup cols={1}>
  <Card title="JetBrains - Darcula Theme" icon="moon" horizontal href="cursor:extension/rokoroku.vscode-theme-darcula">
    Rasakan tema gelap klasik JetBrains Darcula
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="JetBrains PyCharm" icon="python" horizontal href="cursor:extension/gabemahoney.pycharm-dark-theme-for-python" />

  <Card title="IntelliJ" icon="java" horizontal href="cursor:extension/compassak.intellij-idea-new-ui" />

  <Card title="JetBrains Fleet" icon="code" horizontal href="cursor:extension/MichaelZhou.fleet-theme" />

  <Card title="JetBrains Rider" icon="hashtag" horizontal href="cursor:extension/muhammad-sammy.rider-theme" />
</CardGroup>

<CardGroup cols={1}>
  <Card title="JetBrains Icons" icon="icons" horizontal href="cursor:extension/ardonplay.vscode-jetbrains-icon-theme">
    Dapatkan ikon file dan folder JetBrains yang familiar
  </Card>
</CardGroup>

<div id="font">
  ### Font
</div>

Untuk melengkapi pengalaman ala JetBrains, kamu bisa pakai font resmi JetBrains Mono:

1. Unduh dan instal font JetBrains Mono ke sistem kamu:

<CardGroup cols={1}>
  <Card title="Download JetBrains Mono" icon="link" horizontal href="https://www.jetbrains.com/lp/mono/" />
</CardGroup>

2. Restart Cursor setelah menginstal font
3. Buka Settings di Cursor (⌘/Ctrl + ,)
4. Cari "Font Family"
5. Setel font family ke `'JetBrains Mono'`

<Note>
  Biar makin optimal, lo juga bisa nyalain ligatur font dengan nge-set "editor.fontLigatures": true di settings lo.
</Note>

<div id="ide-specific-migration">
  ## Migrasi Spesifik IDE
</div>

Banyak pengguna suka JetBrains IDE karena dukungan bawaan untuk bahasa dan framework yang jadi fokusnya. Cursor beda—sebagai kanvas kosong sejak awal, kamu bisa ngustom sesuai selera, tanpa dibatasi bahasa dan framework yang jadi target IDE tersebut.

Cursor sudah punya akses ke ekosistem ekstensi VS Code, dan hampir semua fungsionalitas (bahkan lebih!) yang ditawarkan JetBrains IDE bisa direplikasi lewat ekstensi-ekstensi ini.

Lihat ekstensi yang disarankan untuk tiap JetBrains IDE di bawah.

<div id="intellij-idea-java">
  ### IntelliJ IDEA (Java)
</div>

<CardGroup cols={2}>
  <Card title="Language Support for Java" icon="java" href="cursor:extension/redhat.java">
    Fitur inti bahasa Java
  </Card>

  <Card title="Debugger for Java" icon="bug" href="cursor:extension/vscjava.vscode-java-debug">
    Dukungan debugging Java
  </Card>

  <Card title="Test Runner for Java" icon="vial" href="cursor:extension/vscjava.vscode-java-test">
    Menjalankan dan debugging test Java
  </Card>

  <Card title="Maven for Java" icon="box" href="cursor:extension/vscjava.vscode-maven">
    Dukungan Maven
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Project Manager for Java" icon="folder-tree" href="cursor:extension/vscjava.vscode-java-dependency" horizontal>
    Alat manajemen proyek
  </Card>
</CardGroup>

<Warning>
  Perbedaan utama:

  * Konfigurasi Build/Run dikelola lewat launch.json
  * Alat Spring Boot tersedia lewat ekstensi ["Spring Boot Extension Pack"](cursor:extension/vmware.vscode-boot-dev-pack)
  * Dukungan Gradle lewat ekstensi ["Gradle for Java"](cursor:extension/vscjava.vscode-gradle)
</Warning>

<div id="pycharm-python">
  ### PyCharm (Python)
</div>

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Dukungan Python inti
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Pengecekan tipe yang cepat
  </Card>

  <Card title="Jupyter" icon="notebook" href="cursor:extension/ms-toolsai.jupyter">
    Dukungan notebook
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Formatter dan linter Python
  </Card>
</CardGroup>

<Note>
  Perbedaan utama:

  * Virtual environment dikelola lewat command palette
  * Konfigurasi debugging di launch.json
  * Manajemen dependencies lewat requirements.txt atau Poetry
</Note>

<div id="webstorm-javascripttypescript">
  ### WebStorm (JavaScript/TypeScript)
</div>

<CardGroup cols={2}>
  <Card title="JavaScript and TypeScript Nightly" icon="js" href="cursor:extension/ms-vscode.vscode-typescript-next">
    Fitur bahasa terbaru
  </Card>

  <Card title="ES7+ React/Redux Snippets" icon="react" href="cursor:extension/dsznajder.es7-react-js-snippets">
    Pengembangan React
  </Card>

  <Card title="Vue Language Features" icon="vuejs" href="cursor:extension/Vue.volar">
    Dukungan Vue.js
  </Card>

  <Card title="Angular Language Service" icon="angular" href="cursor:extension/Angular.ng-template">
    Pengembangan Angular
  </Card>
</CardGroup>

<Info>
  Sebagian besar fitur WebStorm sudah built-in di Cursor/VS Code, termasuk:

  * Tampilan skrip npm
  * Debugging
  * Integrasi Git
  * Dukungan TypeScript
</Info>

<div id="phpstorm-php">
  ### PhpStorm (PHP)
</div>

<CardGroup cols={2}>
  <Card title="PHP Intelephense" icon="php" href="cursor:extension/bmewburn.vscode-intelephense-client">
    Server bahasa PHP
  </Card>

  <Card title="PHP Debug" icon="bug" href="cursor:extension/xdebug.php-debug">
    Integrasi Xdebug
  </Card>

  <Card title="PHP Intellisense" icon="brain" href="cursor:extension/felixfbecker.php-intellisense">
    Kecerdasan kode
  </Card>

  <Card title="PHP DocBlocker" icon="comment-dots" href="cursor:extension/neilbrayfield.php-docblocker">
    Alat dokumentasi
  </Card>
</CardGroup>

<Note>
  Perbedaan utama:

  * Konfigurasi Xdebug lewat launch.json
  * Integrasi Composer lewat terminal
  * Alat basis data lewat ekstensi ["SQLTools"](cursor:extension/mtxr.sqltools)
</Note>

<div id="rider-net">
  ### Rider (.NET)
</div>

<CardGroup cols={2}>
  <Card title="C#" icon="code" href="cursor:extension/anysphere.csharp">
    Dukungan inti C#
  </Card>

  <Card title="DotRush" icon="toolbox" href="cursor:extension/nromanov.dotrush">
    Lingkungan pengembangan C# open source
  </Card>

  <Card title="ReSharper Plugin" icon="box" href="https://www.jetbrains.com/help/resharper-vscode/Get_started.html#installation">
    Plugin C# dari JetBrains
  </Card>

  <Card title=".NET Install Tool" icon="box-open" href="cursor:extension/ms-dotnettools.vscode-dotnet-runtime">
    Pengelolaan .NET SDK
  </Card>
</CardGroup>

<Warning>
  Perbedaan utama:

  * Solution Explorer melalui File Explorer
  * Pengelolaan paket NuGet melalui CLI atau ekstensi
  * Integrasi test runner melalui Test Explorer
</Warning>

<div id="goland-go">
  ### GoLand (Go)
</div>

<CardGroup cols={1}>
  <Card title="Go" icon="golang" href="cursor:extension/golang.Go">
    Ekstensi resmi Go
  </Card>
</CardGroup>

<Note>
  Perbedaan utama:

  * Instalasi alat Go dipicu secara otomatis
  * Debugging melalui launch.json
  * Pengelolaan paket terintegrasi dengan go.mod
</Note>

<div id="tips-for-a-smooth-transition">
  ## Tips untuk Transisi yang Mulus
</div>

<Steps>
  <Step title="Gunakan Command Palette">
    Tekan <kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> buat nyari perintah
  </Step>

  <Step title="Fitur AI">
    Manfaatkan fitur AI Cursor buat pelengkapan kode dan refactoring
  </Step>

  <Step title="Sesuaikan Settings">
    Fine-tune file settings.json biar workflow makin optimal
  </Step>

  <Step title="Integrasi Terminal">
    Gunakan terminal bawaan buat operasi command-line
  </Step>

  <Step title="Extensions">
    Jelajahi marketplace VS Code buat alat tambahan
  </Step>
</Steps>

<Info>
  Ingat, meskipun beberapa workflow mungkin beda, Cursor nawarin fitur coding berbasis AI yang powerful dan bisa ningkatin produktivitas melampaui kemampuan IDE tradisional.
</Info>

---

← Previous: [iOS & macOS (Swift)](./ios-macos-swift.md) | [Index](./index.md) | Next: [VS Code](./vs-code.md) →