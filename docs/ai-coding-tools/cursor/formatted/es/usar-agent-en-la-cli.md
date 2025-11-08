---
title: "Usar Agent en la CLI"
source: "https://docs.cursor.com/es/cli/using"
language: "es"
language_name: "Spanish"
---

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

---

← Previous: [Modo Shell](./modo-shell.md) | [Index](./index.md) | Next: [Atajos de teclado](./atajos-de-teclado.md) →