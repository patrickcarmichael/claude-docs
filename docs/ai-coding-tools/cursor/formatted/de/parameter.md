---
title: "Parameter"
source: "https://docs.cursor.com/de/cli/reference/parameters"
language: "de"
language_name: "German"
---

# Parameter
Source: https://docs.cursor.com/de/cli/reference/parameters

Vollständige Befehlsreferenz für die Cursor-Agent-CLI

<div id="global-options">
  ## Globale Optionen
</div>

Globale Optionen können mit jedem Befehl verwendet werden:

<div class="full-width-table">
  | Option                     | Beschreibung                                                                                                                               |
  | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
  | `-v, --version`            | Versionsnummer ausgeben                                                                                                                    |
  | `-a, --api-key <key>`      | API-Schlüssel für die Authentifizierung (du kannst auch die Umgebungsvariable `CURSOR_API_KEY` verwenden)                                  |
  | `-p, --print`              | Antworten in der Konsole ausgeben (für Skripte oder nicht-interaktive Nutzung). Hat Zugriff auf alle Tools, einschließlich write und bash. |
  | `--output-format <format>` | Ausgabeformat (funktioniert nur mit `--print`): `text`, `json` oder `stream-json` (Standard: `stream-json`)                                |
  | `-b, --background`         | Im Hintergrundmodus starten (Composer-Auswahl beim Start öffnen)                                                                           |
  | `--fullscreen`             | Vollbildmodus aktivieren                                                                                                                   |
  | `--resume [chatId]`        | Eine Chatsitzung fortsetzen                                                                                                                |
  | `-m, --model <model>`      | Zu verwendetes Modell                                                                                                                      |
  | `-f, --force`              | Befehle erzwingen, außer sie wurden ausdrücklich verweigert                                                                                |
  | `-h, --help`               | Hilfe für den Befehl anzeigen                                                                                                              |
</div>

<div id="commands">
  ## Befehle
</div>

<div class="full-width-table">
  | Befehl            | Beschreibung                                       | Verwendung                                        |
  | ----------------- | -------------------------------------------------- | ------------------------------------------------- |
  | `login`           | Bei Cursor anmelden                                | `cursor-agent login`                              |
  | `logout`          | Abmelden und gespeicherte Anmeldedaten löschen     | `cursor-agent logout`                             |
  | `status`          | Anmeldestatus prüfen                               | `cursor-agent status`                             |
  | `mcp`             | MCP-Server verwalten                               | `cursor-agent mcp`                                |
  | `update\|upgrade` | Cursor Agent auf die neueste Version aktualisieren | `cursor-agent update` oder `cursor-agent upgrade` |
  | `ls`              | Eine Chat-Sitzung fortsetzen                       | `cursor-agent ls`                                 |
  | `resume`          | Die letzte Chat-Sitzung fortsetzen                 | `cursor-agent resume`                             |
  | `help [command]`  | Hilfe zu einem Befehl anzeigen                     | `cursor-agent help [command]`                     |
</div>

<Note>
  Wenn du keinen Befehl angibst, startet Cursor Agent standardmäßig im interaktiven Chat-Modus.
</Note>

<div id="mcp">
  ## MCP
</div>

Verwalte MCP-Server, die für den Cursor Agent konfiguriert sind.

<div class="full-width-table">
  | Subcommand                | Beschreibung                                                              | Verwendung                                 |
  | ------------------------- | ------------------------------------------------------------------------- | ------------------------------------------ |
  | `login <identifier>`      | Bei einem in `.cursor/mcp.json` konfigurierten MCP-Server anmelden        | `cursor-agent mcp login <identifier>`      |
  | `list`                    | Konfigurierte MCP-Server und ihren Status anzeigen                        | `cursor-agent mcp list`                    |
  | `list-tools <identifier>` | Verfügbare Tools und ihre Argumentnamen für einen bestimmten MCP anzeigen | `cursor-agent mcp list-tools <identifier>` |
</div>

Alle MCP-Befehle unterstützen `-h, --help` für befehlsbezogene Hilfe.

<div id="arguments">
  ## Argumente
</div>

Wenn du im Chat-Modus startest (Standardverhalten), kannst du eine anfängliche Eingabe angeben:

**Argumente:**

* `prompt` — anfänglicher Prompt für den Agent

<div id="getting-help">
  ## Hilfe erhalten
</div>

Alle Befehle unterstützen die globale Option `-h, --help`, um befehlspezifische Hilfe anzuzeigen.

---

← Previous: [Ausgabeformat](./ausgabeformat.md) | [Index](./index.md) | Next: [Berechtigungen](./berechtigungen.md) →