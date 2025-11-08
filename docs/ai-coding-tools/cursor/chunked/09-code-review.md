# Code Review

**Navigation:** [← Previous](./08-welcome.md) | [Index](./index.md) | [Next →](./10-large-codebases.md)

---

# Code Review
Source: https://docs.cursor.com/es/cli/cookbook/code-review

Crea un flujo de trabajo de GitHub Actions que use Cursor CLI para revisar automáticamente los pull requests y ofrecer comentarios

Este tutorial te muestra cómo configurar el code review usando Cursor CLI en GitHub Actions. El flujo de trabajo analizará los pull requests, identificará problemas y publicará comentarios como respuestas.

<Tip>
  Para la mayoría de usuarios, te recomendamos usar [Bugbot](/es/bugbot). Bugbot ofrece code review automatizado y gestionado sin necesidad de configuración. Este enfoque con la CLI es útil para explorar capacidades y para personalización avanzada.
</Tip>

<div className="space-y-4">
  <Expandable title="archivo completo del flujo de trabajo">
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
        # Omitir la revisión de código automatizada para PR en borrador
        if: github.event.pull_request.draft == false
        steps:
          - name: Checkout repository
            uses: actions/checkout@v4
            with:
              fetch-depth: 0
              ref: ${{ github.event.pull_request.head.sha }}

          - name: Install Cursor CLI
            run: |
              curl https://cursor.com/install -fsS | bash
              echo "$HOME/.cursor/bin" >> $GITHUB_PATH

          - name: Configure git identity
            run: |
              git config user.name "Cursor Agent"
              git config user.email "cursoragent@cursor.com"

          - name: Perform automated code review
            env:
              CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
              MODEL: gpt-5
              GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
              BLOCKING_REVIEW: ${{ vars.BLOCKING_REVIEW || 'false' }}
            run: |
              cursor-agent --force --model "$MODEL" --output-format=text --print 'Estás operando en un runner de GitHub Actions realizando una revisión de código automatizada. La CLI de gh está disponible y autenticada mediante GH_TOKEN. Puedes comentar en pull requests.

              Contexto:
              - Repo: ${{ github.repository }}
              - PR Number: ${{ github.event.pull_request.number }}
              - PR Head SHA: ${{ github.event.pull_request.head.sha }}
              - PR Base SHA: ${{ github.event.pull_request.base.sha }}
              - Blocking Review: ${{ env.BLOCKING_REVIEW }}

              Objetivos:
              1) Volver a revisar los comentarios existentes y responder resuelto cuando ya estén atendidos.
              2) Revisar el diff actual del PR y señalar solo problemas claros y de alta severidad.
              3) Dejar comentarios en línea muy breves (1‑2 frases) solo en las líneas modificadas y un breve resumen al final.

              Procedimiento:
              - Get existing comments: gh pr view --json comments
              - Get diff: gh pr diff
              - Get changed files with patches to compute inline positions: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/files --paginate --jq '.[] | {filename,patch}'
              - Calcular anclajes exactos en línea para cada problema (ruta de archivo + posición en el diff). Los comentarios DEBEN colocarse en línea en la línea modificada del diff, no como comentarios de nivel superior.
              - Detectar comentarios previos de nivel superior del tipo "sin problemas" escritos por este bot (coincidir cuerpos como: "✅ no issues", "No issues found", "LGTM").
              - Si la ejecución ACTUAL encuentra problemas y existe cualquier comentario previo de "sin problemas":
                - Preferir eliminarlos para evitar confusión:
                  - Try deleting top-level issue comments via: gh api -X DELETE repos/${{ github.repository }}/issues/comments/<comment_id>
                  - Si no es posible eliminarlos, minimízalos vía GraphQL (minimizeComment) o edítalos para anteponer "[Superseded by new findings]".
                - Si no es posible ni eliminar ni minimizar, responde a ese comentario: "⚠️ Superseded: issues were found in newer commits".
              - Si un problema reportado previamente parece estar corregido por cambios cercanos, responde: ✅ Este problema parece estar resuelto por los cambios recientes
              - Analizar SOLO:
                - Desreferencias de null/undefined
                - Fugas de recursos (archivos o conexiones sin cerrar)
                - Inyección (SQL/XSS)
                - Concurrencia/condiciones de carrera
                - Falta de manejo de errores en operaciones críticas
                - Errores lógicos evidentes con comportamiento incorrecto
                - Patrones claros anti‑rendimiento con impacto medible
                - Vulnerabilidades de seguridad definitivas
              - Evitar duplicados: omite si ya existe feedback similar en o cerca de las mismas líneas.

              Reglas para comentar:
              - Máximo 10 comentarios en línea en total; prioriza los problemas más críticos
              - Un problema por comentario; colócalo exactamente en la línea modificada
              - Todos los comentarios de problemas DEBEN ser en línea (anclados a un archivo y línea/posición en el diff del PR)
              - Tono natural, específico y accionable; no menciones que es automatizado ni el nivel de confianza
              - Usa emojis: 🚨 Crítico 🔒 Seguridad ⚡ Rendimiento ⚠️ Lógica ✅ Resuelto ✨ Mejora

              Envío:
              - Si NO hay problemas que reportar y ya existe un comentario de nivel superior indicando "sin problemas" (p. ej., "✅ no issues", "No issues found", "LGTM"), NO envíes otro comentario. Omite el envío para evitar redundancia.
              - Si NO hay problemas que reportar y NO existe un comentario previo de "sin problemas", envía un comentario de resumen breve indicando que no hay problemas.
              - Si HAY problemas que reportar y existe un comentario previo de "sin problemas", asegúrate de eliminar/minimizar/marcar como reemplazado el comentario previo antes de enviar la nueva revisión.
              - Si HAY problemas que reportar, envía UNA revisión que contenga SOLO comentarios en línea más un resumen conciso opcional. Usa la API de GitHub Reviews para asegurar que los comentarios sean en línea:
                - Build a JSON array of comments like: [{ "path": "<file>", "position": <diff_position>, "body": "..." }]
                - Submit via: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/reviews -f event=COMMENT -f body="$SUMMARY" -f comments='[$COMMENTS_JSON]'
              - NO uses: gh pr review --approve o --request-changes

              Comportamiento de bloqueo:
              - If BLOCKING_REVIEW is true and any 🚨 or 🔒 issues were posted: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
              - Otherwise: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
              - Always set CRITICAL_ISSUES_FOUND at the end
              '

          - name: Check blocking review results
            if: env.BLOCKING_REVIEW == 'true'
            run: |
              echo "Comprobando problemas críticos..."
              echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

              if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
                echo "❌ Se encontraron problemas críticos y la revisión bloqueante está habilitada. Fallando el flujo de trabajo."
                exit 1
              else
                echo "✅ No se encontraron problemas bloqueantes."
              fi
    ```
  </Expandable>

  <Frame>
    <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=31c7e4b54276532df8010645686ebbbc" alt="Revisión de código automatizada en acción con comentarios en línea en una pull request" data-og-width="2920" width="2920" data-og-height="1272" height="1272" data-path="images/cli/cookbook/code-review/comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=25e552210fa8425a10ff459bf4cd6006 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=234bf271bc595e763549c4f04d2e6fbb 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=b6f6d1444de7fe0197e3d35fa35955e8 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=300314314f5071b77f735460be33985f 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=10e4db857ee84c55d17222cef492611d 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=e65add70ffebfeb9ad05c9bb19a5f4e1 2500w" />
  </Frame>
</div>

<div id="configure-authentication">
  ## Configura la autenticación
</div>

[Configura tu API key y los secretos del repositorio](/es/cli/github-actions#authentication) para autenticar Cursor CLI en GitHub Actions.

<div id="set-up-agent-permissions">
  ## Configura los permisos del agente
</div>

Crea un archivo de configuración para controlar qué acciones puede realizar el agente. Esto evita operaciones no deseadas, como hacer push de código o crear pull requests.

Crea `.cursor/cli.json` en la raíz de tu repositorio:

```json  theme={null}
{
  "permissions": {
    "deny": [
      "Shell(git push)",
      "Shell(gh pr create)",
      "Escribir(**)"
    ]
  }
}
```

Esta configuración permite que el agente lea archivos y use la CLI de GitHub para comentarios, pero impide que haga cambios en tu repositorio. Consulta la [referencia de permisos](/es/cli/reference/permissions) para ver más opciones de configuración.

<div id="build-the-github-actions-workflow">
  ## Crea el flujo de trabajo de GitHub Actions
</div>

Ahora vamos a armar el flujo de trabajo paso a paso.

<div id="set-up-the-workflow-trigger">
  ### Configura el disparador del flujo de trabajo
</div>

Crea `.github/workflows/cursor-code-review.yml` y configúralo para ejecutarse en pull requests:

```yaml  theme={null}
name: Revisión de código de Cursor

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
  ### Revisa el repositorio
</div>

Agrega el paso de checkout para acceder al código del pull request:

```yaml  theme={null}
- name: Checkout del repositorio
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    ref: ${{ github.event.pull_request.head.sha }}
```

<div id="install-cursor-cli">
  ### Instala la CLI de Cursor
</div>

Agrega el paso de instalación de la CLI:

```yaml  theme={null}
- name: Instalar Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH
```

<div id="configure-the-review-agent">
  ### Configura el agente de revisión
</div>

Antes de implementar el paso de revisión completo, entendamos la anatomía de nuestro prompt de revisión. Esta sección describe cómo queremos que se comporte el agente:

**Objetivo**:
Queremos que el agente revise el diff del PR actual y marque solo problemas claros y de alta severidad, luego deje comentarios en línea muy cortos (1-2 frases) solo en líneas modificadas, con un breve resumen al final. Esto mantiene una buena relación señal-ruido.

**Formato**:
Queremos comentarios breves y directos. Usamos emojis para facilitar el escaneo de los comentarios y queremos un resumen de alto nivel de la revisión completa al final.

**Envío**:
Cuando termine la revisión, queremos que el agente incluya un comentario corto basado en lo encontrado durante la revisión. El agente debe enviar una sola revisión que contenga comentarios en línea más un resumen conciso.

**Casos límite**:
Necesitamos manejar:

* Comentarios existentes resueltos: el agente debe marcarlos como listos cuando se aborden
* Evitar duplicados: el agente debe omitir comentar si ya existe feedback similar en o cerca de las mismas líneas

**Prompt final**:
El prompt completo combina todos estos requisitos de comportamiento para crear feedback enfocado y accionable

Ahora implementemos el paso del agente de revisión:

```yaml  theme={null}
- name: Realizar revisión de código
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
    GH_TOKEN: ${{ github.token }}
  run: |
    cursor-agent --force --model "$MODEL" --output-format=text --print "Estás operando en un runner de GitHub Actions realizando una revisión de código automatizada. La CLI de gh está disponible y autenticada mediante GH_TOKEN. Podés comentar en pull requests.
    
    Contexto:
    - Repo: ${{ github.repository }}
    - PR Number: ${{ github.event.pull_request.number }}
    - PR Head SHA: ${{ github.event.pull_request.head.sha }}
    - PR Base SHA: ${{ github.event.pull_request.base.sha }}
    
    Objetivos:
    1) Volver a revisar los comentarios existentes y responder resuelto cuando estén atendidos
    2) Revisar el diff actual del PR y señalar solo problemas claros y de alta severidad
    3) Dejar comentarios en línea muy cortos (1-2 frases) solo en líneas modificadas y un resumen breve al final
    
    Procedimiento:
    - Obtener comentarios existentes: gh pr view --json comments
    - Obtener diff: gh pr diff
    - Si un problema reportado anteriormente parece solucionado por cambios cercanos, responder: ✅ Este problema parece estar resuelto por los cambios recientes
    - Evitar duplicados: omitir si ya existe feedback similar en o cerca de las mismas líneas
    
    Reglas para comentar:
    - Máximo 10 comentarios en línea en total; priorizar los problemas más críticos
    - Un problema por comentario; colocarlo en la línea exacta modificada
    - Tono natural, específico y accionable; no mencionar automatización ni alta confianza
    - Usar emojis: 🚨 Crítico 🔒 Seguridad ⚡ Rendimiento ⚠️ Lógica ✅ Resuelto ✨ Mejora
    
    Envío:
    - Enviar una sola revisión que contenga comentarios en línea más un resumen conciso
    - Usar solo: gh pr review --comment
    - No usar: gh pr review --approve o --request-changes"
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
  ## Prueba tu reviewer
</div>

Crea un pull request de prueba para verificar que el flujo de trabajo funcione y que el agente publique comentarios de revisión con emojis y feedback.

<Frame>
  <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=aa989eb5b7520e6718a48afd8daa70d9" alt="Pull request que muestra comentarios de revisión automatizados con emojis y feedback en línea en líneas específicas" data-og-width="1250" width="1250" data-og-height="704" height="704" data-path="images/cli/cookbook/code-review/github-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=9f2e324beb1cccb8052dcd0682323e47 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f08497ddb17921f4bb4638ef4eec3379 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=3c869c0ed8eb8b5743dd3821e57cd406 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=19e98ed953f4cc17b2c578ce543cf88d 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=4d9f47472af81254bd09b5f6234fc97f 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f3af19e3edd7f8bbbb77ba6566d8e183 2500w" />
</Frame>

<div id="next-steps">
  ## Próximos pasos
</div>

Ahora tienes un sistema de revisión de código automatizada en marcha. Considera estas mejoras:

* Configura flujos de trabajo adicionales para [corregir fallos de CI](/es/cli/cookbook/fix-ci)
* Configura distintos niveles de revisión para diferentes ramas
* Intégralo con el proceso de revisión de código existente de tu equipo
* Personaliza el comportamiento del agente para distintos tipos de archivos o directorios

<Expandable title="Avanzado: Revisiones bloqueantes">
  Puedes configurar el flujo de trabajo para que falle si se encuentran problemas críticos, evitando que se fusione el pull request hasta que se aborden.

  **Añadir comportamiento bloqueante al prompt**

  Primero, actualiza el paso de tu agente de revisión para incluir la variable de entorno `BLOCKING_REVIEW` y añade este comportamiento bloqueante al prompt:

  ```
  Comportamiento bloqueante:
  - Si BLOCKING_REVIEW es true y se publicaron problemas 🚨 o 🔒: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
  - De lo contrario: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
  - Establece siempre CRITICAL_ISSUES_FOUND al final
  ```

  **Añadir el paso de verificación bloqueante**

  Luego, añade este nuevo paso después del paso de revisión de código:

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



# Corregir fallos de CI
Source: https://docs.cursor.com/es/cli/cookbook/fix-ci

Corrige problemas de CI en un repositorio usando Cursor CLI en GitHub Actions

Corrige fallos de CI usando Cursor CLI en GitHub Actions. Este workflow analiza los fallos, aplica correcciones puntuales y crea una rama de fix con un enlace para crear un PR al instante.

Este workflow supervisa por nombre un workflow concreto. Actualiza la lista `workflows` para que coincida con el nombre real de tu workflow de CI.

<CodeGroup>
  ```yaml auto-fix-ci.yml theme={null}
  name: Fix CI Failures

  on:
    workflow_run:
      workflows: [Test]
      types: [completed]

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    attempt-fix:
      if: >-
        ${{ github.event.workflow_run.conclusion == 'failure' && github.event.workflow_run.name != 'Fix CI Failures' }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Fix CI failure
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: ci-fix
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - Workflow Run ID: ${{ github.event.workflow_run.id }}
            - Workflow Run URL: ${{ github.event.workflow_run.html_url }}
            - Fix Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Implement an end-to-end CI fix flow driven by the failing PR, creating a separate persistent fix branch and proposing a quick-create PR back into the original PR's branch.

            # Requirements:
            1) Identify the PR associated with the failed workflow run and determine its base and head branches. Let HEAD_REF be the PR's head branch (the contributor/origin branch).
            2) Maintain a persistent fix branch for this PR head using the Fix Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            3) Attempt to resolve the CI failure by making minimal, targeted edits consistent with the repo's style. Keep changes scoped and safe.
            4) You do NOT have permission to create PRs. Instead, post or update a single natural-language PR comment (1–2 sentences) that briefly explains the CI fix and includes an inline compare link to quick-create a PR.

            # Inputs and conventions:
            - Use `gh api`, `gh run view`, `gh pr view`, `gh pr diff`, `gh pr list`, `gh run download`, and git commands as needed to discover the failing PR and branches.
            - Avoid duplicate comments; if a previous bot comment exists, update it instead of posting a new one.
            - If no actionable fix is possible, make no changes and post no comment.

            # Deliverables when updates occur:
            - Pushed commits to the persistent fix branch for this PR head.
            - A single natural-language PR comment on the original PR that includes the inline compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Auditoría de secretos
Source: https://docs.cursor.com/es/cli/cookbook/secret-audit

Audita los secretos de un repositorio usando Cursor CLI en GitHub Actions

Audita tu repo para detectar vulnerabilidades de seguridad y exposición de secretos usando Cursor CLI. Este workflow busca posibles secretos, detecta patrones de workflow riesgosos y propone correcciones de seguridad.

<CodeGroup>
  ```yaml auto-secret-audit.yml theme={null}
  name: Secrets Audit

  on:
    schedule:
      - cron: "0 4 * * *"
    workflow_dispatch:

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    secrets-audit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Scan and propose hardening
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: audit
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
             - Hardening Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Perform a repository secrets exposure and workflow hardening audit on a schedule, and propose minimal safe fixes.

            # Requirements:
            1) Scan for potential secrets in tracked files and recent history; support allowlist patterns if present (e.g., .gitleaks.toml).
            2) Detect risky workflow patterns: unpinned actions, overbroad permissions, unsafe pull_request_target usage, secrets in forked PR contexts, deprecated insecure commands, missing permissions blocks.
            3) Maintain a persistent branch for this run using the Hardening Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            4) Propose minimal edits: redact literals where safe, add ignore rules, pin actions to SHA, reduce permissions, add guardrails to workflows, and add a SECURITY_LOG.md summarizing changes and remediation guidance.
            5) Push to origin.
            6) If there is at least one open PR in the repo, post or update a single natural-language comment (1–2 sentences) on the most recently updated open PR that briefly explains the hardening changes and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update an existing bot comment if present. If no changes or no open PRs, post nothing.

            # Inputs and conventions:
            - Use `gh` to list PRs and to post comments. Avoid duplicate comments.

            # Deliverables when updates occur:
             - Pushed commits to the persistent hardening branch for this run.
            - A single natural-language PR comment with the compare link above (only if an open PR exists).
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Traducir claves
Source: https://docs.cursor.com/es/cli/cookbook/translate-keys

Traduce claves de un repositorio usando Cursor CLI en GitHub Actions

Administra claves de traducción para internacionalización con Cursor CLI. Este workflow detecta claves i18n nuevas o modificadas en pull requests y completa las traducciones faltantes sin sobrescribir las existentes.

<CodeGroup>
  ```yaml auto-translate-keys.yml theme={null}
  name: Translate Keys

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    i18n:
      if: ${{ !startsWith(github.head_ref, 'translate/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Propose i18n updates
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: translate
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Head Ref: ${{ github.head_ref }}
            - Translate Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Detect i18n keys added or changed in the PR and fill only missing locales in message files. Never overwrite existing translations.

            # Requirements:
            1) Determine changed keys by inspecting the PR diff (source files and messages files).
            2) Compute missing keys per locale using the source/canonical locale as truth.
            3) Add entries only for missing keys. Preserve all existing values untouched.
            4) Validate JSON formatting and schemas.
            5) Maintain a persistent translate branch for this PR head using the Translate Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            6) Post or update a single PR comment on the original PR written in natural language (1–2 sentences) that briefly explains what was updated and why, and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update a previous bot comment if present.
            8) If no changes are necessary, make no commits and post no comment.

            # Inputs and conventions:
            - Use `gh pr diff` and git history to detect changes.

            # Deliverables when updates occur:
            - Pushed commits to the persistent translate branch for this PR head.
            - A single natural-language PR comment on the original PR with the compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



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



# GitHub Actions
Source: https://docs.cursor.com/es/cli/github-actions

Aprende a usar Cursor CLI en GitHub Actions y otros sistemas de integración continua

Usa Cursor CLI en GitHub Actions y otros sistemas CI/CD para automatizar tareas de desarrollo.

<div id="github-actions-integration">
  ## Integración con GitHub Actions
</div>

Configuración básica:

