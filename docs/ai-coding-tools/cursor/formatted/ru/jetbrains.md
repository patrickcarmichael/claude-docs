---
title: "JetBrains"
source: "https://docs.cursor.com/ru/guides/migration/jetbrains"
language: "ru"
language_name: "Russian"
---

# JetBrains
Source: https://docs.cursor.com/ru/guides/migration/jetbrains

Переходи с IDE JetBrains на Cursor с привычными инструментами

Cursor — это современная среда для написания кода с ИИ, которая может заменить твои IDE JetBrains. Поначалу переход может показаться непривычным, но основа Cursor на базе VS Code даёт мощные возможности и широкие возможности настройки.

<div id="editor-components">
  ## Компоненты редактора
</div>

<div id="extensions">
  ### Расширения
</div>

IDE от JetBrains — классные инструменты: они уже преднастроены под нужные языки и фреймворки.

Cursor другой — это чистый холст из коробки: настраивай его как хочешь, не ограничиваясь языками и фреймворками, под которые задумывалась IDE.

У Cursor есть доступ к огромной экосистеме расширений, и почти всю функциональность (и даже больше!), которую предлагают IDE от JetBrains, можно воссоздать с их помощью.

Посмотри на некоторые популярные расширения ниже:

<CardGroup cols={4}>
  <Card title="Remote SSH" icon="network-wired" href="cursor:extension/anysphere.remote-ssh">
    Расширение для SSH
  </Card>

  <Card title="Project Manager" icon="folder-tree" href="cursor:extension/alefragnani.project-manager">
    Управляй несколькими проектами
  </Card>

  <Card title="GitLens" icon="git" href="cursor:extension/eamodio.gitlens">
    Расширенная интеграция с Git
  </Card>

  <Card title="Local History" icon="clock-rotate-left" href="cursor:extension/xyz.local-history">
    Отслеживание локальных изменений файлов
  </Card>

  <Card title="Error Lens" icon="bug" href="cursor:extension/usernamehw.errorlens">
    Подсветка ошибок прямо в коде
  </Card>

  <Card title="ESLint" icon="code-compare" href="cursor:extension/dbaeumer.vscode-eslint">
    Линтинг кода
  </Card>

  <Card title="Prettier" icon="wand-magic-sparkles" href="cursor:extension/esbenp.prettier-vscode">
    Форматирование кода
  </Card>

  <Card title="Todo Tree" icon="folder-tree" href="cursor:extension/Gruntfuggly.todo-tree">
    Отслеживание TODO и FIXME
  </Card>
</CardGroup>

<div id="keyboard-shortcuts">
  ### Комбинации клавиш
</div>

В Cursor есть встроенный менеджер сочетаний клавиш, который позволяет привязывать любимые хоткеи к действиям.

С этим расширением можно перенести почти все сочетания клавиш из IDE JetBrains прямо в Cursor!
Обязательно прочитай документацию расширения, чтобы настроить его под себя:

<Card title="IntelliJ IDEA Keybindings" icon="keyboard" href="cursor:extension/k--kato.intellij-idea-keybindings">
  Установи это расширение, чтобы перенести сочетания клавиш IDE JetBrains в Cursor.
</Card>

<Note>
  Распространённые сочетания, которые отличаются:

  * Find Action: ⌘/Ctrl+Shift+P  (vs. ⌘/Ctrl+Shift+A)
  * Quick Fix: ⌘/Ctrl+.  (vs. Alt+Enter)
  * Go to File: ⌘/Ctrl+P  (vs. ⌘/Ctrl+Shift+N)
</Note>

<div id="themes">
  ### Темы
</div>

Воссоздай внешний вид и ощущения от любимых IDE JetBrains в Cursor с помощью этих тем от сообщества.

Выбирай стандартную тему Darcula или подбери тему под подсветку синтаксиса твоих инструментов JetBrains.

