---
title: "GitHub-Repositories auflisten"
source: "https://docs.cursor.com/de/background-agent/api/list-repositories"
language: "de"
language_name: "German"
---

# GitHub-Repositories auflisten
Source: https://docs.cursor.com/de/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Eine Liste von GitHub-Repositories abrufen, auf die der authentifizierte Nutzer Zugriff hat.

<Warning>
  **Dieser Endpoint hat sehr strenge Rate Limits.**

  Begrenze Anfragen auf **1/Nutzer/Minute** und **30/Nutzer/Stunde.**

  Bei Nutzern mit Zugriff auf viele Repositories kann die Antwort mehrere Dutzend Sekunden dauern.

  Stell sicher, dass du sauber damit umgehst, wenn diese Informationen nicht verfügbar sind.
</Warning>

---

← Previous: [Modelle auflisten](./modelle-auflisten.md) | [Index](./index.md) | Next: [Überblick](./berblick.md) →