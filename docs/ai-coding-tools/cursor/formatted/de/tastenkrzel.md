---
title: "Tastenkürzel"
source: "https://docs.cursor.com/de/configuration/kbd"
language: "de"
language_name: "German"
---

# Tastenkürzel
Source: https://docs.cursor.com/de/configuration/kbd

Tastenkürzel und Keybindings in Cursor

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

Übersicht der Tastenkürzel in Cursor. Sieh dir alle Tastenkürzel an, indem du <Kbd>Cmd R</Kbd> und dann <Kbd>Cmd S</Kbd> drückst oder die Befehlspalette mit <Kbd>Cmd Shift P</Kbd> öffnest und nach `Keyboard Shortcuts` suchst.

Erfahre mehr über Tastenkürzel in Cursor, wobei [Key Bindings for VS Code](https://code.visualstudio.com/docs/getstarted/keybindings) als Grundlage für Cursors Keybindings dient.

Alle Cursor-Keybindings, einschließlich Cursor-spezifischer Features, kannst du in den Einstellungen für Tastenkürzel neu zuweisen.

<div id="general">
  ## Allgemein
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut               | Aktion                                                  |
  | ---------------------- | ------------------------------------------------------- |
  | <Kbd>Cmd I</Kbd>       | Seitenleiste umschalten (falls nicht an Modus gebunden) |
  | <Kbd>Cmd L</Kbd>       | Seitenleiste umschalten (falls nicht an Modus gebunden) |
  | <Kbd>Cmd E</Kbd>       | Steuerzentrale für Background Agent                     |
  | <Kbd>Cmd .</Kbd>       | Modusmenü                                               |
  | <Kbd>Cmd /</Kbd>       | Zwischen AI-Modellen wechseln                           |
  | <Kbd>Cmd Shift J</Kbd> | Cursor-Einstellungen                                    |
  | <Kbd>Cmd ,</Kbd>       | Allgemeine Einstellungen                                |
  | <Kbd>Cmd Shift P</Kbd> | Befehlspalette                                          |
</div>

<div id="chat">
  ## Chat
</div>

Shortcuts für das Chat-Eingabefeld.

<div className="full-width-table equal-table-columns">
  | Shortcut                                             | Action                                   |
  | ---------------------------------------------------- | ---------------------------------------- |
  | <Kbd>Return</Kbd>                                    | Nudge (Standard)                         |
  | <Kbd>Ctrl Return</Kbd>                               | Nachricht in die Warteschlange           |
  | <Kbd>Cmd Return</Kbd> when typing                    | Senden erzwingen                         |
  | <Kbd>Cmd Shift Backspace</Kbd>                       | Generierung abbrechen                    |
  | <Kbd>Cmd Shift L</Kbd> with code selected            | Ausgewählten Code als Kontext hinzufügen |
  | <Kbd>Cmd V</Kbd> with code or log in clipboard       | Zwischenablage als Kontext hinzufügen    |
  | <Kbd>Cmd Shift V</Kbd> with code or log in clipboard | Zwischenablage ins Eingabefeld einfügen  |
  | <Kbd>Cmd Return</Kbd> with suggested changes         | Alle Änderungen übernehmen               |
  | <Kbd>Cmd Backspace</Kbd>                             | Alle Änderungen verwerfen                |
  | <Kbd>Tab</Kbd>                                       | Zum nächsten Beitrag wechseln            |
  | <Kbd>Shift Tab</Kbd>                                 | Zum vorherigen Beitrag wechseln          |
  | <Kbd>Cmd Opt /</Kbd>                                 | Modell umschalten                        |
  | <Kbd>Cmd N</Kbd> / <Kbd>Cmd R</Kbd>                  | Neuer Chat                               |
  | <Kbd>Cmd T</Kbd>                                     | Neuer Chat-Tab                           |
  | <Kbd>Cmd \[</Kbd>                                    | Vorheriger Chat                          |
  | <Kbd>Cmd ]</Kbd>                                     | Nächster Chat                            |
  | <Kbd>Cmd W</Kbd>                                     | Chat schließen                           |
  | <Kbd>Escape</Kbd>                                    | Fokus vom Feld entfernen                 |
</div>

<div id="inline-edit">
  ## Inline-Edit
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut                       | Aktion                  |
  | ------------------------------ | ----------------------- |
  | <Kbd>Cmd K</Kbd>               | Öffnen                  |
  | <Kbd>Cmd Shift K</Kbd>         | Eingabefokus umschalten |
  | <Kbd>Return</Kbd>              | Absenden                |
  | <Kbd>Cmd Shift Backspace</Kbd> | Abbrechen               |
  | <Kbd>Opt Return</Kbd>          | Kurze Frage stellen     |
</div>

## Codeauswahl & Kontext

<div className="full-width-table equal-table-columns">
  | Shortcut                                                 | Aktion                                        |
  | -------------------------------------------------------- | --------------------------------------------- |
  | <Kbd>@</Kbd>                                             | [@-symbols](/de/context/@-symbols/)           |
  | <Kbd>#</Kbd>                                             | Dateien                                       |
  | <Kbd>/</Kbd>                                             | Shortcut-Befehle                              |
  | <Kbd>Cmd Shift L</Kbd>                                   | Auswahl zum Chat hinzufügen                   |
  | <Kbd>Cmd Shift K</Kbd>                                   | Auswahl zum Edit hinzufügen                   |
  | <Kbd>Cmd L</Kbd>                                         | Auswahl zu neuem Chat hinzufügen              |
  | <Kbd>Cmd M</Kbd>                                         | Dateilesestrategien umschalten                |
  | <Kbd>Cmd →</Kbd>                                         | Nächstes Wort des Vorschlags übernehmen       |
  | <Kbd>Cmd Return</Kbd>                                    | Codebase im Chat durchsuchen                  |
  | Code auswählen, <Kbd>Cmd C</Kbd>, <Kbd>Cmd V</Kbd>       | Kopierten Referenzcode als Kontext hinzufügen |
  | Code auswählen, <Kbd>Cmd C</Kbd>, <Kbd>Cmd Shift V</Kbd> | Kopierten Code als Textkontext hinzufügen     |
</div>

<div id="tab">
  ## Tab
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut         | Aktion                 |
  | ---------------- | ---------------------- |
  | <Kbd>Tab</Kbd>   | Vorschlag annehmen     |
  | <Kbd>Cmd →</Kbd> | Nächstes Wort annehmen |
</div>

<div id="terminal">
  ## Terminal
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut              | Aktion                        |
  | --------------------- | ----------------------------- |
  | <Kbd>Cmd K</Kbd>      | Terminal-Eingabeleiste öffnen |
  | <Kbd>Cmd Return</Kbd> | Generierten Befehl ausführen  |
  | <Kbd>Escape</Kbd>     | Befehl übernehmen             |
</div>

---

← Previous: [Agent in der CLI nutzen](./agent-in-der-cli-nutzen.md) | [Index](./index.md) | Next: [Shell-Befehle](./shell-befehle.md) →