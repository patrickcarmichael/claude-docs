---
title: "Admin API"
source: "https://docs.cursor.com/ru/account/teams/admin-api"
language: "ru"
language_name: "Russian"
---

# Admin API
Source: https://docs.cursor.com/ru/account/teams/admin-api

Доступ к командным метрикам, данным об использовании и информации о расходах через API

Admin API позволяет программно получать доступ к данным твоей команды, включая сведения об участниках, метрики использования и детали расходов. Собирай кастомные панели, инструменты мониторинга или интегрируй с существующими рабочими процессами.

<Note>
  Это первый релиз API. Мы расширяем возможности на основе фидбэка — напиши, какие эндпоинты тебе нужны!
</Note>

<div id="authentication">
  ## Аутентификация
</div>

Все запросы к API требуют аутентификации с использованием API‑ключа. Создавать и управлять API‑ключами могут только админы команды.

API‑ключи привязаны к организации, видны всем админам и не зависят от статуса учетной записи их первоначального создателя.

<div id="creating-an-api-key">
  ### Создание API-ключа
</div>

1. Перейди в **cursor.com/dashboard** → вкладка **Settings** → **Cursor Admin API Keys**
2. Нажми **Create New API Key**
3. Дай ключу понятное имя (например, «Usage Dashboard Integration»)
4. Сразу скопируй сгенерированный ключ — потом ты его больше не увидишь

Формат: `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### Использование API-ключа
</div>

Используй свой API-ключ как имя пользователя в базовой аутентификации:

**Использование curl с базовой аутентификацией:**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**Или задай заголовок Authorization вручную:**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## Базовый URL
</div>

Все эндпоинты API используют:

```
https://api.cursor.com
```

<div id="endpoints">
  ## Конечные точки
</div>

<div id="get-team-members">
  ### Получение участников команды
</div>

Получить список всех участников команды и их данные.

```
GET /teams/members
```

#### Ответ

Возвращает массив объектов участников команды:

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: 'владелец' | 'участник' | 'владелец бесплатного тарифа';
  }[];
}
```

<div id="example-response">
  #### Пример отклика
</div>

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "участник"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "владелец"
    }
  ]
}

```

#### Пример запроса

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u ТВОЙ_API_KEY:
```

<div id="get-daily-usage-data">
  ### Получить данные по ежедневному использованию
</div>

Получай подробные метрики по ежедневному использованию для своей команды за заданный период. Дают представление о правках кода, использовании AI‑ассистента и коэффициентах принятия.

```
POST /teams/daily-usage-data
```

#### Тело запроса

<div className="full-width-table">
  | Параметр    | Тип    | Обязательный | Описание                                  |
  | :---------- | :----- | :----------- | :---------------------------------------- |
  | `startDate` | number | Да           | Дата начала в миллисекундах эпохи Unix    |
  | `endDate`   | number | Да           | Дата окончания в миллисекундах эпохи Unix |
</div>

<Note>
  Диапазон дат не может превышать 90 дней. Для более длинных периодов сделай несколько запросов.
</Note>

#### Ответ

