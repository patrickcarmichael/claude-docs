---
title: "Webhooks"
source: "https://docs.cursor.com/id/background-agent/api/webhooks"
language: "id"
language_name: "Indonesian"
---

# Webhooks
Source: https://docs.cursor.com/id/background-agent/api/webhooks

Dapatkan notifikasi real-time tentang perubahan status agen latar belakang

<div id="webhooks">
  # Webhooks
</div>

Saat bikin agent dengan URL webhook, Cursor bakal ngirim request HTTP POST buat ngasih tahu perubahan status. Saat ini, cuma event `statusChange` yang didukung, khususnya ketika agent masuk ke state `ERROR` atau `FINISHED`.

<div id="webhook-verification">
  ## Verifikasi webhook
</div>

Biar yakin request webhook benar-benar dari Cursor, verifikasi signature yang disertakan di setiap request:

<div id="headers">
  ### Headers
</div>

Setiap request webhook menyertakan header berikut:

* **`X-Webhook-Signature`** – Berisi signature HMAC-SHA256 dengan format `sha256=<hex_digest>`
* **`X-Webhook-ID`** – Identifier unik untuk delivery ini (berguna buat logging)
* **`X-Webhook-Event`** – Jenis event (saat ini hanya `statusChange`)
* **`User-Agent`** – Selalu di-set ke `Cursor-Agent-Webhook/1.0`

<div id="signature-verification">
  ### Verifikasi signature
</div>

Buat verifikasi signature webhook, hitung signature yang diharapkan lalu bandingkan dengan signature yang diterima:

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
  const expectedSignature = 'sha256=' + 
    crypto.createHmac('sha256', secret)
          .update(rawBody)
          .digest('hex');
  
  return signature === expectedSignature;
}
```

```python  theme={null}
import hmac
import hashlib

def verify_webhook(secret, raw_body, signature):
    expected_signature = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return signature == expected_signature
```

Selalu gunakan body request mentah (sebelum pemrosesan atau parsing apa pun) saat menghitung signature.

<div id="payload-format">
  ## Format payload
</div>

Payload webhook dikirim dalam bentuk JSON dengan struktur berikut:

```json  theme={null}
{
  "event": "statusChange",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "Menambahkan README.md berisi panduan instalasi"
}
```

Perlu dicatat, beberapa field itu opsional dan cuma bakal disertakan kalau tersedia.

<div id="best-practices">
  ## Praktik terbaik
</div>

* **Verifikasi signature** – Selalu verifikasi signature webhook buat memastikan permintaan itu dari Cursor
* **Tangani retry** – Webhook bisa dicoba ulang kalau endpoint kamu ngembaliin status code error
* **Balas cepat** – Balikin status code 2xx secepat mungkin
* **Pakai HTTPS** – Selalu pakai URL HTTPS buat endpoint webhook di production
* **Simpan payload mentah** – Simpan payload webhook mentah buat debugging dan verifikasi ke depannya

---

← Previous: [Ikhtisar](./ikhtisar.md) | [Index](./index.md) | Next: [Web & Mobile](./web-mobile.md) →