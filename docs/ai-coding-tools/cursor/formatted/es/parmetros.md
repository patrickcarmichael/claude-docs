---
title: "Parámetros"
source: "https://docs.cursor.com/es/cli/reference/parameters"
language: "es"
language_name: "Spanish"
---

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

---

← Previous: [Formato de salida](./formato-de-salida.md) | [Index](./index.md) | Next: [Permisos](./permisos.md) →