```yaml  theme={null}
- name: Instalar la CLI de Cursor
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Ejecutar Cursor Agent
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "Escribe tu prompt aquí" --model gpt-5
```

<div id="cookbook-examples">
  ## Ejemplos de cookbook
</div>

Mira nuestros ejemplos de cookbook para flujos de trabajo prácticos: [actualizar documentación](/es/cli/cookbook/update-docs) y [corregir problemas de CI](/es/cli/cookbook/fix-ci).

<div id="other-ci-systems">
  ## Otros sistemas de CI
</div>

Usa Cursor CLI en cualquier sistema de CI/CD con:

* **Ejecución de scripts de shell** (bash, zsh, etc.)
* **Variables de entorno** para configurar la clave de API
* **Conexión a Internet** para acceder a la API de Cursor

<div id="autonomy-levels">
  ## Niveles de autonomía
</div>

Elige el nivel de autonomía de tu agente:

<div id="full-autonomy-approach">
  ### Enfoque de autonomía total
</div>

Dale al agente control completo sobre operaciones de Git, llamadas a APIs e interacciones externas. Configuración más simple; requiere más confianza.

**Ejemplo:** En nuestro cookbook [Update Documentation](/es/cli/cookbook/update-docs), el primer flujo de trabajo permite que el agente:

* Analice los cambios del PR
* Cree y administre ramas de Git
* Haga commits y haga push de cambios
* Publique comentarios en pull requests
* Maneje todos los escenarios de error

```yaml  theme={null}
- name: Actualizar docs (autonomía total)
  run: |
    cursor-agent -p "Tienes acceso completo a git, la CLI de GitHub y a las operaciones de PR. 
    Ocúpate de todo el flujo de actualización de la documentación, incluidos los commits, los pushes y los comentarios en PR."
```

<div id="restricted-autonomy-approach">
  ### Enfoque de autonomía restringida
</div>

<Note>
  Recomendamos usar este enfoque con **restricciones basadas en permisos** para flujos de trabajo de CI en producción. Te da lo mejor de ambos mundos: el agente puede manejar de forma inteligente análisis complejos y modificaciones de archivos, mientras que las operaciones críticas siguen siendo deterministas y auditables.
</Note>

Limita las operaciones del agente y mueve los pasos críticos a etapas separadas del flujo de trabajo. Mejor control y previsibilidad.

**Ejemplo:** El segundo flujo de trabajo de este mismo cookbook restringe al agente únicamente a realizar modificaciones de archivos:

```yaml  theme={null}
- name: Generar actualizaciones de docs (restringido)
  run: |
    cursor-agent -p "IMPORTANTE: NO crees ramas, no hagas commit ni push, ni publiques comentarios en PR. 
    Modifica únicamente los archivos en el directorio de trabajo. Un paso posterior del flujo se encarga de la publicación."

- name: Publicar rama de docs (determinista)
  run: |
    # Operaciones deterministas de git gestionadas por CI
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: actualización para PR"
    git push origin "docs/${{ github.head_ref }}"

- name: Publicar comentario en PR (determinista)  
  run: |
    # Comentarios de PR deterministas gestionados por CI
    gh pr comment ${{ github.event.pull_request.number }} --body "Docs actualizados"
```

<div id="permission-based-restrictions">
  ### Restricciones basadas en permisos
</div>

Usa las [configuraciones de permisos](/es/cli/reference/permissions) para imponer restricciones a nivel de la CLI:

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
  ## Autenticación
</div>

<div id="generate-your-api-key">
  ### Genera tu clave de API
</div>

Primero, [genera una clave de API](/es/cli/reference/authentication#api-key-authentication) desde tu panel de Cursor.

<div id="configure-repository-secrets">
  ### Configura los secretos del repositorio
</div>

Guarda tu clave de API de Cursor de forma segura en tu repositorio:

1. Ve a tu repositorio de GitHub
2. Haz clic en **Settings** → **Secrets and variables** → **Actions**
3. Haz clic en **New repository secret**
4. Ponle el nombre `CURSOR_API_KEY`
5. Pega tu clave de API como valor
6. Haz clic en **Add secret**

<div id="use-in-workflows">
  ### Úsala en workflows
</div>

Configura tu variable de entorno `CURSOR_API_KEY`:

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```



# Uso de la CLI en modo headless
Source: https://docs.cursor.com/es/cli/headless

Aprende a escribir scripts con la CLI de Cursor para análisis de código automatizado, generación y modificación

Usa la CLI de Cursor en scripts y flujos de automatización para tareas de análisis, generación y refactorización de código.

<div id="how-it-works">
  ## Cómo funciona
</div>

Usa [print mode](/es/cli/using#non-interactive-mode) (`-p, --print`) para scripting y automatización no interactivos.

<div id="file-modification-in-scripts">
  ### Modificación de archivos en scripts
</div>

Combina `--print` con `--force` para modificar archivos desde scripts:

```bash  theme={null}

# Habilita modificaciones de archivos en modo de impresión
cursor-agent -p --force "Refactoriza este código para usar sintaxis moderna de ES6+"


# Sin --force, los cambios solo se proponen; no se aplican
cursor-agent -p "Añade comentarios JSDoc a este archivo"  # No modificará archivos


# Procesamiento por lotes con cambios reales en archivos
find src/ -name "*.js" | while read file; do
  cursor-agent -p --force "Añade comentarios JSDoc detallados a $file"
done
```

<Warning>
  La opción `--force` permite que el agente haga cambios directos en archivos sin pedir confirmación
</Warning>

<div id="setup">
  ## Configuración
</div>

Consulta [Instalación](/es/cli/installation) y [Autenticación](/es/cli/reference/authentication) para ver todos los detalles de configuración.

```bash  theme={null}

# Instalar la CLI de Cursor
curl https://cursor.com/install -fsS | bash


# Configurar la clave de API para scripts  
export CURSOR_API_KEY=tu_api_key_aquí
cursor-agent -p "Analiza este código"
```

<div id="example-scripts">
  ## Scripts de ejemplo
</div>

Usa distintos formatos de salida según las necesidades de cada script. Consulta [Formato de salida](/es/cli/reference/output-format) para más detalles.

<div id="searching-the-codebase">
  ### Búsqueda en el código
</div>

Usa `--output-format text` para respuestas legibles:

```bash  theme={null}
#!/bin/bash

# Pregunta simple sobre el código

cursor-agent -p --output-format text "¿Qué hace este código?"
```

<div id="automated-code-review">
  ### Revisión automática de código
</div>

Usa `--output-format json` para obtener un análisis estructurado:

```bash  theme={null}
#!/bin/bash

# simple-code-review.sh - Script básico de revisión de código

echo "Iniciando la revisión de código..."


# Revisar cambios recientes
cursor-agent -p --force --output-format text \
  "Revisa los cambios de código recientes y da feedback sobre:
  - Calidad y legibilidad del código  
  - Posibles errores o problemas
  - Consideraciones de seguridad
  - Cumplimiento de buenas prácticas

  Ofrece sugerencias específicas de mejora y escribe en review.txt"

if [ $? -eq 0 ]; then
  echo "✅ Revisión de código completada correctamente"
else
  echo "❌ Error en la revisión de código"
  exit 1
fi
```

<div id="real-time-progress-tracking">
  ### Seguimiento del progreso en tiempo real
</div>

Usa `--output-format stream-json` para hacer seguimiento del progreso en tiempo real:

```bash  theme={null}
#!/bin/bash

# stream-progress.sh - Seguimiento del progreso en tiempo real

echo "🚀 Iniciando el procesamiento del stream..."


# Seguimiento del progreso en tiempo real
accumulated_text=""
tool_count=0
start_time=$(date +%s)

cursor-agent -p --force --output-format stream-json \
  "Analiza esta estructura del proyecto y crea un informe de resumen en analysis.txt" | \
  while IFS= read -r line; do
    
    type=$(echo "$line" | jq -r '.type // empty')
    subtype=$(echo "$line" | jq -r '.subtype // empty')
    
    case "$type" in
      "system")
        if [ "$subtype" = "init" ]; then
          model=$(echo "$line" | jq -r '.model // "unknown"')
          echo "🤖 Usando el modelo: $model"
        fi
        ;;
        
      "assistant")
        # Acumular deltas de texto en streaming
        content=$(echo "$line" | jq -r '.message.content[0].text // empty')
        accumulated_text="$accumulated_text$content"
        
        # Mostrar progreso en tiempo real
        printf "\r📝 Generando: %d caracteres" ${#accumulated_text}
        ;;
        
      "tool_call")
        if [ "$subtype" = "started" ]; then
          tool_count=$((tool_count + 1))
          
          # Extraer información de la herramienta
          if echo "$line" | jq -e '.tool_call.writeToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.writeToolCall.args.path // "unknown"')
            echo -e "\n🔧 Herramienta #$tool_count: creando $path"
          elif echo "$line" | jq -e '.tool_call.readToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.readToolCall.args.path // "unknown"')
            echo -e "\n📖 Herramienta #$tool_count: leyendo $path"
          fi
          
        elif [ "$subtype" = "completed" ]; then
          # Extraer y mostrar los resultados de la herramienta
          if echo "$line" | jq -e '.tool_call.writeToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.linesCreated // 0')
            size=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.fileSize // 0')
            echo "   ✅ Se crearon $lines líneas ($size bytes)"
          elif echo "$line" | jq -e '.tool_call.readToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.readToolCall.result.success.totalLines // 0')
            echo "   ✅ Se leyeron $lines líneas"
          fi
        fi
        ;;
        
      "result")
        duration=$(echo "$line" | jq -r '.duration_ms // 0')
        end_time=$(date +%s)
        total_time=$((end_time - start_time))
        
        echo -e "\n\n🎯 Completado en ${duration} ms (${total_time} s en total)"
        echo "📊 Estadísticas finales: $tool_count herramientas, ${#accumulated_text} caracteres generados"
        ;;
    esac
  done
```



# Instalación
Source: https://docs.cursor.com/es/cli/installation

Instala y actualiza la CLI de Cursor

<div id="installation">
  ## Instalación
</div>

<div id="macos-linux-and-windows-wsl">
  ### macOS, Linux y Windows (WSL)
</div>

Instala la CLI de Cursor con un solo comando:

```bash  theme={null}
curl https://cursor.com/install -fsS | bash
```

<div id="verification">
  ### Verificación
</div>

Después de la instalación, confirma que Cursor CLI esté funcionando correctamente:

```bash  theme={null}
cursor-agent --version
```

<div id="post-installation-setup">
  ## Configuración posterior a la instalación
</div>

1. **Añade \~/.local/bin a tu PATH:**

   Para bash:

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

   Para zsh:

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

2. **Empieza a usar Cursor Agent:**
   ```bash  theme={null}
   cursor-agent
   ```

<div id="updates">
  ## Actualizaciones
</div>

De forma predeterminada, Cursor CLI intentará actualizarse automáticamente para que siempre tengas la versión más reciente.

Para actualizar manualmente Cursor CLI a la versión más reciente:

```bash  theme={null}
cursor-agent update

# o 
cursor-agent upgrade
```

Ambos comandos actualizarán Cursor Agent a la última versión.



# MCP
Source: https://docs.cursor.com/es/cli/mcp

Usa servidores MCP con cursor-agent para conectar herramientas y fuentes de datos externas

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="overview">
  ## Descripción general
</div>

La CLI de Cursor es compatible con servidores del [Model Context Protocol (MCP)](/es/context/mcp), lo que te permite conectar herramientas externas y fuentes de datos a `cursor-agent`. **MCP en la CLI usa la misma configuración que el editor**: cualquier servidor MCP que hayas configurado funcionará sin problemas en ambos.

<Card title="Aprende sobre MCP" icon="link" href="/es/context/mcp">
  ¿Eres nuevo en MCP? Lee la guía completa sobre configuración, autenticación y servidores disponibles
</Card>

<div id="cli-commands">
  ## Comandos de CLI
</div>

Usa el comando `cursor-agent mcp` para administrar servidores MCP:

<div id="list-configured-servers">
  ### Listar servidores configurados
</div>

Consulta todos los servidores MCP configurados y su estado actual:

```bash  theme={null}
cursor-agent mcp list
```

Esto muestra:

* Nombres e identificadores de servidores
* Estado de la conexión (conectado/desconectado)
* Origen de la configuración (del proyecto o global)
* Método de transporte (stdio, HTTP, SSE)

<div id="list-available-tools">
  ### Listar herramientas disponibles
</div>

Ver las herramientas que proporciona un servidor MCP específico:

```bash  theme={null}
cursor-agent mcp list-tools <id>
```

Esto muestra:

* Nombres y descripciones de herramientas
* Parámetros obligatorios y opcionales
* Tipos de parámetros y restricciones

<div id="login-to-mcp-server">
  ### Inicia sesión en el servidor MCP
</div>

Autentícate con un servidor MCP configurado en tu `mcp.json`:

```bash  theme={null}
cursor-agent mcp login <id>
```

<div id="disable-mcp-server">
  ### Deshabilitar el servidor MCP
</div>

Quita un servidor MCP de la lista local de aprobados:

```bash  theme={null}
cursor-agent mcp disable <identifier>
```

<div id="using-mcp-with-agent">
  ## Usar MCP con Agent
</div>

Una vez que tengas configurados los servidores MCP (consulta la [guía principal de MCP](/es/context/mcp) para la configuración), `cursor-agent` detecta y utiliza automáticamente las herramientas disponibles cuando sean relevantes para tus solicitudes.

```bash  theme={null}

# Verifica qué servidores MCP están disponibles
cursor-agent mcp list


# Mira qué herramientas ofrece un servidor específico
cursor-agent mcp list-tools playwright


# Usa cursor-agent: emplea herramientas MCP automáticamente cuando conviene
cursor-agent --prompt "Navega a google.com y toma una captura de la página de búsqueda"
```

La CLI sigue la misma prioridad de configuración que el editor (proyecto → global → anidada) y detecta automáticamente las configuraciones en los directorios superiores.

<div id="related">
  ## Relacionado
</div>

<CardGroup cols={2}>
  <Card title="Descripción general de MCP" icon="link" href="/es/context/mcp">
    Guía completa de MCP: instalación, configuración y autenticación
  </Card>

  <Card title="Herramientas MCP disponibles" icon="table" href="/es/tools">
    Explora servidores MCP ya listos que puedes usar
  </Card>
</CardGroup>



# Cursor CLI
Source: https://docs.cursor.com/es/cli/overview

Empieza con Cursor CLI para programar en tu terminal

Cursor CLI te permite interactuar con agentes de IA directamente desde tu terminal para escribir, revisar y modificar código. Ya sea que prefieras una interfaz de terminal interactiva o automatización con salida imprimible para scripts y pipelines de CI, la CLI ofrece una potente asistencia para programar justo donde trabajas.

```bash  theme={null}

# Instalación
curl https://cursor.com/install -fsS | bash


# Iniciar sesión interactiva
cursor-agent
```

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/cli-overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b323547dd61e985df8c0d6179c1492bd" autoPlay loop muted playsInline controls data-path="images/cli/cli-overview.mp4" />
</Frame>

<Info>
  Cursor CLI está en beta, ¡nos encantaría tu opinión!
</Info>

<div id="interactive-mode">
  ### Modo interactivo
</div>

Inicia una sesión conversacional con el agente para describir tus objetivos, revisar los cambios propuestos y aprobar comandos:

```bash  theme={null}

# Inicia una sesión interactiva
cursor-agent


# Empieza con un mensaje inicial
cursor-agent "refactoriza el módulo de auth para usar tokens JWT"
```

<div id="non-interactive-mode">
  ### Modo no interactivo
</div>

Usa el modo de impresión para escenarios no interactivos, como scripts, pipelines de CI o automatización:

```bash  theme={null}

# Ejecuta con un prompt y un modelo específicos
cursor-agent -p "find and fix performance issues" --model "gpt-5"


# Úsalo con los cambios de git incluidos para revisión
cursor-agent -p "review these changes for security issues" --output-format text
```

<div id="sessions">
  ### Sesiones
</div>

Retoma conversaciones anteriores para mantener el contexto a lo largo de varias interacciones:

```bash  theme={null}

# Listar todos los chats anteriores
cursor-agent ls


# Reanudar la conversación más reciente
cursor-agent resume


# Reanudar una conversación específica
cursor-agent --resume="chat-id-here"
```



# Autenticación
Source: https://docs.cursor.com/es/cli/reference/authentication

Autentica Cursor CLI con inicio de sesión en el navegador o claves de API

Cursor CLI admite dos métodos de autenticación: inicio de sesión en el navegador (recomendado) y claves de API.

<div id="browser-authentication-recommended">
  ## Autenticación en el navegador (recomendado)
</div>

Usa el flujo del navegador para la forma más sencilla de autenticarte:

```bash  theme={null}

# Inicia sesión usando el flujo del navegador
cursor-agent login


# Verifica el estado de la autenticación
cursor-agent status


# Cierra sesión y borra la autenticación almacenada
cursor-agent logout
```

El comando de inicio de sesión abrirá tu navegador predeterminado y te pedirá que inicies sesión con tu cuenta de Cursor. Una vez listo, tus credenciales se almacenarán de forma segura en tu equipo.

<div id="api-key-authentication">
  ## Autenticación con clave de API
</div>

Para automatización, scripts o entornos CI/CD, usa la autenticación con clave de API:

<div id="step-1-generate-an-api-key">
  ### Paso 1: Genera una clave de API
</div>

Genera una clave de API en tu panel de Cursor en Integrations > User API Keys.

<div id="step-2-set-the-api-key">
  ### Paso 2: Configura la clave de API
</div>

Podés proporcionar la clave de API de dos maneras:

**Opción 1: Variable de entorno (recomendado)**

```bash  theme={null}
export CURSOR_API_KEY=your_api_key_here
cursor-agent "implementa la autenticación de usuarios"
```

**Opción 2: Indicador de la línea de comandos**

```bash  theme={null}
cursor-agent --api-key your_api_key_here "implementar autenticación de usuario"
```

<div id="authentication-status">
  ## Estado de autenticación
</div>

Consulta tu estado de autenticación actual:

```bash  theme={null}
cursor-agent status
```

Este comando mostrará:

* Si estás autenticado
* La información de tu cuenta
* La configuración actual del endpoint

<div id="troubleshooting">
  ## Solución de problemas
</div>

* **Errores "Not authenticated":** Ejecuta `cursor-agent login` o asegúrate de que tu clave de API esté configurada correctamente
* **Errores de certificado SSL:** Usa la opción `--insecure` para entornos de desarrollo
* **Problemas con el endpoint:** Usa la opción `--endpoint` para especificar un endpoint de API personalizado



# Configuración
Source: https://docs.cursor.com/es/cli/reference/configuration

Referencia de configuración de la Agent CLI para cli-config.json

Configura la Agent CLI usando el archivo `cli-config.json`.

<div id="file-location">
  ## Ubicación del archivo
</div>

<div class="full-width-table">
  | Tipo     | Plataforma  | Ruta                                       |
  | :------- | :---------- | :----------------------------------------- |
  | Global   | macOS/Linux | `~/.cursor/cli-config.json`                |
  | Global   | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | Proyecto | Todas       | `<project>/.cursor/cli.json`               |
</div>

<Note>Solo los permisos pueden configurarse a nivel de proyecto. Todos los demás ajustes de la CLI deben configurarse globalmente.</Note>

Sobrescribir con variables de entorno:

* **`CURSOR_CONFIG_DIR`**: ruta de directorio personalizada
* **`XDG_CONFIG_HOME`** (Linux/BSD): usa `$XDG_CONFIG_HOME/cursor/cli-config.json`

<div id="schema">
  ## Esquema
</div>

<div id="required-fields">
  ### Campos obligatorios
</div>

<div class="full-width-table">
  | Campo               | Tipo      | Descripción                                                                       |
  | :------------------ | :-------- | :-------------------------------------------------------------------------------- |
  | `version`           | number    | Versión del esquema de configuración (actual: `1`)                                |
  | `editor.vimMode`    | boolean   | Activar keybindings de Vim (por defecto: `false`)                                 |
  | `permissions.allow` | string\[] | Operaciones permitidas (consulta [Permissions](/es/cli/reference/permissions))    |
  | `permissions.deny`  | string\[] | Operaciones no permitidas (consulta [Permissions](/es/cli/reference/permissions)) |
</div>

<div id="optional-fields">
  ### Campos opcionales
</div>

<div class="full-width-table">
  | Campo                    | Tipo    | Descripción                                            |
  | :----------------------- | :------ | :----------------------------------------------------- |
  | `model`                  | object  | Configuración del modelo seleccionado                  |
  | `hasChangedDefaultModel` | boolean | Indicador de override del modelo gestionado por la CLI |
</div>

<div id="examples">
  ## Ejemplos
</div>

<div id="minimal-config">
  ### Configuración mínima
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="enable-vim-mode">
  ### Habilitar el modo Vim
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="configure-permissions">
  ### Configurar permisos
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

Consulta [Permissions](/es/cli/reference/permissions) para conocer los tipos de permisos disponibles y ver ejemplos.

<div id="troubleshooting">
  ## Solución de problemas
</div>

**Errores de configuración**: Mueve el archivo a otro lado y reinicia:

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**Los cambios no persisten**: Asegúrate de que el JSON sea válido y de tener permisos de escritura. Algunos campos los gestiona la CLI y pueden sobrescribirse.

<div id="notes">
  ## Notas
</div>

* Formato JSON puro (sin comentarios)
* La CLI se autorrepara cuando faltan campos
* Los archivos dañados se respaldan como `.bad` y se vuelven a crear
* Las entradas de permisos deben coincidir exactamente con la cadena (consulta [Permisos](/es/cli/reference/permissions) para más detalles)



# Formato de salida
Source: https://docs.cursor.com/es/cli/reference/output-format

Esquema de salida para formatos de texto, JSON y stream-JSON

La CLI de Cursor Agent ofrece múltiples formatos de salida con la opción `--output-format` cuando se combina con `--print`. Estos formatos incluyen formatos estructurados para uso programático (`json`, `stream-json`) y un formato de texto simplificado para seguir el progreso de forma legible para humanos.

<Note>
  El `--output-format` predeterminado es `stream-json`. Esta opción solo es válida al imprimir (`--print`) o cuando se infiere el modo de impresión (stdout no TTY o stdin canalizado).
</Note>

<div id="json-format">
  ## Formato JSON
</div>

El formato de salida `json` emite un único objeto JSON (seguido de un salto de línea) cuando la ejecución se completa correctamente. No se emiten deltas ni eventos de herramientas; el texto se agrega en el resultado final.

En caso de error, el proceso termina con un código distinto de cero y escribe un mensaje de error en stderr. No se emite ningún objeto JSON bien formado en casos de error.

<div id="success-response">
  ### Respuesta exitosa
</div>

Cuando se completa correctamente, la CLI imprime un objeto JSON con la siguiente estructura:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "result": "<texto completo del asistente>",
  "session_id": "<uuid>",
  "request_id": "<id de la solicitud opcional>"
}
```

