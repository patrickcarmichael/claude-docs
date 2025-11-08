---
title: "Model Context Protocol (MCP)"
source: "https://docs.cursor.com/de/context/mcp"
language: "de"
language_name: "German"
---

# Model Context Protocol (MCP)
Source: https://docs.cursor.com/de/context/mcp

Externe Tools und Datenquellen per MCP mit Cursor verbinden

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

<div id="what-is-mcp">
  ## Was ist MCP?
</div>

Das [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) ermöglicht Cursor die Verbindung zu externen Tools und Datenquellen.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
</Frame>

<div id="why-use-mcp">
  ### Warum MCP verwenden?
</div>

MCP verbindet Cursor mit externen Systemen und Daten. Anstatt deine Projektstruktur immer wieder zu erklären, integrier dich direkt mit deinen Tools.

Schreib MCP-Server in jeder Sprache, die auf `stdout` ausgeben oder einen HTTP-Endpoint bereitstellen kann – Python, JavaScript, Go, etc.

### So funktioniert's

MCP-Server stellen Fähigkeiten über das Protokoll bereit und verbinden Cursor mit externen Tools oder Datenquellen.

Cursor unterstützt drei Transportmethoden:

<div className="full-width-table">
  | Transport                                                        | Ausführungsumgebung | Bereitstellung           | Nutzer           | Eingabe                    | Auth    |
  | :--------------------------------------------------------------- | :------------------ | :----------------------- | :--------------- | :------------------------- | :------ |
  | **<span className="whitespace-nowrap">`stdio`</span>**           | Lokal               | Von Cursor verwaltet     | Einzelner Nutzer | Shell-Befehl               | Manuell |
  | **<span className="whitespace-nowrap">`SSE`</span>**             | Lokal/Remote        | Als Server bereitstellen | Mehrere Nutzer   | URL zu einem SSE-Endpunkt  | OAuth   |
  | **<span className="whitespace-nowrap">`Streamable HTTP`</span>** | Lokal/Remote        | Als Server bereitstellen | Mehrere Nutzer   | URL zu einem HTTP-Endpunkt | OAuth   |
</div>

<div id="protocol-support">
  ### Protokollunterstützung
</div>

Cursor unterstützt diese MCP-Protokollfunktionen:

<div className="full-width-table">
  | Feature         | Support   | Description                                                                                            |
  | :-------------- | :-------- | :----------------------------------------------------------------------------------------------------- |
  | **Tools**       | Supported | Funktionen, die das KI-Modell ausführen kann                                                           |
  | **Prompts**     | Supported | Vorlagenbasierte Nachrichten und Workflows für Nutzer                                                  |
  | **Resources**   | Supported | Strukturierte Datenquellen, die gelesen und referenziert werden können                                 |
  | **Roots**       | Supported | Vom Server initiierte Abfragen zu URI- oder Dateisystemgrenzen, innerhalb derer gearbeitet werden kann |
  | **Elicitation** | Supported | Vom Server initiierte Anforderungen nach zusätzlichen Informationen von Nutzern                        |
</div>

<div id="installing-mcp-servers">
  ## MCP-Server installieren
</div>

<div id="one-click-installation">
  ### Installation mit einem Klick
</div>

Installier MCP-Server aus unserer Sammlung und authentifizier dich per OAuth.

<Columns cols={2}>
  <Card title="MCP-Tools durchsuchen" icon="table" horizontal href="/de/tools">
    Verfügbare MCP-Server durchsuchen
  </Card>

  <Card title="„Zu Cursor hinzufügen“-Button" icon="plus" horizontal href="/de/deeplinks">
    Einen „Zu Cursor hinzufügen“-Button erstellen
  </Card>
</Columns>

<div id="using-mcpjson">
  ### Verwendung von `mcp.json`
</div>

Konfigurier benutzerdefinierte MCP-Server mit einer JSON-Datei:

