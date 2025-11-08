---
title: "Bugbot"
source: "https://docs.cursor.com/ru/bugbot"
language: "ru"
language_name: "Russian"
---

# Bugbot
Source: https://docs.cursor.com/ru/bugbot

AI‑ревью кода для pull request’ов

Bugbot проверяет pull request’ы и находит баги, уязвимости и проблемы с качеством кода.

<Tip>
  У Bugbot есть бесплатный тариф: каждый пользователь получает ограниченное число бесплатных ревью PR в месяц. Когда ты достигаешь лимита, ревью приостанавливаются до следующего биллингового цикла. В любой момент можно включить 14‑дневный бесплатный Pro‑триал для безлимитных ревью (с учётом стандартных ограничений против злоупотреблений).
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="Bugbot оставляет комментарии в PR" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

<div id="how-it-works">
  ## Как это работает
</div>

Bugbot анализирует диффы PR и оставляет комментарии с объяснениями и предложениями по исправлению. Он запускается автоматически при каждом обновлении PR или вручную по команде.

* Запускает **автоматические обзоры** при каждом обновлении PR
* **Ручной запуск** — комментарием `cursor review` или `bugbot run` в любом PR
* Ссылки **Fix in Cursor** открывают проблемы прямо в Cursor
* Ссылки **Fix in Web** открывают проблемы прямо на [cursor.com/agents](https://cursor.com/agents)

<div id="setup">
  ## Настройка
</div>

Нужны права администратора в Cursor и права администратора организации в GitHub.

1. Перейди на [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot)
2. Открой вкладку Bugbot
3. Нажми `Connect GitHub` (или `Manage Connections`, если уже подключено)
4. Заверши установку GitHub
5. Вернись в дашборд, чтобы включить Bugbot для конкретных репозиториев

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Настройка Bugbot в GitHub" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

<div id="configuration">
  ## Конфигурация
</div>

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### Настройки репозитория

    Включай или отключай Bugbot для каждого репозитория в списке установок. Bugbot запускается только на PR, автором которых являешься ты.

    ### Личные настройки

    * Запускать **только по упоминанию**, оставив комментарий `cursor review` или `bugbot run`
    * Запускать **только один раз** на PR, пропуская последующие коммиты
  </Tab>

  <Tab title="Team">
    ### Настройки репозитория

    Админы команды могут включать Bugbot для каждого репозитория, настраивать allow/deny-листы для ревьюеров и задавать:

    * Запуск **только один раз** на PR для каждой установки, пропуская последующие коммиты
    * **Отключить встроенные ревью**, чтобы Bugbot не оставлял комментарии прямо в строках кода

    Bugbot запускается для всех контрибьюторов в включённых репозиториях, независимо от членства в команде.

    ### Личные настройки

    Участники команды могут переопределять настройки для своих PR:

    * Запускать **только по упоминанию**, оставив комментарий `cursor review` или `bugbot run`
    * Запускать **только один раз** на PR, пропуская последующие коммиты
    * **Включить ревью для черновых PR**, чтобы черновые pull request-ы включались в автоматические проверки
  </Tab>
</Tabs>

<div id="analytics">
  ### Аналитика
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Дашборд Bugbot" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

<div id="rules">
  ## Правила
</div>

Создавай файлы `.cursor/BUGBOT.md`, чтобы добавить проектный контекст для ревью. Bugbot всегда включает корневой `.cursor/BUGBOT.md` и любые дополнительные файлы, найденные при подъёме вверх от изменённых файлов.

```
project/
  .cursor/BUGBOT.md          # Всегда подключается (правила для всего проекта)
  backend/
    .cursor/BUGBOT.md        # Подключается при проверке файлов backend
    api/
      .cursor/BUGBOT.md      # Подключается при проверке файлов API
  frontend/
    .cursor/BUGBOT.md        # Подключается при проверке файлов frontend
```

<AccordionGroup>
  <Accordion title="Пример .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # Рекомендации по ревью проекта

    ## Ключевые аспекты безопасности

    - Валидируй пользовательский ввод в API-эндпоинтах
    - Проверяй уязвимости SQL‑инъекций в запросах к базе данных
    - Обеспечь корректную аутентификацию на защищённых маршрутах

    ## Архитектурные паттерны

    - Используй внедрение зависимостей (dependency injection) для сервисов
    - Следуй паттерну репозитория (repository) для доступа к данным
    - Реализуй корректную обработку ошибок с пользовательскими классами ошибок

    ## Распространённые проблемы

    - Утечки памяти в React‑компонентах (проверь очистку в useEffect)
    - Отсутствуют границы ошибок (error boundaries) в UI‑компонентах
    - Несогласованные соглашения по наименованию (используй camelCase для функций)

    ```
  </Accordion>
</AccordionGroup>

<div id="pricing">
  ## Цены
</div>

Bugbot предлагает два тарифа: **Free** и **Pro**.

<div id="free-tier">
  ### Бесплатный тариф
</div>

Каждый пользователь получает ограниченное число бесплатных PR‑ревью в месяц. В командах у каждого участника есть свои бесплатные ревью. Когда ты достигаешь лимита, ревью приостанавливаются до следующего расчетного периода. В любой момент можно перейти на 14‑дневный бесплатный пробный период Pro с неограниченным числом ревью.

<div id="pro-tier">
  ### Тариф Pro
</div>

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### Фиксированная цена

    \$40 в месяц за неограниченные ревью Bugbot — до 200 PR в месяц по всем репозиториям.

    ### Начало работы

    Оформи подписку в настройках аккаунта.
  </Tab>

  <Tab title="Teams">
    ### Оплата за пользователя

    Команды платят \$40 за пользователя в месяц за неограниченные ревью.

    Под пользователем мы считаем того, кто в течение месяца создал PR, которые ревьюил Bugbot.

    Все лицензии снимаются в начале каждого биллингового цикла и распределяются по принципу «первый пришёл — первый получил». Если пользователь в течение месяца не создал ни одного PR, который ревьюил Bugbot, его место может занять другой.

    ### Лимиты мест

    Админы команды могут задавать максимальное число мест Bugbot в месяц, чтобы контролировать расходы.

    ### Начало работы

    Оформи подписку через командную панель, чтобы включить биллинг.

    ### Защита от злоупотреблений

    Чтобы предотвратить злоупотребления, действует общий лимит — 200 pull request в месяц на каждую лицензию Bugbot. Если тебе нужно больше 200 pull request в месяц, напиши нам на [hi@cursor.com](mailto:hi@cursor.com), и мы с радостью поможем.

    Например, если в твоей команде 100 пользователей, организация изначально сможет ревьюить 20 000 pull request в месяц. Если ты естественным образом достигнешь этого лимита, свяжись с нами — мы с радостью его увеличим.
  </Tab>
</Tabs>

<div id="troubleshooting">
  ## Устранение неполадок
</div>

Если Bugbot не работает:

1. **Включи подробный режим** — оставь комментарий `cursor review verbose=true` или `bugbot run verbose=true`, чтобы получить подробные логи и ID запроса
2. **Проверь права доступа**, чтобы убедиться, что у Bugbot есть доступ к репозиторию
3. **Проверь установку**, чтобы подтвердить, что GitHub‑приложение установлено и включено

Когда сообщаешь о проблемах, обязательно укажи ID запроса из подробного режима.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Bugbot поддерживает режим повышенной конфиденциальности?">
    Да, Bugbot соответствует тем же требованиям к конфиденциальности, что и Cursor, и обрабатывает данные так же, как и другие запросы Cursor.
  </Accordion>

  <Accordion title="Что происходит, когда я достигаю лимита бесплатного тарифа?">
    Когда ты достигаешь ежемесячного лимита бесплатного тарифа, проверки Bugbot приостанавливаются до следующего расчетного периода. Ты можешь перейти на 14‑дневную бесплатную пробную версию Pro с неограниченными проверками (с учетом стандартных механизмов защиты от злоупотреблений).
  </Accordion>
</AccordionGroup>

```
```

---

← Previous: [Веб и Мобайл](./section.md) | [Index](./index.md) | Next: [Code Review](./code-review.md) →