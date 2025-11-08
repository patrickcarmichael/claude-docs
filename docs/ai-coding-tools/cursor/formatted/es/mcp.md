---
title: "MCP"
source: "https://docs.cursor.com/es/cli/mcp"
language: "es"
language_name: "Spanish"
---

# MCP
Source: https://docs.cursor.com/es/cli/mcp

Usa servidores MCP con cursor-agent para conectar herramientas y fuentes de datos externas

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

<div id="overview">
  ## Descripción general
</div>

La CLI de Cursor es compatible con servidores del [Model Context Protocol (MCP)](/es/context/mcp), lo que te permite conectar herramientas externas y fuentes de datos a `cursor-agent`. **MCP en la CLI usa la misma configuración que el editor**: cualquier servidor MCP que hayas configurado funcionará sin problemas en ambos.

<Card title="Aprende sobre MCP" icon="link" href="/es/context/mcp">
  ¿Eres nuevo en MCP? Lee la guía completa sobre configuración, autenticación y servidores disponibles
</Card>

<div id="cli-commands">
  ## Comandos de CLI
</div>

Usa el comando `cursor-agent mcp` para administrar servidores MCP:

<div id="list-configured-servers">
  ### Listar servidores configurados
</div>

Consulta todos los servidores MCP configurados y su estado actual:

```bash  theme={null}
cursor-agent mcp list
```

Esto muestra:

* Nombres e identificadores de servidores
* Estado de la conexión (conectado/desconectado)
* Origen de la configuración (del proyecto o global)
* Método de transporte (stdio, HTTP, SSE)

<div id="list-available-tools">
  ### Listar herramientas disponibles
</div>

Ver las herramientas que proporciona un servidor MCP específico:

```bash  theme={null}
cursor-agent mcp list-tools <id>
```

Esto muestra:

* Nombres y descripciones de herramientas
* Parámetros obligatorios y opcionales
* Tipos de parámetros y restricciones

<div id="login-to-mcp-server">
  ### Inicia sesión en el servidor MCP
</div>

Autentícate con un servidor MCP configurado en tu `mcp.json`:

```bash  theme={null}
cursor-agent mcp login <id>
```

<div id="disable-mcp-server">
  ### Deshabilitar el servidor MCP
</div>

Quita un servidor MCP de la lista local de aprobados:

```bash  theme={null}
cursor-agent mcp disable <identifier>
```

<div id="using-mcp-with-agent">
  ## Usar MCP con Agent
</div>

Una vez que tengas configurados los servidores MCP (consulta la [guía principal de MCP](/es/context/mcp) para la configuración), `cursor-agent` detecta y utiliza automáticamente las herramientas disponibles cuando sean relevantes para tus solicitudes.

```bash  theme={null}

---

← Previous: [Instalación](./instalacin.md) | [Index](./index.md) | Next: [Cursor CLI](./cursor-cli.md) →