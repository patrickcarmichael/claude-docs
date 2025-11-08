---
title: "Actualizar docs"
source: "https://docs.cursor.com/es/cli/cookbook/update-docs"
language: "es"
language_name: "Spanish"
---

# Actualizar docs
Source: https://docs.cursor.com/es/cli/cookbook/update-docs

Actualiza las docs de un repositorio usando Cursor CLI en GitHub Actions

Actualiza las docs usando Cursor CLI en GitHub Actions. Dos enfoques: autonomía total del agente o flujo de trabajo determinista con modificaciones de archivos solo por parte del agente.

<CodeGroup>
  ```yaml auto-update-docs.yml theme={null}
  name: Actualizar docs

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
        - name: Checkout del repositorio
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Instalar Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configurar git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Actualizar docs
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Estás operando en un runner de GitHub Actions.

            La GitHub CLI está disponible como `gh` y está autenticada con `GH_TOKEN`. Git está disponible. Tenés acceso de escritura al contenido del repositorio y podés comentar en pull requests, pero no debés crear ni editar PR.

            # Contexto:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}
            - Docs Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Objetivo:
            - Implementar un flujo de actualización de docs de extremo a extremo impulsado por cambios incrementales en el PR original.

            # Requisitos:
            1) Determinar qué cambió en el PR original y, si hubo múltiples pushes, calcular los diffs incrementales desde la última actualización de los docs.
            2) Actualizar solo los docs relevantes basados en esos cambios incrementales.
            3) Mantener la rama persistente de docs para esta head del PR usando el prefijo de rama de docs del Contexto. Creala si no existe; de lo contrario, actualizala y pusheá los cambios al origin.
            4) No tenés permiso para crear PR. En su lugar, publicá o actualizá un único comentario en lenguaje natural en el PR (1–2 oraciones) que explique brevemente las actualizaciones de los docs e incluya un enlace de comparación inline para crear rápido un PR

            # Entradas y convenciones:
            - Usá `gh pr diff` y el historial de git para detectar cambios y derivar rangos incrementales desde la última actualización de los docs.
            - No intentes crear ni editar PR directamente. Usá el formato de enlace de comparación anterior.
            - Mantené los cambios al mínimo y consistentes con el estilo del repo. Si no hacen falta actualizaciones de docs, no hagas cambios ni publiques comentarios.

            # Entregables cuando haya actualizaciones:
            - Commits pusheados a la rama persistente de docs para esta head del PR.
            - Un único comentario en lenguaje natural en el PR original que incluya el enlace de comparación inline anterior. Evitá publicar duplicados; actualizá un comentario previo del bot si existe.
            " --force --model "$MODEL" --output-format=text
  ```

  ```yaml auto-update-docs-deterministic.yml theme={null}
  name: Actualizar docs

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
        - name: Checkout del repositorio
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Instalar Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configurar git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Generar actualizaciones de docs (sin commit/push/comentario)
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Estás operando en un runner de GitHub Actions.

            La CLI de GitHub está disponible como `gh` y autenticada con `GH_TOKEN`. Git está disponible.

            IMPORTANTE: No crees ramas ni hagas commit, push o publiques comentarios en el PR. Solo modifica los archivos en el directorio de trabajo según sea necesario. Un paso posterior del workflow se encarga de publicar los cambios y comentar en el PR.

            # Contexto:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}

            # Objetivo:
            - Actualizar la documentación del repositorio según los cambios incrementales introducidos por este PR.

            # Requisitos:
            1) Determina qué cambió en el PR original (usa `gh pr diff` y el historial de git según sea necesario). Si existe una rama persistente de docs `${{ env.BRANCH_PREFIX }}/${{ github.head_ref }}`, podés usarla como referencia de solo lectura para entender actualizaciones previas.
            2) Actualizá solo la documentación relevante en función de esos cambios. Mantené las ediciones mínimas y consistentes con el estilo del repositorio.
            3) No hagas commit, push, crees ramas ni publiques comentarios en el PR. Dejá el árbol de trabajo solo con los archivos actualizados; un paso posterior publicará.

            # Entradas y convenciones:
            - Usá `gh pr diff` y el historial de git para detectar cambios y enfocar las ediciones de documentación en consecuencia.
            - Si no son necesarias actualizaciones de documentación, no hagas cambios ni generes salida.

            # Entregables cuando haya actualizaciones:
            - Archivos de documentación modificados solo en el directorio de trabajo (sin commits/push/comentarios).
            " --force --model "$MODEL" --output-format=text

        - name: Publicar rama de docs
          id: publish_docs
          env:
            BRANCH_PREFIX: docs
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |
            echo "changes_published=false" >> "$GITHUB_OUTPUT"

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"

            # Asegurate de que estemos en una rama local que podamos pushear
            git fetch origin --prune

            # Crear/cambiar a la rama persistente de docs, manteniendo los cambios actuales en el árbol de trabajo
            git checkout -B "$DOCS_BRANCH"

            # Preparar y detectar cambios
            git add -A
            if git diff --staged --quiet; then
              echo "No hay cambios de docs para publicar. Omitiendo commit/push."
              exit 0
            fi

            COMMIT_MSG="docs: update for PR #${PR_NUMBER} (${HEAD_REF} @ $(git rev-parse --short HEAD))"
            git commit -m "$COMMIT_MSG"
            git push --set-upstream origin "$DOCS_BRANCH"

            echo "changes_published=true" >> "$GITHUB_OUTPUT"

        - name: Publicar o actualizar comentario del PR
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
              echo "Cursor actualizó la rama de docs: \`${DOCS_BRANCH}\`"
              echo "Ahora podés [ver el diff y crear rápidamente un PR para mergear estas actualizaciones de docs](${COMPARE_URL})."
              echo
              echo "_Este comentario se actualizará en ejecuciones posteriores a medida que cambie el PR._"
              echo
              echo "<!-- auto-update-docs-split -->"
            } > "$COMMENT_FILE"

            # Si editar el último comentario del bot falla (gh más antiguo), recurrí a crear un comentario nuevo
            if gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE" --edit-last; then
              echo "Se actualizó el comentario existente del PR."
            else
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              echo "Se publicó un comentario nuevo en el PR."
            fi
  ```
</CodeGroup>

---

← Previous: [Traducir claves](./traducir-claves.md) | [Index](./index.md) | Next: [GitHub Actions](./github-actions.md) →