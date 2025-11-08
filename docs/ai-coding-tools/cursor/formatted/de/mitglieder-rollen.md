---
title: "Mitglieder & Rollen"
source: "https://docs.cursor.com/de/account/teams/members"
language: "de"
language_name: "German"
---

# Mitglieder & Rollen
Source: https://docs.cursor.com/de/account/teams/members

Teammitglieder und Rollen verwalten

Cursor-Teams haben drei Rollen:

<div id="roles">
  ## Rollen
</div>

**Mitglieder** sind die Standardrolle mit Zugriff auf die Pro-Funktionen von Cursor.

* Voller Zugriff auf die Pro-Funktionen von Cursor
* Kein Zugriff auf Abrechnungseinstellungen oder das Admin-Dashboard
* Können die eigene Nutzung und das verbleibende nutzungsbasierte Budget sehen

**Admins** steuern die Teamverwaltung und Sicherheitseinstellungen.

* Voller Zugriff auf Pro-Funktionen
* Mitglieder hinzufügen/entfernen, Rollen ändern, SSO einrichten
* Nutzungsbasierte Preise und Ausgabelimits konfigurieren
* Zugriff auf Team-Analytics

**Unbezahlte Admins** verwalten Teams, ohne einen bezahlten Seat zu verwenden – ideal für IT- oder Finance-Mitarbeitende, die keinen Cursor-Zugriff brauchen.

* Nicht abrechenbar, keine Pro-Funktionen
* Gleiche administrativen Möglichkeiten wie Admins

<Info>Unbezahlte Admins erfordern mindestens einen bezahlten User im Team.</Info>

<div id="role-comparison">
  ## Rollenvergleich
</div>

<div className="full-width-table">
  | Funktionalität                        | Mitglied | Admin | Unbezahlter Admin |
  | ------------------------------------- | :------: | :---: | :---------------: |
  | Cursor‑Funktionen nutzen              |     ✓    |   ✓   |                   |
  | Mitglieder einladen                   |     ✓    |   ✓   |         ✓         |
  | Mitglieder entfernen                  |          |   ✓   |         ✓         |
  | Benutzerrollen ändern                 |          |   ✓   |         ✓         |
  | Admin‑Dashboard                       |          |   ✓   |         ✓         |
  | SSO/Sicherheit konfigurieren          |          |   ✓   |         ✓         |
  | Abrechnung verwalten                  |          |   ✓   |         ✓         |
  | Analysen einsehen                     |          |   ✓   |         ✓         |
  | Zugriffe verwalten                    |          |   ✓   |         ✓         |
  | Nutzungsgrenzen festlegen             |          |   ✓   |         ✓         |
  | Erfordert kostenpflichtigen Sitzplatz |     ✓    |   ✓   |                   |
</div>

<div id="managing-members">
  ## Mitglieder verwalten
</div>

Alle Teammitglieder können andere einladen. Einladungen werden aktuell nicht eingeschränkt.

<div id="add-member">
  ### Mitglied hinzufügen
</div>

Füge Mitglieder auf drei Arten hinzu:

1. **E-Mail-Einladung**

   * Klicke auf `Invite Members`
   * Gib E-Mail-Adressen ein
   * Nutzer erhalten E-Mail-Einladungen

2. **Einladungslink**

   * Klicke auf `Invite Members`
   * Kopiere `Invite Link`
   * Teile ihn mit Teammitgliedern

3. **SSO**
   * Konfiguriere SSO im [Admin-Dashboard](/de/account/teams/sso)
   * Nutzer treten automatisch bei, wenn sie sich mit ihrer SSO-E-Mail anmelden

<Warning>
  Einladungslinks haben eine lange Gültigkeitsdauer – jeder mit dem Link kann beitreten.
  Widerrufe sie oder nutze [SSO](/de/account/teams/sso)
</Warning>

<div id="remove-member">
  ### Mitglied entfernen
</div>

