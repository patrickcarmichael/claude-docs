---
title: "Pengindeksan Codebase"
source: "https://docs.cursor.com/id/context/codebase-indexing"
language: "id"
language_name: "Indonesian"
---

# Pengindeksan Codebase
Source: https://docs.cursor.com/id/context/codebase-indexing

Cara Cursor mempelajari codebase kamu untuk pemahaman yang lebih baik

Cursor mengindeks codebase kamu dengan menghitung embedding untuk setiap file. Ini meningkatkan kualitas jawaban AI tentang kodenya. Saat kamu membuka proyek, Cursor mulai mengindeks secara otomatis. File baru diindeks secara bertahap.
Cek status pengindeksan di: `Cursor Settings` > `Indexing & Docs`

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="Indikator progres pengindeksan codebase" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
</Frame>

<div id="configuration">
  ## Konfigurasi
</div>

Cursor mengindeks semua file kecuali yang ada di [ignore files](/id/context/ignore-files) (misalnya `.gitignore`, `.cursorignore`).

Klik `Show Settings` untuk:

* Mengaktifkan pengindeksan otomatis untuk repositori baru
* Menentukan file mana yang ingin diabaikan

<Tip>
  [Mengabaikan file konten berukuran besar](/id/context/ignore-files) dapat meningkatkan akurasi jawaban.
</Tip>

<div id="view-indexed-files">
  ### Lihat file yang diindeks
</div>

Untuk melihat path file yang diindeks: `Cursor Settings` > `Indexing & Docs` > `View included files`

Ini akan membuka file `.txt` yang mencantumkan semua file yang diindeks.

<div id="multi-root-workspaces">
  ## Workspace multi-root
</div>

Cursor mendukung [workspace multi-root](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces), bikin lo bisa kerja bareng banyak codebase:

* Semua codebase keindeks otomatis
* Konteks tiap codebase tersedia buat AI
* `.cursor/rules` jalan di semua folder

<div id="pr-search">
  ## Pencarian PR
</div>

Pencarian PR bantu lo ngerti evolusi codebase lo dengan bikin perubahan historis bisa dicari dan diakses lewat AI.

<div id="how-it-works">
  ### Cara kerjanya
</div>

Cursor otomatis **mengindeks semua PR yang sudah di-merge** dari riwayat repositori lo. Ringkasan muncul di hasil pencarian semantik, dengan penyaringan pintar yang memprioritaskan perubahan terbaru.

Agent bisa **ngambil PR, commit, issue, atau branch** ke konteks pakai `@[PR number]`, `@[commit hash]`, atau `@[branch name]`. Termasuk komentar GitHub dan review Bugbot kalau terhubung.

**Dukungan platform** mencakup GitHub, GitHub Enterprise, dan Bitbucket. GitLab saat ini belum didukung.

<Note>
  Pengguna GitHub Enterprise: Tool fetch bakal fallback ke perintah git karena
  keterbatasan autentikasi VSCode.
</Note>

<div id="using-pr-search">
  ### Menggunakan pencarian PR
</div>

Tanyain hal-hal kayak "Gimana layanan diimplementasi di PR lain?" dan Agent bakal otomatis ngambil PR yang relevan ke konteks buat ngasih jawaban komprehensif berdasarkan riwayat repositori lo.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Di mana aku bisa lihat semua codebase yang terindeks?">
    Belum ada daftar global. Cek tiap proyek satu per satu dengan membukanya di
    Cursor dan mengecek pengaturan Codebase Indexing.
  </Accordion>

  <Accordion title="Gimana cara hapus semua codebase yang terindeks?">
    Hapus akun Cursor kamu dari Settings untuk menghapus semua codebase yang terindeks.
    Atau, hapus codebase satu per satu dari pengaturan Codebase Indexing di tiap proyek.
  </Accordion>

  <Accordion title="Berapa lama codebase yang terindeks dipertahankan?">
    Codebase yang terindeks akan dihapus setelah 6 minggu tanpa aktivitas. Membuka kembali
    proyek akan memicu reindexing.
  </Accordion>

  <Accordion title="Apakah source code-ku disimpan di server Cursor?">
    Tidak. Cursor membuat embedding tanpa menyimpan nama file atau source code. Nama file diobfuski dan potongan kode dienkripsi.

    Saat Agent mencari di codebase, Cursor mengambil embedding dari server dan mendekripsi potongan tersebut.
  </Accordion>
</AccordionGroup>

---

← Previous: [/command](./command.md) | [Index](./index.md) | Next: [Mengabaikan file](./mengabaikan-file.md) →