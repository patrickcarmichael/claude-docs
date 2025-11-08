---
title: "Admin API"
source: "https://docs.cursor.com/id/account/teams/admin-api"
language: "id"
language_name: "Indonesian"
---

# Admin API
Source: https://docs.cursor.com/id/account/teams/admin-api

Akses metrik tim, data penggunaan, dan informasi pengeluaran lewat API

Admin API bikin lo bisa ngeakses data tim lo secara terprogram, termasuk info member, metrik penggunaan, dan detail pengeluaran. Bangun dashboard kustom, alat monitoring, atau integrasiin ke workflow yang udah ada.

<Note>
  API ini baru rilis pertama. Kita lagi nambahin kapabilitas berdasarkan feedback — kasih tahu kita endpoint apa yang lo butuhin!
</Note>

<div id="authentication">
  ## Autentikasi
</div>

Semua permintaan API memerlukan autentikasi menggunakan kunci API. Hanya admin tim yang bisa membuat dan mengelola kunci API.

Kunci API terikat ke organisasi, dapat dilihat oleh semua admin, dan tidak terpengaruh oleh status akun pembuatnya.

<div id="creating-an-api-key">
  ### Membuat API Key
</div>

1. Buka **cursor.com/dashboard** → tab **Settings** → **Cursor Admin API Keys**
2. Klik **Create New API Key**
3. Kasih nama yang deskriptif buat key lo (misalnya, "Usage Dashboard Integration")
4. Segera salin key yang dihasilkan — lo nggak bakal bisa lihat itu lagi

Format: `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### Pakai API key lo
</div>

Pakai API key lo sebagai username di basic authentication:

**Pakai curl dengan basic auth:**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**Atau atur header Authorization secara langsung:**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## URL Dasar
</div>

Semua endpoint API menggunakan:

```
https://api.cursor.com
```

<div id="endpoints">
  ## Endpoint
</div>

<div id="get-team-members">
  ### Ambil Anggota Tim
</div>

Mengambil semua anggota tim beserta detailnya.

```
GET /teams/members
```

#### Respons

Mengembalikan array objek anggota tim:

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
  }[];
}
```

#### Contoh Tanggapan

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "member"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "owner"
    }
  ]
}

```

<div id="example-requests">
  #### Contoh Permintaan
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u API_KEY_KAMU:
```

<div id="get-daily-usage-data">
  ### Dapatkan Data Penggunaan Harian
</div>

Ambil metrik penggunaan harian yang detail buat tim lo dalam rentang tanggal tertentu. Ngasih insight tentang pengeditan kode, penggunaan bantuan AI, dan tingkat penerimaan.

```
POST /teams/daily-usage-data
```

#### Body Request

<div className="full-width-table">
  | Parameter   | Type   | Required | Description                         |
  | :---------- | :----- | :------- | :---------------------------------- |
  | `startDate` | number | Yes      | Tanggal mulai dalam milidetik epoch |
  | `endDate`   | number | Yes      | Tanggal akhir dalam milidetik epoch |
</div>

<Note>
  Rentang tanggal nggak boleh lebih dari 90 hari. Buat beberapa request untuk periode yang lebih panjang.
</Note>

#### Respons

