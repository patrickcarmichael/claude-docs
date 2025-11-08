---
title: "Admin API"
source: "https://docs.cursor.com/zh/account/teams/admin-api"
language: "zh"
language_name: "Chinese"
---

# Admin API
Source: https://docs.cursor.com/zh/account/teams/admin-api

通过 API 访问团队指标、使用数据和支出信息

Admin API 让你以编程方式访问团队数据，包括成员信息、使用指标和支出详情。你可以构建自定义仪表盘、监控工具，或与现有工作流集成。

<Note>
  该 API 为首个发布版本。我们会根据反馈逐步扩展功能——告诉我们你需要哪些端点！
</Note>

<div id="authentication">
  ## 身份验证
</div>

所有 API 请求都需要使用 API 密钥进行身份验证。只有团队管理员可以创建和管理 API 密钥。

API 密钥与组织绑定，对所有管理员可见，且不受原始创建者账号状态影响。

<div id="creating-an-api-key">
  ### 创建 API Key
</div>

1. 前往 **cursor.com/dashboard** → **Settings** 标签页 → **Cursor Admin API Keys**
2. 点击 **Create New API Key**
3. 给密钥起个清晰易懂的名字（例如：“Usage Dashboard Integration”）
4. 立刻复制生成的密钥——之后将无法再次查看

格式：`key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### 使用你的 API 密钥
</div>

在基本身份验证中，将你的 API 密钥作为用户名：

**使用 curl 进行基本身份验证：**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**或者直接设置 Authorization 标头：**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## 基础 URL
</div>

所有 API 端点都使用：

```
https://api.cursor.com
```

<div id="endpoints">
  ## 端点
</div>

<div id="get-team-members">
  ### 获取团队成员
</div>

获取所有团队成员及其详细信息。

```
GET /teams/members
```

#### 响应

返回一个团队成员对象的数组：

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: '拥有者' | '成员' | '免费拥有者';
  }[];
}
```

<div id="example-responses">
  #### 示例回复
</div>

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "成员"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "拥有者"
    }
  ]
}

```

<div id="example-requests">
  #### 示例请求
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u 你的API密钥：
```

<div id="get-daily-usage-data">
  ### 获取每日用量数据
</div>

在指定日期范围内获取你团队的每日用量指标，了解代码编辑、AI 协作使用情况与接受率等详细洞察。

```
POST /teams/daily-usage-data
```

#### 请求体

<div className="full-width-table">
  | 参数          | 类型     | 必填 | 描述             |
  | :---------- | :----- | :- | :------------- |
  | `startDate` | number | 是  | 起始日期（Epoch 毫秒） |
  | `endDate`   | number | 是  | 结束日期（Epoch 毫秒） |
</div>

<Note>
  日期范围不能超过 90 天。更长的时间段请分多次发起请求。
</Note>

#### 返回

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
  #### 响应字段
</div>

<div className="full-width-table">
  | 字段                         | 描述                |
  | :------------------------- | :---------------- |
  | `date`                     | 以 epoch 毫秒表示的日期   |
  | `isActive`                 | 该日用户是否活跃          |
  | `totalLinesAdded`          | 新增代码行数            |
  | `totalLinesDeleted`        | 删除代码行数            |
  | `acceptedLinesAdded`       | 来自已接受 AI 建议的新增行数  |
  | `acceptedLinesDeleted`     | 来自已接受 AI 建议的删除行数  |
  | `totalApplies`             | Apply 操作次数        |
  | `totalAccepts`             | 接受的建议数            |
  | `totalRejects`             | 拒绝的建议数            |
  | `totalTabsShown`           | 显示的 Tab 补全次数      |
  | `totalTabsAccepted`        | 接受的 Tab 补全次数      |
  | `composerRequests`         | Composer 请求数      |
  | `chatRequests`             | Chat 请求数          |
  | `agentRequests`            | Agent 请求数         |
  | `cmdkUsages`               | 命令面板（Cmd+K）使用次数   |
  | `subscriptionIncludedReqs` | 订阅内请求数            |
  | `apiKeyReqs`               | API Key 请求数       |
  | `usageBasedReqs`           | 按用量计费请求数          |
  | `bugbotUsages`             | Bug 检测使用次数        |
  | `mostUsedModel`            | 最常用的 AI 模型        |
  | `applyMostUsedExtension`   | Apply 使用最频繁的文件扩展名 |
  | `tabMostUsedExtension`     | Tab 使用最频繁的文件扩展名   |
  | `clientVersion`            | Cursor 版本         |
  | `email`                    | 用户邮箱              |
</div>

<div id="example-responses">
  #### 示例回复
