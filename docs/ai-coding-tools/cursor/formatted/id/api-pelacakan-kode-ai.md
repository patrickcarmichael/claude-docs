---
title: "API Pelacakan Kode AI"
source: "https://docs.cursor.com/id/account/teams/ai-code-tracking-api"
language: "id"
language_name: "Indonesian"
---

# API Pelacakan Kode AI
Source: https://docs.cursor.com/id/account/teams/ai-code-tracking-api

Akses analitik kode berbasis AI buat repositori tim lo

Akses analitik kode berbasis AI buat repositori tim lo. Ini mencakup penggunaan AI per commit serta perubahan AI yang diterima secara granular.

<Note>
  API ini baru rilis pertama. Kami lagi nambah kapabilitas berdasarkan feedback—kasih tahu kami endpoint apa yang lo butuhin!
</Note>

* **Ketersediaan**: Hanya buat tim enterprise
* **Status**: Alpha (bentuk respons dan field bisa berubah)

<div id="authentication">
  ## Autentikasi
</div>

Semua request ke API harus diautentikasi pakai API key. API ini menggunakan skema autentikasi Admin API yang sama seperti endpoint lainnya.

Untuk panduan autentikasi yang lebih rinci, lihat [Admin API authentication](/id/account/teams/admin-api#authentication).

<div id="base-url">
  ## URL Dasar
</div>

Semua endpoint API menggunakan:

```
https://api.cursor.com
```

<div id="rate-limits">
  ## Batas Permintaan
</div>

* 5 permintaan per menit per tim, per endpoint

<div id="query-parameters">
  ## Parameter Query
</div>

Semua endpoint di bawah menerima parameter query yang sama lewat query string:

<div className="full-width-table">
  | Parameter   | Type   | Required | Description                                                                                                                                                                         |                                                                                                                           |
  | :---------- | :----- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
  | `startDate` | string | date     | No                                                                                                                                                                                  | String tanggal ISO, literal "now", atau hari relatif seperti "7d" (berarti sekarang - 7 hari). Default: sekarang - 7 hari |
  | `endDate`   | string | date     | No                                                                                                                                                                                  | String tanggal ISO, literal "now", atau hari relatif seperti "0d". Default: sekarang                                      |
  | `page`      | number | No       | Nomor halaman (basis 1). Default: 1                                                                                                                                                 |                                                                                                                           |
  | `pageSize`  | number | No       | Jumlah hasil per halaman. Default: 100, Maks: 1000                                                                                                                                  |                                                                                                                           |
  | `user`      | string | No       | Filter opsional untuk satu pengguna. Menerima email (mis., [developer@company.com](mailto:developer@company.com)), ID terenkode (mis., user\_abc123...), atau ID numerik (mis., 42) |                                                                                                                           |
</div>

<Note>
  Respons mengembalikan userId sebagai ID eksternal terenkode dengan prefiks user\_. Nilai ini stabil untuk konsumsi API.
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## Semantik dan Cara Perhitungan Metrik
</div>

* **Sumber**: "TAB" merepresentasikan inline completions yang diterima; "COMPOSER" merepresentasikan diff yang diterima dari Composer
* **Metrik baris**: tabLinesAdded/Deleted dan composerLinesAdded/Deleted dihitung terpisah; nonAiLinesAdded/Deleted diturunkan sebagai max(0, totalLines - AI lines)
* **Mode privasi**: Jika diaktifkan di klien, beberapa metadata (seperti fileName) mungkin dihilangkan
* **Info branch**: isPrimaryBranch bernilai true ketika branch saat ini sama dengan default branch repo; bisa undefined jika info repo tidak tersedia

Lo bisa nge-scan file itu buat paham gimana commit dan perubahan dideteksi dan dilaporkan.

<div id="endpoints">
  ## Endpoint
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### Dapatkan Metrik Commit AI (JSON, dengan pagination)
</div>

Ambil metrik agregat per-commit yang mengatribusikan baris ke TAB, COMPOSER, dan non-AI.

```
GET /analytics/ai-code/commits
```

#### Respons

```typescript  theme={null}
{
  items: AiCommitMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### Field AiCommitMetric
</div>

<div className="full-width-table">
  | Field                  | Type    | Description                                   |                                   |
  | :--------------------- | :------ | :-------------------------------------------- | --------------------------------- |
  | `commitHash`           | string  | Hash commit Git                               |                                   |
  | `userId`               | string  | ID pengguna terenkode (mis., user\_abc123)    |                                   |
  | `userEmail`            | string  | Alamat email pengguna                         |                                   |
  | `repoName`             | string  | null                                          | Nama repositori                   |
  | `branchName`           | string  | null                                          | Nama branch                       |
  | `isPrimaryBranch`      | boolean | null                                          | Apakah ini branch utama           |
  | `totalLinesAdded`      | number  | Total baris yang ditambahkan dalam commit     |                                   |
  | `totalLinesDeleted`    | number  | Total baris yang dihapus dalam commit         |                                   |
  | `tabLinesAdded`        | number  | Baris yang ditambahkan lewat penyelesaian TAB |                                   |
  | `tabLinesDeleted`      | number  | Baris yang dihapus lewat penyelesaian TAB     |                                   |
  | `composerLinesAdded`   | number  | Baris yang ditambahkan lewat Composer         |                                   |
  | `composerLinesDeleted` | number  | Baris yang dihapus lewat Composer             |                                   |
  | `nonAiLinesAdded`      | number  | null                                          | Baris non-AI yang ditambahkan     |
  | `nonAiLinesDeleted`    | number  | null                                          | Baris non-AI yang dihapus         |
  | `message`              | string  | null                                          | Pesan commit                      |
  | `commitTs`             | string  | null                                          | Stempel waktu commit (format ISO) |
  | `createdAt`            | string  | Stempel waktu ingestion (format ISO)          |                                   |
</div>

<div id="example-response">
  #### Contoh Respons
</div>

```json  theme={null}
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "Refactor: ekstraksi klien analytics"
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

<div id="example-requests">
  #### Contoh Permintaan
</div>

**Permintaan dasar:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u API_KEY_KAMU:
```

**Filter berdasarkan pengguna (email):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u API_KEY_KAMU:
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### Download Metrik Commit AI (CSV, streaming)
</div>

Unduh data metrik commit dalam format CSV untuk ekstraksi data berskala besar.

```
GET /analytics/ai-code/commits.csv
```

#### Respons

Header:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### Kolom CSV
</div>

<div className="full-width-table">
  | Kolom                    | Tipe    | Deskripsi                                    |
  | :----------------------- | :------ | :------------------------------------------- |
  | `commit_hash`            | string  | Hash commit Git                              |
  | `user_id`                | string  | ID pengguna yang dienkode                    |
  | `user_email`             | string  | Alamat email pengguna                        |
  | `repo_name`              | string  | Nama repositori                              |
  | `branch_name`            | string  | Nama branch                                  |
  | `is_primary_branch`      | boolean | Apakah ini branch utama                      |
  | `total_lines_added`      | number  | Total baris yang ditambahkan dalam commit    |
  | `total_lines_deleted`    | number  | Total baris yang dihapus dalam commit        |
  | `tab_lines_added`        | number  | Baris yang ditambahkan lewat pelengkapan TAB |
  | `tab_lines_deleted`      | number  | Baris yang dihapus lewat pelengkapan TAB     |
  | `composer_lines_added`   | number  | Baris yang ditambahkan lewat Composer        |
  | `composer_lines_deleted` | number  | Baris yang dihapus lewat Composer            |
  | `non_ai_lines_added`     | number  | Baris non-AI yang ditambahkan                |
  | `non_ai_lines_deleted`   | number  | Baris non-AI yang dihapus                    |
  | `message`                | string  | Pesan commit                                 |
  | `commit_ts`              | string  | Timestamp commit (format ISO)                |
  | `created_at`             | string  | Timestamp ingest (format ISO)                |
</div>

<div id="sample-csv-output">
  #### Contoh Output CSV
</div>

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"Refactor: ekstraksi klien analitik",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"Tambahkan penanganan error",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-requests">
  #### Contoh Permintaan
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u API_KEY_KAMU: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### Dapatkan Metrik Perubahan Kode AI (JSON, paginasi)
</div>

Ambil perubahan AI terperinci yang diterima, dikelompokkan berdasarkan changeId deterministik. Berguna buat nganalisis event AI yang diterima secara independen dari commit.

```
GET /analytics/ai-code/changes
```

<div id="response">
  #### Tanggapan
</div>

```typescript  theme={null}
{
  items: AiCodeChangeMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### Field AiCodeChangeMetric
</div>

<div className="full-width-table">
  | Field               | Type   | Description                                                  |                         |
  | :------------------ | :----- | :----------------------------------------------------------- | ----------------------- |
  | `changeId`          | string | ID deterministik untuk perubahan                             |                         |
  | `userId`            | string | ID pengguna yang dienkode (misalnya, user\_abc123)           |                         |
  | `userEmail`         | string | Alamat email pengguna                                        |                         |
  | `source`            | "TAB"  | "COMPOSER"                                                   | Sumber perubahan AI     |
  | `model`             | string | null                                                         | Model AI yang digunakan |
  | `totalLinesAdded`   | number | Total baris yang ditambahkan                                 |                         |
  | `totalLinesDeleted` | number | Total baris yang dihapus                                     |                         |
  | `createdAt`         | string | Timestamp ingestion (format ISO)                             |                         |
  | `metadata`          | Array  | Metadata file (fileName bisa dihilangkan dalam mode privasi) |                         |
</div>

<div id="example-response">
  #### Contoh Respons
</div>

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
      "metadata": [
        { "fileName": "src/analytics/report.ts", "fileExtension": "ts", "linesAdded": 12, "linesDeleted": 3 },
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

<div id="example-requests">
  #### Contoh Permintaan
</div>

**Permintaan dasar:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u API_KEY_KAMU:
```

**Filter berdasarkan pengguna (ID terenkripsi):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u API_KEY_KAMU:
```

**Filter berdasarkan pengguna (email):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u KUNCI_API_LO:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### Unduh Metrik Perubahan Kode AI (CSV, streaming)
</div>

Unduh data metrik perubahan dalam format CSV untuk ekstraksi data berskala besar.

```
GET /analytics/ai-code/changes.csv
```

#### Respons

Header:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### Kolom CSV
</div>

<div className="full-width-table">
  | Kolom                 | Tipe   | Deskripsi                                       |
  | :-------------------- | :----- | :---------------------------------------------- |
  | `change_id`           | string | ID deterministik untuk perubahan                |
  | `user_id`             | string | ID pengguna yang dienkode                       |
  | `user_email`          | string | Alamat email pengguna                           |
  | `source`              | string | Sumber perubahan AI (TAB atau COMPOSER)         |
  | `model`               | string | Model AI yang digunakan                         |
  | `total_lines_added`   | number | Total baris yang ditambahkan                    |
  | `total_lines_deleted` | number | Total baris yang dihapus                        |
  | `created_at`          | string | Timestamp ingestion (format ISO)                |
  | `metadata_json`       | string | Array entri metadata yang dijadikan string JSON |
</div>

<div id="notes">
  #### Catatan
</div>

* metadata\_json adalah array entri metadata yang dijadikan string JSON (mungkin menghilangkan fileName dalam mode privasi)
* Saat memproses CSV, pastikan untuk mengurai field yang diapit tanda kutip

<div id="sample-csv-output">
  #### Contoh Output CSV
</div>

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-requests">
  #### Contoh Permintaan
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u API_KEY_KAMU: \
  -o changes.csv
```

<div id="tips">
  ## Tips
</div>

* Pakai parameter `user` buat cepat filter satu user di semua endpoint
* Buat ekstraksi data besar, pilih endpoint CSV—mereka nge-stream per halaman 10.000 record di sisi server
* `isPrimaryBranch` bisa undefined kalau client nggak bisa resolve default branch
* `commitTs` adalah timestamp commit; `createdAt` adalah waktu ingestion di server kami
* Beberapa field mungkin nggak ada kalau privacy mode diaktifkan di client

<div id="changelog">
  ## Changelog
</div>

* **Rilis alpha**: Endpoint awal untuk commit dan perubahan. Bentuk respons bisa berubah seiring masukan

---

← Previous: [Admin API](./admin-api.md) | [Index](./index.md) | Next: [Analytics](./analytics.md) →