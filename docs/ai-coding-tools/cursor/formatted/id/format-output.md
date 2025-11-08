---
title: "Format output"
source: "https://docs.cursor.com/id/cli/reference/output-format"
language: "id"
language_name: "Indonesian"
---

# Format output
Source: https://docs.cursor.com/id/cli/reference/output-format

Skema output untuk format teks, JSON, dan stream-JSON

Cursor Agent CLI menyediakan beberapa format output melalui opsi `--output-format` saat digabungkan dengan `--print`. Format ini mencakup format terstruktur untuk penggunaan terprogram (`json`, `stream-json`) dan format teks yang lebih sederhana untuk pelacakan progres yang mudah dibaca manusia.

<Note>
  Nilai default `--output-format` adalah `stream-json`. Opsi ini hanya berlaku saat melakukan print (`--print`) atau ketika mode print diinferensikan (stdout non-TTY atau stdin yang dipipe).
</Note>

<div id="json-format">
  ## Format JSON
</div>

Format output `json` menghasilkan satu objek JSON (diikuti baris baru) saat run selesai dengan sukses. Delta dan event tool tidak dikeluarkan; teks digabungkan ke hasil akhir.

Jika gagal, proses keluar dengan kode non-zero dan menulis pesan error ke stderr. Tidak ada objek JSON yang terformat dengan benar yang dikeluarkan dalam kasus kegagalan.

<div id="success-response">
  ### Respons sukses
</div>

Saat berhasil, CLI mengeluarkan objek JSON dengan struktur berikut:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "result": "<teks lengkap asisten>",
  "session_id": "<uuid>",
  "request_id": "<id permintaan (opsional)>"
}
```

<div class="full-width-table">
  | Field             | Deskripsi                                                                 |
  | ----------------- | ------------------------------------------------------------------------- |
  | `type`            | Selalu `"result"` untuk hasil di terminal                                 |
  | `subtype`         | Selalu `"success"` untuk penyelesaian yang sukses                         |
  | `is_error`        | Selalu `false` untuk respons yang sukses                                  |
  | `duration_ms`     | Total waktu eksekusi dalam milidetik                                      |
  | `duration_api_ms` | Waktu permintaan API dalam milidetik (saat ini sama dengan `duration_ms`) |
  | `result`          | Teks respons asisten lengkap (penggabungan semua delta teks)              |
  | `session_id`      | Identifier sesi unik                                                      |
  | `request_id`      | Identifier permintaan opsional (bisa dihilangkan)                         |
</div>

<div id="stream-json-format">
  ## Format JSON stream
</div>

Format output `stream-json` menghasilkan JSON yang dipisahkan baris baru (NDJSON). Setiap baris berisi satu objek JSON yang merepresentasikan event real-time selama eksekusi.

Stream berakhir dengan event terminal `result` saat berhasil. Jika gagal, proses keluar dengan kode non-nol dan stream bisa berakhir lebih awal tanpa event terminal; pesan error ditulis ke stderr.

<div id="event-types">
  ### Jenis event
</div>

<div id="system-initialization">
  #### Inisialisasi sistem
</div>

Dikirim sekali di awal setiap sesi:

```json  theme={null}
{
  "type": "system",
  "subtype": "init",
  "apiKeySource": "env|flag|login",
  "cwd": "/absolute/path",
  "session_id": "<uuid>",
  "model": "<model display name>",
  "permissionMode": "default"
}
```

<Note>
  Di masa mendatang, bidang seperti `tools` dan `mcp_servers` mungkin akan ditambahkan ke event ini.
</Note>

<div id="user-message">
  #### Pesan pengguna
</div>

Berisi prompt yang dimasukkan pengguna:

```json  theme={null}
{
  "type": "user",
  "message": {
    "role": "user",
    "content": [{ "type": "text", "text": "<prompt>" }]
  },
  "session_id": "<uuid>"
}
```

<div id="assistant-text-delta">
  #### Delta teks asisten
</div>

Dipancarkan beberapa kali saat asisten menghasilkan responsnya. Event ini berisi potongan teks bertahap:

```json  theme={null}
{
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [{ "type": "text", "text": "<cuplikan delta>" }]
  },
  "session_id": "<uuid>"
}
```

<Note>
  Gabungkan semua nilai `message.content[].text` secara berurutan untuk menyusun ulang respons lengkap asisten.
</Note>

<div id="tool-call-events">
  #### Peristiwa pemanggilan alat
</div>

Pemanggilan alat dilacak dengan peristiwa mulai dan selesai:

**Pemanggilan alat dimulai:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "started",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" }
    }
  },
  "session_id": "<uuid>"
}
```

