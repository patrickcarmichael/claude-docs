---
title: "Verwendung der Headless-CLI"
source: "https://docs.cursor.com/de/cli/headless"
language: "de"
language_name: "German"
---

# Verwendung der Headless-CLI
Source: https://docs.cursor.com/de/cli/headless

Lerne, wie du mit der Cursor-CLI Skripte für automatisierte Codeanalyse, -generierung und -änderung schreibst

Verwende die Cursor-CLI in Skripten und Automatisierungs-Workflows für Codeanalyse, -generierung und Refactoring.

## So funktioniert's

Verwende den [Print-Modus](/de/cli/using#non-interactive-mode) (`-p, --print`) für nicht-interaktives Scripting und Automatisierung.

<div id="file-modification-in-scripts">
  ### Dateiänderungen in Skripten
</div>

Kombiniere `--print` mit `--force`, um Dateien in Skripten zu ändern:

```bash  theme={null}

---

← Previous: [GitHub Actions](./github-actions.md) | [Index](./index.md) | Next: [Installation](./installation.md) →