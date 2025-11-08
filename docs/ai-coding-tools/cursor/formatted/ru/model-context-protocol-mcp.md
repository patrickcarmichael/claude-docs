---
title: "Model Context Protocol (MCP)"
source: "https://docs.cursor.com/ru/context/mcp"
language: "ru"
language_name: "Russian"
---

# Model Context Protocol (MCP)
Source: https://docs.cursor.com/ru/context/mcp

Подключай внешние инструменты и источники данных к Cursor через MCP

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

<div id="what-is-mcp">
  ## Что такое MCP?
</div>

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) даёт Cursor возможность подключаться к внешним инструментам и источникам данных.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
</Frame>

<div id="why-use-mcp">
  ### Зачем использовать MCP?
</div>

MCP подключает Cursor к внешним системам и данным. Вместо того чтобы каждый раз заново объяснять структуру проекта, интегрируйся напрямую со своими инструментами.

Пиши серверы MCP на любом языке, который выводит в `stdout` или поднимает HTTP-эндпоинт — Python, JavaScript, Go и т. д.

<div id="how-it-works">
  ### Как это работает
</div>

Серверы MCP предоставляют возможности через протокол, подключая Cursor к внешним инструментам и источникам данных.

Cursor поддерживает три способа транспорта:

<div className="full-width-table">
  | Транспорт                                                        | Среда выполнения  | Развертывание             | Пользователи            | Ввод               | Аутентификация |
  | :--------------------------------------------------------------- | :---------------- | :------------------------ | :---------------------- | :----------------- | :------------- |
  | **<span className="whitespace-nowrap">`stdio`</span>**           | Локально          | Управляется Cursor        | Один пользователь       | Команда в shell    | Вручную        |
  | **<span className="whitespace-nowrap">`SSE`</span>**             | Локально/удалённо | Развёртывание как сервера | Несколько пользователей | URL SSE-эндпоинта  | OAuth          |
  | **<span className="whitespace-nowrap">`Streamable HTTP`</span>** | Локально/удалённо | Развёртывание как сервера | Несколько пользователей | URL HTTP-эндпоинта | OAuth          |
</div>

<div id="protocol-support">
  ### Поддержка протокола
</div>

Cursor поддерживает следующие возможности протокола MCP:

<div className="full-width-table">
  | Возможность     | Поддержка      | Описание                                                                                   |
  | :-------------- | :------------- | :----------------------------------------------------------------------------------------- |
  | **Tools**       | Поддерживается | Функции, которые выполняет модель ИИ                                                       |
  | **Prompts**     | Поддерживается | Шаблоны сообщений и пользовательские рабочие процессы                                      |
  | **Resources**   | Поддерживается | Структурированные источники данных для чтения и ссылок                                     |
  | **Roots**       | Поддерживается | Запросы сервера к границам URI или файловой системы, в пределах которых выполнять операции |
  | **Elicitation** | Поддерживается | Инициируемые сервером запросы на дополнительную информацию от пользователей                |
</div>

<div id="installing-mcp-servers">
  ## Установка серверов MCP
</div>

<div id="one-click-installation">
  ### Установка в один клик
</div>

Ставь MCP‑серверы из нашей коллекции и входи через OAuth.

<Columns cols={2}>
  <Card title="Browse MCP Tools" icon="table" horizontal href="/ru/tools">
    Просматривай доступные MCP‑серверы
  </Card>

  <Card title="Add to Cursor Button" icon="plus" horizontal href="/ru/deeplinks">
    Создай кнопку «Add to Cursor»
  </Card>
</Columns>

<div id="using-mcpjson">
  ### Использование `mcp.json`
</div>

Настрой свои пользовательские MCP‑серверы с помощью JSON‑файла:

<CodeGroup>
  ```json CLI Server - Node.js theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "npx",
        "args": ["-y", "mcp-server"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json CLI Server - Python theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "python",
        "args": ["mcp-server.py"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json Remote Server theme={null}
  // MCP‑сервер по HTTP или SSE — запускается на сервере
  {
    "mcpServers": {
      "server-name": {
        "url": "http://localhost:3000/mcp",
        "headers": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```
</CodeGroup>

<div id="stdio-server-configuration">
  ### Конфигурация STDIO‑сервера
</div>

Для STDIO‑серверов (локальных серверов командной строки) настрой эти поля в `mcp.json`:

