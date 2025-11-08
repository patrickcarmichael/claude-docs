---
title: "SCIM"
source: "https://docs.cursor.com/id/account/teams/scim"
language: "id"
language_name: "Indonesian"
---

# SCIM
Source: https://docs.cursor.com/id/account/teams/scim

Siapkan provisioning SCIM untuk otomatisasi pengelolaan pengguna dan grup

<div id="overview">
  ## Gambaran Umum
</div>

Provisioning SCIM 2.0 otomatis ngatur anggota tim dan grup direktori lewat identity provider lo. Tersedia di paket Enterprise dengan SSO diaktifkan.

<product_visual type="screenshot">
  Dasbor pengaturan SCIM yang menampilkan konfigurasi Active Directory Management
</product_visual>

<div id="prerequisites">
  ## Prasyarat
</div>

* Paket Cursor Enterprise
* SSO harus dikonfigurasi dulu — **SCIM perlu koneksi SSO yang aktif**
* Akses admin ke penyedia identitas lo (Okta, Azure AD, dll.)
* Akses admin ke organisasi Cursor lo

<div id="how-it-works">
  ## Cara kerjanya
</div>

<div id="user-provisioning">
  ### Provisioning pengguna
</div>

Pengguna otomatis ditambahkan ke Cursor saat ditetapkan ke aplikasi SCIM di identity provider kamu. Saat penetapan dicabut, mereka akan dihapus. Perubahan disinkronkan secara real-time.

<div id="directory-groups">
  ### Grup direktori
</div>

Grup direktori beserta keanggotaannya disinkronkan dari identity provider kamu. Pengelolaan grup dan pengguna harus dilakukan melalui identity provider kamu—Cursor menampilkan informasi ini sebagai read-only.

<div id="spend-management">
  ### Manajemen pengeluaran
</div>

Atur batas pengeluaran per pengguna yang berbeda untuk setiap grup direktori. Batas grup direktori memiliki prioritas dibanding batas di tingkat tim. Pengguna yang berada di beberapa grup akan menerima batas pengeluaran tertinggi yang berlaku.

<div id="setup">
  ## Penyiapan
</div>

<Steps>
  <Step title="Pastikan SSO sudah dikonfigurasi">
    SCIM memerlukan SSO disiapkan terlebih dulu. Kalau kamu belum mengonfigurasi SSO,
    ikuti [panduan penyiapan SSO](/id/account/teams/sso) sebelum lanjut.
  </Step>

  <Step title="Akses Active Directory Management">
    Buka
    [cursor.com/dashboard?tab=active-directory](https://www.cursor.com/dashboard?tab=active-directory)
    dengan akun admin, atau masuk ke pengaturan dashboard dan pilih tab
    "Active Directory Management".
  </Step>

  <Step title="Mulai penyiapan SCIM">
    Setelah SSO terverifikasi, kamu bakal lihat tautan untuk penyiapan SCIM langkah demi langkah. Klik
    ini untuk mulai wizard konfigurasi.
  </Step>

  <Step title="Konfigurasikan SCIM di identity provider kamu">
    Di identity provider kamu: Buat atau konfigurasikan aplikasi SCIM. Gunakan
    SCIM endpoint dan token yang disediakan Cursor. Aktifkan provisioning pengguna dan push grup.
    Uji koneksinya.
  </Step>

  <Step title="Atur batas pengeluaran (opsional)">
    Kembali ke halaman Active Directory Management di Cursor: Lihat grup direktori
    yang tersinkron. Setel batas pengeluaran per pengguna untuk grup tertentu sesuai kebutuhan.
    Tinjau batas yang berlaku untuk pengguna yang ada di beberapa grup.
  </Step>
</Steps>

<div id="identity-provider-setup">
  ### Penyiapan identity provider
</div>

Untuk instruksi penyiapan spesifik per provider:

<Card title="Panduan Identity Provider" icon="book" href="https://workos.com/docs/integrations">
  Instruksi penyiapan untuk Okta, Azure AD, Google Workspace, dan lainnya.
</Card>

<div id="managing-users-and-groups">
  ## Mengelola pengguna dan grup
</div>

<Warning>
  Semua pengelolaan pengguna dan grup harus dilakukan lewat identity provider lo.
  Perubahan yang lo buat di identity provider bakal otomatis tersinkron ke Cursor, tapi
  lo nggak bisa langsung ngubah pengguna atau grup di Cursor.
</Warning>

<div id="user-management">
  ### Manajemen pengguna
</div>

* Tambahin pengguna dengan nge-assign mereka ke aplikasi SCIM lo di identity provider
* Hapus pengguna dengan nge-unassign mereka dari aplikasi SCIM
* Perubahan profil pengguna (nama, email) bakal otomatis tersinkron dari identity provider lo

<div id="group-management">
  ### Manajemen grup
</div>

* Grup direktori otomatis disinkronkan dari identity provider lo
* Perubahan keanggotaan grup bakal keliatan secara real-time
* Pakai grup buat ngatur pengguna dan ngeset batas pengeluaran yang berbeda

<div id="spend-limits">
  ### Batas pengeluaran
</div>

* Set batas per pengguna yang berbeda untuk tiap grup direktori
* Pengguna bakal mewarisi batas pengeluaran tertinggi dari grup mereka
* Batas grup bakal nge-override batas default per pengguna di seluruh tim

<div id="faq">
  ## FAQ
</div>

<div id="why-isnt-scim-management-showing-up-in-my-dashboard">
  ### Kenapa manajemen SCIM nggak muncul di dashboard?
</div>

Pastikan SSO udah dikonfigurasi dengan benar dan jalan sebelum nyetel SCIM. SCIM butuh koneksi SSO yang aktif buat berfungsi.

<div id="why-arent-users-syncing">
  ### Kenapa pengguna nggak ke-sync?
</div>

Pastikan pengguna udah ditetapkan (assigned) ke aplikasi SCIM di identity provider. Pengguna harus ditetapkan secara eksplisit biar muncul di Cursor.

<div id="why-arent-groups-appearing">
  ### Kenapa grup nggak muncul?
</div>

Cek apakah push group provisioning diaktifkan di pengaturan SCIM di identity provider. Sinkronisasi grup harus dikonfigurasi terpisah dari sinkronisasi pengguna.

<div id="why-arent-spend-limits-applying">
  ### Kenapa batas pengeluaran nggak kepakai?
</div>

Pastikan pengguna udah ditetapkan ke grup yang sesuai di identity provider. Keanggotaan grup yang nentuin batas pengeluaran mana yang berlaku.

<div id="can-i-manage-scim-users-and-groups-directly-in-cursor">
  ### Bisa nggak ngelola pengguna dan grup SCIM langsung di Cursor?
</div>

Nggak. Semua manajemen pengguna dan grup harus dilakukan lewat identity provider. Cursor nampilin info ini sebagai read-only.

<div id="how-quickly-do-changes-sync">
  ### Perubahan ke-sync secepat apa?
</div>

Perubahan yang dibuat di identity provider bakal ke-sync ke Cursor secara real-time. Mungkin ada jeda singkat buat operasi bulk yang besar.

---

← Previous: [Anggota & Peran](./anggota-peran.md) | [Index](./index.md) | Next: [Mulai](./mulai.md) →