---
title: "SCIM"
source: "https://docs.cursor.com/de/account/teams/scim"
language: "de"
language_name: "German"
---

# SCIM
Source: https://docs.cursor.com/de/account/teams/scim

Richte SCIM-Provisioning für die automatisierte Verwaltung von Benutzer:innen und Gruppen ein

<div id="overview">
  ## Überblick
</div>

Die SCIM‑2.0‑Provisionierung verwaltet automatisch deine Teammitglieder und Verzeichnisgruppen über deinen Identity Provider. Verfügbar in Enterprise‑Plänen mit aktiviertem SSO.

<product_visual type="screenshot">
  SCIM‑Einstellungen‑Dashboard mit Konfiguration für Active Directory Management
</product_visual>

<div id="prerequisites">
  ## Voraussetzungen
</div>

* Cursor Enterprise-Plan
* SSO muss zuerst eingerichtet sein – **SCIM setzt eine aktive SSO-Verbindung voraus**
* Admin-Zugriff auf deinen Identity-Provider (Okta, Azure AD, etc.)
* Admin-Zugriff auf deine Cursor-Organisation

## So funktioniert's

<div id="user-provisioning">
  ### Benutzerbereitstellung
</div>

Nutzer werden automatisch zu Cursor hinzugefügt, wenn sie in deinem Identity-Provider der SCIM-Anwendung zugewiesen werden. Wenn die Zuweisung entfernt wird, werden sie gelöscht. Änderungen werden in Echtzeit synchronisiert.

<div id="directory-groups">
  ### Verzeichnisgruppen
</div>

Verzeichnisgruppen und deren Mitgliedschaften werden aus deinem Identity-Provider synchronisiert. Gruppen- und Nutzerverwaltung müssen über deinen Identity-Provider erfolgen – Cursor zeigt diese Informationen nur schreibgeschützt an.

<div id="spend-management">
  ### Ausgabenverwaltung
</div>

Lege unterschiedliche Ausgabenlimits pro Nutzer für jede Verzeichnisgruppe fest. Limits auf Verzeichnisgruppenebene haben Vorrang vor Team-Limits. Nutzer in mehreren Gruppen erhalten das jeweils höchste anwendbare Ausgabenlimit.

<div id="setup">
  ## Setup
</div>

