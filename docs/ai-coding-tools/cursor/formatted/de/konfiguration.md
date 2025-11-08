---
title: "Konfiguration"
source: "https://docs.cursor.com/de/cli/reference/configuration"
language: "de"
language_name: "German"
---

# Konfiguration
Source: https://docs.cursor.com/de/cli/reference/configuration

Konfigurationsreferenz der Agent-CLI für cli-config.json

Konfigurier die Agent-CLI mit der Datei `cli-config.json`.

<div id="file-location">
  ## Speicherort der Datei
</div>

<div class="full-width-table">
  | Typ     | Plattform   | Pfad                                       |
  | :------ | :---------- | :----------------------------------------- |
  | Global  | macOS/Linux | `~/.cursor/cli-config.json`                |
  | Global  | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | Projekt | Alle        | `<project>/.cursor/cli.json`               |
</div>

<Note>Auf Projektebene lassen sich nur Berechtigungen konfigurieren. Alle anderen CLI-Einstellungen müssen global gesetzt werden.</Note>

Per Umgebungsvariablen überschreiben:

* **`CURSOR_CONFIG_DIR`**: benutzerdefinierter Verzeichnispfad
* **`XDG_CONFIG_HOME`** (Linux/BSD): verwendet `$XDG_CONFIG_HOME/cursor/cli-config.json`

<div id="schema">
  ## Schema
</div>

<div id="required-fields">
  ### Pflichtfelder
</div>

<div class="full-width-table">
  | Feld                | Typ       | Beschreibung                                                               |
  | :------------------ | :-------- | :------------------------------------------------------------------------- |
  | `version`           | number    | Version des Konfigurationsschemas (aktuell: `1`)                           |
  | `editor.vimMode`    | boolean   | Vim-Keybindings aktivieren (Standard: `false`)                             |
  | `permissions.allow` | string\[] | Erlaubte Operationen (siehe [Permissions](/de/cli/reference/permissions))  |
  | `permissions.deny`  | string\[] | Verbotene Operationen (siehe [Permissions](/de/cli/reference/permissions)) |
</div>

<div id="optional-fields">
  ### Optionale Felder
</div>

<div class="full-width-table">
  | Feld                     | Typ     | Beschreibung                                                   |
  | :----------------------- | :------ | :------------------------------------------------------------- |
  | `model`                  | object  | Ausgewählte Modellkonfiguration                                |
  | `hasChangedDefaultModel` | boolean | Vom CLI verwaltetes Flag zum Überschreiben des Standardmodells |
</div>

<div id="examples">
  ## Beispiele
</div>

<div id="minimal-config">
  ### Minimalkonfiguration
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="enable-vim-mode">
  ### Vim-Modus einschalten
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="configure-permissions">
  ### Berechtigungen konfigurieren
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

Sieh dir die [Permissions](/de/cli/reference/permissions) für verfügbare Berechtigungstypen und Beispiele an.

<div id="troubleshooting">
  ## Fehlerbehebung
</div>

**Konfigurationsfehler**: Leg die Datei zur Seite und starte neu:

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**Änderungen werden nicht beibehalten**: Achte auf gültiges JSON und ausreichende Schreibrechte. Manche Felder werden vom CLI verwaltet und können überschrieben werden.

<div id="notes">
  ## Hinweise
</div>

* Reines JSON-Format (keine Kommentare)
* Die CLI repariert fehlende Felder automatisch
* Beschädigte Dateien werden als `.bad` gesichert und neu erstellt
* Berechtigungseinträge sind exakte Zeichenketten (siehe [Permissions](/de/cli/reference/permissions) für Details)

---

← Previous: [Authentifizierung](./authentifizierung.md) | [Index](./index.md) | Next: [Ausgabeformat](./ausgabeformat.md) →