<CodeGroup>
  ```json CLI Server - Node.js theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "npx",
        "args": ["-y", "mcp-server"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json CLI Server - Python theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "python",
        "args": ["mcp-server.py"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json Remote Server theme={null}
  // MCP-Server über HTTP oder SSE – läuft auf einem Server
  {
    "mcpServers": {
      "server-name": {
        "url": "http://localhost:3000/mcp",
        "headers": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```
</CodeGroup>

<div id="stdio-server-configuration">
  ### STDIO-Serverkonfiguration
</div>

Für STDIO-Server (lokale Kommandozeilenserver) konfigurier diese Felder in deiner `mcp.json`:

<div className="full-width-table">
  | Feld        | Erforderlich | Beschreibung                                                                                                          | Beispiele                                 |
  | :---------- | :----------- | :-------------------------------------------------------------------------------------------------------------------- | :---------------------------------------- |
  | **type**    | Ja           | Verbindungstyp des Servers                                                                                            | `"stdio"`                                 |
  | **command** | Ja           | Befehl zum Starten der Server-Binary. Muss in deinem Systempfad verfügbar sein oder den vollständigen Pfad enthalten. | `"npx"`, `"node"`, `"python"`, `"docker"` |
  | **args**    | Nein         | Array von Argumenten, die an den Befehl übergeben werden                                                              | `["server.py", "--port", "3000"]`         |
  | **env**     | Nein         | Umgebungsvariablen für den Server                                                                                     | `{"API_KEY": "${input:api-key}"}`         |
  | **envFile** | Nein         | Pfad zu einer Umgebungsdatei, um weitere Variablen zu laden                                                           | `".env"`, `"${workspaceFolder}/.env"`     |
</div>

<div id="using-the-extension-api">
  ### Verwendung der Extension-API
</div>

Für die programmgesteuerte Registrierung von MCP-Servern stellt Cursor eine Extension-API bereit, die eine dynamische Konfiguration ermöglicht, ohne `mcp.json`-Dateien anzupassen. Das ist besonders nützlich für Enterprise-Umgebungen und automatisierte Setup-Workflows.

<Card title="MCP Extension API Reference" icon="code" href="/de/context/mcp-extension-api">
  Erfahre, wie du MCP-Server programmgesteuert mit `vscode.cursor.mcp.registerServer()` registrierst
</Card>

<div id="configuration-locations">
  ### Speicherorte für Konfiguration
</div>

<CardGroup cols={2}>
  <Card title="Projektkonfiguration" icon="folder-tree">
    Erstell in deinem Projekt die Datei `.cursor/mcp.json` für projektspezifische Tools.
  </Card>

  <Card title="Globale Konfiguration" icon="globe">
    Erstell in deinem Home-Verzeichnis die Datei `~/.cursor/mcp.json` für Tools, die überall verfügbar sind.
  </Card>
</CardGroup>

<div id="config-interpolation">
  ### Konfigurationsinterpolation
</div>

Verwende Variablen in `mcp.json`-Werten. Cursor ersetzt Variablen in diesen Feldern: `command`, `args`, `env`, `url` und `headers`.

Unterstützte Syntax:

* `${env:NAME}` Umgebungsvariablen
* `${userHome}` Pfad zu deinem Home-Verzeichnis
* `${workspaceFolder}` Projektstamm (der Ordner, der `.cursor/mcp.json` enthält)
* `${workspaceFolderBasename}` Name des Projektstamms
* `${pathSeparator}` und `${/}` Betriebssystem-Pfadtrennzeichen

Beispiele

