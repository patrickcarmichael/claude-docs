---
title: "Codebase-Indexierung"
source: "https://docs.cursor.com/de/context/codebase-indexing"
language: "de"
language_name: "German"
---

# Codebase-Indexierung
Source: https://docs.cursor.com/de/context/codebase-indexing

Wie Cursor deine Codebase indexiert, um sie besser zu verstehen

Cursor indexiert deine Codebase, indem es für jede Datei Embeddings berechnet. Das verbessert KI-generierte Antworten zu deinem Code. Wenn du ein Projekt öffnest, startet Cursor automatisch mit der Indexierung. Neue Dateien werden fortlaufend indexiert.
Check den Indexierungsstatus unter: `Cursor Settings` > `Indexing & Docs`

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="Fortschrittsanzeige der Codebase-Indexierung" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
</Frame>

<div id="configuration">
  ## Konfiguration
</div>

Cursor indexiert alle Dateien außer denen in [Ignore-Dateien](/de/context/ignore-files) (z. B. `.gitignore`, `.cursorignore`).

Klick auf `Show Settings`, um:

* automatisches Indexieren für neue Repositories zu aktivieren
* festzulegen, welche Dateien ignoriert werden

<Tip>
  [Große Inhaltsdateien zu ignorieren](/de/context/ignore-files) verbessert die Antwortgenauigkeit.
</Tip>

<div id="view-indexed-files">
  ### Indizierte Dateien anzeigen
</div>

So siehst du indizierte Dateipfade: `Cursor Settings` > `Indexing & Docs` > `View included files`

Dadurch wird eine `.txt`-Datei geöffnet, in der alle indizierten Dateien aufgelistet sind.

<div id="multi-root-workspaces">
  ## Multi-Root-Workspaces
</div>

Cursor unterstützt [Multi-Root-Workspaces](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces), sodass du mit mehreren Codebases arbeiten kannst:

* Alle Codebases werden automatisch indexiert
* Der Kontext jeder Codebase steht der KI zur Verfügung
* `.cursor/rules` gelten in allen Ordnern

<div id="pr-search">
  ## PR-Suche
</div>

Die PR-Suche hilft dir, die Entwicklung deiner Codebase nachzuvollziehen, indem historische Änderungen durchsuchbar und per KI zugänglich werden.

<div id="how-it-works">
  ### So funktioniert’s
</div>

Cursor **indiziert automatisch alle gemergten PRs** aus der Repository-Historie. Zusammenfassungen erscheinen in semantischen Suchergebnissen, mit smarten Filtern zur Priorisierung aktueller Änderungen.

Agent kann **PRs, Commits, Issues oder Branches** per `@[PR number]`, `@[commit hash]` oder `@[branch name]` in den Kontext holen. Bezieht GitHub-Kommentare und Bugbot-Reviews ein, wenn verbunden.

**Plattformunterstützung** umfasst GitHub, GitHub Enterprise und Bitbucket. GitLab wird derzeit nicht unterstützt.

<Note>
  GitHub-Enterprise-User: Das Fetch-Tool greift aufgrund von
  VSCode-Auth-Einschränkungen auf git-Befehle zurück.
</Note>

<div id="using-pr-search">
  ### PR-Suche verwenden
</div>

Stell Fragen wie „Wie sind Services in anderen PRs implementiert?“ und Agent holt automatisch relevante PRs in den Kontext, um umfassende Antworten basierend auf der Historie deines Repos zu liefern.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Where can I see all indexed codebases?">
    Es gibt noch keine globale Liste. Schau dir jedes Projekt einzeln an, indem du es in
    Cursor öffnest und die Einstellungen für Codebase Indexing prüfst.
  </Accordion>

  <Accordion title="How do I delete all indexed codebases?">
    Lösch deinen Cursor-Account in den Einstellungen, um alle indizierten Codebases zu entfernen.
    Alternativ lösch einzelne Codebases in den Codebase-Indexing-
    Einstellungen des jeweiligen Projekts.
  </Accordion>

  <Accordion title="How long are indexed codebases retained?">
    Indizierte Codebases werden nach 6 Wochen Inaktivität gelöscht. Das erneute Öffnen des
    Projekts löst eine erneute Indizierung aus.
  </Accordion>

  <Accordion title="Is my source code stored on Cursor servers?">
    Nein. Cursor erstellt Embeddings, ohne Dateinamen oder Quellcode zu speichern. Dateinamen werden verschleiert und Code-Segmente werden verschlüsselt.

    Wenn der Agent die Codebase durchsucht, ruft Cursor die Embeddings vom Server ab und entschlüsselt die Segmente.
  </Accordion>
</AccordionGroup>

---

← Previous: [/command](./command.md) | [Index](./index.md) | Next: [Dateien ignorieren](./dateien-ignorieren.md) →