---
title: "Slack"
source: "https://docs.cursor.com/ru/integrations/slack"
language: "ru"
language_name: "Russian"
---

# Slack
Source: https://docs.cursor.com/ru/integrations/slack

Работай с Background Agents из Slack

export const SlackThread = ({messages = []}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg bg-neutral-50 dark:bg-neutral-900/50 py-4 overflow-hidden">
      {messages.map((msg, index) => <div key={index} className={`group hover:bg-[#f0f0f0] dark:hover:bg-[#333] px-6 py-2 -mx-2 -my-1 transition-colors`}>
          <div className="flex items-start gap-3">
            <div className="w-9 h-9 rounded-md bg-neutral-300 dark:bg-neutral-800 flex items-center justify-center text-white text-sm font-semibold flex-shrink-0">
              {msg.name ? msg.name.charAt(0).toUpperCase() : 'U'}
            </div>

            <div className="flex-1 min-w-0">
              <div className="flex items-baseline gap-2">
                <span className="font-semibold text-neutral-900 dark:text-neutral-100 text-sm">
                  {msg.name || 'User'}
                </span>
                <span className="text-xs text-neutral-500 dark:text-neutral-400">
                  {msg.timestamp || ''}
                </span>
              </div>
              <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
                <MessageWithMentions text={msg.message} />
              </div>

              {msg.reactions && msg.reactions.length > 0 && <div className="flex gap-1 mt-1">
                  {msg.reactions.map((reaction, rIndex) => <div key={rIndex} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded text-xs hover:bg-neutral-100 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
                      <span>{reaction.emoji}</span>
                      <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
                    </div>)}
                </div>}
            </div>
          </div>
        </div>)}
    </div>;
};

export const SlackInlineMessage = ({message}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] hover:bg-[#1264A3]/10 dark:hover:bg-[#1264A3]/25 px-0.5 rounded">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <span className="inline rounded p-0.5 bg-neutral-50 dark:bg-neutral-800/30">
      <MessageWithMentions text={message} />
    </span>;
};

export const SlackUserMessage = ({message, reactions = [], replies = null}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-800/50 transition-colors px-5 py-3 group">
      <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
        <MessageWithMentions text={message} />
      </div>

      {reactions.length > 0 && <div className="flex gap-1 mt-1">
          {reactions.map((reaction, index) => <div key={index} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-neutral-100 dark:bg-neutral-800 rounded text-xs hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
              <span>{reaction.emoji}</span>
              <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
            </div>)}
        </div>}

      {replies && <div className="flex items-center gap-1.5 mt-2 text-[#1264A3] hover:underline cursor-pointer">
          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M7.707 10.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V6h5a2 2 0 012 2v7a2 2 0 01-2 2H4a2 2 0 01-2-2V8a2 2 0 012-2h5v5.586l-1.293-1.293z" />
          </svg>
          <span className="text-sm font-medium">{replies.count} {replies.count === 1 ? 'reply' : 'replies'}</span>
          {replies.lastReplyTime && <span className="text-xs text-neutral-500 dark:text-neutral-400">{replies.lastReplyTime}</span>}
        </div>}
    </div>;
};

С интеграцией Cursor для Slack ты можешь использовать [Background Agents](/ru/background-agent) и выполнять задачи прямо из Slack — просто упомяни <SlackInlineMessage message="@Cursor" /> с промптом.

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-agent.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=aa7aa2681db1e363047334c6a8e33f72" controls autoplay muted loop data-path="images/background-agent/slack/slack-agent.mp4" />
</Frame>

<div id="get-started">
  ## Начало работы
</div>

<div id="installation">
  ### Установка
</div>

1. Перейди в [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations)

