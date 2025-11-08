---
title: "Webhooks"
source: "https://docs.cursor.com/es/background-agent/api/webhooks"
language: "es"
language_name: "Spanish"
---

# Webhooks
Source: https://docs.cursor.com/es/background-agent/api/webhooks

Recibe notificaciones en tiempo real sobre cambios en el estado del agente en segundo plano

<div id="webhooks">
  # Webhooks
</div>

Cuando creas un agente con una URL de webhook, Cursor enviará solicitudes HTTP POST para notificarte sobre cambios de estado. Actualmente, solo se admiten eventos `statusChange`, específicamente cuando un agente entra en estado `ERROR` o `FINISHED`.

<div id="webhook-verification">
  ## Verificación de webhooks
</div>

Para asegurarte de que las solicitudes de webhook provienen auténticamente de Cursor, verificá la firma incluida con cada solicitud:

<div id="headers">
  ### Encabezados
</div>

Cada solicitud de webhook incluye los siguientes encabezados:

* **`X-Webhook-Signature`** – Contiene la firma HMAC-SHA256 con el formato `sha256=<hex_digest>`
* **`X-Webhook-ID`** – Un identificador único para esta entrega (útil para el logging)
* **`X-Webhook-Event`** – El tipo de evento (actualmente solo `statusChange`)
* **`User-Agent`** – Siempre establecido en `Cursor-Agent-Webhook/1.0`

<div id="signature-verification">
  ### Verificación de firma
</div>

Para verificar la firma del webhook, calculá la firma esperada y comparala con la firma recibida:

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
  const firmaEsperada = 'sha256=' +
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
    firma_esperada = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return signature == expected_signature
```

Usa siempre el cuerpo sin procesar de la solicitud (antes de cualquier parsing) al calcular la firma.

<div id="payload-format">
  ## Formato del payload
</div>

El payload del webhook se envía como JSON con la siguiente estructura:

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
  "summary": "Se agregó README.md con instrucciones de instalación"
}
```

Ten en cuenta que algunos campos son opcionales y solo se incluirán cuando estén disponibles.

<div id="best-practices">
  ## Mejores prácticas
</div>

* **Verifica las firmas** – Verifica siempre la firma del webhook para asegurarte de que la solicitud venga de Cursor
* **Maneja los reintentos** – Los webhooks pueden reintentarse si tu endpoint devuelve un código de estado de error
* **Responde rápido** – Devuelve un código de estado 2xx lo antes posible
* **Usa HTTPS** – Usa siempre URLs HTTPS para los endpoints de webhooks en producción
* **Almacena el payload sin procesar** – Guarda el payload del webhook sin procesar para depuración y verificación futuras

---

← Previous: [Descripción general](./descripcin-general.md) | [Index](./index.md) | Next: [Web y móvil](./web-y-mvil.md) →