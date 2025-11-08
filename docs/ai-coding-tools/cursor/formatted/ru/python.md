---
title: "Python"
source: "https://docs.cursor.com/ru/guides/languages/python"
language: "ru"
language_name: "Russian"
---

# Python
Source: https://docs.cursor.com/ru/guides/languages/python

Настрой разработку на Python с расширениями и инструментами для линтинга

<Note>
  Этот гайд во многом вдохновлён работой [Jack Fields](https://x.com/OrdinaryInds)
  и его
  [статьёй](https://medium.com/ordinaryindustries/the-ultimate-vs-code-setup-for-python-538026b34d94)
  о настройке VS Code для разработки на Python. Загляни в его статью для
  подробностей.
</Note>

<div id="prerequisites">
  ## Необходимые условия
</div>

Прежде чем начать, убедись, что у тебя есть:

* Установленный [Python](https://python.org) (рекомендуется версия 3.8 или новее)
* [Git](https://git-scm.com/) для системы контроля версий
* Установленный Cursor, обновлённый до последней версии

<div id="essential-extensions">
  ## Важные расширения
</div>

Следующие расширения настраивают Cursor как полноценную среду для разработки на Python. Они дают подсветку синтаксиса, линтинг, отладку и модульное тестирование.

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Базовая поддержка языка от Microsoft
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Быстрый сервер языка Python
  </Card>

  <Card title="Python Debugger" icon="bug" href="cursor:extension/ms-python.debugpy">
    Расширенные возможности отладки
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Линтер и форматтер для Python
  </Card>
</CardGroup>

<div id="advanced-python-tooling">
  ### Продвинутые инструменты для Python
</div>

Хотя перечисленные выше расширения раньше были самыми популярными для разработки на Python в Cursor, мы также добавили дополнительные расширения, которые помогут выжать максимум из разработки на Python.

<div id="uv-python-environment-manager">
  #### `uv` — менеджер Python-окружений
</div>

[uv](https://github.com/astral-sh/uv) — современный менеджер пакетов для Python, который можно использовать для создания и управления виртуальными окружениями, а также как замену pip по умолчанию.

Чтобы установить uv, выполни следующую команду в терминале:

```bash  theme={null}
pip install uv
```

<div id="ruff-python-linter-and-formatter">
  #### `ruff` — линтер и форматтер для Python
</div>

[Ruff](https://docs.astral.sh/ruff/) — современный линтер и форматтер для Python, который помогает находить ошибки, соблюдать код-стайл и подсказывает варианты рефакторинга. Его можно использовать вместе с Black для форматирования кода.

Чтобы установить Ruff, выполни в терминале команду:

```bash  theme={null}
pip install ruff
```

<div id="cursor-configuration">
  ## Настройка Cursor
</div>

<div id="1-python-interpreter">
  ### 1. Интерпретатор Python
</div>

Настрой интерпретатор Python в Cursor:

1. Открой Command Palette (Cmd/Ctrl + Shift + P)
2. Найди «Python: Select Interpreter»
3. Выбери интерпретатор Python (или виртуальное окружение, если ты его используешь)

<div id="2-code-formatting">
  ### 2. Форматирование кода
</div>

Включи автоформатирование кода с помощью Black:

<Note>
  Black — это форматтер кода, который автоматически приводит твой код к
  единому стилю. Он не требует конфигурации и широко используется
  в сообществе Python.
</Note>

Чтобы установить Black, выполни в терминале команду:

```bash  theme={null}
pip install black
```

Далее настрой Cursor на использование Black для форматирования кода, добавив в свой файл `settings.json` следующий блок:

```json  theme={null}
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.formatting.blackArgs": ["--line-length", "88"]
}
```

<div id="3-linting">
  ### 3. Линтинг
</div>

Мы можем использовать PyLint для поиска ошибок в коде, соблюдения стандартов и предложений по рефакторингу.

Чтобы установить PyLint, запусти в терминале следующую команду:

```bash  theme={null}
pip install pylint
```

```json  theme={null}
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.lintOnSave": true
}
```

<div id="4-type-checking">
  ### 4. Проверка типов
</div>

Помимо линтинга можно использовать MyPy для проверки ошибок типов.

Чтобы установить MyPy, выполни в терминале следующую команду:

```bash  theme={null}
pip install mypy
```

```json  theme={null}
{
  "python.linting.mypyEnabled": true
}
```

<div id="debugging">
  ## Отладка
</div>

В Cursor есть мощные инструменты отладки для Python:

1. Ставь точки останова, кликая по полю слева от номера строки
2. Открывай панель Debug (Cmd/Ctrl + Shift + D)
3. Настрой `launch.json` для кастомных конфигураций отладки

<div id="recommended-features">
  ## Рекомендуемые функции
</div>

<CardGroup cols={3}>
  <Card title="Tab Completion" icon="wand-magic-sparkles" href="/ru/tab/overview">
    Умные подсказки кода, которые понимают, что ты делаешь
  </Card>

  <Card title="Chat" icon="comments" href="/ru/chat/overview">
    Изучай и понимай код через естественные диалоги
  </Card>

  <Card title="Agent" icon="robot" href="/ru/chat/agent">
    Решай сложные задачи разработки с помощью ИИ
  </Card>

  <Card title="Context" icon="network-wired" href="/ru/context/model-context-protocol">
    Подтягивай контекст из сторонних систем
  </Card>

  <Card title="Auto-Imports" icon="file-import" href="/ru/tab/auto-import">
    Автоматически импортируй модули по мере написания кода
  </Card>

  <Card title="AI Review" icon="check-double" href="/ru/tab/overview#quality">
    Cursor постоянно проверяет твой код с помощью ИИ
  </Card>
</CardGroup>

<div id="framework-support">
  ## Поддержка фреймворков
</div>

Cursor без проблем работает с популярными фреймворками для Python:

* **Веб‑фреймворки**: Django, Flask, FastAPI
* **Data Science**: Jupyter, NumPy, Pandas
* **Машинное обучение**: TensorFlow, PyTorch, scikit-learn
* **Тестирование**: pytest, unittest
* **API**: requests, aiohttp
* **Базы данных**: SQLAlchemy, psycopg2

---

← Previous: [JavaScript & TypeScript](./javascript-typescript.md) | [Index](./index.md) | Next: [iOS и macOS (Swift)](./ios-macos-swift.md) →