```json  theme={null}
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

```json  theme={null}
{
  "mcpServers": {
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    }
  }
}
```

<div id="authentication">
  ### Authentifizierung
</div>

MCP-Server verwenden Umgebungsvariablen für die Authentifizierung. Übergib API-Schlüssel und Tokens über die Konfiguration.

Cursor unterstützt OAuth für Server, die es erfordern.

<div id="using-mcp-in-chat">
  ## MCP im Chat verwenden
</div>

Der Composer-Agent nutzt automatisch relevante MCP-Tools, die unter `Available Tools` aufgeführt sind. Frag nach einem bestimmten Tool beim Namen oder beschreib, was du brauchst. Aktiviere oder deaktiviere Tools in den Einstellungen.

<div id="toggling-tools">
  ### Tools umschalten
</div>

Aktiviere oder deaktiviere MCP-Tools direkt in der Chatoberfläche. Klick in der Toolliste auf einen Toolnamen, um ihn umzuschalten. Deaktivierte Tools werden nicht in den Kontext geladen und sind für den Agent nicht verfügbar.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-toggle.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fa3060f593cae3e5fb7c7d2f041a715" autoPlay loop muted playsInline controls data-path="images/context/mcp/tool-toggle.mp4" />
</Frame>

<div id="tool-approval">
  ### Toolfreigabe
</div>

Der Agent fragt standardmäßig nach deiner Freigabe, bevor er MCP-Tools verwendet. Klick auf den Pfeil neben dem Toolnamen, um die Argumente anzuzeigen.

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bf9b19d5f23abc65914f712185b3ec72" alt="" data-og-width="1212" width="1212" data-og-height="902" height="902" data-path="images/context/mcp/tool-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e3f900fad0b8f2a469460c70fa1dd1dc 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de2f90138de39d75d70c5800f13be93a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b9c616ce7a4080ea4088a0fdd0050c7c 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3f783e62a7a31957b8988edb97c139f9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10bf2c1dbfd5c2a03aa95334f53cd571 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=231c0e3cd60df5ad12455d5e8ef308d2 2500w" /></Frame>

<div id="auto-run">
  #### Auto-Run
</div>

Aktiviere Auto-Run, damit der Agent MCP-Tools ohne Rückfrage nutzen kann. Funktioniert wie Terminal-Befehle. Mehr über die Auto-Run-Einstellungen findest du [hier](/de/agent/tools#auto-run).

<div id="tool-response">
  ### Tool-Antwort
</div>

Cursor zeigt die Antwort im Chat mit aufklappbaren Ansichten von Argumenten und Ergebnissen:

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=30af3f35869e9a78781f455bdbc0e3b5" alt="" data-og-width="1212" width="1212" data-og-height="952" height="952" data-path="images/context/mcp/tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8821ac7bad00ad54a18abc614c2e3d5c 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9d55f089ad53a89da99b8ddd524f6de 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a107d68a1fb05ed43851548b34fb4496 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b409b4941c2fd783043770fad0bd6390 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2a331b5e2bb9be0b9659393157454c2e 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=585b769dfa2a5114b111eb901a969845 2500w" /></Frame>

<div id="images-as-context">
  ### Bilder als Kontext
</div>

MCP-Server können Bilder zurückgeben – Screenshots, Diagramme usw. Gib sie als Base64-codierte Strings zurück:

```js  theme={null}
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ vollständiger Base64-String aus Gründen der Lesbarkeit gekürzt