```typescript  theme={null}
{
  data: {
    date: number;
    isActive: boolean;
    totalLinesAdded: number;
    totalLinesDeleted: number;
    acceptedLinesAdded: number;
    acceptedLinesDeleted: number;
    totalApplies: number;
    totalAccepts: number;
    totalRejects: number;
    totalTabsShown: number;
    totalTabsAccepted: number;
    composerRequests: number;
    chatRequests: number;
    agentRequests: number;
    cmdkUsages: number;
    subscriptionIncludedReqs: number;
    apiKeyReqs: number;
    usageBasedReqs: number;
    bugbotUsages: number;
    mostUsedModel: string;
    applyMostUsedExtension?: string;
    tabMostUsedExtension?: string;
    clientVersion?: string;
    email?: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### Kolom Respons
</div>

<div className="full-width-table">
  | Field                      | Description                                              |
  | :------------------------- | :------------------------------------------------------- |
  | `date`                     | Tanggal dalam milidetik epoch                            |
  | `isActive`                 | Pengguna aktif pada hari tersebut                        |
  | `totalLinesAdded`          | Jumlah baris kode yang ditambahkan                       |
  | `totalLinesDeleted`        | Jumlah baris kode yang dihapus                           |
  | `acceptedLinesAdded`       | Jumlah baris dari saran AI yang diterima dan ditambahkan |
  | `acceptedLinesDeleted`     | Jumlah baris dari saran AI yang diterima dan dihapus     |
  | `totalApplies`             | Operasi apply                                            |
  | `totalAccepts`             | Saran yang diterima                                      |
  | `totalRejects`             | Saran yang ditolak                                       |
  | `totalTabsShown`           | Tab completion yang ditampilkan                          |
  | `totalTabsAccepted`        | Tab completion yang diterima                             |
  | `composerRequests`         | Permintaan Composer                                      |
  | `chatRequests`             | Permintaan Chat                                          |
  | `agentRequests`            | Permintaan Agent                                         |
  | `cmdkUsages`               | Penggunaan Command Palette (Cmd+K)                       |
  | `subscriptionIncludedReqs` | Permintaan yang termasuk dalam langganan                 |
  | `apiKeyReqs`               | Permintaan API key                                       |
  | `usageBasedReqs`           | Permintaan bayar per penggunaan                          |
  | `bugbotUsages`             | Penggunaan deteksi bug                                   |
  | `mostUsedModel`            | Model AI yang paling sering digunakan                    |
  | `applyMostUsedExtension`   | Ekstensi file yang paling sering digunakan untuk apply   |
  | `tabMostUsedExtension`     | Ekstensi file yang paling sering digunakan untuk tab     |
  | `clientVersion`            | Versi Cursor                                             |
  | `email`                    | Email pengguna                                           |
</div>

#### Contoh Tanggapan

```json  theme={null}
{
  "data": [
    {
      "date": 1710720000000,
      "isActive": true,
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalApplies": 87,
      "totalAccepts": 73,
      "totalRejects": 14,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "cmdkUsages": 67,
      "subscriptionIncludedReqs": 180,
      "apiKeyReqs": 0,
      "usageBasedReqs": 5,
      "bugbotUsages": 3,
      "mostUsedModel": "gpt-4",
      "applyMostUsedExtension": ".tsx",
      "tabMostUsedExtension": ".ts",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    },
    {
      "date": 1710806400000,
      "isActive": true,
      "totalLinesAdded": 2104,
      "totalLinesDeleted": 1203,
      "acceptedLinesAdded": 1876,
      "acceptedLinesDeleted": 987,
      "totalApplies": 102,
      "totalAccepts": 91,
      "totalRejects": 11,
      "totalTabsShown": 456,
      "totalTabsAccepted": 398,
      "composerRequests": 67,
      "chatRequests": 156,
      "agentRequests": 23,
      "cmdkUsages": 89,
      "subscriptionIncludedReqs": 320,
      "apiKeyReqs": 15,
      "usageBasedReqs": 0,
      "bugbotUsages": 5,
      "mostUsedModel": "claude-3-opus",
      "applyMostUsedExtension": ".py",
      "tabMostUsedExtension": ".py",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

<div id="example-requests">
  #### Contoh Permintaan
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u API_KEY_KAMU: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### Dapatkan Data Pengeluaran
</div>

Ambil data pengeluaran untuk bulan kalender berjalan, lengkap dengan pencarian, penyortiran, dan pagination.

```
POST /teams/spend
```

#### Request Body

<div className="full-width-table">
  | Parameter       | Type   | Required | Description                                                |
  | :-------------- | :----- | :------- | :--------------------------------------------------------- |
  | `searchTerm`    | string | No       | Cari di nama dan email pengguna                            |
  | `sortBy`        | string | No       | Urutkan menurut: `amount`, `date`, `user`. Default: `date` |
  | `sortDirection` | string | No       | Arah pengurutan: `asc`, `desc`. Default: `desc`            |
  | `page`          | number | No       | Nomor halaman (indeks mulai 1). Default: `1`               |
  | `pageSize`      | number | No       | Jumlah hasil per halaman                                   |
</div>

#### Respons

```typescript  theme={null}
{
  teamMemberSpend: {
    spendCents: number;
    fastPremiumRequests: number;
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
    hardLimitOverrideDollars: number;
  }[];
  subscriptionCycleStart: number;
  totalMembers: number;
  totalPages: number;
}
```

#### Field Respons

<div className="full-width-table">
  | Field                      | Description                              |
  | :------------------------- | :--------------------------------------- |
  | `spendCents`               | Total pengeluaran dalam sen              |
  | `fastPremiumRequests`      | Permintaan model premium cepat           |
  | `name`                     | Nama anggota                             |
  | `email`                    | Email anggota                            |
  | `role`                     | Peran dalam tim                          |
  | `hardLimitOverrideDollars` | Penggantian batas pengeluaran kustom     |
  | `subscriptionCycleStart`   | Mulai siklus langganan (milidetik epoch) |
  | `totalMembers`             | Total anggota tim                        |
  | `totalPages`               | Total halaman                            |
</div>

#### Contoh Tanggapan

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "member",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "owner"
      "hardLimitOverrideDollars": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

<div id="example-requests">
  #### Contoh Permintaan
</div>

**Data pengeluaran dasar:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Cari pengguna tertentu dengan paginasi:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

<div id="get-usage-events-data">
  ### Dapatkan Data Event Penggunaan
</div>

Ambil data event penggunaan yang detail untuk tim lo, dengan opsi filter, pencarian, dan paginasi yang lengkap. Endpoint ini ngasih insight granular tentang panggilan API per request, penggunaan model, konsumsi token, dan biaya.

```
POST /teams/filtered-usage-events
```

<div id="request-body">
  #### Body Permintaan
</div>

<div className="full-width-table">
  | Parameter   | Tipe   | Wajib | Deskripsi                                     |
  | :---------- | :----- | :---- | :-------------------------------------------- |
  | `startDate` | number | Tidak | Tanggal mulai dalam milidetik epoch           |
  | `endDate`   | number | Tidak | Tanggal akhir dalam milidetik epoch           |
  | `userId`    | number | Tidak | Filter berdasarkan ID pengguna tertentu       |
  | `page`      | number | Tidak | Nomor halaman (diindeks dari 1). Default: `1` |
  | `pageSize`  | number | Tidak | Jumlah hasil per halaman. Default: `10`       |
  | `email`     | string | Tidak | Filter berdasarkan alamat email pengguna      |
</div>

#### Respons

```typescript  theme={null}
{
  totalUsageEventsCount: number;
  pagination: {
    numPages: number;
    currentPage: number;
    pageSize: number;
    hasNextPage: boolean;
    hasPreviousPage: boolean;
  };
  usageEvents: {
    timestamp: string;
    model: string;
    kind: string;
    maxMode: boolean;
    requestsCosts: number;
    isTokenBasedCall: boolean;
    tokenUsage?: {
      inputTokens: number;
      outputTokens: number;
      cacheWriteTokens: number;
      cacheReadTokens: number;
      totalCents: number;
    };
    isFreeBugbot: boolean;
    userEmail: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields-explained">
  #### Penjelasan Field Respons
</div>

<div className="full-width-table">
  | Field                   | Description                                                           |
  | :---------------------- | :-------------------------------------------------------------------- |
  | `totalUsageEventsCount` | Jumlah total event penggunaan yang sesuai dengan query                |
  | `pagination`            | Metadata paginasi untuk menavigasi hasil                              |
  | `timestamp`             | Stempel waktu event dalam epoch millisecond                           |
  | `model`                 | Model AI yang dipakai untuk request                                   |
  | `kind`                  | Kategori penggunaan (mis., "Usage-based", "Included in Business")     |
  | `maxMode`               | Apakah max mode diaktifkan                                            |
  | `requestsCosts`         | Biaya dalam unit request                                              |
  | `isTokenBasedCall`      | True saat event ditagihkan sebagai event berbasis penggunaan          |
  | `tokenUsage`            | Rincian konsumsi token (tersedia saat isTokenBasedCall bernilai true) |
  | `isFreeBugbot`          | Apakah ini penggunaan bugbot gratis                                   |
  | `userEmail`             | Email user yang membuat request                                       |
  | `period`                | Rentang tanggal dari data yang di-query                               |
</div>

#### Contoh Tanggapan

```json  theme={null}
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "model": "claude-4-opus",
      "kind": "Berbasis penggunaan",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750979173824",
      "model": "claude-4-opus",
      "kind": "Usage-based",
      "maxMode": true,
      "requestsCosts": 10,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 5805,
        "outputTokens": 311,
        "cacheWriteTokens": 11964,
        "cacheReadTokens": 0,
        "totalCents": 40.16699999999999
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750978339901",
      "model": "claude-4-sonnet-thinking",
      "kind": "Termasuk dalam Paket Business"
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isFreeBugbot": false,
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

<div id="example-requests">
  #### Contoh Permintaan
</div>

**Ambil semua peristiwa penggunaan dengan paginasi default:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Filter berdasarkan rentang tanggal dan pengguna tertentu:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u API_KEY_KAMU: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**Ambil event penggunaan untuk user tertentu dengan paginasi kustom:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### Set Batas Pengeluaran Pengguna
</div>

Atur batas pengeluaran buat tiap anggota tim. Ini bikin lo bisa ngatur seberapa banyak tiap user boleh ngehabisin buat penggunaan AI di tim lo.

```
POST /teams/batas-pengeluaran-user
```

<Note>
  **Batas laju:** 60 permintaan per menit per tim
</Note>

#### Request Body

<div className="full-width-table">
  | Parameter           | Type   | Required | Description                                                          |
  | :------------------ | :----- | :------- | :------------------------------------------------------------------- |
  | `userEmail`         | string | Yes      | Alamat email anggota tim                                             |
  | `spendLimitDollars` | number | Yes      | Batas pengeluaran dalam dolar (hanya bilangan bulat, tanpa desimal). |
</div>

<Note>
  * Pengguna harus sudah menjadi anggota tim kamu
  * Hanya nilai bilangan bulat yang diterima (tanpa angka desimal)
  * Mengatur `spendLimitDollars` ke 0 akan menetapkan batas menjadi \$0
</Note>

#### Respons

Mengembalikan respons standar yang menunjukkan apakah operasi berhasil atau gagal:

```typescript  theme={null}
{
  outcome: 'sukses' | 'error';
  message: string;
}
```

<div id="example-responses">
  #### Contoh Respons
</div>

**Berhasil mengatur batas:**

```json  theme={null}
{
  "outcome": "sukses",
  "message": "Batas pengeluaran ditetapkan menjadi $100 untuk pengguna developer@company.com"
}
```

**Respons kesalahan:**

```json  theme={null}
{
  "outcome": "error",
  "message": "Format email tidak valid"
}
```

<div id="example-requests">
  #### Contoh Permintaan
</div>

**Atur batas pengeluaran:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### Repo Blocklists API
</div>

Tambahkan repositori dan terapkan pola untuk mencegah file atau direktori diindeks atau digunakan sebagai konteks buat tim.

<div id="get-team-repo-blocklists">
  #### Dapatkan Blocklist Repo Tim
</div>

Ambil semua blocklist repository yang dikonfigurasi untuk tim lo.

```
GET /settings/repo-blocklists/repos
```

<div id="response">
  ##### Respons
</div>

Mengembalikan array objek daftar blokir repositori:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-response">
  ##### Contoh Tanggapan
</div>

```json  theme={null}
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

<div id="example-request">
  ##### Contoh Permintaan
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u API_KEY_KAMU:
```

<div id="upsert-repo-blocklists">
  #### Upsert Repo Blocklists
</div>

Ganti blocklist repo yang sudah ada untuk repo yang diberikan.
*Catatan: Endpoint ini cuma bakal menimpa pola untuk repo yang diberikan. Repo lainnya nggak akan terpengaruh.*

```
POST /settings/repo-blocklists/repos/upsert
```

##### Request Body

| Parameter | Type  | Required | Description                      |
| --------- | ----- | -------- | -------------------------------- |
| repos     | array | Yes      | Array objek blocklist repository |

Setiap objek repository harus berisi:

| Field    | Type      | Required | Description                                              |
| -------- | --------- | -------- | -------------------------------------------------------- |
| url      | string    | Yes      | URL repository untuk dimasukkan ke blocklist             |
| patterns | string\[] | Yes      | Array pola file yang akan diblokir (mendukung pola glob) |

<div id="response">
  ##### Respons
</div>

Mengembalikan daftar blocklist repositori yang diperbarui:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-request">
  ##### Contoh Permintaan
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u API_KEY_KAMU: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      },
      {
        "url": "https://github.com/company/internal-tools", 
        "patterns": ["*"]
      }
    ]
  }'
```

<div id="delete-repo-blocklist">
  #### Hapus Daftar Blokir Repo
</div>

Hapus repositori tertentu dari daftar blokir.

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### Parameter
</div>

| Parameter | Tipe   | Wajib | Deskripsi                                 |
| --------- | ------ | ----- | ----------------------------------------- |
| repoId    | string | Ya    | ID blocklist repositori yang akan dihapus |

<div id="response">
  ##### Respons
</div>

Mengembalikan 204 No Content ketika penghapusan berhasil.

<div id="example-request">
  ##### Contoh Permintaan
</div>

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u KUNCI_API_LO:
```

<div id="pattern-examples">
  #### Contoh Pola
</div>

Pola blocklist yang umum:

* `*` - Blokir seluruh repository
* `*.env` - Blokir semua file .env
* `config/*` - Blokir semua file di direktori config
* `**/*.secret` - Blokir semua file .secret di subdirektori mana pun
* `src/api/keys.ts` - Blokir file tertentu

---

← Previous: [Harga](./harga.md) | [Index](./index.md) | Next: [API Pelacakan Kode AI](./api-pelacakan-kode-ai.md) →