---
title: "Schnellstart"
source: "https://docs.cursor.com/de/get-started/quickstart"
language: "de"
language_name: "German"
---

# Schnellstart
Source: https://docs.cursor.com/de/get-started/quickstart

Starte mit Cursor in 5 Minuten

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

Dieses Quickstart führt dich durch ein Projekt mit den Kernfunktionen von Cursor. Am Ende bist du mit Tab, Inline Edit und Agent vertraut.

<div id="open-a-project-in-cursor">
  ## Öffne ein Projekt in Cursor
</div>

Verwende ein bestehendes Projekt oder klone unser Beispiel:

<Tabs>
  <Tab title="Beispielprojekt klonen">
    1. Stell sicher, dass Git installiert ist
    2. Klone das Beispielprojekt:

    ```bash  theme={null}
    git clone git@github.com:voxelize/voxelize.git && \
    cd voxelize && \
    cursor .
    ```
  </Tab>

  <Tab title="Bestehendes Projekt nutzen">
    1. Öffne Cursor
    2. Öffne einen Projektordner mit <Kbd>Cmd O</Kbd> oder `cursor <path-to-project>`
  </Tab>
</Tabs>

Wir zeigen das Ganze am Beispielprojekt, aber du kannst jedes beliebige lokale Projekt verwenden.

<div id="autocomplete-with-tab">
  ## Autocomplete mit [Tab](/de/kbd#tab)
</div>

Tab ist das Autocomplete-Modell, das wir intern trainiert haben. Es ist ein guter Weg, um entspannt in KI-unterstütztes Coden reinzukommen, wenn du noch nicht dran gewöhnt bist. Mit Tab kannst du:

* **Mehrere Zeilen und Blöcke** Code automatisch vervollständigen
* **In** Dateien und **über** Dateien hinweg zur nächsten Autocomplete-Eingabe springen

1. Fang an, den Anfang einer Funktion zu tippen:
   ```javascript  theme={null}
   function calculate
   ```
2. Tab-Vorschläge erscheinen automatisch
3. Drück Tab, um den Vorschlag zu übernehmen
4. Cursor schlägt Parameter und Funktionskörper vor

<div id="inline-edit-a-selection">
  ## [Inline Edit](/de/inline-edit) für eine Auswahl
</div>

1. Wähl die Funktion aus, die du gerade erstellt hast
2. Drück <Kbd>Cmd K</Kbd>
3. Tipp „make this function calculate fibonacci numbers“
4. Drück <Kbd>Return</Kbd>, um die Änderungen anzuwenden
5. Cursor fügt Importe und Dokumentation hinzu

<div id="chat-with-agent">
  ## Chat mit [Agent](/de/agent)
</div>

1. Öffne das Chat-Panel (<Kbd>Cmd I</Kbd>)
2. Sag: „Füg dieser Funktion Tests hinzu und führ sie aus“
3. Der Agent erstellt eine Testdatei, schreibt Testfälle und führt sie für dich aus

<div id="bonus">
  ## Bonus
</div>

Erweiterte Funktionen:

<AccordionGroup>
  <Accordion title="Arbeit an den Background Agent übergeben">
    1. Öffne das Background-Agent-Control-Panel (<Kbd>Cmd E</Kbd>)
    2. Frag: „Find and fix a bug in this project“
    3. Der [Background Agent](/de/background-agent) wird:
       * Eine Remote-VM (Virtual Machine) erstellen
       * Dein Projekt erkunden
       * Bugs erkennen
       * Fixes vorschlagen

    Änderungen prüfen und anwenden.
  </Accordion>

  {" "}

  <Accordion title="Eine Regel schreiben">
    1. Öffne die Command Palette (<Kbd>Cmd Shift P</Kbd>) 2. Such: „New Cursor
       Rule“ 3. Benenn sie (z. B. `style-guide`) 4. Wähl als Rule Type „Always“ 5. Definiere
       deinen Stil: `Prefer using camelCase for variable names`
  </Accordion>

  <Accordion title="Einen MCP-Server einrichten">
    1. Besuch unser [MCP-Verzeichnis](https://docs.cursor.com/tools)
    2. Wähl ein Tool
    3. Klick auf „Install“

    Server können auch manuell installiert werden:

    1. Öffne die Cursor Settings (<Kbd>Cmd Shift J</Kbd>)
    2. Geh zu „Tools & Integrations“
    3. Klick auf „New MCP Server“
  </Accordion>
</AccordionGroup>

<div id="next-steps">
  ## Nächste Schritte
</div>

Schau dir diese Guides an, um mehr zu erfahren:

<CardGroup cols={2}>
  <Card title="Working with Context" href="/de/guides/working-with-context">
    Liefere effektiven Kontext für bessere Ergebnisse
  </Card>

  <Card title="Selecting Models" href="/de/guides/selecting-models">
    Wähle das passende Modell für deine Aufgabe
  </Card>
</CardGroup>

Lerne alle [Cursor-Konzepte](/de/get-started/concepts) kennen und leg los!

---

← Previous: [Installation](./installation.md) | [Index](./index.md) | Next: [Data Science](./data-science.md) →