<Steps>
  <Step title="Stell sicher, dass SSO konfiguriert ist">
    SCIM setzt voraus, dass SSO zuerst eingerichtet ist. Wenn du SSO noch nicht konfiguriert hast,
    folge der [SSO-Einrichtungsanleitung](/de/account/teams/sso), bevor du fortfährst.
  </Step>

  <Step title="Öffne die Active-Directory-Verwaltung">
    Navigiere zu
    [cursor.com/dashboard?tab=active-directory](https://www.cursor.com/dashboard?tab=active-directory)
    mit einem Admin-Account, oder geh in deine Dashboard-Einstellungen und wähle den
    Tab „Active Directory Management“.
  </Step>

  <Step title="Starte die SCIM-Einrichtung">
    Sobald SSO verifiziert ist, siehst du einen Link für die schrittweise SCIM-Einrichtung. Klick
    darauf, um den Konfigurationsassistenten zu starten.
  </Step>

  <Step title="Konfiguriere SCIM in deinem Identity-Provider">
    In deinem Identity-Provider: - Erstelle oder konfiguriere deine SCIM-App - Verwende
    den von Cursor bereitgestellten SCIM-Endpoint und das Token - Aktiviere User- und Gruppen-
    Provisioning (Push) - Teste die Verbindung
  </Step>

  <Step title="Ausgabenlimits konfigurieren (optional)">
    Zurück in der Active-Directory-Verwaltung von Cursor: - Sieh dir deine synchronisierten
    Verzeichnisgruppen an - Setze nutzerbezogene Ausgabenlimits für bestimmte Gruppen nach Bedarf -
    Prüfe, welche Limits für User in mehreren Gruppen gelten
  </Step>
</Steps>

<div id="identity-provider-setup">
  ### Identity-Provider-Setup
</div>

Für providerspezifische Setup-Anleitungen:

<Card title="Identity Provider Guides" icon="book" href="https://workos.com/docs/integrations">
  Setup-Anleitungen für Okta, Azure AD, Google Workspace und mehr.
</Card>

<div id="managing-users-and-groups">
  ## Benutzer und Gruppen verwalten
</div>

<Warning>
  Die gesamte Benutzer- und Gruppenverwaltung muss über deinen Identity-Provider erfolgen.
  Änderungen in deinem Identity-Provider werden automatisch mit Cursor synchronisiert,
  aber du kannst Benutzer oder Gruppen nicht direkt in Cursor ändern.
</Warning>

<div id="user-management">
  ### Benutzerverwaltung
</div>

* Füge Benutzer hinzu, indem du sie in deinem Identity-Provider deiner SCIM-Anwendung zuweist
* Entferne Benutzer, indem du die Zuweisung zur SCIM-Anwendung aufhebst
* Änderungen am Benutzerprofil (Name, E-Mail) werden automatisch aus deinem Identity-Provider übernommen

<div id="group-management">
  ### Gruppenverwaltung
</div>

* Verzeichnisgruppen werden automatisch aus deinem Identity-Provider synchronisiert
* Änderungen an der Gruppenmitgliedschaft werden in Echtzeit übernommen
* Nutze Gruppen, um Benutzer zu organisieren und unterschiedliche Ausgabenlimits festzulegen

<div id="spend-limits">
  ### Ausgabenlimits
</div>

* Lege unterschiedliche Pro-Benutzer-Limits für jede Verzeichnisgruppe fest
* Benutzer erben das höchste Ausgabenlimit aus ihren Gruppen
* Gruppenlimits überschreiben das standardmäßige, teamweite Pro-Benutzer-Limit

<div id="faq">
  ## FAQ
</div>

<div id="why-isnt-scim-management-showing-up-in-my-dashboard">
  ### Warum wird die SCIM-Verwaltung in meinem Dashboard nicht angezeigt?
</div>

Stell sicher, dass SSO korrekt konfiguriert ist und funktioniert, bevor du SCIM einrichtest. SCIM erfordert eine aktive SSO-Verbindung.

<div id="why-arent-users-syncing">
  ### Warum werden Nutzer nicht synchronisiert?
</div>

Überprüf, ob Nutzer in deinem Identity Provider der SCIM-App zugewiesen sind. Nutzer müssen explizit zugewiesen werden, um in Cursor zu erscheinen.

<div id="why-arent-groups-appearing">
  ### Warum werden Gruppen nicht angezeigt?
</div>

Prüf, ob die Bereitstellung für Gruppen-Push in den SCIM-Einstellungen deines Identity Providers aktiviert ist. Die Gruppensynchronisierung muss getrennt von der Nutzersynchronisierung konfiguriert werden.

<div id="why-arent-spend-limits-applying">
  ### Warum werden Ausgabenlimits nicht angewendet?
</div>

Stell sicher, dass Nutzer in deinem Identity Provider den erwarteten Gruppen korrekt zugeordnet sind. Die Gruppenmitgliedschaft bestimmt, welche Ausgabenlimits gelten.

<div id="can-i-manage-scim-users-and-groups-directly-in-cursor">
  ### Kann ich SCIM-Nutzer und -Gruppen direkt in Cursor verwalten?
</div>

Nein. Die gesamte Nutzer- und Gruppenverwaltung muss über deinen Identity Provider erfolgen. Cursor zeigt diese Informationen nur lesend an.

<div id="how-quickly-do-changes-sync">
  ### Wie schnell werden Änderungen synchronisiert?
</div>

Änderungen in deinem Identity Provider werden in Echtzeit mit Cursor synchronisiert. Bei großen Bulk-Operationen kann es zu einer kurzen Verzögerung kommen.

---

← Previous: [Mitglieder & Rollen](./mitglieder-rollen.md) | [Index](./index.md) | Next: [Leg los](./leg-los.md) →