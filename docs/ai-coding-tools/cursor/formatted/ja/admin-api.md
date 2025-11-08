---
title: "Admin API"
source: "https://docs.cursor.com/ja/account/teams/admin-api"
language: "ja"
language_name: "Japanese"
---

# Admin API
Source: https://docs.cursor.com/ja/account/teams/admin-api

API 経由でチームのメトリクス、利用データ、支出情報にアクセス

Admin API は、メンバー情報、利用メトリクス、支出の詳細など、チームのデータへプログラムからアクセスできる。カスタムダッシュボードや監視ツールを作成したり、既存のワークフローに統合したりできる。

<Note>
  この API は初回リリース。フィードバックに基づいて機能を拡張中—必要なエンドポイントを教えてね！
</Note>

<div id="authentication">
  ## 認証
</div>

すべての API リクエストには API キーによる認証が必要。API キーの作成と管理ができるのはチーム管理者のみ。

API キーは組織に紐づき、すべての管理者が閲覧でき、作成者本人のアカウント状況の影響は受けない。

<div id="creating-an-api-key">
  ### APIキーの作成
</div>

1. **cursor.com/dashboard** → **Settings** タブ → **Cursor Admin API Keys** に移動
2. **Create New API Key** をクリック
3. キーにわかりやすい名前を付ける（例：「Usage Dashboard Integration」）
4. 生成されたキーはその場でコピーしておく—あとからは確認できない

形式: `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### APIキーの使用
</div>

基本認証では、ユーザー名にAPIキーを指定する:

**Basic認証を使った curl の例:**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**または Authorization ヘッダーを直接指定する:**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## ベースURL
</div>

すべてのAPIエンドポイントは次を使用する：

```
https://api.cursor.com
```

<div id="endpoints">
  ## エンドポイント
</div>

<div id="get-team-members">
  ### チームメンバーの取得
</div>

すべてのチームメンバーとその詳細を取得する。

```
GET /teams/members
```

#### レスポンス

チームメンバーオブジェクトの配列を返す：

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: 'オーナー' | 'メンバー' | 'フリー・オーナー';
  }[];
}
```

#### 応答例

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "メンバー"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "オーナー"
    }
  ]
}

```

#### 例: リクエスト

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u YOUR_API_KEY:
```

<div id="get-daily-usage-data">
  ### 日次利用データを取得
</div>

指定した日付範囲でチームの詳細な日次利用メトリクスを取得。コード編集、AI支援の利用状況、受け入れ率に関するインサイトを提供するよ。

```
POST /teams/daily-usage-data
```

#### リクエストボディ

<div className="full-width-table">
  | パラメーター      | 型      | 必須  | 説明           |
  | :---------- | :----- | :-- | :----------- |
  | `startDate` | number | Yes | エポックミリ秒の開始日時 |
  | `endDate`   | number | Yes | エポックミリ秒の終了日時 |
</div>

<Note>
  日付範囲は90日を超えない。より長い期間は複数回に分けてリクエストしてね。
</Note>

#### 応答

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
  #### レスポンスフィールド
</div>

<div className="full-width-table">
  | フィールド                      | 説明                   |
  | :------------------------- | :------------------- |
  | `date`                     | エポックミリ秒の日時           |
  | `isActive`                 | 当日のユーザーアクティブ状態       |
  | `totalLinesAdded`          | 追加されたコード行数           |
  | `totalLinesDeleted`        | 削除されたコード行数           |
  | `acceptedLinesAdded`       | 承認されたAI提案による追加行数     |
  | `acceptedLinesDeleted`     | 承認されたAI提案による削除行数     |
  | `totalApplies`             | Applyの実行回数           |
  | `totalAccepts`             | 承認された提案数             |
  | `totalRejects`             | 却下された提案数             |
  | `totalTabsShown`           | 表示されたタブ補完数           |
  | `totalTabsAccepted`        | 承認されたタブ補完数           |
  | `composerRequests`         | Composerリクエスト数       |
  | `chatRequests`             | Chatリクエスト数           |
  | `agentRequests`            | Agentリクエスト数          |
  | `cmdkUsages`               | コマンドパレット（Cmd+K）の使用回数 |
  | `subscriptionIncludedReqs` | サブスクリプション対象のリクエスト数   |
  | `apiKeyReqs`               | APIキー経由のリクエスト数       |
  | `usageBasedReqs`           | 従量課金リクエスト数           |
  | `bugbotUsages`             | バグ検出機能の使用回数          |
  | `mostUsedModel`            | 最も頻繁に使用されたAIモデル      |
  | `applyMostUsedExtension`   | Applyで最も使用されたファイル拡張子 |
  | `tabMostUsedExtension`     | タブで最も使用されたファイル拡張子    |
  | `clientVersion`            | Cursorのバージョン         |
  | `email`                    | ユーザーのメールアドレス         |
