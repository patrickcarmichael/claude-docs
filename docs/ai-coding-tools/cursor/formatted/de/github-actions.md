---
title: "GitHub Actions"
source: "https://docs.cursor.com/de/cli/github-actions"
language: "de"
language_name: "German"
---

# GitHub Actions
Source: https://docs.cursor.com/de/cli/github-actions

Erfahre, wie du die Cursor-CLI in GitHub Actions und anderen Continuous-Integration-Systemen nutzt

Nutze die Cursor-CLI in GitHub Actions und anderen CI/CD-Systemen, um Entwicklungsaufgaben zu automatisieren.

<div id="github-actions-integration">
  ## GitHub-Actions-Integration
</div>

Grundkonfiguration:

```yaml  theme={null}
- name: Cursor-CLI installieren
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Cursor-Agent ausführen
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "Dein Prompt hier" --model gpt-5
```

<div id="cookbook-examples">
  ## Cookbook-Beispiele
</div>

Schau dir unsere Cookbook-Beispiele für praktische Workflows an: [Dokumentation aktualisieren](/de/cli/cookbook/update-docs) und [CI-Issues beheben](/de/cli/cookbook/fix-ci).

<div id="other-ci-systems">
  ## Andere CI-Systeme
</div>

Verwende die Cursor-CLI in jedem CI/CD-System mit:

* **Ausführung von Shell-Skripten** (bash, zsh usw.)
* **Umgebungsvariablen** zur Konfiguration des API-Keys
* **Internetverbindung**, um die Cursor-API zu erreichen

<div id="autonomy-levels">
  ## Autonomie‑Stufen
</div>

Wähle die Autonomie‑Stufe deines Agents:

<div id="full-autonomy-approach">
  ### Vollautonomer Ansatz
</div>

Gib dem Agenten die vollständige Kontrolle über Git‑Operationen, API‑Aufrufe und externe Interaktionen. Einfacheres Setup, erfordert mehr Vertrauen.

**Beispiel:** In unserem [Update Documentation](/de/cli/cookbook/update-docs)‑Cookbook ermöglicht der erste Workflow dem Agenten:

* PR‑Änderungen analysieren
* Git‑Branches erstellen und verwalten
* Änderungen committen und pushen
* Kommentare zu Pull Requests posten
* Alle Fehlerszenarien behandeln

```yaml  theme={null}
- name: Doku aktualisieren (volle Autonomie)
  run: |
    cursor-agent -p "Du hast vollen Zugriff auf Git, die GitHub-CLI und PR-Operationen. 
    Übernimm den gesamten Doku-Update-Workflow, einschließlich Commits, Pushes und PR-Kommentaren."
```

<div id="restricted-autonomy-approach">
  ### Ansatz mit eingeschränkter Autonomie
</div>

<Note>
  Wir empfehlen, diesen Ansatz mit **berechtigungsbasierten Einschränkungen** für produktive CI-Workflows zu verwenden. So bekommst du das Beste aus beiden Welten: Der Agent kann komplexe Analysen und Dateänderungen intelligent ausführen, während kritische Operationen deterministisch und nachvollziehbar bleiben.
</Note>

Beschränke die Aktionen des Agents und führe kritische Schritte in separaten Workflow-Schritten aus. So erreichst du bessere Kontrolle und Vorhersehbarkeit.

**Beispiel:** Der zweite Workflow im selben Cookbook beschränkt den Agent auf reine Dateänderungen:

```yaml  theme={null}
- name: Docs-Updates generieren (eingeschränkt)
  run: |
    cursor-agent -p "WICHTIG: Keine Branches erstellen, keine Commits, keine Pushes und keine PR-Kommentare posten. 
    Nur Dateien im Arbeitsverzeichnis ändern. Ein späterer Workflow-Schritt übernimmt das Veröffentlichen."

- name: Docs-Branch veröffentlichen (deterministisch)
  run: |
    # Deterministische Git-Operationen werden von CI ausgeführt
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: Update für PR"
    git push origin "docs/${{ github.head_ref }}"

- name: PR-Kommentar posten (deterministisch)  
  run: |
    # Deterministisches Posten von PR-Kommentaren wird von CI ausgeführt
    gh pr comment ${{ github.event.pull_request.number }} --body "Docs aktualisiert"
```

<div id="permission-based-restrictions">
  ### Berechtigungsbasierte Einschränkungen
</div>

Verwende [Berechtigungskonfigurationen](/de/cli/reference/permissions), um Einschränkungen auf CLI-Ebene zu erzwingen:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Write(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": [
      "Shell(git)",
      "Shell(gh)", 
      "Write(.env*)",
      "Write(package.json)"
    ]
  }
}
```

<div id="authentication">
  ## Authentifizierung
</div>

<div id="generate-your-api-key">
  ### API-Schlüssel generieren
</div>

Zuerst [einen API-Schlüssel generieren](/de/cli/reference/authentication#api-key-authentication) im Cursor-Dashboard.

<div id="configure-repository-secrets">
  ### Repository-Secrets konfigurieren
</div>

Speichere deinen Cursor-API-Schlüssel sicher in deinem Repository:

1. Geh zu deinem GitHub-Repository
2. Klick auf **Settings** → **Secrets and variables** → **Actions**
3. Klick auf **New repository secret**
4. Nenn ihn `CURSOR_API_KEY`
5. Füg deinen API-Schlüssel als Wert ein
6. Klick auf **Add secret**

<div id="use-in-workflows">
  ### In Workflows verwenden
</div>

Setz deine Umgebungsvariable `CURSOR_API_KEY`:

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```

---

← Previous: [Docs aktualisieren](./docs-aktualisieren.md) | [Index](./index.md) | Next: [Verwendung der Headless-CLI](./verwendung-der-headless-cli.md) →