</div>

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

<div id="example-requests">
  #### 示例请求
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u 你的_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### 获取支出数据
</div>

支持通过搜索、排序和分页检索本日历月的支出信息。

```
POST /teams/spend
```

#### 请求体

<div className="full-width-table">
  | 参数              | 类型     | 必填 | 描述                                     |
  | :-------------- | :----- | :- | :------------------------------------- |
  | `searchTerm`    | string | 否  | 在用户名和邮箱中搜索                             |
  | `sortBy`        | string | 否  | 排序字段：`amount`、`date`、`user`。默认值：`date` |
  | `sortDirection` | string | 否  | 排序方向：`asc`、`desc`。默认值：`desc`           |
  | `page`          | number | 否  | 页码（从 1 开始）。默认值：`1`                     |
  | `pageSize`      | number | 否  | 每页结果数                                  |
</div>

#### 返回

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
  #### 响应字段
</div>

<div className="full-width-table">
  | 字段                         | 描述                 |
  | :------------------------- | :----------------- |
  | `spendCents`               | 总花费（单位：美分）         |
  | `fastPremiumRequests`      | Fast 高级模型请求数       |
  | `name`                     | 成员名称               |
  | `email`                    | 成员邮箱               |
  | `role`                     | 团队角色               |
  | `hardLimitOverrideDollars` | 自定义支出上限（美元）        |
  | `subscriptionCycleStart`   | 订阅周期起始时间（Epoch 毫秒） |
  | `totalMembers`             | 团队成员总数             |
  | `totalPages`               | 总页数                |
</div>

<div id="example-responses">
  #### 示例回复
</div>

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "member",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "owner",
      "hardLimitOverrideDollars": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

<div id="example-requests">
  #### 示例请求
</div>

**基础消费数据：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**分页搜索指定用户：**

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
  ### 获取使用事件数据
</div>

通过完整的筛选、搜索和分页选项，为你的团队获取详细的使用事件数据。这个端点提供关于单次 API 调用、模型使用、令牌（token）消耗和成本的细粒度洞察。

```
POST /teams/filtered-usage-events
```

#### 请求体

<div className="full-width-table">
  | 参数          | 类型     | 必填 | 描述                 |
  | :---------- | :----- | :- | :----------------- |
  | `startDate` | number | 否  | 起始日期（epoch 毫秒）     |
  | `endDate`   | number | 否  | 结束日期（epoch 毫秒）     |
  | `userId`    | number | 否  | 按指定用户 ID 过滤        |
  | `page`      | number | 否  | 页码（从 1 开始）。默认值：`1` |
  | `pageSize`  | number | 否  | 每页返回数量。默认值：`10`    |
  | `email`     | string | 否  | 按用户邮箱地址过滤          |
</div>

#### 返回

```typescript  theme={null}
{
  totalUsageEventsCount: number; // 使用事件总数
  pagination: {
    numPages: number; // 总页数
    currentPage: number; // 当前页
    pageSize: number; // 每页大小
    hasNextPage: boolean; // 是否有下一页
    hasPreviousPage: boolean; // 是否有上一页
  };
  usageEvents: {
    timestamp: string; // 时间戳
    model: string; // 模型
    kind: string; // 类型
    maxMode: boolean; // 是否为最大模式
    requestsCosts: number; // 请求成本
    isTokenBasedCall: boolean; // 是否为按 Token 计费调用
    tokenUsage?: {
      inputTokens: number; // 输入 Token
      outputTokens: number; // 输出 Token
      cacheWriteTokens: number; // 缓存写入 Token
      cacheReadTokens: number; // 缓存读取 Token
      totalCents: number; // 总费用（美分）
    };
    isFreeBugbot: boolean; // 是否为免费 Bugbot
    userEmail: string; // 用户邮箱
  }[];
  period: {
    startDate: number; // 开始日期（时间戳）
    endDate: number; // 结束日期（时间戳）
  };
}
```

<div id="response-fields-explained">
  #### 响应字段说明
</div>

<div className="full-width-table">
  | 字段                      | 说明                                    |
  | :---------------------- | :------------------------------------ |
  | `totalUsageEventsCount` | 与查询匹配的使用事件总数                          |
  | `pagination`            | 用于浏览结果的分页元数据                          |
  | `timestamp`             | 事件时间戳（自纪元起的毫秒数）                       |
  | `model`                 | 此请求使用的 AI 模型                          |
  | `kind`                  | 使用类别（例如，“按用量计费”、“商用版包含”）              |
  | `maxMode`               | 是否启用了 Max 模式                          |
  | `requestsCosts`         | 按请求计量单位计算的成本                          |
  | `isTokenBasedCall`      | 当事件按令牌用量计费时为 true                     |
  | `tokenUsage`            | 令牌用量明细（当 isTokenBasedCall 为 true 时可用） |
  | `isFreeBugbot`          | 是否为免费 Bugbot 使用                       |
  | `userEmail`             | 发起请求的用户邮箱                             |
  | `period`                | 查询数据的日期范围                             |