<div className="full-width-table">
  | Поле        | Обязательно | Описание                                                                                                   | Примеры                                   |
  | :---------- | :---------- | :--------------------------------------------------------------------------------------------------------- | :---------------------------------------- |
  | **type**    | Да          | Тип подключения сервера                                                                                    | `"stdio"`                                 |
  | **command** | Да          | Команда для запуска исполняемого файла сервера. Должна находиться в PATH системы или содержать полный путь | `"npx"`, `"node"`, `"python"`, `"docker"` |
  | **args**    | Нет         | Массив аргументов, передаваемых команде                                                                    | `["server.py", "--port", "3000"]`         |
  | **env**     | Нет         | Переменные окружения для сервера                                                                           | `{"API_KEY": "${input:api-key}"}`         |
  | **envFile** | Нет         | Путь к файлу окружения для загрузки дополнительных переменных                                              | `".env"`, `"${workspaceFolder}/.env"`     |
</div>

<div id="using-the-extension-api">
  ### Использование Extension API
</div>

Для программной регистрации MCP‑серверов Cursor предоставляет Extension API, который позволяет настраивать их динамически без изменения файлов `mcp.json`. Это особенно полезно для корпоративных сред и автоматизированных сценариев развёртывания.

<Card title="Справочник по MCP Extension API" icon="code" href="/ru/context/mcp-extension-api">
  Узнай, как программно регистрировать MCP‑серверы с помощью `vscode.cursor.mcp.registerServer()`
</Card>

<div id="configuration-locations">
  ### Где хранится конфигурация
</div>

<CardGroup cols={2}>
  <Card title="Конфигурация проекта" icon="folder-tree">
    Создай `.cursor/mcp.json` в своём проекте для проектных инструментов.
  </Card>

  <Card title="Глобальная конфигурация" icon="globe">
    Создай `~/.cursor/mcp.json` в домашнем каталоге, чтобы инструменты были доступны везде.
  </Card>
</CardGroup>

<div id="config-interpolation">
  ### Интерполяция конфигурации
</div>

Используй переменные в значениях `mcp.json`. Cursor подставляет переменные в следующих полях: `command`, `args`, `env`, `url` и `headers`.

Поддерживаемый синтаксис:

* `${env:NAME}` — переменные окружения
* `${userHome}` — путь к твоей домашней папке
* `${workspaceFolder}` — корень проекта (папка, которая содержит `.cursor/mcp.json`)
* `${workspaceFolderBasename}` — имя корневой папки проекта
* `${pathSeparator}` и `${/}` — разделитель путей ОС

Примеры

```json  theme={null}
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

```json  theme={null}
{
  "mcpServers": {
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    }
  }
}
```

<div id="authentication">
  ### Аутентификация
</div>

Серверы MCP используют переменные окружения для аутентификации. Передавай API‑ключи и токены через конфиг.

Cursor поддерживает OAuth для серверов, которым это нужно.

<div id="using-mcp-in-chat">
  ## Использование MCP в чате
</div>

Агент Composer автоматически использует инструменты MCP из раздела `Available Tools`, когда это уместно. Попроси нужный инструмент по имени или опиши, что тебе нужно. Включай или отключай инструменты в настройках.

<div id="toggling-tools">
  ### Переключение инструментов
</div>

Включай или отключай инструменты MCP прямо из чата. Нажми на название инструмента в списке, чтобы переключить его. Отключённые инструменты не подгружаются в контекст и недоступны для Agent.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-toggle.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fa3060f593cae3e5fb7c7d2f041a715" autoPlay loop muted playsInline controls data-path="images/context/mcp/tool-toggle.mp4" />
</Frame>

<div id="tool-approval">
  ### Подтверждение использования инструментов
</div>

По умолчанию Agent запрашивает подтверждение перед использованием инструментов MCP. Нажми на стрелку рядом с названием инструмента, чтобы посмотреть передаваемые аргументы.

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bf9b19d5f23abc65914f712185b3ec72" alt="" data-og-width="1212" width="1212" data-og-height="902" height="902" data-path="images/context/mcp/tool-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e3f900fad0b8f2a469460c70fa1dd1dc 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de2f90138de39d75d70c5800f13be93a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b9c616ce7a4080ea4088a0fdd0050c7c 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3f783e62a7a31957b8988edb97c139f9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10bf2c1dbfd5c2a03aa95334f53cd571 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=231c0e3cd60df5ad12455d5e8ef308d2 2500w" /></Frame>

<div id="auto-run">
  #### Автозапуск
</div>

Включи автозапуск, чтобы Agent мог использовать инструменты MCP без подтверждений. Работает как команды терминала. Подробнее о настройках автозапуска читай [здесь](/ru/agent/tools#auto-run).

<div id="tool-response">
  ### Ответ инструмента
</div>

Cursor показывает ответ в чате с разворачиваемыми панелями аргументов и результатов:

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=30af3f35869e9a78781f455bdbc0e3b5" alt="" data-og-width="1212" width="1212" data-og-height="952" height="952" data-path="images/context/mcp/tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8821ac7bad00ad54a18abc614c2e3d5c 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9d55f089ad53a89da99b8ddd524f6de 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a107d68a1fb05ed43851548b34fb4496 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b409b4941c2fd783043770fad0bd6390 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2a331b5e2bb9be0b9659393157454c2e 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=585b769dfa2a5114b111eb901a969845 2500w" /></Frame>

<div id="images-as-context">
  ### Изображения как контекст
</div>

Серверы MCP могут возвращать изображения — скриншоты, диаграммы и т. п. Возвращай их в виде строк в кодировке base64:

```js  theme={null}
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ полный base64 обрезан для удобства чтения