<div class="full-width-table">
  | Campo             | Descripción                                                                               |
  | ----------------- | ----------------------------------------------------------------------------------------- |
  | `type`            | Siempre `"result"` para resultados del terminal                                           |
  | `subtype`         | Siempre `"success"` para completaciones correctas                                         |
  | `is_error`        | Siempre `false` para respuestas correctas                                                 |
  | `duration_ms`     | Tiempo total de ejecución en milisegundos                                                 |
  | `duration_api_ms` | Tiempo de la solicitud a la API en milisegundos (actualmente igual a `duration_ms`)       |
  | `result`          | Texto completo de la respuesta del asistente (concatenación de todos los deltas de texto) |
  | `session_id`      | Identificador único de la sesión                                                          |
  | `request_id`      | Identificador opcional de la solicitud (puede omitirse)                                   |
</div>

<div id="stream-json-format">
  ## Formato JSON de streaming
</div>

El formato de salida `stream-json` emite JSON delimitado por saltos de línea (NDJSON). Cada línea contiene un único objeto JSON que representa un evento en tiempo real durante la ejecución.

El stream termina con un evento terminal `result` en caso de éxito. En caso de fallo, el proceso finaliza con un código distinto de cero y el stream puede terminar antes sin un evento terminal; se escribe un mensaje de error en stderr.

<div id="event-types">
  ### Tipos de eventos
</div>

<div id="system-initialization">
  #### Inicialización del sistema
</div>

Emitido una vez al inicio de cada sesión:

```json  theme={null}
{
  "type": "system",
  "subtype": "init",
  "apiKeySource": "env|flag|login",
  "cwd": "/ruta/absoluta",
  "session_id": "<uuid>",
  "model": "<nombre visible del modelo>",
  "permissionMode": "predeterminado"
}
```

<Note>
  En el futuro, podrían añadirse a este evento campos como `tools` y `mcp_servers`.
</Note>

<div id="user-message">
  #### Mensaje del usuario
</div>

Contiene el prompt que ingresó el usuario:

```json  theme={null}
{
  "type": "user",
  "message": {
    "role": "user",
    "content": [{ "type": "text", "text": "<prompt>" }]
  },
  "session_id": "<uuid>"
}
```

<div id="assistant-text-delta">
  #### Delta de texto del assistant
</div>

Se emite varias veces mientras el assistant genera su respuesta. Estos eventos contienen fragmentos de texto incrementales:

```json  theme={null}
{
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [{ "type": "text", "text": "<fragmento delta>" }]
  },
  "session_id": "<uuid>"
}
```

<Note>
  Concatena todos los valores de `message.content[].text` en orden para reconstruir la respuesta completa del asistente.
</Note>

<div id="tool-call-events">
  #### Eventos de llamada a herramientas
</div>

Las llamadas a herramientas se registran con eventos de inicio y finalización:

**Inicio de llamada a herramienta:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "started",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" }
    }
  },
  "session_id": "<uuid>"
}
```

**Llamada de herramienta completada:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "completed",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" },
      "result": {
        "success": {
          "content": "contenido del archivo...",
          "isEmpty": false,
          "exceededLimit": false,
          "totalLines": 54,
          "totalChars": 1254
        }
      }
    }
  },
  "session_id": "<uuid>"
}
```

<div id="tool-call-types">
  #### Tipos de llamadas de herramienta
</div>

**Herramienta de lectura de archivos:**

* **Iniciada**: `tool_call.readToolCall.args` contiene `{ "path": "file.txt" }`
* **Completada**: `tool_call.readToolCall.result.success` incluye metadatos y contenido del archivo

**Herramienta de escritura de archivos:**

* **Iniciada**: `tool_call.writeToolCall.args` contiene `{ "path": "file.txt", "fileText": "content...", "toolCallId": "id" }`
* **Completada**: `tool_call.writeToolCall.result.success` incluye `{ "path": "/absolute/path", "linesCreated": 19, "fileSize": 942 }`

**Otras herramientas:**

* Puede usar la estructura `tool_call.function` con `{ "name": "tool_name", "arguments": "..." }`

<div id="terminal-result">
  #### Resultado del terminal
</div>

El evento final emitido al completarse correctamente:

```json  theme={null}
{
  "type": "result",
  "subtype": "correcto",
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "is_error": false,
  "result": "<texto completo del asistente>",
  "session_id": "<uuid>",
  "request_id": "<id de la solicitud opcional>"
}
```

<div id="example-sequence">
  ### Secuencia de ejemplo
</div>

Aquí tienes una secuencia NDJSON representativa que muestra el flujo típico de eventos:

```json  theme={null}
{"type":"system","subtype":"init","apiKeySource":"login","cwd":"/Users/user/project","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","model":"Claude 4 Sonnet","permissionMode":"default"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"Lee el README.md y crea un resumen"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"Voy a "}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"leer el archivo README.md"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"},"result":{"success":{"content":"# Project\n\nThis is a sample project...","isEmpty":false,"exceededLimit":false,"totalLines":54,"totalChars":1254}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":" y crear un resumen"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README Summary\n\nThis project contains...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README Summary\n\nThis project contains...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"},"result":{"success":{"path":"/Users/user/project/summary.txt","linesCreated":19,"fileSize":942}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"result","subtype":"success","duration_ms":5234,"duration_api_ms":5234,"is_error":false,"result":"Voy a leer el archivo README.md y crear un resumen","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","request_id":"10e11780-df2f-45dc-a1ff-4540af32e9c0"}
```

<div id="text-format">
  ## Formato de texto
</div>

El formato de salida `text` ofrece un flujo simplificado y legible para humanos de las acciones del agente. En lugar de eventos JSON detallados, entrega descripciones de texto concisas sobre lo que el agente está haciendo en tiempo real.

Este formato sirve para monitorear el progreso del agente sin la carga de parsear datos estructurados, lo que lo hace ideal para logging, depuración o un seguimiento simple del progreso.

<div id="example-output">
  ### Ejemplo de salida
</div>

```
Leyó un archivo
Editó un archivo
Ejecutó un comando en la terminal
Creó un archivo nuevo
```

Cada acción aparece en una nueva línea a medida que el agente la ejecuta, ofreciendo feedback inmediato sobre el progreso del agente en la tarea.

<div id="implementation-notes">
  ## Notas de implementación
</div>

* Cada evento se emite como una única línea terminada en `\n`
* Los eventos `thinking` se suprimen en modo impresión y no aparecen en ninguno de los formatos de salida
* Se pueden agregar campos con el tiempo de forma retrocompatible (los consumidores deben ignorar los campos desconocidos)
* El formato de flujo (stream) ofrece actualizaciones en tiempo real, mientras que el formato JSON espera a que finalice para mostrar los resultados
* Concatena todos los deltas del mensaje de `assistant` para reconstruir la respuesta completa
* Los IDs de llamadas a herramientas pueden usarse para correlacionar los eventos de inicio y finalización
* Los IDs de sesión se mantienen consistentes durante una única ejecución del agente



# Parámetros
Source: https://docs.cursor.com/es/cli/reference/parameters

Referencia completa de comandos del CLI de Cursor Agent

<div id="global-options">
  ## Opciones globales
</div>

Las opciones globales se pueden usar con cualquier comando:

<div class="full-width-table">
  | Opción                     | Descripción                                                                                                                              |
  | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
  | `-v, --version`            | Muestra la versión                                                                                                                       |
  | `-a, --api-key <key>`      | Clave de API para autenticación (también se puede usar la variable de entorno `CURSOR_API_KEY`)                                          |
  | `-p, --print`              | Imprime las respuestas en la consola (para scripts o uso no interactivo). Tiene acceso a todas las herramientas, incluidas write y bash. |
  | `--output-format <format>` | Formato de salida (solo funciona con `--print`): `text`, `json` o `stream-json` (predeterminado: `stream-json`)                          |
  | `-b, --background`         | Inicia en modo en segundo plano (abre el selector del compositor al iniciar)                                                             |
  | `--fullscreen`             | Activa el modo de pantalla completa                                                                                                      |
  | `--resume [chatId]`        | Reanuda una sesión de chat                                                                                                               |
  | `-m, --model <model>`      | Modelo a utilizar                                                                                                                        |
  | `-f, --force`              | Fuerza permitir comandos salvo que se denieguen explícitamente                                                                           |
  | `-h, --help`               | Muestra la ayuda del comando                                                                                                             |
</div>

<div id="commands">
  ## Comandos
</div>

<div class="full-width-table">
  | Comando           | Descripción                                     | Uso                                            |
  | ----------------- | ----------------------------------------------- | ---------------------------------------------- |
  | `login`           | Autentícate con Cursor                          | `cursor-agent login`                           |
  | `logout`          | Cierra sesión y borra la autenticación guardada | `cursor-agent logout`                          |
  | `status`          | Consulta el estado de autenticación             | `cursor-agent status`                          |
  | `mcp`             | Administra servidores MCP                       | `cursor-agent mcp`                             |
  | `update\|upgrade` | Actualiza Cursor Agent a la última versión      | `cursor-agent update` o `cursor-agent upgrade` |
  | `ls`              | Reanuda una sesión de chat                      | `cursor-agent ls`                              |
  | `resume`          | Reanuda la última sesión de chat                | `cursor-agent resume`                          |
  | `help [command]`  | Muestra ayuda para el comando                   | `cursor-agent help [command]`                  |
</div>

<Note>
  Cuando no se especifica un comando, Cursor Agent se inicia en modo de chat interactivo de forma predeterminada.
</Note>

<div id="mcp">
  ## MCP
</div>

Administra servidores MCP configurados para Cursor Agent.

<div class="full-width-table">
  | Subcomando                | Descripción                                                                               | Uso                                        |
  | ------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------ |
  | `login <identifier>`      | Autentícate con un servidor MCP configurado en `.cursor/mcp.json`                         | `cursor-agent mcp login <identifier>`      |
  | `list`                    | Lista los servidores MCP configurados y su estado                                         | `cursor-agent mcp list`                    |
  | `list-tools <identifier>` | Lista las herramientas disponibles y los nombres de sus argumentos para un MCP específico | `cursor-agent mcp list-tools <identifier>` |
</div>

Todos los comandos de MCP admiten `-h, --help` para ver ayuda específica de cada comando.

<div id="arguments">
  ## Argumentos
</div>

Al iniciar en el modo chat (comportamiento predeterminado), podés proporcionar un prompt inicial:

**Argumentos:**

* `prompt` — Prompt inicial para el agente

<div id="getting-help">
  ## Obtener ayuda
</div>

Todos los comandos admiten la opción global `-h, --help` para mostrar la ayuda específica del comando.



# Permisos
Source: https://docs.cursor.com/es/cli/reference/permissions

Tipos de permisos para controlar el acceso del agente a archivos y comandos

Configura qué puede hacer el agente usando tokens de permisos en tu configuración de la CLI. Los permisos se definen en `~/.cursor/cli-config.json` (global) o `<project>/.cursor/cli.json` (por proyecto).

<div id="permission-types">
  ## Tipos de permisos
</div>

<div id="shell-commands">
  ### Comandos de shell
</div>

**Formato:** `Shell(commandBase)`

Controla el acceso a comandos de shell. `commandBase` es el primer token de la línea de comandos.

<div class="full-width-table">
  | Ejemplo      | Descripción                                                           |
  | ------------ | --------------------------------------------------------------------- |
  | `Shell(ls)`  | Permitir ejecutar comandos `ls`                                       |
  | `Shell(git)` | Permitir cualquier subcomando de `git`                                |
  | `Shell(npm)` | Permitir comandos del gestor de paquetes npm                          |
  | `Shell(rm)`  | Denegar eliminaciones destructivas de archivos (comúnmente en `deny`) |
</div>

<div id="file-reads">
  ### Lecturas de archivos
</div>

**Formato:** `Read(pathOrGlob)`

Controla el acceso de lectura a archivos y directorios. Admite patrones glob.

<div class="full-width-table">
  | Ejemplo             | Descripción                                            |
  | ------------------- | ------------------------------------------------------ |
  | `Read(src/**/*.ts)` | Permitir leer archivos TypeScript en `src`             |
  | `Read(**/*.md)`     | Permitir leer archivos markdown en cualquier ubicación |
  | `Read(.env*)`       | Denegar la lectura de archivos de entorno              |
  | `Read(/etc/passwd)` | Denegar la lectura de archivos del sistema             |
</div>

<div id="file-writes">
  ### Escrituras de archivos
</div>

**Formato:** `Write(pathOrGlob)`

Controla el acceso de escritura a archivos y directorios. Admite patrones glob. Al usar en modo print, se requiere `--force` para escribir archivos.

<div class="full-width-table">
  | Ejemplo               | Descripción                                            |
  | --------------------- | ------------------------------------------------------ |
  | `Write(src/**)`       | Permitir escribir en cualquier archivo dentro de `src` |
  | `Write(package.json)` | Permitir modificar `package.json`                      |
  | `Write(**/*.key)`     | Denegar la escritura de archivos de claves privadas    |
  | `Write(**/.env*)`     | Denegar la escritura de archivos de entorno            |
</div>

<div id="configuration">
  ## Configuración
</div>

Agrega permisos al objeto `permissions` en tu archivo de configuración de la CLI:

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
  ## Coincidencia de patrones
</div>

* Los patrones glob usan los comodines `**`, `*` y `?`
* Las rutas relativas se limitan al espacio de trabajo actual
* Las rutas absolutas pueden apuntar a archivos fuera del proyecto
* Las reglas de denegación tienen prioridad sobre las reglas de permiso



# Comandos de barra
Source: https://docs.cursor.com/es/cli/reference/slash-commands

Acciones rápidas disponibles en sesiones de Cursor CLI

<div class="full-width-table">
  | Command               | Description                                                            |
  | --------------------- | ---------------------------------------------------------------------- |
  | `/model <model>`      | Configura o muestra los modelos                                        |
  | `/auto-run [state]`   | Activa/desactiva auto-run (por defecto) o establece \[on\|off\|status] |
  | `/new-chat`           | Inicia una nueva sesión de chat                                        |
  | `/vim`                | Activa/desactiva teclas de Vim                                         |
  | `/help [command]`     | Muestra ayuda (/help \[cmd])                                           |
  | `/feedback <message>` | Comparte feedback con el equipo                                        |
  | `/resume <chat>`      | Reanuda un chat anterior por nombre de carpeta                         |
  | `/copy-req-id`        | Copia el último ID de la solicitud                                     |
  | `/logout`             | Cierra sesión en Cursor                                                |
  | `/quit`               | Salir                                                                  |
</div>



# Modo Shell
Source: https://docs.cursor.com/es/cli/shell-mode

Ejecuta comandos de shell directamente desde la CLI sin salir de tu conversación

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

El modo Shell ejecuta comandos directamente desde la CLI sin salir de tu conversación. Úsalo para comandos rápidos y no interactivos, con comprobaciones de seguridad y el output mostrado en la conversación.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

<div id="command-execution">
  ## Ejecución de comandos
</div>

Los comandos se ejecutan en tu shell de inicio de sesión (`$SHELL`) con el directorio de trabajo y el entorno del CLI. Encadena comandos para ejecutarlos en otros directorios:

```bash  theme={null}
cd subdir && npm test
```

<div id="output">
  ## Salida
</div>

<product_visual type="screenshot">
  Salida del comando que muestra un encabezado con el código de salida, la visualización de stdout/stderr y controles de truncado
</product_visual>

Las salidas extensas se truncan automáticamente y los procesos de larga ejecución expiran por tiempo de espera para mantener el rendimiento.

<div id="limitations">
  ## Limitaciones
</div>

* Los comandos se agotan después de 30 segundos
* No se admiten procesos de larga ejecución, servidores ni prompts interactivos
* Usa comandos cortos y no interactivos para obtener mejores resultados

<div id="permissions">
  ## Permisos
</div>

Los comandos se comprueban contra tus permisos y la configuración del equipo antes de ejecutarse. Consulta [Permisos](/es/cli/reference/permissions) para ver la configuración detallada.

<product_visual type="screenshot">
  Banner de decisión con opciones de aprobación: Ejecutar, Rechazar/Proponer, Añadir a la allowlist y Autoejecutar
</product_visual>

Las políticas de administrador pueden bloquear ciertos comandos, y los comandos con redirección no pueden añadirse a la allowlist en línea.

<div id="usage-guidelines">
  ## Guías de uso
</div>

Shell Mode funciona bien para verificar estados, hacer compilaciones rápidas, operar con archivos e inspeccionar el entorno.

Evita servidores de larga ejecución, aplicaciones interactivas y comandos que requieran entrada.

Cada comando se ejecuta de forma independiente; usa `cd <dir> && ...` para ejecutar comandos en otros directorios.

<div id="troubleshooting">
  ## Solución de problemas
</div>

* Si un comando se queda colgado, cancélalo con <Kbd>Ctrl+C</Kbd> y agrega flags no interactivos
* Cuando se te pidan permisos, apruébalos una vez o añade a la allowlist con <Kbd>Tab</Kbd>
* Si la salida se trunca, usa <Kbd>Ctrl+O</Kbd> para expandirla
* Para ejecutar en diferentes directorios, usa `cd <dir> && ...` ya que los cambios no persisten
* El modo Shell es compatible con zsh y bash según tu variable `$SHELL`

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="¿`cd` persiste entre ejecuciones?">
    No. Cada comando se ejecuta de forma independiente. Usa `cd <dir> && ...` para ejecutar comandos en diferentes directorios.
  </Accordion>

  <Accordion title="¿Puedo cambiar el tiempo de espera?">
    No. Los comandos están limitados a 30 segundos y no es configurable.
  </Accordion>

  <Accordion title="¿Dónde se configuran los permisos?">
    Los permisos se gestionan desde la CLI y la configuración del equipo. Usa el banner de decisiones para agregar comandos a la allowlist.
  </Accordion>

  <Accordion title="¿Cómo salgo del modo Shell?">
    Presiona <Kbd>Escape</Kbd> cuando el campo de entrada esté vacío, <Kbd>Backspace</Kbd>/<Kbd>Delete</Kbd> con la entrada vacía, o <Kbd>Ctrl+C</Kbd> para limpiar y salir.
  </Accordion>
