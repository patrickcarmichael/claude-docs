---
title: "Permisos"
source: "https://docs.cursor.com/es/cli/reference/permissions"
language: "es"
language_name: "Spanish"
---

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

---

← Previous: [Parámetros](./parmetros.md) | [Index](./index.md) | Next: [Comandos de barra](./comandos-de-barra.md) →