---
title: "Permissions"
source: "https://docs.cursor.com/id/cli/reference/permissions"
language: "id"
language_name: "Indonesian"
---

# Permissions
Source: https://docs.cursor.com/id/cli/reference/permissions

Jenis izin untuk mengontrol akses agen ke file dan perintah

Atur apa yang boleh dilakukan agen pakai token izin di konfigurasi CLI lo. Izin disetel di `~/.cursor/cli-config.json` (global) atau `<project>/.cursor/cli.json` (spesifik proyek).

<div id="permission-types">
  ## Jenis izin
</div>

<div id="shell-commands">
  ### Perintah shell
</div>

**Format:** `Shell(commandBase)`

Mengontrol akses ke perintah shell. `commandBase` adalah token pertama di baris perintah.

<div class="full-width-table">
  | Contoh       | Deskripsi                                                  |
  | ------------ | ---------------------------------------------------------- |
  | `Shell(ls)`  | Izinkan menjalankan perintah `ls`                          |
  | `Shell(git)` | Izinkan subperintah `git` apa pun                          |
  | `Shell(npm)` | Izinkan perintah pengelola paket npm                       |
  | `Shell(rm)`  | Tolak penghapusan file yang destruktif (umumnya di `deny`) |
</div>

<div id="file-reads">
  ### Pembacaan file
</div>

**Format:** `Read(pathOrGlob)`

Mengontrol akses baca ke file dan direktori. Mendukung pola glob.

<div class="full-width-table">
  | Contoh              | Deskripsi                                 |
  | ------------------- | ----------------------------------------- |
  | `Read(src/**/*.ts)` | Izinkan membaca file TypeScript di `src`  |
  | `Read(**/*.md)`     | Izinkan membaca file Markdown di mana pun |
  | `Read(.env*)`       | Tolak membaca file environment            |
  | `Read(/etc/passwd)` | Tolak membaca file sistem                 |
</div>

<div id="file-writes">
  ### Penulisan file
</div>

**Format:** `Write(pathOrGlob)`

Mengontrol akses tulis ke file dan direktori. Mendukung pola glob. Saat digunakan dalam mode print, `--force` diperlukan untuk menulis file.

<div class="full-width-table">
  | Contoh                | Deskripsi                                      |
  | --------------------- | ---------------------------------------------- |
  | `Write(src/**)`       | Izinkan menulis ke file apa pun di bawah `src` |
  | `Write(package.json)` | Izinkan memodifikasi package.json              |
  | `Write(**/*.key)`     | Tolak menulis file kunci privat                |
  | `Write(**/.env*)`     | Tolak menulis file environment                 |
</div>

<div id="configuration">
  ## Konfigurasi
</div>

Tambah izin ke objek `permissions` di file konfigurasi CLI lo:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)", 
      "Read(src/**/*.ts)",
      "Write(package.json)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  }
}
```

<div id="pattern-matching">
  ## Pencocokan pola
</div>

* Pola glob menggunakan wildcard `**`, `*`, dan `?`
* Path relatif berlaku dalam workspace saat ini
* Path absolut bisa menargetkan file di luar proyek
* Aturan deny memiliki prioritas dibanding aturan allow

---

← Previous: [Parameter](./parameter.md) | [Index](./index.md) | Next: [Perintah slash](./perintah-slash.md) →