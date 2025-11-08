---
title: "Agent in der CLI nutzen"
source: "https://docs.cursor.com/de/cli/using"
language: "de"
language_name: "German"
---

# Agent in der CLI nutzen
Source: https://docs.cursor.com/de/cli/using

Mit der Cursor-CLI effektiv prompten, reviewen und iterieren

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

Formuliere deine Absicht klar, um die besten Ergebnisse zu bekommen. Du kannst zum Beispiel den Prompt „do not write any code“ verwenden, um sicherzustellen, dass der Agent keine Dateien verändert. Das ist besonders hilfreich, wenn du Aufgaben planst, bevor du sie umsetzt.

Der Agent hat derzeit Tools für Dateioperationen, Suche und das Ausführen von Shell-Befehlen. Weitere Tools werden hinzugefügt, ähnlich wie beim IDE-Agenten.

<div id="mcp">
  ## MCP
</div>

Agent unterstützt [MCP (Model Context Protocol)](/de/tools/mcp) für erweiterte Funktionalität und Integrationen. Die CLI erkennt deine `mcp.json`-Konfigurationsdatei automatisch und berücksichtigt sie, sodass dieselben MCP-Server und -Tools genutzt werden, die du für die IDE konfiguriert hast.

<div id="rules">
  ## Regeln
</div>

Der CLI-Agent unterstützt dasselbe [Regelsystem](/de/context/rules) wie die IDE. Du kannst im Verzeichnis `.cursor/rules` Regeln erstellen, um dem Agenten Kontext und Guidance zu geben. Diese Regeln werden basierend auf ihrer Konfiguration automatisch geladen und angewendet, sodass du das Verhalten des Agenten für verschiedene Teile deines Projekts oder bestimmte Dateitypen anpassen kannst.

<Note>
  Die CLI liest außerdem `AGENTS.md` und `CLAUDE.md` im Projektstammverzeichnis (falls vorhanden) und wendet sie zusammen mit `.cursor/rules` als Regeln an.
</Note>

<div id="working-with-agent">
  ## Arbeiten mit Agent
</div>

<div id="navigation">
  ### Navigation
</div>

Vorherige Nachrichten kannst du mit Pfeil nach oben (<Kbd>ArrowUp</Kbd>) aufrufen und durch sie navigieren.

<div id="review">
  ### Review
</div>

Überprüf Änderungen mit <Kbd>Cmd+R</Kbd>. Drück <Kbd>i</Kbd>, um Folgeanweisungen hinzuzufügen. Verwende <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd> zum Scrollen und <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd> zum Dateiwechsel.

<div id="selecting-context">
  ### Kontext auswählen
</div>

Wähle Dateien und Ordner mit <Kbd>@</Kbd> aus, um sie in den Kontext aufzunehmen. Mach Platz im Kontextfenster, indem du `/compress` ausführst. Details findest du unter [Summarization](/de/agent/chat/summarization).

<div id="history">
  ## Verlauf
</div>

Mach mit einem bestehenden Thread weiter mit `--resume [thread id]`, um den vorherigen Kontext zu laden.

Um die neueste Unterhaltung fortzusetzen, nutz `cursor-agent resume`.

Du kannst auch `cursor-agent ls` ausführen, um eine Liste früherer Unterhaltungen anzuzeigen.

<div id="command-approval">
  ## Befehlsfreigabe
</div>

Bevor Terminalbefehle ausgeführt werden, fragt dich die CLI, ob du die Ausführung erlauben (<Kbd>y</Kbd>) oder ablehnen (<Kbd>n</Kbd>) willst.

<div id="non-interactive-mode">
  ## Nicht-interaktiver Modus
</div>

Verwende `-p` oder `--print`, um Agent im nicht-interaktiven Modus auszuführen. Dadurch wird die Antwort in der Konsole ausgegeben.

Im nicht-interaktiven Modus kannst du Agent nicht-interaktiv aufrufen. So kannst du ihn in Skripte, CI-Pipelines usw. integrieren.

Du kannst das mit `--output-format` kombinieren, um zu steuern, wie die Ausgabe formatiert wird. Verwende zum Beispiel `--output-format json` für strukturierte Ausgaben, die sich in Skripten leichter verarbeiten lassen, oder `--output-format text` für reine Textausgaben.

<Note>
  Cursor hat im nicht-interaktiven Modus vollen Schreibzugriff.
</Note>

---

← Previous: [Shell-Modus](./shell-modus.md) | [Index](./index.md) | Next: [Tastenkürzel](./tastenkrzel.md) →