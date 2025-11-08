---
title: "Linear"
source: "https://docs.cursor.com/ru/integrations/linear"
language: "ru"
language_name: "Russian"
---

# Linear
Source: https://docs.cursor.com/ru/integrations/linear

Работай с Background Agents прямо из Linear

Используй [Background Agents](/ru/background-agent) напрямую в Linear — делегируй задачи Cursor или упоминай `@Cursor` в комментариях.

<Frame>
  <video src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-agent.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ac4bacf6bf42c541f45325ba72f8c25f" controls autoPlay muted loop playsInline data-path="images/integrations/linear/linear-agent.mp4" />
</Frame>

<div id="get-started">
  ## Начало работы
</div>

<div id="installation">
  ### Установка
</div>

<Note>
  Ты должен быть админом Cursor, чтобы подключить интеграцию с Linear. Другие настройки команды доступны и для участников без прав админа.
</Note>

1. Перейди в [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations)
2. Нажми *Connect* рядом с Linear
3. Подключи своё рабочее пространство Linear и выбери команду
4. Нажми *Authorize*
5. Заверши оставшуюся настройку Background Agent в Cursor:
   * Подключи GitHub и выбери репозиторий по умолчанию
   * Включи тарификацию по использованию
   * Подтверди настройки конфиденциальности

<div id="account-linking">
  ### Связка аккаунтов
</div>

При первом запуске будет предложено связать аккаунты Cursor и Linear. Подключение GitHub требуется для создания PR.

<div id="how-to-use">
  ## Как пользоваться
</div>

Делегируй задачи Cursor или упоминай `@Cursor` в комментариях. Cursor анализирует задачи и автоматически отсекает работу, не связанную с разработкой.

<div id="delegating-issues">
  ### Делегирование задач
</div>

1. Открой задачу в Linear
2. Нажми на поле assignee
3. Выбери «Cursor»

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c9a6536a083cfe4a7798c626360e53cc" alt="Делегирование задачи Cursor в Linear" data-og-width="1637" width="1637" data-og-height="1046" height="1046" data-path="images/integrations/linear/linear-delegate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b30e2ccb68c4a15b921cf86721878676 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1ac5dfd75e06451de0e688ff87e1ce4c 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7393e80c07e1fe5c33690a970029fe31 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2a07cc74a1d65581a341cf2225b51a37 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5684841fe823ef85472f74748730278c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f7818cae47a652e14557eb20f20b04e 2500w" />
</Frame>

<div id="mentioning-cursor">
  ### Упоминание Cursor
</div>

Упомяни `@Cursor` в комментарии, чтобы назначить нового агента или дать дополнительные инструкции, например: `@Cursor исправь описанную выше ошибку аутентификации`.

<div id="workflow">
  ## Процесс работы
</div>

Background Agents показывают статус в реальном времени в Linear и автоматически создают PR по завершении. Отслеживай прогресс в [дашборде Cursor](https://www.cursor.com/dashboard?tab=background-agents).

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eecf562be6db4d44c397f4786b8ef273" alt="Обновления статуса Background Agent в Linear" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-activity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=238da245aee71392f22644cb85f7cee4 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21f515fbd2e5917fcf63b8801f66307 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f88441301e6d614ba47756cb886e023 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4927a8d00768a3dbbc0bd5be1faad80e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1707f8223126480c46639428ad5fc85a 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=74ca2ad37e8158bbb86188821bf96299 2500w" />
</Frame>

<div id="follow-up-instructions">
  ### Последующие инструкции
</div>

Можешь ответить прямо в сессии агента — это уйдёт к нему как последующий комментарий. Просто упомяни `@Cursor` в комментарии в Linear, чтобы дать дополнительные указания запущенному Background Agent.

<div id="configuration">
  ## Конфигурация
</div>

Настрой параметры Background Agent в [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents).

<div className="full-width-table">
  | Setting                | Location         | Description                                                 |
  | :--------------------- | :--------------- | :---------------------------------------------------------- |
  | **Default Repository** | Cursor Dashboard | Основной репозиторий, если репозиторий проекта не задан     |
  | **Default Model**      | Cursor Dashboard | AI‑модель для Background Agents                             |
  | **Base Branch**        | Cursor Dashboard | Базовая ветка для создания PR (обычно `main` или `develop`) |
</div>

<div id="configuration-options">
  ### Параметры конфигурации
</div>

Поведение Background Agent можно настроить несколькими способами:

**Описание issue или комментарии**: используй синтаксис `[key=value]`, например:

* `@cursor please fix [repo=anysphere/everysphere]`
* `@cursor implement feature [model=claude-3.5-sonnet] [branch=feature-branch]`

**Метки issue**: используй иерархию меток родитель → дочерняя, где родительская метка — ключ конфигурации, а дочерняя — значение.

**Метки проекта**: та же иерархия, что и для меток issue, применяется на уровне проекта.

Поддерживаемые ключи конфигурации:

* `repo`: укажи целевой репозиторий (например, `owner/repository`)
* `branch`: укажи базовую ветку для создания PR
* `model`: укажи используемую AI‑модель

<div id="repository-selection">
  ### Выбор репозитория
</div>

Cursor определяет, с каким репозиторием работать, в следующем порядке приоритетов:

1. **Описание issue/комментарии**: синтаксис `[repo=owner/repository]` в тексте issue или комментариях
2. **Метки issue**: метки репозитория, добавленные к конкретному issue в Linear
3. **Метки проекта**: метки репозитория, добавленные к проекту в Linear
4. **Репозиторий по умолчанию**: репозиторий, указанный в настройках Cursor Dashboard

<div id="setting-up-repository-labels">
  #### Настройка меток репозитория
</div>

Чтобы создать метки репозитория в Linear:

1. Перейди в **Settings** своего рабочего пространства Linear
2. Нажми **Labels**
3. Нажми **New group**
4. Назови группу "repo" (регистронезависимо — должно быть именно "repo", не "Repository" и не другие варианты)
5. Внутри этой группы создай метки для каждого репозитория в формате `owner/repo`

Эти метки потом можно назначать issue или проектам, чтобы указать, с каким репозиторием должен работать Background Agent.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6e2b90ce09957a72fdef3c1ed4ef93aa" alt="Настройка меток репозитория в Linear" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-project-labels.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1933d2112631527116bd1d817f1a6153 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=93f344ff848172ce6bd97ef652ab03de 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea9f19d7248f39086a20606c6ec14ac6 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=55bfa5cf5b87def6cbe51c3345579eee 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d99c0f06c5fbf33794408350b143f655 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1f731d1978dc5e60c545b745bb9d8ad 2500w" />
</Frame>

{/* ### Getting help

  Check [agent activity](https://www.cursor.com/dashboard?tab=background-agents) and include request IDs when contacting support.

  ## Feedback

  Share feedback through Linear comments or your Cursor dashboard support channels. */}

---

← Previous: [GitHub](./github.md) | [Index](./index.md) | Next: [Slack](./slack.md) →