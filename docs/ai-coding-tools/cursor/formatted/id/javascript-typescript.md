---
title: "JavaScript & TypeScript"
source: "https://docs.cursor.com/id/guides/languages/javascript"
language: "id"
language_name: "Indonesian"
---

# JavaScript & TypeScript
Source: https://docs.cursor.com/id/guides/languages/javascript

Pengembangan JavaScript dan TypeScript dengan dukungan framework

Selamat datang di pengembangan JavaScript dan TypeScript di Cursor! Editor ini punya dukungan yang sangat baik untuk pengembangan JS/TS lewat ekosistem ekstensi. Berikut yang perlu kamu tahu untuk memaksimalkan penggunaan Cursor.

<div id="essential-extensions">
  ## Ekstensi Esensial
</div>

Meski Cursor bekerja lancar dengan ekstensi apa pun yang kamu pakai, kami rekomendasikan yang ini buat kamu yang baru mulai:

* **ESLint** - Diperlukan untuk kemampuan perbaikan lint berbasis AI di Cursor
* **JavaScript and TypeScript Language Features** - Dukungan bahasa dan IntelliSense yang lebih kaya
* **Path Intellisense** - Pelengkapan jalur cerdas untuk path file

<div id="cursor-features">
  ## Fitur Cursor
</div>

Cursor ngasih tenaga ke alur kerja JavaScript/TypeScript yang sudah kamu pakai dengan:

* **Tab Completions**: Saran kode kontekstual yang paham struktur proyek kamu
* **Automatic Imports**: Tab bisa otomatis mengimpor library begitu kamu pakai
* **Inline Editing**: Pakai `CMD+K` di baris mana pun untuk ngedit dengan sintaks yang rapi
* **Composer Guidance**: Rencanakan dan edit kode kamu lintas banyak file dengan Composer

<div id="framework-intelligence-with-docs">
  ### Framework Intelligence dengan @Docs
</div>

Fitur @Docs dari Cursor bikin pengembangan JavaScript kamu makin ngebut dengan nambahin sumber dokumentasi kustom yang bisa dirujuk AI. Tambahin dokumentasi dari MDN, Node.js, atau framework favorit kamu biar saran kode jadi lebih akurat dan kontekstual.

<Card title="Pelajari lebih lanjut tentang @Docs" icon="book" href="/id/context/@-symbols/@-docs">
  Pelajari cara nambah dan ngelola sumber dokumentasi kustom di Cursor.
</Card>

<div id="automatic-linting-resolution">
  ### Penyelesaian Linting Otomatis
</div>

Salah satu fitur unggulan Cursor adalah integrasi mulusnya dengan ekstensi linter.
Pastikan kamu punya linter seperti ESLint yang sudah disetel, dan aktifkan pengaturan 'Iterate on Lints'.

Terus, pas kamu pakai Agent mode di Composer, begitu AI nyoba jawab pertanyaan kamu dan bikin perubahan kode, AI bakal otomatis baca output dari linter dan coba benerin error lint yang mungkin belum ketangkep sebelumnya.

<div id="framework-support">
  ## Dukungan Framework
</div>

Cursor bekerja mulus dengan semua framework dan library JavaScript utama, seperti:

### React & Next.js

* Dukungan penuh JSX/TSX dengan saran komponen yang cerdas
* Kecerdasan untuk server component dan rute API di Next.js
* Rekomendasi: ekstensi [**React Developer Tools**](cursor:extension/msjsdiag.vscode-react-native)

<div id="vuejs">
  ### Vue.js
</div>

* Dukungan sintaks template dengan integrasi Volar
* Pelengkapan otomatis komponen dan pemeriksaan tipe
* Rekomendasi: [**Vue Language Features**](cursor:extension/vue.volar)

<div id="angular">
  ### Angular
</div>

* Validasi template dan dukungan decorator TypeScript
* Pembuatan komponen dan service
* Rekomendasi: [**Angular Language Service**](cursor:extension/Angular.ng-template)

<div id="svelte">
  ### Svelte
</div>

* Highlighting sintaks komponen dan pelengkapan cerdas
* Saran untuk reactive statement dan store
* Rekomendasi: [**Svelte for VS Code**](cursor:extension/svelte.svelte-vscode)

<div id="backend-frameworks-expressnestjs">
  ### Backend Frameworks (Express/NestJS)
</div>

* Kecerdasan untuk route dan middleware
* Dukungan decorator TypeScript untuk NestJS
* Integrasi alat pengujian API

Ingat, fitur AI Cursor bekerja dengan baik di semua framework ini, memahami pola dan best practice mereka untuk ngasih saran yang relevan. AI bisa bantu dari pembuatan komponen sampai refactoring yang kompleks, sambil tetap menghormati pola yang sudah ada di proyek lo.

---

← Previous: [Java](./java.md) | [Index](./index.md) | Next: [Python](./python.md) →