</AccordionGroup>



# Usar Agent en la CLI
Source: https://docs.cursor.com/es/cli/using

Solicita, revisa e itera de forma efectiva con Cursor CLI

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="prompting">
  ## Prompting
</div>

Se recomienda declarar la intención con claridad para obtener los mejores resultados. Por ejemplo, podés usar el prompt "do not write any code" para asegurarte de que el agente no modifique ningún archivo. Esto suele ser útil al planificar tareas antes de implementarlas.

El agente actualmente cuenta con herramientas para operaciones con archivos, búsqueda y ejecución de comandos de shell. Se están incorporando más herramientas, similares a las del agente del IDE.

<div id="mcp">
  ## MCP
</div>

Agent es compatible con [MCP (Model Context Protocol)](/es/tools/mcp) para ampliar funcionalidades e integraciones. La CLI detecta automáticamente y respeta tu archivo de configuración `mcp.json`, habilitando los mismos servidores y herramientas MCP que configuraste para el IDE.

<div id="rules">
  ## Reglas
</div>

El agente de la CLI admite el mismo [sistema de reglas](/es/context/rules) que el IDE. Puedes crear reglas en el directorio `.cursor/rules` para darle contexto y guía al agente. Estas reglas se cargarán y aplicarán automáticamente según su configuración, lo que te permite personalizar el comportamiento del agente para distintas partes de tu proyecto o tipos de archivo específicos.

<Note>
  La CLI también lee `AGENTS.md` y `CLAUDE.md` en la raíz del proyecto (si están presentes) y los aplica como reglas junto con `.cursor/rules`.
</Note>

<div id="working-with-agent">
  ## Trabajar con Agent
</div>

<div id="navigation">
  ### Navegación
</div>

Podés acceder a mensajes anteriores con la flecha arriba (<Kbd>ArrowUp</Kbd>) y recorrerlos.

<div id="review">
  ### Revisión
</div>

Revisá los cambios con <Kbd>Cmd+R</Kbd>. Presioná <Kbd>i</Kbd> para agregar instrucciones de seguimiento. Usá <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd> para desplazarte y <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd> para cambiar de archivo.

<div id="selecting-context">
  ### Seleccionar contexto
</div>

Seleccioná archivos y carpetas para incluir en el contexto con <Kbd>@</Kbd>. Liberá espacio en la ventana de contexto ejecutando `/compress`. Consultá [Resumen](/es/agent/chat/summarization) para más detalles.

<div id="history">
  ## Historial
</div>

Continúa un hilo existente con `--resume [thread id]` para cargar el contexto previo.

Para reanudar la conversación más reciente, usa `cursor-agent resume`.

También podés ejecutar `cursor-agent ls` para ver una lista de conversaciones anteriores.

<div id="command-approval">
  ## Aprobación de comandos
</div>

Antes de ejecutar comandos en la terminal, la CLI te pedirá que apruebes (<Kbd>y</Kbd>) o rechaces (<Kbd>n</Kbd>) la ejecución.

<div id="non-interactive-mode">
  ## Modo no interactivo
</div>

Usa `-p` o `--print` para ejecutar Agent en modo no interactivo. Esto imprimirá la respuesta en la consola.

Con el modo no interactivo, puedes invocar Agent de forma no interactiva. Esto te permite integrarlo en scripts, pipelines de CI, etc.

Puedes combinarlo con `--output-format` para controlar el formato de la salida. Por ejemplo, usa `--output-format json` para obtener una salida estructurada que sea más fácil de analizar en scripts, o `--output-format text` para una salida de texto plano.

<Note>
  Cursor tiene acceso de escritura completo en modo no interactivo.
</Note>



# Atajos de teclado
Source: https://docs.cursor.com/es/configuration/kbd

Atajos de teclado y combinaciones de teclas en Cursor

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Descripción general de los atajos de teclado en Cursor. Mira todos los atajos de teclado presionando <Kbd>Cmd R</Kbd> y luego <Kbd>Cmd S</Kbd>, o abriendo la paleta de comandos con <Kbd>Cmd Shift P</Kbd> y buscando `Keyboard Shortcuts`.

