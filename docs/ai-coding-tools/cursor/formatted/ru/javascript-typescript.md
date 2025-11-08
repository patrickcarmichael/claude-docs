---
title: "JavaScript & TypeScript"
source: "https://docs.cursor.com/ru/guides/languages/javascript"
language: "ru"
language_name: "Russian"
---

# JavaScript & TypeScript
Source: https://docs.cursor.com/ru/guides/languages/javascript

Разработка на JavaScript и TypeScript с поддержкой фреймворков

Добро пожаловать в мир JavaScript и TypeScript в Cursor! Редактор отлично поддерживает разработку на JS/TS благодаря экосистеме расширений. Вот что тебе нужно знать, чтобы выжать из Cursor максимум.

<div id="essential-extensions">
  ## Важные расширения
</div>

Хотя Cursor отлично работает с любыми расширениями, которые тебе нравятся, для старта мы рекомендуем следующие:

* **ESLint** — нужен для AI-функций Cursor по автоисправлению проблем линтинга
* **JavaScript and TypeScript Language Features** — расширенная поддержка языков и IntelliSense
* **Path Intellisense** — умное автодополнение путей к файлам

<div id="cursor-features">
  ## Возможности Cursor
</div>

Cursor прокачивает твой текущий рабочий процесс на JavaScript/TypeScript благодаря:

* **Дополнениям по Tab**: Контекстно‑зависимые подсказки кода, понимающие структуру твоего проекта
* **Автоматическим импортам**: Tab может автоматически импортировать библиотеки, как только ты их используешь
* **Встроенному редактированию**: Жми `CMD+K` на любой строке, чтобы редактировать с идеальным синтаксисом
* **Подсказкам Composer**: Планируй и редактируй код в нескольких файлах с помощью Composer

<div id="framework-intelligence-with-docs">
  ### Интеллект фреймворков с @Docs
</div>

Функция @Docs в Cursor позволяет прокачать разработку на JavaScript, добавляя кастомные источники документации, к которым может обращаться ИИ. Добавь документацию из MDN, Node.js или своего любимого фреймворка, чтобы получать более точные и контекстные подсказки кода.

<Card title="Узнай больше про @Docs" icon="book" href="/ru/context/@-symbols/@-docs">
  Узнай, как добавлять и управлять пользовательскими источниками документации в Cursor.
</Card>

<div id="automatic-linting-resolution">
  ### Автоматическое исправление предупреждений линтера
</div>

Одна из ключевых фишек Cursor — бесшовная интеграция с расширениями линтеров.
Убедись, что у тебя настроен линтер, например ESLint, и включена настройка «Iterate on Lints».

Затем, при использовании режима Agent в Composer, после того как ИИ попытается ответить на твой запрос и внесёт изменения в код, он автоматически прочитает вывод линтера и попытается исправить любые ошибки линтинга, о которых мог не знать.

<div id="framework-support">
  ## Поддержка фреймворков
</div>

Cursor без швов работает со всеми основными JavaScript‑фреймворками и библиотеками, такими как:

### React & Next.js

* Полная поддержка JSX/TSX с умными подсказками по компонентам
* Понимание серверных компонентов и API‑маршрутов в Next.js
* Рекомендуется: расширение [**React Developer Tools**](cursor:extension/msjsdiag.vscode-react-native)

<div id="vuejs">
  ### Vue.js
</div>

* Поддержка синтаксиса шаблонов с интеграцией Volar
* Автодополнение компонентов и проверка типов
* Рекомендуется: [**Vue Language Features**](cursor:extension/vue.volar)

<div id="angular">
  ### Angular
</div>

* Проверка шаблонов и поддержка декораторов TypeScript
* Генерация компонентов и сервисов
* Рекомендуется: [**Angular Language Service**](cursor:extension/Angular.ng-template)

<div id="svelte">
  ### Svelte
</div>

* Подсветка синтаксиса компонентов и умные автодополнения
* Подсказки для реактивных выражений и store
* Рекомендуется: [**Svelte for VS Code**](cursor:extension/svelte.svelte-vscode)

<div id="backend-frameworks-expressnestjs">
  ### Серверные фреймворки (Express/NestJS)
</div>

* Понимание маршрутов и middleware
* Поддержка декораторов TypeScript для NestJS
* Интеграция инструментов для тестирования API

Помни, AI‑возможности Cursor отлично работают со всеми этими фреймворками: они понимают их паттерны и лучшие практики и выдают релевантные подсказки. AI поможет со всем — от создания компонентов до сложного рефакторинга, при этом соблюдая существующие паттерны твоего проекта.

---

← Previous: [Java](./java.md) | [Index](./index.md) | Next: [Python](./python.md) →