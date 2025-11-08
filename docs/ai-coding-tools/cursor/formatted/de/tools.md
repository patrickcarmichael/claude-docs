---
title: "Tools"
source: "https://docs.cursor.com/de/agent/tools"
language: "de"
language_name: "German"
---

# Tools
Source: https://docs.cursor.com/de/agent/tools

Tools, die Agenten zum Suchen, Bearbeiten und Ausführen von Code zur Verfügung stehen

Eine Liste aller Tools, die den Modi innerhalb des [Agent](/de/agent/overview) zur Verfügung stehen und die du beim Erstellen deiner eigenen [Custom Modes](/de/agent/modes#custom) aktivieren oder deaktivieren kannst.

<Note>
  Es gibt kein Limit für die Anzahl der Tool-Aufrufe, die Agent während einer Aufgabe durchführen kann. Agent verwendet die Tools nach Bedarf weiter, bis deine Anfrage erfüllt ist.
</Note>

<div id="search">
  ## Suche
</div>

Tools, mit denen du deine Codebase und das Web durchsuchen kannst, um relevante Informationen zu finden.

<AccordionGroup>
  <Accordion title="Datei lesen" icon="file-lines">
    Liest bis zu 250 Zeilen (750 im Max-Modus) einer Datei.
  </Accordion>

  <Accordion title="Verzeichnis auflisten" icon="folder-open">
    Liest die Struktur eines Verzeichnisses, ohne Dateiinhalte zu öffnen.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    Führe semantische Suchen in deiner [indizierten
    Codebase](/de/context/codebase-indexing) durch.
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Suche nach exakten Schlüsselwörtern oder Mustern in Dateien.
  </Accordion>

  <Accordion title="Dateien suchen" icon="file-magnifying-glass">
    Finde Dateien anhand des Namens mit Fuzzy-Matching.
  </Accordion>

  <Accordion title="Web" icon="globe">
    Generiere Suchanfragen und führe Websuchen durch.
  </Accordion>

  <Accordion title="Regeln abrufen" icon="gavel">
    Rufe bestimmte [Regeln](/de/context/rules) basierend auf Typ und Beschreibung ab.
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## Edit
</div>

Tools, mit denen du gezielt Änderungen an deinen Dateien und in deinem Codebase vornimmst.

<AccordionGroup>
  <Accordion title="Edit & Reapply" icon="pencil">
    Schlage Änderungen an Dateien vor und [wende](/de/agent/apply) sie automatisch an.
  </Accordion>

  <Accordion title="Datei löschen" icon="trash">
    Lösche Dateien autonom (kann in den Einstellungen deaktiviert werden).
  </Accordion>
</AccordionGroup>

<div id="run">
  ## Ausführen
</div>

Chat kann mit deinem Terminal interagieren.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Terminalbefehle ausführen und Ausgaben überwachen.
  </Accordion>
</AccordionGroup>

<Note>Standardmäßig verwendet Cursor das erste verfügbare Terminalprofil.</Note>

So legst du dein bevorzugtes Terminalprofil fest:

1. Öffne die Befehlspalette (`Cmd/Ctrl+Shift+P`)
2. Suche nach „Terminal: Select Default Profile“
3. Wähle das gewünschte Profil aus

<div id="mcp">
  ## MCP
</div>

Chat kann konfigurierte MCP-Server nutzen, um mit externen Diensten wie Datenbanken oder Drittanbieter-APIs zu interagieren.

<AccordionGroup>
  <Accordion title="MCP-Server umschalten" icon="server">
    Verfügbare MCP-Server umschalten. Berücksichtigt die Auto-Run-Konfiguration.
  </Accordion>
</AccordionGroup>

Erfahre mehr über das [Model Context Protocol](/de/context/model-context-protocol) und entdecke verfügbare Server im [MCP-Verzeichnis](/de/tools).

<div id="advanced-options">
  ## Erweiterte Optionen
</div>

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    Änderungen automatisch anwenden, ohne manuelle Bestätigung.
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    Terminalbefehle automatisch ausführen und Änderungen übernehmen. Nützlich, um Test-Suites laufen zu lassen und Änderungen zu verifizieren.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    Allow-Lists konfigurieren, um festzulegen, welche Tools automatisch ausgeführt werden dürfen. Allow-Lists erhöhen die Sicherheit, indem zulässige Operationen explizit definiert werden.
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    Linter-Fehler und -Warnungen automatisch beheben, wenn der Agent darauf stößt.
  </Accordion>
</AccordionGroup>

---

← Previous: [Terminal](./terminal.md) | [Index](./index.md) | Next: [Hintergrund-Agents](./hintergrund-agents.md) →