Aprende más sobre los atajos de teclado en Cursor usando [Key Bindings for VS Code](https://code.visualstudio.com/docs/getstarted/keybindings) como referencia base para los keybindings de Cursor.

Todos los keybindings de Cursor, incluidas las funciones específicas de Cursor, se pueden reasignar en la configuración de Keyboard Shortcuts.

<div id="general">
  ## General
</div>

<div className="full-width-table equal-table-columns">
  | Atajo                  | Acción                                                              |
  | ---------------------- | ------------------------------------------------------------------- |
  | <Kbd>Cmd I</Kbd>       | Mostrar/ocultar panel lateral (a menos que esté asociado a un modo) |
  | <Kbd>Cmd L</Kbd>       | Mostrar/ocultar panel lateral (a menos que esté asociado a un modo) |
  | <Kbd>Cmd E</Kbd>       | Panel de control del agente en segundo plano                        |
  | <Kbd>Cmd .</Kbd>       | Menú de modos                                                       |
  | <Kbd>Cmd /</Kbd>       | Alternar entre modelos de IA                                        |
  | <Kbd>Cmd Shift J</Kbd> | Ajustes de Cursor                                                   |
  | <Kbd>Cmd ,</Kbd>       | Ajustes generales                                                   |
  | <Kbd>Cmd Shift P</Kbd> | Paleta de comandos                                                  |
</div>

<div id="chat">
  ## Chat
</div>

Atajos para la caja de entrada del chat.

<div className="full-width-table equal-table-columns">
  | Shortcut                                             | Action                                                     |
  | ---------------------------------------------------- | ---------------------------------------------------------- |
  | <Kbd>Return</Kbd>                                    | Nudge (predeterminado)                                     |
  | <Kbd>Ctrl Return</Kbd>                               | Poner el mensaje en cola                                   |
  | <Kbd>Cmd Return</Kbd> when typing                    | Forzar envío del mensaje                                   |
  | <Kbd>Cmd Shift Backspace</Kbd>                       | Cancelar la generación                                     |
  | <Kbd>Cmd Shift L</Kbd> with code selected            | Agregar el código seleccionado como contexto               |
  | <Kbd>Cmd V</Kbd> with code or log in clipboard       | Agregar el contenido del portapapeles como contexto        |
  | <Kbd>Cmd Shift V</Kbd> with code or log in clipboard | Agregar el contenido del portapapeles a la caja de entrada |
  | <Kbd>Cmd Return</Kbd> with suggested changes         | Aceptar todos los cambios                                  |
  | <Kbd>Cmd Backspace</Kbd>                             | Rechazar todos los cambios                                 |
  | <Kbd>Tab</Kbd>                                       | Pasar al siguiente mensaje                                 |
  | <Kbd>Shift Tab</Kbd>                                 | Volver al mensaje anterior                                 |
  | <Kbd>Cmd Opt /</Kbd>                                 | Alternar modelo                                            |
  | <Kbd>Cmd N</Kbd> / <Kbd>Cmd R</Kbd>                  | Nuevo chat                                                 |
  | <Kbd>Cmd T</Kbd>                                     | Nueva pestaña de chat                                      |
  | <Kbd>Cmd \[</Kbd>                                    | Chat anterior                                              |
  | <Kbd>Cmd ]</Kbd>                                     | Siguiente chat                                             |
  | <Kbd>Cmd W</Kbd>                                     | Cerrar chat                                                |
  | <Kbd>Escape</Kbd>                                    | Quitar el foco del campo                                   |
</div>

<div id="inline-edit">
  ## Edición inline
</div>

<div className="full-width-table equal-table-columns">
  | Atajo                          | Acción                     |
  | ------------------------------ | -------------------------- |
  | <Kbd>Cmd K</Kbd>               | Abrir                      |
  | <Kbd>Cmd Shift K</Kbd>         | Alternar el foco del campo |
  | <Kbd>Return</Kbd>              | Enviar                     |
  | <Kbd>Cmd Shift Backspace</Kbd> | Cancelar                   |
  | <Kbd>Opt Return</Kbd>          | Hacer una pregunta rápida  |
</div>

<div id="code-selection-context">
  ## Selección de código y contexto
</div>

<div className="full-width-table equal-table-columns">
  | Atajo                                                 | Acción                                             |
  | ----------------------------------------------------- | -------------------------------------------------- |
  | <Kbd>@</Kbd>                                          | [símbolos @](/es/context/@-symbols/)               |
  | <Kbd>#</Kbd>                                          | Archivos                                           |
  | <Kbd>/</Kbd>                                          | Comandos rápidos                                   |
  | <Kbd>Cmd Shift L</Kbd>                                | Agregar selección al chat                          |
  | <Kbd>Cmd Shift K</Kbd>                                | Agregar selección a Edit                           |
  | <Kbd>Cmd L</Kbd>                                      | Agregar selección a un chat nuevo                  |
  | <Kbd>Cmd M</Kbd>                                      | Alternar estrategias de lectura de archivos        |
  | <Kbd>Cmd →</Kbd>                                      | Aceptar la siguiente palabra de la sugerencia      |
  | <Kbd>Cmd Return</Kbd>                                 | Buscar en la base de código dentro del chat        |
  | Select code, <Kbd>Cmd C</Kbd>, <Kbd>Cmd V</Kbd>       | Agregar código de referencia copiado como contexto |
  | Select code, <Kbd>Cmd C</Kbd>, <Kbd>Cmd Shift V</Kbd> | Agregar código copiado como contexto de texto      |
</div>

<div id="tab">
  ## Tab
</div>

<div className="full-width-table equal-table-columns">
  | Atajo            | Acción                       |
  | ---------------- | ---------------------------- |
  | <Kbd>Tab</Kbd>   | Aceptar sugerencia           |
  | <Kbd>Cmd →</Kbd> | Aceptar la siguiente palabra |
</div>

<div id="terminal">
  ## Terminal
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut              | Acción                                   |
  | --------------------- | ---------------------------------------- |
  | <Kbd>Cmd K</Kbd>      | Abrir la barra de solicitud del terminal |
  | <Kbd>Cmd Return</Kbd> | Ejecutar el comando generado             |
  | <Kbd>Escape</Kbd>     | Aceptar el comando                       |
</div>



# Comandos de shell
Source: https://docs.cursor.com/es/configuration/shell

Instala y usa los comandos de shell de Cursor

Cursor ofrece herramientas de línea de comandos para abrir archivos y carpetas desde tu terminal. Instala los comandos `cursor` y `code` para integrar Cursor en tu flujo de trabajo de desarrollo.

<div id="installing-cli-commands">
  ## Instalación de los comandos de la CLI
</div>

Instala los comandos de la CLI desde la Command Palette:

1. Abre la Command Palette (Cmd/Ctrl + P)
2. Escribe "Install" para filtrar los comandos de instalación
3. Selecciona y ejecuta `Install 'cursor' to shell`
4. Repite y selecciona `Install 'code' to shell`

<product_visual type="screenshot">
  Command Palette mostrando opciones de instalación de la CLI
</product_visual>

<div id="using-the-cli-commands">
  ## Uso de los comandos de la CLI
</div>

Después de la instalación, usa cualquiera de estos comandos para abrir archivos o carpetas en Cursor:

```bash  theme={null}

# Usar el comando cursor
cursor ruta/al/archivo.js
cursor ruta/a/la/carpeta/


# Usar el comando code (compatible con VS Code)
code ruta/al/archivo.js
code ruta/a/la/carpeta/
```

<div id="command-options">
  ## Opciones de comandos
</div>

Ambos comandos admiten estas opciones:

* Abrir un archivo: `cursor file.js`
* Abrir una carpeta: `cursor ./my-project`
* Abrir varios elementos: `cursor file1.js file2.js folder1/`
* Abrir en una nueva ventana: `cursor -n` o `cursor --new-window`
* Esperar a que se cierre la ventana: `cursor -w` o `cursor --wait`

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="¿Cuál es la diferencia entre los comandos cursor y code?">
    Son idénticos. El comando `code` se incluye por compatibilidad con VS Code.
  </Accordion>

  <Accordion title="¿Necesito instalar ambos comandos?">
    No. Instala uno o ambos, según prefieras.
  </Accordion>

  <Accordion title="¿Dónde se instalan los comandos?">
    Los comandos se añaden al archivo de configuración de la shell predeterminada de tu sistema (p. ej., `.bashrc`, `.zshrc` o `.config/fish/config.fish`).
  </Accordion>
</AccordionGroup>



# Temas
Source: https://docs.cursor.com/es/configuration/themes

Personaliza la apariencia de Cursor

Cursor admite temas claros y oscuros para tu entorno de desarrollo. Cursor hereda las capacidades de tematización de VS Code: usa cualquier tema de VS Code, crea temas personalizados e instala extensiones de temas desde el marketplace.

<div id="changing-theme">
  ## Cambiar el tema
</div>

1. Abre la Paleta de comandos (Cmd/Ctrl + P)
2. Escribe "theme" para filtrar los comandos
3. Selecciona "Preferences: Color Theme"
4. Elige un tema

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de83bbba983509af2002e4dfafe703ff" alt="Menú de selección de tema en Cursor con los temas de color disponibles" data-og-width="3584" width="3584" data-og-height="2072" height="2072" data-path="images/config/themes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=85b365baa01a725becb482e69eed6292 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=46eb0bed7d0d98612968135d727ee838 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8629851793f4498e7639ee4347484c88 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ea75113e217cc84f99f8f6d63af34ade 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ec5b85b5a4464d2af801f92b317a7e31 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=54fc29efe263f9935ba3273675ced7be 2500w" />
</Frame>

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="¿Puedo usar mis temas de VS Code en Cursor?">
    ¡Sí! Cursor es compatible con los temas de VS Code. Instala cualquier tema del Marketplace de VS Code o copia tus archivos de temas personalizados.
  </Accordion>

  <Accordion title="¿Cómo creo un tema personalizado?">
    Crea temas personalizados igual que en VS Code. Usa "Developer: Generate Color Theme From Current Settings" para partir de tu configuración actual, o sigue la guía de creación de temas de VS Code.
  </Accordion>
</AccordionGroup>



# @Code
Source: https://docs.cursor.com/es/context/@-symbols/@-code

Haz referencia a fragmentos de código específicos en Cursor usando @Code

Haz referencia a secciones específicas de código usando el símbolo `@Code`. Esto te da un control más granular que [`@Files & Folders`](/es/context/@-symbols/@-files-and-folders), permitiéndote seleccionar fragmentos de código precisos en lugar de archivos completos.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fba3d385441084e243cd168eee8c9a9a" data-og-width="1850" width="1850" data-og-height="948" height="948" data-path="images/context/symbols/@-code.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6337ef4855301fdfef729012783d3cee 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ef348ae46e4a51ee298a6a5fa356eebd 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=40ec3857dd21120790037ea409fac80d 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=604bfeb6907e96da64b1f814681232c8 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=cee1a79d449a4d163f566a6013b69318 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d4bb99b85dfa5ad539e63c3670171abe 2500w" />
</Frame>



# @Cursor Rules
Source: https://docs.cursor.com/es/context/@-symbols/@-cursor-rules

Aplica reglas y pautas específicas del proyecto

El símbolo `@Cursor Rules` te da acceso a las [reglas del proyecto](/es/context/rules) y a las pautas que configuraste, para que puedas aplicarlas explícitamente a tu contexto.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e2f45682a0b471e5726cd5452ab6bceb" data-og-width="1518" width="1518" data-og-height="973" height="973" data-path="images/context/symbols/@-rules.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6e67889ef0390f9be3c557247469c95b 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1c22061fe8c8d000deeabbf404f1650d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a220fd7fbef492c2d523ed9e31324666 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44224ba38fd2a5460963b884c994d178 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=df766d5499d8b54ca4fa2211600515f6 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a06393ddd0d85711ad72d7b8991946a5 2500w" />
</Frame>



# @Files & Folders
Source: https://docs.cursor.com/es/context/@-symbols/@-files-and-folders

Referencia archivos y carpetas como contexto en Chat y Inline Edit

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="files">
  ## Archivos
</div>

Hace referencia a archivos completos en Chat e Inline Edit seleccionando `@Files & Folders` y luego el nombre del archivo para buscarlos. También podés arrastrar archivos desde la barra lateral directamente a Agent para agregarlos como contexto.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8d46d3c961a3e898fd12c0cc1e1c8dce" data-og-width="2227" width="2227" data-og-height="1414" height="1414" data-path="images/context/symbols/@-files-folders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a3a78c7a6d2311a31efb941c40fbe11b 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bfe1eff4516dce93f789e560e92f14ad 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=462239ebfd0181acfe36d2f937f32ca6 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1a64cd3cc0a07825c51d70c40dfe72fd 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=64ea129f283dd98fd9814820d6684a99 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b40e591d3e500f06eeb32fac49d4f90c 2500w" />
</Frame>

<div id="folders">
  ## Carpetas
</div>

Al hacer referencia a carpetas con `@Folders`, Cursor proporciona la ruta de la carpeta y un resumen de su contenido para ayudar a la IA a entender qué hay disponible.

<Tip>
  Después de seleccionar una carpeta, escribe “/” para navegar a niveles más profundos y ver todas las subcarpetas.
</Tip>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9a102e1c1cb7180c3ec6a1356273839a" data-og-width="2150" width="2150" data-og-height="1367" height="1367" data-path="images/context/symbols/@-folders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4b91de3b118c842aec8e1da04ca233d2 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fcba40013ff1349c28382151b52d5853 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=83cc5ac8db19a0d59de9a980c0ea10d7 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b87a80a369b62d48a2363a97a391de2 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29e93d39857f71ba7e00947e209514de 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=aa9b88463b43fa482c0654a0a0b362ca 2500w" />
</Frame>

<div id="full-folder-content">
  ### Contenido completo de la carpeta
</div>

Activa **Contenido completo de la carpeta** en la configuración. Cuando está activado, Cursor intenta incluir todos los archivos de la carpeta en el contexto.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ee37944a2e874a708b9d8281a063e580" data-og-width="1996" width="1996" data-og-height="296" height="296" data-path="images/context/symbols/folder-setting.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=09520107c0518601c58f099ed119adab 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=748aecb97c43066f0be03416f9ed6ed0 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fd7e7c816092c9eed3182382fa77ff8f 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=91baab4860e0f671196607f3c364b4d8 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d2450ee2fcd6d8c59ba2412fad11121 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f4690bdb099c27092b9ddb6143bd8068 2500w" />
</Frame>

Para carpetas grandes que exceden la ventana de contexto, aparece una vista de esquema con un tooltip que muestra cuántos archivos se incluyeron mientras Cursor gestiona el espacio de contexto disponible.

<Note>
  Usar contenido completo de carpeta con el [modo Max activado](/es/context/max-mode)
  aumenta significativamente los costos de la solicitud, ya que se consumen más tokens de entrada.
</Note>

<div id="context-management">
  ## Gestión del contexto
</div>

Los archivos y carpetas grandes se condensan automáticamente para ajustarse a los límites de contexto. Consulta [condensación de archivos y carpetas](/es/agent/chats/summarization#file--folder-condensation) para más detalles.



# @Git
Source: https://docs.cursor.com/es/context/@-symbols/@-git

Consulta cambios de Git y diferencias entre ramas

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=dba4c696d66e1274b96bf3261c8d927b" data-og-width="1658" width="1658" data-og-height="932" height="932" data-path="images/context/symbols/@-git.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=69bf90d13f034275fb78ab48e71d25ac 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e8c89a03ebdd5a1c1a576c8555380957 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5ec7309f9ec4364c4ac0d237a9977f23 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f2d82f1eb2be6275c8b91ae63e943ee7 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4e27a0a13a731fc0fe85a85a327f9884 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=aa1acf93e5e87b7a81d766a52601960d 2500w" />
</Frame>

* `@Commit`: Consulta los cambios del estado de trabajo actual respecto al último commit. Muestra todos los archivos modificados, agregados y eliminados que aún no se han confirmado.
* `@Branch`: Compara los cambios de tu rama actual con la rama main. Muestra todos los commits y cambios que están en tu rama pero no en main.



# @Link
Source: https://docs.cursor.com/es/context/@-symbols/@-link

Incluye contenido web pegando URLs

Cuando pegas una URL en Chat, Cursor la etiqueta automáticamente como `@Link` y obtiene el contenido para usarlo como contexto. Esto incluye compatibilidad con documentos PDF: Cursor extrae y analiza el texto de cualquier URL de PDF de acceso público.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d96b384a0480aba7981b6fbebee1fac8" data-og-width="1618" width="1618" data-og-height="1035" height="1035" data-path="images/context/symbols/@-link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d251326cc25b2835488b1f25b05f2c4f 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d1b64f393d89cfc547c6e12ae7a6adef 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d5a2aa41c6a6affea03379adac5e76c8 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e94e2c0610eafea625996386374e8898 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=404333e65fa1c98e2e92fd941d2e8b92 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=63d9a66571fde75678b6fa0d0cbac44f 2500w" />
</Frame>

<div id="unlink">
  ## Desvincular
</div>

Para usar una URL como texto sin formato sin recuperar su contenido:

* Haz clic en el enlace con etiqueta y selecciona `Desvincular`
* O pega mientras mantienes presionado `Shift` para evitar el etiquetado automático

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5eca9b93aa4c2ba4f8d0f6a97a34052f" data-og-width="1212" width="1212" data-og-height="408" height="408" data-path="images/context/symbols/@-link-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=be5f171437d0d3c79ded195c7a387741 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5ca29084e45c832b6aa9015fcd5cf680 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=eb394772d364e392ff794c43ed1fbfcc 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5df343df91b3bf4aed9edb32fc192059 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a35df3274c439984b2072eb758d05fb1 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a20f166b838435ade65084c844cc3c6a 2500w" />
</Frame>



# @Linter Errors
Source: https://docs.cursor.com/es/context/@-symbols/@-linter-errors

Accede y consulta errores de linting en tu codebase

El símbolo `@Linter Errors` captura automáticamente y aporta contexto sobre errores y advertencias de linting del archivo activo. [Agent](/es/agent/overview) puede ver errores de lint por defecto.

<Note>
  Para que se vean los errores del linter, necesitas tener instalado y
  configurado el language server adecuado para tu lenguaje de programación.
  Cursor detecta y usa automáticamente los language servers instalados, pero
  puede que necesites instalar extensiones o herramientas adicionales para
  lenguajes específicos.
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6ef34b3ae96a7d49695035cb5c3ac9f9" data-og-width="1590" width="1590" data-og-height="1017" height="1017" data-path="images/context/symbols/@-linter-errors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=13e682f26536e5cb104142bcc7becbeb 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=cf3947376ee2e17f83c08809b23e864c 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=13d026063f9bc5e61c78740fee8eebc5 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29c834609d2f549b295be53cdbf7eec6 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b2131adda5b89685d7d7a26ed218fee 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9cd3c3e34cbee0f73fe478024018539 2500w" />
</Frame>



# @Past Chats
Source: https://docs.cursor.com/es/context/@-symbols/@-past-chats

Incluye chats del historial en versión resumida

When working on complex tasks in [Chat](/es/chat), you might need to reference context or decisions from previous conversations. The `@Past Chats` symbol includes summarized versions of previous chats as context.

Particularly useful when:

* You have a long Chat session with important context to reference
* You're starting a new related task and want continuity
* You want to share reasoning or decisions from a previous session

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6839cf571e64e1ed10dd5dc270d4ac45" data-og-width="2340" width="2340" data-og-height="1485" height="1485" data-path="images/context/symbols/@-past-chats.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0278e6fdce8d8771ecd6f64faf5048db 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3a2d4722e90c1078c11fcd695993d84a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d46e21680b56820aef7a9baf34891e0 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f19f25e6988729059f40731378ce4fab 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=86f9457d09e7dd4578c8609fd3cff6b5 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8efb9e097f9e434d0b7f03cac9b02396 2500w" />
</Frame>



# @Recent Changes
Source: https://docs.cursor.com/es/context/@-symbols/@-recent-changes

Incluye código modificado recientemente como contexto

El símbolo `@Recent Changes` incluye cambios de código recientes como contexto en conversaciones con la IA.

* Los cambios se ordenan cronológicamente
* Da prioridad a los últimos 10 cambios
* Respeta la configuración de `.cursorignore`

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e6968afeeed9e790121d8280f63b670d" data-og-width="1556" width="1556" data-og-height="996" height="996" data-path="images/context/symbols/@-recent-changes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=beae76f109d8eb29788ab3c90f72b831 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c4e6ad386c30f9546e1485ca4c14c0f2 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7d80d31e720b167408cd308204fa666a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=868a93753377dcb2d6820c748b9b17d7 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e84e94c4fe64f9e4270fd72883a4962d 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=139ffc703716759bb8b8c35e57bd6dbf 2500w" />
</Frame>



# @Web
Source: https://docs.cursor.com/es/context/@-symbols/@-web

Buscar en la web información actualizada

Con `@Web`, Cursor busca en la web usando [exa.ai](https://exa.ai) para encontrar información al día y añadirla como contexto. También puede extraer contenido de archivos PDF a partir de enlaces directos.

<Note>
  La búsqueda en la web está deshabilitada de forma predeterminada. Actívala en Settings → Features → Web Search.
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=17621610c12478f27190b96db57ca8de" data-og-width="1700" width="1700" data-og-height="1085" height="1085" data-path="images/context/symbols/@-web.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1be39cb8bbbfa22f2341635e7c5fe6d0 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=40b6aac5bee79bb5656024077bee7ece 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9a8515d8c9c5624135665a9545de32db 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8c7b721901f8cb82d39458ed054ee946 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=255c56da352f6faff0d92cf24f7dabb2 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=22561389d116bcbe01f5a860c0097b27 2500w" />
</Frame>



# Descripción general
Source: https://docs.cursor.com/es/context/@-symbols/overview

Referencia código, archivos y documentación usando símbolos @

Navega las sugerencias con las teclas de flecha. Pulsa `Enter` para seleccionar. Si la sugerencia es una categoría como `Files`, las sugerencias se filtrarán para mostrar los elementos más relevantes dentro de esa categoría.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=98029d0ecb83175a496ef16ccb1c92d7" data-og-width="1230" width="1230" data-og-height="794" height="794" data-path="images/context/symbols/context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=edadefb46f31037df216bdc41ff65f0e 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a0e30bf50ab5525b72b23d5d9847c7f8 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=903ab32cc5460a6573deef144b445945 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8820522f1a505b3205c0ffc2a3f1a382 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b46b89fa6da137cea339ed94eb711b3c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2e9ff863747cbf6faa2b675d400a7f6e 2500w" />
</Frame>

Esta es la lista de todos los símbolos @ disponibles:

* [@Files](/es/context/@-symbols/@-files) - Hace referencia a archivos específicos de tu proyecto
* [@Folders](/es/context/@-symbols/@-folders) - Hace referencia a carpetas completas para aportar más contexto
* [@Code](/es/context/@-symbols/@-code) - Hace referencia a fragmentos de código o símbolos específicos de tu codebase
* [@Docs](/es/context/@-symbols/@-docs) - Accede a documentación y guías
* [@Git](/es/context/@-symbols/@-git) - Accede al historial y a los cambios de Git
* [@Past Chats](/es/context/@-symbols/@-past-chats) - Trabaja con sesiones del compositor resumidas
* [@Cursor Rules](/es/context/@-symbols/@-cursor-rules) - Trabaja con las reglas de Cursor
* [@Web](/es/context/@-symbols/@-web) - Hace referencia a recursos web externos y documentación
* [@Link (paste)](/es/context/@-symbols/@-link) - Crea enlaces a código o documentación específicos
* [@Recent Changes](/es/context/@-symbols/@-recent-changes) - Crea enlaces a código o documentación específicos
* [@Lint Errors](/es/context/@-symbols/@-lint-errors) - Hace referencia a errores de lint (solo [Chat](/es/chat/overview))
* [@Definitions](/es/context/@-symbols/@-definitions) - Busca definiciones de símbolos (solo [Inline Edit](/es/inline-edit/overview))
* [# Files](/es/context/@-symbols/pill-files) - Agrega archivos al contexto sin referenciarlos
* [/ Commands](/es/context/@-symbols/slash-commands) - Agrega archivos abiertos y activos al contexto



# #Files
Source: https://docs.cursor.com/es/context/@-symbols/pill-files

Selecciona archivos específicos usando el prefijo #

Usa `#` seguido del nombre de un archivo para centrarte en archivos específicos. Combínalo con `@` para un control de contexto más preciso.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=398736830d51713f6d6624461e6ef676" alt="selector de archivos con #" data-og-width="1999" width="1999" data-og-height="1271" height="1271" data-path="images/context/symbols/pill-files.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=33af09f18a1b7a5fe3ba0b4e93549071 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d319809654c16625c4de82f2aeee7c4c 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5caee0c1350068f46f863e9ca95c0d3f 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2e12a692efce4423fe0bd9b8a955f84a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=eeb6db065f3cc70e660c91e8e9821e3a 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b22bbb70e1c96f4b55e2edbf133733a9 2500w" />
</Frame>



# /command
Source: https://docs.cursor.com/es/context/@-symbols/slash-commands

Comandos rápidos para agregar archivos y controlar el contexto

El comando `/` te da acceso rápido a las pestañas abiertas del editor y te permite agregar varios archivos como contexto.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d3700f8210564e99807492fbcc4053e9" alt="contexto de comandos /" data-og-width="1714" width="1714" data-og-height="1094" height="1094" data-path="images/context/symbols/slash-command.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8c780db9f04819960d70c3bbd8a20d1f 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de3998b2f22ef72d254f77424e1e7d39 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7035008674181675bc50c9bc352499b0 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5b403646c8d1d9f6a1bc0c2f22fa8d2d 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=efbd3f3f46ced09844d39c0e99c81917 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=391cc3a09397088b71213476219a763b 2500w" />
</Frame>

<div id="commands">
  ## Comandos
</div>

* **`/Reset Context`**: Restablece el contexto al estado predeterminado
* **`/Generate Cursor Rules`**: Genera reglas para que Cursor las siga
* **`/Disable Iterate on Lints`**: No intentará corregir errores y advertencias del linter
* **`/Add Open Files to Context`**: Incluye todas las pestañas del editor que están abiertas actualmente
* **`/Add Active Files to Context`**: Incluye todas las pestañas del editor actualmente visibles (útil con vistas divididas)



# Indexación del codebase
Source: https://docs.cursor.com/es/context/codebase-indexing

Cómo Cursor aprende tu codebase para entenderla mejor

Cursor indexa tu codebase calculando embeddings para cada archivo. Esto mejora las respuestas generadas por IA sobre tu código. Cuando abres un proyecto, Cursor empieza a indexar automáticamente. Los archivos nuevos se indexan de forma incremental.
Revisa el estado de la indexación en: `Cursor Settings` > `Indexing & Docs`

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="Indicador de progreso de la indexación del codebase" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
</Frame>

<div id="configuration">
  ## Configuración
</div>

Cursor indexa todos los archivos excepto los que estén en [archivos de ignorados](/es/context/ignore-files) (p. ej., `.gitignore`, `.cursorignore`).

Haz clic en `Show Settings` para:

* Habilitar la indexación automática para repositorios nuevos
* Configurar qué archivos ignorar

<Tip>
  [Ignorar archivos de contenido grandes](/es/context/ignore-files) mejora la
  precisión de las respuestas.
</Tip>

<div id="view-indexed-files">
  ### Ver archivos indexados
</div>

Para ver las rutas de los archivos indexados: `Cursor Settings` > `Indexing & Docs` > `View included files`

Esto abre un archivo `.txt` con el listado de todos los archivos indexados.

<div id="multi-root-workspaces">
  ## Espacios de trabajo de múltiples raíces
</div>

Cursor admite [espacios de trabajo de múltiples raíces](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces), lo que te permite trabajar con varias bases de código:

* Todas las bases de código se indexan automáticamente
* El contexto de cada base de código está disponible para la IA
* `.cursor/rules` funciona en todas las carpetas

<div id="pr-search">
  ## Búsqueda de PR
</div>

La búsqueda de PR te ayuda a entender la evolución de tu base de código al hacer que los cambios históricos sean consultables y accesibles con IA.

<div id="how-it-works">
  ### Cómo funciona
</div>

Cursor **indexa automáticamente todos los PR mergeados** del historial de tu repositorio. Los resúmenes aparecen en los resultados de búsqueda semántica, con filtrado inteligente para priorizar los cambios recientes.

Agent puede **traer PR, commits, issues o ramas** al contexto usando `@[PR number]`, `@[commit hash]` o `@[branch name]`. Incluye comentarios de GitHub y revisiones de Bugbot cuando está conectado.

**Compatibilidad de la plataforma**: GitHub, GitHub Enterprise y Bitbucket. GitLab no está actualmente disponible.

<Note>
  Usuarios de GitHub Enterprise: La herramienta de fetch recurre a comandos de git debido a
  limitaciones de autenticación de VSCode.
</Note>

<div id="using-pr-search">
  ### Uso de la búsqueda de PR
</div>

Haz preguntas como "¿Cómo se implementan los servicios en otros PR?" y Agent traerá automáticamente PR relevantes al contexto para ofrecer respuestas completas basadas en el historial de tu repositorio.

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="Where can I see all indexed codebases?">
    Aún no existe una lista global. Revisa cada proyecto por separado abriéndolo en
    Cursor y consultando la configuración de Codebase Indexing.
  </Accordion>

  <Accordion title="How do I delete all indexed codebases?">
    Elimina tu cuenta de Cursor desde Settings para borrar todas las bases de código indexadas.
    Si no, elimina las bases de código individualmente desde la configuración de Codebase Indexing
    de cada proyecto.
  </Accordion>

  <Accordion title="How long are indexed codebases retained?">
    Las bases de código indexadas se eliminan tras 6 semanas de inactividad. Al reabrir el
    proyecto, se vuelve a indexar.
  </Accordion>

  <Accordion title="Is my source code stored on Cursor servers?">
    No. Cursor crea embeddings sin almacenar nombres de archivo ni código fuente. Los nombres de archivo se ofuscan y los fragmentos de código se cifran.

    Cuando Agent busca en la base de código, Cursor recupera los embeddings del servidor y descifra los fragmentos.
  </Accordion>
</AccordionGroup>



# Ignorar archivos
Source: https://docs.cursor.com/es/context/ignore-files

Control del acceso a archivos con .cursorignore y .cursorindexingignore

<div id="overview">
  ## Descripción general
</div>

Cursor lee e indexa el código de tu proyecto para habilitar sus funciones. Controla a qué directorios y archivos puede acceder Cursor usando un archivo `.cursorignore` en tu directorio raíz.

Cursor bloquea el acceso a los archivos listados en `.cursorignore` para:

* Indexación del código base
* Código accesible por [Tab](/es/tab/overview), [Agent](/es/agent/overview) y [Inline Edit](/es/inline-edit/overview)
* Código accesible mediante [referencias con el símbolo @](/es/context/@-symbols/overview)

<Warning>
  Las llamadas a herramientas iniciadas por Agent, como la terminal y los servidores MCP, no pueden bloquear
  el acceso al código gobernado por `.cursorignore`
</Warning>

<div id="why-ignore-files">
  ## ¿Por qué ignorar archivos?
</div>

**Seguridad**: Restringe el acceso a claves de API, credenciales y secretos. Aunque Cursor bloquea los archivos ignorados, no se puede garantizar una protección total debido a la imprevisibilidad de los LLM.

**Rendimiento**: En bases de código grandes o monorepos, excluye partes irrelevantes para un indexado más rápido y una detección de archivos más precisa.

<div id="global-ignore-files">
  ## Archivos globales de ignore
</div>

Configura patrones de ignore para todos los proyectos en la configuración de usuario y así excluir archivos sensibles sin tener que configurar cada proyecto por separado.

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d5bb9e6b18ca466ec69ddd1b216320c9" alt="Lista global de ignore de Cursor" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/settings/global-ignore.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ce566e71f1fcac6a85942f9fbb741889 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=c833cf55c470463ce31ae936ee122971 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=a3c3f6c6b40a9e91487237f0cf37cbca 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=03284fab1ddfadb64346dc912ea97048 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=5bd5b338808979f9fa42faa7df69d39a 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=676448c72358de369a119b34a8dcf9c5 2500w" />
</Frame>

Los patrones predeterminados incluyen:

* Archivos de entorno: `**/.env`, `**/.env.*`
* Credenciales: `**/credentials.json`, `**/secrets.json`
* Claves: `**/*.key`, `**/*.pem`, `**/id_rsa`

<div id="configuring-cursorignore">
  ## Configurar `.cursorignore`
</div>

Crea un archivo `.cursorignore` en tu directorio raíz usando la sintaxis de `.gitignore`.

<div id="pattern-examples">
  ### Ejemplos de patrones
</div>

```sh  theme={null}
config.json      # Archivo específico
dist/           # Directorio
*.log           # Extensión de archivo
**/logs         # Directorios anidados
!app/           # Quitar de la lista de ignorados (negación)
```

<div id="hierarchical-ignore">
  ### Ignorar jerárquico
</div>

Activa `Cursor Settings` > `Features` > `Editor` > `Hierarchical Cursor Ignore` para buscar en los directorios superiores archivos `.cursorignore`.

**Notas**: Los comentarios empiezan con `#`. Los patrones posteriores reemplazan a los anteriores. Los patrones son relativos a la ubicación del archivo.

<div id="limit-indexing-with-cursorindexingignore">
  ## Limita la indexación con `.cursorindexingignore`
</div>

Usa `.cursorindexingignore` para excluir archivos únicamente de la indexación. Estos archivos siguen estando disponibles para las funciones de IA, pero no aparecerán en las búsquedas del código.

<div id="files-ignored-by-default">
  ## Archivos ignorados de forma predeterminada
</div>

Cursor ignora automáticamente los archivos de `.gitignore` y la lista de ignorados predeterminada de abajo. Podés anular esto con el prefijo `!` en `.cursorignore`.

<Accordion title="Lista de ignorados predeterminada">
  Solo para indexación, estos archivos se ignoran además de los que estén en tu `.gitignore`, `.cursorignore` y `.cursorindexingignore`:

  ```sh  theme={null}
  package-lock.json
  pnpm-lock.yaml
  yarn.lock
  composer.lock
  Gemfile.lock
  bun.lockb
  .env*
  .git/
  .svn/
  .hg/
  *.lock
  *.bak
  *.tmp
  *.bin
  *.exe
  *.dll
  *.so
  *.lockb
  *.qwoff
  *.isl
  *.csv
  *.pdf
  *.doc
  *.doc
  *.xls
  *.xlsx
  *.ppt
  *.pptx
  *.odt
  *.ods
  *.odp
  *.odg
  *.odf
  *.sxw
  *.sxc
  *.sxi
  *.sxd
  *.sdc
  *.jpg
  *.jpeg
  *.png
  *.gif
  *.bmp
  *.tif
  *.mp3
  *.wav
  *.wma
  *.ogg
  *.flac
  *.aac
  *.mp4
  *.mov
  *.wmv
  *.flv
  *.avi
  *.zip
  *.tar
  *.gz
  *.7z
  *.rar
  *.tgz
  *.dmg
  *.iso
  *.cue
  *.mdf
  *.mds
  *.vcd
  *.toast
  *.img
  *.apk
  *.msi
  *.cab
  *.tar.gz
  *.tar.xz
  *.tar.bz2
  *.tar.lzma
  *.tar.Z
  *.tar.sz
  *.lzma
  *.ttf
  *.otf
  *.pak
  *.woff
  *.woff2
  *.eot
  *.webp
  *.vsix
  *.rmeta
  *.rlib
  *.parquet
  *.svg
  .egg-info/
  .venv/
  node_modules/
  __pycache__/
  .next/
  .nuxt/
  .cache/
  .sass-cache/
  .gradle/
  .DS_Store/
  .ipynb_checkpoints/
  .pytest_cache/
  .mypy_cache/
  .tox/
  .git/
  .hg/
  .svn/
  .bzr/
  .lock-wscript/
  .Python/
  .jupyter/
  .history/
  .yarn/
  .yarn-cache/
  .eslintcache/
  .parcel-cache/
  .cache-loader/
  .nyc_output/
  .node_repl_history/
  .pnp.js/
  .pnp/
  ```
</Accordion>

<div id="negation-pattern-limitations">
  ### Limitaciones de los patrones de negación
</div>

Al usar patrones de negación (con el prefijo `!`), no podés volver a incluir un archivo si un directorio padre está excluido mediante `*`.

```sh  theme={null}

# Ignora todos los archivos en la carpeta public
public/*


# ✅ Esto funciona, porque el archivo existe en el nivel superior
!public/index.html


# ❌ Esto no funciona: no se pueden volver a incluir archivos de directorios anidados
!public/assets/style.css
```

**Alternativa**: Excluí explícitamente los directorios anidados:

```sh  theme={null}
public/assets/*
!public/assets/style.css # Este archivo ahora es accesible
```

Por rendimiento, no se recorren los directorios excluidos, así que los patrones sobre archivos dentro de ellos no surten efecto.
Esto coincide con la implementación de .gitignore para patrones de negación en directorios anidados. Para más detalles, consulta la [documentación oficial de Git sobre los patrones de gitignore](https://git-scm.com/docs/gitignore).

<div id="troubleshooting">
  ## Solución de problemas
</div>

Proba patrones con `git check-ignore -v [file]`.



# Protocolo de Contexto del Modelo (MCP)
Source: https://docs.cursor.com/es/context/mcp

Conecta herramientas externas y fuentes de datos a Cursor con MCP

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="what-is-mcp">
  ## ¿Qué es MCP?
</div>

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) permite que Cursor se conecte con herramientas externas y fuentes de datos.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
</Frame>

<div id="why-use-mcp">
  ### ¿Por qué usar MCP?
</div>

MCP conecta Cursor con sistemas y datos externos. En lugar de explicar la estructura de tu proyecto una y otra vez, intégrate directamente con tus herramientas.

Escribe servidores MCP en cualquier lenguaje que pueda imprimir en `stdout` o exponer un endpoint HTTP: Python, JavaScript, Go, etc.

<div id="how-it-works">
  ### Cómo funciona
</div>

Los servidores MCP exponen capacidades a través del protocolo, conectando Cursor con herramientas externas y fuentes de datos.

Cursor admite tres métodos de transporte:

<div className="full-width-table">
  | Transporte                                                       | Entorno de ejecución | Implementación            | Usuarios        | Entrada                | Autenticación |
  | :--------------------------------------------------------------- | :------------------- | :------------------------ | :-------------- | :--------------------- | :------------ |
  | **<span className="whitespace-nowrap">`stdio`</span>**           | Local                | Gestionado por Cursor     | Un solo usuario | Comando de shell       | Manual        |
  | **<span className="whitespace-nowrap">`SSE`</span>**             | Local/Remoto         | Implementar como servidor | Varios usuarios | URL a un endpoint SSE  | OAuth         |
  | **<span className="whitespace-nowrap">`Streamable HTTP`</span>** | Local/Remoto         | Implementar como servidor | Varios usuarios | URL a un endpoint HTTP | OAuth         |
</div>

<div id="protocol-support">
  ### Compatibilidad con el protocolo
</div>

Cursor admite estas capacidades del protocolo MCP:

<div className="full-width-table">
  | Función         | Compatibilidad | Descripción                                                                                              |
  | :-------------- | :------------- | :------------------------------------------------------------------------------------------------------- |
  | **Tools**       | Compatible     | Funciones que el modelo de IA puede ejecutar                                                             |
  | **Prompts**     | Compatible     | Mensajes y flujos de trabajo con plantillas para usuaries                                                |
  | **Resources**   | Compatible     | Fuentes de datos estructuradas que se pueden leer y consultar                                            |
  | **Roots**       | Compatible     | Consultas iniciadas por el servidor sobre los límites de URI o del sistema de archivos en los que operar |
  | **Elicitation** | Compatible     | Solicitudes iniciadas por el servidor para obtener información adicional de les usuaries                 |
</div>

<div id="installing-mcp-servers">
  ## Instalación de servidores MCP
</div>

<div id="one-click-installation">
  ### Instalación con un clic
</div>

Instala servidores MCP de nuestra colección y autentícate con OAuth.

<Columns cols={2}>
  <Card title="Browse MCP Tools" icon="table" horizontal href="/es/tools">
    Explora los servidores MCP disponibles
  </Card>

  <Card title="Add to Cursor Button" icon="plus" horizontal href="/es/deeplinks">
    Crea un botón “Add to Cursor”
  </Card>
</Columns>

<div id="using-mcpjson">
  ### Uso de `mcp.json`
</div>

Configura servidores MCP personalizados con un archivo JSON:

<CodeGroup>
  ```json CLI Server - Node.js theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "npx",
        "args": ["-y", "mcp-server"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json CLI Server - Python theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "python",
        "args": ["mcp-server.py"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json Remote Server theme={null}
  // Servidor MCP vía HTTP o SSE: se ejecuta de forma remota
  {
    "mcpServers": {
      "server-name": {
        "url": "http://localhost:3000/mcp",
        "headers": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```
</CodeGroup>

<div id="stdio-server-configuration">
  ### Configuración del servidor STDIO
</div>

Para servidores STDIO (servidores locales de línea de comandos), configura estos campos en tu `mcp.json`:

<div className="full-width-table">
  | Campo       | Requerido | Descripción                                                                                                                          | Ejemplos                                  |
  | :---------- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------- |
  | **type**    | Sí        | Tipo de conexión del servidor                                                                                                        | `"stdio"`                                 |
  | **command** | Sí        | Comando para iniciar el ejecutable del servidor. Debe estar disponible en la variable PATH de tu sistema o incluir su ruta completa. | `"npx"`, `"node"`, `"python"`, `"docker"` |
  | **args**    | No        | Lista de argumentos pasados al comando                                                                                               | `["server.py", "--port", "3000"]`         |
  | **env**     | No        | Variables de entorno para el servidor                                                                                                | `{"API_KEY": "${input:api-key}"}`         |
  | **envFile** | No        | Ruta a un archivo de entorno para cargar más variables                                                                               | `".env"`, `"${workspaceFolder}/.env"`     |
</div>

<div id="using-the-extension-api">
  ### Uso de la API de extensión
</div>

Para registrar servidores MCP de forma programática, Cursor ofrece una API de extensión que permite una configuración dinámica sin modificar archivos `mcp.json`. Esto es especialmente útil en entornos empresariales y en flujos de configuración automatizados.

<Card title="Referencia de la API de extensión de MCP" icon="code" href="/es/context/mcp-extension-api">
  Aprende a registrar servidores MCP de forma programática usando `vscode.cursor.mcp.registerServer()`
</Card>

<div id="configuration-locations">
  ### Ubicaciones de configuración
</div>

<CardGroup cols={2}>
  <Card title="Configuración del proyecto" icon="folder-tree">
    Crea `.cursor/mcp.json` en tu proyecto para herramientas específicas del proyecto.
  </Card>

  <Card title="Configuración global" icon="globe">
    Crea `~/.cursor/mcp.json` en tu directorio personal para tener las herramientas disponibles en cualquier lugar.
  </Card>
</CardGroup>

<div id="config-interpolation">
  ### Interpolación de configuración
</div>

Usa variables en los valores de `mcp.json`. Cursor resuelve variables en estos campos: `command`, `args`, `env`, `url` y `headers`.

Sintaxis admitida:

* `${env:NAME}` variables de entorno
* `${userHome}` ruta a tu carpeta personal
* `${workspaceFolder}` raíz del proyecto (la carpeta que contiene `.cursor/mcp.json`)
* `${workspaceFolderBasename}` nombre de la carpeta raíz del proyecto
* `${pathSeparator}` y `${/}` separador de rutas del sistema operativo

Ejemplos

```json  theme={null}
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

```json  theme={null}
{
  "mcpServers": {
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    }
  }
}
```

<div id="authentication">
  ### Autenticación
</div>

Los servidores MCP usan variables de entorno para la autenticación. Pasa las claves de API y los tokens a través de la configuración.

Cursor admite OAuth para los servidores que lo requieran.

<div id="using-mcp-in-chat">
  ## Usar MCP en el chat
</div>

El Composer Agent utiliza automáticamente las herramientas MCP que aparecen en `Available Tools` cuando corresponde. Pide una herramienta específica por su nombre o describe lo que necesitas. Activa o desactiva herramientas desde Settings.

<div id="toggling-tools">
  ### Activar o desactivar herramientas
</div>

Activa o desactiva herramientas MCP directamente desde la interfaz del chat. Haz clic en el nombre de una herramienta en la lista para activarla o desactivarla. Las herramientas desactivadas no se cargarán en el contexto ni estarán disponibles para Agent.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-toggle.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fa3060f593cae3e5fb7c7d2f041a715" autoPlay loop muted playsInline controls data-path="images/context/mcp/tool-toggle.mp4" />
</Frame>

<div id="tool-approval">
  ### Aprobación de herramientas
</div>

De forma predeterminada, el agente solicita aprobación antes de usar herramientas MCP. Haz clic en la flecha junto al nombre de la herramienta para ver los argumentos.

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bf9b19d5f23abc65914f712185b3ec72" alt="" data-og-width="1212" width="1212" data-og-height="902" height="902" data-path="images/context/mcp/tool-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e3f900fad0b8f2a469460c70fa1dd1dc 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de2f90138de39d75d70c5800f13be93a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b9c616ce7a4080ea4088a0fdd0050c7c 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3f783e62a7a31957b8988edb97c139f9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10bf2c1dbfd5c2a03aa95334f53cd571 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=231c0e3cd60df5ad12455d5e8ef308d2 2500w" /></Frame>

<div id="auto-run">
  #### Auto-run
</div>

Activa Auto-run para que Agent use las herramientas MCP sin pedir confirmación. Funciona como comandos de terminal. Lee más sobre la configuración de Auto-run [aquí](/es/agent/tools#auto-run).

<div id="tool-response">
  ### Respuesta de la herramienta
</div>

Cursor muestra la respuesta en el chat con vistas desplegables de los argumentos y las respuestas:

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=30af3f35869e9a78781f455bdbc0e3b5" alt="" data-og-width="1212" width="1212" data-og-height="952" height="952" data-path="images/context/mcp/tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8821ac7bad00ad54a18abc614c2e3d5c 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9d55f089ad53a89da99b8ddd524f6de 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a107d68a1fb05ed43851548b34fb4496 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b409b4941c2fd783043770fad0bd6390 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2a331b5e2bb9be0b9659393157454c2e 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=585b769dfa2a5114b111eb901a969845 2500w" /></Frame>

<div id="images-as-context">
  ### Imágenes como contexto
</div>

Los servidores MCP pueden devolver imágenes —capturas de pantalla, diagramas, etc.—. Devuélvelas como cadenas codificadas en base64:

```js  theme={null}
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ base64 completo omitido para mejorar la legibilidad

server.tool("generate_image", async (params) => {
  return {
    content: [
      {
        type: "image",
        data: RED_CIRCLE_BASE64,
        mimeType: "image/jpeg",
      },
    ],
  };
});
```

Consulta este [servidor de ejemplo](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js) para ver los detalles de implementación. Cursor adjunta las imágenes devueltas al chat. Si el modelo admite imágenes, las analiza.

<div id="security-considerations">
  ## Consideraciones de seguridad
</div>

Al instalar servidores MCP, ten en cuenta estas prácticas de seguridad:

* **Verifica el origen**: Instala servidores MCP solo de desarrolladores y repositorios de confianza
* **Revisa los permisos**: Comprueba a qué datos y APIs tendrá acceso el servidor
* **Limita las claves de API**: Usa claves de API restringidas con los permisos mínimos necesarios
* **Audita el código**: Para integraciones críticas, revisa el código fuente del servidor

Recuerda que los servidores MCP pueden acceder a servicios externos y ejecutar código en tu nombre. Asegúrate de entender qué hace un servidor antes de instalarlo.

<div id="real-world-examples">
  ## Ejemplos del mundo real
</div>

Para ver ejemplos prácticos de MCP en acción, consulta nuestra [guía de desarrollo web](/es/guides/tutorials/web-development), donde mostramos cómo integrar Linear, Figma y herramientas del navegador en tu flujo de trabajo de desarrollo.

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="¿Para qué sirven los servidores MCP?">
    Los servidores MCP conectan Cursor con herramientas externas como Google Drive, Notion y
    otros servicios para incorporar documentos y requisitos a tu flujo de trabajo de código.
  </Accordion>

  {" "}

  <Accordion title="¿Cómo depuro problemas con servidores MCP?">
    Revisa los logs de MCP así: 1. Abre el panel Output en Cursor (<Kbd>Cmd+Shift+U</Kbd>) 2. Selecciona "MCP Logs" en el menú desplegable 3. Busca errores de conexión, problemas de autenticación o caídas del servidor. Los logs muestran la inicialización del servidor, llamadas a herramientas y mensajes de error.
  </Accordion>

  {" "}

  <Accordion title="¿Puedo desactivar temporalmente un servidor MCP?">
    ¡Sí! Activa o desactiva servidores sin quitarlos: 1. Abre Settings (<Kbd>Cmd+Shift+J</Kbd>) 2. Ve a Features → Model Context Protocol 3. Haz clic en el interruptor junto a cualquier servidor para habilitar o deshabilitar. Los servidores deshabilitados no se cargan ni aparecen en el chat. Esto es útil para depurar o reducir el ruido de herramientas.
  </Accordion>

  {" "}

  <Accordion title="¿Qué pasa si un servidor MCP se bloquea o supera el tiempo de espera?">
    Si un servidor MCP falla: - Cursor muestra un mensaje de error en el chat - La llamada a la herramienta se marca como fallida - Puedes reintentar la operación o revisar los logs para ver detalles - Otros servidores MCP siguen funcionando con normalidad. Cursor aísla las fallas de servidores para evitar que uno afecte a los demás.
  </Accordion>

  {" "}

  <Accordion title="¿Cómo actualizo un servidor MCP?">
    Para servidores basados en npm: 1. Quita el servidor desde Settings 2. Limpia la caché de npm: `npm cache clean --force` 3. Vuelve a agregar el servidor para obtener la versión más reciente. Para servidores personalizados, actualiza tus archivos locales y reinicia Cursor.
  </Accordion>

  <Accordion title="¿Puedo usar servidores MCP con datos sensibles?">
    Sí, pero sigue las mejores prácticas de seguridad: - Usa variables de entorno para secretos; nunca los hardcodees - Ejecuta servidores sensibles localmente con transporte `stdio` - Limita los permisos de las API keys al mínimo necesario - Revisa el código del servidor antes de conectarlo a sistemas sensibles - Considera ejecutar los servidores en entornos aislados
  </Accordion>
</AccordionGroup>



# Memories
Source: https://docs.cursor.com/es/context/memories



Las Memories son reglas generadas automáticamente a partir de tus conversaciones en Chat. Estas Memories se limitan a tu proyecto y mantienen el contexto entre sesiones.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/memories.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d10452508d962d7a9ec37de1c22245d1" alt="Memories en Cursor" controls data-path="images/context/rules/memories.mp4" />
</Frame>

<div id="how-memories-are-created">
  ## Cómo se crean los recuerdos
</div>

1. **Observación con sidecar**: Cursor usa un enfoque de sidecar en el que otro modelo observa tus conversaciones y extrae automáticamente recuerdos relevantes. Esto ocurre de forma pasiva en segundo plano mientras trabajas. Los recuerdos generados en segundo plano requieren tu aprobación antes de guardarse, lo que garantiza confianza y control sobre lo que se recuerda.

2. **Llamadas a herramientas**: Agent puede crear recuerdos directamente mediante llamadas a herramientas cuando le pides explícitamente que recuerde algo o cuando detecta información importante que debería conservarse para sesiones futuras.

<div id="manage-memories">
  ## Administrar memorias
</div>

Podés administrar las memorias desde Cursor Settings → Rules.



# Reglas
Source: https://docs.cursor.com/es/context/rules

Controla cómo se comporta el modelo Agent con instrucciones reutilizables y con alcance.

Las reglas proporcionan instrucciones a nivel de sistema para Agent e Inline Edit. Pensalas como contexto, preferencias o flujos de trabajo persistentes para tus proyectos.

Cursor admite cuatro tipos de reglas:

<CardGroup cols={2}>
  <Card title="Project Rules" icon="folder-tree">
    Almacenadas en `.cursor/rules`, con control de versiones y aplicadas al alcance de tu base de código.
  </Card>

  <Card title="User Rules" icon="user">
    Globales para tu entorno de Cursor. Definidas en la configuración y siempre aplicadas.
  </Card>

  <Card title="AGENTS.md" icon="robot">
    Instrucciones para Agent en formato Markdown. Alternativa simple a `.cursor/rules`.
  </Card>

  <Card title=".cursorrules (Legacy)" icon="clock-rotate-left">
    Aún compatibles, pero obsoletas. Usá Project Rules en su lugar.
  </Card>
</CardGroup>

<div id="how-rules-work">
  ## Cómo funcionan las reglas
</div>

Los modelos de lenguaje grandes no retienen memoria entre completions. Las reglas proporcionan contexto persistente y reutilizable a nivel de prompt.

Cuando se aplican, los contenidos de las reglas se incluyen al inicio del contexto del modelo. Esto le da a la IA una guía coherente para generar código, interpretar ediciones o ayudar con flujos de trabajo.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Regla aplicada en el contexto con el chat" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
</Frame>

<Info>
  Las reglas se aplican a [Chat](/es/chat/overview) y a [Inline Edit](/es/inline-edit/overview). Las reglas activas se muestran en la barra lateral del agente.
</Info>

<div id="project-rules">
  ## Reglas del proyecto
</div>

Las reglas del proyecto se encuentran en `.cursor/rules`. Cada regla es un archivo y está bajo control de versiones. Pueden limitarse mediante patrones de ruta, invocarse manualmente o incluirse según su relevancia. Los subdirectorios pueden incluir su propio directorio `.cursor/rules` con alcance limitado a esa carpeta.

Usa las reglas del proyecto para:

* Codificar conocimiento específico del dominio sobre tu base de código
* Automatizar flujos de trabajo o plantillas específicos del proyecto
* Estandarizar decisiones de estilo o de arquitectura

<div id="rule-anatomy">
  ### Anatomía de una regla
</div>

Cada archivo de regla está escrito en **MDC** (`.mdc`), un formato que admite metadatos y contenido. Controla cómo se aplican las reglas desde el menú desplegable de tipo, que modifica las propiedades `description`, `globs`, `alwaysApply`.

| <span class="no-wrap">Rule Type</span>         | Description                                                                       |
| :--------------------------------------------- | :-------------------------------------------------------------------------------- |
| <span class="no-wrap">`Always`</span>          | Siempre incluida en el contexto del modelo                                        |
| <span class="no-wrap">`Auto Attached`</span>   | Incluida cuando se referencian archivos que coinciden con un patrón glob          |
| <span class="no-wrap">`Agent Requested`</span> | Disponible para la IA, que decide si incluirla. Debe proporcionar una descripción |
| <span class="no-wrap">`Manual`</span>          | Solo se incluye cuando se menciona explícitamente usando `@ruleName`              |

```
---
description: Plantilla de servicio RPC
globs:
alwaysApply: false
---

- Usa nuestro patrón interno de RPC al definir servicios
- Usa siempre snake_case para los nombres de los servicios.

@service-template.ts
```

<div id="nested-rules">
  ### Reglas anidadas
</div>

Organiza las reglas colocándolas en directorios `.cursor/rules` a lo largo de tu proyecto. Las reglas anidadas se aplican automáticamente cuando se hace referencia a archivos dentro de su directorio.

```
project/
  .cursor/rules/        # Reglas para todo el proyecto
  backend/
    server/
      .cursor/rules/    # Reglas específicas del backend
  frontend/
    .cursor/rules/      # Reglas específicas del frontend
```

<div id="creating-a-rule">
  ### Crear una regla
</div>

Crea reglas con el comando `New Cursor Rule` o desde `Cursor Settings > Rules`. Esto crea un nuevo archivo de regla en `.cursor/rules`. Desde la configuración puedes ver todas las reglas y su estado.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=db8142786bbb7b7771ae0db8b2704b0b" alt="Comparación entre reglas concisas y extensas" data-og-width="6016" width="6016" data-og-height="3334" height="3334" data-path="images/context/rules/rule-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b6e9b8d6ca799d1af62957726b1cc52 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bfe1482ab9afc0995fe13371b26074b 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a847d915b3f106c42cba7cb1245bb138 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=356963b3607152f7ffe128cd1a2d050e 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b1e50d3721d42c691a434189729921c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d2081cf016d65053f1e517eb5734079e 2500w" />
</Frame>

<div id="generating-rules">
  ### Generar reglas
</div>

Genera reglas directamente en las conversaciones usando el comando `/Generate Cursor Rules`. Útil cuando ya definiste el comportamiento del agente y quieres reutilizarlo.

<Frame>
  <video src="https://www.cursor.com/changelog/049/generate-rules.mp4" controls>
    Tu navegador no admite la etiqueta de video.
  </video>
</Frame>

<div id="best-practices">
  ## Mejores prácticas
</div>

Las buenas reglas son concretas, accionables y bien acotadas.

* Mantén las reglas por debajo de 500 líneas
* Divide las reglas grandes en varias reglas componibles
* Proporciona ejemplos concretos o archivos de referencia
* Evita las indicaciones vagas. Escribe las reglas como documentación interna clara
* Reutiliza reglas cuando repitas prompts en el chat

<div id="examples">
  ## Ejemplos
</div>

<AccordionGroup>
  <Accordion title="Estándares para componentes de frontend y validación de API">
    Esta regla define estándares para componentes de frontend:

    Al trabajar en el directorio de components:

    * Usa siempre Tailwind para estilos
    * Usa Framer Motion para animaciones
    * Sigue las convenciones de nomenclatura de componentes

    Esta regla aplica validación para endpoints de API:

    En el directorio de API:

    * Usa zod para toda la validación
    * Define los tipos de retorno con esquemas de zod
    * Exporta los tipos generados a partir de los esquemas
  </Accordion>

  <Accordion title="Plantillas para servicios de Express y componentes de React">
    Esta regla proporciona una plantilla para servicios de Express:

    Usa esta plantilla al crear un servicio de Express:

    * Sigue los principios RESTful
    * Incluye middleware de manejo de errores
    * Configura un logging adecuado

    @express-service-template.ts

    Esta regla define la estructura de los componentes de React:

    Los componentes de React deben seguir este esquema:

    * Interfaz de Props al inicio
    * Componente como export nombrado
    * Estilos al final

    @component-template.tsx
  </Accordion>

  <Accordion title="Automatización de flujos de desarrollo y generación de documentación">
    Esta regla automatiza el análisis de la app:

    Cuando te pidan analizar la app:

    1. Ejecuta el servidor de desarrollo con `npm run dev`
    2. Obtén los logs de la consola
    3. Sugiere mejoras de rendimiento

    Esta regla ayuda a generar documentación:

    Ayuda a redactar documentación:

    * Extrayendo comentarios del código
    * Analizando README.md
    * Generando documentación en Markdown
  </Accordion>

  <Accordion title="Añadir una nueva configuración en Cursor">
    Primero crea una propiedad con toggle en `@reactiveStorageTypes.ts`.

    Añade el valor por defecto en `INIT_APPLICATION_USER_PERSISTENT_STORAGE` en `@reactiveStorageService.tsx`.

    Para funciones beta, agrega el toggle en `@settingsBetaTab.tsx`; de lo contrario, agrégalo en `@settingsGeneralTab.tsx`. Los toggles se pueden añadir como `<SettingsSubSection>` para checkboxes generales. Revisa el resto del archivo para ver ejemplos.

    ```
    <SettingsSubSection
    				label="Your feature name"
    				description="Your feature description"
    				value={
    					vsContext.reactiveStorageService.applicationUserPersistentStorage
    						.myNewProperty ?? false
    				}
    				onChange={(newVal) => {
    					vsContext.reactiveStorageService.setApplicationUserPersistentStorage(
    						'myNewProperty',
    						newVal
    					);
    				}}
    			/>
    ```

    Para usarlo en la app, importa reactiveStorageService y usa la propiedad:

    ```
    const flagIsEnabled = vsContext.reactiveStorageService.applicationUserPersistentStorage.myNewProperty
    ```
  </Accordion>
</AccordionGroup>

Hay muchos ejemplos disponibles de proveedores y frameworks. Las reglas aportadas por la comunidad se encuentran en colecciones y repositorios colaborativos en línea.

<div id="agentsmd">
  ## AGENTS.md
</div>

`AGENTS.md` es un archivo markdown simple para definir instrucciones de agentes. Ponlo en la raíz de tu proyecto como alternativa a `.cursor/rules` para casos de uso sencillos.

A diferencia de las Reglas del proyecto, `AGENTS.md` es un archivo markdown sin metadatos ni configuraciones complejas. Es perfecto para proyectos que necesitan instrucciones simples y fáciles de leer, sin la sobrecarga de reglas estructuradas.

```markdown  theme={null}

# Instrucciones del proyecto

## Estilo de código
- Usa TypeScript para todos los archivos nuevos
- Prefiere componentes funcionales en React
- Usa snake_case para las columnas de la base de datos

## Arquitectura
- Sigue el patrón de repositorio
- Mantén la lógica de negocio en las capas de servicio
```

<div id="user-rules">
  ## Reglas de usuario
</div>

Las reglas de usuario son preferencias globales definidas en **Cursor Settings → Rules** que se aplican a todos los proyectos. Son texto plano y van perfectas para establecer tu estilo de comunicación preferido o tus convenciones de código:

```
Respondé de forma concisa. Evitá la repetición innecesaria o el lenguaje de relleno.
```

<div id="cursorrules-legacy">
  ## `.cursorrules` (Legacy)
</div>

El archivo `.cursorrules` en la raíz de tu proyecto sigue siendo compatible, pero se va a deprecar. Te recomendamos migrar a Project Rules para tener más control, flexibilidad y visibilidad.

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="¿Por qué no se aplica mi regla?">
    Revisa el tipo de regla. Para `Agent Requested`, asegúrate de que haya una descripción definida. Para `Auto Attached`, asegúrate de que el patrón de archivos coincida con los archivos referenciados.
  </Accordion>

  {" "}

  <Accordion title="¿Pueden las reglas referenciar otras reglas o archivos?">
    Sí. Usa `@filename.ts` para incluir archivos en el contexto de tu regla.
  </Accordion>

  {" "}

  <Accordion title="¿Puedo crear una regla desde el chat?">
    Sí, genera reglas del proyecto desde el chat usando el comando `/Generate Cursor Rules`.
    Si Memories está habilitado, las memorias se generan automáticamente.
  </Accordion>

  <Accordion title="¿Las reglas afectan a Cursor Tab u otras funciones de IA?">
    No. Las reglas solo se aplican a Agent y a Inline Edit.
  </Accordion>
</AccordionGroup>



# Conceptos
Source: https://docs.cursor.com/es/get-started/concepts

Conoce las funciones clave que hacen que Cursor sea tan potente

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div className="flex flex-col gap-12">
  <Columns className="gap-4">
    <div>
      <h2 className="text-lg font-medium mb-2">
        <a href="/es/tab/overview" className="hover:text-primary transition-colors">
          Tab
        </a>
      </h2>

      <p className="text-sm">
        Autocompletado de código que predice modificaciones de varias líneas. Presiona Tab para aceptar
        sugerencias basadas en tu código actual y en los cambios recientes.
      </p>
    </div>

    <Frame>
      <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=5357dd01f6e7560c5ecb14367f4046f0" alt="Autocompletado con Tab" data-og-width="960" width="960" data-og-height="540" height="540" data-path="images/tab/tab-simple.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=9248a129c1f0ff309e522a26f7a2ca2b 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=894e4b876dfefd45d4b7259fb15a1789 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fd7441e84be11187ee8d0cbcdabd0222 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=b4e150615b4f0a82a347d4f47baa775b 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=f5db727f7b719651434684d1de0cbe90 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=cc1bd1fa532d878fe7e01700b28204f7 2500w" />
    </Frame>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/agent/overview" className="hover:text-primary transition-colors">
          Agent
        </a>
      </h3>

      <p className="text-sm">
        Una IA que puede leer y modificar código en varios archivos. Describe
        los cambios en lenguaje natural y Agent los ejecuta.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" alt="Modo Agent" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/background-agent" className="hover:text-primary transition-colors">
          Agente en segundo plano
        </a>
      </h3>

      <p className="text-sm">
        Ejecuta tareas de forma asíncrona mientras sigues trabajando. Puedes acceder
        desde el editor o mediante integraciones externas como Slack.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=07d084420ba9377c6a454b519a138e1a" alt="Agente en segundo plano" data-og-width="2452" width="2452" data-og-height="1380" height="1380" data-path="images/background-agent/cmd-e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=da4af3c5bedf87e80eb247c0f90b3e19 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8d2cb1c8514e6fbc965ebaeaa1ce05a7 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=50e2e022f3912f1e819ea59b128b57bc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5a0ad429a7894a70ba218609679e9e4f 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4140cf5142bb912b712bd76c828f2c9d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=67d608ee4c0a3c56647a3787a2d65661 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/inline-edit/overview" className="hover:text-primary transition-colors">
          Edición en línea
        </a>
      </h3>

      <p className="text-sm">
        Edita el código seleccionado con lenguaje natural. Presiona <Kbd>Cmd+K</Kbd> para
        describir los cambios y ver cómo se aplican ahí mismo.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=739ac6db99d802de30f55ddedc3da272" alt="Edición en línea" data-og-width="2960" width="2960" data-og-height="1657" height="1657" data-path="images/inline-edit/qq.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a58d16e85db7340c0e86cdcfd38ce67b 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a50013ce1196be4d688ff832c4fa026b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ce103df31faa30ed7e9eaa40d4f0cdd1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=0f20974d2d2013dba35bca117e84d68f 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7dbd27505e9ce9665576650fec7d77d4 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=0b88e0a5ce44c4f6f1aa7f25d6460244 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/agent/chats/tabs" className="hover:text-primary transition-colors">
          Chat
        </a>
      </h3>

      <p className="text-sm">
        Interfaz para conversaciones con IA. Admite múltiples pestañas, historial
        de conversaciones, checkpoints y exportación.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/context/rules" className="hover:text-primary transition-colors">
          Reglas
        </a>
      </h3>

      <p className="text-sm">
        Instrucciones personalizadas que definen el comportamiento de la IA. Configurá estándares de código,
        preferencias de frameworks y convenciones específicas del proyecto.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1be049cdaea7bca34d91a1b5bc29d55c" alt="Reglas de la IA" data-og-width="2318" width="2318" data-og-height="1304" height="1304" data-path="images/context/rules/mdc-editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=21331e8350c3fb52634bf1060f3e0e60 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=603820d50edcfe38aaa9b148d26e450e 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=795cf8aa5a5b177132b3cfa98a9a6174 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=49a57c4b1d0a6a70a0192feda2f4e754 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=369273301d1a35916926ca382ce81951 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=92fbb9585a42907596b983afd666dbf4 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/context/memories" className="hover:text-primary transition-colors">
          Memories
        </a>
      </h3>

      <p className="text-sm">
        Almacenamiento persistente del contexto del proyecto y de las decisiones tomadas en conversaciones anteriores. Se usa automáticamente como referencia en interacciones futuras.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/memories.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d10452508d962d7a9ec37de1c22245d1" autoPlay loop muted playsInline controls data-path="images/context/rules/memories.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/context/codebase-indexing" className="hover:text-primary transition-colors">
          Indexación del codebase
        </a>
      </h3>

      <p className="text-sm">
        Análisis semántico de tu codebase. Permite buscar código, encontrar referencias y ofrecer sugerencias con contexto.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="Indexación del codebase" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/context/mcp" className="hover:text-primary transition-colors">
          MCP
        </a>
      </h3>

      <p className="text-sm">
        Model Context Protocol para integrar herramientas externas. Se conecta con
        bases de datos, API y fuentes de documentación.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/guides/working-with-context" className="hover:text-primary transition-colors">
          Contexto
        </a>
      </h3>

      <p className="text-sm">
        Información que se le proporciona a los modelos de IA durante la generación de código. Incluye archivos,
        símbolos y el historial de la conversación.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=98029d0ecb83175a496ef16ccb1c92d7" alt="Administración de contexto" data-og-width="1230" width="1230" data-og-height="794" height="794" data-path="images/context/symbols/context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=edadefb46f31037df216bdc41ff65f0e 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a0e30bf50ab5525b72b23d5d9847c7f8 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=903ab32cc5460a6573deef144b445945 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8820522f1a505b3205c0ffc2a3f1a382 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b46b89fa6da137cea339ed94eb711b3c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2e9ff863747cbf6faa2b675d400a7f6e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/models" className="hover:text-primary transition-colors">
          Modelos
        </a>
      </h3>

      <p className="text-sm">
        Modelos de IA disponibles para generar código. Cada modelo tiene
        características distintas en velocidad y capacidad.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f039569ed0dc2ad7e02bb1b2e9cea71" alt="Selección de modelo" data-og-width="2256" width="2256" data-og-height="1248" height="1248" data-path="images/models/model-picker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=49c6a091945972253eb6e819593e45f0 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f9bddfb2e130789d8d51a3d1a4eeba94 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=db7273f399bb5decfed9d1b06f389df4 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=920fe98d4f99b5d7fddd47a14fb45699 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3b049686e5826263800b63299f4c19ca 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=72ddd56b4d3ea9b2efa4001a155566fd 2500w" />
      </Frame>
    </div>
  </Columns>
</div>



# Instalación
Source: https://docs.cursor.com/es/get-started/installation

Instala Cursor en tu computadora en solo unos minutos

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="download-cursor">
  ## Descargar Cursor
</div>

Empezar es fácil:

1. Ve a [cursor.com](https://cursor.com) y haz clic en “Download”
2. Ejecuta el instalador cuando termine de descargarse
3. Abre Cursor cuando finalice la instalación

<Info>
  ¿Necesitas una versión específica? Encuentra todas las plataformas y métodos de instalación en
  [cursor.com/downloads](https://cursor.com/downloads)
</Info>

<div id="first-time-setup">
  ## Configuración inicial
</div>

Cuando abras Cursor por primera vez, te vamos a guiar por una configuración rápida:

* Elegí atajos de teclado que te resulten familiares
* Elegí un tema que te guste
* Configurá tus preferencias del terminal

<Frame>
  <video controls width="100%">
    <source src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/cursor-onboarding.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=cda00fa83569cd85c6b7322c34f4843e" type="video/mp4" data-path="images/get-started/cursor-onboarding.mp4" />

    Tu navegador no admite la etiqueta de video.
  </video>
</Frame>

<Tip>
  Podés volver al asistente de configuración en cualquier momento presionando <Kbd>Cmd Shift P</Kbd>{" "}
  y buscando `Cursor: Start Onboarding`.
</Tip>

Leé más sobre [Atajos de teclado](/es/kbd), [Temas](/es/settings/themes) y [Comandos de shell](/es/settings/shell)

<CardGroup cols={3}>
  <Card title="Atajos de teclado" href="/es/configuration/kbd" arrow>
    Ver atajos de teclado
  </Card>

  <Card title="Temas" href="/es/configuration/themes" arrow>
    Elegir un tema en Cursor
  </Card>

  <Card title="Comandos de shell" href="/es/configuration/shell" arrow>
    Instalar comandos de shell
  </Card>
</CardGroup>

<div id="moving-from-another-editor">
  ## ¿Vienes de otro editor?
</div>

Si ya usas otro editor de código, te lo ponemos fácil para cambiarte:

<CardGroup cols={2}>
  <Card title="VS Code" href="/es/guides/migration/vscode" arrow>
    Importa directamente la configuración de VS Code
  </Card>

  <Card title="Jetbrains" href="/es/guides/migration/jetbrains" arrow>
    Guías de migración para JetBrains, Eclipse, Neovim y Sublime
  </Card>
</CardGroup>

Pronto habrá más guías de migración.

<div id="language-support">
  ## Compatibilidad con idiomas
</div>

Cursor funciona con todos los lenguajes de programación principales. Aquí van algunos populares con soporte de IA mejorado:

<CardGroup cols={4}>
  <Card
    title="TypeScript"
    href="/es/guides/languages/javascript"
    icon={<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none">
<rect width={512} height={512} fill="#3178c6" rx={50} />
<rect width={512} height={512} fill="#3178c6" rx={50} />
<path
fill="#fff"
fillRule="evenodd"
d="M316.939 407.424v50.061c8.138 4.172 17.763 7.3 28.875 9.386S368.637 470 380.949 470c11.999 0 23.397-1.147 34.196-3.442 10.799-2.294 20.268-6.075 28.406-11.342 8.138-5.266 14.581-12.15 19.328-20.65S470 415.559 470 403.044c0-9.074-1.356-17.026-4.069-23.857s-6.625-12.906-11.738-18.225c-5.112-5.319-11.242-10.091-18.389-14.315s-15.207-8.213-24.18-11.967c-6.573-2.712-12.468-5.345-17.685-7.9-5.217-2.556-9.651-5.163-13.303-7.822-3.652-2.66-6.469-5.476-8.451-8.448-1.982-2.973-2.974-6.336-2.974-10.091 0-3.441.887-6.544 2.661-9.308s4.278-5.136 7.512-7.118c3.235-1.981 7.199-3.52 11.894-4.615 4.696-1.095 9.912-1.642 15.651-1.642 4.173 0 8.581.313 13.224.938 4.643.626 9.312 1.591 14.008 2.894a97.514 97.514 0 0 1 13.694 4.928c4.434 1.982 8.529 4.276 12.285 6.884v-46.776c-7.616-2.92-15.937-5.084-24.962-6.492S415.797 238 404.112 238c-11.895 0-23.163 1.278-33.805 3.833s-20.006 6.544-28.093 11.967c-8.086 5.424-14.476 12.333-19.171 20.729-4.695 8.395-7.043 18.433-7.043 30.114 0 14.914 4.304 27.638 12.912 38.172 8.607 10.533 21.675 19.45 39.204 26.751 6.886 2.816 13.303 5.579 19.25 8.291s11.086 5.528 15.415 8.448c4.33 2.92 7.747 6.101 10.252 9.543 2.504 3.441 3.756 7.352 3.756 11.733 0 3.233-.783 6.231-2.348 8.995s-3.939 5.162-7.121 7.196-7.147 3.624-11.894 4.771c-4.748 1.148-10.303 1.721-16.668 1.721-10.851 0-21.597-1.903-32.24-5.71-10.642-3.806-20.502-9.516-29.579-17.13zM232.78 284.082H297V243H118v41.082h63.906V467h50.874z"
clipRule="evenodd"
/>
</svg>}
    arrow
  />

  <Card
    title="Java"
    href="/es/guides/languages/java"
    icon={ <svg
xmlns="http://www.w3.org/2000/svg"
fill="none"
aria-label="Java"
viewBox="0 0 512 512"
width="32"

>

<rect width={512} height={512} fill="#fff" rx="15%" />
<path
fill="#f8981d"
d="M274 235c18 21-5 40-5 40s47-24 25-54-35-42 48-90c0-1-131 32-68 104m20-182s40 40-38 100c-62 49-14 77 0 109-36-33-63-61-45-88 27-40 99-59 83-121"
/>
<path
fill="#5382a1"
d="M206 347s-15 8 10 11 46 3 79-3a137 137 0 0 0 21 10c-74 32-169-1-110-18m-9-42s-16 12 9 15 58 4 102-5a45 45 0 0 0 16 10c-91 26-192 2-127-20m175 73s11 9-12 16c-43 13-179 17-217 1-14-6 15-17 33-17-17-10-98 21-42 30 153 24 278-12 238-30M213 262s-69 16-25 22c19 3 57 2 92-1s57-8 57-8a122 122 0 0 0-17 9c-70 18-206 10-167-9s60-13 60-13m124 69c73-37 39-80 7-66 36-30 101 36-9 68v-2M220 432c69 4 174-2 176-35 0 0-5 12-57 22s-131 10-174 3c1 0 10 7 55 10"
/>

</svg>}
    arrow
  />

  <Card
    title="Python"
    href="/es/guides/languages/python"
    icon={
<svg
xmlns="http://www.w3.org/2000/svg"
width="24"
height="24"
fill="none"
viewBox="0 0 32 32"
>
<path
fill="url(#a)"
fillRule="evenodd"
d="M13.016 2C10.82 2 9.038 3.725 9.038 5.852v2.667h6.886v.74H5.978C3.781 9.26 2 10.984 2 13.111v5.778c0 2.127 1.781 3.852 3.978 3.852h2.295v-3.26c0-2.127 1.781-3.851 3.978-3.851h7.345c1.859 0 3.366-1.46 3.366-3.26V5.852C22.962 3.725 21.18 2 18.984 2h-5.968Zm-.918 4.74c.76 0 1.377-.596 1.377-1.333 0-.736-.616-1.333-1.377-1.333-.76 0-1.377.597-1.377 1.333 0 .737.617 1.334 1.377 1.334Z"
clipRule="evenodd"
/>
<path
fill="url(#b)"
fillRule="evenodd"
d="M18.983 30c2.197 0 3.979-1.724 3.979-3.852v-2.666h-6.886v-.741h9.946c2.197 0 3.978-1.725 3.978-3.852V13.11c0-2.127-1.781-3.852-3.978-3.852h-2.295v3.26c0 2.127-1.782 3.851-3.979 3.851h-7.344c-1.859 0-3.366 1.46-3.366 3.26v6.518c0 2.128 1.781 3.852 3.978 3.852h5.967Zm.918-4.74c-.76 0-1.377.596-1.377 1.333 0 .736.617 1.333 1.377 1.333.761 0 1.378-.597 1.378-1.333 0-.737-.617-1.334-1.378-1.334Z"
clipRule="evenodd"
/>
<defs>
<linearGradient
id="a"
x1={12.481}
x2={12.481}
y1={2}
y2={22.741}
gradientUnits="userSpaceOnUse"
>
<stop stopColor="#327EBD" />
<stop offset={1} stopColor="#1565A7" />
</linearGradient>
<linearGradient
id="b"
x1={19.519}
x2={19.519}
y1={9.259}
y2={30}
gradientUnits="userSpaceOnUse"
>
<stop stopColor="#FFDA4B" />
<stop offset={1} stopColor="#F9C600" />
</linearGradient>
</defs>
</svg>
}
    arrow
  />

  <Card
    title="Swift"
    href="/es/guides/languages/swift"
    icon={
<svg
xmlns="http://www.w3.org/2000/svg"
xmlSpace="preserve"
width="24"
height="24"
viewBox="0 0 59.391 59.391"
>
<path
fill="#F05138"
d="M59.387 16.45a82.463 82.463 0 0 0-.027-1.792c-.035-1.301-.112-2.614-.343-3.9-.234-1.307-.618-2.523-1.222-3.71a12.464 12.464 0 0 0-5.453-5.452C51.156.992 49.941.609 48.635.374c-1.288-.232-2.6-.308-3.902-.343a85.714 85.714 0 0 0-1.792-.027C42.23 0 41.52 0 40.813 0H18.578c-.71 0-1.419 0-2.128.004-.597.004-1.195.01-1.792.027-.325.009-.651.02-.978.036-.978.047-1.959.133-2.924.307-.98.176-1.908.436-2.811.81A12.503 12.503 0 0 0 3.89 3.89a12.46 12.46 0 0 0-2.294 3.158C.992 8.235.61 9.45.374 10.758c-.231 1.286-.308 2.599-.343 3.9a85.767 85.767 0 0 0-.027 1.792C-.001 17.16 0 17.869 0 18.578v22.235c0 .71 0 1.418.004 2.128.004.597.01 1.194.027 1.791.035 1.302.112 2.615.343 3.901.235 1.307.618 2.523 1.222 3.71a12.457 12.457 0 0 0 5.453 5.453c1.186.603 2.401.986 3.707 1.22 1.287.232 2.6.31 3.902.344.597.016 1.195.023 1.793.027.709.005 1.417.004 2.127.004h22.235c.709 0 1.418 0 2.128-.004.597-.004 1.194-.011 1.792-.027 1.302-.035 2.614-.112 3.902-.343 1.306-.235 2.521-.618 3.707-1.222a12.461 12.461 0 0 0 5.453-5.452c.604-1.187.987-2.403 1.222-3.71.231-1.286.308-2.6.343-3.9.016-.598.023-1.194.027-1.792.004-.71.004-1.419.004-2.129V18.578c0-.71 0-1.419-.004-2.128z"
/>
<path
fill="#FFF"
d="m47.06 36.66-.004-.004c.066-.224.134-.446.191-.675 2.465-9.821-3.55-21.432-13.731-27.546 4.461 6.048 6.434 13.374 4.681 19.78-.156.571-.344 1.12-.552 1.653-.225-.148-.51-.316-.89-.527 0 0-10.127-6.252-21.103-17.312-.288-.29 5.852 8.777 12.822 16.14-3.284-1.843-12.434-8.5-18.227-13.802.712 1.187 1.558 2.33 2.489 3.43C17.573 23.932 23.882 31.5 31.44 37.314c-5.31 3.25-12.814 3.502-20.285.003a30.646 30.646 0 0 1-5.193-3.098c3.162 5.058 8.033 9.423 13.96 11.97 7.07 3.039 14.1 2.833 19.336.05l-.004.007c.024-.016.055-.032.08-.047.214-.116.428-.234.636-.358 2.516-1.306 7.485-2.63 10.152 2.559.654 1.27 2.041-5.46-3.061-11.74z"
/>
</svg>
}
    arrow
  />
</CardGroup>

Podés agregar soporte para más lenguajes mediante extensiones, igual que en VS Code.

<div id="creating-your-account">
  ## Crear tu cuenta
</div>

Aunque Cursor funciona sin una cuenta, registrarte desbloquea todas las funciones de IA:

1. Se te pedirá que te registres durante la configuración, o puedes hacerlo después en Settings (<Kbd>Cmd Shift J</Kbd>)
2. Una vez que te registres, administra tu cuenta en [cursor.com/dashboard](https://cursor.com/dashboard)

<div id="understanding-codebase-indexing">
  ## Cómo funciona la indexación del código
</div>

Cuando abres un proyecto, Cursor empieza a aprender sobre tu código. A esto se le llama “indexación” y es lo que hace que las sugerencias de la IA sean precisas.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="Indicador de progreso de la indexación del código" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
</Frame>

* La indexación empieza automáticamente cuando abres un proyecto
* Tarda entre 1 y 15 minutos según el tamaño de tu proyecto
* Cuanto más aprende Cursor sobre tu código, más inteligentes se vuelven sus sugerencias
* Los equipos pueden compartir índices entre sí para ahorrar tiempo
* Puedes revisar el progreso de la indexación en Settings (<Kbd>Cmd Shift J</Kbd>) → Indexing & Docs

¿Quieres saber más? Consulta [cómo funciona la indexación](/es/context/codebase-indexing)

<div id="next-steps">
  ## Próximos pasos
</div>

Ahora que instalaste Cursor, ya estás listo para probar la programación con IA:

* Sigue nuestra [guía de inicio rápido](/es/get-started/quickstart) para aprender lo básico en 5 minutos
* Lee sobre [conceptos clave](/es/get-started/concepts) para entender cómo funciona Cursor
* [Explora las guías](/es/guides) para descubrir qué puedes crear con Cursor
* Si te topas con problemas, [pide ayuda](/es/troubleshooting/common-issues) en nuestra guía de solución de problemas
* [Únete a nuestra comunidad](https://cursor.com/community) para conectarte con otros usuarios de Cursor



# Guía rápida
Source: https://docs.cursor.com/es/get-started/quickstart

Comenzá con Cursor en 5 minutos

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Esta guía rápida te llevará por un proyecto usando las funciones principales de Cursor. Al final, ya estarás familiarizado con Tab, Inline Edit y Agent.

<div id="open-a-project-in-cursor">
  ## Abre un proyecto en Cursor
</div>

Usa un proyecto existente o clona nuestro ejemplo:

<Tabs>
  <Tab title="Clona el proyecto de ejemplo">
    1. Asegúrate de tener git instalado
    2. Clona el proyecto de ejemplo:

    ```bash  theme={null}
    git clone git@github.com:voxelize/voxelize.git && \
    cd voxelize && \
    cursor .
    ```
  </Tab>

  <Tab title="Usa un proyecto existente">
    1. Abre Cursor
    2. Abre una carpeta de proyecto con <Kbd>Cmd O</Kbd> o `cursor <ruta-al-proyecto>`
  </Tab>
</Tabs>

Vamos a mostrarlo con el proyecto de ejemplo, pero puedes usar cualquier proyecto que tengas en local.

<div id="autocomplete-with-tab">
  ## Autocomplete con [Tab](/es/kbd#tab)
</div>

Tab es el modelo de autocompletado que entrenamos internamente. Es una gran forma de empezar con el código asistido por IA si no estás acostumbrado. Con Tab, podés:

* Autocompletar **múltiples líneas y bloques** de código
* Saltar **dentro** y **entre** archivos a la siguiente sugerencia de autocompletado

1. Empezá a escribir el comienzo de una función:
   ```javascript  theme={null}
   function calculate
   ```
2. Las sugerencias de Tab aparecen automáticamente
3. Presioná Tab para aceptar la sugerencia
4. Cursor sugiere parámetros y cuerpos de funciones

<div id="inline-edit-a-selection">
  ## [Edición en línea](/es/inline-edit) de una selección
</div>

1. Selecciona la función que acabas de crear
2. Presiona <Kbd>Cmd K</Kbd>
3. Escribe "make this function calculate Fibonacci numbers"
4. Presiona <Kbd>Return</Kbd> para aplicar los cambios
5. Cursor agrega imports y documentación

<div id="chat-with-agent">
  ## Chatea con [Agent](/es/agent)
</div>

1. Abre el panel de chat (<Kbd>Cmd I</Kbd>)
2. Di: "Add tests for this function and run them"
3. Agent creará un archivo de pruebas, escribirá casos de prueba y los ejecutará por ti

<div id="bonus">
  ## Bonus
</div>

Funciones avanzadas:

<AccordionGroup>
  <Accordion title="Delegar trabajo a Background Agent">
    1. Abre el panel de control de Background Agent (<Kbd>Cmd E</Kbd>)
    2. Pide: "Find and fix a bug in this project"
    3. [Background Agent](/es/background-agent) hará lo siguiente:
       * Crear una máquina virtual (VM) remota
       * Explorar tu proyecto
       * Detectar errores
       * Proponer correcciones

    Revisa y aplica los cambios.
  </Accordion>

  {" "}

  <Accordion title="Escribir una regla">
    1. Abre la paleta de comandos (<Kbd>Cmd Shift P</Kbd>) 2. Busca: "New Cursor
       Rule" 3. Ponle un nombre (p. ej., `style-guide`) 4. Selecciona el tipo de regla "Always" 5. Define
       tu estilo: `Prefer using camelCase for variable names`
  </Accordion>

  <Accordion title="Configurar un servidor MCP">
    1. Visita nuestro [directorio de MCP](https://docs.cursor.com/tools)
    2. Elige una herramienta
    3. Haz clic en "Install"

    Los servidores también se pueden instalar manualmente:

    1. Abre Cursor Settings (<Kbd>Cmd Shift J</Kbd>)
    2. Ve a "Tools & Integrations"
    3. Haz clic en "New MCP Server"
  </Accordion>
</AccordionGroup>

<div id="next-steps">
  ## Próximos pasos
</div>

Explora estas guías para aprender más:

<CardGroup cols={2}>
  <Card title="Working with Context" href="/es/guides/working-with-context">
    Proporciona un buen contexto para obtener mejores resultados
  </Card>

  <Card title="Selecting Models" href="/es/guides/selecting-models">
    Elige el modelo adecuado para tu tarea
  </Card>
</CardGroup>

Aprende todos los [conceptos de Cursor](/es/get-started/concepts) y ¡empieza a crear!



# Ciencia de datos
Source: https://docs.cursor.com/es/guides/advanced/datascience

Aprende a configurar Cursor para flujos de trabajo de ciencia de datos, incluidos Python, R y SQL, con notebooks, entornos remotos y análisis con IA

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Cursor ofrece herramientas integradas para el desarrollo de ciencia de datos mediante entornos reproducibles, compatibilidad con notebooks y asistencia de código impulsada por IA. Esta guía cubre patrones esenciales de configuración para flujos de trabajo en Python, R y SQL.

<div id="notebook-development">
  ## Desarrollo con notebooks
</div>

<Note>
  Para obtener compatibilidad completa con notebooks, descarga la extensión Jupyter (id: ms-toolsai.jupyter), publicada por ms-toolsai.
</Note>

Cursor es compatible con archivos `.ipynb` y `.py` con ejecución de celdas integrada. Tab, Inline Edit y Agents
funcionan en notebooks, igual que en otros archivos de código.

Funciones clave:

* La **ejecución de celdas en línea** corre código directamente en la interfaz del editor
* **Tab, Inline Edit y Agent** entienden bibliotecas de ciencia de datos como pandas, NumPy, scikit-learn y comandos mágicos de SQL

<div id="database-integration">
  ## Integración de bases de datos
</div>

Puedes integrar bases de datos con Cursor de dos formas principales: servidores MCP y extensiones.

* **Servidores MCP** permiten que tus agentes se conecten a tus bases de datos
* **Extensiones** integran tu IDE en general con tus bases de datos

<div id="via-mcp">
  ### Vía MCP
</div>

Los servidores MCP permiten que tu agente haga consultas directamente a tu base de datos. Esto le permite decidir consultar tu base de datos, escribir la consulta adecuada, ejecutar el comando y analizar los resultados, todo como parte de una tarea en curso.

Por ejemplo, puedes conectar una base de datos de Postgres a tu instancia de Cursor agregando la siguiente [configuración de MCP](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres) a Cursor:

```json  theme={null}
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://localhost/mibase"
      ]
    }
  }
}
```

Para más información sobre MCP, consulta nuestra [documentación de MCP](/es/tools/mcp).

<Frame>
  <video autoPlay loop muted playsInline controls width="100%">
    <source src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/postgres-mcp.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=334439f58b7d88b16d97134cf9c147aa" type="video/mp4" data-path="images/guides/advanced/datascience/postgres-mcp.mp4" />

    Tu navegador no admite la etiqueta de video.
  </video>
</Frame>

<div id="via-extensions">
  ### Mediante extensiones
</div>

Instala extensiones específicas para bases de datos (PostgreSQL, BigQuery, SQLite, Snowflake) para ejecutar consultas directamente desde el editor. Esto evita cambiar de contexto entre herramientas y habilita la asistencia de IA para optimizar consultas.

```sql  theme={null}
-- Cursor sugiere índices, funciones de ventana y optimizaciones de consultas
SELECT
    user_id,
    event_type,
    COUNT(*) AS total_eventos,
    RANK() OVER (PARTITION BY user_id ORDER BY COUNT(*) DESC) AS ranking_frecuencia
