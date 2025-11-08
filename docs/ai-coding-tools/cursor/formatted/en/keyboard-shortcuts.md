---
title: "Keyboard Shortcuts"
source: "https://docs.cursor.com/en/configuration/kbd"
language: "en"
language_name: "English"
---

# Keyboard Shortcuts
Source: https://docs.cursor.com/en/configuration/kbd

Keyboard shortcuts and keybindings in Cursor

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

Overview of keyboard shortcuts in Cursor. See all keyboard shortcuts by pressing <Kbd>Cmd R</Kbd> then <Kbd>Cmd S</Kbd> or by opening command palette <Kbd>Cmd Shift P</Kbd> and searching for `Keyboard Shortcuts`.

Learn more about Keyboard Shortcuts in Cursor with [Key Bindings for VS Code](https://code.visualstudio.com/docs/getstarted/keybindings) as a baseline for Cursor's keybindings.

All Cursor keybindings, including Cursor-specific features, can be remapped in Keyboard Shortcuts settings.

## General

<div className="full-width-table equal-table-columns">
  | Shortcut               | Action                                  |
  | ---------------------- | --------------------------------------- |
  | <Kbd>Cmd I</Kbd>       | Toggle Sidepanel (unless bound to mode) |
  | <Kbd>Cmd L</Kbd>       | Toggle Sidepanel (unless bound to mode) |
  | <Kbd>Cmd E</Kbd>       | Background Agent control panel          |
  | <Kbd>Cmd .</Kbd>       | Mode Menu                               |
  | <Kbd>Cmd /</Kbd>       | Loop between AI models                  |
  | <Kbd>Cmd Shift J</Kbd> | Cursor settings                         |
  | <Kbd>Cmd ,</Kbd>       | General settings                        |
  | <Kbd>Cmd Shift P</Kbd> | Command palette                         |
</div>

## Chat

Shortcuts for the chat input box.

<div className="full-width-table equal-table-columns">
  | Shortcut                                             | Action                       |
  | ---------------------------------------------------- | ---------------------------- |
  | <Kbd>Return</Kbd>                                    | Nudge (default)              |
  | <Kbd>Ctrl Return</Kbd>                               | Queue message                |
  | <Kbd>Cmd Return</Kbd> when typing                    | Force send message           |
  | <Kbd>Cmd Shift Backspace</Kbd>                       | Cancel generation            |
  | <Kbd>Cmd Shift L</Kbd> with code selected            | Add selected code as context |
  | <Kbd>Cmd V</Kbd> with code or log in clipboard       | Add clipboard as context     |
  | <Kbd>Cmd Shift V</Kbd> with code or log in clipboard | Add clipboard to input box   |
  | <Kbd>Cmd Return</Kbd> with suggested changes         | Accept all changes           |
  | <Kbd>Cmd Backspace</Kbd>                             | Reject all changes           |
  | <Kbd>Tab</Kbd>                                       | Cycle to next message        |
  | <Kbd>Shift Tab</Kbd>                                 | Cycle to previous message    |
  | <Kbd>Cmd Opt /</Kbd>                                 | Model toggle                 |
  | <Kbd>Cmd N</Kbd> / <Kbd>Cmd R</Kbd>                  | New chat                     |
  | <Kbd>Cmd T</Kbd>                                     | New chat tab                 |
  | <Kbd>Cmd \[</Kbd>                                    | Previous chat                |
  | <Kbd>Cmd ]</Kbd>                                     | Next chat                    |
  | <Kbd>Cmd W</Kbd>                                     | Close chat                   |
  | <Kbd>Escape</Kbd>                                    | Unfocus field                |
</div>

## Inline Edit

<div className="full-width-table equal-table-columns">
  | Shortcut                       | Action             |
  | ------------------------------ | ------------------ |
  | <Kbd>Cmd K</Kbd>               | Open               |
  | <Kbd>Cmd Shift K</Kbd>         | Toggle input focus |
  | <Kbd>Return</Kbd>              | Submit             |
  | <Kbd>Cmd Shift Backspace</Kbd> | Cancel             |
  | <Kbd>Opt Return</Kbd>          | Ask quick question |
</div>

## Code Selection & Context

<div className="full-width-table equal-table-columns">
  | Shortcut                                              | Action                               |
  | ----------------------------------------------------- | ------------------------------------ |
  | <Kbd>@</Kbd>                                          | [@-symbols](/en/context/@-symbols/)  |
  | <Kbd>#</Kbd>                                          | Files                                |
  | <Kbd>/</Kbd>                                          | Shortcut Commands                    |
  | <Kbd>Cmd Shift L</Kbd>                                | Add selection to Chat                |
  | <Kbd>Cmd Shift K</Kbd>                                | Add selection to Edit                |
  | <Kbd>Cmd L</Kbd>                                      | Add selection to new chat            |
  | <Kbd>Cmd M</Kbd>                                      | Toggle file reading strategies       |
  | <Kbd>Cmd →</Kbd>                                      | Accept next word of suggestion       |
  | <Kbd>Cmd Return</Kbd>                                 | Search codebase in chat              |
  | Select code, <Kbd>Cmd C</Kbd>, <Kbd>Cmd V</Kbd>       | Add copied reference code as context |
  | Select code, <Kbd>Cmd C</Kbd>, <Kbd>Cmd Shift V</Kbd> | Add copied code as text context      |
</div>

## Tab

<div className="full-width-table equal-table-columns">
  | Shortcut         | Action            |
  | ---------------- | ----------------- |
  | <Kbd>Tab</Kbd>   | Accept suggestion |
  | <Kbd>Cmd →</Kbd> | Accept next word  |
</div>

## Terminal

<div className="full-width-table equal-table-columns">
  | Shortcut              | Action                   |
  | --------------------- | ------------------------ |
  | <Kbd>Cmd K</Kbd>      | Open terminal prompt bar |
  | <Kbd>Cmd Return</Kbd> | Run generated command    |
  | <Kbd>Escape</Kbd>     | Accept command           |
</div>

---

← Previous: [Using Agent in CLI](./using-agent-in-cli.md) | [Index](./index.md) | Next: [Shell Commands](./shell-commands.md) →