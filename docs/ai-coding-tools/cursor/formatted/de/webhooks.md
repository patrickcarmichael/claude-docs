---
title: "Webhooks"
source: "https://docs.cursor.com/de/background-agent/api/webhooks"
language: "de"
language_name: "German"
---

# Webhooks
Source: https://docs.cursor.com/de/background-agent/api/webhooks

Erhalte Echtzeit-Benachrichtigungen über Statusänderungen von Background Agents

<div id="webhooks">
  # Webhooks
</div>

Wenn du einen Agent mit einer Webhook-URL erstellst, sendet Cursor HTTP-POST-Anfragen, um dich über Statusänderungen zu informieren. Derzeit werden nur `statusChange`-Events unterstützt – konkret, wenn ein Agent den Zustand `ERROR` oder `FINISHED` erreicht.

<div id="webhook-verification">
  ## Webhook-Verifizierung
</div>

Um sicherzugehen, dass die Webhook-Anfragen wirklich von Cursor stammen, überprüf die Signatur, die jeder Anfrage beigefügt ist:

<div id="headers">
  ### Header
</div>

Jede Webhook-Anfrage enthält die folgenden Header:

* **`X-Webhook-Signature`** – Enthält die HMAC-SHA256-Signatur im Format `sha256=<hex_digest>`
* **`X-Webhook-ID`** – Eine eindeutige Kennung für diese Zustellung (nützlich fürs Logging)
* **`X-Webhook-Event`** – Der Ereignistyp (aktuell nur `statusChange`)
* **`User-Agent`** – Immer gesetzt auf `Cursor-Agent-Webhook/1.0`

<div id="signature-verification">
  ### Signaturüberprüfung
</div>

Um die Webhook-Signatur zu verifizieren, berechne die erwartete Signatur und vergleiche sie mit der empfangenen:

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

Verwende zum Berechnen der Signatur immer den unveränderten Request-Body (vor jeglicher Parsing-Logik).

<div id="payload-format">
  ## Payload-Format
</div>

Die Webhook-Payload wird als JSON mit folgender Struktur gesendet:

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
  "summary": "README.md mit Installationsanleitung hinzugefügt"
}
```

Beachte, dass einige Felder optional sind und nur angezeigt werden, wenn sie verfügbar sind.

<div id="best-practices">
  ## Best Practices
</div>

* **Signaturen prüfen** – überprüf die Webhook-Signatur, um sicherzustellen, dass die Anfrage von Cursor kommt
* **Retries behandeln** – Webhooks können erneut zugestellt werden, wenn dein Endpoint einen Fehlerstatuscode zurückgibt
* **Schnell antworten** – gib so schnell wie möglich einen 2xx-Statuscode zurück
* **HTTPS verwenden** – nutz in Produktion immer HTTPS-URLs für Webhook-Endpoints
* **Rohpayloads speichern** – speichere die rohe Webhook-Payload fürs Debugging und für spätere Verifizierung

---

← Previous: [Überblick](./berblick.md) | [Index](./index.md) | Next: [Web & Mobile](./web-mobile.md) →