---
title: "Linear"
source: "https://docs.cursor.com/ja/integrations/linear"
language: "ja"
language_name: "Japanese"
---

# Linear
Source: https://docs.cursor.com/ja/integrations/linear

Linear から Background Agents を利用する

Linear から直接 [Background Agents](/ja/background-agent) を使えるよ。課題を Cursor に委任するか、コメントで `@Cursor` をメンションしてね。

<Frame>
  <video src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-agent.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ac4bacf6bf42c541f45325ba72f8c25f" controls autoPlay muted loop playsInline data-path="images/integrations/linear/linear-agent.mp4" />
</Frame>

<div id="get-started">
  ## はじめよう
</div>

<div id="installation">
  ### インストール
</div>

<Note>
  Linear 連携を有効化するには、Cursor の管理者である必要があるよ。ほかのチーム設定は管理者以外のメンバーでも使える。
</Note>

1. [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations) に移動
2. Linear の横の *Connect* をクリック
3. Linear ワークスペースに接続してチームを選択
4. *Authorize* をクリック
5. Cursor で残りの Background Agent のセットアップを完了:
   * GitHub を接続してデフォルトのリポジトリを選択
   * 従量課金を有効化
   * プライバシー設定を確認

<div id="account-linking">
  ### アカウント連携
</div>

初回利用時に Cursor と Linear のアカウント連携が求められるよ。PR を作成するには GitHub の接続が必要。

<div id="how-to-use">
  ## 使い方
</div>

課題を Cursor にアサインするか、コメントで `@Cursor` をメンションしてね。Cursor は課題を解析して、開発タスク以外を自動で除外するよ。

<div id="delegating-issues">
  ### 課題を委任する
</div>

1. Linear の課題を開く
2. 担当者フィールドをクリック
3. 「Cursor」を選択

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c9a6536a083cfe4a7798c626360e53cc" alt="Linear で課題を Cursor に委任する" data-og-width="1637" width="1637" data-og-height="1046" height="1046" data-path="images/integrations/linear/linear-delegate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b30e2ccb68c4a15b921cf86721878676 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1ac5dfd75e06451de0e688ff87e1ce4c 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7393e80c07e1fe5c33690a970029fe31 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2a07cc74a1d65581a341cf2225b51a37 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5684841fe823ef85472f74748730278c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f7818cae47a652e14557eb20f20b04e 2500w" />
</Frame>

<div id="mentioning-cursor">
  ### Cursor をメンションする
</div>

新しくエージェントを割り当てたり、追加の指示を出したいときは、コメントで `@Cursor` をメンションしてね。例: `@Cursor 上で説明した認証バグを修正して`

<div id="workflow">
  ## ワークフロー
</div>

Background Agents は Linear 上でリアルタイムにステータスを表示し、完了すると自動で PR を作成する。進捗は [Cursor dashboard](https://www.cursor.com/dashboard?tab=background-agents) で確認できる。

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eecf562be6db4d44c397f4786b8ef273" alt="Linear 上の Background Agent のステータス更新" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-activity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=238da245aee71392f22644cb85f7cee4 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21f515fbd2e5917fcf63b8801f66307 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f88441301e6d614ba47756cb886e023 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4927a8d00768a3dbbc0bd5be1faad80e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1707f8223126480c46639428ad5fc85a 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=74ca2ad37e8158bbb86188821bf96299 2500w" />
</Frame>

<div id="follow-up-instructions">
  ### フォローアップ手順
</div>

エージェントのセッションに返信すると、そのままフォローアップとしてエージェントに送信される。実行中の Background Agent に追加の指示を出すには、Linear のコメントで `@Cursor` をメンションすれば OK。

<div id="configuration">
  ## 設定
</div>

[Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents) から Background Agent の設定を行おう。

<div className="full-width-table">
  | Setting                | Location         | Description                                 |
  | :--------------------- | :--------------- | :------------------------------------------ |
  | **Default Repository** | Cursor Dashboard | プロジェクトのリポジトリが未設定のときに使うデフォルトのリポジトリ           |
  | **Default Model**      | Cursor Dashboard | Background Agents で使用する AI モデル              |
  | **Base Branch**        | Cursor Dashboard | PR の作成元となるベースブランチ（通常は `main` または `develop`） |
</div>

<div id="configuration-options">
  ### 設定オプション
</div>

Background Agent の挙動は複数の方法で設定できる:

**Issue の説明やコメント**: `[key=value]` 構文を使う。例:

* `@cursor please fix [repo=anysphere/everysphere]`
* `@cursor implement feature [model=claude-3.5-sonnet] [branch=feature-branch]`

**Issue ラベル**: 親子ラベル構造を使い、親ラベルを設定キー、子ラベルを値にする。

**Project ラベル**: Issue ラベルと同じ親子構造をプロジェクトレベルに適用。

サポートされている設定キー:

* `repo`: 対象リポジトリを指定（例: `owner/repository`）
* `branch`: PR 作成時のベースブランチを指定
* `model`: 使用する AI モデルを指定

<div id="repository-selection">
  ### リポジトリの選択
</div>

Cursor は次の優先順位で作業対象のリポジトリを決定する:

1. **Issue の説明/コメント**: Issue テキストやコメント内の `[repo=owner/repository]` 構文
2. **Issue ラベル**: 該当 Linear Issue に付与されたリポジトリラベル
3. **Project ラベル**: Linear プロジェクトに付与されたリポジトリラベル
4. **Default repository**: Cursor ダッシュボード設定で指定されたリポジトリ

<div id="setting-up-repository-labels">
  #### リポジトリラベルのセットアップ
</div>

Linear でリポジトリラベルを作成する手順:

1. Linear ワークスペースの **Settings** に移動
2. **Labels** をクリック
3. **New group** をクリック
4. グループ名を "repo" にする（大文字小文字は不問。正確に "repo" で、"Repository" などは不可）
5. そのグループ内で、`owner/repo` 形式で各リポジトリのラベルを作成

これらのラベルを Issue や Project に付与することで、Background Agent が作業すべきリポジトリを指定できる。

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6e2b90ce09957a72fdef3c1ed4ef93aa" alt="Linear でのリポジトリラベルの設定" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-project-labels.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1933d2112631527116bd1d817f1a6153 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=93f344ff848172ce6bd97ef652ab03de 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea9f19d7248f39086a20606c6ec14ac6 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=55bfa5cf5b87def6cbe51c3345579eee 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d99c0f06c5fbf33794408350b143f655 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1f731d1978dc5e60c545b745bb9d8ad 2500w" />
</Frame>

{/* ### Getting help

  Check [agent activity](https://www.cursor.com/dashboard?tab=background-agents) and include request IDs when contacting support.

  ## Feedback

  Share feedback through Linear comments or your Cursor dashboard support channels. */}

---

← Previous: [GitHub](./github.md) | [Index](./index.md) | Next: [Slack](./slack.md) →