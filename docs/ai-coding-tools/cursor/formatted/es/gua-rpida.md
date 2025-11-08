---
title: "Guía rápida"
source: "https://docs.cursor.com/es/get-started/quickstart"
language: "es"
language_name: "Spanish"
---

# Guía rápida
Source: https://docs.cursor.com/es/get-started/quickstart

Comenzá con Cursor en 5 minutos

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

Esta guía rápida te llevará por un proyecto usando las funciones principales de Cursor. Al final, ya estarás familiarizado con Tab, Inline Edit y Agent.

<div id="open-a-project-in-cursor">
  ## Abre un proyecto en Cursor
</div>

Usa un proyecto existente o clona nuestro ejemplo:

<Tabs>
  <Tab title="Clona el proyecto de ejemplo">
    1. Asegúrate de tener git instalado
    2. Clona el proyecto de ejemplo:

    ```bash  theme={null}
    git clone git@github.com:voxelize/voxelize.git && \
    cd voxelize && \
    cursor .
    ```
  </Tab>

  <Tab title="Usa un proyecto existente">
    1. Abre Cursor
    2. Abre una carpeta de proyecto con <Kbd>Cmd O</Kbd> o `cursor <ruta-al-proyecto>`
  </Tab>
</Tabs>

Vamos a mostrarlo con el proyecto de ejemplo, pero puedes usar cualquier proyecto que tengas en local.

<div id="autocomplete-with-tab">
  ## Autocomplete con [Tab](/es/kbd#tab)
</div>

Tab es el modelo de autocompletado que entrenamos internamente. Es una gran forma de empezar con el código asistido por IA si no estás acostumbrado. Con Tab, podés:

* Autocompletar **múltiples líneas y bloques** de código
* Saltar **dentro** y **entre** archivos a la siguiente sugerencia de autocompletado

1. Empezá a escribir el comienzo de una función:
   ```javascript  theme={null}
   function calculate
   ```
2. Las sugerencias de Tab aparecen automáticamente
3. Presioná Tab para aceptar la sugerencia
4. Cursor sugiere parámetros y cuerpos de funciones

<div id="inline-edit-a-selection">
  ## [Edición en línea](/es/inline-edit) de una selección
</div>

1. Selecciona la función que acabas de crear
2. Presiona <Kbd>Cmd K</Kbd>
3. Escribe "make this function calculate Fibonacci numbers"
4. Presiona <Kbd>Return</Kbd> para aplicar los cambios
5. Cursor agrega imports y documentación

<div id="chat-with-agent">
  ## Chatea con [Agent](/es/agent)
</div>

1. Abre el panel de chat (<Kbd>Cmd I</Kbd>)
2. Di: "Add tests for this function and run them"
3. Agent creará un archivo de pruebas, escribirá casos de prueba y los ejecutará por ti

<div id="bonus">
  ## Bonus
</div>

Funciones avanzadas:

<AccordionGroup>
  <Accordion title="Delegar trabajo a Background Agent">
    1. Abre el panel de control de Background Agent (<Kbd>Cmd E</Kbd>)
    2. Pide: "Find and fix a bug in this project"
    3. [Background Agent](/es/background-agent) hará lo siguiente:
       * Crear una máquina virtual (VM) remota
       * Explorar tu proyecto
       * Detectar errores
       * Proponer correcciones

    Revisa y aplica los cambios.
  </Accordion>

  {" "}

  <Accordion title="Escribir una regla">
    1. Abre la paleta de comandos (<Kbd>Cmd Shift P</Kbd>) 2. Busca: "New Cursor
       Rule" 3. Ponle un nombre (p. ej., `style-guide`) 4. Selecciona el tipo de regla "Always" 5. Define
       tu estilo: `Prefer using camelCase for variable names`
  </Accordion>

  <Accordion title="Configurar un servidor MCP">
    1. Visita nuestro [directorio de MCP](https://docs.cursor.com/tools)
    2. Elige una herramienta
    3. Haz clic en "Install"

    Los servidores también se pueden instalar manualmente:

    1. Abre Cursor Settings (<Kbd>Cmd Shift J</Kbd>)
    2. Ve a "Tools & Integrations"
    3. Haz clic en "New MCP Server"
  </Accordion>
</AccordionGroup>

<div id="next-steps">
  ## Próximos pasos
</div>

Explora estas guías para aprender más:

<CardGroup cols={2}>
  <Card title="Working with Context" href="/es/guides/working-with-context">
    Proporciona un buen contexto para obtener mejores resultados
  </Card>

  <Card title="Selecting Models" href="/es/guides/selecting-models">
    Elige el modelo adecuado para tu tarea
  </Card>
</CardGroup>

Aprende todos los [conceptos de Cursor](/es/get-started/concepts) y ¡empieza a crear!

---

← Previous: [Instalación](./instalacin.md) | [Index](./index.md) | Next: [Ciencia de datos](./ciencia-de-datos.md) →