---
title: "Quickstart"
source: "https://docs.cursor.com/en/get-started/quickstart"
language: "en"
language_name: "English"
---

# Quickstart
Source: https://docs.cursor.com/en/get-started/quickstart

Get started with Cursor in 5 minutes

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

This quickstart will walk you through a project using Cursor's core features. By the end, you'll be familiar with Tab, Inline Edit, and Agent.

## Open a project in Cursor

Use an existing project or clone our example:

<Tabs>
  <Tab title="Clone example project">
    1. Ensure git is installed
    2. Clone the example project:

    ```bash  theme={null}
    git clone git@github.com:voxelize/voxelize.git && \
    cd voxelize && \
    cursor .
    ```
  </Tab>

  <Tab title="Use existing project">
    1. Open Cursor
    2. Open a project folder with <Kbd>Cmd O</Kbd> or `cursor <path-to-project>`
  </Tab>
</Tabs>

We'll be showcasing using the example project, but you can use any project you have locally.

## Autocomplete with [Tab](/en/kbd#tab)

Tab is the autocomplete model we've trained in-house. It's a great way to ease into AI assisted coding if you're not used to it. With Tab, you can:

* Autocomplete **multiple lines and blocks** of code
* Jump **in** and **across** files to the next autocomplete suggestion

1. Start typing the beginning of a function:
   ```javascript  theme={null}
   function calculate
   ```
2. Tab suggestions appear automatically
3. Press Tab to accept the suggestion
4. Cursor suggests parameters and function bodies

## [Inline Edit](/en/inline-edit) a selection

1. Select the function you just created
2. Press <Kbd>Cmd K</Kbd>
3. Type "make this function calculate fibonacci numbers"
4. Press <Kbd>Return</Kbd> to apply the changes
5. Cursor adds imports and documentation

## Chat with [Agent](/en/agent)

1. Open the Chat panel (<Kbd>Cmd I</Kbd>)
2. Ask: "Add tests for this function and run them"
3. Agent will create a test file, write test cases, and run them for you

## Bonus

Advanced features:

<AccordionGroup>
  <Accordion title="Handoff work to Background Agent">
    1. Open the Background Agent control panel (<Kbd>Cmd E</Kbd>)
    2. Ask: "Find and fix a bug in this project"
    3. [Background Agent](/en/background-agent) will:
       * Create a remote Virtual Machine (VM)
       * Explore your project
       * Detect bugs
       * Propose fixes

    Review and apply changes.
  </Accordion>

  {" "}

  <Accordion title="Write a rule">
    1. Open the command palette (<Kbd>Cmd Shift P</Kbd>) 2. Search: "New Cursor
       Rule" 3. Name it (e.g., `style-guide`) 4. Select Rule Type "Always" 5. Define
       your style: `Prefer using camelCase for variable names`
  </Accordion>

  <Accordion title="Set up an MCP server">
    1. Visit our [MCP directory](https://docs.cursor.com/tools)
    2. Choose a tool
    3. Click "Install"

    Servers can also be installed manually:

    1. Open Cursor Settings (<Kbd>Cmd Shift J</Kbd>)
    2. Go to "Tools & Integrations"
    3. Click "New MCP Server"
  </Accordion>
</AccordionGroup>

## Next steps

Explore these guides to learn more:

<CardGroup cols={2}>
  <Card title="Working with Context" href="/en/guides/working-with-context">
    Provide effective context for better results
  </Card>

  <Card title="Selecting Models" href="/en/guides/selecting-models">
    Choose the right model for your task
  </Card>
</CardGroup>

Learn all [Cursor concepts](/en/get-started/concepts) and start building!

---

← Previous: [Installation](./installation.md) | [Index](./index.md) | Next: [Data Science](./data-science.md) →