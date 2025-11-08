---
title: "Git"
source: "https://docs.cursor.com/de/integrations/git"
language: "de"
language_name: "German"
---

# Git
Source: https://docs.cursor.com/de/integrations/git

KI-gestützte Git-Funktionen, darunter das Generieren von Commit-Nachrichten und das Lösen von Merge-Konflikten

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

Cursor bietet KI-gestützte Git-Funktionen, die deinen Workflow vereinfachen, darunter das automatische Generieren von Commit-Nachrichten und die intelligente Auflösung von Merge-Konflikten.

<div id="ai-commit-message">
  ## KI-Commit-Nachricht
</div>

Cursor generiert Commit-Nachrichten aus gestagten Änderungen.

1. Dateien für den Commit stagen
2. Den Git-Tab in der Seitenleiste öffnen
3. Auf das Funkel-Icon (✨) neben dem Commit-Nachrichtenfeld klicken

Die generierten Nachrichten berücksichtigen die gestagten Änderungen und die Git-Historie des Repos. Wenn du Konventionen wie [Conventional Commits](https://www.conventionalcommits.org/) nutzt, folgen die Nachrichten demselben Muster.

<div id="add-shortcut">
  ### Shortcut hinzufügen
</div>

An eine Tastenkombination binden:

1. Zu Keyboard Shortcuts gehen (<Kbd>Cmd+R Cmd+S</Kbd> oder <Kbd>Cmd+Shift+P</Kbd> und nach "Open Keyboard Shortcuts (JSON)" suchen)
2. Dieses Binding für <Kbd>Cmd+M</Kbd> hinzufügen:
   ```json  theme={null}
   {
     "key": "cmd+m",
     "command": "cursor.generateGitCommitMessage"
   }
   ```
3. Speichern

<Info>
  Du kannst die Generierung von Commit-Nachrichten nicht anpassen. Cursor passt sich deinem bestehenden Commit-Stil an.
</Info>

<div id="ai-resolve-conflicts">
  ## Konflikte mit KI lösen
</div>

Wenn Merge-Konflikte auftreten, kann der Cursor-Agent helfen, sie zu lösen, indem er beide Seiten des Konflikts versteht und eine Lösung vorschlägt.

<div id="how-to-use">
  ### So verwendest du’s
</div>

1. Wenn ein Merge-Konflikt auftritt, siehst du die Konfliktmarkierungen in deiner Datei
2. Klick auf den **Resolve in Chat**-Button, der in der Merge-Konflikt-UI erscheint
3. Der Agent analysiert beide Versionen und schlägt eine Lösung vor
4. Schau dir die vorgeschlagenen Änderungen an und übernimm sie

---

← Previous: [Terminal](./terminal.md) | [Index](./index.md) | Next: [GitHub](./github.md) →