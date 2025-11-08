---
title: "Rules"
source: "https://docs.cursor.com/ru/context/rules"
language: "ru"
language_name: "Russian"
---

# Rules
Source: https://docs.cursor.com/ru/context/rules

Управляй поведением модели Agent с помощью многоразовых инструкций с ограниченной областью.

Правила задают системные инструкции для Agent и Inline Edit. Думай о них как о постоянном контексте, предпочтениях или рабочих процессах для твоих проектов.

Cursor поддерживает четыре типа правил:

<CardGroup cols={2}>
  <Card title="Project Rules" icon="folder-tree">
    Хранятся в `.cursor/rules`, под версионным контролем и привязаны к твоей кодовой базе.
  </Card>

  <Card title="User Rules" icon="user">
    Глобальные для твоего окружения Cursor. Задаются в настройках и всегда применяются.
  </Card>

  <Card title="AGENTS.md" icon="robot">
    Инструкции для Agent в формате Markdown. Простая альтернатива `.cursor/rules`.
  </Card>

  <Card title=".cursorrules (Legacy)" icon="clock-rotate-left">
    По-прежнему поддерживается, но устарело. Используй Project Rules.
  </Card>
</CardGroup>

<div id="how-rules-work">
  ## Как работают правила
</div>

Большие языковые модели не хранят состояние между ответами. Правила задают постоянный, многократно используемый контекст на уровне промпта.

При применении содержимое правил добавляется в начало контекста модели. Это даёт ИИ стабильные ориентиры для генерации кода, интерпретации правок и помощи с рабочими процессами.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Правило применено в контексте чата" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
</Frame>

<Info>
  Правила работают в [Chat](/ru/chat/overview) и [Inline
  Edit](/ru/inline-edit/overview). Активные правила отображаются в боковой панели Agent.
</Info>

<div id="project-rules">
  ## Правила проекта
</div>

Правила проекта хранятся в `.cursor/rules`. Каждое правило — отдельный файл под контролем версий. Их можно ограничивать шаблонами путей, вызывать вручную или подключать по степени релевантности. Вложенные директории могут иметь собственный `.cursor/rules`, применяемый в пределах этой папки.

Используй правила проекта, чтобы:

* Закодировать предметно-специфичные знания о своей кодовой базе
* Автоматизировать проектные рабочие процессы или шаблоны
* Стандартизировать решения по стилю или архитектуре

<div id="rule-anatomy">
  ### Анатомия правила
</div>

Каждый файл правила пишется в **MDC** (`.mdc`) — формате, который поддерживает метаданные и содержимое. Управляй применением правил через выпадающий список типа — он меняет свойства `description`, `globs`, `alwaysApply`.

| <span class="no-wrap">Тип правила</span>       | Описание                                                                  |
| :--------------------------------------------- | :------------------------------------------------------------------------ |
| <span class="no-wrap">`Always`</span>          | Всегда включается в контекст модели                                       |
| <span class="no-wrap">`Auto Attached`</span>   | Включается, когда упоминаются файлы, совпадающие с glob‑шаблоном          |
| <span class="no-wrap">`Agent Requested`</span> | Доступно ИИ, который решает, включать его или нет. Нужно указать описание |
| <span class="no-wrap">`Manual`</span>          | Включается только при явном упоминании с помощью `@ruleName`              |

```
---
description: Заготовка сервиса RPC
globs:
alwaysApply: false
---

- Используй наш внутренний RPC-паттерн при определении сервисов
- Всегда используй snake_case для названий сервисов.

@service-template.ts
```

<div id="nested-rules">
  ### Вложенные правила
</div>

Организуй правила, размещая их в каталогах `.cursor/rules` по всему проекту. Вложенные правила автоматически подключаются, когда используются файлы из соответствующего каталога.

```
project/
  .cursor/rules/        # Общие правила проекта
  backend/
    server/
      .cursor/rules/    # Правила для backend'а
  frontend/
    .cursor/rules/      # Правила для frontend'а
```

<div id="creating-a-rule">
  ### Создание правила
</div>

Создавай правила с помощью команды `New Cursor Rule` или через `Cursor Settings > Rules`. Это создаст новый файл правила в `.cursor/rules`. В настройках ты можешь увидеть все правила и их статус.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=db8142786bbb7b7771ae0db8b2704b0b" alt="Сравнение кратких и длинных правил" data-og-width="6016" width="6016" data-og-height="3334" height="3334" data-path="images/context/rules/rule-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b6e9b8d6ca799d1af62957726b1cc52 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bfe1482ab9afc0995fe13371b26074b 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a847d915b3f106c42cba7cb1245bb138 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=356963b3607152f7ffe128cd1a2d050e 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b1e50d3721d42c691a434189729921c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d2081cf016d65053f1e517eb5734079e 2500w" />
</Frame>