FROM events
WHERE created_at >= NOW() - INTERVAL '7 days'
GROUP BY user_id, event_type;
```

Usa Agents para analizar consultas lentas, sugerir mejoras de rendimiento o generar código de visualización para los resultados de las consultas. Cursor entiende el contexto de SQL y puede recomendar tipos de gráficos adecuados según la estructura de tus datos.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7c14c60dc3c0523fb565c9462ac49029" alt="Extensión de Snowflake" data-og-width="2324" width="2324" data-og-height="1602" height="1602" data-path="images/guides/advanced/datascience/snowflake-extension.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a8f316c0a5e756aed89423082dfa11d8 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a8a66623964651cac9182159d880a511 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2dc2566fa81d26a920d681178cb1d209 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=52c3a74cea69f812e869c2bc25457462 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d3322864e752c413fb3bfb2b686136f3 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9ee01c8736f8eb78a04aab6340c4eaae 2500w" />
</Frame>

<div id="data-visualization">
  ## Visualización de datos
</div>

La asistencia de IA de Cursor se extiende a bibliotecas de visualización de datos como Matplotlib, Plotly y Seaborn. El agente puede generar código para visualización de datos, ayudándote a explorar datos rápida y fácilmente, mientras crea un artefacto replicable y compartible.

```python  theme={null}
import plotly.express as px
import pandas as pd


