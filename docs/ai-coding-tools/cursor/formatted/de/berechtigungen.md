---
title: "Berechtigungen"
source: "https://docs.cursor.com/de/cli/reference/permissions"
language: "de"
language_name: "German"
---

# Berechtigungen
Source: https://docs.cursor.com/de/cli/reference/permissions

Berechtigungstypen zur Steuerung des Agentenzugriffs auf Dateien und Befehle

Konfigurier, was der Agent darf, indem du Berechtigungstokens in deiner CLI-Konfiguration verwendest. Berechtigungen werden in `~/.cursor/cli-config.json` (global) oder `<project>/.cursor/cli.json` (projektspezifisch) festgelegt.

<div id="permission-types">
  ## Berechtigungstypen
</div>

<div id="shell-commands">
  ### Shell-Befehle
</div>

**Format:** `Shell(commandBase)`

Steuert den Zugriff auf Shell-Befehle. `commandBase` ist das erste Token in der Befehlszeile.

<div class="full-width-table">
  | Beispiel     | Beschreibung                                                   |
  | ------------ | -------------------------------------------------------------- |
  | `Shell(ls)`  | Erlaubt das Ausführen von `ls`-Befehlen                        |
  | `Shell(git)` | Erlaubt beliebige `git`-Unterbefehle                           |
  | `Shell(npm)` | Erlaubt Befehle des npm-Paketmanagers                          |
  | `Shell(rm)`  | Verweigert destruktives Löschen von Dateien (häufig in `deny`) |
</div>

<div id="file-reads">
  ### Dateilesen
</div>

**Format:** `Read(pathOrGlob)`

Steuert Lesezugriff auf Dateien und Verzeichnisse. Unterstützt Glob-Muster.

<div class="full-width-table">
  | Beispiel            | Beschreibung                                      |
  | ------------------- | ------------------------------------------------- |
  | `Read(src/**/*.ts)` | Erlaubt das Lesen von TypeScript-Dateien in `src` |
  | `Read(**/*.md)`     | Erlaubt das Lesen von Markdown-Dateien überall    |
  | `Read(.env*)`       | Verweigert das Lesen von Umgebungsdateien         |
  | `Read(/etc/passwd)` | Verweigert das Lesen von Systemdateien            |
</div>

<div id="file-writes">
  ### Dateischreiben
</div>

**Format:** `Write(pathOrGlob)`

Steuert Schreibzugriff auf Dateien und Verzeichnisse. Unterstützt Glob-Muster. Im Print-Modus ist `--force` erforderlich, um Dateien zu schreiben.

<div class="full-width-table">
  | Beispiel              | Beschreibung                                           |
  | --------------------- | ------------------------------------------------------ |
  | `Write(src/**)`       | Erlaubt das Schreiben in beliebige Dateien unter `src` |
  | `Write(package.json)` | Erlaubt das Ändern von package.json                    |
  | `Write(**/*.key)`     | Verweigert das Schreiben privater Schlüsseldateien     |
  | `Write(**/.env*)`     | Verweigert das Schreiben von Umgebungsdateien          |
</div>

<div id="configuration">
  ## Konfiguration
</div>

Füg dem `permissions`-Objekt in deiner CLI-Konfigurationsdatei Berechtigungen hinzu:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)", 
      "Read(src/**/*.ts)",
      "Write(package.json)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  }
}
```

<div id="pattern-matching">
  ## Pattern Matching
</div>

* Glob-Muster verwenden die Platzhalter `**`, `*` und `?`
* Relative Pfade sind auf den aktuellen Workspace begrenzt
* Absolute Pfade können auf Dateien außerhalb des Projekts zeigen
* Deny-Regeln haben Vorrang vor Allow-Regeln

---

← Previous: [Parameter](./parameter.md) | [Index](./index.md) | Next: [Slash-Befehle](./slash-befehle.md) →