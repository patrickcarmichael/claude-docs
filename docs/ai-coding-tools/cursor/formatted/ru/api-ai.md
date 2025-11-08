---
title: "API отслеживания AI‑кода"
source: "https://docs.cursor.com/ru/account/teams/ai-code-tracking-api"
language: "ru"
language_name: "Russian"
---

# API отслеживания AI‑кода
Source: https://docs.cursor.com/ru/account/teams/ai-code-tracking-api

Доступ к аналитике кода, сгенерированной AI, для репозиториев твоей команды

Доступ к аналитике кода, сгенерированной AI, для репозиториев твоей команды. Включает использование AI по каждому коммиту и детализированные принятые изменения, сгенерированные AI.

<Note>
  API в первой версии. Мы расширяем возможности на основе обратной связи — дай знать, какие эндпоинты тебе нужны!
</Note>

* **Доступность**: Только для enterprise‑команд
* **Статус**: Альфа (схемы ответов и поля могут меняться)

<div id="authentication">
  ## Аутентификация
</div>

Все запросы к API требуют аутентификации с помощью ключа API. Этот API использует ту же схему аутентификации Admin API, что и другие эндпоинты.

Подробные инструкции по аутентификации см. в разделе [Admin API authentication](/ru/account/teams/admin-api#authentication).

<div id="base-url">
  ## Базовый URL
</div>

Все эндпоинты API используют:

```
https://api.cursor.com
```

<div id="rate-limits">
  ## Лимиты запросов
</div>

* 5 запросов в минуту на команду на каждый endpoint

<div id="query-parameters">
  ## Параметры запроса
</div>

Все конечные точки ниже принимают одинаковые параметры через строку запроса:

<div className="full-width-table">
  | Parameter   | Type   | Required | Description                                                                                                                                                                                                  |                                                                                                                        |
  | :---------- | :----- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
  | `startDate` | string | date     | No                                                                                                                                                                                                           | Дата в формате ISO, литерал "now" или относительные дни вроде "7d" (означает now - 7 days). По умолчанию: now - 7 days |
  | `endDate`   | string | date     | No                                                                                                                                                                                                           | Дата в формате ISO, литерал "now" или относительные дни вроде "0d". По умолчанию: now                                  |
  | `page`      | number | No       | Номер страницы (начиная с 1). По умолчанию: 1                                                                                                                                                                |                                                                                                                        |
  | `pageSize`  | number | No       | Количество результатов на страницу. По умолчанию: 100, максимум: 1000                                                                                                                                        |                                                                                                                        |
  | `user`      | string | No       | Необязательный фильтр по одному пользователю. Принимает email (например, [developer@company.com](mailto:developer@company.com)), кодированный ID (например, user\_abc123...), или числовой ID (например, 42) |                                                                                                                        |
</div>

<Note>
  В ответах userId возвращается как кодированный внешний ID с префиксом user\_. Значение стабильно для использования через API.
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## Семантика и вычисление метрик
</div>

* **Источники**: "TAB" — принятые встроенные автодополнения; "COMPOSER" — принятые диффы из Composer
* **Метрики по строкам**: tabLinesAdded/Deleted и composerLinesAdded/Deleted считаются отдельно; nonAiLinesAdded/Deleted вычисляются как max(0, totalLines - AI lines)
* **Режим приватности**: если включён в клиенте, часть метаданных (например, fileName) может быть опущена
* **Информация о ветке**: isPrimaryBranch имеет значение true, когда текущая ветка совпадает с веткой по умолчанию в репозитории; может быть undefined, если данные о репозитории недоступны

Можешь пролистать этот файл, чтобы понять, как обнаруживаются и отображаются коммиты и изменения.

<div id="endpoints">
  ## Эндпоинты
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### Получить метрики AI-коммитов (JSON, с пагинацией)
</div>

Получить агрегированные метрики по каждому коммиту с распределением строк между TAB, COMPOSER и non‑AI.

```
GET /analytics/ai-code/commits
```

<div id="response">
  #### Ответ
</div>

```typescript  theme={null}
{
  items: AiCommitMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### Поля AiCommitMetric
</div>

<div className="full-width-table">
  | Field                  | Type    | Description                                             |                                      |
  | :--------------------- | :------ | :------------------------------------------------------ | ------------------------------------ |
  | `commitHash`           | string  | Хеш коммита Git                                         |                                      |
  | `userId`               | string  | Закодированный ID пользователя (например, user\_abc123) |                                      |
  | `userEmail`            | string  | Адрес электронной почты пользователя                    |                                      |
  | `repoName`             | string  | null                                                    | Название репозитория                 |
  | `branchName`           | string  | null                                                    | Название ветки                       |
  | `isPrimaryBranch`      | boolean | null                                                    | Является ли это основной веткой      |
  | `totalLinesAdded`      | number  | Всего строк добавлено в коммите                         |                                      |
  | `totalLinesDeleted`    | number  | Всего строк удалено в коммите                           |                                      |
  | `tabLinesAdded`        | number  | Строк добавлено с помощью автодополнения по TAB         |                                      |
  | `tabLinesDeleted`      | number  | Строк удалено с помощью автодополнения по TAB           |                                      |
  | `composerLinesAdded`   | number  | Строк добавлено через Composer                          |                                      |
  | `composerLinesDeleted` | number  | Строк удалено через Composer                            |                                      |
  | `nonAiLinesAdded`      | number  | null                                                    | Строк, добавленных не ИИ             |
  | `nonAiLinesDeleted`    | number  | null                                                    | Строк, удаленных не ИИ               |
  | `message`              | string  | null                                                    | Сообщение коммита                    |
  | `commitTs`             | string  | null                                                    | Временная метка коммита (формат ISO) |
  | `createdAt`            | string  | Временная метка загрузки (формат ISO)                   |                                      |
</div>

<div id="example-response">
  #### Пример ответа
</div>

```json  theme={null}
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "Рефакторинг: вынести клиент аналитики"
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

<div id="example-requests">
  #### Примеры запросов
</div>

**Простой запрос:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u ТВОЙ_API_KEY:
```

**Фильтр по пользователю (email):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u ТВОЙ_API_KEY:
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### Скачать метрики AI Commit (CSV, стриминг)
</div>

Скачай метрики коммитов в формате CSV для выгрузки больших объемов данных.

```
GET /analytics/ai-code/commits.csv
```

<div id="response">
  #### Ответ
</div>

Заголовки:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### Колонки CSV
</div>

<div className="full-width-table">
  | Column                   | Type    | Description                         |
  | :----------------------- | :------ | :---------------------------------- |
  | `commit_hash`            | string  | Хеш коммита Git                     |
  | `user_id`                | string  | Кодированный ID пользователя        |
  | `user_email`             | string  | Электронная почта пользователя      |
  | `repo_name`              | string  | Название репозитория                |
  | `branch_name`            | string  | Название ветки                      |
  | `is_primary_branch`      | boolean | Является ли это основной веткой     |
  | `total_lines_added`      | number  | Всего строк добавлено в коммите     |
  | `total_lines_deleted`    | number  | Всего строк удалено в коммите       |
  | `tab_lines_added`        | number  | Строк добавлено через TAB-комплишны |
  | `tab_lines_deleted`      | number  | Строк удалено через TAB-комплишны   |
  | `composer_lines_added`   | number  | Строк добавлено через Composer      |
  | `composer_lines_deleted` | number  | Строк удалено через Composer        |
  | `non_ai_lines_added`     | number  | Строк, добавленных без ИИ           |
  | `non_ai_lines_deleted`   | number  | Строк, удалённых без ИИ             |
  | `message`                | string  | Сообщение коммита                   |
  | `commit_ts`              | string  | Метка времени коммита (ISO)         |
  | `created_at`             | string  | Метка времени загрузки (ISO)        |
</div>

<div id="sample-csv-output">
  #### Пример CSV-вывода
</div>

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"Рефакторинг: выделить клиент аналитики",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"Добавить обработку ошибок",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-request">
  #### Пример запроса
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u ТВОЙ_API_KEY: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### Получить метрики изменений кода ИИ (JSON, постранично)
</div>

Получай детальные принятые изменения ИИ, сгруппированные по детерминированному changeId. Полезно для анализа принятых событий ИИ независимо от коммитов.

```
GET /analytics/ai-code/changes
```

<div id="response">
  #### Ответ
</div>

```typescript  theme={null}
{
  items: МетрикаИзмененийКодаИИ[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### Поля AiCodeChangeMetric
</div>

<div className="full-width-table">
  | Поле                | Тип    | Описание                                                           |                        |
  | :------------------ | :----- | :----------------------------------------------------------------- | ---------------------- |
  | `changeId`          | string | Детерминированный идентификатор изменения                          |                        |
  | `userId`            | string | Кодированный идентификатор пользователя (например, user\_abc123)   |                        |
  | `userEmail`         | string | Адрес электронной почты пользователя                               |                        |
  | `source`            | "TAB"  | "COMPOSER"                                                         | Источник AI-изменения  |
  | `model`             | string | null                                                               | Используемая модель ИИ |
  | `totalLinesAdded`   | number | Всего добавленных строк                                            |                        |
  | `totalLinesDeleted` | number | Всего удалённых строк                                              |                        |
  | `createdAt`         | string | Время загрузки (ISO-формат)                                        |                        |
  | `metadata`          | Array  | Метаданные файла (fileName может быть опущен в режиме приватности) |                        |
</div>

<div id="example-response">
  #### Пример ответа
</div>

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
      "metadata": [
        { "fileName": "src/analytics/report.ts", "fileExtension": "ts", "linesAdded": 12, "linesDeleted": 3 },
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

<div id="example-requests">
  #### Примеры запросов
</div>

**Простой запрос:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u ТВОЙ_API_KEY:
```

**Фильтр по пользователю (кодированный ID):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u ТВОЙ_API_KEY:
```

**Фильтр по пользователю (email):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u ТВОЙ_API_KEY:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### Скачать метрики изменений кода ИИ (CSV, стриминг)
</div>

Скачай метрики изменений в формате CSV для больших выгрузок.

```
GET /analytics/ai-code/changes.csv
```

<div id="response">
  #### Ответ
</div>

Заголовки:

* Content-Type: text/csv; charset=utf-8

#### Столбцы CSV

<div className="full-width-table">
  | Column                | Type   | Description                                                        |
  | :-------------------- | :----- | :----------------------------------------------------------------- |
  | `change_id`           | string | Детерминированный идентификатор изменения                          |
  | `user_id`             | string | Кодированный идентификатор пользователя                            |
  | `user_email`          | string | Адрес электронной почты пользователя                               |
  | `source`              | string | Источник AI-изменения (TAB или COMPOSER)                           |
  | `model`               | string | Используемая AI‑модель                                             |
  | `total_lines_added`   | number | Всего добавлено строк                                              |
  | `total_lines_deleted` | number | Всего удалено строк                                                |
  | `created_at`          | string | Время загрузки (формат ISO)                                        |
  | `metadata_json`       | string | Строка JSON со строковым представлением массива записей метаданных |
</div>

<div id="notes">
  #### Примечания
</div>

* metadata\_json — это строка JSON со строковым представлением массива записей метаданных (в режиме приватности может опускаться fileName)
* При чтении CSV обязательно парсь поля в кавычках

#### Пример вывода CSV

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-request">
  #### Пример запроса
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u YOUR_API_KEY: \
  -o changes.csv
```

<div id="tips">
  ## Советы
</div>

* Используй параметр `user`, чтобы быстро отфильтровать одного пользователя на всех эндпоинтах
* Для больших выгрузок данных предпочитай CSV-эндпоинты — они передают данные потоками по 10 000 записей на стороне сервера
* `isPrimaryBranch` может быть `undefined`, если клиент не смог определить ветку по умолчанию
* `commitTs` — это метка времени коммита; `createdAt` — время приёма данных на наших серверах
* Некоторые поля могут отсутствовать, если на клиенте включён режим конфиденциальности

<div id="changelog">
  ## Журнал изменений
</div>

* **Альфа-релиз**: Первичные эндпоинты для коммитов и изменений. Форматы ответов могут меняться на основе обратной связи

---

← Previous: [Admin API](./admin-api.md) | [Index](./index.md) | Next: [Аналитика](./section.md) →