**Panggilan alat selesai:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "completed",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" },
      "result": {
        "success": {
          "content": "konten file...",
          "isEmpty": false,
          "exceededLimit": false,
          "totalLines": 54,
          "totalChars": 1254
        }
      }
    }
  },
  "session_id": "<uuid>"
}
```

<div id="tool-call-types">
  #### Jenis pemanggilan tool
</div>

**Tool baca file:**

* **Dimulai**: `tool_call.readToolCall.args` memuat `{ "path": "file.txt" }`
* **Selesai**: `tool_call.readToolCall.result.success` memuat metadata dan konten file

**Tool tulis file:**

* **Dimulai**: `tool_call.writeToolCall.args` memuat `{ "path": "file.txt", "fileText": "content...", "toolCallId": "id" }`
* **Selesai**: `tool_call.writeToolCall.result.success` memuat `{ "path": "/absolute/path", "linesCreated": 19, "fileSize": 942 }`

**Tool lainnya:**

* Bisa menggunakan struktur `tool_call.function` dengan `{ "name": "tool_name", "arguments": "..." }`

<div id="terminal-result">
  #### Hasil terminal
</div>

Event terakhir yang dipancarkan saat berhasil selesai:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "is_error": false,
  "result": "<teks lengkap asisten>",
  "session_id": "<uuid>",
  "request_id": "<opsional id permintaan>"
}
```

<div id="example-sequence">
  ### Contoh urutan
</div>

Berikut adalah urutan NDJSON representatif yang menunjukkan alur kejadian yang khas:

```json  theme={null}
{"type":"system","subtype":"init","apiKeySource":"login","cwd":"/Users/user/project","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","model":"Claude 4 Sonnet","permissionMode":"default"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"Baca README.md dan buat ringkasan"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"Aku akan "}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"membaca berkas README.md"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"},"result":{"success":{"content":"# Proyek\n\nIni adalah proyek contoh...","isEmpty":false,"exceededLimit":false,"totalLines":54,"totalChars":1254}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":" dan membuat ringkasan"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# Ringkasan README\n\nProyek ini berisi...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# Ringkasan README\n\nProyek ini berisi...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"},"result":{"success":{"path":"/Users/user/project/summary.txt","linesCreated":19,"fileSize":942}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"result","subtype":"success","duration_ms":5234,"duration_api_ms":5234,"is_error":false,"result":"Aku akan membaca berkas README.md dan membuat ringkasan","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","request_id":"10e11780-df2f-45dc-a1ff-4540af32e9c0"}
```

<div id="text-format">
  ## Format teks
</div>

Format output `text` menyajikan rangkaian tindakan agen yang disederhanakan dan mudah dibaca. Alih-alih event JSON yang detail, format ini menampilkan deskripsi teks ringkas tentang apa yang lagi dilakukan agen secara real-time.

Format ini berguna buat memantau progress agen tanpa overhead parsing data terstruktur, jadi ideal buat logging, debugging, atau pelacakan progress sederhana.

<div id="example-output">
  ### Contoh output
</div>

```
Membaca file
Mengedit file
Menjalankan perintah di terminal
Membuat file baru
```

Setiap aksi muncul di baris baru saat agen mengeksekusinya, memberi umpan balik instan tentang progres agen dalam menyelesaikan tugas.

<div id="implementation-notes">
  ## Catatan implementasi
</div>

* Setiap event dipancarkan sebagai satu baris yang diakhiri dengan `\n`
* Event `thinking` disembunyikan dalam mode cetak dan tidak akan muncul di kedua format output
* Penambahan field dapat terjadi dari waktu ke waktu dengan cara yang kompatibel mundur (konsumen harus mengabaikan field yang tidak dikenal)
* Format stream memberikan pembaruan waktu nyata, sementara format JSON menunggu hingga selesai sebelum mengeluarkan hasil
* Gabungkan semua delta pesan `assistant` untuk merekonstruksi respons lengkap
* ID pemanggilan tool dapat digunakan untuk mengorelasikan event mulai/selesai
* ID sesi tetap konsisten sepanjang satu eksekusi agen

---

← Previous: [Konfigurasi](./konfigurasi.md) | [Index](./index.md) | Next: [Parameter](./parameter.md) →