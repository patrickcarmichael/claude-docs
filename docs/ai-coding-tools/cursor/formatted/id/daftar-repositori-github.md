---
title: "Daftar Repositori GitHub"
source: "https://docs.cursor.com/id/background-agent/api/list-repositories"
language: "id"
language_name: "Indonesian"
---

# Daftar Repositori GitHub
Source: https://docs.cursor.com/id/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Ambil daftar repositori GitHub yang bisa diakses oleh pengguna terautentikasi.

<Warning>
  **Endpoint ini punya rate limit yang sangat ketat.**

  Batasin request ke **1 / pengguna / menit**, dan **30 / pengguna / jam.**

  Request ini bisa butuh puluhan detik buat ngerespons kalau pengguna punya akses ke banyak repositori.

  Pastikan lo nangani kondisi saat informasi ini nggak tersedia dengan baik.
</Warning>

---

← Previous: [Daftar Model](./daftar-model.md) | [Index](./index.md) | Next: [Ikhtisar](./ikhtisar.md) →