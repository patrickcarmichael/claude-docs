---
title: "Planung"
source: "https://docs.cursor.com/de/agent/planning"
language: "de"
language_name: "German"
---

# Planung
Source: https://docs.cursor.com/de/agent/planning

Wie Agent komplexe Aufgaben mit To-dos und Warteschlangen plant und verwaltet

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

Agent kann vorausplanen und komplexe Aufgaben mit strukturierten To-do-Listen und Message-Queuing verwalten – so bleiben langfristige Tasks leichter nachvollziehbar und verständlich.

<div id="agent-to-dos">
  ## Agent-To-dos
</div>

Agent kann längere Aufgaben in überschaubare Schritte mit Abhängigkeiten aufteilen und so einen strukturierten Plan erstellen, der sich während der Arbeit laufend aktualisiert.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### So funktioniert’s
</div>

* Agent erstellt automatisch To-do-Listen für komplexe Aufgaben
* Jeder Eintrag kann Abhängigkeiten zu anderen Aufgaben haben
* Die Liste aktualisiert sich in Echtzeit, während die Arbeit voranschreitet
* Abgeschlossene Aufgaben werden automatisch abgehakt

<div id="visibility">
  ### Sichtbarkeit
</div>

* To-dos erscheinen in der Chat-Oberfläche
* Wenn die [Slack-Integration](/de/slack) eingerichtet ist, sind To-dos auch dort sichtbar
* Du kannst die vollständige Aufgabenübersicht jederzeit ansehen

<Tip>
  Für bessere Planung: Beschreibe dein Endziel klar. Agent erstellt
  genauere Aufgabenaufteilungen, wenn der gesamte Umfang klar ist.
</Tip>

<Note>Planung und To-dos werden derzeit im Auto-Modus nicht unterstützt.</Note>

<div id="queued-messages">
  ## Nachrichten in der Warteschlange
</div>

Stell Folge­nachrichten in die Warteschlange, während Agent an der aktuellen Aufgabe arbeitet. Deine Anweisungen warten der Reihe nach und werden automatisch ausgeführt, sobald sie dran sind.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

<div id="using-the-queue">
  ### Warteschlange verwenden
</div>

1. Während Agent arbeitet, tipp deine nächste Anweisung
2. Drück <Kbd>Ctrl+Enter</Kbd>, um sie zur Warteschlange hinzuzufügen
3. Nachrichten erscheinen der Reihe nach unter der aktiven Aufgabe
4. Ändere die Reihenfolge der wartenden Nachrichten, indem du auf den Pfeil klickst
5. Agent verarbeitet sie der Reihe nach, sobald er fertig ist

<div id="override-the-queue">
  ### Warteschlange überschreiben
</div>

Um deine Nachricht in die Warteschlange zu stellen statt die Standardübermittlung zu verwenden, nutz <Kbd>Ctrl+Enter</Kbd>. Um eine Nachricht sofort ohne Warteschlange zu senden, nutz <Kbd>Cmd+Enter</Kbd>. Das „force-pusht“ deine Nachricht, umgeht die Warteschlange und führt sie sofort aus.

<div id="default-messaging">
  ## Standardnachrichten
</div>

Nachrichten werden standardmäßig so schnell wie möglich gesendet und erscheinen in der Regel direkt, nachdem Agent einen Toolaufruf abgeschlossen hat. Das sorgt für die schnellstmögliche Reaktion.

<div id="how-default-messaging-works">
  ### So funktionieren Standardnachrichten
</div>

* Deine Nachricht wird an die zuletzt gesendete Nutzer-Nachricht im Chat angehängt
* Nachrichten werden normalerweise an Tool-Ergebnisse angehängt und sofort gesendet, sobald sie vorliegen
* Das sorgt für einen natürlicheren Gesprächsfluss, ohne die aktuelle Arbeit von Agent zu unterbrechen
* Standardmäßig passiert das, wenn du Enter drückst, während Agent arbeitet

---

← Previous: [Überblick](./berblick.md) | [Index](./index.md) | Next: [Diffs & Review](./diffs-review.md) →