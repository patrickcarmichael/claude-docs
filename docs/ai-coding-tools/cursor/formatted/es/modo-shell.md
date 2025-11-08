---
title: "Modo Shell"
source: "https://docs.cursor.com/es/cli/shell-mode"
language: "es"
language_name: "Spanish"
---

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

---

← Previous: [Comandos de barra](./comandos-de-barra.md) | [Index](./index.md) | Next: [Usar Agent en la CLI](./usar-agent-en-la-cli.md) →