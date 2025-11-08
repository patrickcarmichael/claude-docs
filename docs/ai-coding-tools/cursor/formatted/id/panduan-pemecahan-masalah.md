---
title: "Panduan Pemecahan Masalah"
source: "https://docs.cursor.com/id/troubleshooting/troubleshooting-guide"
language: "id"
language_name: "Indonesian"
---

# Panduan Pemecahan Masalah
Source: https://docs.cursor.com/id/troubleshooting/troubleshooting-guide

Langkah untuk memperbaiki masalah dan melaporkan bug

Masalah di Cursor bisa berasal dari ekstensi, data aplikasi, atau gangguan sistem. Coba langkah pemecahan masalah berikut.

<CardGroup cols={1}>
  <Card horizontal title="Melaporkan Masalah" icon="bug" href="#reporting-an-issue">
    Langkah untuk melaporkan masalah ke tim Cursor
  </Card>
</CardGroup>

<div id="troubleshooting">
  ## Pemecahan Masalah
</div>

<Steps>
  <Step title="Periksa konektivitas jaringan">
    Pertama, cek apakah Cursor bisa terhubung ke layanannya.

    **Jalankan diagnostik jaringan:** Buka `Cursor Settings` > `Network` dan klik `Run Diagnostics`. Ini akan menguji koneksi ke server Cursor dan mengidentifikasi masalah jaringan yang memengaruhi fitur AI, pembaruan, atau fungsionalitas online lainnya.

    Kalau diagnostik menunjukkan masalah konektivitas, cek pengaturan firewall, konfigurasi proxy, atau pembatasan jaringan yang memblokir akses Cursor.
  </Step>

  <Step title="Menghapus data ekstensi">
    Untuk masalah ekstensi:

    **Nonaktifkan semua ekstensi sementara:** Jalankan `cursor --disable-extensions` dari command line. Kalau masalahnya hilang, aktifkan lagi ekstensi satu per satu untuk menemukan yang bermasalah.

    **Reset data ekstensi:** Copot dan pasang ulang ekstensi yang bermasalah untuk mereset data yang tersimpan. Cek juga pengaturan ekstensi yang tetap bertahan setelah pemasangan ulang.
  </Step>

  <Step title="Menghapus data aplikasi">
    <Warning>
      Tindakan ini akan menghapus data aplikasi, termasuk ekstensi, tema, snippet, dan data terkait instalasi. Ekspor profil dulu biar data ini tetap tersimpan.
    </Warning>

    Cursor menyimpan data aplikasi di luar aplikasi agar bisa dipulihkan saat pembaruan atau pemasangan ulang.

    Untuk menghapus data aplikasi:

    **Windows:** Jalankan perintah berikut di Command Prompt:

    ```txt  theme={null}
    rd /s /q "%USERPROFILE%\AppData\Local\Programs\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Local\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Roaming\Cursor"
    del /f /q "%USERPROFILE%\.cursor*"
    rd /s /q "%USERPROFILE%\.cursor"
    ```

    **MacOS:** Jalankan `sudo rm -rf ~/Library/Application\ Support/Cursor` dan `rm -f ~/.cursor.json` di Terminal.

    **Linux:** Jalankan `rm -rf ~/.cursor ~/.config/Cursor/` di Terminal.
  </Step>

  <Step title="Menghapus instalasi Cursor">
    Untuk menghapus instalasi Cursor:

    <CardGroup cols={1}>
      <Card horizontal title="Windows" icon="windows">
        Cari "Add or Remove Programs" di Start Menu, temukan "Cursor", klik "Uninstall".
      </Card>

      <Card horizontal title="MacOS" icon="apple">
        Buka folder Applications, klik kanan "Cursor", pilih "Move to Trash".
      </Card>

      <Card horizontal title="Linux" icon="linux">
        **Untuk paket .deb:** `sudo apt remove cursor`

        **Untuk paket .rpm:** `sudo dnf remove cursor` atau `sudo yum remove cursor`

        **Untuk AppImage:** Hapus file Cursor.appimage dari lokasinya.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Menginstal ulang Cursor">
    Instal ulang dari [halaman Downloads](https://www.cursor.com/downloads). Kalau kamu nggak menghapus data aplikasi, Cursor akan dipulihkan ke keadaan sebelumnya. Kalau dihapus, kamu bakal dapat instalasi yang benar-benar baru.
  </Step>
</Steps>

<div id="reporting-an-issue">
  ## Melaporkan Masalah
</div>

Kalau langkah-langkah ini nggak membantu, laporkan ke [forum](https://forum.cursor.com/).

<Card horizontal title="Cursor Forum" icon="message" href="https://forum.cursor.com/">
  Laporkan bug atau masalah di forum Cursor
</Card>

Biar cepat ditangani, sertakan:

<CardGroup cols={2}>
  <Card title="Screenshot of Issue" icon="image">
    Ambil screenshot, sembunyikan info sensitif.
  </Card>

  <Card title="Steps to Reproduce" icon="list-check">
    Dokumentasikan langkah-langkah persis untuk mereproduksi masalah.
  </Card>

  <Card title="System Information" icon="computer">
    Dapatkan info sistem dari:

    <br />

    `Cursor` > `Help` > `About`
  </Card>

  <Card title="Request IDs" icon="shield-halved" href="/id/troubleshooting/request-reporting">
    Klik untuk melihat panduan mengumpulkan Request ID
  </Card>

  <Card title="Console Errors" icon="bug">
    Cek developer console: <br />
    `Developer: Toggle Developer Tools`
  </Card>

  <Card title="Logs" icon="file-lines">
    Akses log: <br />
    `Developer: Open Logs Folder`
  </Card>
</CardGroup>

---

← Previous: [Mendapatkan ID Permintaan](./mendapatkan-id-permintaan.md) | [Index](./index.md) | Next: [Selamat datang](./selamat-datang.md) →