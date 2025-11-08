---
title: "Shell-Modus"
source: "https://docs.cursor.com/de/cli/shell-mode"
language: "de"
language_name: "German"
---

# Shell-Modus
Source: https://docs.cursor.com/de/cli/shell-mode

Führ Shell-Befehle direkt in der CLI aus, ohne deinen Chat zu verlassen

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

Shell Mode führt Shell-Befehle direkt aus der CLI aus, ohne dass du die Unterhaltung verlassen musst. Nutz ihn für schnelle, nicht interaktive Befehle mit Sicherheitschecks; die Ausgabe wird direkt in der Unterhaltung angezeigt.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

<div id="command-execution">
  ## Befehlsausführung
</div>

Befehle laufen in deiner Login-Shell (`$SHELL`) mit dem Arbeitsverzeichnis und der Umgebung der CLI. Verkette Befehle, um sie in anderen Verzeichnissen auszuführen:

```bash  theme={null}
cd subdir && npm test
```

<div id="output">
  ## Ausgabe
</div>

<product_visual type="screenshot">
  Befehlsausgabe mit Kopfzeile samt Exit-Code, Anzeige von stdout/stderr und Steuerelementen zum Kürzen
</product_visual>

Lange Ausgaben werden automatisch gekürzt, und lang laufende Prozesse werden zur Wahrung der Performance nach einer Zeitüberschreitung beendet.

<div id="limitations">
  ## Einschränkungen
</div>

* Befehle laufen nach 30 Sekunden in ein Timeout
* Lang laufende Prozesse, Server und interaktive Eingabeaufforderungen werden nicht unterstützt
* Verwende kurze, nicht interaktive Befehle für die besten Ergebnisse

<div id="permissions">
  ## Berechtigungen
</div>

Bevor Befehle ausgeführt werden, werden sie gegen deine Berechtigungen und Teameinstellungen geprüft. Weitere Details findest du unter [Berechtigungen](/de/cli/reference/permissions).

<product_visual type="screenshot">
  Decision banner showing approval options: Run, Reject/Propose, Add to allowlist, and Auto-run
</product_visual>

Adminrichtlinien können bestimmte Befehle blockieren, und Befehle mit Umleitungen können nicht direkt zur Allowlist hinzugefügt werden.

<div id="usage-guidelines">
  ## Nutzungsrichtlinien
</div>

Shell Mode eignet sich für Statuschecks, schnelle Builds, Dateioperationen und das Überprüfen der Umgebung.

Vermeide lang laufende Server, interaktive Anwendungen und Befehle, die Eingaben erfordern.

Jeder Befehl läuft unabhängig – nutz `cd <dir> && ...`, um Befehle in anderen Verzeichnissen auszuführen.

<div id="troubleshooting">
  ## Fehlerbehebung
</div>

* Wenn ein Befehl hängen bleibt, mit <Kbd>Ctrl+C</Kbd> abbrechen und nicht-interaktive Flags hinzufügen
* Wenn nach Berechtigungen gefragt wird, einmal bestätigen oder mit <Kbd>Tab</Kbd> zur Allowlist hinzufügen
* Bei abgeschnittener Ausgabe mit <Kbd>Ctrl+O</Kbd> erweitern
* Um in verschiedenen Verzeichnissen auszuführen, `cd <dir> && ...` verwenden, da Änderungen nicht bestehen bleiben
* Shell Mode unterstützt zsh und bash basierend auf deiner `$SHELL`-Variable

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Bleibt `cd` über mehrere Ausführungen hinweg bestehen?">
    Nee. Jeder Befehl läuft für sich. Verwende `cd <dir> && ...`, um Befehle in verschiedenen Verzeichnissen auszuführen.
  </Accordion>

  <Accordion title="Kann ich das Timeout ändern?">
    Nein. Befehle sind auf 30 Sekunden begrenzt und das ist nicht konfigurierbar.
  </Accordion>

  <Accordion title="Wo werden Berechtigungen konfiguriert?">
    Berechtigungen werden über die CLI und die Teamkonfiguration verwaltet. Verwende das Decision-Banner, um Befehle zu Allowlists hinzuzufügen.
  </Accordion>

  <Accordion title="Wie beende ich den Shell-Modus?">
    Drück <Kbd>Escape</Kbd>, wenn das Eingabefeld leer ist, <Kbd>Backspace</Kbd>/<Kbd>Delete</Kbd> bei leerer Eingabe oder <Kbd>Strg+C</Kbd>, um zu leeren und zu beenden.
  </Accordion>
</AccordionGroup>

---

← Previous: [Slash-Befehle](./slash-befehle.md) | [Index](./index.md) | Next: [Agent in der CLI nutzen](./agent-in-der-cli-nutzen.md) →