# La IA sugiere tipos de gráficos relevantes según las columnas del conjunto de datos
df = pd.read_csv('sales_data.csv')
fig = px.scatter(df, x='advertising_spend', y='revenue',
                 color='region', size='customer_count',
                 title='Ingresos vs gasto en publicidad por región')
fig.show()
```

<Frame>
  <video autoPlay loop muted playsInline controls width="100%">
    <source src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/datascience-visualization.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=0ebce62250db235a6a3740ca3bcb188b" type="video/mp4" data-path="images/guides/advanced/datascience/datascience-visualization.mp4" />

    Tu navegador no admite la etiqueta de video.
  </video>
</Frame>

<div id="frequently-asked-questions">
  ## Preguntas frecuentes
</div>

**¿Puedo usar notebooks de Jupyter existentes?**
Sí, Cursor abre archivos `.ipynb` con ejecución completa de celdas y compatibilidad con completado por IA.

**¿Cómo manejo datasets grandes que no caben en memoria?**
Usa bibliotecas de computación distribuida como Dask o conéctate a clústeres de Spark mediante conexiones Remote-SSH a máquinas más potentes.

**¿Cursor admite archivos R y SQL?**
Sí, Cursor ofrece asistencia con IA y resaltado de sintaxis para scripts de R (`.R`) y archivos SQL (`.sql`).

**¿Cuál es la forma recomendada de compartir entornos de desarrollo?**
Haz commit de la carpeta `.devcontainer` al control de versiones. Los miembros del equipo pueden reconstruir el entorno automáticamente al abrir el proyecto.

**¿Cómo depuro pipelines de procesamiento de datos?**
Usa el depurador integrado de Cursor con puntos de interrupción en scripts de Python, o aprovecha Agent para analizar y explicar transformaciones de datos complejas paso a paso.

<div id="environment-reproducibility">
  ## Reproducibilidad del entorno
</div>

<div id="development-containers">
  ### Contenedores de desarrollo
</div>

Los contenedores de desarrollo te ayudan a garantizar entornos de ejecución y dependencias consistentes entre los miembros del equipo y los entornos de despliegue. Pueden eliminar errores específicos del entorno y reducir el tiempo de onboarding de nuevos miembros del equipo.

Para usar un contenedor de desarrollo, empieza creando una carpeta `.devcontainer` en la raíz de tu repositorio. Luego crea un archivo `devcontainer.json`, un `Dockerfile` y un `requirements.txt`.

```json  theme={null}
// .devcontainer/devcontainer.json
{
  "name": "ds-env",
  "build": { "dockerfile": "Dockerfile" },
  "features": {
    "ghcr.io/devcontainers/features/python:1": { "version": "3.11" }
  },
  "postCreateCommand": "pip install -r requirements.txt"
}
```

```dockerfile  theme={null}

# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.11
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
```

```txt  theme={null}

# requirements.txt
pandas==2.3.0
numpy

# agrega otras dependencias que necesites para tu proyecto
```

Cursor detectará automáticamente el devcontainer y te pedirá volver a abrir tu proyecto dentro de un contenedor. También podés reabrirlo manualmente en un contenedor usando la Command Palette (<Kbd>Cmd+Shift+P</Kbd>) y buscando `Reopen in Container`.

Los contenedores de desarrollo ofrecen varias ventajas:

* **Aislamiento de dependencias** evita conflictos entre proyectos
* **Compilaciones reproducibles** garantizan un comportamiento consistente entre entornos de desarrollo y producción
* **Onboarding simplificado** permite que nuevos miembros del equipo empiecen de inmediato sin configuración manual

<div id="remote-development-with-ssh">
  ### Desarrollo remoto con SSH
</div>

Cuando tu trabajo requiera recursos de cómputo adicionales, GPUs o acceso a datasets privados, conectate a máquinas remotas manteniendo tu entorno de desarrollo local.

1. Aprovisioná una instancia en la nube o accedé a un servidor on‑premises con los recursos necesarios
2. Cloná tu repositorio en la máquina remota, incluyendo la configuración `.devcontainer`
3. Conectate mediante Cursor: <Kbd>Cmd+Shift+P</Kbd> → "Remote-SSH: Connect to Host"

Este enfoque mantiene un tooling consistente mientras escala los recursos de cómputo según sea necesario. La misma configuración del contenedor de desarrollo funciona tanto en entornos locales como remotos.




---

**Navigation:** [← Previous](./08-welcome.md) | [Index](./index.md) | [Next →](./10-large-codebases.md)