server.tool("generate_image", async (params) => {
  return {
    content: [
      {
        type: "image",
        data: RED_CIRCLE_BASE64,
        mimeType: "image/jpeg",
      },
    ],
  };
});
```

См. этот [пример сервера](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js) для подробностей реализации. Cursor прикрепляет возвращённые изображения к чату. Если модель поддерживает изображения, она их анализирует.

<div id="security-considerations">
  ## Вопросы безопасности
</div>

Когда устанавливаешь MCP‑серверы, учитывай такие практики безопасности:

* **Проверяй источник**: ставь MCP‑серверы только от доверенных разработчиков и из проверенных репозиториев
* **Проверяй разрешения**: смотри, к каким данным и API сервер будет получать доступ
* **Ограничивай API‑ключи**: используй ограниченные ключи с минимально необходимыми правами
* **Проводи аудит кода**: для критичных интеграций просматривай исходники сервера

Помни, что MCP‑серверы могут обращаться к внешним сервисам и выполнять код от твоего имени. Всегда разбирайся, что именно делает сервер, перед установкой.

<div id="real-world-examples">
  ## Примеры из реальной практики
</div>

Для наглядных примеров MCP в действии загляни в наш [гайд по веб‑разработке](/ru/guides/tutorials/web-development), где показано, как интегрировать Linear, Figma и инструменты браузера в твой рабочий процесс разработки.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Зачем нужны MCP‑серверы?">
    MCP‑серверы подключают Cursor к внешним инструментам — Google Drive, Notion и другим сервисам — чтобы подтягивать документы и требования прямо в твой рабочий процесс.
  </Accordion>

  {" "}

  <Accordion title="Как отладить проблемы с MCP‑сервером?">
    Посмотри логи MCP: 1) Открой панель Output в Cursor (<Kbd>Cmd+Shift+U</Kbd>)
    2\) Выбери «MCP Logs» в выпадающем списке 3) Проверь ошибки подключения,
    проблемы с аутентификацией или падения сервера. Логи показывают инициализацию сервера,
    вызовы инструментов и сообщения об ошибках.
  </Accordion>

  {" "}

  <Accordion title="Можно ли временно отключить MCP‑сервер?">
    Да! Переключай серверы вкл/выкл, не удаляя их: 1) Открой Settings (
    <Kbd>Cmd+Shift+J</Kbd>) 2) Перейди в Features → Model Context Protocol 3) Нажми
    тумблер рядом с нужным сервером, чтобы включить/отключить. Отключённые серверы не будут загружаться и
    появляться в чате. Это удобно для отладки или чтобы не захламлять список инструментов.
  </Accordion>

  {" "}

  <Accordion title="Что будет, если MCP‑сервер упадёт или истечёт таймаут?">
    Если MCP‑сервер не отработал: — Cursor покажет сообщение об ошибке в чате — Вызов
    инструмента пометится как неуспешный — Можно повторить операцию или посмотреть логи для
    деталей — Другие MCP‑серверы продолжат работать нормально. Cursor изолирует сбои,
    чтобы один сервер не влиял на другие.
  </Accordion>

  {" "}

  <Accordion title="Как обновить MCP‑сервер?">
    Для серверов на npm: 1) Удали сервер в настройках 2) Очисти кэш npm:
    `npm cache clean --force` 3) Добавь сервер заново, чтобы получить последнюю версию. Для
    кастомных серверов обнови локальные файлы и перезапусти Cursor.
  </Accordion>

  <Accordion title="Можно ли использовать MCP‑серверы с чувствительными данными?">
    Да, но соблюдай лучшие практики безопасности: — Используй переменные окружения для
    секретов, никогда не хардкодь их — Запускай чувствительные серверы локально с транспортом `stdio`
    — Ограничивай права API‑ключей до минимума — Проверяй код сервера перед подключением к чувствительным системам — Рассмотри запуск серверов в изолированных окружениях
  </Accordion>
</AccordionGroup>

---

← Previous: [Игнорирование файлов](./section.md) | [Index](./index.md) | Next: [Memories](./memories.md) →