<CardGroup cols={1}>
  <Card title="JetBrains - Darcula Theme" icon="moon" horizontal href="cursor:extension/rokoroku.vscode-theme-darcula">
    Ощути классическую тёмную тему JetBrains Darcula
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="JetBrains PyCharm" icon="python" horizontal href="cursor:extension/gabemahoney.pycharm-dark-theme-for-python" />

  <Card title="IntelliJ" icon="java" horizontal href="cursor:extension/compassak.intellij-idea-new-ui" />

  <Card title="JetBrains Fleet" icon="code" horizontal href="cursor:extension/MichaelZhou.fleet-theme" />

  <Card title="JetBrains Rider" icon="hashtag" horizontal href="cursor:extension/muhammad-sammy.rider-theme" />
</CardGroup>

<CardGroup cols={1}>
  <Card title="JetBrains Icons" icon="icons" horizontal href="cursor:extension/ardonplay.vscode-jetbrains-icon-theme">
    Привычные значки файлов и папок JetBrains
  </Card>
</CardGroup>

<div id="font">
  ### Шрифт
</div>

Чтобы завершить «джетбрейнс-подобный» опыт, можно использовать официальный шрифт JetBrains Mono:

1. Скачай и установи шрифт JetBrains Mono в систему:

<CardGroup cols={1}>
  <Card title="Download JetBrains Mono" icon="link" horizontal href="https://www.jetbrains.com/lp/mono/" />
</CardGroup>

2. Перезапусти Cursor после установки шрифта
3. Открой Settings в Cursor (⌘/Ctrl + ,)
4. Найди "Font Family"
5. Выбери семейство шрифтов `'JetBrains Mono'`

<Note>
  Для лучшего опыта можно включить лигатуры шрифта, установив в настройках «editor.fontLigatures»: true.
</Note>

<div id="ide-specific-migration">
  ## Миграция под конкретные IDE
</div>

Многим нравятся IDE от JetBrains за готовую из коробки поддержку языков и фреймворков, под которые они создавались. Cursor другой — это чистый холст из коробки: ты настраиваешь его под себя и не ограничиваешься наборами языков и фреймворков, на которые изначально рассчитана IDE.

У Cursor уже есть доступ к экосистеме расширений VS Code, и практически весь функционал (и даже больше!), который предлагают IDE от JetBrains, можно воспроизвести через эти расширения.

Ниже посмотри рекомендуемые расширения для каждой IDE JetBrains.

<div id="intellij-idea-java">
  ### IntelliJ IDEA (Java)
</div>

<CardGroup cols={2}>
  <Card title="Language Support for Java" icon="java" href="cursor:extension/redhat.java">
    Базовые возможности языка Java
  </Card>

  <Card title="Debugger for Java" icon="bug" href="cursor:extension/vscjava.vscode-java-debug">
    Поддержка отладки Java
  </Card>

  <Card title="Test Runner for Java" icon="vial" href="cursor:extension/vscjava.vscode-java-test">
    Запуск и отладка тестов Java
  </Card>

  <Card title="Maven for Java" icon="box" href="cursor:extension/vscjava.vscode-maven">
    Поддержка Maven
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Project Manager for Java" icon="folder-tree" href="cursor:extension/vscjava.vscode-java-dependency" horizontal>
    Инструменты управления проектами
  </Card>
</CardGroup>

<Warning>
  Ключевые отличия:

  * Конфигурации сборки/запуска управляются через launch.json
  * Инструменты Spring Boot доступны через расширение ["Spring Boot Extension Pack"](cursor:extension/vmware.vscode-boot-dev-pack)
  * Поддержка Gradle через расширение ["Gradle for Java"](cursor:extension/vscjava.vscode-gradle)
</Warning>

<div id="pycharm-python">
  ### PyCharm (Python)
</div>

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Базовая поддержка Python
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Быстрая проверка типов
  </Card>

  <Card title="Jupyter" icon="notebook" href="cursor:extension/ms-toolsai.jupyter">
    Поддержка ноутбуков
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Форматтер и линтер для Python
  </Card>
</CardGroup>

<Note>
  Ключевые отличия:

  * Виртуальные окружения управляются через палитру команд
  * Конфигурации отладки в launch.json
  * Управление зависимостями через requirements.txt или Poetry
</Note>

<div id="webstorm-javascripttypescript">
  ### WebStorm (JavaScript/TypeScript)
</div>