</div>

<div id="example-responses">
  #### 示例回复
</div>

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
      "kind": "按用量计费",
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
      "kind": "Usage-based",
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
      "kind": "包含在商务版中"
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
  #### 示例请求
</div>

**使用默认分页获取所有使用事件：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**按日期范围和指定用户筛选：**

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

**获取特定用户的使用事件（支持自定义分页）：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### 设置用户花费上限
</div>

为各个团队成员设置花费上限。这样就能控制每个用户在团队内使用 AI 的花费额度。

```
POST /teams/user-spend-limit
```

<Note>
  **速率限制：** 每个团队每分钟最多 60 次请求
</Note>

#### 请求体

<div className="full-width-table">
  | 参数                  | 类型     | 必填 | 说明                    |
  | :------------------ | :----- | :- | :-------------------- |
  | `userEmail`         | string | 是  | 团队成员的邮箱地址             |
  | `spendLimitDollars` | number | 是  | 以美元计的花费上限（仅限整数，不含小数）。 |
</div>

<Note>
  * 该用户必须已是你团队的成员
  * 只接受整数值（不含小数金额）
  * 将 `spendLimitDollars` 设为 0 会把上限设为 \$0
</Note>

#### 响应

返回一个标准化的响应，用于指示成功或失败：

```typescript  theme={null}
{
  outcome: 'success' | 'error';
  message: string;
}
```

<div id="example-responses">
  #### 示例回复
</div>

**已成功设置限制：**

```json  theme={null}
{
  "outcome": "success",
  "message": "已将用户 developer@company.com 的支出上限设为 $100"
}
```

**错误响应：**

```json  theme={null}
{
  "outcome": "error",
  "message": "邮箱格式无效"
}
```

<div id="example-requests">
  #### 示例请求
</div>

**设置消费上限：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### Repo Blocklists API
</div>

添加仓库并使用匹配规则，防止文件或目录被索引，或被用作你团队的上下文。

<div id="get-team-repo-blocklists">
  #### 获取团队仓库黑名单
</div>

检索你团队配置的所有仓库黑名单。

```
GET /settings/repo-blocklists/repos
```

<div id="response">
  ##### 响应
</div>

返回一个仓库封禁列表对象的数组：

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-response">
  ##### 示例回复
</div>

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
  ##### 示例请求
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u 你的_API_KEY:
```

<div id="upsert-repo-blocklists">
  #### 覆盖更新 Repo 阻止列表
</div>

为提供的仓库替换其现有的阻止列表。
*注意：此端点只会覆盖所提供仓库的匹配模式，其他仓库不受影响。*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### 请求体
</div>

| 参数    | 类型    | 必填 | 说明         |
| ----- | ----- | -- | ---------- |
| repos | array | 是  | 仓库阻止列表对象数组 |

每个仓库对象必须包含：

| 字段       | 类型        | 必填 | 说明                      |
| -------- | --------- | -- | ----------------------- |
| url      | string    | 是  | 要加入阻止列表的仓库 URL          |
| patterns | string\[] | 是  | 要阻止的文件模式数组（支持 glob 通配符） |

<div id="response">
  ##### 响应
</div>

返回更新后的仓库封锁列表：

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
  ##### 示例请求
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
  #### 删除仓库封锁列表
</div>

从封锁列表中移除指定仓库。

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### 参数
</div>

| 参数     | 类型     | 必填 | 描述            |
| ------ | ------ | -- | ------------- |
| repoId | string | 是  | 要删除的仓库黑名单的 ID |

<div id="response">
  ##### 响应
</div>

删除成功时返回 204 No Content。

<div id="example-request">
  ##### 示例请求
</div>

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u 你的_API_KEY:
```

<div id="pattern-examples">
  #### 模式示例
</div>

常见的 blocklist 模式：

* `*` - 屏蔽整个仓库
* `*.env` - 屏蔽所有 .env 文件
* `config/*` - 屏蔽 config 目录中的所有文件
* `**/*.secret` - 屏蔽任意子目录中的所有 .secret 文件
* `src/api/keys.ts` - 屏蔽指定文件

---

← Previous: [定价](./section.md) | [Index](./index.md) | Next: [AI Code Tracking API](./ai-code-tracking-api.md) →