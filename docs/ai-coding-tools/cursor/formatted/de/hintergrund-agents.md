---
title: "Hintergrund-Agents"
source: "https://docs.cursor.com/de/background-agent"
language: "de"
language_name: "German"
---

# Hintergrund-Agents
Source: https://docs.cursor.com/de/background-agent

Asynchrone Remote-Agents in Cursor

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

Mit Background Agents spawnst du asynchrone Agents, die Code in einer Remote-Umgebung bearbeiten und ausführen. Sieh dir ihren Status an, schick Follow-ups oder übernimm jederzeit.

<div id="how-to-use">
  ## Verwendung
</div>

Du kannst auf Background Agents auf zwei Arten zugreifen:

1. **Background-Agenten-Seitenleiste**: Nutze den Tab für Background Agents in der nativen Cursor-Seitenleiste, um alle mit deinem Account verknüpften Background Agents anzuzeigen, bestehende Agents zu durchsuchen und neue zu starten.
2. **Background-Agent-Mode**: Drück <Kbd tooltip="Trigger background agent mode">Cmd E</Kbd>, um den Background-Agent-Mode in der UI zu aktivieren.

Nachdem du eine Eingabe abgeschickt hast, wähl deinen Agent aus der Liste, um den Status anzusehen und in die Machine einzusteigen.

<Note>
  <p className="!mb-0">
    Background Agents benötigen eine Datenaufbewahrung über einige Tage.
  </p>
</Note>

<div id="setup">
  ## Setup
</div>

Background-Agents laufen standardmäßig auf einer isolierten, Ubuntu-basierten Maschine. Die Agents haben Internetzugang und können Pakete installieren.

<div id="github-connection">
  #### GitHub-Verbindung
</div>

Background Agents klonen dein Repo von GitHub und arbeiten auf einem eigenen Branch; sie pushen ihre Änderungen in dein Repo, damit die Übergabe leicht fällt.

Gewähre Lese- und Schreibrechte für dein Repo (sowie alle abhängigen Repos oder Submodule). In Zukunft werden wir weitere Anbieter (GitLab, Bitbucket usw.) unterstützen.

<div id="ip-allow-list-configuration">
  ##### Konfiguration der IP-Allowlist
</div>

