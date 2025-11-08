---
title: "Analytics"
source: "https://docs.cursor.com/id/account/teams/analytics"
language: "id"
language_name: "Indonesian"
---

# Analytics
Source: https://docs.cursor.com/id/account/teams/analytics

Lacak metrik penggunaan dan aktivitas tim

Admin tim bisa ngelacak metrik dari [dashboard](/id/account/teams/dashboard).

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a8a4a0ca334e5f5acac55307b2ebeadf" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=73c11df8fcb2862e5c1fd551e6399159 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c3eaa0d4faa7d6fdf5e3c79dfd11fb5a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e9ee5fc554ae46e9d0e2cf53c19e652d 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5f0afded72e0b02142c5a85e448f2d4e 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a6dec2a182ac88d7de75f7a42b1f5ff 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a8ac7dafe559da435f3f4974b04df52 2500w" />
</Frame>

<div id="total-usage">
  ### Total Usage
</div>

Lihat metrik gabungan di seluruh tim, termasuk total tab dan permintaan premium. Buat tim yang umurnya kurang dari 30 hari, metrik nunjukin penggunaan sejak tim dibuat, termasuk aktivitas anggota sebelum gabung.

<div id="per-active-user">
  ### Per Active User
</div>

Lihat rata-rata per pengguna aktif: tab yang diterima, jumlah baris kode, dan permintaan premium.

<div id="user-activity">
  ### User Activity
</div>

Lacak pengguna aktif mingguan dan bulanan.

<div id="analytics-report-headers">
  ## Header Laporan Analytics
</div>

Saat kamu mengekspor data analytics dari dashboard, laporan menyertakan metrik terperinci tentang perilaku pengguna dan penggunaan fitur. Berikut arti tiap header:

<div id="user-information">
  ### Informasi Pengguna
</div>

<ResponseField name="Date" type="ISO 8601 timestamp">
  Tanggal saat data analytics direkam (mis., 2024-01-15T04:30:00.000Z)
</ResponseField>

<ResponseField name="User ID" type="string">
  Pengidentifikasi unik untuk setiap pengguna di sistem
</ResponseField>

<ResponseField name="Email" type="string">
  Alamat email pengguna yang terhubung ke akun mereka
</ResponseField>

<ResponseField name="Is Active" type="boolean">
  Menunjukkan apakah pengguna aktif pada tanggal tersebut
</ResponseField>

<div id="ai-generated-code-metrics">
  ### Metrik Kode yang Dihasilkan AI
</div>

<ResponseField name="Chat Suggested Lines Added" type="number">
  Total baris kode yang disarankan oleh fitur chat AI
</ResponseField>

<ResponseField name="Chat Suggested Lines Deleted" type="number">
  Total baris kode yang disarankan untuk dihapus oleh chat AI
</ResponseField>

<ResponseField name="Chat Accepted Lines Added" type="number">
  Baris yang disarankan AI dan diterima lalu ditambahkan ke kode
</ResponseField>

<ResponseField name="Chat Accepted Lines Deleted" type="number">
  Penghapusan yang disarankan AI dan diterima
</ResponseField>

<div id="feature-usage-metrics">
  ### Metrik Penggunaan Fitur
</div>

<ResponseField name="Chat Total Applies" type="number">
  Jumlah penerapan perubahan yang dihasilkan AI dari chat
</ResponseField>

<ResponseField name="Chat Total Accepts" type="number">
  Jumlah penerimaan saran AI
</ResponseField>

<ResponseField name="Chat Total Rejects" type="number">
  Jumlah penolakan saran AI
</ResponseField>

<ResponseField name="Chat Tabs Shown" type="number">
  Jumlah tampilan tab saran AI kepada pengguna
</ResponseField>

<ResponseField name="Tabs Accepted" type="number">
  Jumlah tab saran AI yang diterima
</ResponseField>

<div id="request-type-metrics">
  ### Metrik Jenis Permintaan
</div>

<ResponseField name="Edit Requests" type="number">
  Permintaan yang dibuat lewat fitur composer/edit (Cmd+K inline edits)
</ResponseField>

<ResponseField name="Ask Requests" type="number">
  Permintaan chat saat pengguna mengajukan pertanyaan ke AI
</ResponseField>

<ResponseField name="Agent Requests" type="number">
  Permintaan ke AI agent (asisten AI khusus)
</ResponseField>

<ResponseField name="Cmd+K Usages" type="number">
  Jumlah penggunaan command palette Cmd+K (atau Ctrl+K)
</ResponseField>

<div id="subscription-and-api-metrics">
  ### Metrik Langganan dan API
</div>

<ResponseField name="Subscription Included Reqs" type="number">
  Permintaan AI yang tercakup dalam paket langganan pengguna
</ResponseField>

<ResponseField name="API Key Reqs" type="number">
  Permintaan yang dibuat menggunakan API key untuk akses terprogram
</ResponseField>

<ResponseField name="Usage-Based Reqs" type="number">
  Permintaan yang dihitung dalam penagihan berbasis penggunaan
</ResponseField>

<div id="additional-features">
  ### Fitur Tambahan
</div>

<ResponseField name="Bugbot Usages" type="number">
  Jumlah penggunaan fitur AI deteksi/perbaikan bug
</ResponseField>

<div id="configuration-information">
  ### Informasi Konfigurasi
</div>

<ResponseField name="Most Used Model" type="string">
  Model AI yang paling sering digunakan oleh pengguna (mis., GPT-4, Claude)
</ResponseField>

<ResponseField name="Most Used Apply Extension" type="string">
  Ekstensi file yang paling sering digunakan saat menerapkan saran AI (mis., .ts,
  .py, .java)
</ResponseField>

<ResponseField name="Most Used Tab Extension" type="string">
  Ekstensi file yang paling sering digunakan dengan fitur tab completion
</ResponseField>

<ResponseField name="Client Version" type="string">
  Versi editor Cursor yang digunakan
</ResponseField>

<div id="calculated-metrics">
  ### Metrik Terkalkulasi
</div>

Laporan juga menyertakan data terproses yang membantu memahami kontribusi kode AI:

* Total Lines Added/Deleted: Hitungan mentah semua perubahan kode
* Accepted Lines Added/Deleted: Baris yang berasal dari saran AI dan diterima
* Composer Requests: Permintaan yang dibuat lewat fitur inline composer
* Chat Requests: Permintaan yang dibuat lewat antarmuka chat

<Note>
  Semua nilai numerik default ke 0 jika tidak ada, nilai boolean default ke
  false, dan nilai string default ke string kosong. Metrik diagregasi
  harian per pengguna.
</Note>

---

← Previous: [API Pelacakan Kode AI](./api-pelacakan-kode-ai.md) | [Index](./index.md) | Next: [Analytics V2](./analytics-v2.md) →