<CardGroup cols={2}>
  <Card title="JavaScript and TypeScript Nightly" icon="js" href="cursor:extension/ms-vscode.vscode-typescript-next">
    Самые свежие возможности языка
  </Card>

  <Card title="ES7+ React/Redux Snippets" icon="react" href="cursor:extension/dsznajder.es7-react-js-snippets">
    Разработка на React
  </Card>

  <Card title="Vue Language Features" icon="vuejs" href="cursor:extension/Vue.volar">
    Поддержка Vue.js
  </Card>

  <Card title="Angular Language Service" icon="angular" href="cursor:extension/Angular.ng-template">
    Разработка на Angular
  </Card>
</CardGroup>

<Info>
  Большинство возможностей WebStorm встроены в Cursor/VS Code, включая:

  * просмотр npm-скриптов
  * отладку
  * интеграцию с Git
  * поддержку TypeScript
</Info>

<div id="phpstorm-php">
  ### PhpStorm (PHP)
</div>

<CardGroup cols={2}>
  <Card title="PHP Intelephense" icon="php" href="cursor:extension/bmewburn.vscode-intelephense-client">
    Языковой сервер PHP
  </Card>

  <Card title="PHP Debug" icon="bug" href="cursor:extension/xdebug.php-debug">
    Интеграция с Xdebug
  </Card>

  <Card title="PHP Intellisense" icon="brain" href="cursor:extension/felixfbecker.php-intellisense">
    Интеллектуальные подсказки кода
  </Card>

  <Card title="PHP DocBlocker" icon="comment-dots" href="cursor:extension/neilbrayfield.php-docblocker">
    Инструменты документации
  </Card>
</CardGroup>

<Note>
  Ключевые отличия:

  * Конфигурация Xdebug через launch.json
  * Интеграция Composer через терминал
  * Инструменты работы с базами данных через расширение ["SQLTools"](cursor:extension/mtxr.sqltools)
</Note>

<div id="rider-net">
  ### Rider (.NET)
</div>

<CardGroup cols={2}>
  <Card title="C#" icon="code" href="cursor:extension/anysphere.csharp">
    Базовая поддержка C#
  </Card>

  <Card title="DotRush" icon="toolbox" href="cursor:extension/nromanov.dotrush">
    Открытая среда разработки C#
  </Card>

  <Card title="ReSharper Plugin" icon="box" href="https://www.jetbrains.com/help/resharper-vscode/Get_started.html#installation">
    Плагин JetBrains для C#
  </Card>

  <Card title=".NET Install Tool" icon="box-open" href="cursor:extension/ms-dotnettools.vscode-dotnet-runtime">
    Управление .NET SDK
  </Card>
</CardGroup>

<Warning>
  Ключевые отличия:

  * Обозреватель решений через проводник файлов
  * Управление пакетами NuGet через CLI или расширения
  * Интеграция тест-раннера через обозреватель тестов
</Warning>

<div id="goland-go">
  ### GoLand (Go)
</div>

<CardGroup cols={1}>
  <Card title="Go" icon="golang" href="cursor:extension/golang.Go">
    Официальное расширение Go
  </Card>
</CardGroup>

<Note>
  Ключевые отличия:

  * Установка инструментов Go предлагается автоматически
  * Отладка через launch.json
  * Управление пакетами интегрировано с go.mod
</Note>

<div id="tips-for-a-smooth-transition">
  ## Советы для плавного перехода
</div>

<Steps>
  <Step title="Используй командную палитру">
    Нажми <kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>, чтобы найти команды
  </Step>

  <Step title="AI‑возможности">
    Используй AI‑возможности Cursor для автодополнения кода и рефакторинга
  </Step>

  <Step title="Настройка параметров">
    Точно настрой свой settings.json для оптимального рабочего процесса
  </Step>

  <Step title="Интеграция терминала">
    Пользуйся встроенным терминалом для работы в командной строке
  </Step>

  <Step title="Расширения">
    Просматривай маркетплейс VS Code в поисках дополнительных инструментов
  </Step>
</Steps>

<Info>
  Помни: хотя некоторые сценарии работы могут отличаться, Cursor предлагает мощные AI‑функции для помощи в написании кода, которые повысят твою продуктивность сверх возможностей традиционных IDE.
</Info>

---

← Previous: [iOS и macOS (Swift)](./ios-macos-swift.md) | [Index](./index.md) | Next: [VS Code](./vs-code.md) →