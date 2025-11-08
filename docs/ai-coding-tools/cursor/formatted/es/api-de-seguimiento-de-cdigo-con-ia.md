---
title: "API de seguimiento de código con IA"
source: "https://docs.cursor.com/es/account/teams/ai-code-tracking-api"
language: "es"
language_name: "Spanish"
---

# API de seguimiento de código con IA
Source: https://docs.cursor.com/es/account/teams/ai-code-tracking-api

Accede a analíticas de código generadas por IA para los repositorios de tu equipo

Accede a analíticas de código generadas por IA para los repositorios de tu equipo. Incluye uso de IA por commit y cambios de IA aceptados a nivel granular.

<Note>
  La API está en su primera versión. Estamos ampliando funcionalidades según el feedback; ¡cuéntanos qué endpoints necesitas!
</Note>

* **Disponibilidad**: Solo para equipos Enterprise
* **Estado**: Alpha (las estructuras y los campos de la respuesta pueden cambiar)

<div id="authentication">
  ## Autenticación
</div>

Todas las solicitudes a la API requieren autenticación con una clave de API. Esta API usa el mismo método de autenticación del Admin API que otros endpoints.

Para ver instrucciones detalladas de autenticación, consulta [Autenticación del Admin API](/es/account/teams/admin-api#authentication).

<div id="base-url">
  ## URL base
</div>

Todas las rutas de la API usan:

```
https://api.cursor.com
```

<div id="rate-limits">
  ## Límites de uso
</div>

* 5 solicitudes por minuto por equipo y por endpoint

<div id="query-parameters">
  ## Parámetros de consulta
</div>

Todos los endpoints a continuación aceptan los mismos parámetros a través del query string:

<div className="full-width-table">
  | Parámetro   | Tipo   | Obligatorio | Descripción                                                                                                                                                                            |                                                                                                                              |
  | :---------- | :----- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
  | `startDate` | string | date        | No                                                                                                                                                                                     | Cadena de fecha ISO, el literal "now" o días relativos como "7d" (equivale a ahora - 7 días). Predeterminado: ahora - 7 días |
  | `endDate`   | string | date        | No                                                                                                                                                                                     | Cadena de fecha ISO, el literal "now" o días relativos como "0d". Predeterminado: ahora                                      |
  | `page`      | number | No          | Número de página (base 1). Predeterminado: 1                                                                                                                                           |                                                                                                                              |
  | `pageSize`  | number | No          | Resultados por página. Predeterminado: 100, máx.: 1000                                                                                                                                 |                                                                                                                              |
  | `user`      | string | No          | Filtro opcional por un único usuario. Acepta email (p. ej., [developer@company.com](mailto:developer@company.com)), ID codificado (p. ej., user\_abc123...) o ID numérico (p. ej., 42) |                                                                                                                              |
</div>

<Note>
  Las respuestas devuelven userId como un ID externo codificado con el prefijo user\_. Esto es estable para el consumo por API.
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## Semántica y cómo se calculan las métricas
</div>

* **Origen**: "TAB" representa las completions en línea aceptadas; "COMPOSER" representa diffs aceptados desde Composer
* **Métricas de líneas**: tabLinesAdded/Deleted y composerLinesAdded/Deleted se cuentan por separado; nonAiLinesAdded/Deleted se calculan como max(0, totalLines - AI lines)
* **Modo de privacidad**: Si está habilitado en el cliente, puede omitirse cierta metadata (como fileName)
* **Información de la rama**: isPrimaryBranch es true cuando la rama actual es igual a la rama predeterminada del repo; puede ser undefined si la info del repo no está disponible

Podés escanear ese archivo para entender cómo se detectan y reportan los commits y cambios.

<div id="endpoints">
  ## Endpoints
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### Obtener métricas de commits con IA (JSON, paginadas)
</div>

Obtén métricas agregadas por commit que atribuyen líneas a TAB, COMPOSER y no IA.

```
GET /analytics/ai-code/commits
```

<div id="response">
  #### Respuesta
</div>

```typescript  theme={null}
{
  items: MetricasDeCommitAI[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### Campos de AiCommitMetric
</div>

<div className="full-width-table">
  | Campo                  | Tipo    | Descripción                                       |                                          |
  | :--------------------- | :------ | :------------------------------------------------ | ---------------------------------------- |
  | `commitHash`           | string  | Hash del commit de Git                            |                                          |
  | `userId`               | string  | ID de usuario codificado (p. ej., user\_abc123)   |                                          |
  | `userEmail`            | string  | Dirección de correo electrónico del usuario       |                                          |
  | `repoName`             | string  | null                                              | Nombre del repositorio                   |
  | `branchName`           | string  | null                                              | Nombre de la rama                        |
  | `isPrimaryBranch`      | boolean | null                                              | Indica si es la rama principal           |
  | `totalLinesAdded`      | number  | Total de líneas añadidas en el commit             |                                          |
  | `totalLinesDeleted`    | number  | Total de líneas eliminadas en el commit           |                                          |
  | `tabLinesAdded`        | number  | Líneas añadidas mediante autocompletado con TAB   |                                          |
  | `tabLinesDeleted`      | number  | Líneas eliminadas mediante autocompletado con TAB |                                          |
  | `composerLinesAdded`   | number  | Líneas añadidas mediante Composer                 |                                          |
  | `composerLinesDeleted` | number  | Líneas eliminadas mediante Composer               |                                          |
  | `nonAiLinesAdded`      | number  | null                                              | Líneas no generadas por IA añadidas      |
  | `nonAiLinesDeleted`    | number  | null                                              | Líneas no generadas por IA eliminadas    |
  | `message`              | string  | null                                              | Mensaje del commit                       |
  | `commitTs`             | string  | null                                              | Marca de tiempo del commit (formato ISO) |
  | `createdAt`            | string  | Marca de tiempo de ingesta (formato ISO)          |                                          |
</div>

<div id="example-response">
  #### Ejemplo de respuesta
</div>

```json  theme={null}
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "Refactor: extraer cliente de analíticas",
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

<div id="example-requests">
  #### Ejemplos de solicitudes
</div>

**Solicitud básica:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u TU_API_KEY:
```

**Filtrar por usuario (correo):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u TU_API_KEY:
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### Descargar métricas de commits con IA (CSV, streaming)
</div>

Descarga métricas de commits en formato CSV para extracciones de datos de gran volumen.

```
GET /analytics/ai-code/commits.csv
```

<div id="response">
  #### Respuesta
</div>

Encabezados:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### Columnas del CSV
</div>

<div className="full-width-table">
  | Columna                  | Tipo    | Descripción                                  |
  | :----------------------- | :------ | :------------------------------------------- |
  | `commit_hash`            | string  | Hash del commit de Git                       |
  | `user_id`                | string  | ID de usuario codificado                     |
  | `user_email`             | string  | Dirección de correo electrónico del usuario  |
  | `repo_name`              | string  | Nombre del repositorio                       |
  | `branch_name`            | string  | Nombre de la rama                            |
  | `is_primary_branch`      | boolean | Si es la rama principal                      |
  | `total_lines_added`      | number  | Total de líneas añadidas en el commit        |
  | `total_lines_deleted`    | number  | Total de líneas eliminadas en el commit      |
  | `tab_lines_added`        | number  | Líneas añadidas con autocompletado por TAB   |
  | `tab_lines_deleted`      | number  | Líneas eliminadas con autocompletado por TAB |
  | `composer_lines_added`   | number  | Líneas añadidas con Composer                 |
  | `composer_lines_deleted` | number  | Líneas eliminadas con Composer               |
  | `non_ai_lines_added`     | number  | Líneas no generadas por IA añadidas          |
  | `non_ai_lines_deleted`   | number  | Líneas no generadas por IA eliminadas        |
  | `message`                | string  | Mensaje del commit                           |
  | `commit_ts`              | string  | Marca de tiempo del commit (formato ISO)     |
  | `created_at`             | string  | Marca de tiempo de ingesta (formato ISO)     |
</div>

#### Ejemplo de salida CSV

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"Refactor: extraer cliente de analítica",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"Añadir manejo de errores",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-request">
  #### Ejemplo de solicitud
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u TU_API_KEY: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### Obtener métricas de cambios de IA (JSON, paginadas)
</div>

Obtén cambios de IA aceptados a nivel granular, agrupados por un changeId determinista. Útil para analizar eventos de IA aceptados de forma independiente a los commits.

```
GET /analytics/ai-code/changes
```

<div id="response">
  #### Respuesta
</div>

```typescript  theme={null}
{
  items: MetricaCambioCodigoIA[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### Campos de AiCodeChangeMetric
</div>

<div className="full-width-table">
  | Campo               | Tipo   | Descripción                                                              |                                   |
  | :------------------ | :----- | :----------------------------------------------------------------------- | --------------------------------- |
  | `changeId`          | string | ID determinista del cambio                                               |                                   |
  | `userId`            | string | ID de usuario codificado (p. ej., user\_abc123)                          |                                   |
  | `userEmail`         | string | Dirección de correo del usuario                                          |                                   |
  | `source`            | "TAB"  | "COMPOSER"                                                               | Origen del cambio generado por IA |
  | `model`             | string | null                                                                     | Modelo de IA usado                |
  | `totalLinesAdded`   | number | Total de líneas añadidas                                                 |                                   |
  | `totalLinesDeleted` | number | Total de líneas eliminadas                                               |                                   |
  | `createdAt`         | string | Marca de tiempo de ingesta (formato ISO)                                 |                                   |
  | `metadata`          | Array  | Metadatos del archivo (fileName puede omitirse en el modo de privacidad) |                                   |
</div>

#### Respuesta de ejemplo

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
      "metadata": [
        { "fileName": "src/analytics/report.ts", "fileExtension": "ts", "linesAdded": 12, "linesDeleted": 3 },
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

<div id="example-requests">
  #### Ejemplos de solicitudes
</div>

**Solicitud básica:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u TU_API_KEY:
```

**Filtrar por usuario (ID codificado):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u TU_API_KEY:
```

**Filtrar por usuario (correo):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u TU_CLAVE_DE_API:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### Descargar métricas de cambios de código con IA (CSV, streaming)
</div>

Descarga métricas de cambios en formato CSV para extracciones de datos a gran escala.

```
GET /analytics/ai-code/changes.csv
```

<div id="response">
  #### Respuesta
</div>

Encabezados:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### Columnas del CSV
</div>

<div className="full-width-table">
  | Columna               | Tipo   | Descripción                                          |
  | :-------------------- | :----- | :--------------------------------------------------- |
  | `change_id`           | string | ID determinista del cambio                           |
  | `user_id`             | string | ID de usuario codificado                             |
  | `user_email`          | string | Dirección de correo del usuario                      |
  | `source`              | string | Origen del cambio de IA (TAB o COMPOSER)             |
  | `model`               | string | Modelo de IA utilizado                               |
  | `total_lines_added`   | number | Total de líneas agregadas                            |
  | `total_lines_deleted` | number | Total de líneas eliminadas                           |
  | `created_at`          | string | Marca de tiempo de ingesta (formato ISO)             |
  | `metadata_json`       | string | Arreglo de entradas de metadatos serializado en JSON |
</div>

<div id="notes">
  #### Notas
</div>

* metadata\_json es un arreglo de entradas de metadatos serializado en JSON (puede omitir fileName en modo de privacidad)
* Al consumir CSV, asegúrate de analizar los campos entre comillas

<div id="sample-csv-output">
  #### Salida de ejemplo en CSV
</div>

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-request">
  #### Ejemplo de solicitud
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u TU_API_KEY: \
  -o changes.csv
```

<div id="tips">
  ## Consejos
</div>

* Usa el parámetro `user` para filtrar rápido a un solo usuario en todos los endpoints
* Para extracciones de datos grandes, prefiere los endpoints CSV: hacen streaming en páginas de 10.000 registros del lado del servidor
* `isPrimaryBranch` puede ser `undefined` si el cliente no pudo resolver la rama predeterminada
* `commitTs` es la marca de tiempo del commit; `createdAt` es la hora de ingesta en nuestros servidores
* Algunos campos pueden estar ausentes cuando el modo de privacidad está habilitado en el cliente

<div id="changelog">
  ## Registro de cambios
</div>

* **Versión alfa**: Endpoints iniciales para commits y cambios. Las formas de las respuestas pueden evolucionar según el feedback

---

← Previous: [Admin API](./admin-api.md) | [Index](./index.md) | Next: [Analytics](./analytics.md) →