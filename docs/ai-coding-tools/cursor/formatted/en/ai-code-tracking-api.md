---
title: "AI Code Tracking API"
source: "https://docs.cursor.com/en/account/teams/ai-code-tracking-api"
language: "en"
language_name: "English"
---

# AI Code Tracking API
Source: https://docs.cursor.com/en/account/teams/ai-code-tracking-api

Access AI-generated code analytics for your team's repositories

Access AI-generated code analytics for your team's repositories. This includes per-commit AI usage as well as granular accepted AI changes.

<Note>
  The API is in its first release. We're expanding capabilities based on feedback - let us know what endpoints you need!
</Note>

* **Availability**: Only for enterprise teams
* **Status**: Alpha (response shapes and fields may change)

## Authentication

All API requests require authentication using an API key. This API uses the same Admin API authentication as other endpoints.

For detailed authentication instructions, see [Admin API authentication](/en/account/teams/admin-api#authentication).

## Base URL

All API endpoints use:

```
https://api.cursor.com
```

## Rate Limits

* 5 requests per minute per team, per endpoint

## Query Parameters

All endpoints below accept the same query parameters via query string:

<div className="full-width-table">
  | Parameter   | Type           | Required | Description                                                                                                                                                                 |
  | :---------- | :------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `startDate` | string \| date | No       | ISO date string, the literal "now", or relative days like "7d" (means now - 7 days). Default: now - 7 days                                                                  |
  | `endDate`   | string \| date | No       | ISO date string, the literal "now", or relative days like "0d". Default: now                                                                                                |
  | `page`      | number         | No       | Page number (1-based). Default: 1                                                                                                                                           |
  | `pageSize`  | number         | No       | Results per page. Default: 100, Max: 1000                                                                                                                                   |
  | `user`      | string         | No       | Optional filter by a single user. Accepts email (e.g., [developer@company.com](mailto:developer@company.com)), encoded ID (e.g., user\_abc123...), or numeric ID (e.g., 42) |
</div>

<Note>
  Responses return userId as an encoded external ID with the prefix user\_. This is stable for API consumption.
</Note>

## Semantics and How Metrics Are Computed

* **Sources**: "TAB" represents inline completions that were accepted; "COMPOSER" represents accepted diffs from Composer
* **Lines metrics**: tabLinesAdded/Deleted and composerLinesAdded/Deleted are separately counted; nonAiLinesAdded/Deleted are derived as max(0, totalLines - AI lines)
* **Privacy mode**: If enabled in the client, some metadata (like fileName) may be omitted
* **Branch info**: isPrimaryBranch is true when the current branch equals the repo's default branch; may be undefined if repo info is unavailable

You can scan that file to understand how commits and changes are detected and reported.

## Endpoints

### Get AI Commit Metrics (JSON, paginated)

Retrieve aggregated per-commit metrics that attribute lines to TAB, COMPOSER, and non-AI.

```
GET /analytics/ai-code/commits
```

#### Response

```typescript  theme={null}
{
  items: AiCommitMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

#### AiCommitMetric Fields

<div className="full-width-table">
  | Field                  | Type            | Description                          |
  | :--------------------- | :-------------- | :----------------------------------- |
  | `commitHash`           | string          | Git commit hash                      |
  | `userId`               | string          | Encoded user ID (e.g., user\_abc123) |
  | `userEmail`            | string          | User's email address                 |
  | `repoName`             | string \| null  | Repository name                      |
  | `branchName`           | string \| null  | Branch name                          |
  | `isPrimaryBranch`      | boolean \| null | Whether this is the primary branch   |
  | `totalLinesAdded`      | number          | Total lines added in commit          |
  | `totalLinesDeleted`    | number          | Total lines deleted in commit        |
  | `tabLinesAdded`        | number          | Lines added via TAB completions      |
  | `tabLinesDeleted`      | number          | Lines deleted via TAB completions    |
  | `composerLinesAdded`   | number          | Lines added via Composer             |
  | `composerLinesDeleted` | number          | Lines deleted via Composer           |
  | `nonAiLinesAdded`      | number \| null  | Non-AI lines added                   |
  | `nonAiLinesDeleted`    | number \| null  | Non-AI lines deleted                 |
  | `message`              | string \| null  | Commit message                       |
  | `commitTs`             | string \| null  | Commit timestamp (ISO format)        |
  | `createdAt`            | string          | Ingestion timestamp (ISO format)     |
</div>

#### Example Response

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
      "message": "Refactor: extract analytics client",
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

#### Example Requests

**Basic request:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u YOUR_API_KEY:
```

**Filter by user (email):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u YOUR_API_KEY:
```

### Download AI Commit Metrics (CSV, streaming)

Download commit metrics data in CSV format for large data extractions.

```
GET /analytics/ai-code/commits.csv
```

#### Response

Headers:

* Content-Type: text/csv; charset=utf-8

#### CSV Columns

<div className="full-width-table">
  | Column                   | Type    | Description                        |
  | :----------------------- | :------ | :--------------------------------- |
  | `commit_hash`            | string  | Git commit hash                    |
  | `user_id`                | string  | Encoded user ID                    |
  | `user_email`             | string  | User's email address               |
  | `repo_name`              | string  | Repository name                    |
  | `branch_name`            | string  | Branch name                        |
  | `is_primary_branch`      | boolean | Whether this is the primary branch |
  | `total_lines_added`      | number  | Total lines added in commit        |
  | `total_lines_deleted`    | number  | Total lines deleted in commit      |
  | `tab_lines_added`        | number  | Lines added via TAB completions    |
  | `tab_lines_deleted`      | number  | Lines deleted via TAB completions  |
  | `composer_lines_added`   | number  | Lines added via Composer           |
  | `composer_lines_deleted` | number  | Lines deleted via Composer         |
  | `non_ai_lines_added`     | number  | Non-AI lines added                 |
  | `non_ai_lines_deleted`   | number  | Non-AI lines deleted               |
  | `message`                | string  | Commit message                     |
  | `commit_ts`              | string  | Commit timestamp (ISO format)      |
  | `created_at`             | string  | Ingestion timestamp (ISO format)   |
</div>

#### Sample CSV Output

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"Refactor: extract analytics client",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"Add error handling",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

#### Example Request

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u YOUR_API_KEY: \
  -o commits.csv
```

### Get AI Code Change Metrics (JSON, paginated)

Retrieve granular accepted AI changes, grouped by deterministic changeId. Useful to analyze accepted AI events independent of commits.

```
GET /analytics/ai-code/changes
```

#### Response

```typescript  theme={null}
{
  items: AiCodeChangeMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

#### AiCodeChangeMetric Fields

<div className="full-width-table">
  | Field               | Type                | Description                                             |
  | :------------------ | :------------------ | :------------------------------------------------------ |
  | `changeId`          | string              | Deterministic ID for the change                         |
  | `userId`            | string              | Encoded user ID (e.g., user\_abc123)                    |
  | `userEmail`         | string              | User's email address                                    |
  | `source`            | "TAB" \| "COMPOSER" | Source of the AI change                                 |
  | `model`             | string \| null      | AI model used                                           |
  | `totalLinesAdded`   | number              | Total lines added                                       |
  | `totalLinesDeleted` | number              | Total lines deleted                                     |
  | `createdAt`         | string              | Ingestion timestamp (ISO format)                        |
  | `metadata`          | Array               | File metadata (fileName may be omitted in privacy mode) |
</div>

#### Example Response

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

#### Example Requests

**Basic request:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u YOUR_API_KEY:
```

**Filter by user (encoded ID):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u YOUR_API_KEY:
```

**Filter by user (email):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u YOUR_API_KEY:
```

### Download AI Code Change Metrics (CSV, streaming)

Download change metrics data in CSV format for large data extractions.

```
GET /analytics/ai-code/changes.csv
```

#### Response

Headers:

* Content-Type: text/csv; charset=utf-8

#### CSV Columns

<div className="full-width-table">
  | Column                | Type   | Description                                |
  | :-------------------- | :----- | :----------------------------------------- |
  | `change_id`           | string | Deterministic ID for the change            |
  | `user_id`             | string | Encoded user ID                            |
  | `user_email`          | string | User's email address                       |
  | `source`              | string | Source of the AI change (TAB or COMPOSER)  |
  | `model`               | string | AI model used                              |
  | `total_lines_added`   | number | Total lines added                          |
  | `total_lines_deleted` | number | Total lines deleted                        |
  | `created_at`          | string | Ingestion timestamp (ISO format)           |
  | `metadata_json`       | string | JSON stringified array of metadata entries |
</div>

#### Notes

* metadata\_json is a JSON stringified array of metadata entries (may omit fileName under privacy mode)
* When consuming CSV, be sure to parse quoted fields

#### Sample CSV Output

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

#### Example Request

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u YOUR_API_KEY: \
  -o changes.csv
```

## Tips

* Use `user` parameter to quickly filter a single user across all endpoints
* For large data extractions, prefer CSV endpoints—they stream in pages of 10,000 records server-side
* `isPrimaryBranch` may be undefined if the client couldn't resolve the default branch
* `commitTs` is the commit timestamp; `createdAt` is the ingestion time on our servers
* Some fields may be absent when privacy mode is enabled on the client

## Changelog

* **Alpha release**: Initial endpoints for commits and changes. Response shapes may evolve based on feedback

---

← Previous: [Admin API](./admin-api.md) | [Index](./index.md) | Next: [Analytics](./analytics.md) →