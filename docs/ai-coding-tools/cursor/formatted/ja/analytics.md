---
title: "Analytics"
source: "https://docs.cursor.com/ja/account/teams/analytics"
language: "ja"
language_name: "Japanese"
---

# Analytics
Source: https://docs.cursor.com/ja/account/teams/analytics

チームの利用状況とアクティビティ指標を追跡

チーム管理者は[ダッシュボード](/ja/account/teams/dashboard)から各種メトリクスを確認できる。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a8a4a0ca334e5f5acac55307b2ebeadf" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=73c11df8fcb2862e5c1fd551e6399159 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c3eaa0d4faa7d6fdf5e3c79dfd11fb5a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e9ee5fc554ae46e9d0e2cf53c19e652d 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5f0afded72e0b02142c5a85e448f2d4e 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a6dec2a182ac88d7de75f7a42b1f5ff 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a8ac7dafe559da435f3f4974b04df52 2500w" />
</Frame>

<div id="total-usage">
  ### Total Usage
</div>

チーム全体の集計指標を表示。合計タブ数やプレミアムリクエスト数を含む。作成から30日未満のチームでは、作成以降の利用状況を反映し、メンバーの参加前のアクティビティも含む。

<div id="per-active-user">
  ### Per Active User
</div>

アクティブユーザー1人あたりの平均指標を表示：受け入れられたタブ数、コード行数、プレミアムリクエスト数。

<div id="user-activity">
  ### User Activity
</div>

週次・月次のアクティブユーザー数を追跡。

<div id="analytics-report-headers">
  ## 分析レポートのヘッダー
</div>

ダッシュボードから分析データをエクスポートすると、レポートにはユーザー行動と機能利用に関する詳細なメトリクスが含まれる。各ヘッダーの意味は次のとおり。

<div id="user-information">
  ### ユーザー情報
</div>

<ResponseField name="Date" type="ISO 8601 timestamp">
  分析データが記録された日時（例: 2024-01-15T04:30:00.000Z）
</ResponseField>

<ResponseField name="User ID" type="string">
  システム内の各ユーザーに割り当てられた一意の識別子
</ResponseField>

<ResponseField name="Email" type="string">
  アカウントに紐づくユーザーのメールアドレス
</ResponseField>

<ResponseField name="Is Active" type="boolean">
  当日にユーザーがアクティブだったかを示す
</ResponseField>

<div id="ai-generated-code-metrics">
  ### AI生成コードのメトリクス
</div>

<ResponseField name="Chat Suggested Lines Added" type="number">
  AIチャット機能が追加を提案した行の合計
</ResponseField>

<ResponseField name="Chat Suggested Lines Deleted" type="number">
  AIチャット機能が削除を提案した行の合計
</ResponseField>

<ResponseField name="Chat Accepted Lines Added" type="number">
  ユーザーが受け入れてコードに追加したAI提案の行数
</ResponseField>

<ResponseField name="Chat Accepted Lines Deleted" type="number">
  ユーザーが受け入れたAI提案の削除行数
</ResponseField>

<div id="feature-usage-metrics">
  ### 機能利用メトリクス
</div>

<ResponseField name="Chat Total Applies" type="number">
  チャットからAI生成の変更を適用した回数
</ResponseField>

<ResponseField name="Chat Total Accepts" type="number">
  AI提案を受け入れた回数
</ResponseField>

<ResponseField name="Chat Total Rejects" type="number">
  AI提案を拒否した回数
</ResponseField>

<ResponseField name="Chat Tabs Shown" type="number">
  ユーザーにAI提案タブが表示された回数
</ResponseField>

<ResponseField name="Tabs Accepted" type="number">
  ユーザーが受け入れたAI提案タブの数
</ResponseField>

<div id="request-type-metrics">
  ### リクエスト種別メトリクス
</div>

<ResponseField name="Edit Requests" type="number">
  composer/edit機能を通じて行われたリクエスト（Cmd+Kのインライン編集）
</ResponseField>

<ResponseField name="Ask Requests" type="number">
  ユーザーがAIに質問したチャットリクエスト
</ResponseField>

<ResponseField name="Agent Requests" type="number">
  AIエージェント（特化型AIアシスタント）へのリクエスト
</ResponseField>

<ResponseField name="Cmd+K Usages" type="number">
  Cmd+K（またはCtrl+K）のコマンドパレットが使用された回数
</ResponseField>

<div id="subscription-and-api-metrics">
  ### サブスクリプションとAPIのメトリクス
</div>

<ResponseField name="Subscription Included Reqs" type="number">
  ユーザーのサブスクリプションプランでカバーされるAIリクエスト
</ResponseField>

<ResponseField name="API Key Reqs" type="number">
  プログラムからのアクセスでAPIキーを使用して行われたリクエスト
</ResponseField>

<ResponseField name="Usage-Based Reqs" type="number">
  従量課金の対象となるリクエスト
</ResponseField>

<div id="additional-features">
  ### 追加機能
</div>

<ResponseField name="Bugbot Usages" type="number">
  バグ検出/修正AI機能が使用された回数
</ResponseField>

<div id="configuration-information">
  ### 構成情報
</div>

<ResponseField name="Most Used Model" type="string">
  ユーザーが最も頻繁に使用したAIモデル（例: GPT-4、Claude）
</ResponseField>

<ResponseField name="Most Used Apply Extension" type="string">
  AI提案を適用する際に最もよく使用されたファイル拡張子（例: .ts、.py、.java）
</ResponseField>

<ResponseField name="Most Used Tab Extension" type="string">
  タブ補完機能で最もよく使用されたファイル拡張子
</ResponseField>

<ResponseField name="Client Version" type="string">
  使用中のCursorエディタのバージョン
</ResponseField>

<div id="calculated-metrics">
  ### 算出メトリクス
</div>

レポートには、AIのコード貢献度を把握するための加工データも含まれる。

* Total Lines Added/Deleted: すべてのコード変更の生の件数
* Accepted Lines Added/Deleted: AI提案に由来し、受け入れられた行数
* Composer Requests: インラインcomposer機能を通じて行われたリクエスト
* Chat Requests: チャットインターフェースを通じて行われたリクエスト

<Note>
  数値は未設定の場合はすべて0、booleanはfalse、文字列は空文字にデフォルト設定される。メトリクスはユーザーごとの日次で集計される。
</Note>

---

← Previous: [AI Code Tracking API](./ai-code-tracking-api.md) | [Index](./index.md) | Next: [Analytics V2](./analytics-v2.md) →