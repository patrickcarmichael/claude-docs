---
title: "MCP"
source: "https://docs.cursor.com/de/cli/mcp"
language: "de"
language_name: "German"
---

# MCP
Source: https://docs.cursor.com/de/cli/mcp

Verwende MCP-Server mit cursor-agent, um externe Tools und Datenquellen anzubinden

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
  ## Überblick
</div>

Die Cursor-CLI unterstützt [Model Context Protocol (MCP)](/de/context/mcp)-Server und ermöglicht dir, externe Tools und Datenquellen mit `cursor-agent` zu verbinden. **MCP in der CLI verwendet dieselbe Konfiguration wie der Editor** – alle von dir eingerichteten MCP-Server funktionieren nahtlos in beiden.

<Card title="Mehr über MCP erfahren" icon="link" href="/de/context/mcp">
  Neu bei MCP? Lies den vollständigen Leitfaden zu Konfiguration, Authentifizierung und verfügbaren Servern
</Card>

<div id="cli-commands">
  ## CLI-Befehle
</div>

Verwende den Befehl `cursor-agent mcp`, um MCP-Server zu verwalten:

<div id="list-configured-servers">
  ### Konfigurierte Server auflisten
</div>

Zeige alle konfigurierten MCP-Server und ihren aktuellen Status an:

```bash  theme={null}
cursor-agent mcp list
```

Das zeigt:

* Servernamen und Bezeichner
* Verbindungsstatus (verbunden/getrennt)
* Konfigurationsquelle (Projekt oder global)
* Transportmethode (stdio, HTTP, SSE)

<div id="list-available-tools">
  ### Verfügbare Tools auflisten
</div>

Tools anzeigen, die von einem bestimmten MCP-Server bereitgestellt werden:

```bash  theme={null}
cursor-agent mcp list-tools <Bezeichner>
```

Dies zeigt:

* Toolnamen und -beschreibungen
* Erforderliche und optionale Parameter
* Parametertypen und -beschränkungen

<div id="login-to-mcp-server">
  ### Beim MCP-Server anmelden
</div>

Authentifiziere dich bei einem in deiner `mcp.json` konfigurierten MCP-Server:

```bash  theme={null}
cursor-agent mcp login <ID>
```

<div id="disable-mcp-server">
  ### MCP-Server deaktivieren
</div>

Entferne einen MCP-Server aus der lokal freigegebenen Liste:

```bash  theme={null}
cursor-agent mcp disable <Bezeichner>
```

<div id="using-mcp-with-agent">
  ## MCP mit Agent verwenden
</div>

Sobald du MCP-Server eingerichtet hast (siehe die [MCP-Hauptanleitung](/de/context/mcp) zur Einrichtung), erkennt und nutzt `cursor-agent` automatisch verfügbare Tools, wenn sie für deine Anfragen relevant sind.

```bash  theme={null}

---

← Previous: [Installation](./installation.md) | [Index](./index.md) | Next: [Cursor CLI](./cursor-cli.md) →