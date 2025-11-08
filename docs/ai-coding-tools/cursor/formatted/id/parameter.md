---
title: "Parameter"
source: "https://docs.cursor.com/id/cli/reference/parameters"
language: "id"
language_name: "Indonesian"
---

# Parameter
Source: https://docs.cursor.com/id/cli/reference/parameters

Referensi lengkap perintah untuk Cursor Agent CLI

<div id="global-options">
  ## Opsi global
</div>

Opsi global bisa dipakai dengan perintah apa pun:

<div class="full-width-table">
  | Opsi                       | Deskripsi                                                                                                                |
  | -------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
  | `-v, --version`            | Tampilkan nomor versi                                                                                                    |
  | `-a, --api-key <key>`      | API key untuk autentikasi (juga bisa pakai variabel lingkungan `CURSOR_API_KEY`)                                         |
  | `-p, --print`              | Cetak respons ke konsol (buat skrip atau penggunaan non-interaktif). Punya akses ke semua tool, termasuk write dan bash. |
  | `--output-format <format>` | Format output (hanya berfungsi dengan `--print`): `text`, `json`, atau `stream-json` (default: `stream-json`)            |
  | `-b, --background`         | Mulai dalam mode latar belakang (buka composer picker saat diluncurkan)                                                  |
  | `--fullscreen`             | Aktifkan mode layar penuh                                                                                                |
  | `--resume [chatId]`        | Lanjutkan sesi chat                                                                                                      |
  | `-m, --model <model>`      | Model yang dipakai                                                                                                       |
  | `-f, --force`              | Paksa izinkan perintah kecuali yang secara eksplisit ditolak                                                             |
  | `-h, --help`               | Tampilkan bantuan untuk perintah                                                                                         |
</div>

<div id="commands">
  ## Perintah
</div>

<div class="full-width-table">
  | Perintah          | Deskripsi                                   | Penggunaan                                        |
  | ----------------- | ------------------------------------------- | ------------------------------------------------- |
  | `login`           | Autentikasi dengan Cursor                   | `cursor-agent login`                              |
  | `logout`          | Keluar dan hapus autentikasi yang tersimpan | `cursor-agent logout`                             |
  | `status`          | Cek status autentikasi                      | `cursor-agent status`                             |
  | `mcp`             | Kelola server MCP                           | `cursor-agent mcp`                                |
  | `update\|upgrade` | Perbarui Cursor Agent ke versi terbaru      | `cursor-agent update` atau `cursor-agent upgrade` |
  | `ls`              | Lanjutkan sesi chat                         | `cursor-agent ls`                                 |
  | `resume`          | Lanjutkan sesi chat terbaru                 | `cursor-agent resume`                             |
  | `help [command]`  | Tampilkan bantuan untuk perintah            | `cursor-agent help [command]`                     |
</div>

<Note>
  Kalau nggak ada perintah yang ditentukan, Cursor Agent bakal mulai dalam mode chat interaktif secara default.
</Note>

<div id="mcp">
  ## MCP
</div>

Kelola server MCP yang dikonfigurasi untuk Cursor Agent.

<div class="full-width-table">
  | Subcommand                | Deskripsi                                                              | Penggunaan                                 |
  | ------------------------- | ---------------------------------------------------------------------- | ------------------------------------------ |
  | `login <identifier>`      | Masuk ke server MCP yang dikonfigurasi di `.cursor/mcp.json`           | `cursor-agent mcp login <identifier>`      |
  | `list`                    | Lihat daftar server MCP yang dikonfigurasi beserta statusnya           | `cursor-agent mcp list`                    |
  | `list-tools <identifier>` | Lihat daftar tool yang tersedia dan nama argumennya untuk MCP tertentu | `cursor-agent mcp list-tools <identifier>` |
</div>

Semua perintah MCP mendukung `-h, --help` untuk bantuan khusus perintah.

<div id="arguments">
  ## Argumen
</div>

Saat mulai dalam mode chat (perilaku default), lo bisa ngasih prompt awal:

**Argumen:**

* `prompt` — Prompt awal buat agen

<div id="getting-help">
  ## Mendapatkan bantuan
</div>

Semua perintah mendukung opsi global `-h, --help` untuk menampilkan bantuan khusus untuk perintah tersebut.

---

← Previous: [Format output](./format-output.md) | [Index](./index.md) | Next: [Permissions](./permissions.md) →