---
title: "Atajos de teclado"
source: "https://docs.cursor.com/es/configuration/kbd"
language: "es"
language_name: "Spanish"
---

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

---

← Previous: [Usar Agent en la CLI](./usar-agent-en-la-cli.md) | [Index](./index.md) | Next: [Comandos de shell](./comandos-de-shell.md) →