Admins können Mitglieder jederzeit über das Kontextmenü → „Remove“ entfernen. Wenn ein Mitglied bereits Credits genutzt hat, bleibt sein Platz bis zum Ende des Abrechnungszeitraums belegt.

<div id="change-role">
  ### Rolle ändern
</div>

Admins können Rollen für andere Mitglieder ändern, indem sie das Kontextmenü öffnen und anschließend die Option „Change role“ verwenden.<br />

Es muss jederzeit mindestens ein Admin und ein zahlendes Mitglied im Team sein.

## Sicherheit & SSO

SAML 2.0 Single Sign-On (SSO) ist in Team-Plänen verfügbar. Zu den wichtigsten Funktionen gehören:

* SSO-Verbindungen konfigurieren ([mehr erfahren](/de/account/teams/sso))
* Domainverifizierung einrichten
* Automatische Benutzerbereitstellung
* Optionen zur Erzwingung von SSO
* Integration von Identitätsanbietern (Okta usw.)

<Note>
  <p className="!mb-0">Für die Aktivierung von SSO ist eine Domainverifizierung erforderlich.</p>
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: `32px 64px`, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="usage-controls">
  ## Nutzungssteuerung
</div>

Greif auf die Nutzungseinstellungen zu, um:

* nutzungsbasierte Abrechnung zu aktivieren
* Premium-Modelle zu aktivieren
* Änderungen nur für Admins zuzulassen
* monatliche Ausgabenlimits festzulegen
* die teamweite Nutzung zu überwachen

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8149f830c27308af1bcc329c25e38b5" style={{ backgroundColor: "#0c0c0c" }} data-og-width="1668" width="1668" data-og-height="1160" height="1160" data-path="images/account/usage-based-pricing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc308a967251694ad7b03189c1083c61 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ddc293e19fa993e65be8c09ced649b4f 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a4df7d48d75c6166ab215550a641ca6 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f9051947c802ae54fd964196c50a3701 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ed775e3e98611ead1b938aedaf917f11 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b26f86bce94dc981d3cf71853a965374 2500w" />
</Frame>

<div id="billing">
  ## Abrechnung
</div>

Wenn du Teammitglieder hinzufügst:

* Jedes Mitglied oder jeder Admin belegt einen kostenpflichtigen Sitzplatz (siehe [Preise](https://cursor.com/pricing))
* Neue Mitglieder werden anteilig für die verbleibende Zeit im Abrechnungszeitraum berechnet
* Unbezahlte Admin-Sitzplätze werden nicht mitgezählt

Bei Ergänzungen mitten im Monat zahlst du nur für die genutzten Tage. Wenn du Mitglieder entfernst, die Credits genutzt haben, bleibt ihr Sitzplatz bis zum Ende des Abrechnungszyklus belegt – anteilige Rückerstattungen gibt es nicht.

Rollenänderungen (z. B. Admin zu Unpaid Admin) wirken sich ab dem Änderungsdatum auf die Abrechnung aus. Wähle monatliche oder jährliche Abrechnung.

Die monatliche/jährliche Verlängerung erfolgt an deinem ursprünglichen Anmeldedatum – unabhängig von Änderungen bei den Mitgliedern.

<div id="switch-to-yearly-billing">
  ### Zur jährlichen Abrechnung wechseln
</div>

Spare **20 %**, indem du von monatlich auf jährlich wechselst:

1. Geh zum [Dashboard](https://cursor.com/dashboard)
2. Klick im Kontobereich auf „Advanced“ und dann auf „Upgrade to yearly billing“

<Note>
  Du kannst nur über das Dashboard von monatlich auf jährlich wechseln. Um von
  jährlich auf monatlich zu wechseln, schreib an [hi@cursor.com](mailto:hi@cursor.com).
</Note>

---

← Previous: [Enterprise-Einstellungen](./enterprise-einstellungen.md) | [Index](./index.md) | Next: [SCIM](./scim.md) →