</div>

#### 例のレスポンス

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

#### リクエストの例

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
  ### 支出データを取得
</div>

検索、ソート、ページネーションに対応し、当月（暦月）の支出情報を取得する。

```
POST /teams/spend
```

#### リクエストボディ

<div className="full-width-table">
  | パラメータ           | 型      | 必須  | 説明                                           |
  | :-------------- | :----- | :-- | :------------------------------------------- |
  | `searchTerm`    | string | いいえ | ユーザー名とメールアドレス内を検索                            |
  | `sortBy`        | string | いいえ | 並び替え基準: `amount`, `date`, `user`。既定値: `date` |
  | `sortDirection` | string | いいえ | 並び順: `asc`, `desc`。既定値: `desc`               |
  | `page`          | number | いいえ | ページ番号（1始まり）。既定値: `1`                         |
  | `pageSize`      | number | いいえ | 1ページあたりの件数                                   |
</div>

#### レスポンス

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
  #### レスポンスフィールド
</div>

<div className="full-width-table">
  | フィールド                      | 説明                         |
  | :------------------------- | :------------------------- |
  | `spendCents`               | 合計支出（セント）                  |
  | `fastPremiumRequests`      | Fast プレミアムモデルのリクエスト数       |
  | `name`                     | メンバー名                      |
  | `email`                    | メンバーのメールアドレス               |
  | `role`                     | チーム内ロール                    |
  | `hardLimitOverrideDollars` | カスタム支出上限の上書き（ドル）           |
  | `subscriptionCycleStart`   | サブスクリプションサイクル開始時刻（エポックミリ秒） |
  | `totalMembers`             | チームメンバー総数                  |
  | `totalPages`               | 総ページ数                      |
</div>

#### 応答例

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "メンバー",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "オーナー"
      "hardLimitOverrideDollars": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

<div id="example-requests">
  #### リクエスト例
</div>

**基本的な支出データ：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**ページネーション付きで特定のユーザーを検索する:**

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
  ### 使用イベントデータの取得
</div>

チームの使用イベントを、柔軟なフィルタリング、検索、ページネーションで詳細に取得できる。このエンドポイントは、個々の API 呼び出し、モデルの利用状況、トークン消費量、コストに関するきめ細かなインサイトを提供する。

```
POST /teams/filtered-usage-events
```

#### リクエストボディ

<div className="full-width-table">
  | パラメータ       | 型      | 必須  | 説明                    |
  | :---------- | :----- | :-- | :-------------------- |
  | `startDate` | number | いいえ | エポックミリ秒の開始日時          |
  | `endDate`   | number | いいえ | エポックミリ秒の終了日時          |
  | `userId`    | number | いいえ | 特定のユーザーIDでフィルタリング     |
  | `page`      | number | いいえ | ページ番号（1始まり）。既定値: `1`  |
  | `pageSize`  | number | いいえ | 1ページあたりの結果数。既定値: `10` |
  | `email`     | string | いいえ | ユーザーのメールアドレスでフィルタリング  |
</div>

#### 応答

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
  #### レスポンスフィールドの説明
</div>

<div className="full-width-table">
  | フィールド                   | 説明                                             |
  | :---------------------- | :--------------------------------------------- |
  | `totalUsageEventsCount` | クエリに一致する利用イベントの総数                              |
  | `pagination`            | 結果を移動するためのページネーション用メタデータ                       |
  | `timestamp`             | イベントのエポックミリ秒でのタイムスタンプ                          |
  | `model`                 | リクエストで使用された AI モデル                             |
  | `kind`                  | 利用区分（例: "Usage-based", "Included in Business"） |
  | `maxMode`               | Max Mode が有効だったかどうか                            |
  | `requestsCosts`         | リクエスト単位のコスト                                    |
  | `isTokenBasedCall`      | イベントが従量課金として計上される場合は true                      |
  | `tokenUsage`            | トークン消費の詳細（isTokenBasedCall が true の場合に提供）      |
  | `isFreeBugbot`          | 無料の Bugbot 利用かどうか                              |
  | `userEmail`             | リクエスト実行ユーザーのメールアドレス                            |
  | `period`                | クエリ対象データの期間（日時範囲）                              |
