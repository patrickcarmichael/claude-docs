---
title: "Code Review"
source: "https://docs.cursor.com/de/cli/cookbook/code-review"
language: "de"
language_name: "German"
---

# Code Review
Source: https://docs.cursor.com/de/cli/cookbook/code-review

Erstell einen GitHub-Actions-Workflow, der die Cursor-CLI verwendet, um Pull Requests automatisch zu prüfen und Feedback zu geben

Dieses Tutorial zeigt dir, wie du Code Reviews mit der Cursor-CLI in GitHub Actions einrichtest. Der Workflow analysiert Pull Requests, identifiziert Probleme und postet Feedback als Kommentare.

<Tip>
  Für die meisten Nutzer empfehlen wir stattdessen [Bugbot](/de/bugbot). Bugbot bietet ein verwaltetes, automatisiertes Code Review ohne Setup. Dieser CLI-Ansatz ist hilfreich, um die Möglichkeiten zu erkunden und für fortgeschrittene Anpassungen.
</Tip>

<div className="space-y-4">
  <Expandable title="vollständige Workflow-Datei">
    ```yaml cursor-code-review.yml theme={null}
    name: Code Review

    on:
      pull_request:
        types: [opened, synchronize, reopened, ready_for_review]

    permissions:
      pull-requests: write
      contents: read
      issues: write

    jobs:
      code-review:
        runs-on: ubuntu-latest
        # Automatisierte Code-Reviews für Entwurfs-PRs überspringen
        if: github.event.pull_request.draft == false
        steps:
          - name: Repository auschecken
            uses: actions/checkout@v4
            with:
              fetch-depth: 0
              ref: ${{ github.event.pull_request.head.sha }}

          - name: Cursor-CLI installieren
            run: |
              curl https://cursor.com/install -fsS | bash
              echo "$HOME/.cursor/bin" >> $GITHUB_PATH

          - name: Git-Identität konfigurieren
            run: |
              git config user.name "Cursor Agent"
              git config user.email "cursoragent@cursor.com"

          - name: Automatisiertes Code-Review durchführen
            env:
              CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
              MODEL: gpt-5
              GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
              BLOCKING_REVIEW: ${{ vars.BLOCKING_REVIEW || 'false' }}
            run: |
              cursor-agent --force --model "$MODEL" --output-format=text --print 'Du arbeitest in einem GitHub-Actions-Runner und führst ein automatisiertes Code-Review durch. Die gh-CLI ist verfügbar und über GH_TOKEN authentifiziert. Du darfst Pull Requests kommentieren.

              Kontext:
              - Repo: ${{ github.repository }}
              - PR Number: ${{ github.event.pull_request.number }}
              - PR Head SHA: ${{ github.event.pull_request.head.sha }}
              - PR Base SHA: ${{ github.event.pull_request.base.sha }}
              - Blockierendes Review: ${{ env.BLOCKING_REVIEW }}

              Ziele:
              1) Bestehende Review-Kommentare erneut prüfen und mit resolved antworten, wenn erledigt.
              2) Den aktuellen PR-Diff prüfen und nur eindeutige, schwerwiegende Probleme markieren.
              3) Sehr kurze Inline-Kommentare (1–2 Sätze) ausschließlich auf geänderten Zeilen hinterlassen und am Ende eine kurze Zusammenfassung.

              Vorgehen:
              - Bestehende Kommentare abrufen: gh pr view --json comments
              - Diff abrufen: gh pr diff
              - Geänderte Dateien mit Patches abrufen, um Inline-Positionen zu berechnen: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/files --paginate --jq '.[] | {filename,patch}'
              - Exakte Inline-Anker für jedes Problem berechnen (Dateipfad + Diff-Position). Kommentare MÜSSEN inline auf der geänderten Zeile im Diff platziert werden, nicht als Top-Level-Kommentare.
              - Frühere Top-Level-Kommentare im Stil „keine Probleme“ erkennen, die von diesem Bot verfasst wurden (Texte wie: "✅ no issues", "No issues found", "LGTM").
              - Wenn beim aktuellen Lauf Probleme gefunden werden und frühere „keine Probleme“-Kommentare existieren:
                - Diese nach Möglichkeit entfernen, um Verwirrung zu vermeiden:
                  - Versuchen, Top-Level-Kommentare zu löschen via: gh api -X DELETE repos/${{ github.repository }}/issues/comments/<comment_id>
                  - Falls Löschen nicht möglich ist, via GraphQL minimieren (minimizeComment) oder so bearbeiten, dass "[Superseded by new findings]" vorangestellt wird.
                - Falls weder Löschen noch Minimieren möglich ist, auf diesen Kommentar antworten: "⚠️ Superseded: issues were found in newer commits".
              - Wenn ein zuvor gemeldetes Problem durch nahe Änderungen behoben erscheint, antworte: ✅ This issue appears to be resolved by the recent changes
              - NUR analysieren auf:
                - Null/undefined-Dereferenzierungen
                - Ressourcenlecks (nicht geschlossene Dateien oder Verbindungen)
                - Injection (SQL/XSS)
                - Nebenläufigkeit/Race Conditions
                - Fehlende Fehlerbehandlung bei kritischen Operationen
                - Offensichtliche Logikfehler mit fehlerhaftem Verhalten
                - Klare Performance-Anti-Patterns mit messbarem Einfluss
                - Eindeutige Sicherheitslücken
              - Duplikate vermeiden: überspringen, wenn ähnliches Feedback bereits auf oder nahe derselben Zeile existiert.

              Kommentarregeln:
              - Maximal 10 Inline-Kommentare insgesamt; priorisiere die kritischsten Probleme
              - Ein Problem pro Kommentar; exakt auf der geänderten Zeile platzieren
              - Alle Problemkommentare MÜSSEN inline sein (an Datei und Zeile/Position im PR-Diff verankert)
              - Natürlicher Ton, spezifisch und umsetzbar; nicht erwähnen, dass es automatisiert ist oder auf hoher Sicherheit beruht
              - Emojis verwenden: 🚨 Kritisch 🔒 Sicherheit ⚡ Performance ⚠️ Logik ✅ Behoben ✨ Verbesserung

              Einreichung:
              - Wenn es KEINE Probleme zu melden gibt und bereits ein bestehender Top-Level-Kommentar vorhanden ist, der „keine Probleme“ angibt (z. B. "✅ no issues", "No issues found", "LGTM"), KEINEN weiteren Kommentar einreichen. Einreichung überspringen, um Redundanz zu vermeiden.
              - Wenn es KEINE Probleme zu melden gibt und KEIN vorheriger „keine Probleme“-Kommentar existiert, einen kurzen Zusammenfassungskommentar einreichen, der keine Probleme vermerkt.
              - Wenn es Probleme zu melden gibt und ein vorheriger „keine Probleme“-Kommentar existiert, sicherstellen, dass der vorherige Kommentar vor Einreichung des neuen Reviews gelöscht/minimiert/als überholt markiert wird.
              - Wenn es Probleme zu melden gibt, EIN Review einreichen, das NUR Inline-Kommentare plus einen optionalen knappen Zusammenfassungstext enthält. Die GitHub-Reviews-API verwenden, um sicherzustellen, dass Kommentare inline sind:
                - Ein JSON-Array von Kommentaren erstellen wie: [{ "path": "<file>", "position": <diff_position>, "body": "..." }]
                - Einreichen via: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/reviews -f event=COMMENT -f body="$SUMMARY" -f comments='[$COMMENTS_JSON]'
              - NICHT verwenden: gh pr review --approve oder --request-changes

              Blockierendes Verhalten:
              - Wenn BLOCKING_REVIEW true ist und irgendein 🚨- oder 🔒-Problem gepostet wurde: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
              - Andernfalls: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
              - CRITICAL_ISSUES_FOUND immer am Ende setzen
              '

          - name: Ergebnisse des blockierenden Reviews prüfen
            if: env.BLOCKING_REVIEW == 'true'
            run: |
              echo "Prüfe auf kritische Probleme..."
              echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

              if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
                echo "❌ Kritische Probleme gefunden und blockierendes Review ist aktiviert. Workflow wird fehlgeschlagen."
                exit 1
              else
                echo "✅ Keine blockierenden Probleme gefunden."
              fi
    ```
  </Expandable>

  <Frame>
    <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=31c7e4b54276532df8010645686ebbbc" alt="Automatisiertes Code-Review in Aktion mit Inline-Kommentaren in einem Pull Request" data-og-width="2920" width="2920" data-og-height="1272" height="1272" data-path="images/cli/cookbook/code-review/comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=25e552210fa8425a10ff459bf4cd6006 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=234bf271bc595e763549c4f04d2e6fbb 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=b6f6d1444de7fe0197e3d35fa35955e8 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=300314314f5071b77f735460be33985f 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=10e4db857ee84c55d17222cef492611d 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=e65add70ffebfeb9ad05c9bb19a5f4e1 2500w" />
  </Frame>
