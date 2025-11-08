---
title: "SSO"
source: "https://docs.cursor.com/id/account/teams/sso"
language: "id"
language_name: "Indonesian"
---

# SSO
Source: https://docs.cursor.com/id/account/teams/sso

Setel single sign-on buat tim lo

<div id="overview">
  ## Ikhtisar
</div>

SSO SAML 2.0 tersedia tanpa biaya tambahan di paket Business. Pakai identity provider (IdP) yang sudah ada buat mengautentikasi anggota tim tanpa perlu akun Cursor terpisah.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## Prasyarat
</div>

* Paket Cursor Team
* Akses admin ke penyedia identitas lo (misalnya Okta)
* Akses admin ke organisasi Cursor lo

<div id="configuration-steps">
  ## Langkah Konfigurasi
</div>

<Steps>
  <Step title="Masuk ke akun Cursor lo">
    Buka [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings) pakai akun admin.
  </Step>

  <Step title="Cari konfigurasi SSO">
    Temuin bagian "Single Sign-On (SSO)" lalu buka.
  </Step>

  <Step title="Mulai proses setup">
    Klik tombol "SSO Provider Connection settings" buat mulai setup SSO dan ikutin wizard.
  </Step>

  <Step title="Konfigurasi identity provider lo">
    Di identity provider lo (misalnya Okta):

    * Bikin aplikasi SAML baru
    * Konfigurasi pengaturan SAML pakai info dari Cursor
    * Set up Just-in-Time (JIT) provisioning
  </Step>

  <Step title="Verifikasi domain">
    Verifikasi domain user lo di Cursor dengan klik tombol "Domain verification settings".
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### Panduan Setup Identity Provider
</div>

Buat instruksi setup per provider:

<Card title="Panduan Identity Provider" icon="book" href="https://workos.com/docs/integrations">
  Instruksi setup untuk Okta, Azure AD, Google Workspace, dan lainnya.
</Card>

<div id="additional-settings">
  ## Pengaturan Tambahan
</div>

* Atur penerapan SSO lewat dasbor admin
* Pengguna baru otomatis terdaftar saat masuk lewat SSO
* Kelola pengguna lewat penyedia identitas lo

<div id="troubleshooting">
  ## Pemecahan Masalah
</div>

Kalau ada masalah:

* Pastikan domain sudah terverifikasi di Cursor
* Pastikan atribut SAML dipetakan dengan benar
* Cek SSO sudah diaktifkan di dasbor admin
* Samakan nama depan dan belakang antara identity provider dan Cursor
* Cek panduan khusus penyedia di atas
* Hubungi [hi@cursor.com](mailto:hi@cursor.com) kalau masalah tetap berlanjut

---

← Previous: [Mulai](./mulai.md) | [Index](./index.md) | Next: [Akses Pembaruan](./akses-pembaruan.md) →