---
title: "Режим Shell"
source: "https://docs.cursor.com/ru/cli/shell-mode"
language: "ru"
language_name: "Russian"
---

# Режим Shell
Source: https://docs.cursor.com/ru/cli/shell-mode

Запускай shell-команды прямо из CLI, не выходя из диалога

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

Режим Shell запускает команды оболочки прямо из CLI, не покидая текущий диалог. Используй его для быстрых, неинтерактивных команд: с проверками безопасности и выводом результатов прямо в разговоре.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

<div id="command-execution">
  ## Выполнение команд
</div>

Команды выполняются в твоей оболочке входа (`$SHELL`) с рабочей директорией и окружением CLI. Связывай команды, чтобы запускать их в других каталогах:

```bash  theme={null}
cd subdir && npm test
```

<div id="output">
  ## Вывод
</div>

<product_visual type="screenshot">
  Command output showing header with exit code, stdout/stderr display, and truncation controls
</product_visual>

Большие выводы автоматически обрезаются, а долгие процессы прерываются по тайм-ауту, чтобы сохранить производительность.

<div id="limitations">
  ## Ограничения
</div>

* Команды прерываются по тайм-ауту через 30 секунд
* Долгоживущие процессы, серверы и интерактивные запросы не поддерживаются
* Для лучших результатов используй короткие, неинтерактивные команды

<div id="permissions">
  ## Права доступа
</div>

Перед выполнением команды проверяются на соответствие твоим правам доступа и настройкам команды. См. [Permissions](/ru/cli/reference/permissions) для подробной конфигурации.

<product_visual type="screenshot">
  Баннер решений с вариантами: Run, Reject/Propose, Add to allowlist и Auto-run
</product_visual>

Администраторские политики могут блокировать отдельные команды, а команды с перенаправлением нельзя добавить в allowlist прямо в интерфейсе.

<div id="usage-guidelines">
  ## Рекомендации по использованию
</div>

Shell Mode отлично подходит для проверок состояния, быстрых сборок, операций с файлами и анализа окружения.

Избегай долгоживущих серверов, интерактивных приложений и команд, которые требуют ввода.

Каждая команда выполняется отдельно — используй `cd <dir> && ...`, чтобы запускать команды в других каталогах.

<div id="troubleshooting">
  ## Устранение неполадок
</div>

* Если команда зависла, отмени с <Kbd>Ctrl+C</Kbd> и добавь флаги для неинтерактивного режима
* Когда попросят разрешения, один раз подтверди или добавь в allowlist с помощью <Kbd>Tab</Kbd>
* Если вывод обрезан, нажми <Kbd>Ctrl+O</Kbd>, чтобы развернуть
* Чтобы запускать команды в разных каталогах, используй `cd <dir> && ...`, поскольку изменения не сохраняются
* Режим Shell поддерживает zsh и bash на основе значения переменной `$SHELL`

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Сохраняется ли `cd` между запусками?">
    Нет. Каждая команда выполняется отдельно. Используй `cd <dir> && ...`, чтобы запускать команды в разных каталогах.
  </Accordion>

  <Accordion title="Могу ли я изменить таймаут?">
    Нет. Команды ограничены 30 секундами, и это нельзя настроить.
  </Accordion>

  <Accordion title="Где настраиваются разрешения?">
    Разрешения задаются в конфигурации CLI и команды. Используй баннер с решением, чтобы добавлять команды в allowlist.
  </Accordion>

  <Accordion title="Как выйти из Shell Mode?">
    Нажми <Kbd>Escape</Kbd>, когда поле ввода пустое, <Kbd>Backspace</Kbd>/<Kbd>Delete</Kbd> при пустом вводе или <Kbd>Ctrl+C</Kbd>, чтобы очистить и выйти.
  </Accordion>
</AccordionGroup>

---

← Previous: [Slash-команды](./slash.md) | [Index](./index.md) | Next: [Использование агента в CLI](./cli.md) →