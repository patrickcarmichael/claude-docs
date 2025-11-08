---
title: "Keamanan Agent"
source: "https://docs.cursor.com/id/account/agent-security"
language: "id"
language_name: "Indonesian"
---

# Keamanan Agent
Source: https://docs.cursor.com/id/account/agent-security

Pertimbangan keamanan saat menggunakan Cursor Agent

Prompt injection, halusinasi AI, dan masalah lain bisa bikin AI bertingkah di luar dugaan dan berpotensi berbahaya. Sambil terus ngejar solusi prompt injection di level yang lebih mendasar, perlindungan utama di produk Cursor adalah guardrail tentang apa yang boleh dilakukan agent, termasuk mewajibkan persetujuan manual untuk tindakan sensitif secara default. Tujuan dokumen ini adalah menjelaskan guardrail kami dan apa yang bisa lo harapkan dari itu.

Semua kontrol dan perilaku di bawah ini adalah pengaturan default sekaligus yang kami rekomendasikan.

<div id="first-party-tool-calls">
  ## Panggilan tool pihak pertama
</div>

Cursor dibekali dengan tool yang memungkinkan agent bantu pengguna nulis kode. Ini termasuk baca file, edit, jalanin perintah terminal, nyari dokumentasi di web, dan lainnya.

Tool baca tidak butuh persetujuan (mis. membaca file, mencari di seluruh kode). Pengguna bisa pakai [.cursorignore](/id/context/ignore-files) buat ngeblokir agent mengakses file tertentu sama sekali, tapi selain itu pembacaan umumnya diizinkan tanpa persetujuan. Untuk tindakan yang berisiko mengekfiltrasi data sensitif, kami butuh persetujuan eksplisit.

Mengubah file di workspace saat ini tidak butuh persetujuan eksplisit dengan beberapa pengecualian. Begitu agent mengubah file, perubahan langsung disimpan ke disk. Kami rekomendasikan menjalankan Cursor di workspace yang pakai version control, biar isi file bisa dibalikin kapan aja. Kami butuh persetujuan eksplisit sebelum mengubah file yang memodifikasi konfigurasi IDE/CLI kami, seperti file pengaturan workspace editor. Namun, pengguna yang auto-reload saat file berubah perlu sadar kalau perubahan agent ke file bisa memicu eksekusi otomatis sebelum sempat meninjau perubahan.

Perintah terminal apa pun yang disaranin agent butuh persetujuan secara default. Kami rekomendasikan pengguna meninjau tiap perintah sebelum agent jalanin. Pengguna yang menerima risikonya bisa milih ngizinin agent jalanin semua perintah tanpa persetujuan. Kami menyertakan fitur [allowlist](/id/agent/tools) di Cursor, tapi kami tidak menganggapnya sebagai kontrol keamanan. Beberapa pengguna milih ngizinin perintah tertentu, tapi ini sistem best effort dan bypass mungkin terjadi. Kami tidak merekomendasikan "Run Everything", yang melewati allowlist apa pun yang dikonfigurasi.

<div id="third-party-tool-calls">
  ## Panggilan tool pihak ketiga
</div>

Cursor memungkinkan menghubungkan tool eksternal lewat [MCP](/id/context/mcp). Semua koneksi MCP pihak ketiga harus disetujui secara eksplisit oleh pengguna. Setelah pengguna menyetujui sebuah MCP, secara default setiap panggilan tool yang disarankan di Agent Mode untuk setiap integrasi MCP eksternal harus disetujui secara eksplisit sebelum dijalankan.

<div id="network-requests">
  ## Permintaan jaringan
</div>

Permintaan jaringan bisa dimanfaatkan penyerang untuk mengekfiltrasi data. Saat ini kami tidak mendukung alat first‑party apa pun yang membuat permintaan jaringan ke luar sejumlah kecil host terpilih (mis. GitHub), pengambilan tautan secara eksplisit, serta dukungan penelusuran web dengan penyedia tertentu yang dipilih. Permintaan jaringan agen yang sewenang‑wenang diblokir dengan pengaturan default.

<div id="workspace-trust">
  ## Kepercayaan workspace
</div>

Cursor IDE mendukung fitur standar [workspace trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) yang secara default *nonaktif*. Workspace trust bakal nampilin prompt saat lo buka workspace baru untuk milih mode normal atau mode terbatas. Mode terbatas bakal bikin AI dan fitur lain yang biasanya dipakai di Cursor jadi nggak berfungsi. Kami saranin pakai tool lain, seperti text editor basic, buat kerjaan dengan repo yang lo nggak percaya.

Workspace trust bisa diaktifin di pengaturan pengguna dengan langkah-langkah ini:

1. Buka file user settings.json lo
2. Tambahin konfigurasi berikut:
   ```json  theme={null}
   "security.workspace.trust.enabled": true
   ```

Pengaturan ini juga bisa dipaksain di seluruh organisasi lewat solusi Mobile Device Management (MDM).

<div id="responsible-disclosure">
  ## Pengungkapan yang bertanggung jawab
</div>

Kalau kamu menemukan kerentanan di Cursor, ikuti panduan di halaman GitHub Security kami dan kirim laporannya di sana. Kalau nggak bisa pakai GitHub, kamu juga bisa hubungi kami di [security@cursor.com](mailto:security@cursor.com).

Kami berkomitmen untuk mengakui penerimaan laporan kerentanan dalam 5 hari kerja dan menangani laporan tersebut secepatnya. Kami akan memublikasikan hasilnya dalam bentuk security advisory di halaman GitHub Security kami. Insiden kritis akan dikomunikasikan di halaman GitHub Security dan juga lewat email ke semua pengguna.

---

← Previous: [Index](./index.md) | [Index](./index.md) | Next: [Billing](./billing.md) →