```typescript  theme={null}
{
  data: {
    date: number;
    isActive: boolean;
    totalLinesAdded: number;
    totalLinesDeleted: number;
    acceptedLinesAdded: number;
    acceptedLinesDeleted: number;
    totalApplies: number;
    totalAccepts: number;
    totalRejects: number;
    totalTabsShown: number;
    totalTabsAccepted: number;
    composerRequests: number;
    chatRequests: number;
    agentRequests: number;
    cmdkUsages: number;
    subscriptionIncludedReqs: number;
    apiKeyReqs: number;
    usageBasedReqs: number;
    bugbotUsages: number;
    mostUsedModel: string;
    applyMostUsedExtension?: string;
    tabMostUsedExtension?: string;
    clientVersion?: string;
    email?: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### Поля ответа
</div>

<div className="full-width-table">
  | Field                      | Description                                   |
  | :------------------------- | :-------------------------------------------- |
  | `date`                     | Дата в миллисекундах с начала эпохи           |
  | `isActive`                 | Пользователь активен в этот день              |
  | `totalLinesAdded`          | Добавленные строки кода                       |
  | `totalLinesDeleted`        | Удалённые строки кода                         |
  | `acceptedLinesAdded`       | Строки, добавленные из принятых AI-подсказок  |
  | `acceptedLinesDeleted`     | Строки, удалённые из принятых AI-подсказок    |
  | `totalApplies`             | Операции Apply                                |
  | `totalAccepts`             | Принятые подсказки                            |
  | `totalRejects`             | Отклонённые подсказки                         |
  | `totalTabsShown`           | Показанные автодополнения Tab                 |
  | `totalTabsAccepted`        | Принятые автодополнения Tab                   |
  | `composerRequests`         | Запросы Composer                              |
  | `chatRequests`             | Запросы Chat                                  |
  | `agentRequests`            | Запросы Agent                                 |
  | `cmdkUsages`               | Использования палитры команд (Cmd+K)          |
  | `subscriptionIncludedReqs` | Запросы, включённые в подписку                |
  | `apiKeyReqs`               | Запросы с API-ключом                          |
  | `usageBasedReqs`           | Запросы с оплатой по факту использования      |
  | `bugbotUsages`             | Использования детектора багов                 |
  | `mostUsedModel`            | Самая часто используемая AI‑модель            |
  | `applyMostUsedExtension`   | Самое используемое расширение файла для Apply |
  | `tabMostUsedExtension`     | Самое используемое расширение файла для Tab   |
  | `clientVersion`            | Версия Cursor                                 |
  | `email`                    | Электронная почта пользователя                |
</div>

#### Пример ответа

```json  theme={null}
{
  "data": [
    {
      "date": 1710720000000,
      "isActive": true,
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalApplies": 87,
      "totalAccepts": 73,
      "totalRejects": 14,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "cmdkUsages": 67,
      "subscriptionIncludedReqs": 180,
      "apiKeyReqs": 0,
      "usageBasedReqs": 5,
      "bugbotUsages": 3,
      "mostUsedModel": "gpt-4",
      "applyMostUsedExtension": ".tsx",
      "tabMostUsedExtension": ".ts",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    },
    {
      "date": 1710806400000,
      "isActive": true,
      "totalLinesAdded": 2104,
      "totalLinesDeleted": 1203,
      "acceptedLinesAdded": 1876,
      "acceptedLinesDeleted": 987,
      "totalApplies": 102,
      "totalAccepts": 91,
      "totalRejects": 11,
      "totalTabsShown": 456,
      "totalTabsAccepted": 398,
      "composerRequests": 67,
      "chatRequests": 156,
      "agentRequests": 23,
      "cmdkUsages": 89,
      "subscriptionIncludedReqs": 320,
      "apiKeyReqs": 15,
      "usageBasedReqs": 0,
      "bugbotUsages": 5,
      "mostUsedModel": "claude-3-opus",
      "applyMostUsedExtension": ".py",
      "tabMostUsedExtension": ".py",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

#### Пример запроса

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### Получить данные о расходах
</div>

Получай информацию о расходах за текущий календарный месяц с поддержкой поиска, сортировки и пагинации.

```
POST /teams/spend
```

#### Тело запроса

<div className="full-width-table">
  | Параметр        | Тип    | Обязательно | Описание                                                        |
  | :-------------- | :----- | :---------- | :-------------------------------------------------------------- |
  | `searchTerm`    | string | Нет         | Поиск по именам пользователей и адресам email                   |
  | `sortBy`        | string | Нет         | Сортировать по: `amount`, `date`, `user`. По умолчанию — `date` |
  | `sortDirection` | string | Нет         | Направление сортировки: `asc`, `desc`. По умолчанию — `desc`    |
  | `page`          | number | Нет         | Номер страницы (начиная с 1). По умолчанию — `1`                |
  | `pageSize`      | number | Нет         | Количество результатов на странице                              |
</div>

#### Ответ

```typescript  theme={null}
{
  teamMemberSpend: {
    spendCents: number;
    fastPremiumRequests: number;
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
    hardLimitOverrideDollars: number;
  }[];
  subscriptionCycleStart: number;
  totalMembers: number;
  totalPages: number;
}
```

<div id="response-fields">
  #### Поля ответа
</div>

<div className="full-width-table">
  | Поле                       | Описание                                                     |
  | :------------------------- | :----------------------------------------------------------- |
  | `spendCents`               | Общие траты в центах                                         |
  | `fastPremiumRequests`      | Запросы к быстрой премиум‑модели                             |
  | `name`                     | Имя участника                                                |
  | `email`                    | Email участника                                              |
  | `role`                     | Роль в команде                                               |
  | `hardLimitOverrideDollars` | Пользовательское переопределение лимита трат                 |
  | `subscriptionCycleStart`   | Начало расчетного периода подписки (миллисекунды Unix Epoch) |
  | `totalMembers`             | Общее число участников команды                               |
  | `totalPages`               | Общее число страниц                                          |
</div>

#### Пример ответа

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "участник",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "владелец"
      "hardLimitOverrideDollars": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

<div id="example-requests">
  #### Примеры запросов
</div>

**Основные данные о расходах:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Поиск конкретного пользователя с пагинацией:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

<div id="get-usage-events-data">
  ### Получить данные о событиях использования
</div>

Получи подробные данные о событиях использования для своей команды с расширенной фильтрацией, поиском и пагинацией. Этот эндпоинт дает детализированную информацию по отдельным вызовам API, использованию моделей, расходу токенов и затратам.

```
POST /teams/filtered-usage-events
```

#### Тело запроса

<div className="full-width-table">
  | Параметр    | Тип    | Обязательный | Описание                                               |
  | :---------- | :----- | :----------- | :----------------------------------------------------- |
  | `startDate` | number | Нет          | Дата начала в миллисекундах эпохи Unix                 |
  | `endDate`   | number | Нет          | Дата окончания в миллисекундах эпохи Unix              |
  | `userId`    | number | Нет          | Фильтр по конкретному ID пользователя                  |
  | `page`      | number | Нет          | Номер страницы (начиная с 1). По умолчанию: `1`        |
  | `pageSize`  | number | Нет          | Количество результатов на странице. По умолчанию: `10` |
  | `email`     | string | Нет          | Фильтр по адресу электронной почты пользователя        |
</div>

#### Ответ

```typescript  theme={null}
{
  totalUsageEventsCount: number;
  pagination: {
    numPages: number;
    currentPage: number;
    pageSize: number;
    hasNextPage: boolean;
    hasPreviousPage: boolean;
  };
  usageEvents: {
    timestamp: string;
    model: string;
    kind: string;
    maxMode: boolean;
    requestsCosts: number;
    isTokenBasedCall: boolean;
    tokenUsage?: {
      inputTokens: number;
      outputTokens: number;
      cacheWriteTokens: number;
      cacheReadTokens: number;
      totalCents: number;
    };
    isFreeBugbot: boolean;
    userEmail: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields-explained">
  #### Пояснение полей ответа
</div>

<div className="full-width-table">
  | Field                   | Description                                                                       |
  | :---------------------- | :-------------------------------------------------------------------------------- |
  | `totalUsageEventsCount` | Общее число событий использования, соответствующих запросу                        |
  | `pagination`            | Метаданные пагинации для навигации по результатам                                 |
  | `timestamp`             | Временная метка события в миллисекундах эпохи                                     |
  | `model`                 | Используемая для запроса модель ИИ                                                |
  | `kind`                  | Категория использования (например, «Usage-based», «Included in Business»)         |
  | `maxMode`               | Включён ли max mode                                                               |
  | `requestsCosts`         | Стоимость в единицах запросов                                                     |
  | `isTokenBasedCall`      | True, если событие тарифицируется как основанное на токенах                       |
  | `tokenUsage`            | Детализированное потребление токенов (доступно, если isTokenBasedCall равен true) |
  | `isFreeBugbot`          | Было ли это бесплатное использование bugbot                                       |
  | `userEmail`             | Email пользователя, который сделал запрос                                         |
  | `period`                | Диапазон дат запрошенных данных                                                   |
</div>

#### Пример ответа

```json  theme={null}
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "model": "claude-4-opus",
      "kind": "Оплата по использованию",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750979173824",
      "model": "claude-4-opus",
      "kind": "Оплата по использованию",
      "maxMode": true,
      "requestsCosts": 10,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 5805,
        "outputTokens": 311,
        "cacheWriteTokens": 11964,
        "cacheReadTokens": 0,
        "totalCents": 40.16699999999999
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750978339901",
      "model": "claude-4-sonnet-thinking",
      "kind": "Включено в Business"
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isFreeBugbot": false,
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

<div id="example-requests">
  #### Примеры запросов
</div>

**Получить все события использования с пагинацией по умолчанию:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Фильтрация по диапазону дат и конкретному пользователю:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**Получай события использования для конкретного пользователя с кастомной пагинацией:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u ТВОЙ_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### Установить лимит расходов пользователя
</div>

Настрой лимиты расходов для отдельных участников команды. Это позволит контролировать, сколько каждый пользователь может тратить на использование ИИ в твоей команде.

```
POST /teams/user-spend-limit
```

<Note>
  **Лимит запросов:** 60 запросов в минуту на команду
</Note>

#### Тело запроса

<div className="full-width-table">
  | Параметр            | Тип    | Обязательный | Описание                                                              |
  | :------------------ | :----- | :----------- | :-------------------------------------------------------------------- |
  | `userEmail`         | string | Да           | Email участника команды                                               |
  | `spendLimitDollars` | number | Да           | Лимит расходов в долларах (только целое число, без дробных значений). |
</div>

<Note>
  * Пользователь уже должен быть участником твоей команды
  * Принимаются только целые числа (без дробных сумм)
  * Если установить `spendLimitDollars` в 0, лимит будет \$0
</Note>

#### Ответ

Возвращает унифицированный ответ об успехе или неудаче:

```typescript  theme={null}
{
  outcome: 'success' | 'error';
  message: string;
}
```

<div id="example-responses">
  #### Примеры ответов
</div>

**Лимит успешно задан:**

```json  theme={null}
{
  "outcome": "success",
  "message": "Лимит расходов установлен в $100 для пользователя developer@company.com"
}
```

**Сообщение об ошибке:**

```json  theme={null}
{
  "outcome": "error",
  "message": "Недопустимый формат e-mail"
}
```

<div id="example-requests">
  #### Примеры запросов
</div>

**Задать лимит расходов:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u ТВОЙ_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### API списков блокировки репозиториев
</div>

Добавляй репозитории и настраивай шаблоны, чтобы файлы и директории не индексировались и не использовались как контекст для твоей команды.

<div id="get-team-repo-blocklists">
  #### Получить блоклисты репозиториев команды
</div>

Получить все блоклисты репозиториев, настроенные для твоей команды.

```
GET /settings/repo-blocklists/repos
```

<div id="response">
  ##### Ответ
</div>

Возвращает массив объектов списка блокировок репозиториев:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

##### Пример ответа

```json  theme={null}
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

<div id="example-request">
  ##### Пример запроса
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u ТВОЙ_API_KEY:
```

<div id="upsert-repo-blocklists">
  #### Обновить/создать блок-листы репозиториев
</div>

Заменяет существующие блок-листы для указанных репозиториев.
*Примечание: этот эндпоинт перезапишет шаблоны только для указанных репозиториев. Все остальные репозитории останутся без изменений.*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### Тело запроса
</div>

| Параметр | Тип   | Обязателен | Описание                                       |
| -------- | ----- | ---------- | ---------------------------------------------- |
| repos    | array | Да         | Массив объектов списка блокировки репозиториев |

Каждый объект репозитория должен содержать:

| Поле     | Тип       | Обязателен | Описание                                                              |
| -------- | --------- | ---------- | --------------------------------------------------------------------- |
| url      | string    | Да         | URL репозитория для добавления в список блокировки                    |
| patterns | string\[] | Да         | Массив файловых шаблонов для блокировки (поддерживаются glob‑шаблоны) |

<div id="response">
  ##### Ответ
</div>

Возвращает обновлённый список блок-листов репозиториев:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-request">
  ##### Пример запроса
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      },
      {
        "url": "https://github.com/company/internal-tools", 
        "patterns": ["*"]
      }
    ]
  }'
```

<div id="delete-repo-blocklist">
  #### Удалить репозиторий из блоклиста
</div>

Удалить конкретный репозиторий из блоклиста.

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### Параметры
</div>

| Параметр | Тип    | Обязателен | Описание                                      |
| -------- | ------ | ---------- | --------------------------------------------- |
| repoId   | string | Да         | ID списка блокировок репозитория для удаления |

<div id="response">
  ##### Ответ
</div>

Возвращает статус 204 No Content при успешном удалении.

<div id="example-request">
  ##### Пример запроса
</div>

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u ТВОЙ_API_КЛЮЧ:
```

<div id="pattern-examples">
  #### Примеры шаблонов
</div>

Распространённые шаблоны блоклиста:

* `*` — Заблокировать весь репозиторий
* `*.env` — Заблокировать все файлы .env
* `config/*` — Заблокировать все файлы в каталоге config
* `**/*.secret` — Заблокировать все файлы .secret в любых подкаталогах
* `src/api/keys.ts` — Заблокировать конкретный файл

---

← Previous: [Стоимость](./section.md) | [Index](./index.md) | Next: [API отслеживания AI‑кода](./api-ai.md) →