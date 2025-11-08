---
title: "GitHub"
source: "https://docs.cursor.com/id/integrations/github"
language: "id"
language_name: "Indonesian"
---

# GitHub
Source: https://docs.cursor.com/id/integrations/github

Aplikasi GitHub Cursor resmi untuk agen latar belakang

[Background Agents](/id/background-agent) dan [Bugbot](/id/bugbot) memerlukan aplikasi GitHub Cursor untuk mengklona repositori dan mendorong perubahan.

<div id="installation">
  ## Instalasi
</div>

1. Buka [Integrations di Dashboard](https://cursor.com/dashboard?tab=integrations)
2. Klik **Connect** di sebelah GitHub
3. Pilih repositori: **All repositories** atau **Selected repositories**

Untuk memutuskan sambungan akun GitHub, kembali ke dashboard Integrations dan klik **Disconnect Account**.

<div id="using-agent-in-github">
  ## Menggunakan Agent di GitHub
</div>

Integrasi GitHub memungkinkan alur kerja agent di latar belakang langsung dari pull request dan issue. Lo bisa memicu agent untuk membaca konteks, menerapkan perbaikan, dan nge-push commit dengan komentar `@cursor [prompt]` di PR atau issue apa pun.

Kalau lo ngaktifin [Bugbot](/id/bugbot), lo bisa komentar `@cursor fix` buat ngebaca perbaikan yang direkomendasi Bugbot dan nge-trigger agent di latar belakang buat nangani issue tersebut.

<div id="permissions">
  ## Permissions
</div>

Aplikasi GitHub memerlukan izin tertentu untuk bekerja dengan agen latar belakang:

<div className="full-width-table">
  | Permission                | Purpose                                                   |
  | ------------------------- | --------------------------------------------------------- |
  | **Repository access**     | Nge-clone kode lo dan bikin working branch                |
  | **Pull requests**         | Bikin PR berisi perubahan dari agen buat lo review        |
  | **Issues**                | Ngelacak bug dan task yang ditemukan atau diperbaiki agen |
  | **Checks and statuses**   | Ngelaporin kualitas kode dan hasil test                   |
  | **Actions and workflows** | Memonitor pipeline CI/CD dan status deployment            |
</div>

Semua izin mengikuti prinsip least privilege yang diperlukan untuk fungsionalitas agen latar belakang.

<div id="ip-allow-list-configuration">
  ## Konfigurasi Daftar Izinkan IP
</div>

Kalau organisasi lo pakai fitur daftar izinkan IP GitHub buat ngebatesin akses ke repositori, lo perlu kontak support dulu buat ngaktifin fungsionalitas daftar izinkan IP buat tim lo.

<div id="contact-support">
  ### Hubungi Support
</div>

Sebelum ngonfigurasi daftar izinkan IP, kontak [hi@cursor.com](mailto:hi@cursor.com) buat ngaktifin fitur ini buat tim lo. Ini wajib buat kedua metode konfigurasi di bawah.

<div id="enable-ip-allow-list-configuration-for-installed-github-apps-recommended">
  ### Aktifkan konfigurasi daftar izinkan IP untuk GitHub Apps yang terpasang (Direkomendasikan)
</div>

Aplikasi GitHub Cursor udah punya daftar IP yang preconfigured. Lo bisa ngaktifin allowlist buat aplikasi yang terpasang biar otomatis mewarisi daftar ini. Ini **pendekatan yang direkomendasikan**, karena memungkinkan kami memperbarui daftar dan organisasi lo bakal nerima pembaruan secara otomatis.

Untuk ngaktifinnya:

1. Buka pengaturan Security organisasi lo
2. Masuk ke pengaturan daftar izinkan IP
3. Centang **"Allow access by GitHub Apps"**

Buat instruksi lengkap, lihat [dokumentasi GitHub](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps).

<div id="add-ips-directly-to-your-allowlist">
  ### Tambahin IP langsung ke allowlist lo
</div>

Kalau organisasi lo pakai allowlist yang ditentuin IdP di GitHub atau nggak bisa pakai allowlist yang preconfigured, lo bisa nambahin alamat IP secara manual:

```
184.73.225.134
3.209.66.12
52.44.113.131
```

<Note>
  Daftar alamat IP bisa sesekali berubah. Tim yang pakai allowlist IP bakal dapat pemberitahuan terlebih dulu sebelum alamat IP ditambahkan atau dihapus.
</Note>

<div id="troubleshooting">
  ## Pemecahan Masalah
</div>

<AccordionGroup>
  <Accordion title="Agent nggak bisa akses repository">
    * Install app GitHub dengan akses ke repository
    * Cek permission repository buat repo privat
    * Verifikasi permission akun GitHub lo
  </Accordion>

  <Accordion title="Permission ditolak buat pull request">
    * Kasih app akses write ke pull request
    * Cek aturan proteksi branch
    * Install ulang kalau instalasi app udah kedaluwarsa
  </Accordion>

  <Accordion title="App nggak kelihatan di pengaturan GitHub">
    * Cek apakah di-install di level organisasi
    * Install ulang dari [github.com/apps/cursor](https://github.com/apps/cursor)
    * Hubungi support kalau instalasinya corrupt
  </Accordion>
</AccordionGroup>

---

← Previous: [Git](./git.md) | [Index](./index.md) | Next: [Linear](./linear.md) →