---
title: "Docs aktualisieren"
source: "https://docs.cursor.com/de/cli/cookbook/update-docs"
language: "de"
language_name: "German"
---

# Docs aktualisieren
Source: https://docs.cursor.com/de/cli/cookbook/update-docs

Aktualisiere die Doku für ein Repository mit der Cursor-CLI in GitHub Actions

Aktualisiere die Doku mit der Cursor-CLI in GitHub Actions. Zwei Ansätze: vollständige Agent-Autonomie oder deterministischer Workflow, bei dem nur der Agent Dateien ändert.

<CodeGroup>
  ```yaml auto-update-docs.yml theme={null}
  name: Dokumentation aktualisieren

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Repository auschecken
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Cursor-CLI installieren
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Git konfigurieren
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Docs aktualisieren
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Du arbeitest in einem GitHub-Actions-Runner.

            Die GitHub-CLI ist als `gh` verfügbar und über `GH_TOKEN` authentifiziert. Git ist verfügbar. Du hast Schreibzugriff auf die Repository-Inhalte und kannst Pull Requests kommentieren, darfst aber keine PRs erstellen oder bearbeiten.

            # Kontext:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}
            - Docs Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Ziel:
            - Implementiere einen End-to-End-Flow zur Aktualisierung der Docs, gesteuert durch inkrementelle Änderungen am ursprünglichen PR.

            # Anforderungen:
            1) Ermittle, was sich im ursprünglichen PR geändert hat, und falls es mehrere Pushes gab, berechne die inkrementellen Diffs seit der letzten erfolgreichen Docs-Aktualisierung.
            2) Aktualisiere nur die relevanten Docs basierend auf diesen inkrementellen Änderungen.
            3) Pflege den persistenten Docs-Branch für diesen PR-Head mithilfe des Docs-Branch-Präfixes aus dem Kontext. Erstelle ihn, wenn er fehlt, aktualisiere ihn andernfalls und pushe Änderungen nach origin.
            4) Du hast KEINE Berechtigung, PRs zu erstellen. Verfasse stattdessen einen einzelnen, natürlichsprachlichen PR-Kommentar (1–2 Sätze), der die Docs-Updates kurz erklärt und einen Inline-Compare-Link enthält, um schnell einen PR zu erstellen

            # Eingaben und Konventionen:
            - Verwende `gh pr diff` und die Git-Historie, um Änderungen zu erkennen und inkrementelle Bereiche seit der letzten Docs-Aktualisierung abzuleiten.
            - Versuche nicht, PRs direkt zu erstellen oder zu bearbeiten. Verwende das oben genannte Compare-Link-Format.
            - Halte Änderungen minimal und konsistent mit dem Repo-Stil. Wenn keine Docs-Updates notwendig sind, nimm keine Änderungen vor und poste keinen Kommentar.

            # Ergebnisse bei Updates:
            - Gepushte Commits in den persistenten Docs-Branch für diesen PR-Head.
            - Ein einzelner natürlichsprachlicher PR-Kommentar im ursprünglichen PR, der den oben genannten Inline-Compare-Link enthält. Vermeide Duplikate; aktualisiere einen vorherigen Bot-Kommentar, falls vorhanden.
            " --force --model "$MODEL" --output-format=text
  ```

  ```yaml auto-update-docs-deterministic.yml theme={null}
  name: Docs aktualisieren

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Repository auschecken
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Cursor-CLI installieren
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Git konfigurieren
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Doku-Updates generieren (kein Commit/Push/Kommentar)
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Du arbeitest in einem GitHub-Actions-Runner.

            Die GitHub-CLI ist als `gh` verfügbar und über `GH_TOKEN` authentifiziert. Git ist verfügbar.

            WICHTIG: Erstelle keine Branches, nicht committen, nicht pushen und keine PR-Kommentare posten. Änder nur Dateien im Arbeitsverzeichnis, wenn nötig. Ein späterer Workflow-Schritt veröffentlicht die Änderungen und kommentiert die PR.

            # Kontext:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}

            # Ziel:
            - Aktualisiere die Repository-Dokumentation basierend auf den inkrementellen Änderungen dieses PR.

            # Anforderungen:
            1) Ermittle, was sich im ursprünglichen PR geändert hat (verwende `gh pr diff` und die Git-Historie nach Bedarf). Falls ein bestehender persistenter Doku-Branch `${{ env.BRANCH_PREFIX }}/${{ github.head_ref }}` existiert, darfst du ihn als schreibgeschützte Referenz nutzen, um frühere Updates nachzuvollziehen.
            2) Aktualisiere nur die relevanten Dokus basierend auf diesen Änderungen. Halte Anpassungen minimal und zum Repo-Stil passend.
            3) Nicht committen, nicht pushen, keine Branches erstellen und keine PR-Kommentare posten. Lass den Working Tree nur mit aktualisierten Dateien zurück; ein späterer Schritt übernimmt das Veröffentlichen.

            # Eingaben und Konventionen:
            - Verwende `gh pr diff` und die Git-Historie, um Änderungen zu erkennen und Doku-Anpassungen gezielt vorzunehmen.
            - Wenn keine Doku-Updates nötig sind, nimm keine Änderungen vor und gib nichts aus.

            # Ergebnisse, wenn Updates erfolgen:
            - Geänderte Dokumentationsdateien nur im Arbeitsverzeichnis (keine Commits/Pushes/Kommentare).
            " --force --model "$MODEL" --output-format=text

        - name: Doku-Branch veröffentlichen
          id: publish_docs
          env:
            BRANCH_PREFIX: docs
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |
            echo "changes_published=false" >> "$GITHUB_OUTPUT"

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"

            # Sicherstellen, dass wir auf einem lokalen Branch sind, den wir pushen können
            git fetch origin --prune

            # Persistenten Doku-Branch erstellen/wechseln, aktuelle Working-Tree-Änderungen beibehalten
            git checkout -B "$DOCS_BRANCH"

            # Änderungen stagen und erkennen
            git add -A
            if git diff --staged --quiet; then
              echo "Keine Doku-Änderungen zu veröffentlichen. Commit/Push wird übersprungen."
              exit 0
            fi

            COMMIT_MSG="docs: update for PR #${PR_NUMBER} (${HEAD_REF} @ $(git rev-parse --short HEAD))"
            git commit -m "$COMMIT_MSG"
            git push --set-upstream origin "$DOCS_BRANCH"

            echo "changes_published=true" >> "$GITHUB_OUTPUT"

        - name: PR-Kommentar posten oder aktualisieren
          if: steps.publish_docs.outputs.changes_published == 'true'
          env:
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
            REPO: ${{ github.repository }}
            BASE_REF: ${{ github.base_ref }}
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"
            COMPARE_URL="https://github.com/${REPO}/compare/${BASE_REF}...${DOCS_BRANCH}?quick_pull=1&title=docs%3A+updates+for+PR+%23${PR_NUMBER}"

            COMMENT_FILE="${RUNNER_TEMP}/auto-docs-comment.md"
            {
              echo "Cursor hat den Doku-Branch aktualisiert: \`${DOCS_BRANCH}\`"
              echo "Du kannst jetzt [den Diff ansehen und schnell eine PR erstellen, um diese Doku-Updates zu mergen](${COMPARE_URL})."
              echo
              echo "_Dieser Kommentar wird bei nachfolgenden Läufen aktualisiert, wenn sich der PR ändert._"
              echo
              echo "<!-- auto-update-docs-split -->"
            } > "$COMMENT_FILE"

            # Falls das Bearbeiten des letzten Bot-Kommentars fehlschlägt (älteres gh), als Fallback einen neuen Kommentar erstellen
            if gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE" --edit-last; then
              echo "Bestehenden PR-Kommentar aktualisiert."
            else
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              echo "Neuen PR-Kommentar veröffentlicht."
  ```
</CodeGroup>

---

← Previous: [Schlüssel übersetzen](./schlssel-bersetzen.md) | [Index](./index.md) | Next: [GitHub Actions](./github-actions.md) →