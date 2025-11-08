---
title: "Admin API"
source: "https://docs.cursor.com/es/account/teams/admin-api"
language: "es"
language_name: "Spanish"
---

# Admin API
Source: https://docs.cursor.com/es/account/teams/admin-api

Accedé a métricas del equipo, datos de uso e información de gastos vía API

La Admin API te permite acceder de forma programática a los datos de tu equipo, incluyendo información de miembros, métricas de uso y detalles de gastos. Creá dashboards personalizados, herramientas de monitoreo o integrá con tus workflows existentes.

<Note>
  La API está en su primera versión. Estamos ampliando capacidades según el feedback: ¡contanos qué endpoints necesitás!
</Note>

<div id="authentication">
  ## Autenticación
</div>

Todas las solicitudes a la API requieren autenticación con una clave de API. Solo los administradores del equipo pueden crear y gestionar claves de API.

Las claves de API están vinculadas a la organización, son visibles para todos los administradores y no se ven afectadas por el estado de la cuenta de quien las creó originalmente.

<div id="creating-an-api-key">
  ### Crear una clave de API
</div>

1. Ve a **cursor.com/dashboard** → pestaña **Settings** → **Cursor Admin API Keys**
2. Haz clic en **Create New API Key**
3. Dale a tu clave un nombre descriptivo (p. ej., "Integración del panel de uso")
4. Copia la clave generada de inmediato: no la volverás a ver

Formato: `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### Usar tu clave de API
</div>

Usa tu clave de API como nombre de usuario en la autenticación básica:

**Usar curl con autenticación básica:**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**O bien establece directamente el encabezado Authorization:**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## URL base
</div>

Todos los endpoints de la API utilizan:

```
https://api.cursor.com
```

<div id="endpoints">
  ## Endpoints
</div>

<div id="get-team-members">
  ### Obtener miembros del equipo
</div>

Obtén todos los miembros del equipo y sus detalles.

```
GET /teams/members
```

#### Respuesta

Devuelve un array de objetos de miembros del equipo:

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
  }[];
}
```

#### Respuesta de ejemplo

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "miembro"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "dueño"
    }
  ]
}

```

#### Ejemplo de solicitud

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u TU_CLAVE_API:
```

<div id="get-daily-usage-data">
  ### Obtener datos de uso diario
</div>

Obtén métricas diarias detalladas para tu equipo en un rango de fechas. Ofrece información sobre ediciones de código, uso de la IA de asistencia y tasas de aceptación.

```
POST /teams/uso-diario
```

#### Cuerpo de la solicitud

<div className="full-width-table">
  | Parámetro   | Tipo   | Requerido | Descripción                              |
  | :---------- | :----- | :-------- | :--------------------------------------- |
  | `startDate` | number | Sí        | Fecha de inicio en milisegundos de época |
  | `endDate`   | number | Sí        | Fecha de fin en milisegundos de época    |
</div>

<Note>
  El rango de fechas no puede superar los 90 días. Haz varias solicitudes para periodos más largos.
</Note>

#### Respuesta