2. Нажми *Connect* рядом со Slack или перейди на [installation page](https://cursor.com/api/install-slack-app) отсюда

3. Тебе предложат установить приложение Cursor для Slack в твоё рабочее пространство.

4. После установки в Slack тебя перенаправят обратно в Cursor для завершения настройки

   1. Подключи GitHub (если ещё не подключён) и выбери репозиторий по умолчанию
   2. Включи оплату по фактическому использованию
   3. Подтверди настройки конфиденциальности

5. Начни использовать Background Agents в Slack, упомянув <SlackInlineMessage message="@Cursor" />

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/cursor-slack-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd5b3c65b1a0de08b46c90515b6056a6" controls autoplay muted loop data-path="images/background-agent/slack/cursor-slack-install.mp4" />
</Frame>

<div id="how-to-use">
  ## Как использовать
</div>

Упомяни <SlackInlineMessage message="@Cursor" /> и дай свой запрос. Этого хватает для большинства случаев, но можно использовать команды ниже, чтобы тонко настроить агента.

Например, упомяни <SlackInlineMessage message="@Cursor fix the login bug" /> прямо в переписке или используй команды вроде <SlackInlineMessage message="@Cursor [repo=torvalds/linux] fix bug" /> для нацеливания на конкретный репозиторий.

<div id="commands">
  ### Команды
</div>

Запусти <SlackInlineMessage message="@Cursor help" /> для актуального списка команд.

<div className="full-width-table">
  | Команда                                                     | Описание                                                                                         |
  | :---------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
  | <SlackInlineMessage message="@Cursor [prompt]" />           | Запускает Background Agent. В тредах с уже запущенными агентами добавляет последующие инструкции |
  | <SlackInlineMessage message="@Cursor settings" />           | Настроить значения по умолчанию и репозиторий по умолчанию для канала                            |
  | <SlackInlineMessage message="@Cursor [options] [prompt]" /> | Использовать расширенные опции: `branch`, `model`, `repo`                                        |
  | <SlackInlineMessage message="@Cursor agent [prompt]" />     | Принудительно создать нового агента в треде                                                      |
  | <SlackInlineMessage message="@Cursor list my agents" />     | Показать запущенные агенты                                                                       |
</div>

<div id="options">
  #### Опции
</div>

Настрой поведение Background Agent с помощью этих опций:

<div className="full-width-table">
  | Опция    | Описание                                      | Пример            |
  | :------- | :-------------------------------------------- | :---------------- |
  | `branch` | Указать базовую ветку                         | `branch=main`     |
  | `model`  | Выбрать модель ИИ                             | `model=o3`        |
  | `repo`   | Нацелить на конкретный репозиторий            | `repo=owner/repo` |
  | `autopr` | Включить/выключить автоматическое создание PR | `autopr=false`    |
</div>

<div id="syntax-formats">
  ##### Форматы синтаксиса
</div>

Используй опции несколькими способами:

1. **Формат с квадратными скобками**

   <SlackInlineMessage message="@Cursor [branch=dev, model=o3, repo=owner/repo, autopr=false] Fix the login bug" />

2. **Встроенный формат**
   <SlackInlineMessage message="@Cursor branch=dev model=o3 repo=owner/repo autopr=false Fix the login bug" />

<div id="option-precedence">
  ##### Приоритет опций
</div>

При комбинировании опций:

* **Явные значения** переопределяют значения по умолчанию
* **Более поздние значения** переопределяют более ранние при дублировании
* **Встроенные опции** имеют приоритет над значениями из окна настроек

Бот парсит опции из любого места в сообщении, позволяя писать команды естественно.

<div id="using-thread-context">
  #### Использование контекста треда
</div>

Background Agents понимают и используют контекст из обсуждения в существующем треде. Полезно, когда команда обсуждает проблему, и ты хочешь, чтобы агент реализовал решение на основе этой беседы.

<SlackThread
  messages={[
{
  message:
    "Hey team, we're getting reports that users can't log in after the latest deploy",
  timestamp: "2:30 PM",
  name: "Sarah",
},
{
  message:
    "I checked the logs - looks like the auth token validation is failing on line 247 of auth.js",
  timestamp: "2:32 PM",
  name: "Mike",
},
{
  message:
    "Oh, I think it's because we changed the token format but didn't update the validation regex",
  timestamp: "2:33 PM",
  name: "Alex",
},
{
  message:
    "Yeah, the regex still expects the old format. We need to update it to handle both old and new formats for backwards compatibility",
  timestamp: "2:35 PM",
  name: "Sarah",
},
{
  message: "@Cursor fix this",
  timestamp: "2:36 PM",
  name: "You",
  reactions: [{ emoji: "⏳", count: 1 }],
},
]}
/>

<Note>
  Background Agents читают весь тред для контекста при вызове
  и реализуют решения на основе обсуждения команды.
</Note>

<div id="when-to-use-force-commands">
  #### Когда использовать принудительные команды
</div>

**Когда нужен <SlackInlineMessage message="@Cursor agent" />?**

В тредах с существующими агентами <SlackInlineMessage message="@Cursor [prompt]" /> добавляет последующие инструкции (работает только если агент принадлежит тебе). Используй <SlackInlineMessage message="@Cursor agent [prompt]" /> чтобы запустить отдельного агента.

**Когда нужна `Add follow-up` (из контекстного меню)?**

Используй контекстное меню (⋯) на ответе агента для последующих инструкций. Полезно, когда в треде несколько агентов и нужно указать, к какому из них дать follow-up.

<div id="status-updates-handoff">
  ### Обновления статуса и хендов
</div>

Когда запускается Background Agent, сначала ты получаешь опцию *Open in Cursor*.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=496d3775ca5cc1e20dd1dc34952f76fd" style={{ backgroundColor: "#1b1d21" }} data-og-width="1236" width="1236" data-og-height="258" height="258" data-path="images/background-agent/slack/slack-open-in-cursor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9136ecf72e3f7e75b2178a2922878fbd 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d6977f43055c3e8cb69071fe7b48367 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5264cb584c1160bd8ac3cdeaae320777 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a065e6c1a08d4413464e1251eab1b2a6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e067f0dc80ed77bce7843f777f2d7970 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fbcb8e474fd1681219964c558ea2952d 2500w" />
</Frame>

Когда Background Agent завершит работу, ты получишь уведомление в Slack и сможешь открыть созданный PR на GitHub.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d0f5f15094f682a5617c936bea88db3d" style={{ backgroundColor: "#1b1d21" }} data-og-width="1272" width="1272" data-og-height="496" height="496" data-path="images/background-agent/slack/slack-view-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a51c98f13fef794ba8f54a28ad42e99d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbde7fe552a04a8ed44b1771bbc3f55c 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=616811c969184b9061435e9753f63ddb 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90fe4582797d75782019c7d0c3232ea8 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffe4d6a78cad700f82e770418c7f6e13 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ec4dac244e5982d0150d058ddac0d205 2500w" />
</Frame>

<div id="managing-agents">
  ### Управление агентами
</div>

Чтобы посмотреть все запущенные агенты, отправь команду <SlackInlineMessage message="@Cursor list my agents" />.

Управляй Background Agents через контекстное меню: нажми на три точки (⋯) в любом сообщении агента.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a92748d0f4d3450d51a2c2cdd989eb1" style={{ backgroundColor: "#1b1d21" }} data-og-width="1982" width="1982" data-og-height="1498" height="1498" data-path="images/background-agent/slack/slack-context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6af034b2f0c1b510510622b111c8d4e7 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7d28c9785328aa414eba66704d7f4f08 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=810f99ed15ec100cdfee183ef9b7f827 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f4c00c380996793b50d31ef3ac95219c 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=94bccdd7d7a9f1301fdb4e832e008efa 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90e628735b628ec71d5a78547db2441c 2500w" />
</Frame>

Доступные действия:

* **Add follow-up**: добавить инструкции существующему агенту
* **Delete**: остановить и архивировать Background Agent
* **View request ID**: посмотреть уникальный ID запроса для диагностики (укажи при обращении в поддержку)
* **Give feedback**: оставить отзыв о работе агента

<div id="configuration">
  ## Конфигурация
</div>

Управляй настройками по умолчанию и параметрами конфиденциальности в [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents).

<div id="settings">
  ### Настройки
</div>

<div id="default-model">
  #### Модель по умолчанию
</div>

Используется, когда модель явно не задана через <SlackInlineMessage message="@Cursor [model=...]" />. Смотри доступные варианты в [настройках](https://www.cursor.com/dashboard?tab=background-agents).

<div id="default-repository">
  #### Репозиторий по умолчанию
</div>

Используется, когда репозиторий не указан. Используй такие форматы:

* `https://github.com/org/repository`
* `org/repository`

<Note>
  Если указать несуществующий репозиторий, будет казаться, что у тебя нет доступа.
  Это отразится в сообщении об ошибке при неудачном запуске Background Agent.
</Note>

<div id="base-branch">
  #### Базовая ветка
</div>

Начальная ветка для Background Agent. Оставь пустым, чтобы использовать ветку по умолчанию репозитория (обычно `main`).

<div id="channel-settings">
  ### Настройки канала
</div>

Настраивай значения по умолчанию на уровне канала с помощью <SlackInlineMessage message="@Cursor settings" />. Эти настройки задаются для команды и переопределяют твои личные значения по умолчанию для этого канала.

Особенно полезно, когда:

* Разные каналы работают с разными репозиториями
* Команды хотят единообразные настройки для всех участников
* Хочется не указывать репозиторий в каждой команде

Чтобы настроить параметры канала:

1. Запусти <SlackInlineMessage message="@Cursor settings" /> в нужном канале
2. Задай репозиторий по умолчанию для этого канала
3. Все участники команды, использующие Background Agents в этом канале, будут использовать эти значения по умолчанию

<Note>
  Настройки канала имеют приоритет над личными настройками по умолчанию, но могут быть
  переопределены явными опциями, например{" "}

  <SlackInlineMessage message="@Cursor [repo=...] [prompt]" />
</Note>

<div id="privacy">
  ### Конфиденциальность
</div>

Background Agents поддерживают режим конфиденциальности.

Подробнее о [режиме конфиденциальности](https://www.cursor.com/privacy-overview) или управляй своими [настройками конфиденциальности](https://www.cursor.com/dashboard?tab=background-agents).

<Warning>
  Legacy-режим конфиденциальности не поддерживается. Background Agents требуют временного
  хранения кода во время работы.
</Warning>

<div id="display-agent-summary">
  #### Показывать сводку агента
</div>

Показывать сводки агента и diff-изображения. Может содержать пути к файлам или фрагменты кода. Можно включать/выключать.

<div id="display-agent-summary-in-external-channels">
  #### Показывать сводку агента во внешних каналах
</div>

Для Slack Connect с другими рабочими пространствами или каналами с внешними участниками, например гостями, можно включить показ сводок агента во внешних каналах.

<div id="permissions">
  ## Разрешения
</div>

Cursor запрашивает эти разрешения Slack, чтобы Background Agents могли работать в твоём рабочем пространстве:

<div className="full-width-table">
  | Разрешение          | Описание                                                                                              |
  | :------------------ | :---------------------------------------------------------------------------------------------------- |
  | `app_mentions:read` | Отслеживает @упоминания, чтобы запускать Background Agents и отвечать на запросы                      |
  | `channels:history`  | Читает предыдущие сообщения в тредах для контекста при добавлении последующих инструкций              |
  | `channels:join`     | Автоматически присоединяется к публичным каналам по приглашению или запросу                           |
  | `channels:read`     | Доступ к метаданным каналов (ID и названия), чтобы публиковать ответы и обновления                    |
  | `chat:write`        | Отправляет обновления статуса, уведомления о завершении и ссылки на PR, когда агенты завершили работу |
  | `files:read`        | Скачивает общие файлы (логи, скриншоты, примеры кода) для дополнительного контекста                   |
  | `files:write`       | Загружает визуальные сводки изменений агентов для быстрого просмотра                                  |
  | `groups:history`    | Читает предыдущие сообщения в приватных каналах для контекста в многошаговых диалогах                 |
  | `groups:read`       | Доступ к метаданным приватных каналов, чтобы публиковать ответы и поддерживать ход беседы             |
  | `im:history`        | Доступ к истории личных сообщений для контекста в продолжающихся беседах                              |
  | `im:read`           | Читает метаданные ЛС, чтобы идентифицировать участников и поддерживать корректную нитку обсуждения    |
  | `im:write`          | Инициирует личные сообщения для приватных уведомлений или индивидуального общения                     |
  | `mpim:history`      | Доступ к истории групповых ЛС для бесед с несколькими участниками                                     |
  | `mpim:read`         | Читает метаданные групповых ЛС, чтобы обращаться к участникам и обеспечивать корректную доставку      |
  | `reactions:read`    | Отслеживает эмодзи-реакции для обратной связи и сигналов статуса                                      |
  | `reactions:write`   | Добавляет эмодзи-реакции для отметки статуса — ⏳ выполняется, ✅ завершено, ❌ ошибка                   |
  | `team:read`         | Определяет параметры рабочего пространства, чтобы разделять установки и применять настройки           |
  | `users:read`        | Сопоставляет пользователей Slack с аккаунтами Cursor для прав и безопасного доступа                   |
</div>

---

← Previous: [Linear](./linear.md) | [Index](./index.md) | Next: [Модели](./section.md) →