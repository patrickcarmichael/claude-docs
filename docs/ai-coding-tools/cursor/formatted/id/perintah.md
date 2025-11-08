---
title: "Perintah"
source: "https://docs.cursor.com/id/agent/chat/commands"
language: "id"
language_name: "Indonesian"
---

# Perintah
Source: https://docs.cursor.com/id/agent/chat/commands

Tentukan perintah untuk alur kerja yang dapat digunakan ulang

Perintah kustom memungkinkan lo bikin alur kerja yang bisa dipakai ulang dan dipicu dengan awalan sederhana `/` di kotak input chat. Perintah ini bantu nyeragamin proses di seluruh tim lo dan bikin tugas-tugas umum jadi lebih efisien.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  Perintah saat ini masih beta. Fitur dan sintaksnya bisa berubah seiring kami terus ningkatin fiturnya.
</Info>

<div id="how-commands-work">
  ## Cara kerja command
</div>

Command didefinisikan sebagai file Markdown biasa yang bisa disimpan di dua lokasi:

1. **Project commands**: Disimpan di direktori `.cursor/commands` di project lo
2. **Global commands**: Disimpan di direktori `~/.cursor/commands` di home directory lo

Saat lo ngetik `/` di kotak input chat, Cursor bakal otomatis mendeteksi dan nampilin command yang tersedia dari kedua direktori tersebut, jadi langsung bisa diakses di seluruh workflow lo.

<div id="creating-commands">
  ## Membuat command
</div>

1. Bikin direktori `.cursor/commands` di root project
2. Tambahin file `.md` dengan nama yang deskriptif (misalnya, `review-code.md`, `write-tests.md`)
3. Tulis konten Markdown biasa yang ngejelasin apa yang harus dilakukan command
4. Command bakal otomatis muncul di chat pas lo ngetik `/`

Nih contoh struktur direktori command lo:

```
.cursor/
└── commands/
    ├── tanggapi-komentar-pr-github.md
    ├── daftar-periksa-code-review.md
    ├── buat-pr.md
    ├── review-ringan-diff-yang-ada.md
    ├── onboarding-developer-baru.md
    ├── jalankan-semua-test-dan-perbaiki.md
    ├── audit-keamanan.md
    └── setup-fitur-baru.md
```

<div id="examples">
  ## Contoh
</div>

Coba perintah ini di proyek lo biar kerasa cara kerjanya.

