---
title: "Ikhtisar"
source: "https://docs.cursor.com/id/background-agent/api/overview"
language: "id"
language_name: "Indonesian"
---

# Ikhtisar
Source: https://docs.cursor.com/id/background-agent/api/overview

Buat dan kelola agent latar belakang yang bekerja di repositori kamu secara terprogram

<div id="background-agents-api">
  # Background Agents API
</div>

<Badge variant="beta">Beta</Badge>

Background Agents API memungkinkan lo bikin dan ngelola agen coding bertenaga AI secara terprogram yang bekerja secara otonom di repositori lo.
Lo bisa pakai API ini buat otomatis nanggepin masukan pengguna, benerin bug, update dokumentasi, dan banyak lagi!

<Info>
  Background Agents API saat ini masih beta, kami bakal seneng banget nerima masukan dari lo!
</Info>

<div id="key-features">
  ## Fitur utama
</div>

* **Pembuatan kode otonom** - Bikin agen yang bisa paham prompt lo dan ngeubah codebase lo
* **Integrasi repository** - Kerja langsung dengan repository GitHub
* Follow-up prompt - Tambahin instruksi tambahan ke agen yang lagi jalan
* **Harga berbasis penggunaan** - Bayar cuma buat token yang lo pakai
* **Skalabel** - Dukungan sampai 256 agen aktif per API key

<div id="quick-start">
  ## Mulai cepat
</div>

<div id="1-get-your-api-key">
  ### 1. Dapatkan kunci API-mu
</div>

**Buka** [Cursor Dashboard → Integrations](https://cursor.com/dashboard?tab=integrations) untuk membuat kunci API-mu.

<div id="2-start-using-the-api">
  ### 2. Mulai pakai API
</div>

Semua endpoint API relatif terhadap:

```
https://api.cursor.com
```

Lihat [referensi API](/id/background-agent/api/launch-an-agent) buat daftar endpoint yang lengkap.

<div id="authentication">
  ## Autentikasi
</div>

Semua request API perlu autentikasi dengan token Bearer:

```
Authorization: Bearer KUNCI_API_LO
```

Kunci API dibuat di [Cursor Dashboard](https://cursor.com/dashboard?tab=integrations). Kunci ini terikat ke akun lo dan memberi izin untuk membuat serta mengelola agent (tergantung batas paket lo dan akses repositori).

<div id="pricing">
  ## Harga
</div>

API saat ini masih dalam beta dengan harga yang sama seperti Background Agents. Harga bisa berubah seiring pertumbuhan layanan. Lihat [harga Background Agent](/id/account/pricing#background-agent).

<div id="next-steps">
  ## Langkah berikutnya
</div>

* Baca [ikhtisar utama Background Agents](/id/background-agent) untuk memahami environment, permissions, dan workflows.
* Coba Background Agents di [web & mobile](/id/background-agent/web-and-mobile).
* Gabung diskusi di [Discord #background-agent](https://discord.gg/jfgpZtYpmb) atau kirim email ke [background-agent-feedback@cursor.com](mailto:background-agent-feedback@cursor.com).

---

← Previous: [Daftar Repositori GitHub](./daftar-repositori-github.md) | [Index](./index.md) | Next: [Webhooks](./webhooks.md) →