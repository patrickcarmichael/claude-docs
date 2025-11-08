---
title: "Mettre à jour la doc"
source: "https://docs.cursor.com/fr/cli/cookbook/update-docs"
language: "fr"
language_name: "French"
---

# Mettre à jour la doc
Source: https://docs.cursor.com/fr/cli/cookbook/update-docs

Mets à jour la doc d’un dépôt avec Cursor CLI dans GitHub Actions

Mets à jour la doc avec Cursor CLI dans GitHub Actions. Deux approches : autonomie complète de l’agent ou workflow déterministe où seul l’agent modifie les fichiers.

<CodeGroup>
  ```yaml auto-update-docs.yml theme={null}
  name: Mettre à jour la doc

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
        - name: Cloner le dépôt
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Installer l’interface en ligne de commande Cursor
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configurer Git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Mettre à jour la doc
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Tu tournes dans un runner GitHub Actions.

            Le CLI GitHub est disponible sous `gh` et authentifié via `GH_TOKEN`. Git est disponible. Tu as un accès en écriture au contenu du dépôt et tu peux commenter les pull requests, mais tu ne dois pas créer ni modifier de PR.

            # Contexte :
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}
            - Docs Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Objectif :
            - Mettre en place un flux de mise à jour de la doc de bout en bout, piloté par les changements incrémentaux de la PR d’origine.

            # Exigences :
            1) Déterminer ce qui a changé dans la PR d’origine et, s’il y a eu plusieurs pushs, calculer les diffs incrémentiels depuis la dernière mise à jour de la doc réussie.
            2) Mettre à jour uniquement la doc pertinente en fonction de ces changements incrémentiels.
            3) Maintenir la branche de doc persistante pour le head de cette PR en utilisant le préfixe de branche Docs indiqué dans le Contexte. La créer si elle est absente, sinon la mettre à jour, puis pousser les changements vers origin.
            4) Tu n’as PAS la permission de créer des PR. À la place, publie ou mets à jour un unique commentaire en langage naturel sur la PR (1–2 phrases) qui explique brièvement les mises à jour de la doc et inclut un lien de comparaison en ligne pour créer rapidement une PR.

            # Entrées et conventions :
            - Utilise `gh pr diff` et l’historique Git pour détecter les changements et dériver les plages incrémentielles depuis la dernière mise à jour de la doc.
            - N’essaie pas de créer ou de modifier des PR directement. Utilise le format de lien de comparaison ci-dessus.
            - Garde les changements minimaux et cohérents avec le style du dépôt. S’il n’y a pas de mises à jour de doc nécessaires, ne fais aucun changement et ne publie aucun commentaire.

            # Livrables en cas de mises à jour :
            - Commits poussés vers la branche de doc persistante pour le head de cette PR.
            - Un unique commentaire en langage naturel sur la PR d’origine qui inclut le lien de comparaison en ligne ci-dessus. Évite les doublons ; mets à jour un précédent commentaire du bot s’il existe.
            " --force --model "$MODEL" --output-format=text
  ```

  ```yaml auto-update-docs-deterministic.yml theme={null}
  name: Mettre à jour la doc

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
        - name: Récupérer le dépôt
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Installer le CLI Cursor
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configurer git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Générer les mises à jour de la doc (pas de commit/push/commentaire)
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Tu es en train d’exécuter dans un runner GitHub Actions.

            Le CLI GitHub est disponible sous `gh` et authentifié via `GH_TOKEN`. Git est disponible.

            IMPORTANT : Ne crée pas de branches, ne fais pas de commit, ne push pas et ne poste pas de commentaires sur la PR. Modifie uniquement les fichiers dans le répertoire de travail si nécessaire. Une étape ultérieure du workflow publiera les changements et commentera la PR.

            # Contexte :
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}

            # Objectif :
            - Mettre à jour la documentation du dépôt en fonction des changements incrémentaux introduits par cette PR.

            # Exigences :
            1) Détermine ce qui a changé dans la PR d’origine (utilise `gh pr diff` et l’historique git si nécessaire). Si une branche de doc persistante `${{ env.BRANCH_PREFIX }}/${{ github.head_ref }}` existe, tu peux l’utiliser comme point de référence en lecture seule pour comprendre les mises à jour précédentes.
            2) Mets à jour uniquement la doc pertinente en fonction de ces changements. Garde les modifications minimales et conformes au style du dépôt.
            3) Ne fais pas de commit, ne push pas, ne crée pas de branches et ne poste pas de commentaires sur la PR. Laisse l’arbre de travail avec uniquement les fichiers mis à jour ; une étape ultérieure publiera.

            # Entrées et conventions :
            - Utilise `gh pr diff` et l’historique git pour détecter les changements et cibler les modifications de la doc en conséquence.
            - Si aucune mise à jour de la doc n’est nécessaire, ne fais aucun changement et ne produis aucune sortie.

            # Livrables lorsque des mises à jour ont lieu :
            - Fichiers de doc modifiés dans le répertoire de travail uniquement (pas de commits/push/commentaires).
            " --force --model "$MODEL" --output-format=text

        - name: Publier la branche de doc
          id: publish_docs
          env:
            BRANCH_PREFIX: docs
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |
            echo "changes_published=false" >> "$GITHUB_OUTPUT"

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"

            # Assure-toi d’être sur une branche locale que l’on peut pousser
            git fetch origin --prune

            # Crée/bascule vers la branche persistante de doc, en conservant les changements actuels de l’arborescence de travail
            git checkout -B "$DOCS_BRANCH"

            # Indexer et détecter les changements
            git add -A
            if git diff --staged --quiet; then
              echo "Aucun changement de doc à publier. On saute le commit/push."
              exit 0
            fi

            COMMIT_MSG="docs: update for PR #${PR_NUMBER} (${HEAD_REF} @ $(git rev-parse --short HEAD))"
            git commit -m "$COMMIT_MSG"
            git push --set-upstream origin "$DOCS_BRANCH"

            echo "changes_published=true" >> "$GITHUB_OUTPUT"

        - name: Publier ou mettre à jour le commentaire de la PR
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
              echo "Cursor a mis à jour la branche de doc : \`${DOCS_BRANCH}\`"
              echo "Tu peux maintenant [voir le diff et créer rapidement une PR pour fusionner ces mises à jour de doc](${COMPARE_URL})."
              echo
              echo "_Ce commentaire sera mis à jour lors des exécutions suivantes au fur et à mesure que la PR évolue._"
              echo
              echo "<!-- auto-update-docs-split -->"
            } > "$COMMENT_FILE"

            # Si la modification du dernier commentaire du bot échoue (gh plus ancien), on revient à la création d’un nouveau commentaire
            if gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE" --edit-last; then
              echo "Commentaire de PR existant mis à jour."
            else
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              echo "Nouveau commentaire de PR publié."
            fi
  ```
</CodeGroup>

---

← Previous: [Traduire des clés](./traduire-des-cls.md) | [Index](./index.md) | Next: [GitHub Actions](./github-actions.md) →