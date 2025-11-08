---
title: "GitHub Actions"
source: "https://docs.cursor.com/ja/cli/github-actions"
language: "ja"
language_name: "Japanese"
---

# GitHub Actions
Source: https://docs.cursor.com/ja/cli/github-actions

GitHub Actions やその他の継続的インテグレーションシステムで Cursor CLI を使う方法を学ぶ

GitHub Actions やその他の CI/CD システムで Cursor CLI を使って開発タスクを自動化しよう。

<div id="github-actions-integration">
  ## GitHub Actions の統合
</div>

基本的なセットアップ：

```yaml  theme={null}
- name: Cursor CLI のインストール
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Cursor Agent の実行
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "プロンプトを入力" --model gpt-5
```

<div id="cookbook-examples">
  ## クックブックの例
</div>

実践的なワークフローについては、クックブックの例を参照してください：[ドキュメントの更新](/ja/cli/cookbook/update-docs) および [CI の問題の修正](/ja/cli/cookbook/fix-ci)。

<div id="other-ci-systems">
  ## 他のCIシステム
</div>

次の条件がそろっていれば、どんなCI/CDシステムでもCursor CLIを使えるよ:

* **シェルスクリプトの実行**（bash、zsh など）
* **環境変数**でのAPIキー設定
* CursorのAPIにアクセスできる**インターネット接続**

<div id="autonomy-levels">
  ## 自律性レベル
</div>

エージェントの自律性レベルを選ぼう:

<div id="full-autonomy-approach">
  ### フル自律アプローチ
</div>

エージェントに git 操作、API 呼び出し、外部連携の完全なコントロールを与える。セットアップはシンプルで、その分だけ信頼が必要。

**例:** [Update Documentation](/ja/cli/cookbook/update-docs) クックブックでは、最初のワークフローでエージェントが次を実行できる:

* PR の変更を分析
* git ブランチを作成・管理
* 変更をコミットしてプッシュ
* プルリクエストにコメントを投稿
* あらゆるエラーシナリオを処理

```yaml  theme={null}
- name: ドキュメントを更新（完全自律）
  run: |
    cursor-agent -p "git、GitHub CLI、PR 操作にフルアクセスがある。 
    コミット、プッシュ、PR コメントを含むドキュメント更新のワークフロー全体を処理して。"
```

<div id="restricted-autonomy-approach">
  ### 制限付き自律アプローチ
</div>

<Note>
  本番の CI ワークフローには、**権限ベースの制限**と組み合わせたこのアプローチをおすすめ。これなら両方の良さを活かせる：エージェントは複雑な分析やファイル変更を賢くこなしつつ、クリティカルな処理は決定論的で監査可能なままにできる。
</Note>

クリティカルなステップは別のワークフローステップで処理しつつ、エージェントの操作を制限する。制御しやすく、予測可能性も高まる。

**例:** 同じクックブック内の 2 つ目のワークフローでは、エージェントをファイル変更のみに制限している:

```yaml  theme={null}
- name: ドキュメント更新の生成（制限付き）
  run: |
    cursor-agent -p "重要: ブランチの作成、コミット、プッシュ、または PR へのコメント投稿はしないでください。 
    作業ディレクトリ内のファイルのみを変更してください。公開は後続のワークフローステップが実行します。"

- name: ドキュメント用ブランチの公開（決定的）
  run: |
    # 決定的な git 操作は CI が実行
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: PR 用更新"
    git push origin "docs/${{ github.head_ref }}"

- name: PR コメントの投稿（決定的）  
  run: |
    # 決定的な PR コメント投稿は CI が実行
    gh pr comment ${{ github.event.pull_request.number }} --body "Docs を更新しました"
```

<div id="permission-based-restrictions">
  ### 権限ベースの制限
</div>

[権限設定](/ja/cli/reference/permissions) を使って、CLI レベルで制限を適用しよう:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Write(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": [
      "Shell(git)",
      "Shell(gh)",
      "Write(.env*)",
      "Write(package.json)"
    ]
  }
}
```

<div id="authentication">
  ## 認証
</div>

<div id="generate-your-api-key">
  ### API キーを生成
</div>

まずは、Cursor ダッシュボードで[API キーを生成](/ja/cli/reference/authentication#api-key-authentication)しよう。

<div id="configure-repository-secrets">
  ### リポジトリシークレットを設定
</div>

Cursor の API キーをリポジトリ内で安全に保存しよう:

1. GitHub のリポジトリへ移動
2. **Settings** → **Secrets and variables** → **Actions** をクリック
3. **New repository secret** をクリック
4. 名前を `CURSOR_API_KEY` に設定
5. 値に API キーを貼り付け
6. **Add secret** をクリック

<div id="use-in-workflows">
  ### ワークフローで使用する
</div>

`CURSOR_API_KEY` 環境変数を設定しよう:

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```

---

← Previous: [ドキュメントの更新](./section.md) | [Index](./index.md) | Next: [Headless CLI の使用](./headless-cli.md) →