---
title: "SSO"
source: "https://docs.cursor.com/de/account/teams/sso"
language: "de"
language_name: "German"
---

# SSO
Source: https://docs.cursor.com/de/account/teams/sso

Richte Single Sign-on für dein Team ein

<div id="overview">
  ## Überblick
</div>

SAML 2.0 SSO ist ohne zusätzliche Kosten in Business-Plänen verfügbar. Verwende deinen bestehenden Identity-Provider (IdP), um Teammitglieder zu authentifizieren, ohne separate Cursor-Konten zu benötigen.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## Voraussetzungen
</div>

* Cursor Team-Plan
* Admin-Zugriff auf deinen Identity-Provider (z. B. Okta)
* Admin-Zugriff auf deine Cursor-Organisation

<div id="configuration-steps">
  ## Konfigurationsschritte
</div>

<Steps>
  <Step title="Melde dich bei deinem Cursor-Konto an">
    Navigiere mit einem Admin-Konto zu [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings).
  </Step>

  <Step title="SSO-Konfiguration finden">
    Suche den Abschnitt „Single Sign-On (SSO)“ und klappe ihn aus.
  </Step>

  <Step title="Einrichtung starten">
    Klicke auf die Schaltfläche „SSO Provider Connection settings“, um die SSO-Einrichtung zu starten, und folge dem Assistenten.
  </Step>

  <Step title="Identity Provider konfigurieren">
    In deinem Identity Provider (z. B. Okta):

    * Neue SAML-Anwendung erstellen
    * SAML-Einstellungen mit den Informationen von Cursor konfigurieren
    * Just-in-Time-(JIT)-Bereitstellung einrichten
  </Step>

  <Step title="Domain verifizieren">
    Verifiziere die Domain deiner Nutzer in Cursor, indem du auf die Schaltfläche „Domain verification settings“ klickst.
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### Anleitungen zur Einrichtung von Identity Providern
</div>

Für anbieterbezogene Einrichtungsanleitungen:

<Card title="Identity Provider Guides" icon="book" href="https://workos.com/docs/integrations">
  Einrichtungsanleitungen für Okta, Azure AD, Google Workspace und mehr.
</Card>

<div id="additional-settings">
  ## Zusätzliche Einstellungen
</div>

* SSO-Erzwingung im Admin-Dashboard verwalten
* Neue Nutzer werden bei der Anmeldung über SSO automatisch aufgenommen
* Nutzerverwaltung über deinen Identity Provider steuern

<div id="troubleshooting">
  ## Fehlerbehebung
</div>

Wenn Probleme auftreten:

* Prüf, ob die Domain in Cursor verifiziert ist
* Stell sicher, dass SAML-Attribute korrekt zugeordnet sind
* Prüf, ob SSO im Admin-Dashboard aktiviert ist
* Gleiche Vor- und Nachnamen zwischen Identity Provider und Cursor ab
* Schau dir die anbieter­spezifischen Anleitungen oben an
* Schreib an [hi@cursor.com](mailto:hi@cursor.com), wenn die Probleme weiter bestehen

---

← Previous: [Leg los](./leg-los.md) | [Index](./index.md) | Next: [Update-Zugriff](./update-zugriff.md) →