</div>

<div id="configure-authentication">
  ## Authentifizierung konfigurieren
</div>

[Richte deinen API-Schlüssel und die Repository-Secrets ein](/de/cli/github-actions#authentication), um die Cursor-CLI in GitHub Actions zu authentifizieren.

<div id="set-up-agent-permissions">
  ## Agent-Berechtigungen einrichten
</div>

Erstell eine Konfigurationsdatei, um festzulegen, welche Aktionen der Agent ausführen darf. So verhinderst du unbeabsichtigte Aktionen wie das Pushen von Code oder das Erstellen von Pull Requests.

Erstell `.cursor/cli.json` im Root-Verzeichnis deines Repos:

```json  theme={null}
{
  "permissions": {
    "deny": [
      "Shell(git push)",
      "Shell(gh pr create)",
      "Write(**)"
    ]
  }
}
```

Diese Konfiguration erlaubt dem Agenten, Dateien zu lesen und die GitHub-CLI für Kommentare zu verwenden, verhindert aber, dass er Änderungen an deinem Repository vornimmt. Sieh dir die [Berechtigungsreferenz](/de/cli/reference/permissions) für weitere Konfigurationsoptionen an.

<div id="build-the-github-actions-workflow">
  ## Baue den GitHub-Actions-Workflow
</div>

Lass uns den Workflow jetzt Schritt für Schritt aufsetzen.

<div id="set-up-the-workflow-trigger">
  ### Richte den Workflow-Trigger ein
</div>

Erstelle `.github/workflows/cursor-code-review.yml` und konfiguriere ihn so, dass er bei Pull Requests ausgeführt wird:

```yaml  theme={null}
name: Cursor-Code-Review

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

jobs:
  code-review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    
    steps:
```

<div id="checkout-the-repository">
  ### Repository auschecken
</div>

Füg den Checkout-Schritt hinzu, um auf den Pull-Request-Code zuzugreifen:

```yaml  theme={null}
- name: Repository auschecken
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    ref: ${{ github.event.pull_request.head.sha }}
```

<div id="install-cursor-cli">
  ### Cursor-CLI installieren
</div>

Füg den CLI-Installationsschritt hinzu:

```yaml  theme={null}
- name: Cursor-CLI installieren
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH
```

<div id="configure-the-review-agent">
  ### Konfiguriere den Review-Agent
</div>

Bevor wir den vollständigen Review-Schritt implementieren, lass uns die Struktur unseres Review-Prompts verstehen. Dieser Abschnitt beschreibt, wie sich der Agent verhalten soll:

**Ziel**:
Wir wollen, dass der Agent den aktuellen PR-Diff prüft und nur eindeutige, schwerwiegende Probleme markiert, dann sehr kurze Inline-Kommentare (1–2 Sätze) ausschließlich zu geänderten Zeilen hinterlässt, mit einer kurzen Zusammenfassung am Ende. Das hält das Signal-Rausch-Verhältnis ausgewogen.

**Format**:
Wir wollen Kommentare, die kurz und auf den Punkt sind. Wir verwenden Emojis, um das Durchscannen der Kommentare zu erleichtern, und möchten am Ende eine High-Level-Zusammenfassung des gesamten Reviews.

**Abgabe**:
Wenn das Review abgeschlossen ist, soll der Agent einen kurzen Kommentar basierend auf den während des Reviews gefundenen Punkten hinzufügen. Der Agent sollte ein einziges Review einreichen, das Inline-Kommentare plus eine prägnante Zusammenfassung enthält.

**Edge Cases**:
Wir müssen Folgendes handhaben:

* Bereits vorhandene, aufgelöste Kommentare: Der Agent sollte sie als erledigt markieren, wenn sie adressiert wurden
* Duplikate vermeiden: Der Agent sollte das Kommentieren überspringen, wenn ähnliches Feedback bereits auf oder nahe derselben Zeile existiert

**Finaler Prompt**:
Der vollständige Prompt kombiniert all diese Verhaltensanforderungen, um fokussiertes, umsetzbares Feedback zu liefern

Jetzt lass uns den Review-Agent-Schritt implementieren:

```yaml  theme={null}
- name: Code-Review durchführen
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
    GH_TOKEN: ${{ github.token }}
  run: |
    cursor-agent --force --model "$MODEL" --output-format=text --print "Du arbeitest in einem GitHub-Actions-Runner und führst eine automatisierte Code-Review durch. Die gh-CLI ist verfügbar und über GH_TOKEN authentifiziert. Du darfst Pull Requests kommentieren.
    
    Kontext:
    - Repo: ${{ github.repository }}
    - PR-Nummer: ${{ github.event.pull_request.number }}
    - PR Head SHA: ${{ github.event.pull_request.head.sha }}
    - PR Base SHA: ${{ github.event.pull_request.base.sha }}
    
    Ziele:
    1) Bestehende Review-Kommentare erneut prüfen und bei Erledigung mit „resolved“ antworten
    2) Den aktuellen PR-Diff prüfen und nur eindeutige, schwerwiegende Probleme markieren
    3) Sehr kurze Inline-Kommentare (1–2 Sätze) nur auf geänderten Zeilen hinterlassen und am Ende eine kurze Zusammenfassung
    
    Vorgehen:
    - Vorhandene Kommentare abrufen: gh pr view --json comments
    - Diff abrufen: gh pr diff
    - Wenn ein zuvor gemeldetes Problem durch nahe Änderungen behoben wirkt, antworten: ✅ Dieses Problem scheint durch die jüngsten Änderungen behoben zu sein
    - Duplikate vermeiden: überspringen, wenn ähnliches Feedback bereits auf oder nahe denselben Zeilen existiert
    
    Kommentierregeln:
    - Maximal 10 Inline-Kommentare insgesamt; die kritischsten Probleme priorisieren
    - Ein Problem pro Kommentar; exakt auf der geänderten Zeile platzieren
    - Natürlicher Ton, konkret und umsetzbar; keine Erwähnung von Automatisierung oder hoher Sicherheit
    - Emojis verwenden: 🚨 Kritisch 🔒 Sicherheit ⚡ Performance ⚠️ Logik ✅ Erledigt ✨ Verbesserung
    
    Einreichung:
    - Eine Review einreichen, die Inline-Kommentare plus eine prägnante Zusammenfassung enthält
    - Nur verwenden: gh pr review --comment
    - Nicht verwenden: gh pr review --approve oder --request-changes"
```

```text  theme={null}
.
├── .cursor/
│   └── cli.json
├── .github/
│   └── workflows/
│       └── cursor-code-review.yml
```

<div id="test-your-reviewer">
  ## Teste deinen Reviewer
</div>

Erstell einen Test-Pull-Request, um zu prüfen, dass der Workflow funktioniert und der Agent Review-Kommentare mit Emoji-Feedback postet.

<Frame>
  <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=aa989eb5b7520e6718a48afd8daa70d9" alt="Pull-Request mit automatisierten Review-Kommentaren mit Emojis und Inline-Feedback zu bestimmten Zeilen" data-og-width="1250" width="1250" data-og-height="704" height="704" data-path="images/cli/cookbook/code-review/github-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=9f2e324beb1cccb8052dcd0682323e47 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f08497ddb17921f4bb4638ef4eec3379 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=3c869c0ed8eb8b5743dd3821e57cd406 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=19e98ed953f4cc17b2c578ce543cf88d 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=4d9f47472af81254bd09b5f6234fc97f 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f3af19e3edd7f8bbbb77ba6566d8e183 2500w" />
</Frame>

<div id="next-steps">
  ## Nächste Schritte
</div>

Du hast jetzt ein funktionierendes, automatisiertes Code-Review-System. Überleg dir diese Erweiterungen:

* Richte zusätzliche Workflows zum [Beheben von CI-Fehlern](/de/cli/cookbook/fix-ci) ein
* Konfiguriere unterschiedliche Review-Stufen für verschiedene Branches
* Integriere den Workflow in den bestehenden Code-Review-Prozess deines Teams
* Passe das Verhalten des Agents für verschiedene Dateitypen oder Verzeichnisse an

<Expandable title="Fortgeschritten: Blockierende Reviews">
  Du kannst den Workflow so konfigurieren, dass er fehlschlägt, wenn kritische Probleme gefunden werden. So wird der Pull Request so lange nicht gemerged, bis sie behoben sind.

  **Blockierendes Verhalten zum Prompt hinzufügen**

  Aktualisiere zuerst deinen Review-Agent-Schritt, um die Umgebungsvariable `BLOCKING_REVIEW` einzuschließen, und füge dieses blockierende Verhalten zum Prompt hinzu:

  ```
  Blocking behavior:
  - If BLOCKING_REVIEW is true and any 🚨 or 🔒 issues were posted: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
  - Otherwise: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
  - Always set CRITICAL_ISSUES_FOUND at the end
  ```

  **Blockierenden Prüfschritt hinzufügen**

  Füg anschließend diesen neuen Schritt nach deinem Code-Review-Schritt hinzu:

  ```yaml  theme={null}
        - name: Check blocking review results
          if: env.BLOCKING_REVIEW == 'true'
          run: |
            echo "Checking for critical issues..."
            echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

            if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
              echo "❌ Critical issues found and blocking review is enabled. Failing the workflow."
              exit 1
            else
              echo "✅ No blocking issues found."
            fi
  ```
</Expandable>

---

← Previous: [Bugbot](./bugbot.md) | [Index](./index.md) | Next: [CI-Fehler beheben](./ci-fehler-beheben.md) →