---
title: "Agent-Sicherheit"
source: "https://docs.cursor.com/de/account/agent-security"
language: "de"
language_name: "German"
---

# Agent-Sicherheit
Source: https://docs.cursor.com/de/account/agent-security

Sicherheitsaspekte bei der Verwendung von Cursor Agent

Prompt-Injection, KI-Halluzinationen und andere Probleme können dazu führen, dass sich KI unerwartet und potenziell bösartig verhält. Während wir weiter daran arbeiten, Prompt-Injection auf einer grundlegenderen Ebene zu lösen, bestehen unsere wichtigsten Schutzmechanismen in Cursor-Produkten aus Leitplanken für das Handeln eines Agents – einschließlich der standardmäßigen Anforderung einer manuellen Bestätigung für sensible Aktionen. Ziel dieses Dokuments ist es, unsere Leitplanken zu erklären und was du von ihnen erwarten kannst.

Alle unten aufgeführten Steuerungen und Verhaltensweisen sind unsere Standard- und empfohlenen Einstellungen.

<div id="first-party-tool-calls">
  ## First-party-Toolaufrufe
</div>

Cursor wird mit Tools ausgeliefert, die dem Agent helfen, dir beim Coden zu helfen. Dazu gehören Dateilesen, Bearbeitungen, das Ausführen von Terminalbefehlen, die Suche im Web nach Doku und mehr.

Lese-Tools erfordern keine Freigabe (z. B. das Lesen von Dateien, die Suche im Code). Du kannst [.cursorignore](/de/context/ignore-files) verwenden, um dem Agent den Zugriff auf bestimmte Dateien komplett zu blockieren; ansonsten sind Lesevorgänge in der Regel ohne Freigabe erlaubt. Für Aktionen, die das Risiko der Exfiltration sensibler Daten bergen, verlangen wir eine explizite Freigabe.

Das Ändern von Dateien im aktuellen Workspace erfordert keine explizite Freigabe, mit einigen Ausnahmen. Wenn ein Agent Dateien ändert, werden die Änderungen sofort auf die Festplatte geschrieben. Wir empfehlen, Cursor in versionierten Workspaces zu nutzen, sodass Dateiinhalte jederzeit zurückgesetzt werden können. Wir verlangen eine explizite Freigabe, bevor Dateien geändert werden, die die Konfiguration unserer IDE/CLI anpassen, z. B. die Workspace-Einstellungsdatei des Editors. Wenn bei dir ein automatisches Neuladen bei Dateänderungen aktiv ist, beachte, dass Agent-Änderungen an Dateien eine automatische Ausführung auslösen können, bevor du sie prüfen konntest.

Jeder vom Agent vorgeschlagene Terminalbefehl erfordert standardmäßig eine Freigabe. Wir empfehlen, jeden Befehl zu prüfen, bevor der Agent ihn ausführt. Wenn du das Risiko akzeptierst, kannst du dem Agent erlauben, alle Befehle ohne Freigabe auszuführen. Wir bieten in Cursor eine [Allowlist](/de/agent/tools) an, betrachten sie jedoch nicht als Sicherheitskontrolle. Manche Nutzer erlauben bestimmte Befehle, aber das ist ein Best-Effort-System, und Umgehungen sind möglich. Wir empfehlen nicht „Run Everything“, da damit alle konfigurierten Allowlists umgangen werden.

<div id="third-party-tool-calls">
  ## Aufrufe von Drittanbieter-Tools
</div>

Cursor ermöglicht das Einbinden externer Tools über [MCP](/de/context/mcp). Alle MCP-Verbindungen von Drittanbietern müssen ausdrücklich von dir genehmigt werden. Sobald du eine MCP-Verbindung genehmigt hast, muss in Agent Mode standardmäßig jeder vorgeschlagene Tool-Aufruf für jede externe MCP-Integration vor der Ausführung ausdrücklich bestätigt werden.

<div id="network-requests">
  ## Netzwerk-Anfragen
</div>

Netzwerk-Anfragen können von Angreifern genutzt werden, um Daten zu exfiltrieren. Wir unterstützen derzeit keine First‑Party‑Tools, die Netzwerk-Anfragen an andere Hosts als eine sehr kleine, ausgewählte Gruppe (z. B. GitHub) stellen, keine expliziten Linkabrufe und nur Websuche mit einer ausgewählten Gruppe von Anbietern. Beliebige Agenten‑Netzwerk-Anfragen werden in den Standardeinstellungen verhindert.

<div id="workspace-trust">
  ## Workspace-Trust
</div>

Die Cursor-IDE unterstützt die standardmäßige [Workspace-Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust)-Funktion, die *deaktiviert* ist. Workspace-Trust zeigt dir beim Öffnen eines neuen Workspaces einen Dialog, in dem du zwischen normalem und eingeschränktem Modus wählen kannst. Der eingeschränkte Modus deaktiviert AI und andere Features, für die Nutzer Cursor typischerweise verwenden. Wir empfehlen dafür andere Tools, z. B. einen einfachen Texteditor, wenn du mit Repos arbeitest, denen du nicht vertraust.

Workspace-Trust kann in den Benutzereinstellungen aktiviert werden, indem du diese Schritte ausführst:

1. Öffne deine user settings.json-Datei
2. Füge die folgende Konfiguration hinzu:
   ```json  theme={null}
   "security.workspace.trust.enabled": true
   ```

Diese Einstellung kann auch organisationsweit über Mobile-Device-Management-(MDM)-Lösungen erzwungen werden.

<div id="responsible-disclosure">
  ## Verantwortungsvolle Offenlegung
</div>

Wenn du glaubst, eine Sicherheitslücke in Cursor gefunden zu haben, folge bitte der Anleitung auf unserer GitHub-Sicherheitsseite und reiche den Bericht dort ein. Wenn du GitHub nicht nutzen kannst, erreichst du uns auch unter [security@cursor.com](mailto:security@cursor.com).

Wir sagen zu, Meldungen über Sicherheitslücken innerhalb von 5 Werktagen zu bestätigen und sie so schnell wie möglich zu bearbeiten. Wir veröffentlichen die Ergebnisse als Sicherheitshinweise auf unserer GitHub-Sicherheitsseite. Kritische Vorfälle werden sowohl auf der GitHub-Sicherheitsseite als auch per E-Mail an alle Nutzer kommuniziert.

---

← Previous: [Index](./index.md) | [Index](./index.md) | Next: [Abrechnung](./abrechnung.md) →