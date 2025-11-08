---
title: "API-Schlüssel"
source: "https://docs.cursor.com/de/settings/api-keys"
language: "de"
language_name: "German"
---

# API-Schlüssel
Source: https://docs.cursor.com/de/settings/api-keys

Verwende deinen eigenen LLM-Anbieter

Verwende deine eigenen API-Schlüssel, um unbegrenzt AI-Nachrichten auf eigene Kosten zu senden. Wenn eingerichtet, nutzt Cursor deine API-Schlüssel, um LLM-Anbieter direkt aufzurufen.

Um deinen API-Schlüssel zu verwenden, geh zu `Cursor Settings` > `Models` und gib deine API-Schlüssel ein. Klick auf **Verify**. Nach erfolgreicher Prüfung ist dein API-Schlüssel aktiviert.

<Warning>
  Eigene API-Schlüssel funktionieren nur mit Standard-Chatmodellen. Features, die spezialisierte Modelle erfordern (z. B. Tab Completion), verwenden weiterhin die integrierten Modelle von Cursor.
</Warning>

<div id="supported-providers">
  ## Unterstützte Anbieter
</div>

* **OpenAI** - Nur Standard-Chatmodelle ohne Reasoning. Der Model-Picker zeigt die verfügbaren OpenAI-Modelle an.
* **Anthropic** - Alle Claude-Modelle, die über die Anthropic-API verfügbar sind.
* **Google** - Gemini-Modelle, die über die Google AI API verfügbar sind.
* **Azure OpenAI** - In deiner Azure OpenAI Service-Instanz bereitgestellte Modelle.
* **AWS Bedrock** - Verwende AWS Access Keys, Secret Keys oder IAM-Rollen. Funktioniert mit Modellen, die in deiner Bedrock-Konfiguration verfügbar sind.

Nach der Validierung deiner Bedrock-IAM-Rolle wird eine eindeutige externe ID generiert, die du für zusätzliche Sicherheit der Trust-Policy deiner IAM-Rolle hinzufügen kannst.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Wird mein API-Schlüssel gespeichert oder verlässt er mein Gerät?">
    Dein API-Schlüssel wird nicht gespeichert, aber bei jeder Anfrage an unseren Server gesendet. Alle Anfragen laufen über unser Backend, wo der endgültige Prompt zusammengestellt wird.
  </Accordion>
</AccordionGroup>

---

← Previous: [Modelle](./modelle.md) | [Index](./index.md) | Next: [Tab](./tab.md) →