<AccordionGroup>
  <Accordion title="Checklist code review">
    ```markdown  theme={null}
    # Daftar Periksa Code Review

    ## Ikhtisar
    Daftar periksa komprehensif untuk melakukan code review menyeluruh demi memastikan kualitas, keamanan, dan kemudahan pemeliharaan.

    ## Kategori Review

    ### Fungsionalitas
    - [ ] Kode berfungsi sesuai yang diharapkan
    - [ ] Kasus tepi ditangani
    - [ ] Penanganan error sudah tepat
    - [ ] Tidak ada bug atau kesalahan logika yang jelas

    ### Kualitas Kode
    - [ ] Kode mudah dibaca dan terstruktur dengan baik
    - [ ] Fungsi kecil dan fokus
    - [ ] Nama variabel deskriptif
    - [ ] Tidak ada duplikasi kode
    - [ ] Mengikuti konvensi proyek

    ### Keamanan
    - [ ] Tidak ada kerentanan keamanan yang jelas
    - [ ] Validasi input diterapkan
    - [ ] Data sensitif ditangani dengan benar
    - [ ] Tidak ada secret yang di-hardcode
    ```
  </Accordion>

  <Accordion title="Audit keamanan">
    ```markdown  theme={null}
    # Audit Keamanan

    ## Ringkasan
    Tinjauan keamanan menyeluruh untuk mengidentifikasi dan memperbaiki kerentanan pada codebase.

    ## Langkah
    1. **Audit dependensi**
       - Periksa kerentanan yang diketahui
       - Perbarui paket yang usang
       - Tinjau dependensi pihak ketiga

    2. **Tinjauan keamanan kode**
       - Periksa kerentanan umum
       - Tinjau autentikasi/otorisasi
       - Audit praktik penanganan data

    3. **Keamanan infrastruktur**
       - Tinjau variabel lingkungan
       - Periksa kontrol akses
       - Audit keamanan jaringan

    ## Daftar Periksa Keamanan
    - [ ] Dependensi diperbarui dan aman
    - [ ] Tidak ada secret yang di-hardcode
    - [ ] Validasi input diimplementasikan
    - [ ] Autentikasi aman
    - [ ] Otorisasi dikonfigurasi dengan benar
    ```
  </Accordion>

  <Accordion title="Siapkan fitur baru">
    ```markdown  theme={null}
    # Menyiapkan Fitur Baru

    ## Ringkasan
    Menyiapkan fitur baru secara sistematis dari perencanaan awal hingga struktur implementasinya.

    ## Langkah
    1. **Tentukan requirement**
       - Perjelas cakupan dan tujuan fitur
       - Identifikasi user story dan acceptance criteria
       - Rencanakan pendekatan teknis

    2. **Buat feature branch**
       - Branch dari main/develop
       - Siapkan environment pengembangan lokal
       - Konfigurasi dependensi baru (jika ada)

    3. **Rencanakan arsitektur**
       - Rancang model data dan API
       - Rencanakan komponen UI dan alurnya
       - Pertimbangkan strategi pengujian

    ## Checklist Setup Fitur
    - [ ] Requirement terdokumentasi
    - [ ] User story ditulis
    - [ ] Pendekatan teknis direncanakan
    - [ ] Feature branch dibuat
    - [ ] Environment pengembangan siap
    ```
  </Accordion>

  <Accordion title="Buat pull request">
    ```markdown  theme={null}
    # Buat PR

    ## Ringkasan
    Bikin pull request yang terstruktur rapi dengan deskripsi, label, dan reviewer yang tepat.

    ## Langkah
    1. **Siapkan branch**
       - Pastikan semua perubahan sudah di-commit
       - Push branch ke remote
       - Pastikan branch sudah up-to-date dengan main

    2. **Tulis deskripsi PR**
       - Ringkas perubahan dengan jelas
       - Sertakan konteks dan motivasi
       - Cantumkan perubahan yang bersifat breaking
       - Tambahkan screenshot kalau ada perubahan UI

    3. **Setelan PR**
       - Bikin PR dengan judul yang deskriptif
       - Tambahkan label yang sesuai
       - Assign reviewer
       - Tautkan issue terkait

    ## Template PR
    - [ ] Fitur A
    - [ ] Perbaikan bug B
    - [ ] Unit test lulus
    - [ ] Pengujian manual selesai
    ```
  </Accordion>

  <Accordion title="Jalankan test dan perbaiki kegagalan">
    ```markdown  theme={null}
    # Jalankan Semua Tes dan Perbaiki Kegagalan

    ## Ringkasan
    Jalankan seluruh suite pengujian dan perbaiki kegagalan secara sistematis untuk memastikan kualitas dan fungsionalitas kode.

    ## Langkah
    1. **Jalankan suite pengujian**
       - Jalankan semua tes di proyek
       - Simpan output dan identifikasi kegagalan
       - Periksa baik unit test maupun integration test

    2. **Analisis kegagalan**
       - Kategorikan berdasarkan jenis: flaky, broken, failure baru
       - Prioritaskan perbaikan berdasarkan dampaknya
       - Cek apakah kegagalan terkait perubahan terbaru

    3. **Perbaiki masalah secara sistematis**
       - Mulai dari kegagalan yang paling kritis
       - Perbaiki satu masalah dalam satu waktu
       - Jalankan ulang tes setelah setiap perbaikan
    ```
  </Accordion>

  <Accordion title="Onboard developer baru">
    ```markdown  theme={null}
    # Onboarding Developer Baru

    ## Ringkasan
    Proses onboarding komprehensif agar developer baru bisa segera siap dan produktif.

    ## Langkah
    1. **Penyiapan environment**
       - Instal tool yang diperlukan
       - Siapkan environment pengembangan
       - Konfigurasi IDE dan ekstensi
       - Siapkan git dan key SSH

    2. **Pengenalan proyek**
       - Tinjau struktur proyek
       - Pahami arsitektur
       - Baca dokumentasi utama
       - Siapkan database lokal

    ## Daftar Periksa Onboarding
    - [ ] Environment pengembangan siap
    - [ ] Semua test lulus
    - [ ] Bisa menjalankan aplikasi secara lokal
    - [ ] Database disiapkan dan berjalan
    - [ ] PR pertama diajukan
    ```
  </Accordion>
</AccordionGroup>

---

← Previous: [Checkpoints](./checkpoints.md) | [Index](./index.md) | Next: [Compact](./compact.md) →