</div>

#### 応答例

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
      "kind": "利用量課金",
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
      "kind": "Business に含まれる"
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
  #### リクエスト例
</div>

**デフォルトのページネーションで全ての利用イベントを取得:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**日付範囲と特定のユーザーで絞り込み:**

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

**カスタムページネーションで特定ユーザーの利用イベントを取得:**

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
  ### ユーザーの支出上限を設定
</div>

チームメンバーごとに支出上限を設定できる。これで、チーム内で各ユーザーがAIの利用にどれだけ使えるかを管理できる。

```
POST /teams/user-spend-limit
```

<Note>
  **レート制限:** チームあたり毎分60リクエスト
</Note>

#### リクエストボディ

<div className="full-width-table">
  | パラメータ               | 型      | 必須 | 説明                  |
  | :------------------ | :----- | :- | :------------------ |
  | `userEmail`         | string | はい | チームメンバーのメールアドレス     |
  | `spendLimitDollars` | number | はい | 支出上限（米ドル、整数のみ。小数不可） |
</div>

<Note>
  * ユーザーはすでにチームのメンバーである必要がある
  * 受け付けるのは整数値のみ（小数は不可）
  * `spendLimitDollars` を 0 に設定すると、上限は \$0 になる
</Note>

<div id="response">
  #### Response
</div>

成功または失敗を示す標準化されたレスポンスを返します。

```typescript  theme={null}
{
  outcome: 'success' | 'error';
  message: string;
}
```

<div id="example-responses">
  #### レスポンス例
</div>

**上限を設定しました:**

```json  theme={null}
{
  "outcome": "success",
  "message": "ユーザー developer@company.com の支出上限を $100 に設定しました"
}
```

**エラー応答:**

```json  theme={null}
{
  "outcome": "error",
  "message": "無効なメールアドレス形式です"
}
```

<div id="example-requests">
  #### リクエスト例
</div>

**支出の上限を設定する:**

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

リポジトリを追加し、パターンを設定して、チームでのコンテキストとしてファイルやディレクトリがインデックス化・利用されるのを防ぐ。

<div id="get-team-repo-blocklists">
  #### チームのリポジトリ・ブロックリストを取得
</div>

チームで構成されているすべてのリポジトリ・ブロックリストを取得する。

```
GET /settings/repo-blocklists/repos
```

##### レスポンス

リポジトリのブロックリストオブジェクトの配列を返す：

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
  ##### レスポンスの例
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

##### リクエストの例

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u 自分のAPIキー:
```

<div id="upsert-repo-blocklists">
  #### リポジトリブロックリストのアップサート
</div>

指定したリポジトリの既存のブロックリストを置き換える。
*注: このエンドポイントは、指定したリポジトリに対するパターンのみを上書きする。他のリポジトリには影響しない。*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### リクエストボディ
</div>

| Parameter | Type  | Required | Description              |
| --------- | ----- | -------- | ------------------------ |
| repos     | array | Yes      | リポジトリのブロックリスト対象オブジェクトの配列 |

各リポジトリオブジェクトには以下を含める必要がある:

| Field    | Type      | Required | Description                    |
| -------- | --------- | -------- | ------------------------------ |
| url      | string    | Yes      | ブロックリスト対象のリポジトリのURL            |
| patterns | string\[] | Yes      | ブロックするファイルパターンの配列（glob パターン対応） |

##### レスポンス

更新後のリポジトリ・ブロックリスト一覧を返す：

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
  ##### 例: リクエスト
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
  #### リポジトリブロックリストの削除
</div>

ブロックリストから特定のリポジトリを削除する。

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### パラメータ
</div>

| パラメータ  | 型      | 必須 | 説明                   |
| ------ | ------ | -- | -------------------- |
| repoId | string | はい | 削除対象のリポジトリブロックリストのID |

##### レスポンス

削除に成功すると、204 No Content を返します。

##### リクエストの例

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u APIキー:
```

<div id="pattern-examples">
  #### パターン例
</div>

一般的なブロックリストのパターン:

* `*` - リポジトリ全体をブロック
* `*.env` - すべての.envファイルをブロック
* `config/*` - configディレクトリ内のすべてのファイルをブロック
* `**/*.secret` - 任意のサブディレクトリ内のすべての.secretファイルをブロック
* `src/api/keys.ts` - 特定のファイルをブロック

---

← Previous: [料金](./section.md) | [Index](./index.md) | Next: [AI Code Tracking API](./ai-code-tracking-api.md) →