Wenn deine Organisation die IP-Allowlist-Funktion von GitHub verwendet, musst du den Zugriff für Hintergrund-Agents konfigurieren. Sieh dir die [GitHub-Integrationsdokumentation](/de/integrations/github#ip-allow-list-configuration) für vollständige Setup-Anweisungen inklusive Kontaktinformationen und IP-Adressen an.

<div id="base-environment-setup">
  #### Basis-Setup der Umgebung
</div>

Für fortgeschrittene Fälle richtest du die Umgebung selbst ein. Hol dir eine IDE-Instanz, die mit der Remote-Maschine verbunden ist. Richte deine Maschine ein, installiere Tools und Pakete und erstelle dann einen Snapshot. Konfiguriere die Runtime-Einstellungen:

* Der Install-Befehl läuft, bevor ein Agent startet, und installiert Runtime-Abhängigkeiten. Das kann bedeuten, `npm install` oder `bazel build` auszuführen.
* Terminals starten Hintergrundprozesse, während der Agent arbeitet – etwa einen Webserver oder das Kompilieren von Protobuf-Dateien.

Für die anspruchsvollsten Fälle nutze eine Dockerfile für das Maschinen-Setup. Die Dockerfile erlaubt dir, Systemabhängigkeiten einzurichten: bestimmte Compiler-Versionen installieren, Debugger hinzufügen oder das Basis-OS-Image wechseln. Kopiere nicht das gesamte Projekt mit `COPY` – wir verwalten den Workspace und checken den korrekten Commit aus. Die Installation von Abhängigkeiten gehört weiterhin ins Install-Skript.

Gib alle benötigten Secrets für deine Dev-Umgebung ein – sie werden verschlüsselt im Ruhezustand (mit KMS) in unserer Datenbank gespeichert und dem Agent im Hintergrund bereitgestellt.

Das Maschinen-Setup liegt in `.cursor/environment.json`, was in deinem Repo committed werden kann (empfohlen) oder privat gespeichert wird. Der Setup-Flow führt dich durch das Erstellen von `environment.json`.

<div id="maintenance-commands">
  #### Wartungsbefehle
</div>

Beim Einrichten einer neuen Maschine starten wir mit der Basisumgebung und führen dann den `install`-Befehl aus deiner `environment.json` aus. Das ist der Befehl, den ein Developer beim Wechseln von Branches ausführen würde – um neue Dependencies zu installieren.

Für die meisten ist der `install`-Befehl `npm install` oder `bazel build`.

Damit die Maschine schnell startet, cachen wir den Disk-Status, nachdem der `install`-Befehl gelaufen ist. Gestalte ihn so, dass er mehrfach ausgeführt werden kann. Es bleibt nur der Disk-Status aus dem `install`-Befehl bestehen – Prozesse, die hier gestartet werden, laufen nicht mehr, wenn der Agent startet.

<div id="startup-commands">
  #### Startup-Befehle
</div>

Nachdem `install` ausgeführt wurde, startet die Maschine und wir führen den Befehl `start` aus, gefolgt vom Starten aller `terminals`. Dadurch werden Prozesse gestartet, die laufen sollten, wenn der Agent aktiv ist.

Den Befehl `start` kannst du oft überspringen. Nutz ihn, wenn deine Dev-Umgebung auf Docker setzt – pack `sudo service docker start` in den `start`-Befehl.

`terminals` sind für App-Code. Diese Terminals laufen in einer `tmux`-Session, die dir und dem Agent zur Verfügung steht. Viele Website-Repos hinterlegen zum Beispiel `npm run watch` als Terminal.

<div id="the-environmentjson-spec">
  #### Die Spezifikation von `environment.json`
</div>

Die Datei `environment.json` kann so aussehen:

```json  theme={null}
{
  "snapshot": "POPULATED_FROM_SETTINGS",
  "install": "npm install",
  "terminals": [
    {
      "name": "Next.js ausführen",
      "command": "npm run dev"
    }
  ]
}
```

Formal ist die Spezifikation [hier definiert](https://www.cursor.com/schemas/environment.schema.json).

<div id="models">
  ## Modelle
</div>

Für Hintergrund-Agents sind nur Modelle verfügbar, die mit [Max Mode](/de/context/max-mode) kompatibel sind.

<div id="pricing">
  ## Preise
</div>

Erfahre mehr über die [Preise des Background Agents](/de/account/pricing#background-agent).

<div id="security">
  ## Sicherheit
</div>

Background Agents sind im Privacy Mode verfügbar. Wir trainieren niemals auf deinem Code und behalten Code nur so lange, wie der Agent läuft. [Erfahre mehr über den Privacy Mode](https://www.cursor.com/privacy-overview).

Was du wissen solltest:

1. Gewähre unserer GitHub-App Lese- und Schreibrechte für die Repos, die du bearbeiten willst. Wir nutzen das, um das Repo zu klonen und Änderungen vorzunehmen.
2. Dein Code läuft in unserer AWS-Infrastruktur in isolierten VMs und wird auf VM-Datenträgern gespeichert, solange der Agent aktiv ist.
3. Der Agent hat Internetzugang.
4. Der Agent führt alle Terminalbefehle automatisch aus, sodass er Tests iterativ ausführen kann. Das unterscheidet sich vom Foreground Agent, der für jeden Befehl deine Zustimmung benötigt. Automatisches Ausführen birgt ein Risiko der Datenexfiltration: Angreifer könnten Prompt-Injection-Angriffe durchführen und den Agenten dazu bringen, Code auf bösartige Websites hochzuladen. Siehe [OpenAIs Erklärung zu Risiken von Prompt Injection für Background Agents](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access).
5. Wenn der Privacy Mode deaktiviert ist, sammeln wir Prompts und Entwicklungsumgebungen, um das Produkt zu verbessern.
6. Wenn du den Privacy Mode beim Start eines Background Agents deaktivierst und ihn dann während der Laufzeit wieder aktivierst, läuft der Agent weiter mit deaktiviertem Privacy Mode, bis er fertig ist.

<div id="dashboard-settings">
  ## Dashboard-Einstellungen
</div>

Workspace-Admins können zusätzliche Einstellungen auf dem Dashboard im Tab „Background Agents“ konfigurieren.

<div id="defaults-settings">
  ### Standard-Einstellungen
</div>

* **Standardmodell** – das Modell, das verwendet wird, wenn ein Run keins angibt. Wähle ein beliebiges Modell, das den Max Mode unterstützt.
* **Standard-Repository** – wenn leer, bitten die Agents dich, ein Repo auszuwählen. Wenn du hier ein Repo angibst, kannst du diesen Schritt überspringen.
* **Basis-Branch** – der Branch, von dem die Agents beim Erstellen von Pull Requests forken. Leer lassen, um den Standard-Branch des Repositories zu verwenden.

<div id="security-settings">
  ### Sicherheitseinstellungen
</div>

Alle Sicherheitsoptionen erfordern Admin-Rechte.

* **Nutzungsbeschränkungen** – wähle *Keine* (alle Mitglieder können Hintergrund-Agents starten) oder *Allow List*. Wenn *Allow List* aktiv ist, legst du genau fest, welche Teammitglieder Agents erstellen dürfen.
* **Team-Follow-ups** – wenn aktiviert, kann jede Person im Workspace Folge­nachrichten zu einem Agent hinzufügen, den jemand anderes gestartet hat. Deaktiviere das, um Follow-ups auf den Agent-Owner und Admins zu beschränken.
* **Agent-Zusammenfassung anzeigen** – steuert, ob Cursor die File-Diff-Bilder und Code-Snippets des Agents anzeigt. Deaktiviere das, wenn du keine Dateipfade oder Code in der Seitenleiste anzeigen lassen willst.
* **Agent-Zusammenfassung in externen Kanälen anzeigen** – erweitert den vorherigen Schalter auf Slack oder jeden verbundenen externen Kanal.

Änderungen werden sofort gespeichert und gelten sofort für neue Agents.

---

← Previous: [Tools](./tools.md) | [Index](./index.md) | Next: [Nachverfolgung hinzufügen](./nachverfolgung-hinzufgen.md) →