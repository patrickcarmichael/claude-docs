---
title: "Использование агента в CLI"
source: "https://docs.cursor.com/ru/cli/using"
language: "ru"
language_name: "Russian"
---

# Использование агента в CLI
Source: https://docs.cursor.com/ru/cli/using

Эффективно пиши промпты, пересматривай и улучшай их итерациями с Cursor CLI

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
  ## Подсказки
</div>

Лучше всего заранее чётко формулировать намерения. Например, можно использовать подсказку «do not write any code», чтобы агент точно не редактировал файлы. Это особенно полезно при планировании задач перед их выполнением.

Сейчас у агента есть инструменты для работы с файлами, поиска и выполнения команд в оболочке. Постепенно добавляются новые инструменты, похожие на те, что есть у агента IDE.

<div id="mcp">
  ## MCP
</div>

Agent поддерживает [MCP (Model Context Protocol)](/ru/tools/mcp) для расширения функциональности и интеграций. CLI автоматически обнаружит и учтёт твой файл конфигурации `mcp.json`, задействуя те же MCP‑серверы и инструменты, которые ты настроил в IDE.

<div id="rules">
  ## Правила
</div>

CLI-агент поддерживает ту же [систему правил](/ru/context/rules), что и IDE. Ты можешь создавать правила в каталоге `.cursor/rules`, чтобы предоставлять агенту контекст и рекомендации. Эти правила автоматически загружаются и применяются согласно их конфигурации, позволяя настраивать поведение агента для разных частей проекта или конкретных типов файлов.

<Note>
  CLI также читает `AGENTS.md` и `CLAUDE.md` в корне проекта (если они есть) и применяет их как правила вместе с `.cursor/rules`.
</Note>

<div id="working-with-agent">
  ## Работа с Agent
</div>

<div id="navigation">
  ### Навигация
</div>

К предыдущим сообщениям можно перейти стрелкой вверх (<Kbd>ArrowUp</Kbd>) и пролистывать их.

<div id="review">
  ### Просмотр
</div>

Смотри изменения с <Kbd>Cmd+R</Kbd>. Нажми <Kbd>i</Kbd>, чтобы добавить дополнительные инструкции. Используй <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd> для прокрутки и <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd> для переключения файлов.

<div id="selecting-context">
  ### Выбор контекста
</div>

Выбирай файлы и папки для включения в контекст с помощью <Kbd>@</Kbd>. Освободи место в окне контекста, выполнив `/compress`. См. [Summarization](/ru/agent/chat/summarization) для подробностей.

<div id="history">
  ## История
</div>

Продолжай разговор в существующем треде с `--resume [thread id]`, чтобы подгрузить предыдущий контекст.

Чтобы продолжить самый свежий диалог, используй `cursor-agent resume`.

Ты также можешь выполнить `cursor-agent ls`, чтобы посмотреть список прошлых диалогов.

<div id="command-approval">
  ## Подтверждение команд
</div>

Перед выполнением команд в терминале CLI попросит тебя подтвердить (<Kbd>y</Kbd>) или отклонить (<Kbd>n</Kbd>) их выполнение.

<div id="non-interactive-mode">
  ## Неинтерактивный режим
</div>

Используй `-p` или `--print`, чтобы запустить Agent в неинтерактивном режиме. Ответ будет выведен в консоль.

В неинтерактивном режиме можно вызывать Agent без взаимодействия. Это позволяет встроить его в скрипты, CI-пайплайны и т. п.

Можно комбинировать это с `--output-format`, чтобы управлять форматированием вывода. Например, используй `--output-format json` для структурированного вывода, который проще парсить в скриптах, или `--output-format text` для обычного текстового вывода.

<Note>
  В неинтерактивном режиме Cursor имеет полный доступ на запись.
</Note>

---

← Previous: [Режим Shell](./shell.md) | [Index](./index.md) | Next: [Горячие клавиши](./section.md) →