```typescript  theme={null}
{
  data: {
    date: number;
    isActive: boolean;
    totalLinesAdded: number;
    totalLinesDeleted: number;
    acceptedLinesAdded: number;
    acceptedLinesDeleted: number;
    totalApplies: number;
    totalAccepts: number;
    totalRejects: number;
    totalTabsShown: number;
    totalTabsAccepted: number;
    composerRequests: number;
    chatRequests: number;
    agentRequests: number;
    cmdkUsages: number;
    subscriptionIncludedReqs: number;
    apiKeyReqs: number;
    usageBasedReqs: number;
    bugbotUsages: number;
    mostUsedModel: string;
    applyMostUsedExtension?: string;
    tabMostUsedExtension?: string;
    clientVersion?: string;
    email?: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### Campos de respuesta
</div>

<div className="full-width-table">
  | Field                      | Description                                      |
  | :------------------------- | :----------------------------------------------- |
  | `date`                     | Fecha en milisegundos desde la época (epoch)     |
  | `isActive`                 | Usuario activo ese día                           |
  | `totalLinesAdded`          | Líneas de código añadidas                        |
  | `totalLinesDeleted`        | Líneas de código eliminadas                      |
  | `acceptedLinesAdded`       | Líneas añadidas de sugerencias de IA aceptadas   |
  | `acceptedLinesDeleted`     | Líneas eliminadas de sugerencias de IA aceptadas |
  | `totalApplies`             | Operaciones de apply                             |
  | `totalAccepts`             | Sugerencias aceptadas                            |
  | `totalRejects`             | Sugerencias rechazadas                           |
  | `totalTabsShown`           | Autocompletados por tab mostrados                |
  | `totalTabsAccepted`        | Autocompletados por tab aceptados                |
  | `composerRequests`         | Solicitudes del Composer                         |
  | `chatRequests`             | Solicitudes de chat                              |
  | `agentRequests`            | Solicitudes del agente                           |
  | `cmdkUsages`               | Usos de la paleta de comandos (Cmd+K)            |
  | `subscriptionIncludedReqs` | Solicitudes incluidas en la suscripción          |
  | `apiKeyReqs`               | Solicitudes con clave de API                     |
  | `usageBasedReqs`           | Solicitudes de pago por uso                      |
  | `bugbotUsages`             | Usos del detector de bugs                        |
  | `mostUsedModel`            | Modelo de IA más usado                           |
  | `applyMostUsedExtension`   | Extensión de archivo más usada en applies        |
  | `tabMostUsedExtension`     | Extensión de archivo más usada en tabs           |
  | `clientVersion`            | Versión de Cursor                                |
  | `email`                    | Correo electrónico del usuario                   |
</div>

#### Ejemplo de respuesta

```json  theme={null}
{
  "data": [
    {
      "date": 1710720000000,
      "isActive": true,
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalApplies": 87,
      "totalAccepts": 73,
      "totalRejects": 14,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "cmdkUsages": 67,
      "subscriptionIncludedReqs": 180,
      "apiKeyReqs": 0,
      "usageBasedReqs": 5,
      "bugbotUsages": 3,
      "mostUsedModel": "gpt-4",
      "applyMostUsedExtension": ".tsx",
      "tabMostUsedExtension": ".ts",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    },
    {
      "date": 1710806400000,
      "isActive": true,
      "totalLinesAdded": 2104,
      "totalLinesDeleted": 1203,
      "acceptedLinesAdded": 1876,
      "acceptedLinesDeleted": 987,
      "totalApplies": 102,
      "totalAccepts": 91,
      "totalRejects": 11,
      "totalTabsShown": 456,
      "totalTabsAccepted": 398,
      "composerRequests": 67,
      "chatRequests": 156,
      "agentRequests": 23,
      "cmdkUsages": 89,
      "subscriptionIncludedReqs": 320,
      "apiKeyReqs": 15,
      "usageBasedReqs": 0,
      "bugbotUsages": 5,
      "mostUsedModel": "claude-3-opus",
      "applyMostUsedExtension": ".py",
      "tabMostUsedExtension": ".py",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

#### Ejemplo de petición

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### Obtener datos de gastos
</div>

Obtén la información de gastos del mes calendario actual con búsqueda, ordenación y paginación.

```
POST /teams/spend
```

#### Cuerpo de la solicitud

<div className="full-width-table">
  | Parámetro       | Tipo   | Requerido | Descripción                                                  |
  | :-------------- | :----- | :-------- | :----------------------------------------------------------- |
  | `searchTerm`    | string | No        | Busca en nombres de usuario y direcciones de correo          |
  | `sortBy`        | string | No        | Ordena por: `amount`, `date`, `user`. Predeterminado: `date` |
  | `sortDirection` | string | No        | Dirección de orden: `asc`, `desc`. Predeterminado: `desc`    |
  | `page`          | number | No        | Número de página (indexado desde 1). Predeterminado: `1`     |
  | `pageSize`      | number | No        | Resultados por página                                        |
</div>

#### Respuesta

```typescript  theme={null}
{
  teamMemberSpend: {
    spendCents: number;
    fastPremiumRequests: number;
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
    hardLimitOverrideDollars: number;
  }[];
  subscriptionCycleStart: number;
  totalMembers: number;
  totalPages: number;
}
```

<div id="response-fields">
  #### Campos de respuesta
</div>

<div className="full-width-table">
  | Campo                      | Descripción                                                   |
  | :------------------------- | :------------------------------------------------------------ |
  | `spendCents`               | Gasto total en centavos                                       |
  | `fastPremiumRequests`      | Solicitudes al modelo premium rápido                          |
  | `name`                     | Nombre del miembro                                            |
  | `email`                    | Correo electrónico del miembro                                |
  | `role`                     | Rol en el equipo                                              |
  | `hardLimitOverrideDollars` | Anulación del límite de gasto personalizado                   |
  | `subscriptionCycleStart`   | Inicio del ciclo de suscripción (milisegundos desde la época) |
  | `totalMembers`             | Total de miembros del equipo                                  |
  | `totalPages`               | Total de páginas                                              |
</div>

#### Ejemplo de respuesta

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "miembro",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "propietario",
      "hardLimitOverrideDollars": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

#### Solicitudes de ejemplo

**Datos básicos de gastos:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Buscar a un usuario específico con paginación:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

<div id="get-usage-events-data">
  ### Obtener datos de eventos de uso
</div>

Obtén eventos de uso detallados para tu equipo con opciones completas de filtrado, búsqueda y paginación. Este endpoint ofrece información granular sobre llamadas individuales a la API, uso de modelos, consumo de tokens y costos.

```
POST /teams/filtered-usage-events
```

#### Cuerpo de la solicitud

<div className="full-width-table">
  | Parámetro   | Tipo   | Requerido | Descripción                                                |
  | :---------- | :----- | :-------- | :--------------------------------------------------------- |
  | `startDate` | number | No        | Fecha de inicio en milisegundos de época (epoch)           |
  | `endDate`   | number | No        | Fecha de fin en milisegundos de época (epoch)              |
  | `userId`    | number | No        | Filtrar por ID de usuario específico                       |
  | `page`      | number | No        | Número de página (con índice desde 1). Predeterminado: `1` |
  | `pageSize`  | number | No        | Cantidad de resultados por página. Predeterminado: `10`    |
  | `email`     | string | No        | Filtrar por correo electrónico del usuario                 |
</div>

#### Respuesta

```typescript  theme={null}
{
  totalUsageEventsCount: number;
  pagination: {
    numPages: number;
    currentPage: number;
    pageSize: number;
    hasNextPage: boolean;
    hasPreviousPage: boolean;
  };
  usageEvents: {
    timestamp: string;
    model: string;
    kind: string;
    maxMode: boolean;
    requestsCosts: number;
    isTokenBasedCall: boolean;
    tokenUsage?: {
      inputTokens: number;
      outputTokens: number;
      cacheWriteTokens: number;
      cacheReadTokens: number;
      totalCents: number;
    };
    isFreeBugbot: boolean;
    userEmail: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### Campos de respuesta
</div>

<div className="full-width-table">
  | Campo                   | Descripción                                                              |
  | :---------------------- | :----------------------------------------------------------------------- |
  | `totalUsageEventsCount` | Número total de eventos de uso que coinciden con la consulta             |
  | `pagination`            | Metadatos de paginación para navegar los resultados                      |
  | `timestamp`             | Marca de tiempo del evento en milisegundos desde el epoch                |
  | `model`                 | Modelo de IA usado para la solicitud                                     |
  | `kind`                  | Categoría de uso (p. ej., "Usage-based", "Included in Business")         |
  | `maxMode`               | Si el modo máximo estaba habilitado                                      |
  | `requestsCosts`         | Costo en unidades de solicitud                                           |
  | `isTokenBasedCall`      | True cuando el evento se cobra como evento basado en uso                 |
  | `tokenUsage`            | Consumo detallado de tokens (disponible cuando isTokenBasedCall es true) |
  | `isFreeBugbot`          | Si fue un uso gratuito de bugbot                                         |
  | `userEmail`             | Correo del usuario que hizo la solicitud                                 |
  | `period`                | Rango de fechas de los datos consultados                                 |
</div>

#### Ejemplo de respuesta

```json  theme={null}
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "model": "claude-4-opus",
      "kind": "Según uso",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750979173824",
      "model": "claude-4-opus",
      "kind": "Según uso",
      "maxMode": true,
      "requestsCosts": 10,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 5805,
        "outputTokens": 311,
        "cacheWriteTokens": 11964,
        "cacheReadTokens": 0,
        "totalCents": 40.16699999999999
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750978339901",
      "model": "claude-4-sonnet-thinking",
      "kind": "Incluido en Business"
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isFreeBugbot": false,
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

<div id="example-requests">
  #### Ejemplos de solicitudes
</div>

**Obtener todos los eventos de uso con la paginación por defecto:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Filtrar por intervalo de fechas y usuario específico:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**Obtén eventos de uso de un usuario específico con paginación personalizada:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### Establecer límite de gasto por usuario
</div>

Establece límites de gasto para miembros específicos del equipo. Esto te permite controlar cuánto puede gastar cada usuario en uso de IA dentro de tu equipo.

```
POST /teams/user-spend-limit
```

<Note>
  **Limitación de frecuencia:** 60 solicitudes por minuto por equipo
</Note>

#### Cuerpo de la solicitud

<div className="full-width-table">
  | Parámetro           | Tipo   | Obligatorio | Descripción                                                       |
  | :------------------ | :----- | :---------- | :---------------------------------------------------------------- |
  | `userEmail`         | string | Sí          | Dirección de correo del miembro del equipo                        |
  | `spendLimitDollars` | number | Sí          | Límite de gasto en dólares (solo números enteros, sin decimales). |
</div>

<Note>
  * El usuario ya debe ser miembro de tu equipo
  * Solo se aceptan valores enteros (sin decimales)
  * Establecer `spendLimitDollars` en 0 fija el límite en \$0
</Note>

#### Respuesta

Devuelve una respuesta estandarizada que indica si hubo éxito o error:

```typescript  theme={null}
{
  outcome: 'success' | 'error';
  message: string;
}
```

<div id="example-responses">
  #### Respuestas de ejemplo
</div>

**Límite establecido correctamente:**

```json  theme={null}
{
  "outcome": "success",
  "message": "Límite de gasto configurado en $100 para el usuario developer@company.com"
}
```

**Respuesta de error:**

```json  theme={null}
{
  "outcome": "error",
  "message": "Formato de correo electrónico inválido"
}
```

<div id="example-requests">
  #### Ejemplos de solicitudes
</div>

**Configurar un límite de gasto:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u TU_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### API de listas de bloqueo de repos
</div>

Agrega repos y usa patrones para evitar que archivos o directorios se indexen o se usen como contexto para tu equipo.

<div id="get-team-repo-blocklists">
  #### Obtener las blocklists de repos del equipo
</div>

Obtén todas las blocklists de repos configuradas para tu equipo.

```
GET /settings/repo-blocklists/repos
```

<div id="response">
  ##### Respuesta
</div>

Devuelve un array de objetos de lista de bloqueo del repositorio:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-response">
  ##### Ejemplo de respuesta
</div>

```json  theme={null}
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

##### Ejemplo de petición

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u TU_CLAVE_API:
```

<div id="upsert-repo-blocklists">
  #### Upsert de listas de bloqueo de repos
</div>

Reemplaza las listas de bloqueo de repositorios existentes para los repos proporcionados.
*Nota: Este endpoint solo sobrescribirá los patrones de los repositorios proporcionados. Todos los demás repos no se verán afectados.*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### Cuerpo de la solicitud
</div>

| Parámetro | Tipo  | Requerido | Descripción                                 |
| --------- | ----- | --------- | ------------------------------------------- |
| repos     | array | Sí        | Lista de objetos de bloqueo de repositorios |

Cada objeto de repositorio debe contener:

| Campo    | Tipo      | Requerido | Descripción                                                         |
| -------- | --------- | --------- | ------------------------------------------------------------------- |
| url      | string    | Sí        | URL del repositorio a bloquear                                      |
| patterns | string\[] | Sí        | Lista de patrones de archivos a bloquear (se admiten patrones glob) |

<div id="response">
  ##### Respuesta
</div>

Devuelve la lista actualizada de listas de bloqueo del repositorio:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-request">
  ##### Ejemplo de solicitud
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u TU_CLAVE_DE_API: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      },
      {
        "url": "https://github.com/company/internal-tools", 
        "patterns": ["*"]
      }
    ]
  }'
```

<div id="delete-repo-blocklist">
  #### Eliminar la lista de bloqueo de repositorios
</div>

Quita un repositorio específico de la lista de bloqueo.

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### Parámetros
</div>

| Parámetro | Tipo   | Obligatorio | Descripción                                                    |
| --------- | ------ | ----------- | -------------------------------------------------------------- |
| repoId    | string | Sí          | ID de la lista de bloqueo del repositorio que se va a eliminar |

<div id="response">
  ##### Respuesta
</div>

Devuelve 204 No Content si la eliminación se realiza correctamente.

##### Ejemplo de petición

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u TU_API_KEY:
```

<div id="pattern-examples">
  #### Ejemplos de patrones
</div>

Patrones comunes de la blocklist:

* `*` - Bloquear todo el repositorio
* `*.env` - Bloquear todos los archivos .env
* `config/*` - Bloquear todos los archivos del directorio config
* `**/*.secret` - Bloquear todos los archivos .secret en cualquier subdirectorio
* `src/api/keys.ts` - Bloquear un archivo específico

---

← Previous: [Precios](./precios.md) | [Index](./index.md) | Next: [API de seguimiento de código con IA](./api-de-seguimiento-de-cdigo-con-ia.md) →