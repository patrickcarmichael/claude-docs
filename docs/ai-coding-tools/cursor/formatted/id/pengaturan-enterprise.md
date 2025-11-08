---
title: "Pengaturan Enterprise"
source: "https://docs.cursor.com/id/account/teams/enterprise-settings"
language: "id"
language_name: "Indonesian"
---

# Pengaturan Enterprise
Source: https://docs.cursor.com/id/account/teams/enterprise-settings

Kelola pengaturan Cursor secara terpusat untuk organisasimu

<div id="enterprise-settings">
  # Pengaturan enterprise
</div>

Kamu bisa mengelola fitur tertentu di Cursor secara terpusat lewat solusi manajemen perangkat supaya sesuai dengan kebutuhan organisasi kamu. Saat kamu menetapkan kebijakan Cursor, nilainya akan menimpa pengaturan Cursor yang terkait di perangkat pengguna.

Editor pengaturan yang menunjukkan bahwa pengaturan 'Extensions: Allowed' dikelola oleh organisasi.

Saat ini Cursor menyediakan kebijakan untuk mengontrol fitur-fitur yang dikelola admin berikut:

| Policy            | Description                                                                                                         | Cursor setting           | Available since |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------ | --------------- |
| AllowedExtensions | Mengontrol ekstensi mana yang boleh diinstal.                                                                       | extensions.allowed       | 1.2             |
| AllowedTeamId     | Mengontrol ID tim mana yang diizinkan untuk login. Pengguna dengan ID tim yang tidak diizinkan akan dipaksa logout. | cursorAuth.allowedTeamId | 1.3             |

<div id="configure-allowed-extensions">
  ## Konfigurasi ekstensi yang diizinkan
</div>

Pengaturan Cursor `extensions.allowed` mengontrol ekstensi mana yang bisa dipasang. Pengaturan ini menerima objek JSON dengan key berupa nama publisher dan value berupa boolean yang menunjukkan apakah ekstensi dari publisher tersebut diizinkan.

Contohnya, menyetel `extensions.allowed` ke `{"anysphere": true, "github": true}` mengizinkan ekstensi dari publisher Anysphere dan GitHub, sedangkan menyetelnya ke `{"anysphere": false}` memblokir ekstensi dari Anysphere.

Untuk mengelola ekstensi yang diizinkan secara terpusat buat organisasimu, konfigurasikan kebijakan `AllowedExtensions` menggunakan solusi manajemen perangkat lo. Kebijakan ini menimpa pengaturan `extensions.allowed` di perangkat pengguna. Nilai kebijakan ini adalah string JSON yang mendefinisikan publisher yang diizinkan.

Kalau lo mau belajar lebih lanjut tentang ekstensi di Cursor, lihat dokumentasi ekstensi.

<div id="configure-allowed-team-ids">
  ## Konfigurasi ID tim yang diizinkan
</div>

Pengaturan Cursor `cursorAuth.allowedTeamId` ngatur ID tim mana yang boleh login ke Cursor. Pengaturan ini nerima daftar ID tim yang dipisahkan koma yang diotorisasi buat akses.

Misalnya, ngeset `cursorAuth.allowedTeamId` ke `"1,3,7"` ngebolehin pengguna dari ID tim tersebut buat login.

Kalau pengguna coba login pakai ID tim yang nggak ada di daftar yang diizinkan:

* Mereka langsung dipaksa logout
* Muncul pesan error
* Aplikasi ngeblok percobaan autentikasi berikutnya sampai ID tim yang valid dipakai

Buat ngatur ID tim yang diizinkan secara terpusat buat organisasi lo, konfigurasikan kebijakan `AllowedTeamId` pakai solusi manajemen perangkat lo. Kebijakan ini ngeganti pengaturan `cursorAuth.allowedTeamId` di perangkat pengguna. Nilai kebijakan ini berupa string yang berisi daftar ID tim yang diotorisasi dan dipisahkan koma.

<div id="group-policy-on-windows">
  ## Group Policy di Windows
</div>

Cursor mendukung Group Policy berbasis Windows Registry. Saat definisi kebijakan dipasang, admin bisa pakai Local Group Policy Editor buat ngatur nilai kebijakan.

Cara nambahin kebijakan:

