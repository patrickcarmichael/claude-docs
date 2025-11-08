---
title: "AI Code Tracking API"
source: "https://docs.cursor.com/ja/account/teams/ai-code-tracking-api"
language: "ja"
language_name: "Japanese"
---

# AI Code Tracking API
Source: https://docs.cursor.com/ja/account/teams/ai-code-tracking-api

チームのリポジトリ向けAI生成コード分析へのアクセス

チームのリポジトリに対するAI生成コードの分析にアクセスできる。コミット単位のAI利用状況や、受け入れられたAI変更の粒度の細かい内訳を含む。

<Note>
  このAPIは初回リリース。フィードバックに基づき機能を拡張中—必要なエンドポイントを教えて！
</Note>

* **提供状況**: エンタープライズチーム限定
* **ステータス**: Alpha（レスポンスの形やフィールドは変更される可能性あり）

<div id="authentication">
  ## 認証
</div>

すべての API リクエストには、API キーによる認証が必要。この API は、他のエンドポイントと同じ Admin API の認証方式を使ってる。

詳しい手順は [Admin API authentication](/ja/account/teams/admin-api#authentication) を参照してね。

<div id="base-url">
  ## ベース URL
</div>

すべての API エンドポイントで使用されるのは次のとおり：

```
https://api.cursor.com
```

<div id="rate-limits">
  ## レート制限
</div>

* エンドポイントごと・チームごとに、1分あたり5リクエスト

<div id="query-parameters">
  ## クエリパラメータ
</div>

以下のエンドポイントはすべて、クエリ文字列で同じクエリパラメータを受け付ける:

<div className="full-width-table">
  | Parameter   | Type   | Required | Description                                                                                                                       |                                                                     |
  | :---------- | :----- | :------- | :-------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
  | `startDate` | string | date     | No                                                                                                                                | ISO日付文字列、リテラルの "now"、または "7d" のような相対日数（「現在 - 7日」の意味）。デフォルト: 現在 - 7日 |
  | `endDate`   | string | date     | No                                                                                                                                | ISO日付文字列、リテラルの "now"、または "0d" のような相対日数。デフォルト: 現在                    |
  | `page`      | number | No       | ページ番号（1始まり）。デフォルト: 1                                                                                                              |                                                                     |
  | `pageSize`  | number | No       | 1ページあたりの件数。デフォルト: 100、最大: 1000                                                                                                    |                                                                     |
  | `user`      | string | No       | 単一ユーザーによる任意のフィルタ。メール（例: [developer@company.com](mailto:developer@company.com)）、エンコード済みID（例: user\_abc123...）、または数値ID（例: 42）を受け付ける |                                                                     |
</div>

<Note>
  レスポンスでは、接頭辞 user\_ が付いたエンコード済み外部IDとして userId を返す。これは API 連携で安定して利用できる。
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## セマンティクスとメトリクスの算出方法
</div>

* **Sources**: "TAB" は受け入れられたインライン補完、"COMPOSER" は Composer で受け入れられた差分を表す
* **Lines metrics**: tabLinesAdded/Deleted と composerLinesAdded/Deleted は個別にカウントされる。nonAiLinesAdded/Deleted は max(0, totalLines - AI lines) で算出される
* **Privacy mode**: クライアントで有効な場合、fileName など一部のメタデータは省略されることがある
* **Branch info**: 現在のブランチがリポジトリのデフォルトブランチと一致する場合、isPrimaryBranch は true。リポジトリ情報が利用できない場合は undefined になることがある

そのファイルを参照すると、コミットと変更がどのように検出され、報告されるかがわかる。

<div id="endpoints">
  ## エンドポイント
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### AI コミットメトリクスの取得（JSON、ページネーション対応）
</div>

TAB、COMPOSER、非 AI への行の帰属に基づく、コミット単位の集計メトリクスを取得する。

```
GET /analytics/ai-code/commits
```

#### 応答

```typescript  theme={null}
{
  items: AiCommitMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### AiCommitMetric フィールド
</div>

<div className="full-width-table">
  | フィールド                  | 型       | 説明                               |                      |
  | :--------------------- | :------ | :------------------------------- | -------------------- |
  | `commitHash`           | string  | Git のコミットハッシュ                    |                      |
  | `userId`               | string  | エンコード済みのユーザー ID（例: user\_abc123） |                      |
  | `userEmail`            | string  | ユーザーのメールアドレス                     |                      |
  | `repoName`             | string  | null                             | リポジトリ名               |
  | `branchName`           | string  | null                             | ブランチ名                |
  | `isPrimaryBranch`      | boolean | null                             | プライマリブランチかどうか        |
  | `totalLinesAdded`      | number  | コミットで追加された行の合計                   |                      |
  | `totalLinesDeleted`    | number  | コミットで削除された行の合計                   |                      |
  | `tabLinesAdded`        | number  | TAB 補完で追加された行数                   |                      |
  | `tabLinesDeleted`      | number  | TAB 補完で削除された行数                   |                      |
  | `composerLinesAdded`   | number  | Composer で追加された行数                |                      |
  | `composerLinesDeleted` | number  | Composer で削除された行数                |                      |
  | `nonAiLinesAdded`      | number  | null                             | 非 AI による追加行数         |
  | `nonAiLinesDeleted`    | number  | null                             | 非 AI による削除行数         |
  | `message`              | string  | null                             | コミットメッセージ            |
  | `commitTs`             | string  | null                             | コミットのタイムスタンプ（ISO 形式） |
  | `createdAt`            | string  | 取り込みタイムスタンプ（ISO 形式）              |                      |
</div>

<div id="example-response">
  #### レスポンス例
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
      "message": "リファクタリング: analytics クライアントの抽出"
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
  #### リクエスト例
</div>

**基本的なリクエスト:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u YOUR_API_KEY:
```

**ユーザー（メールアドレス）で絞り込み：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u YOUR_API_KEY:
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### AI Commit Metrics のダウンロード（CSV・ストリーミング）
</div>

大規模なデータ抽出向けに、コミットメトリクスのデータを CSV 形式でダウンロードできる。

```
GET /analytics/ai-code/commits.csv
```

<div id="response">
  #### レスポンス
</div>

ヘッダー:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV カラム
</div>

<div className="full-width-table">
  | Column                   | Type    | Description          |
  | :----------------------- | :------ | :------------------- |
  | `commit_hash`            | string  | Git のコミットハッシュ        |
  | `user_id`                | string  | エンコード済みユーザー ID       |
  | `user_email`             | string  | ユーザーのメールアドレス         |
  | `repo_name`              | string  | リポジトリ名               |
  | `branch_name`            | string  | ブランチ名                |
  | `is_primary_branch`      | boolean | プライマリブランチかどうか        |
  | `total_lines_added`      | number  | コミットで追加された行数（合計）     |
  | `total_lines_deleted`    | number  | コミットで削除された行数（合計）     |
  | `tab_lines_added`        | number  | TAB 補完で追加された行数       |
  | `tab_lines_deleted`      | number  | TAB 補完で削除された行数       |
  | `composer_lines_added`   | number  | Composer で追加された行数    |
  | `composer_lines_deleted` | number  | Composer で削除された行数    |
  | `non_ai_lines_added`     | number  | 非 AI の追加行数           |
  | `non_ai_lines_deleted`   | number  | 非 AI の削除行数           |
  | `message`                | string  | コミットメッセージ            |
  | `commit_ts`              | string  | コミットのタイムスタンプ（ISO 形式） |
  | `created_at`             | string  | 取り込みタイムスタンプ（ISO 形式）  |
</div>

<div id="sample-csv-output">
  #### サンプル CSV 出力
</div>

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"リファクタ: analytics クライアントを抽出",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"エラー処理を追加",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-request">
  #### リクエストの例
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u YOUR_API_KEY: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### AIコード変更メトリクスを取得（JSON、ページネーション対応）
</div>

決定的な changeId ごとにグループ化された、粒度の高い承認済みAI変更を取得する。コミットから独立して承認されたAIイベントを分析するのに便利。

```
GET /analytics/ai-code/changes
```

#### 応答

```typescript  theme={null}
{
  items: AiCodeChangeMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### AiCodeChangeMetric のフィールド
</div>

<div className="full-width-table">
  | フィールド               | 型                    | 説明                                          |           |
  | :------------------ | :------------------- | :------------------------------------------ | --------- |
  | `changeId`          | string               | 変更の決定的ID                                    |           |
  | `userId`            | string               | エンコード済みユーザーID（例: user\_abc123）              |           |
  | `userEmail`         | string               | ユーザーのメールアドレス                                |           |
  | `source`            | "TAB" または "COMPOSER" | AI変更の発生元                                    |           |
  | `model`             | string               | null                                        | 使用したAIモデル |
  | `totalLinesAdded`   | number               | 追加行数の合計                                     |           |
  | `totalLinesDeleted` | number               | 削除行数の合計                                     |           |
  | `createdAt`         | string               | 取り込みタイムスタンプ（ISO形式）                          |           |
  | `metadata`          | Array                | ファイルのメタデータ（プライバシーモードでは fileName が省略される場合あり） |           |
</div>

<div id="example-response">
  #### レスポンス例
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
  #### リクエスト例
</div>

**基本的なリクエスト：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u YOUR_API_KEY:
```

**ユーザー（エンコード済みID）で絞り込み：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u YOUR_API_KEY:
```

**ユーザー（メールアドレス）で絞り込み：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u YOUR_API_KEY:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### AIコード変更メトリクスをダウンロード（CSV・ストリーミング）
</div>

大規模なデータ抽出のために、変更メトリクスのデータをCSV形式でダウンロードできる。

```
GET /analytics/ai-code/changes.csv
```

<div id="response">
  #### レスポンス
</div>

ヘッダー:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV カラム
</div>

<div className="full-width-table">
  | 列                     | 型      | 説明                          |
  | :-------------------- | :----- | :-------------------------- |
  | `change_id`           | string | 変更を一意に識別する決定的 ID            |
  | `user_id`             | string | エンコードされたユーザー ID             |
  | `user_email`          | string | ユーザーのメールアドレス                |
  | `source`              | string | AI 変更の発生元（TAB または COMPOSER） |
  | `model`               | string | 使用した AI モデル                 |
  | `total_lines_added`   | number | 追加行数の合計                     |
  | `total_lines_deleted` | number | 削除行数の合計                     |
  | `created_at`          | string | 取り込みタイムスタンプ（ISO 形式）         |
  | `metadata_json`       | string | メタデータエントリ配列の JSON 文字列       |
</div>

<div id="notes">
  #### 注意事項
</div>

* metadata\_json はメタデータエントリ配列の JSON 文字列（プライバシーモードでは fileName を省略する場合がある）
* CSV を読み込む場合は、必ず引用符付きフィールドをパースすること

<div id="sample-csv-output">
  #### サンプル CSV 出力
</div>

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-request">
  #### リクエストの例
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u YOUR_API_KEY: \
  -o changes.csv
```

<div id="tips">
  ## ヒント
</div>

* すべてのエンドポイントで特定のユーザーだけを素早く絞り込むには、`user` パラメータを使う
* 大規模なデータ抽出には CSV エンドポイントを推奨—サーバー側で 10,000 件ごとのページとしてストリーミングされる
* デフォルトブランチをクライアント側で解決できない場合、`isPrimaryBranch` は undefined になることがある
* `commitTs` はコミットのタイムスタンプ、`createdAt` はサーバーでの取り込み時刻
* クライアントでプライバシーモードが有効な場合、一部のフィールドが欠落することがある

<div id="changelog">
  ## 変更履歴
</div>

* **アルファ版リリース**: commits と changes 用の初期エンドポイントを追加。フィードバックに応じてレスポンス形式は変更される可能性があります

---

← Previous: [Admin API](./admin-api.md) | [Index](./index.md) | Next: [Analytics](./analytics.md) →