server.tool("generate_image", async (params) => {
  return {
    content: [
      {
        type: "image",
        data: RED_CIRCLE_BASE64,
        mimeType: "image/jpeg",
      },
    ],
  };
});
```

Sieh dir diesen [Beispielserver](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js) für Implementierungsdetails an. Cursor hängt zurückgegebene Bilder im Chat an. Wenn das Modell Bilder unterstützt, analysiert es sie.

<div id="security-considerations">
  ## Sicherheitshinweise
</div>

Wenn du MCP-Server installierst, beachte diese Sicherheitspraktiken:

* **Quelle überprüfen**: Installiere MCP-Server nur von vertrauenswürdigen Entwickler\*innen und Repositories
* **Berechtigungen prüfen**: Schau nach, auf welche Daten und APIs der Server zugreift
* **API-Schlüssel einschränken**: Verwende eingeschränkte API-Schlüssel mit minimal notwendigen Berechtigungen
* **Code prüfen**: Für kritische Integrationen den Quellcode des Servers überprüfen

Denk daran, dass MCP-Server auf externe Dienste zugreifen und in deinem Namen Code ausführen können. Versteh immer genau, was ein Server macht, bevor du ihn installierst.

<div id="real-world-examples">
  ## Praxisnahe Beispiele
</div>

Für praktische Beispiele von MCP in Aktion schau dir unseren [Web-Development-Guide](/de/guides/tutorials/web-development) an. Er zeigt, wie du Linear, Figma und Browser-Tools in deinen Entwicklungsworkflow integrierst.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Wozu sind MCP-Server gut?">
    MCP-Server verbinden Cursor mit externen Tools wie Google Drive, Notion und
    anderen Diensten, um Dokus und Anforderungen direkt in deinen Coding-Workflow zu holen.
  </Accordion>

  {" "}

  <Accordion title="Wie debugge ich Probleme mit MCP-Servern?">
    So checkst du MCP-Logs: 1. Öffne das Output-Panel in Cursor (<Kbd>Cmd+Shift+U</Kbd>)
    2\. Wähle „MCP Logs“ aus dem Dropdown 3. Prüfe auf Verbindungsfehler,
    Authentifizierungsprobleme oder Serverabstürze. Die Logs zeigen Serverinitialisierung,
    Tool-Aufrufe und Fehlermeldungen.
  </Accordion>

  {" "}

  <Accordion title="Kann ich einen MCP-Server vorübergehend deaktivieren?">
    Ja! Du kannst Server an- oder ausschalten, ohne sie zu entfernen: 1. Öffne die Settings (
    <Kbd>Cmd+Shift+J</Kbd>) 2. Geh zu Features → Model Context Protocol 3. Klick
    den Toggle neben einem Server, um ihn zu aktivieren/deaktivieren. Deaktivierte Server werden nicht geladen und
    erscheinen nicht im Chat. Das ist hilfreich fürs Troubleshooting oder um Tool-Clutter zu reduzieren.
  </Accordion>

  {" "}

  <Accordion title="Was passiert, wenn ein MCP-Server abstürzt oder ein Timeout hat?">
    Wenn ein MCP-Server fehlschlägt: - Cursor zeigt eine Fehlermeldung im Chat - Der Tool-
    Aufruf wird als fehlgeschlagen markiert - Du kannst die Aktion erneut ausführen oder die Logs für
    Details checken - Andere MCP-Server laufen normal weiter. Cursor isoliert Server-
    Ausfälle, damit ein Server die anderen nicht beeinflusst.
  </Accordion>

  {" "}

  <Accordion title="Wie aktualisiere ich einen MCP-Server?">
    Für npm-basierte Server: 1. Entferne den Server aus den Settings 2. Leere den npm-Cache:
    `npm cache clean --force` 3. Füge den Server erneut hinzu, um die neueste Version zu erhalten. Für
    Custom-Server aktualisiere deine lokalen Dateien und starte Cursor neu.
  </Accordion>

  <Accordion title="Kann ich MCP-Server mit sensiblen Daten verwenden?">
    Ja, aber befolge Security-Best Practices: - Verwende Environment-Variablen für
    Secrets, niemals hardcoden - Führe sensible Server lokal mit `stdio`-
    Transport aus - Beschränke API-Key-Berechtigungen auf das Nötigste - Reviewe den Server-
    Code, bevor du ihn mit sensiblen Systemen verbindest - Zieh in Betracht, Server in
    isolierten Umgebungen laufen zu lassen
  </Accordion>
</AccordionGroup>

---

← Previous: [Dateien ignorieren](./dateien-ignorieren.md) | [Index](./index.md) | Next: [Memories](./memories.md) →