<div id="generating-rules">
  ### Генерация правил
</div>

Генерируй правила прямо в чате с помощью команды `/Generate Cursor Rules`. Полезно, когда ты уже решил, как должен вести себя агент, и хочешь повторно использовать эти настройки.

<Frame>
  <video src="https://www.cursor.com/changelog/049/generate-rules.mp4" controls>
    Your browser does not support the video tag.
  </video>
</Frame>

<div id="best-practices">
  ## Рекомендации
</div>

Хорошие правила сфокусированы, применимы на практике и чётко ограничены по области.

* Держи правила короче 500 строк
* Делай крупные правила составными — разбивай их на несколько правил
* Приводи конкретные примеры или ссылки на файлы
* Избегай расплывчатых формулировок. Пиши правила как понятную внутреннюю документацию
* Переиспользуй правила, когда повторяешь подсказки в чате

<div id="examples">
  ## Примеры
</div>

<AccordionGroup>
  <Accordion title="Стандарты для фронтенд‑компонентов и валидации API">
    Это правило задаёт стандарты для фронтенд‑компонентов:

    При работе в директории components:

    * Всегда используй Tailwind для оформления
    * Используй Framer Motion для анимаций
    * Соблюдай соглашения по именованию компонентов

    Это правило требует валидацию для API‑эндпоинтов:

    В директории api:

    * Используй zod для всей валидации
    * Определяй возвращаемые типы с помощью схем zod
    * Экспортируй типы, сгенерированные из схем
  </Accordion>

  <Accordion title="Шаблоны для сервисов Express и компонентов React">
    Это правило предоставляет шаблон для сервисов Express:

    Используй этот шаблон при создании сервиса Express:

    * Следуй принципам REST
    * Подключай middleware для обработки ошибок
    * Настраивай корректное логирование

    @express-service-template.ts

    Это правило определяет структуру компонента React:

    Компоненты React должны придерживаться такой структуры:

    * Интерфейс props сверху
    * Компонент как именованный экспорт
    * Стили внизу

    @component-template.tsx
  </Accordion>

  <Accordion title="Автоматизация рабочих процессов разработки и генерация документации">
    Это правило автоматизирует анализ приложения:

    Когда просят проанализировать приложение:

    1. Запусти dev‑сервер командой `npm run dev`
    2. Собери логи из консоли
    3. Предложи оптимизации производительности

    Это правило помогает генерировать документацию:

    Помоги подготовить документацию, выполняя:

    * Извлечение комментариев из кода
    * Анализ README.md
    * Генерацию документации в Markdown
  </Accordion>

  <Accordion title="Добавление нового параметра настройки в Cursor">
    Сначала создай свойство для переключателя в `@reactiveStorageTypes.ts`.

    Добавь значение по умолчанию в `INIT_APPLICATION_USER_PERSISTENT_STORAGE` в `@reactiveStorageService.tsx`.

    Для бета‑фич добавь переключатель в `@settingsBetaTab.tsx`, иначе — в `@settingsGeneralTab.tsx`. Переключатели можно добавлять как `<SettingsSubSection>` для обычных чекбоксов. Посмотри остальные части файла для примеров.

    ```
    <SettingsSubSection
    				label="Your feature name"
    				description="Your feature description"
    				value={
    					vsContext.reactiveStorageService.applicationUserPersistentStorage
    						.myNewProperty ?? false
    				}
    				onChange={(newVal) => {
    					vsContext.reactiveStorageService.setApplicationUserPersistentStorage(
    						'myNewProperty',
    						newVal
    					);
    				}}
    			/>
    ```

    Чтобы использовать в приложении, импортируй reactiveStorageService и обращайся к свойству:

    ```
    const flagIsEnabled = vsContext.reactiveStorageService.applicationUserPersistentStorage.myNewProperty
    ```
  </Accordion>
</AccordionGroup>

Много примеров доступно от поставщиков и фреймворков. Правила, созданные сообществом, можно найти в краудсорсинговых подборках и репозиториях онлайн.

<div id="agentsmd">
  ## AGENTS.md
</div>

`AGENTS.md` — это простой файл Markdown для задания инструкций агентам. Положи его в корень проекта как альтернативу `.cursor/rules` для прямолинейных сценариев.

В отличие от Project Rules, `AGENTS.md` — это обычный файл Markdown без метаданных и сложных настроек. Он идеально подходит для проектов, где нужны простые, легко читаемые инструкции без лишней сложности структурированных правил.

```markdown  theme={null}

---

← Previous: [Memories](./memories.md) | [Index](./index.md) | Next: [Концепции](./section.md) →