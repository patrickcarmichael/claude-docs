---
title: "Formato de salida"
source: "https://docs.cursor.com/es/cli/reference/output-format"
language: "es"
language_name: "Spanish"
---

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

---

← Previous: [Configuración](./configuracin.md) | [Index](./index.md) | Next: [Parámetros](./parmetros.md) →