---
title: "Konfigurasi"
source: "https://docs.cursor.com/id/cli/reference/configuration"
language: "id"
language_name: "Indonesian"
---

# Konfigurasi
Source: https://docs.cursor.com/id/cli/reference/configuration

Referensi konfigurasi Agent CLI untuk cli-config.json

Atur Agent CLI menggunakan file `cli-config.json`.

<div id="file-location">
  ## Lokasi file
</div>

<div class="full-width-table">
  | Tipe   | Platform    | Path                                       |
  | :----- | :---------- | :----------------------------------------- |
  | Global | macOS/Linux | `~/.cursor/cli-config.json`                |
  | Global | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | Proyek | Semua       | `<project>/.cursor/cli.json`               |
</div>

<Note>Cuma izin yang bisa dikonfigurasi di level proyek. Semua pengaturan CLI lainnya harus diatur secara global.</Note>

Override dengan variabel lingkungan:

* **`CURSOR_CONFIG_DIR`**: path direktori kustom
* **`XDG_CONFIG_HOME`** (Linux/BSD): memakai `$XDG_CONFIG_HOME/cursor/cli-config.json`

<div id="schema">
  ## Skema
</div>

<div id="required-fields">
  ### Field wajib
</div>

<div class="full-width-table">
  | Field               | Type      | Deskripsi                                                                   |
  | :------------------ | :-------- | :-------------------------------------------------------------------------- |
  | `version`           | number    | Versi skema konfigurasi (saat ini: `1`)                                     |
  | `editor.vimMode`    | boolean   | Mengaktifkan keybinding Vim (default: `false`)                              |
  | `permissions.allow` | string\[] | Operasi yang diizinkan (lihat [Permissions](/id/cli/reference/permissions)) |
  | `permissions.deny`  | string\[] | Operasi yang dilarang (lihat [Permissions](/id/cli/reference/permissions))  |
</div>

<div id="optional-fields">
  ### Field opsional
</div>

<div class="full-width-table">
  | Field                    | Type    | Deskripsi                             |
  | :----------------------- | :------ | :------------------------------------ |
  | `model`                  | object  | Konfigurasi model yang dipilih        |
  | `hasChangedDefaultModel` | boolean | Flag override model yang dikelola CLI |
</div>

<div id="examples">
  ## Contoh
</div>

<div id="minimal-config">
  ### Konfigurasi minimal
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="enable-vim-mode">
  ### Aktifkan Mode Vim
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="configure-permissions">
  ### Konfigurasikan izin
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

Lihat [Permissions](/id/cli/reference/permissions) untuk jenis izin yang tersedia dan contohnya.

<div id="troubleshooting">
  ## Pemecahan Masalah
</div>

**Error konfigurasi**: Pindahin file-nya dulu ke lokasi lain, lalu restart:

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**Perubahan nggak tersimpan**: Pastikan JSON valid dan punya izin tulis. Beberapa field dikelola CLI dan bisa ke-overwrite.

<div id="notes">
  ## Catatan
</div>

* Format JSON murni (tanpa komentar)
* CLI melakukan perbaikan otomatis untuk field yang hilang
* File yang rusak dicadangkan sebagai `.bad` dan dibuat ulang
* Entri izin harus berupa string yang persis sama (lihat [Permissions](/id/cli/reference/permissions) untuk detail)

---

← Previous: [Autentikasi](./autentikasi.md) | [Index](./index.md) | Next: [Format output](./format-output.md) →