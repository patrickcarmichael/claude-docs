---
title: "Code Review"
source: "https://docs.cursor.com/es/cli/cookbook/code-review"
language: "es"
language_name: "Spanish"
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

---

← Previous: [Bugbot](./bugbot.md) | [Index](./index.md) | Next: [Corregir fallos de CI](./corregir-fallos-de-ci.md) →