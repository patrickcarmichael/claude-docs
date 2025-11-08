---
title: "Commands"
source: "https://docs.cursor.com/de/agent/chat/commands"
language: "de"
language_name: "German"
---

# Commands
Source: https://docs.cursor.com/de/agent/chat/commands

Definiere Befehle für wiederverwendbare Workflows

Benutzerdefinierte Commands ermöglichen dir, wiederverwendbare Workflows zu erstellen, die mit einem einfachen `/`-Prefix im Chat-Eingabefeld ausgelöst werden können. Diese Commands helfen, Prozesse in deinem Team zu standardisieren und machen häufige Aufgaben effizienter.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  Commands befinden sich derzeit in der Beta. Die Funktion und die Syntax können sich ändern, während wir sie weiter verbessern.
</Info>

<div id="how-commands-work">
  ## Wie Befehle funktionieren
</div>

Befehle sind als einfache Markdown-Dateien definiert und können an zwei Orten gespeichert werden:

1. **Projektbefehle**: Gespeichert im Verzeichnis `.cursor/commands` deines Projekts
2. **Globale Befehle**: Gespeichert im Verzeichnis `~/.cursor/commands` in deinem Home-Verzeichnis

Wenn du im Chat-Eingabefeld `/` tippst, erkennt Cursor automatisch verfügbare Befehle aus beiden Verzeichnissen und zeigt sie an – so sind sie in deinem Workflow sofort verfügbar.

<div id="creating-commands">
  ## Befehle erstellen
</div>

1. Lege im Projekt-Root ein Verzeichnis `.cursor/commands` an
2. Füge `.md`-Dateien mit aussagekräftigen Namen hinzu (z. B. `review-code.md`, `write-tests.md`)
3. Schreib einfachen Markdown-Text, der beschreibt, was der Befehl tun soll
4. Befehle erscheinen automatisch im Chat, wenn du `/` eingibst

So könnte die Struktur deines `commands`-Verzeichnisses aussehen:

```
.cursor/
└── commands/
    ├── github-pr-kommentare-beantworten.md
    ├── code-review-checkliste.md
    ├── pr-erstellen.md
    ├── bestehende-diffs-kurz-prüfen.md
    ├── neuen-entwickler-onboarden.md
    ├── alle-tests-ausführen-und-fixen.md
    ├── sicherheitsaudit.md
    └── neue-funktion-einrichten.md
```

<div id="examples">
  ## Beispiele
</div>

Probier diese Befehle in deinen Projekten aus, um ein Gefühl dafür zu bekommen, wie sie funktionieren.

