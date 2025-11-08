---
title: "GitHub"
source: "https://docs.cursor.com/ja/integrations/github"
language: "ja"
language_name: "Japanese"
---

# GitHub
Source: https://docs.cursor.com/ja/integrations/github

バックグラウンドエージェント向けの公式 Cursor GitHub アプリ

[Background Agents](/ja/background-agent) と [Bugbot](/ja/bugbot) がリポジトリをクローンし、変更をプッシュするには、Cursor GitHub アプリが必要だ。

<div id="installation">
  ## インストール
</div>

1. [ダッシュボードの Integrations](https://cursor.com/dashboard?tab=integrations) に移動
2. GitHub の横にある **Connect** をクリック
3. リポジトリは **All repositories** か **Selected repositories** を選択

GitHub アカウントを切断するには、Integrations ダッシュボードに戻って **Disconnect Account** をクリック。

<div id="using-agent-in-github">
  ## GitHub で Agent を使う
</div>

GitHub 連携を使うと、pull request や issue から直接、バックグラウンドのエージェントワークフローを実行できる。任意の PR や issue に `@cursor [prompt]` とコメントすると、エージェントがコンテキストを読み取り、修正を実装して、コミットをプッシュする。

[Bugbot](/ja/bugbot) を有効にしてる場合は、`@cursor fix` とコメントするだけで、Bugbot の提案修正を読み取り、問題に対応するバックグラウンドエージェントを起動できる。

<div id="permissions">
  ## 権限
</div>

GitHub アプリはバックグラウンドエージェントと連携するために特定の権限が必要だよ:

<div className="full-width-table">
  | 権限                        | 目的                            |
  | ------------------------- | ----------------------------- |
  | **Repository access**     | コードをクローンして作業用ブランチを作成          |
  | **Pull requests**         | エージェントの変更を含む PR を作成してレビュー用に提出 |
  | **Issues**                | エージェントが見つけた／修正したバグやタスクを追跡     |
  | **Checks and statuses**   | コード品質とテスト結果をレポート              |
  | **Actions and workflows** | CI/CD パイプラインとデプロイ状況を監視        |
</div>

すべての権限は、バックグラウンドエージェントの機能に必要な最小権限の原則に従っている。

<div id="ip-allow-list-configuration">
  ## IP許可リストの設定
</div>

組織でGitHubのIP許可リスト機能を使ってリポジトリへのアクセスを制限してる場合、チームでIP許可リスト機能を有効にするために、まずサポートに連絡してね。

<div id="contact-support">
  ### サポートへの連絡
</div>

IP許可リストを設定する前に、この機能をチーム向けに有効化してもらうため [hi@cursor.com](mailto:hi@cursor.com) に連絡してね。これは以下のどちらの設定方法でも必須だよ。

<div id="enable-ip-allow-list-configuration-for-installed-github-apps-recommended">
  ### インストール済みのGitHubアプリ向けにIP許可リスト設定を有効化する（推奨）
</div>

Cursor GitHubアプリには、あらかじめIPリストが設定されてる。インストール済みアプリ向けの許可リストを有効化すると、このリストを自動的に継承できる。これは「推奨の方法」で、こっちでリストを更新すると、組織側にも自動で反映されるよ。

有効化する手順:

1. 組織のSecurity設定へ移動
2. IP許可リスト設定へ進む
3. 「Allow access by GitHub Apps」をチェック

詳しい手順は、[GitHubのドキュメント](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps)を参照してね。

<div id="add-ips-directly-to-your-allowlist">
  ### 許可リストにIPを直接追加する
</div>

組織がGitHubでIdP定義の許可リストを使っている、または事前設定済みの許可リストを使えない場合は、IPアドレスを手動で追加できるよ。

```
184.73.225.134
3.209.66.12
52.44.113.131
```

<Note>
  IP アドレス一覧はまれに変更されることがある。IP アローリストを使っているチームには、IP アドレスの追加や削除の前に事前に案内する。
</Note>

<div id="troubleshooting">
  ## トラブルシューティング
</div>

<AccordionGroup>
  <Accordion title="エージェントがリポジトリにアクセスできない">
    * リポジトリにアクセス権のある GitHub アプリをインストールする
    * プライベートリポジトリの権限を確認する
    * 自分の GitHub アカウントの権限を確認する
  </Accordion>

  <Accordion title="プルリクエストで Permission denied が発生する">
    * アプリにプルリクエストへの書き込み権限を付与する
    * ブランチ保護ルールを確認する
    * アプリのインストールが期限切れの場合は再インストールする
  </Accordion>

  <Accordion title="GitHub 設定にアプリが表示されない">
    * 組織レベルでインストールされているか確認する
    * [github.com/apps/cursor](https://github.com/apps/cursor) から再インストールする
    * インストールが破損している場合はサポートに連絡する
  </Accordion>
</AccordionGroup>

---

← Previous: [Git](./git.md) | [Index](./index.md) | Next: [Linear](./linear.md) →