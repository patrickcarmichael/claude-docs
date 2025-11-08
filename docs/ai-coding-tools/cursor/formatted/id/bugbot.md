---
title: "Bugbot"
source: "https://docs.cursor.com/id/bugbot"
language: "id"
language_name: "Indonesian"
---

# Bugbot
Source: https://docs.cursor.com/id/bugbot

Tinjauan kode AI untuk pull request

Bugbot meninjau pull request dan mengidentifikasi bug, isu keamanan, dan masalah kualitas kode.

<Tip>
  Bugbot punya paket gratis: setiap user dapat jatah tinjauan PR gratis tiap bulan. Saat mencapai batas, tinjauan akan dijeda sampai siklus penagihan berikutnya. Lo bisa upgrade kapan aja ke uji coba Pro gratis 14 hari untuk tinjauan tanpa batas (dengan guardrail anti-penyalahgunaan standar).
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="Bugbot ninggalin komentar di PR" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

<div id="how-it-works">
  ## Cara kerjanya
</div>

Bugbot menganalisis diff PR dan meninggalkan komentar berisi penjelasan serta saran perbaikan. Ini berjalan otomatis di setiap pembaruan PR atau bisa dijalankan manual saat dipicu.

* Menjalankan **review otomatis** di setiap pembaruan PR
* **Pemicu manual** dengan komentar `cursor review` atau `bugbot run` di PR mana pun
* Tautan **Fix in Cursor** membuka issue langsung di Cursor
* Tautan **Fix in Web** membuka issue langsung di [cursor.com/agents](https://cursor.com/agents)

<div id="setup">
  ## Setup
</div>

Butuh akses admin Cursor dan admin untuk organisasi GitHub.

1. Buka [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot)
2. Buka tab Bugbot
3. Klik `Connect GitHub` (atau `Manage Connections` kalau sudah terhubung)
4. Ikuti alur instalasi GitHub
5. Balik ke dashboard untuk mengaktifkan Bugbot di repositori tertentu

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Pengaturan Bugbot di GitHub" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

<div id="configuration">
  ## Konfigurasi
</div>

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### Pengaturan repositori

    Aktifkan atau nonaktifkan Bugbot per repositori dari daftar instalasi lo. Bugbot cuma jalan di PR yang lo bikin.

    ### Pengaturan personal

    * Jalan **hanya kalau disebut** dengan komentar `cursor review` atau `bugbot run`
    * Jalan **hanya sekali** per PR, ngelewatin commit berikutnya
  </Tab>

  <Tab title="Team">
    ### Pengaturan repositori

    Admin tim bisa ngaktifin Bugbot per repositori, nyetel allow/deny list buat reviewer, dan ngatur:

    * Jalan **hanya sekali** per PR per instalasi, ngelewatin commit berikutnya
    * **Nonaktifkan inline review** biar Bugbot gak ninggalin komentar langsung di baris kode

    Bugbot jalan buat semua kontributor di repositori yang diaktifkan, terlepas dari keanggotaan tim.

    ### Pengaturan personal

    Anggota tim bisa override pengaturan buat PR mereka sendiri:

    * Jalan **hanya kalau disebut** dengan komentar `cursor review` atau `bugbot run`
    * Jalan **hanya sekali** per PR, ngelewatin commit berikutnya
    * **Aktifkan review di draft PR** buat nyertain draft pull request dalam review otomatis
  </Tab>
</Tabs>

<div id="analytics">
  ### Analitik
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Dasbor Bugbot" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

<div id="rules">
  ## Aturan
</div>

Buat file `.cursor/BUGBOT.md` untuk ngasih konteks spesifik proyek buat review. Bugbot selalu nyertakan file `.cursor/BUGBOT.md` di root dan file tambahan apa pun yang ketemu saat menelusuri naik dari file yang diubah.

```
project/
  .cursor/BUGBOT.md          # Selalu disertakan (aturan tingkat proyek)
  backend/
    .cursor/BUGBOT.md        # Disertakan saat meninjau file backend
    api/
      .cursor/BUGBOT.md      # Disertakan saat meninjau file API
  frontend/
    .cursor/BUGBOT.md        # Disertakan saat meninjau file frontend
```

<AccordionGroup>
  <Accordion title="Contoh .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # Pedoman peninjauan proyek

    ## Fokus keamanan

    - Validasi input pengguna di endpoint API
    - Periksa kerentanan SQL injection dalam kueri database
    - Pastikan autentikasi yang benar pada rute yang dilindungi

    ## Pola arsitektur

    - Gunakan dependency injection untuk layanan
    - Ikuti pola repository untuk akses data
    - Terapkan penanganan error yang tepat dengan kelas error kustom

    ## Masalah umum

    - Kebocoran memori di komponen React (cek cleanup di useEffect)
    - Tidak ada error boundary di komponen UI
    - Konvensi penamaan tidak konsisten (gunakan camelCase untuk fungsi)

    ```
  </Accordion>
</AccordionGroup>

<div id="pricing">
  ## Harga
</div>

Bugbot menawarkan dua paket: **Gratis** dan **Pro**.

<div id="free-tier">
  ### Paket gratis
</div>

Setiap user dapat jatah terbatas untuk review PR gratis tiap bulan. Buat tim, tiap anggota tim punya jatah review gratisnya sendiri. Begitu nyentuh batas, review bakal ke-pause sampai siklus penagihan berikutnya. Kamu bisa upgrade kapan aja ke uji coba Pro 14 hari gratis buat review tanpa batas.

<div id="pro-tier">
  ### Paket Pro
</div>

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### Tarif tetap

    \$40 per bulan untuk review Bugbot tanpa batas pada hingga 200 PR per bulan di semua repositori.

    ### Memulai

    Berlangganan lewat pengaturan akun.
  </Tab>

  <Tab title="Teams">
    ### Penagihan per pengguna

    Tim membayar \$40 per pengguna per bulan untuk review tanpa batas.

    Kami menganggap pengguna sebagai seseorang yang membuat PR yang direview oleh Bugbot dalam satu bulan.

    Semua lisensi dilepas di awal setiap siklus penagihan, dan akan dialokasikan berdasarkan urutan pendaftaran. Kalau seorang pengguna nggak membuat PR apa pun yang direview oleh Bugbot dalam satu bulan, kursi tersebut bisa dipakai oleh pengguna lain.

    ### Batas kursi

    Admin tim bisa menetapkan jumlah maksimum kursi Bugbot per bulan untuk mengontrol biaya.

    ### Memulai

    Berlangganan lewat dasbor tim untuk mengaktifkan penagihan.

    ### Pembatasan penyalahgunaan

    Untuk mencegah penyalahgunaan, kami punya batas gabungan 200 pull request per bulan untuk setiap lisensi Bugbot. Kalau kamu butuh lebih dari 200 pull request per bulan, hubungi kami di [hi@cursor.com](mailto:hi@cursor.com) dan kami dengan senang hati bakal bantu.

    Misalnya, kalau tim kamu punya 100 pengguna, organisasi kamu awalnya bisa mereview 20.000 pull request per bulan. Kalau kamu mencapai batas itu secara natural, silakan hubungi kami dan kami dengan senang hati akan menaikkan batasnya.
  </Tab>
</Tabs>

<div id="troubleshooting">
  ## Pemecahan Masalah
</div>

Kalau Bugbot nggak jalan:

1. **Aktifin mode verbose** dengan nge-comment `cursor review verbose=true` atau `bugbot run verbose=true` buat log detail dan request ID
2. **Cek permissions** buat mastihin Bugbot punya akses ke repository
3. **Cek instalasi** buat mastihin GitHub app ke-install dan aktif

Sertakan request ID dari mode verbose waktu ngelaporin masalah.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Apakah Bugbot sesuai dengan mode privasi?">
    Ya, Bugbot mengikuti kepatuhan privasi yang sama seperti Cursor dan memproses data dengan cara yang sama seperti permintaan Cursor lainnya.
  </Accordion>

  <Accordion title="Apa yang terjadi saat aku mencapai batas paket gratis?">
    Saat kamu mencapai batas paket gratis bulanan, peninjauan Bugbot akan dijeda sampai siklus penagihan berikutnya. Kamu bisa upgrade ke uji coba Pro gratis 14 hari untuk peninjauan tanpa batas (dengan perlindungan penyalahgunaan standar).
  </Accordion>
</AccordionGroup>

```
```

---

← Previous: [Web & Mobile](./web-mobile.md) | [Index](./index.md) | Next: [Code Review](./code-review.md) →