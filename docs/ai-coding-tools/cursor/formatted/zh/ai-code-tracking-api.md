---
title: "AI Code Tracking API"
source: "https://docs.cursor.com/zh/account/teams/ai-code-tracking-api"
language: "zh"
language_name: "Chinese"
---

# AI Code Tracking API
Source: https://docs.cursor.com/zh/account/teams/ai-code-tracking-api

获取你团队代码库的 AI 生成代码分析

获取你团队代码库的 AI 生成代码分析。支持按提交查看 AI 使用情况，以及精细到变更级别的已接受 AI 修改。

<Note>
  该 API 为首个发布版本。我们会根据反馈持续扩展能力——告诉我们你需要哪些接口！
</Note>

* **Availability**: 仅限企业团队
* **Status**: Alpha（响应结构和字段可能变动）

<div id="authentication">
  ## 身份验证
</div>

所有 API 请求都需要使用 API 密钥进行身份验证。该 API 使用与其他端点相同的 Admin API 身份验证方式。

想了解更详细的身份验证说明，去看 [Admin API 身份验证](/zh/account/teams/admin-api#authentication)。

<div id="base-url">
  ## 基础 URL
</div>

所有 API 端点均使用：

```
https://api.cursor.com
```

<div id="rate-limits">
  ## 速率限制
</div>

* 每个团队在每个端点上每分钟最多 5 次请求

<div id="query-parameters">
  ## 查询参数
</div>

以下所有端点都通过查询字符串接受相同的查询参数：

<div className="full-width-table">
  | 参数          | 类型     | 是否必填 | 描述                                                                                                               |                                                              |
  | :---------- | :----- | :--- | :--------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
  | `startDate` | string | date | 否                                                                                                                | ISO 日期字符串、字面量 "now"，或相对天数（例如 "7d"，表示 now - 7 天）。默认：now - 7 天 |
  | `endDate`   | string | date | 否                                                                                                                | ISO 日期字符串、字面量 "now"，或相对天数（例如 "0d"）。默认：now                    |
  | `page`      | number | 否    | 页码（从 1 开始）。默认：1                                                                                                  |                                                              |
  | `pageSize`  | number | 否    | 每页结果数。默认：100，最大：1000                                                                                             |                                                              |
  | `user`      | string | 否    | 可选的单用户过滤。可填写邮箱（例如 [developer@company.com](mailto:developer@company.com)）、编码 ID（例如 user\_abc123...），或数值 ID（例如 42） |                                                              |
</div>

<Note>
  响应中的 userId 会以带有前缀 user\_ 的外部编码 ID 返回，供 API 稳定使用。
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## 语义与指标的计算方式
</div>

* **Sources**："TAB" 表示接受的内联补全；"COMPOSER" 表示来自 Composer 的已接受差异（diff）
* **Lines metrics**：tabLinesAdded/Deleted 和 composerLinesAdded/Deleted 分别统计；nonAiLinesAdded/Deleted 计算为 max(0, totalLines - AI lines)
* **Privacy mode**：如果在客户端启用，某些元数据（例如 fileName）可能会被省略
* **Branch info**：当当前分支等于仓库的默认分支时，isPrimaryBranch 为 true；如果仓库信息不可用，可能为 undefined

你可以查看该文件，了解如何检测并上报提交与变更。

<div id="endpoints">
  ## 端点
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### 获取 AI 提交指标（JSON，分页）
</div>

获取按提交聚合的指标，将代码行归因于 TAB、COMPOSER 和非 AI。

```
GET /analytics/ai-code/commits
```

<div id="response">
  #### 返回
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
  #### AiCommitMetric 字段
</div>

<div className="full-width-table">
  | 字段                     | 类型      | 描述                         |               |
  | :--------------------- | :------ | :------------------------- | ------------- |
  | `commitHash`           | string  | Git 提交哈希                   |               |
  | `userId`               | string  | 编码后的用户 ID（例如：user\_abc123） |               |
  | `userEmail`            | string  | 用户邮箱地址                     |               |
  | `repoName`             | string  | null                       | 仓库名称          |
  | `branchName`           | string  | null                       | 分支名称          |
  | `isPrimaryBranch`      | boolean | null                       | 是否为主分支        |
  | `totalLinesAdded`      | number  | 提交中新增加的总行数                 |               |
  | `totalLinesDeleted`    | number  | 提交中删除的总行数                  |               |
  | `tabLinesAdded`        | number  | 通过 Tab 补全新增的行数             |               |
  | `tabLinesDeleted`      | number  | 通过 Tab 补全删除的行数             |               |
  | `composerLinesAdded`   | number  | 通过 Composer 新增的行数          |               |
  | `composerLinesDeleted` | number  | 通过 Composer 删除的行数          |               |
  | `nonAiLinesAdded`      | number  | null                       | 非 AI 新增的行数    |
  | `nonAiLinesDeleted`    | number  | null                       | 非 AI 删除的行数    |
  | `message`              | string  | null                       | 提交说明          |
  | `commitTs`             | string  | null                       | 提交时间戳（ISO 格式） |
  | `createdAt`            | string  | 写入时间戳（ISO 格式）              |               |
</div>

<div id="example-response">
  #### 示例响应
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
      "message": "重构：提取 analytics 客户端"
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
  #### 示例请求
</div>

**基本请求：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u 你的_API_KEY:
```

**按用户（邮箱）筛选：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u 你的API密钥：
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### 下载 AI Commit 指标（CSV，流式）
</div>

以 CSV 格式下载提交指标数据，适用于大批量数据导出。

```
GET /analytics/ai-code/commits.csv
```

#### 响应

请求头：

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV 列
</div>

<div className="full-width-table">
  | 列                        | 类型      | 描述                |
  | :----------------------- | :------ | :---------------- |
  | `commit_hash`            | string  | Git 提交哈希值         |
  | `user_id`                | string  | 编码后的用户 ID         |
  | `user_email`             | string  | 用户邮箱地址            |
  | `repo_name`              | string  | 仓库名称              |
  | `branch_name`            | string  | 分支名称              |
  | `is_primary_branch`      | boolean | 是否为主分支            |
  | `total_lines_added`      | number  | 此次提交新增的总行数        |
  | `total_lines_deleted`    | number  | 此次提交删除的总行数        |
  | `tab_lines_added`        | number  | 通过 Tab 补全新增的行数    |
  | `tab_lines_deleted`      | number  | 通过 Tab 补全删除的行数    |
  | `composer_lines_added`   | number  | 通过 Composer 新增的行数 |
  | `composer_lines_deleted` | number  | 通过 Composer 删除的行数 |
  | `non_ai_lines_added`     | number  | 非 AI 新增的行数        |
  | `non_ai_lines_deleted`   | number  | 非 AI 删除的行数        |
  | `message`                | string  | 提交消息              |
  | `commit_ts`              | string  | 提交时间戳（ISO 格式）     |
  | `created_at`             | string  | 导入时间戳（ISO 格式）     |
</div>

<div id="sample-csv-output">
  #### 示例 CSV 输出
</div>

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"重构：抽取 Analytics 客户端",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"添加错误处理",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-requests">
  #### 示例请求
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u 你的 API 密钥: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### 获取 AI 代码变更指标（JSON，分页）
</div>

检索按确定性 changeId 分组的细粒度已接受 AI 变更。可用于在不依赖提交的情况下分析已接受的 AI 事件。

```
GET /analytics/ai-code/changes
```

<div id="response">
  #### 返回
</div>

```typescript  theme={null}
{
  items: AiCodeChangeMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### AiCodeChangeMetric 字段
</div>

<div className="full-width-table">
  | 字段                  | 类型     | 描述                         |          |
  | :------------------ | :----- | :------------------------- | -------- |
  | `changeId`          | string | 更改的确定性 ID                  |          |
  | `userId`            | string | 编码后的用户 ID（例如：user\_abc123） |          |
  | `userEmail`         | string | 用户邮箱地址                     |          |
  | `source`            | "TAB"  | "COMPOSER"                 | AI 更改来源  |
  | `model`             | string | null                       | 所用 AI 模型 |
  | `totalLinesAdded`   | number | 新增总行数                      |          |
  | `totalLinesDeleted` | number | 删除总行数                      |          |
  | `createdAt`         | string | 写入时间戳（ISO 格式）              |          |
  | `metadata`          | Array  | 文件元数据（隐私模式下 fileName 可能省略） |          |
</div>

<div id="example-response">
  #### 示例响应
</div>

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "Composer",
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
  #### 示例请求
</div>

**基本请求：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u 你的_API_KEY:
```

**按用户（编码后的 ID）筛选：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u YOUR_API_KEY:
```

**按用户（邮箱）筛选：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u YOUR_API_KEY:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### 下载 AI 代码变更指标（CSV，流式）
</div>

以 CSV 格式下载变更指标数据，适用于大规模数据抽取。

```
GET /analytics/ai-code/changes.csv
```

#### 响应

Headers:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV 列
</div>

<div className="full-width-table">
  | 列                     | 类型     | 描述                      |
  | :-------------------- | :----- | :---------------------- |
  | `change_id`           | string | 该变更的确定性 ID              |
  | `user_id`             | string | 编码后的用户 ID               |
  | `user_email`          | string | 用户的电子邮箱地址               |
  | `source`              | string | AI 变更来源（TAB 或 COMPOSER） |
  | `model`               | string | 使用的 AI 模型               |
  | `total_lines_added`   | number | 新增行总数                   |
  | `total_lines_deleted` | number | 删除行总数                   |
  | `created_at`          | string | 摄取时间戳（ISO 格式）           |
  | `metadata_json`       | string | JSON 字符串化的元数据条目数组       |
</div>

<div id="notes">
  #### 备注
</div>

* metadata\_json 是 JSON 字符串化的元数据条目数组（隐私模式下可能省略 fileName）
* 处理 CSV 时，务必解析带引号的字段

<div id="sample-csv-output">
  #### 示例 CSV 输出
</div>

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-requests">
  #### 示例请求
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u YOUR_API_KEY: \
  -o changes.csv
```

<div id="tips">
  ## 提示
</div>

* 使用 `user` 参数可在所有端点中快速筛选单个用户
* 对于大规模数据抽取，优先使用 CSV 端点——它们会在服务器端以每页 10,000 条记录的方式进行流式传输
* 如果客户端无法解析默认分支，`isPrimaryBranch` 可能为 undefined
* `commitTs` 是提交时间戳；`createdAt` 是我们服务器上的摄取时间
* 当客户端启用隐私模式时，某些字段可能不会返回

<div id="changelog">
  ## 更新日志
</div>

* **Alpha 版本发布**：提供用于提交（commits）和变更（changes）的初始端点（endpoints）。响应结构可能会根据反馈而调整

---

← Previous: [Admin API](./admin-api.md) | [Index](./index.md) | Next: [Analytics](./analytics.md) →