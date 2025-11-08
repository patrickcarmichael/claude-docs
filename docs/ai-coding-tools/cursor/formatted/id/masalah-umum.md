---
title: "Masalah Umum"
source: "https://docs.cursor.com/id/troubleshooting/common-issues"
language: "id"
language_name: "Indonesian"
---

# Masalah Umum
Source: https://docs.cursor.com/id/troubleshooting/common-issues

Solusi untuk masalah umum dan FAQ

Di bawah ini adalah masalah umum dan solusinya.

<div id="networking-issues">
  ### Masalah Jaringan
</div>

Pertama, cek konektivitas jaringan. Buka `Cursor Settings` > `Network` dan klik `Run Diagnostics`. Ini bakal ngetes koneksi ke server Cursor dan bantu ngidentifikasi masalah jaringan yang mungkin ngefek ke fitur AI, update, atau fungsionalitas online lainnya.

Cursor mengandalkan HTTP/2 buat fitur AI karena paling efisien buat respons streaming. Kalau jaringan lo nggak mendukung HTTP/2, lo mungkin bakal ngalamin kegagalan pengindeksan dan masalah di fitur AI.

Ini sering kejadian di jaringan kantor, VPN, atau kalau pakai proxy kayak Zscaler.

Buat ngatasinnya, aktifin fallback HTTP/1.1 di pengaturan aplikasi (bukan pengaturan Cursor): tekan `CMD/CTRL + ,`, cari `HTTP/2`, terus aktifin `Disable HTTP/2`. Ini maksa pakai HTTP/1.1 dan nge-resolve masalahnya.

Kita berencana nambahin deteksi dan fallback otomatis.

<div id="resource-issues-cpu-ram-etc">
  ### Masalah Sumber Daya (CPU, RAM, dll.)
</div>

Penggunaan CPU atau RAM yang tinggi bisa ngelemotin mesin lo atau munculin peringatan sumber daya.

Walaupun codebase besar butuh lebih banyak resource, penggunaan tinggi biasanya berasal dari ekstensi atau pengaturan.

<Note>
  Kalau lo ngeliat peringatan RAM rendah di **MacOS**, catat bahwa ada bug buat sebagian pengguna yang bisa nampilin nilai yang sangat nggak akurat. Kalau lo nemuin ini, buka Activity Monitor dan cek tab "Memory" buat liat penggunaan memori yang bener.
</Note>

Kalau lo ngalamin penggunaan CPU atau RAM tinggi, coba langkah-langkah ini:

<AccordionGroup>
  <Accordion title="Cek Ekstensi Lo">
    Ekstensi bisa ngaruh ke performa.

    Extension Monitor nunjukin konsumsi resource buat semua ekstensi yang terpasang dan bawaan.

    Aktifin Extension Monitor dari `Settings` > `Application` > `Experimental` dan toggle `Extension Monitor: Enabled`. Ini bakal minta lo buat restart Cursor.

    Buka: `Cmd/Ctrl + Shift + P` → `Developer: Open Extension Monitor`.

    Cursor ngejalanin ekstensi lo di satu atau lebih **extension host**. Biasanya, kebanyakan ekstensi lo bakal jalan di extension host yang sama, artinya ekstensi yang makan waktu CPU banyak bisa “ngesekik” ekstensi tetangganya!

    Extension Monitor bakal nunjukin:

    * Tiap proses jangka panjang yang diluncurin sama ekstensi (MacOS dan Linux doang).
    * **% Ext Host**: Persentase total waktu extension host yang dipakai ekstensi ini. Ngebantu ngidentifikasi ekstensi yang paling banyak makan waktu relatif ke yang lain.
    * **Max Blocking**: Durasi blok eksekusi kontinu terpanjang sebuah ekstensi per interval pemantauan.
    * **% CPU**:
      * Buat ekstensi: Persentase total penggunaan CPU yang dikaitin ke kode ekstensi.
      * Buat proses: Persentase total penggunaan CPU yang dikaitin ke proses yang diluncurin (MacOS dan Linux doang).
    * **Memory**:
      * Buat ekstensi: Jumlah memori heap JS yang dipakai kode ekstensi (alokasi eksternal nggak kehitung).
      * Buat proses: Jumlah memori sistem yang dipakai proses yang diluncurin (MacOS dan Linux doang).

    Lo juga bisa ngetes dengan jalanin `cursor --disable-extensions` dari command line. Kalau performa membaik, aktifin lagi ekstensi satu per satu buat nemuin mana yang bermasalah.

    Coba Extension Bisect buat ngidentifikasi ekstensi yang bermasalah. Baca lebih lanjut [di sini](https://code.visualstudio.com/blogs/2021/02/16/extension-bisect#_welcome-extension-bisect). Catatan: ini paling efektif buat masalah yang muncul langsung, bukan degradasi performa yang bertahap.
  </Accordion>

  <Accordion title="Pakai Process Explorer">
    Process Explorer nunjukin proses mana yang makan resource.

    Buka: Command Palette (`Cmd/Ctrl + Shift + P`) → `Developer: Open Process Explorer`.

    Tinjau proses di bawah:

    * **`extensionHost`**: Masalah terkait ekstensi
    * **`ptyHost`**: Konsumsi resource terminal

    Process Explorer nampilin tiap terminal dan perintah yang lagi jalan buat diagnosis.

    Buat proses lain yang penggunaan resource-nya tinggi, laporin ke [forum](https://forum.cursor.com/).
  </Accordion>

  <Accordion title="Pantau Sumber Daya Sistem">
    Pakai alat pemantauan sistem operasi lo buat nentuin apakah masalahnya spesifik ke Cursor atau ke seluruh sistem.
  </Accordion>

  <Accordion title="Tes Instalasi Minimal">
    Kalau masalah masih muncul, coba tes instalasi Cursor yang minimal.
  </Accordion>
</AccordionGroup>

<div id="general-faqs">
  ## FAQ Umum
</div>

<AccordionGroup>
  <Accordion title="Aku lihat update di changelog tapi Cursor nggak mau update">
    Update baru dirilis bertahap (staged rollout) — pengguna yang dipilih acak dapat duluan. Update-mu biasanya muncul dalam beberapa hari.
  </Accordion>

  <Accordion title="Aku ada masalah login GitHub di Cursor / Gimana cara logout dari GitHub di Cursor?">
    Pakai `Sign Out of GitHub` dari command palette `Ctrl/⌘ + Shift + P`.
  </Accordion>

  <Accordion title="Aku nggak bisa pakai GitHub Codespaces">
    GitHub Codespaces belum didukung.
  </Accordion>

  <Accordion title="Aku kena error saat konek ke Remote SSH">
    SSH ke mesin Mac atau Windows belum didukung. Untuk masalah lain, laporkan ke [forum](https://forum.cursor.com/) lengkap dengan log.
  </Accordion>

  <Accordion title="Masalah Koneksi SSH di Windows">
    Kalau kamu melihat "SSH is only supported in Microsoft versions of VS Code":

    1. Hapus instalasi Remote-SSH:
       * Buka tampilan Extensions (`Ctrl + Shift + X`)
       * Cari "Remote-SSH"
       * Klik ikon gear → "Uninstall"

    2. Pasang Anysphere Remote SSH:
       * Buka Cursor marketplace
       * Cari "SSH"
       * Instal ekstensi Anysphere Remote SSH

    3. Setelah instalasi:
       * Tutup semua instance VS Code dengan koneksi SSH aktif
       * Restart Cursor
       * Sambungkan lagi via SSH

    Pastikan konfigurasi dan key SSH kamu sudah di-setup dengan benar.
  </Accordion>

  <Accordion title="Cursor Tab dan Inline Edit nggak jalan di balik proxy kantor">
    Cursor Tab dan Inline Edit pakai HTTP/2 untuk latensi lebih rendah dan pemakaian resource yang lebih hemat. Beberapa proxy kantor (mis. Zscaler) memblokir HTTP/2. Perbaiki dengan set `"cursor.general.disableHttp2": true` di settings (`Cmd/Ctrl + ,`, cari `http2`).
  </Accordion>

  <Accordion title="Aku baru langganan Pro tapi di app masih gratis">
    Logout lalu login lagi dari Cursor Settings.
  </Accordion>

  <Accordion title="Kapan penggunaan aku ke-reset lagi?">
    Pelanggan Pro: Klik `Manage Subscription` di [Dashboard](https://cursor.com/dashboard) buat lihat tanggal perpanjangan.

    Pengguna gratis: Cek tanggal email Cursor pertamamu. Penggunaan ke-reset bulanan mulai dari tanggal itu.
  </Accordion>

  <Accordion title="Riwayat Chat/Composer aku hilang setelah update">
    Ruang disk yang menipis bisa bikin Cursor ngehapus data historis saat update. Biar nggak kejadian:

    1. Pastikan ruang disk bebas cukup sebelum update
    2. Rutin bersihin file sistem yang nggak perlu
    3. Backup percakapan penting sebelum update
  </Accordion>

  <Accordion title="Gimana cara uninstall Cursor?">
    Ikuti [panduan ini](https://code.visualstudio.com/docs/setup/uninstall). Ganti "VS Code" atau "Code" dengan "Cursor", dan ".vscode" dengan ".cursor".
  </Accordion>

  <Accordion title="Gimana cara hapus akun?">
    Klik `Delete Account` di [Dashboard](https://cursor.com/dashboard). Ini bakal menghapus akun dan semua data terkait secara permanen.
  </Accordion>

  <Accordion title="Gimana cara buka Cursor dari command line?">
    Jalankan `cursor` di terminal. Kalau perintahnya belum ada:

    1. Buka command palette `⌘⇧P`
    2. Ketik `install command`
    3. Pilih `Install 'cursor' command` (opsional: pasang perintah `code` untuk menimpa milik VS Code)
  </Accordion>

  <Accordion title="Nggak bisa Sign In ke Cursor">
    Kalau klik Sign In ngebuka cursor.com tapi kamu tetap nggak masuk, coba matikan firewall atau antivirus—mereka bisa ngeblokir proses sign-in.
  </Accordion>

  <Accordion title="Pesan Aktivitas Mencurigakan">
    Karena belakangan ada peningkatan penyalahgunaan, permintaanmu mungkin diblokir sebagai langkah keamanan. Begini cara beresinnya:

    Pertama, cek VPN-mu. Kalau kamu pakai, coba matikan, soalnya VPN kadang memicu sistem keamanan kami.

    Kalau masih belum kelar, kamu bisa coba:

    * Bikin chat baru
    * Tunggu sebentar lalu coba lagi
    * Bikin akun baru pakai autentikasi Google atau GitHub
    * Upgrade ke Cursor Pro
  </Accordion>
</AccordionGroup>

---

← Previous: [Server MCP](./server-mcp.md) | [Index](./index.md) | Next: [Mendapatkan ID Permintaan](./mendapatkan-id-permintaan.md) →