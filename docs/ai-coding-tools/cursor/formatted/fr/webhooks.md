---
title: "Webhooks"
source: "https://docs.cursor.com/fr/background-agent/api/webhooks"
language: "fr"
language_name: "French"
---

# Webhooks
Source: https://docs.cursor.com/fr/background-agent/api/webhooks

Recevoir des notifications en temps réel sur les changements d’état de l’agent en arrière-plan

<div id="webhooks">
  # Webhooks
</div>

Quand tu crées un agent avec une URL de webhook, Cursor envoie des requêtes HTTP POST pour te notifier des changements d’état. Pour l’instant, seuls les événements `statusChange` sont pris en charge, notamment quand un agent passe en état `ERROR` ou `FINISHED`.

<div id="webhook-verification">
  ## Vérification du webhook
</div>

Pour t’assurer que les requêtes de webhook proviennent bien de Cursor, vérifie la signature incluse avec chaque requête :

<div id="headers">
  ### En-têtes
</div>

Chaque requête de webhook inclut les en-têtes suivants :

* **`X-Webhook-Signature`** – Contient la signature HMAC-SHA256 au format `sha256=<hex_digest>`
* **`X-Webhook-ID`** – Un identifiant unique pour cette livraison (utile pour les logs)
* **`X-Webhook-Event`** – Le type d’événement (actuellement uniquement `statusChange`)
* **`User-Agent`** – Toujours défini sur `Cursor-Agent-Webhook/1.0`

<div id="signature-verification">
  ### Vérification de la signature
</div>

Pour vérifier la signature du webhook, calcule la signature attendue et compare-la à la signature reçue :

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
    signature_attendue = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return signature == expected_signature
```

Utilise toujours le corps brut de la requête (avant toute analyse) pour calculer la signature.

<div id="payload-format">
  ## Format de la charge utile
</div>

La charge utile du webhook est envoyée au format JSON avec la structure suivante :

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
  "summary": "Ajout de README.md avec des instructions d’installation"
}
```

Note que certains champs sont facultatifs et ne seront inclus que s’ils sont disponibles.

<div id="best-practices">
  ## Bonnes pratiques
</div>

* **Vérifie les signatures** – Vérifie toujours la signature du webhook pour t’assurer que la requête vient de Cursor
* **Gère les retentatives** – Les webhooks peuvent être renvoyés si ton endpoint renvoie un code d’erreur
* **Réponds rapidement** – Renvoie un code de statut 2xx dès que possible
* **Utilise HTTPS** – Utilise toujours des URL HTTPS pour les endpoints de webhook en production
* **Stocke les payloads bruts** – Stocke le payload brut du webhook pour le débogage et de futures vérifications

---

← Previous: [Aperçu](./aperu.md) | [Index](./index.md) | Next: [Web & Mobile](./web-mobile.md) →