<AccordionGroup>
  <Accordion title="Code-Review-Checkliste">
    ```markdown  theme={null}
    # Code-Review-Checkliste

    ## Überblick
    Umfassende Checkliste für gründliche Code-Reviews, um Qualität, Sicherheit und Wartbarkeit sicherzustellen.

    ## Review-Kategorien

    ### Funktionalität
    - [ ] Code macht, was er soll
    - [ ] Edge Cases werden abgedeckt
    - [ ] Fehlerbehandlung ist angemessen
    - [ ] Keine offensichtlichen Bugs oder Logikfehler

    ### Codequalität
    - [ ] Code ist gut lesbar und strukturiert
    - [ ] Funktionen sind klein und fokussiert
    - [ ] Variablennamen sind aussagekräftig
    - [ ] Kein doppelter Code
    - [ ] Hält Projektkonventionen ein

    ### Sicherheit
    - [ ] Keine offensichtlichen Sicherheitslücken
    - [ ] Eingabevalidierung vorhanden
    - [ ] Sensible Daten werden korrekt gehandhabt
    - [ ] Keine hardcodierten Secrets
    ```
  </Accordion>

  <Accordion title="Sicherheitsaudit">
    ```markdown  theme={null}
    # Security Audit

    ## Überblick
    Umfassende Sicherheitsüberprüfung zur Identifizierung und Behebung von Schwachstellen im Codebase.

    ## Schritte
    1. **Dependency-Audit**
       - Auf bekannte Schwachstellen prüfen
       - Veraltete Pakete aktualisieren
       - Third-Party-Dependencies überprüfen

    2. **Code Security Review**
       - Auf gängige Schwachstellen prüfen
       - Authentifizierung/Autorisierung überprüfen
       - Datenverarbeitungspraktiken prüfen

    3. **Infrastructure Security**
       - Umgebungsvariablen überprüfen
       - Zugriffssteuerungen prüfen
       - Netzwerksicherheit prüfen

    ## Security Checklist
    - [ ] Dependencies aktualisiert und sicher
    - [ ] Keine hardcodierten Secrets
    - [ ] Eingabevalidierung implementiert
    - [ ] Authentifizierung sicher
    - [ ] Autorisierung korrekt konfiguriert
    ```
  </Accordion>

  <Accordion title="Neue Funktion einrichten">
    ```markdown  theme={null}
    # Neue Funktion einrichten

    ## Überblick
    Eine neue Funktion systematisch vom initialen Plan bis zur Implementierungsstruktur aufsetzen.

    ## Schritte
    1. **Anforderungen definieren**
       - Funktionsumfang und Ziele klären
       - User Stories und Akzeptanzkriterien festlegen
       - Technischen Ansatz planen

    2. **Feature-Branch erstellen**
       - Von main/develop abzweigen
       - Lokale Entwicklungsumgebung aufsetzen
       - Neue Abhängigkeiten konfigurieren

    3. **Architektur planen**
       - Datenmodelle und APIs entwerfen
       - UI-Komponenten und Flows planen
       - Teststrategie definieren

    ## Checkliste für das Feature-Setup
    - [ ] Anforderungen dokumentiert
    - [ ] User Stories geschrieben
    - [ ] Technischer Ansatz geplant
    - [ ] Feature-Branch erstellt
    - [ ] Entwicklungsumgebung bereit
    ```
  </Accordion>

  <Accordion title="Pull Request erstellen">
    ```markdown  theme={null}
    # PR erstellen

    ## Überblick
    Erstelle einen gut strukturierten Pull Request mit klarer Beschreibung, passenden Labels und Reviewern.

    ## Schritte
    1. **Branch vorbereiten**
       - Sicherstellen, dass alle Änderungen committed sind
       - Branch zum Remote pushen
       - Prüfen, dass der Branch mit main auf dem neuesten Stand ist

    2. **PR-Beschreibung schreiben**
       - Änderungen klar zusammenfassen
       - Kontext und Motivation angeben
       - Breaking Changes auflisten
       - Screenshots hinzufügen, wenn es UI-Änderungen gibt

    3. **PR einrichten**
       - PR mit aussagekräftigem Titel erstellen
       - Passende Labels hinzufügen
       - Reviewer zuweisen
       - Zugehörige Issues verlinken

    ## PR-Vorlage
    - [ ] Feature A
    - [ ] Bugfix B
    - [ ] Unit-Tests bestehen
    - [ ] Manuelles Testen abgeschlossen
    ```
  </Accordion>

  <Accordion title="Tests ausführen und Fehler beheben">
    ```markdown  theme={null}
    # Alle Tests ausführen und Fehler beheben

    ## Übersicht
    Führe die vollständige Testsuite aus und behebe systematisch alle Fehlerschläge, um Codequalität und Funktionalität sicherzustellen.

    ## Schritte
    1. **Testsuite ausführen**
       - Alle Tests im Projekt ausführen
       - Ausgabe erfassen und fehlgeschlagene Tests identifizieren
       - Sowohl Unit- als auch Integrationstests prüfen

    2. **Fehler analysieren**
       - Nach Typ kategorisieren: flaky, defekt, neu
       - Fixes nach Impact priorisieren
       - Prüfen, ob Fehler mit jüngsten Änderungen zusammenhängen

    3. **Probleme systematisch beheben**
       - Mit den kritischsten Fehlern beginnen
       - Ein Problem nach dem anderen beheben
       - Tests nach jedem Fix erneut ausführen
    ```
  </Accordion>

  <Accordion title="Neuen Entwickler onboarden">
    ```markdown  theme={null}
    # Neue·n Developer onboarden

    ## Übersicht
    Umfassender Onboarding‑Prozess, um einen neuen Developer schnell startklar zu machen.

    ## Schritte
    1. **Environment‑Setup**
       - Erforderliche Tools installieren
       - Entwicklungsumgebung einrichten
       - IDE und Extensions konfigurieren
       - Git und SSH‑Keys einrichten

    2. **Projekteinstieg**
       - Projektstruktur durchgehen
       - Architektur verstehen
       - Wichtige Doku lesen
       - Lokale Datenbank einrichten

    ## Onboarding‑Checkliste
    - [ ] Entwicklungsumgebung bereit
    - [ ] Alle Tests grün
    - [ ] Anwendung lokal startbar
    - [ ] Datenbank eingerichtet und funktionsfähig
    - [ ] Erste·r PR erstellt
    ```
  </Accordion>
</AccordionGroup>

---

← Previous: [Checkpoints](./checkpoints.md) | [Index](./index.md) | Next: [Kompakt](./kompakt.md) →