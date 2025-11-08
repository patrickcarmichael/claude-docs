---
title: "Webhook’lar"
source: "https://docs.cursor.com/tr/background-agent/api/webhooks"
language: "tr"
language_name: "Turkish"
---

# Webhook’lar
Source: https://docs.cursor.com/tr/background-agent/api/webhooks

Arka plan aracısı durum değişiklikleri için gerçek zamanlı bildirimler al

<div id="webhooks">
  # Webhook'lar
</div>

Bir agent'i bir webhook URL'siyle oluşturduğunda, Cursor durum değişiklikleri hakkında seni bilgilendirmek için HTTP POST istekleri gönderir. Şu anda yalnızca `statusChange` olayları destekleniyor; özellikle bir agent `ERROR` veya `FINISHED` durumuna geçtiğinde.

<div id="webhook-verification">
  ## Webhook doğrulama
</div>

Webhook isteklerinin gerçekten Cursor’dan geldiğinden emin olmak için, her isteğe eklenen imzayı doğrula:

<div id="headers">
  ### Headers
</div>

Her webhook isteği aşağıdaki header’ları içerir:

* **`X-Webhook-Signature`** – `sha256=<hex_digest>` formatında HMAC-SHA256 imzasını içerir
* **`X-Webhook-ID`** – Bu teslimat için benzersiz bir tanımlayıcı (loglama için yararlı)
* **`X-Webhook-Event`** – Olay türü (şu anda yalnızca `statusChange`)
* **`User-Agent`** – Her zaman `Cursor-Agent-Webhook/1.0` olarak ayarlanır

<div id="signature-verification">
  ### İmza doğrulama
</div>

Webhook imzasını doğrulamak için beklenen imzayı hesapla ve alınan imzayla karşılaştır:

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

def webhooku_dogrula(gizli_anahtar, ham_govde, imza):
    beklenen_imza = 'sha256=' + hmac.new(
        gizli_anahtar.encode(),
        ham_govde,
        hashlib.sha256
    ).hexdigest()
    
    return imza == beklenen_imza
```

İmzayı hesaplarken her zaman pars edilmeden önceki ham istek gövdesini kullan.

<div id="payload-format">
  ## Yük biçimi
</div>

Webhook yükü, aşağıdaki yapıda JSON olarak gönderilir:

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
  "summary": "Kurulum talimatlarını içeren README.md eklendi"
}
```

Bazı alanların isteğe bağlı olduğunu ve yalnızca mevcut olduklarında dahil edileceğini unutma.

<div id="best-practices">
  ## En iyi uygulamalar
</div>

* **İmzaları doğrula** – İsteğin Cursor’dan geldiğinden emin olmak için webhook imzasını her zaman doğrula
* **Yeniden denemeleri ele al** – Uç noktan hata durum kodu döndürürse webhooks yeniden denenebilir
* **Hızlı yanıt ver** – Mümkün olan en kısa sürede 2xx durum kodu döndür
* **HTTPS kullan** – Üretimde webhook uç noktaları için her zaman HTTPS URL’leri kullan
* **Ham payload’ları sakla** – Hata ayıklama ve ilerideki doğrulamalar için ham webhook payload’ını sakla

---

← Previous: [Genel Bakış](./genel-bak.md) | [Index](./index.md) | Next: [Web ve Mobil](./web-ve-mobil.md) →