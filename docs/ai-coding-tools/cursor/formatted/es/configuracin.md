---
title: "Configuración"
source: "https://docs.cursor.com/es/cli/reference/configuration"
language: "es"
language_name: "Spanish"
---

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

---

← Previous: [Autenticación](./autenticacin.md) | [Index](./index.md) | Next: [Formato de salida](./formato-de-salida.md) →