1. Salin file ADMX dan ADML kebijakan dari `AppData\Local\Programs\cursor\policies`.
2. Tempel file ADMX ke direktori `C:\Windows\PolicyDefinitions`, dan file ADML ke direktori `C:\Windows\PolicyDefinitions\<your-locale>\`.
3. Restart Local Group Policy Editor.
4. Setel nilai kebijakan yang sesuai (contoh: `{"anysphere": true, "github": true}` untuk kebijakan `AllowedExtensions`) di Local Group Policy Editor.

Kebijakan bisa disetel di level Computer maupun User. Kalau dua-duanya disetel, level Computer bakal jadi prioritas. Saat nilai kebijakan disetel, nilai itu akan menimpa nilai pengaturan Cursor yang dikonfigurasi di level mana pun (default, user, workspace, dll.).

<div id="configuration-profiles-on-macos">
  ## Profil konfigurasi di macOS
</div>

Profil konfigurasi mengelola pengaturan di perangkat macOS. Profil adalah file XML berisi pasangan key/value yang sesuai dengan kebijakan yang tersedia. Profil bisa didistribusikan lewat solusi Mobile Device Management (MDM) atau dipasang manual.

<Accordion title="Contoh file .mobileconfig">
  Contoh file `.mobileconfig` untuk macOS ada di bawah:

  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  <plist version="1.0">
  	<dict>
  		<key>PayloadContent</key>
  		<array>
  			<dict>
  				<key>PayloadDisplayName</key>
  				<string>Cursor</string>
  				<key>PayloadIdentifier</key>
  				<string>com.todesktop.230313mzl4w4u92.J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadType</key>
  				<string>com.todesktop.230313mzl4w4u92</string>
  				<key>PayloadUUID</key>
  				<string>J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadVersion</key>
  				<integer>1</integer>
  				<key>AllowedExtensions</key>
  				<string>{"anysphere":true}</string>
  				<key>AllowedTeamId</key>
  				<string>1,2</string>
  			</dict>
  		</array>
  		<key>PayloadDescription</key>
  		<string>This profile manages Cursor.</string>
  		<key>PayloadDisplayName</key>
  		<string>Cursor</string>
  		<key>PayloadIdentifier</key>
  		<string>com.todesktop.230313mzl4w4u92</string>
  		<key>PayloadOrganization</key>
  		<string>Anysphere</string>
  		<key>PayloadType</key>
  		<string>Configuration</string>
  		<key>PayloadUUID</key>
  		<string>F2C1A7B3-9D4E-4B2C-8E1F-7A6C5D4B3E2F</string>
  		<key>PayloadVersion</key>
  		<integer>1</integer>
  		<key>TargetDeviceType</key>
  		<integer>5</integer>
  	</dict>
  </plist>
  ```
</Accordion>

<div id="string-policies">
  ### Kebijakan string
</div>

Contoh berikut menunjukkan konfigurasi kebijakan `AllowedExtensions`. Nilai kebijakan di file sampel awalnya kosong (tidak ada ekstensi yang diizinkan).

```
<key>EkstensiDiizinkan</key>
<string></string>
```

Tambahkan string JSON yang sesuai yang mendefinisikan policy lo di antara tag `<string>`.

```
<key>AllowedExtensions</key>
<string>{"anysphere": true, "github": true}</string>
```

Untuk kebijakan `AllowedTeamId`, tambahkan daftar ID tim yang dipisahkan koma:

```
<key>AllowedTeamId</key>
<string>1,3,7</string>
```

**Penting:** File `.mobileconfig` yang disediakan menginisialisasi **semua** kebijakan yang tersedia di versi Cursor tersebut. Hapus kebijakan yang nggak kamu butuhkan.

Kalau kamu nggak mengedit atau menghapus suatu kebijakan dari contoh `.mobileconfig`, kebijakan itu bakal diterapkan dengan nilai default (lebih ketat).

Pasang profil konfigurasi secara manual dengan mengklik dua kali profil `.mobileconfig` di Finder, lalu aktifkan di System Settings lewat **General** > **Device Management**. Menghapus profil dari System Settings bakal menghapus kebijakan dari Cursor.

Untuk info selengkapnya tentang profil konfigurasi, lihat dokumentasi Apple.

<div id="additional-policies">
  ## Kebijakan tambahan
</div>

Tujuannya adalah mengangkat pengaturan Cursor saat ini menjadi kebijakan dan mengikuti pengaturan yang ada dengan ketat, supaya penamaan dan perilakunya konsisten. Kalau ada permintaan untuk menerapkan lebih banyak kebijakan, buka issue di repositori GitHub Cursor. Tim bakal menentukan apakah sudah ada pengaturan yang sesuai untuk perilaku tersebut atau perlu dibuat pengaturan baru untuk mengontrol perilaku yang diinginkan.

<div id="frequently-asked-questions">
  ## Pertanyaan yang sering diajukan
</div>

<div id="does-cursor-support-configuration-profiles-on-linux">
  ### Apakah Cursor mendukung profil konfigurasi di Linux?
</div>

Dukungan untuk Linux belum ada di roadmap. Kalau lo tertarik sama profil konfigurasi di Linux, buka issue di repositori GitHub Cursor dan ceritain detail skenario lo.

---

← Previous: [Dashboard](./dashboard.md) | [Index](./index.md) | Next: [Anggota & Peran](./anggota-peran.md) →