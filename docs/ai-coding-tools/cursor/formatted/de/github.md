---
title: "GitHub"
source: "https://docs.cursor.com/de/integrations/github"
language: "de"
language_name: "German"
---

# GitHub
Source: https://docs.cursor.com/de/integrations/github

Offizielle Cursor-GitHub-App für Background Agents

[Background Agents](/de/background-agent) und [Bugbot](/de/bugbot) benötigen die Cursor-GitHub-App, um Repositories zu klonen und Änderungen zu pushen.

<div id="installation">
  ## Installation
</div>

1. Geh zu [Integrations im Dashboard](https://cursor.com/dashboard?tab=integrations)
2. Klick auf **Connect** neben GitHub
3. Wähl das Repository: entweder **All repositories** oder **Selected repositories**

Um dein GitHub-Konto zu trennen, geh zurück zum Integrations-Dashboard und klick auf **Disconnect Account**.

<div id="using-agent-in-github">
  ## Agent in GitHub verwenden
</div>

Die GitHub-Integration ermöglicht Hintergrund-Workflows mit dem Agent direkt aus Pull Requests und Issues. Du kannst einen Agent starten, der Kontext liest, Fixes umsetzt und Commits pusht, indem du `@cursor [prompt]` in einem beliebigen PR oder Issue kommentierst.

Wenn du [Bugbot](/de/bugbot) aktiviert hast, kannst du `@cursor fix` kommentieren, damit der Agent den von Bugbot vorgeschlagenen Fix übernimmt und das Problem im Hintergrund angeht.

<div id="permissions">
  ## Berechtigungen
</div>

Die GitHub-App benötigt bestimmte Berechtigungen, um mit Hintergrundagenten zu arbeiten:

<div className="full-width-table">
  | Berechtigung              | Zweck                                                          |
  | ------------------------- | -------------------------------------------------------------- |
  | **Repository-Zugriff**    | Deinen Code klonen und Arbeitsbranches erstellen               |
  | **Pull Requests**         | PRs mit Änderungen der Agenten zu deiner Überprüfung erstellen |
  | **Issues**                | Bugs und Tasks verfolgen, die Agenten entdecken oder beheben   |
  | **Checks und Status**     | Über Codequalität und Testergebnisse berichten                 |
  | **Actions und Workflows** | CI/CD-Pipelines und Deployments überwachen                     |
</div>

Alle Berechtigungen folgen dem Prinzip der geringsten erforderlichen Rechte, die für die Funktionalität von Hintergrundagenten nötig sind.

<div id="ip-allow-list-configuration">
  ## Konfiguration der IP-Allowlist
</div>

Wenn deine Organisation die IP-Allowlist-Funktion von GitHub nutzt, um den Zugriff auf deine Repositories zu beschränken, musst du zuerst den Support kontaktieren, damit die Allowlist-Funktion für dein Team aktiviert wird.

<div id="contact-support">
  ### Support kontaktieren
</div>

Bevor du IP-Allowlists konfigurierst, schreib an [hi@cursor.com](mailto:hi@cursor.com), damit dieses Feature für dein Team aktiviert wird. Das ist für beide Konfigurationsmethoden unten erforderlich.

<div id="enable-ip-allow-list-configuration-for-installed-github-apps-recommended">
  ### IP-Allowlist-Konfiguration für installierte GitHub-Apps aktivieren (empfohlen)
</div>

Die Cursor-GitHub-App hat die IP-Liste bereits vorkonfiguriert. Du kannst die Allowlist für installierte Apps aktivieren, damit sie diese Liste automatisch übernehmen. Das ist der **empfohlene Ansatz**, weil wir die Liste aktualisieren können und deine Organisation Updates automatisch erhält.

So aktivierst du das:

1. Geh zu den Sicherheitseinstellungen deiner Organisation
2. Navigiere zu den Einstellungen der IP-Allowlist
3. Aktiviere „Allow access by GitHub Apps“

Ausführliche Anweisungen findest du in [GitHubs Dokumentation](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps).

<div id="add-ips-directly-to-your-allowlist">
  ### IPs direkt zu deiner Allowlist hinzufügen
</div>

Wenn deine Organisation IdP-definierte Allowlists in GitHub verwendet oder die vorkonfigurierte Allowlist nicht nutzen kann, kannst du die IP-Adressen manuell hinzufügen:

```
184.73.225.134
3.209.66.12
52.44.113.131
```

<Note>
  Die Liste der IP-Adressen kann sich gelegentlich ändern. Teams, die IP-Allowlists verwenden, werden im Voraus benachrichtigt, bevor IP-Adressen hinzugefügt oder entfernt werden.
</Note>

<div id="troubleshooting">
  ## Fehlerbehebung
</div>

<AccordionGroup>
  <Accordion title="Agent kann nicht auf das Repository zugreifen">
    * Installier die GitHub-App mit Repository-Zugriff
    * Check die Repository-Berechtigungen für private Repos
    * Prüf die Berechtigungen deines GitHub-Kontos
  </Accordion>

  <Accordion title="Zugriff auf Pull Requests verweigert">
    * Gewähr der App Schreibzugriff auf Pull Requests
    * Prüf die Branch-Schutzregeln
    * Installier neu, wenn die App-Installation abgelaufen ist
  </Accordion>

  <Accordion title="App in den GitHub-Einstellungen nicht sichtbar">
    * Prüf, ob sie auf Organisationsebene installiert ist
    * Installier neu über [github.com/apps/cursor](https://github.com/apps/cursor)
    * Kontaktiere den Support, wenn die Installation beschädigt ist
  </Accordion>
</AccordionGroup>

---

← Previous: [Git](./git.md) | [Index](./index.md) | Next: [Linear](./linear.md) →