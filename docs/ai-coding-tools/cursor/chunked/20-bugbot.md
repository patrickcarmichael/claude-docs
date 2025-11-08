# Bugbot

**Navigation:** [← Previous](./19-panduan-pemecahan-masalah.md) | [Index](./index.md) | [Next →](./21-データサイエンス.md)

---

# Bugbot
Source: https://docs.cursor.com/ja/bugbot

プルリクエスト向けのAIコードレビュー

Bugbotはプルリクエストをレビューし、バグ、セキュリティ上の問題、コード品質の課題を検出する。

<Tip>
  Bugbotには無料プランがあって、毎月使える無料のPRレビュー回数には上限がある。上限に達すると、次回の請求サイクルまでレビューはいったん停止される。いつでもアップグレードして、14日間の無料Proトライアルで無制限レビューを利用できる（標準的な不正利用防止のガードレールが適用される）。
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="PRにコメントを残すBugbot" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

<div id="how-it-works">
  ## 仕組み
</div>

Bugbot は PR の差分を解析して、説明と修正提案つきのコメントを残す。各 PR の更新時に自動で実行されるほか、手動でトリガーすることもできる。

* すべての PR 更新で**自動レビュー**を実行
* どの PR でも `cursor review` または `bugbot run` とコメントして**手動でトリガー**
* **Fix in Cursor** リンクで、課題を Cursor で直接開く
* **Fix in Web** リンクで、課題を [cursor.com/agents](https://cursor.com/agents) で直接開く

<div id="setup">
  ## セットアップ
</div>

Cursor の管理者権限と GitHub 組織の管理者権限が必要だよ。

1. [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot) にアクセス
2. Bugbot タブに移動
3. `Connect GitHub`（すでに接続済みなら `Manage Connections`）をクリック
4. GitHub のインストール手順に従う
5. ダッシュボードに戻って、特定のリポジトリで Bugbot を有効化

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Bugbot の GitHub セットアップ" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

<div id="configuration">
  ## 設定
</div>

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### リポジトリ設定

    インストール一覧からリポジトリ単位で Bugbot を有効/無効にできる。Bugbot は自分が作成した PR に対してのみ動作する。

    ### 個人設定

    * コメントで `cursor review` または `bugbot run` と書いて言及されたときに**のみ実行**する
    * 後続のコミットはスキップし、PR ごとに**一度だけ実行**する
  </Tab>

  <Tab title="Team">
    ### リポジトリ設定

    チーム管理者はリポジトリ単位で Bugbot を有効化し、レビュアーの許可/拒否リストを設定し、次を構成できる:

    * 後続のコミットはスキップし、インストールごとに PR ごと**一度だけ実行**する
    * Bugbot がコード行に直接コメントしないように、**インラインレビューを無効化**する

    Bugbot は、チームメンバーかどうかに関係なく、有効化されたリポジトリのすべてのコントリビューターに対して実行される。

    ### 個人設定

    チームメンバーは自分の PR に対する設定を上書きできる:

    * コメントで `cursor review` または `bugbot run` と書いて言及されたときに**のみ実行**する
    * 後続のコミットはスキップし、PR ごとに**一度だけ実行**する
    * 下書きのプルリクエストも自動レビューに含めるために、**ドラフト PR でのレビューを有効化**する
  </Tab>
</Tabs>

<div id="analytics">
  ### アナリティクス
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Bugbot ダッシュボード" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

<div id="rules">
  ## ルール
</div>

レビュー用のプロジェクト固有コンテキストを提供するために、`.cursor/BUGBOT.md` ファイルを作成しよう。Bugbot は、ルートの `.cursor/BUGBOT.md` に加えて、変更されたファイルから上位ディレクトリへたどっていく中で見つかった追加のファイルも常に取り込む。

```
project/
  .cursor/BUGBOT.md          # 常に含める（プロジェクト全体のルール）
  backend/
    .cursor/BUGBOT.md        # バックエンドのファイルをレビューする際に含める
    api/
      .cursor/BUGBOT.md      # API のファイルをレビューする際に含める
  frontend/
    .cursor/BUGBOT.md        # フロントエンドのファイルをレビューする際に含める
```

<AccordionGroup>
  <Accordion title="Example .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # プロジェクトレビュー・ガイドライン

    ## セキュリティの重点領域

    - API エンドポイントでのユーザー入力の検証
    - データベースクエリにおける SQL インジェクション脆弱性の確認
    - 保護されたルートでの適切な認証の確保

    ## アーキテクチャパターン

    - サービスへの依存性注入の採用
    - データアクセスにリポジトリパターンを適用
    - カスタムエラークラスによる適切なエラーハンドリングの実装

    ## よくある問題

    - React コンポーネントのメモリリーク（useEffect のクリーンアップを確認）
    - UI コンポーネントにおけるエラーバウンダリの未実装
    - 命名規則の不整合（関数は camelCase を使用）

    ```
  </Accordion>
</AccordionGroup>

<div id="pricing">
  ## 料金
</div>

Bugbot には **Free** と **Pro** の2つのプランがあるよ。

<div id="free-tier">
  ### Free tier
</div>

毎月、各ユーザーに無料のPRレビューが限られた回数付与される。チームでは、各メンバーにそれぞれ無料レビュー枠がある。上限に達すると、次の請求サイクルまでレビューは一時停止。無制限でレビューしたい場合は、いつでも14日間の無料Proトライアルにアップグレードできる。

<div id="pro-tier">
  ### Proティア
</div>

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### 定額

    すべてのリポジトリで、月あたり最大200件のPRに対して、Bugbotの無制限レビューが月額\$40。

    ### はじめ方

    アカウント設定から購読してね。
  </Tab>

  <Tab title="Teams">
    ### ユーザー課金

    チームは無制限レビューに対して、ユーザー1人あたり月額\$40を支払う。

    ユーザーは、その月にBugbotがレビューしたPRの作成者としてカウントする。

    すべてのライセンスは各請求サイクルの開始時に解放され、先着順で割り当てられる。あるユーザーがその月にBugbotでレビューされたPRを1件も作成しなかった場合、そのシートは別のユーザーが利用できる。

    ### シート数の上限

    チーム管理者はコスト管理のため、月ごとのBugbotシートの上限を設定できる。

    ### はじめ方

    チームのダッシュボードから購読して、請求を有効化してね。

    ### 悪用防止のガードレール

    悪用を防ぐため、各Bugbotライセンスに対して月あたり200件のプルリクエストのプール上限を設けている。月に200件以上のプルリクエストが必要なら、[hi@cursor.com](mailto:hi@cursor.com) まで連絡してね。対応するよ。

    たとえば、チームに100人のユーザーがいる場合、組織は初期状態で月あたり20,000件のプルリクエストをレビューできる。この上限に自然到達したら、連絡してね。上限を引き上げるよ。
  </Tab>
</Tabs>

<div id="troubleshooting">
  ## トラブルシューティング
</div>

Bugbot が動かないときは:

1. **verbose モードを有効化**: 詳細ログとリクエスト ID を得るために、`cursor review verbose=true` または `bugbot run verbose=true` をコメントで指定
2. **権限を確認**: Bugbot にリポジトリへのアクセス権があるかチェック
3. **インストールを確認**: GitHub アプリがインストールされ、有効になっているか確認

問題を報告するときは、verbose モードで取得したリクエスト ID を含めてね。

<div id="faq">
  ## よくある質問
</div>

<AccordionGroup>
  <Accordion title="Bugbot はプライバシーモードに準拠してる？">
    うん、Bugbot は Cursor と同じプライバシー基準に準拠してて、他の Cursor リクエストと同じ方法でデータを処理するよ。
  </Accordion>

  <Accordion title="無料枠の上限に達したらどうなる？">
    月間の無料枠に達すると、次の請求サイクルまで Bugbot のレビューはいったん停止されるよ。無制限でレビューしたいなら、標準的な不正防止のガードレールが適用される前提で、14日間の無料 Pro トライアルにアップグレードできる。
  </Accordion>
</AccordionGroup>

```
```



# コードレビュー
Source: https://docs.cursor.com/ja/cli/cookbook/code-review

Cursor CLI を使ってプルリクエストを自動レビューし、フィードバックを返す GitHub Actions ワークフローを構築する

このチュートリアルでは、GitHub Actions で Cursor CLI を使ったコードレビューの設定方法を紹介する。ワークフローはプルリクエストを解析し、問題を検出し、コメントでフィードバックを投稿する。

<Tip>
  ほとんどのユーザーには、代わりに [Bugbot](/ja/bugbot) の利用をおすすめする。Bugbot はセットアップ不要で、マネージドな自動コードレビューを提供する。この CLI アプローチは、機能の検証や高度なカスタマイズに役立つ。
</Tip>

<div className="space-y-4">
  <Expandable title="ワークフロー全体のファイル">
    ```yaml cursor-code-review.yml theme={null}
    name: コードレビュー

    on:
      pull_request:
        types: [opened, synchronize, reopened, ready_for_review]

    permissions:
      pull-requests: write
      contents: read
      issues: write

    jobs:
      code-review:
        runs-on: ubuntu-latest
        # 下書き PR は自動コードレビューをスキップ
        if: github.event.pull_request.draft == false
        steps:
          - name: リポジトリをチェックアウト
            uses: actions/checkout@v4
            with:
              fetch-depth: 0
              ref: ${{ github.event.pull_request.head.sha }}

          - name: Cursor CLI をインストール
            run: |
              curl https://cursor.com/install -fsS | bash
              echo "$HOME/.cursor/bin" >> $GITHUB_PATH

          - name: git のユーザー情報を設定
            run: |
              git config user.name "Cursor Agent"
              git config user.email "cursoragent@cursor.com"

          - name: 自動コードレビューを実行
            env:
              CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
              MODEL: gpt-5
              GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
              BLOCKING_REVIEW: ${{ vars.BLOCKING_REVIEW || 'false' }}
            run: |
              cursor-agent --force --model "$MODEL" --output-format=text --print 'GitHub Actions のランナー上で自動コードレビューを実行してる。gh CLI は利用可能で、GH_TOKEN で認証済み。pull request にコメントしてOK。

              コンテキスト:
              - リポジトリ: ${{ github.repository }}
              - PR 番号: ${{ github.event.pull_request.number }}
              - PR ヘッド SHA: ${{ github.event.pull_request.head.sha }}
              - PR ベース SHA: ${{ github.event.pull_request.base.sha }}
              - ブロッキングレビュー: ${{ env.BLOCKING_REVIEW }}

              目的:
              1) 既存のレビューコメントを再チェックし、解決済みなら返信で resolved と記す。
              2) 現在の PR の差分をレビューし、明確で重大度の高い問題だけを指摘する。
              3) 変更行にのみごく短いインラインコメント（1～2文）を残し、最後に簡潔なサマリーを書く。

              手順:
              - 既存コメントを取得: gh pr view --json comments
              - 差分を取得: gh pr diff
              - インライン位置計算用にパッチ付き変更ファイルを取得: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/files --paginate --jq '.[] | {filename,patch}'
              - 各問題の正確なインラインアンカーを計算（ファイルパス + 差分位置）。コメントは必ず差分の変更行にインラインで配置し、トップレベルコメントにはしない。
              - このボットが作成した過去のトップレベル「問題なし」系コメントを検出（本文が "✅ no issues"、"No issues found"、"LGTM" などに一致）。
              - 今回の実行で問題が見つかり、過去に「問題なし」コメントがある場合:
                - 混乱を避けるため削除を優先:
                  - トップレベルの該当コメントを削除: gh api -X DELETE repos/${{ github.repository }}/issues/comments/<comment_id>
                  - 削除不可なら GraphQL（minimizeComment）で最小化、または本文の先頭に "[Superseded by new findings]" を付与して編集。
                - 削除も最小化も不可なら、そのコメントに返信: "⚠️ Superseded: issues were found in newer commits"
              - 以前報告した問題が近傍の変更で解決されたと思われる場合は返信: ✅ This issue appears to be resolved by the recent changes
              - 次のみを解析対象にする:
                - null/undefined 参照
                - リソースリーク（未クローズのファイルや接続）
                - インジェクション（SQL/XSS）
                - 並行性/レースコンディション
                - 重要な処理でのエラーハンドリング欠如
                - 明白なロジックエラーによる不正な挙動
                - 明確なパフォーマンスのアンチパターンで測定可能な影響があるもの
                - 明確なセキュリティ脆弱性
              - 重複回避: 同一または近接行に類似フィードバックがある場合はスキップ。

              コメント規約:
              - インラインコメントは最大 10 件まで。重要度の高いものを優先
              - コメント 1 件につき問題は 1 つ。正確な変更行に配置
              - すべての問題コメントはインライン必須（PR 差分内のファイルと位置に紐付け）
              - 口調は自然で、具体的かつ実行可能な内容にする。自動化や確信度には触れない
              - 絵文字を使用: 🚨 重大 🔒 セキュリティ ⚡ パフォーマンス ⚠️ ロジック ✅ 解決 ✨ 改善

              送信:
              - 報告すべき問題がなく、既に「問題なし」を示すトップレベルコメント（例: "✅ no issues"、"No issues found"、"LGTM"）が存在する場合は、新たなコメントは送信しない。冗長を避けるためスキップ。
              - 報告すべき問題がなく、過去の「問題なし」コメントもない場合は、問題なしを記す短いサマリーコメントを 1 件送信。
              - 報告すべき問題があり、過去に「問題なし」コメントがある場合は、新規レビュー送信前にそれを削除/最小化/新発見で上書き済みと明記。
              - 報告すべき問題がある場合は、インラインコメントのみで構成されるレビューを 1 件だけ送信し、必要なら簡潔なサマリー本文を付与。GitHub Reviews API を用いてコメントがインラインになるようにする:
                - Build a JSON array of comments like: [{ "path": "<file>", "position": <diff_position>, "body": "..." }]
                - Submit via: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/reviews -f event=COMMENT -f body="$SUMMARY" -f comments='[$COMMENTS_JSON]'
              - 使用禁止: gh pr review --approve や --request-changes

              ブロッキング動作:
              - BLOCKING_REVIEW が true で、🚨 または 🔒 の問題を投稿した場合: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
              - それ以外: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
              - 最後に必ず CRITICAL_ISSUES_FOUND を設定
              '

          - name: ブロッキングレビューの結果を確認
            if: env.BLOCKING_REVIEW == 'true'
            run: |
              echo "重大な問題がないか確認中..."
              echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

              if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
                echo "❌ 重大な問題が見つかり、ブロッキングレビューが有効。ワークフローを失敗させる。"
                exit 1
              else
                echo "✅ ブロック対象の問題は見つからなかった。"
              fi
    ```
  </Expandable>

  <Frame>
    <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=31c7e4b54276532df8010645686ebbbc" alt="プルリクエストでインラインコメントを示す自動コードレビューの実行例" data-og-width="2920" width="2920" data-og-height="1272" height="1272" data-path="images/cli/cookbook/code-review/comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=25e552210fa8425a10ff459bf4cd6006 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=234bf271bc595e763549c4f04d2e6fbb 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=b6f6d1444de7fe0197e3d35fa35955e8 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=300314314f5071b77f735460be33985f 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=10e4db857ee84c55d17222cef492611d 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=e65add70ffebfeb9ad05c9bb19a5f4e1 2500w" />
  </Frame>
</div>

<div id="configure-authentication">
  ## 認証の設定
</div>

GitHub Actions で Cursor CLI を認証するには、[API キーとリポジトリのシークレットを設定](/ja/cli/github-actions#authentication)してね。

<div id="set-up-agent-permissions">
  ## エージェントの権限を設定する
</div>

エージェントが実行できるアクションを制御するための設定ファイルを作成しよう。これで、コードのプッシュやプルリクエストの作成といった意図しない操作を防げる。

リポジトリのルートに `.cursor/cli.json` を作成:

```json  theme={null}
{
  "permissions": {
    "deny": [
      "Shell(git push)",
      "Shell(gh pr create)",
      "Write(**)"
    ]
  }
}
```

この設定により、エージェントはファイルを読み取り、コメントには GitHub CLI を使えるけど、リポジトリを変更することはできない。設定の詳細は [permissions reference](/ja/cli/reference/permissions) を見てね。

<div id="build-the-github-actions-workflow">
  ## GitHub Actions のワークフローを構築する
</div>

それじゃあ、ワークフローをステップごとに作っていこう。

<div id="set-up-the-workflow-trigger">
  ### ワークフローのトリガーを設定する
</div>

`.github/workflows/cursor-code-review.yml` を作成して、pull request で実行されるように設定しよう:

```yaml  theme={null}
name: Cursor コードレビュー

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

jobs:
  code-review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    
    steps:
```

<div id="checkout-the-repository">
  ### リポジトリをチェックアウト
</div>

プルリクエストのコードにアクセスできるよう、チェックアウトの手順を追加しよう：

```yaml  theme={null}
- name: リポジトリのチェックアウト
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    ref: ${{ github.event.pull_request.head.sha }}
```

<div id="install-cursor-cli">
  ### Cursor CLI をインストールする
</div>

CLI のインストール手順を追加:

```yaml  theme={null}
- name: Cursor CLI のインストール
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH
```

<div id="configure-the-review-agent">
  ### レビューエージェントを設定する
</div>

完全なレビュー手順を実装する前に、まずレビュー用プロンプトの構造を押さえよう。このセクションでは、エージェントにどう動いてほしいかをまとめる:

**目的**:
エージェントには、現在の PR diff をレビューして、明確で重大度の高い問題だけをフラグし、変更行にのみごく短いインラインコメント（1〜2文）を残し、最後に簡潔なサマリーを付けてほしい。これでシグナルとノイズのバランスを保てる。

**フォーマット**:
コメントは短く、要点だけにする。スキャンしやすくするために絵文字を使い、最後にレビュー全体のハイレベルなサマリーがほしい。

**送信**:
レビューが完了したら、レビューで見つかった内容に基づく短いコメントを含めてほしい。エージェントは、インラインコメントと簡潔なサマリーを含む単一のレビューを送信すべき。

**エッジケース**:
次に対応する必要がある:

* 既存コメントの解決: 対応済みなら完了としてマークする
* 重複回避: 同様の指摘が同一行または近傍にすでにある場合はコメントをスキップする

**最終プロンプト**:
上記の振る舞い要件をすべて組み合わせて、フォーカスされた実行可能なフィードバックを生成する

ではレビューエージェントのステップを実装しよう:

```yaml  theme={null}
- name: コードレビューを実行
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
    GH_TOKEN: ${{ github.token }}
  run: |
    cursor-agent --force --model "$MODEL" --output-format=text --print "GitHub Actions のランナー上で自動コードレビューを実行している。gh CLI は GH_TOKEN で認証済みで利用可能。プルリクエストにコメントしてOK。
    
    コンテキスト:
    - Repo: ${{ github.repository }}
    - PR Number: ${{ github.event.pull_request.number }}
    - PR Head SHA: ${{ github.event.pull_request.head.sha }}
    - PR Base SHA: ${{ github.event.pull_request.base.sha }}
    
    目的:
    1) 既存のレビューコメントを再確認し、対応済みであれば「resolved」と返信
    2) 現在の PR の差分をレビューし、明確で重大度の高い問題のみを指摘
    3) 変更行にのみ非常に短いインラインコメント（1～2文）を残し、最後に簡潔なサマリーを付ける
    
    手順:
    - 既存コメントの取得: gh pr view --json comments
    - 差分の取得: gh pr diff
    - 以前報告した問題が近傍の変更で修正されたと見受けられる場合は、次のように返信: ✅ この問題は最近の変更で解消されたようです
    - 重複回避: 同様のフィードバックが同じ行付近に既にある場合はスキップ
    
    コメントルール:
    - インラインコメントは合計最大10件まで。最も重要な問題を優先
    - 1コメントにつき1件の問題。正確に変更行に付与
    - 口調は自然で、具体的かつ実行可能に。自動化や高確度である旨は言及しない
    - 絵文字の使用: 🚨 重大 🔒 セキュリティ ⚡ パフォーマンス ⚠️ ロジック ✅ 解決 ✨ 改善
    
    提出:
    - インラインコメントと簡潔なサマリーを含むレビューを1件提出
    - 次のみ使用: gh pr review --comment
    - 使用しない: gh pr review --approve または --request-changes"
```

```text  theme={null}
.
├── .cursor/
│   └── cli.json
├── .github/
│   └── workflows/
│       └── cursor-code-review.yml
```

<div id="test-your-reviewer">
  ## レビュアーをテストしよう
</div>

ワークフローが正しく動作し、エージェントが絵文字付きのフィードバックでレビューコメントを投稿することを確認するために、テスト用のプルリクエストを作成しよう。

<Frame>
  <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=aa989eb5b7520e6718a48afd8daa70d9" alt="特定の行へのインラインフィードバックと絵文字付きの自動レビューコメントが表示されたプルリクエスト" data-og-width="1250" width="1250" data-og-height="704" height="704" data-path="images/cli/cookbook/code-review/github-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=9f2e324beb1cccb8052dcd0682323e47 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f08497ddb17921f4bb4638ef4eec3379 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=3c869c0ed8eb8b5743dd3821e57cd406 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=19e98ed953f4cc17b2c578ce543cf88d 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=4d9f47472af81254bd09b5f6234fc97f 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f3af19e3edd7f8bbbb77ba6566d8e183 2500w" />
</Frame>

<div id="next-steps">
  ## 次のステップ
</div>

これで自動コードレビューシステムが動くようになった。次の拡張も検討してみて:

* [CI の失敗を修正](/ja/cli/cookbook/fix-ci)するための追加ワークフローをセットアップ
* ブランチごとに異なるレビュー レベルを設定
* チームの既存のコードレビュー プロセスと統合
* ファイルタイプやディレクトリごとにエージェントの動作をカスタマイズ

<Expandable title="高度: ブロッキングレビュー">
  致命的な問題が見つかった場合にワークフローを失敗させ、対応されるまで pull request のマージを防げる。

  **プロンプトにブロッキング動作を追加**

  まず、レビューエージェントのステップを更新して、`BLOCKING_REVIEW` 環境変数を含め、このブロッキング動作をプロンプトに追加する:

  ```
  Blocking behavior:
  - If BLOCKING_REVIEW is true and any 🚨 or 🔒 issues were posted: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
  - Otherwise: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
  - Always set CRITICAL_ISSUES_FOUND at the end
  ```

  **ブロッキングチェックのステップを追加**

  次に、コードレビューのステップの後にこの新しいステップを追加する:

  ```yaml  theme={null}
        - name: Check blocking review results
          if: env.BLOCKING_REVIEW == 'true'
          run: |
            echo "Checking for critical issues..."
            echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

            if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
              echo "❌ Critical issues found and blocking review is enabled. Failing the workflow."
              exit 1
            else
              echo "✅ No blocking issues found."
            fi
  ```
</Expandable>



# CI 失敗の修正
Source: https://docs.cursor.com/ja/cli/cookbook/fix-ci

GitHub Actions で Cursor CLI を使ってリポジトリの CI 問題を修正する

GitHub Actions 上で Cursor CLI を使って CI の失敗を修正する。このワークフローは失敗を解析し、最小限かつ的確に修正を行い、クイック作成用 PR リンク付きの修正ブランチを作成する。

このワークフローは名前で特定のワークフローを監視する。実際の CI ワークフロー名に合わせて `workflows` のリストを更新してね。

<CodeGroup>
  ```yaml auto-fix-ci.yml theme={null}
  name: Fix CI Failures

  on:
    workflow_run:
      workflows: [Test]
      types: [completed]

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    attempt-fix:
      if: >-
        ${{ github.event.workflow_run.conclusion == 'failure' && github.event.workflow_run.name != 'Fix CI Failures' }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Fix CI failure
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: ci-fix
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - Workflow Run ID: ${{ github.event.workflow_run.id }}
            - Workflow Run URL: ${{ github.event.workflow_run.html_url }}
            - Fix Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Implement an end-to-end CI fix flow driven by the failing PR, creating a separate persistent fix branch and proposing a quick-create PR back into the original PR's branch.

            # Requirements:
            1) Identify the PR associated with the failed workflow run and determine its base and head branches. Let HEAD_REF be the PR's head branch (the contributor/origin branch).
            2) Maintain a persistent fix branch for this PR head using the Fix Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            3) Attempt to resolve the CI failure by making minimal, targeted edits consistent with the repo's style. Keep changes scoped and safe.
            4) You do NOT have permission to create PRs. Instead, post or update a single natural-language PR comment (1–2 sentences) that briefly explains the CI fix and includes an inline compare link to quick-create a PR.

            # Inputs and conventions:
            - Use `gh api`, `gh run view`, `gh pr view`, `gh pr diff`, `gh pr list`, `gh run download`, and git commands as needed to discover the failing PR and branches.
            - Avoid duplicate comments; if a previous bot comment exists, update it instead of posting a new one.
            - If no actionable fix is possible, make no changes and post no comment.

            # Deliverables when updates occur:
            - Pushed commits to the persistent fix branch for this PR head.
            - A single natural-language PR comment on the original PR that includes the inline compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Secret Audit
Source: https://docs.cursor.com/ja/cli/cookbook/secret-audit

GitHub Actions で Cursor CLI を使ってリポジトリのシークレットを監査する

Cursor CLI を使って、リポジトリのセキュリティ脆弱性とシークレット漏えいを監査しよう。ワークフローは潜在的なシークレットをスキャンし、リスクの高いワークフローパターンを検出して、セキュリティ修正案を提案する。

<CodeGroup>
  ```yaml auto-secret-audit.yml theme={null}
  name: Secrets Audit

  on:
    schedule:
      - cron: "0 4 * * *"
    workflow_dispatch:

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    secrets-audit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Scan and propose hardening
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: audit
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
             - Hardening Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Perform a repository secrets exposure and workflow hardening audit on a schedule, and propose minimal safe fixes.

            # Requirements:
            1) Scan for potential secrets in tracked files and recent history; support allowlist patterns if present (e.g., .gitleaks.toml).
            2) Detect risky workflow patterns: unpinned actions, overbroad permissions, unsafe pull_request_target usage, secrets in forked PR contexts, deprecated insecure commands, missing permissions blocks.
            3) Maintain a persistent branch for this run using the Hardening Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            4) Propose minimal edits: redact literals where safe, add ignore rules, pin actions to SHA, reduce permissions, add guardrails to workflows, and add a SECURITY_LOG.md summarizing changes and remediation guidance.
            5) Push to origin.
            6) If there is at least one open PR in the repo, post or update a single natural-language comment (1–2 sentences) on the most recently updated open PR that briefly explains the hardening changes and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update an existing bot comment if present. If no changes or no open PRs, post nothing.

            # Inputs and conventions:
            - Use `gh` to list PRs and to post comments. Avoid duplicate comments.

            # Deliverables when updates occur:
             - Pushed commits to the persistent hardening branch for this run.
            - A single natural-language PR comment with the compare link above (only if an open PR exists).
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# キーの翻訳
Source: https://docs.cursor.com/ja/cli/cookbook/translate-keys

GitHub Actions で Cursor CLI を使ってリポジトリの翻訳キーを管理する

Cursor CLI を使って i18n の翻訳キーを管理する。このワークフローは、プルリクエストで追加・変更された i18n キーを検出し、既存の翻訳を上書きせずに不足分だけを補完する。

<CodeGroup>
  ```yaml auto-translate-keys.yml theme={null}
  name: Translate Keys

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    i18n:
      if: ${{ !startsWith(github.head_ref, 'translate/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Propose i18n updates
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: translate
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Head Ref: ${{ github.head_ref }}
            - Translate Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Detect i18n keys added or changed in the PR and fill only missing locales in message files. Never overwrite existing translations.

            # Requirements:
            1) Determine changed keys by inspecting the PR diff (source files and messages files).
            2) Compute missing keys per locale using the source/canonical locale as truth.
            3) Add entries only for missing keys. Preserve all existing values untouched.
            4) Validate JSON formatting and schemas.
            5) Maintain a persistent translate branch for this PR head using the Translate Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            6) Post or update a single PR comment on the original PR written in natural language (1–2 sentences) that briefly explains what was updated and why, and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update a previous bot comment if present.
            8) If no changes are necessary, make no commits and post no comment.

            # Inputs and conventions:
            - Use `gh pr diff` and git history to detect changes.

            # Deliverables when updates occur:
            - Pushed commits to the persistent translate branch for this PR head.
            - A single natural-language PR comment on the original PR with the compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# ドキュメントの更新
Source: https://docs.cursor.com/ja/cli/cookbook/update-docs

GitHub Actions で Cursor CLI を使ってリポジトリのドキュメントを更新

GitHub Actions で Cursor CLI を使ってドキュメントを更新。方法は2つある: エージェントに全自律で任せるか、エージェントによるファイル変更のみを許可する決定的なワークフロー。

<CodeGroup>
  ```yaml auto-update-docs.yml theme={null}
  name: ドキュメント更新

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: リポジトリのチェックアウト
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Cursor CLI のインストール
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: git の設定
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: ドキュメント更新
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "GitHub Actions のランナー上で動作している。

            GitHub CLI は `gh` として利用可能で、`GH_TOKEN` で認証済み。Git も利用可能。リポジトリ内容への書き込み権限があり、プルリクエストにコメントできるが、PR の作成や編集は行ってはいけない。

            # コンテキスト:
            - リポジトリ: ${{ github.repository }}
            - オーナー: ${{ github.repository_owner }}
            - PR 番号: ${{ github.event.pull_request.number }}
            - ベースリファレンス: ${{ github.base_ref }}
            - ヘッドリファレンス: ${{ github.head_ref }}
            - ドキュメント用ブランチのプレフィックス: ${{ env.BRANCH_PREFIX }}

            # 目標:
            - 元の PR の増分変更に基づいて、エンドツーエンドのドキュメント更新フローを実装する。

            # 要件:
            1) 元の PR での変更点を特定し、複数回のプッシュがある場合は、直近のドキュメント更新以降の増分差分を算出する。
            2) その増分変更に基づき、関連するドキュメントのみを更新する。
            3) コンテキストで指定されたドキュメント用ブランチのプレフィックスを使い、この PR のヘッドに対応する永続的なドキュメント用ブランチを維持する。なければ作成し、あれば更新し、変更を origin にプッシュする。
            4) PR を作成する権限はない。代わりに、ドキュメント更新を簡潔に説明し、PR を素早く作成できるインラインの比較リンクを含む、1～2文の自然言語による単一の PR コメントを投稿または更新すること。

            # 入力と規約:
            - 変更を検出し、直近のドキュメント更新以降の増分範囲を導き出すために、`gh pr diff` と git の履歴を使用する。
            - PR を直接作成または編集しない。上記の比較リンク形式を使用する。
            - 変更は最小限にし、リポジトリのスタイルに合わせる。ドキュメント更新が不要な場合は、変更もコメント投稿も行わない。

            # 更新が発生した場合の成果物:
            - この PR のヘッドに対応する永続的なドキュメント用ブランチへのコミットをプッシュする。
            - 元の PR に対して、上記のインライン比較リンクを含む自然言語による単一の PR コメント。重複投稿は避け、既存のボットコメントがあればそれを更新する。
            " --force --model "$MODEL" --output-format=text
  ```

  ```yaml auto-update-docs-deterministic.yml theme={null}
  name: ドキュメント更新

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: リポジトリのチェックアウト
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Cursor CLI のインストール
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: git の設定
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: ドキュメント更新を生成（コミット/プッシュ/コメントなし）
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available.

            IMPORTANT: Do NOT create branches, commit, push, or post PR comments. Only modify files in the working directory as needed. A later workflow step is responsible for publishing changes and commenting on the PR.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}

            # Goal:
            - この PR によって導入された増分変更に基づいて、リポジトリのドキュメントを更新する。

            # Requirements:
            1) 元の PR で何が変わったかを特定する（必要に応じて `gh pr diff` と git の履歴を使用）。永続的なドキュメント用ブランチ `${{ env.BRANCH_PREFIX }}/${{ github.head_ref }}` が存在する場合は、過去の更新を把握するための参照専用として利用してよい。
            2) それらの変更に基づいて、関連するドキュメントのみを更新する。編集は最小限に留め、リポジトリのスタイルに合わせる。
            3) ブランチの作成、コミット、プッシュ、PR へのコメント投稿はしない。作業ツリー内のファイルのみ更新した状態で残し、公開は後続ステップに任せる。

            # Inputs and conventions:
            - `gh pr diff` と git の履歴を使って変更点を検出し、それに応じてドキュメント編集の焦点を絞る。
            - ドキュメント更新が不要な場合は、変更も出力も行わない。

            # Deliverables when updates occur:
            - 作業ディレクトリ内の変更済みドキュメントファイルのみ（コミット/プッシュ/コメントなし）。
            " --force --model "$MODEL" --output-format=text

        - name: ドキュメント用ブランチの公開
          id: publish_docs
          env:
            BRANCH_PREFIX: docs
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |
            echo "changes_published=false" >> "$GITHUB_OUTPUT"

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"

            # プッシュ可能なローカルブランチ上にいることを確認
            git fetch origin --prune

            # 現在の作業ツリーの変更を維持したまま、永続的なドキュメント用ブランチを作成/切り替え
            git checkout -B "$DOCS_BRANCH"

            # 変更をステージして検出
            git add -A
            if git diff --staged --quiet; then
              echo "公開するドキュメントの変更はありません。コミット/プッシュをスキップします。"
              exit 0
            fi

            COMMIT_MSG="docs: PR #${PR_NUMBER} 向けの更新（${HEAD_REF} @ $(git rev-parse --short HEAD)）"
            git commit -m "$COMMIT_MSG"
            git push --set-upstream origin "$DOCS_BRANCH"

            echo "changes_published=true" >> "$GITHUB_OUTPUT"

        - name: PR コメントの投稿または更新
          if: steps.publish_docs.outputs.changes_published == 'true'
          env:
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
            REPO: ${{ github.repository }}
            BASE_REF: ${{ github.base_ref }}
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"
            COMPARE_URL="https://github.com/${REPO}/compare/${BASE_REF}...${DOCS_BRANCH}?quick_pull=1&title=docs%3A+updates+for+PR+%23${PR_NUMBER}"

            COMMENT_FILE="${RUNNER_TEMP}/auto-docs-comment.md"
            {
              echo "Cursor がドキュメント用ブランチを更新しました: \`${DOCS_BRANCH}\`"
              echo "今すぐ[差分を確認して、このドキュメント更新をマージするための PR をクイック作成](${COMPARE_URL})できるよ。"
              echo
              echo "_このコメントは、PR の変更に応じて後続の実行で更新されるよ。_"
              echo
              echo "<!-- auto-update-docs-split -->"
            } > "$COMMENT_FILE"

            # 直近のボットコメントの編集に失敗した場合（古い gh）、新規コメント作成にフォールバック
            if gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE" --edit-last; then
              echo "既存の PR コメントを更新しました。"
            else
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              echo "新しい PR コメントを投稿しました。"
            fi
  ```
</CodeGroup>



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



# Headless CLI の使用
Source: https://docs.cursor.com/ja/cli/headless

Cursor CLI を使って、自動コード解析・生成・変更のためのスクリプトを書く方法を学ぶ

コード解析・生成・リファクタリングのタスク向けに、スクリプトや自動化ワークフローで Cursor CLI を使おう。

<div id="how-it-works">
  ## 仕組み
</div>

非対話型のスクリプトや自動化には [print mode](/ja/cli/using#non-interactive-mode) (`-p, --print`) を使おう。

<div id="file-modification-in-scripts">
  ### スクリプトでのファイル変更
</div>

スクリプト内でファイルを変更するなら、`--print` と `--force` を組み合わせよう:

```bash  theme={null}

# print モードでファイルの変更を有効化
cursor-agent -p --force "このコードをモダンな ES6+ 構文にリファクタリングして"


# --force を付けない場合、変更は提案のみで適用されない
cursor-agent -p "このファイルに JSDoc コメントを追加して"  # ファイルは変更されない


# 実際にファイルを書き換えるバッチ処理
find src/ -name "*.js" | while read file; do
  cursor-agent -p --force "$file に網羅的な JSDoc コメントを追加して"
done
```

<Warning>
  `--force` フラグを使うと、エージェントが確認なしでファイルを直接変更できる
</Warning>

<div id="setup">
  ## セットアップ
</div>

詳細なセットアップ手順は、[Installation](/ja/cli/installation) と [Authentication](/ja/cli/reference/authentication) を参照してね。

```bash  theme={null}

# Cursor CLI をインストール
curl https://cursor.com/install -fsS | bash


# スクリプト用のAPIキーを設定
export CURSOR_API_KEY=your_api_key_here
cursor-agent -p "このコードを分析して"
```

<div id="example-scripts">
  ## サンプルスクリプト
</div>

スクリプトの用途に合わせて出力形式を使い分けよう。詳しくは [Output format](/ja/cli/reference/output-format) を参照してね。

<div id="searching-the-codebase">
  ### コードベースを検索する
</div>

読みやすい出力には `--output-format text` を使おう:

```bash  theme={null}
#!/bin/bash

# コードベースに関する簡単な質問

cursor-agent -p --output-format text "このコードベースは何をするの？"
```

<div id="automated-code-review">
  ### 自動コードレビュー
</div>

構造化された分析には `--output-format json` を使おう:

```bash  theme={null}
#!/bin/bash

# simple-code-review.sh - 基本的なコードレビュー用スクリプト

echo "コードレビューを開始..."


# 直近の変更をレビュー
cursor-agent -p --force --output-format text \
  "直近のコード変更をレビューして、次の点についてフィードバックして:
  - コード品質と可読性
  - バグや問題の可能性
  - セキュリティ面での考慮事項
  - ベストプラクティスの遵守状況

  改善のための具体的な提案をして、review.txt に書き込んで"

if [ $? -eq 0 ]; then
  echo "✅ コードレビューが正常に完了"
else
  echo "❌ コードレビューに失敗"
  exit 1
fi
```

<div id="real-time-progress-tracking">
  ### リアルタイム進捗のトラッキング
</div>

リアルタイムで進捗を追跡するには、`--output-format stream-json` を使ってね：

```bash  theme={null}
#!/bin/bash

# stream-progress.sh - リアルタイムで進捗を追跡

echo "🚀 ストリーム処理を開始..."


# リアルタイムで進捗を追跡
accumulated_text=""
tool_count=0
start_time=$(date +%s)

cursor-agent -p --force --output-format stream-json \
  "このプロジェクトの構成を分析し、analysis.txt に要約レポートを作成して"
  while IFS= read -r line; do
    
    type=$(echo "$line" | jq -r '.type // empty')
    subtype=$(echo "$line" | jq -r '.subtype // empty')
    
    case "$type" in
      "system")
        if [ "$subtype" = "init" ]; then
          model=$(echo "$line" | jq -r '.model // "unknown"')
          echo "🤖 使用モデル: $model"
        fi
        ;;
        
      "assistant")
        # ストリーミング中のテキスト差分を蓄積
        content=$(echo "$line" | jq -r '.message.content[0].text // empty')
        accumulated_text="$accumulated_text$content"
        
        # 進捗をライブ表示
        printf "\r📝 生成中: %d 文字" ${#accumulated_text}
        ;;
        
      "tool_call")
        if [ "$subtype" = "started" ]; then
          tool_count=$((tool_count + 1))
          
          # ツール情報を抽出
          if echo "$line" | jq -e '.tool_call.writeToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.writeToolCall.args.path // "unknown"')
            echo -e "\n🔧 ツール #$tool_count: $path を作成"
          elif echo "$line" | jq -e '.tool_call.readToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.readToolCall.args.path // "unknown"')
            echo -e "\n📖 ツール #$tool_count: $path を読み取り"
          fi
          
        elif [ "$subtype" = "completed" ]; then
          # ツールの結果を抽出して表示
          if echo "$line" | jq -e '.tool_call.writeToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.linesCreated // 0')
            size=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.fileSize // 0')
            echo "   ✅ $lines 行を作成（$size バイト）"
          elif echo "$line" | jq -e '.tool_call.readToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.readToolCall.result.success.totalLines // 0')
            echo "   ✅ $lines 行を読み取り"
          fi
        fi
        ;;
        
      "result")
        duration=$(echo "$line" | jq -r '.duration_ms // 0')
        end_time=$(date +%s)
        total_time=$((end_time - start_time))
        
        echo -e "\n\n🎯 完了: ${duration}ms（合計 ${total_time}s）"
        echo "📊 最終統計: ツール $tool_count 個、生成文字数 ${#accumulated_text}"
        ;;
    esac
  done
```



# インストール
Source: https://docs.cursor.com/ja/cli/installation

Cursor CLI のインストールと更新

<div id="installation">
  ## インストール
</div>

<div id="macos-linux-and-windows-wsl">
  ### macOS、Linux、Windows（WSL）
</div>

ワンコマンドで Cursor CLI をインストール:

```bash  theme={null}
curl https://cursor.com/install -fsS | bash
```

<div id="verification">
  ### 検証
</div>

インストール後、Cursor CLI が正しく動作しているか確認する:

```bash  theme={null}
cursor-agent --version
```

<div id="post-installation-setup">
  ## インストール後のセットアップ
</div>

1. **\~/.local/bin を PATH に追加:**

   bash の場合:

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

   zsh の場合:

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

2. **Cursor Agent を使い始める:**
   ```bash  theme={null}
   cursor-agent
   ```

<div id="updates">
  ## アップデート
</div>

Cursor CLI は、常に最新バージョンを使えるように、デフォルトで自動更新を行う。

Cursor CLI を手動で最新バージョンに更新するには：

```bash  theme={null}
cursor-agent update

# または 
cursor-agent upgrade
```

どっちのコマンドでも、Cursor Agent を最新バージョンに更新できるよ。



# MCP
Source: https://docs.cursor.com/ja/cli/mcp

MCP サーバーを cursor-agent と組み合わせて外部ツールやデータソースに接続する

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="overview">
  ## 概要
</div>

Cursor CLI は [Model Context Protocol (MCP)](/ja/context/mcp) サーバーをサポートしていて、外部ツールやデータソースを `cursor-agent` に接続できる。**CLI の MCP はエディターと同じ設定を使う** — 設定した MCP サーバーはどちらでもシームレスに動く。

<Card title="MCP について学ぶ" icon="link" href="/ja/context/mcp">
  MCP は初めて？ 設定、認証、利用可能なサーバーに関する完全ガイドを読もう
</Card>

<div id="cli-commands">
  ## CLI コマンド
</div>

`cursor-agent mcp` コマンドで MCP サーバーを管理する:

<div id="list-configured-servers">
  ### 設定済みサーバーの一覧
</div>

設定済みの MCP サーバーと現在の状態をすべて表示する:

```bash  theme={null}
cursor-agent mcp list
```

This shows:

* サーバー名と識別子
* 接続状態（接続済み／切断）
* 設定の参照元（プロジェクトまたはグローバル）
* トランスポート方式（stdio、HTTP、SSE）

<div id="list-available-tools">
  ### 利用可能なツールを一覧表示
</div>

特定の MCP サーバーが提供するツールを表示:

```bash  theme={null}
cursor-agent mcp list-tools <ID>
```

This displays:

* ツール名と説明
* 必須・任意パラメータ
* パラメータの型と制約

<div id="login-to-mcp-server">
  ### MCP サーバーにログイン
</div>

`mcp.json` で設定した MCP サーバーで認証する:

```bash  theme={null}
cursor-agent mcp login <識別子>
```

<div id="disable-mcp-server">
  ### MCP サーバーを無効化する
</div>

ローカルの承認リストから MCP サーバーを削除する:

```bash  theme={null}
cursor-agent mcp disable <identifier>
```

<div id="using-mcp-with-agent">
  ## Agent で MCP を使う
</div>

MCP サーバーの設定が完了したら（セットアップ手順は[メインの MCP ガイド](/ja/context/mcp)を参照）、`cursor-agent` はリクエストに関係する場面で、利用可能なツールを自動的に検出して使うよ。

```bash  theme={null}

# 利用可能な MCP サーバーを確認
cursor-agent mcp list


# 特定のサーバーが提供するツールを確認
cursor-agent mcp list-tools playwright


# cursor-agent を使う — 必要に応じて自動で MCP ツールを使用
cursor-agent --prompt "google.com にアクセスして検索ページのスクリーンショットを撮って"
```

CLI はエディタと同じ設定の優先順位（project → global → nested）に従い、親ディレクトリから設定を自動検出する。

<div id="related">
  ## 関連
</div>

<CardGroup cols={2}>
  <Card title="MCP 概要" icon="link" href="/ja/context/mcp">
    セットアップ、構成、認証までのMCP完全ガイド
  </Card>

  <Card title="利用可能な MCP ツール" icon="table" href="/ja/tools">
    すぐ使えるプリビルトのMCPサーバーを探す
  </Card>
</CardGroup>



# Cursor CLI
Source: https://docs.cursor.com/ja/cli/overview

ターミナルでのコーディングを始めるなら Cursor CLI

Cursor CLI は、ターミナルから AI エージェントに直接アクセスして、コードの作成・レビュー・変更を行える。対話型のターミナル UI はもちろん、スクリプトや CI パイプライン向けの出力自動化にも対応し、作業する場所でそのまま強力なコーディング支援を提供する。

```bash  theme={null}

# インストール
curl https://cursor.com/install -fsS | bash


# 対話型セッションを起動
cursor-agent
```

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/cli-overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b323547dd61e985df8c0d6179c1492bd" autoPlay loop muted playsInline controls data-path="images/cli/cli-overview.mp4" />
</Frame>

<Info>
  Cursor CLI は現在ベータ版。ぜひフィードバックを聞かせてほしい！
</Info>

<div id="interactive-mode">
  ### インタラクティブモード
</div>

エージェントとの会話セッションを開始して、目標を伝え、提案された変更を確認し、コマンドを承認しよう:

```bash  theme={null}

# 対話セッションを開始
cursor-agent


# 初期プロンプトで開始
cursor-agent "auth モジュールを JWT トークンを用いるようにリファクタリングして"
```

<div id="non-interactive-mode">
  ### 非対話モード
</div>

スクリプト、CI パイプライン、自動化などの非対話シナリオでは、print モードを使う：

```bash  theme={null}

# 特定のプロンプトとモデルで実行
cursor-agent -p "パフォーマンス問題を見つけて修正して" --model "gpt-5"


# レビューのために git の変更を含めて実行
cursor-agent -p "これらの変更にセキュリティ上の問題がないかレビューして" --output-format text
```

<div id="sessions">
  ### セッション
</div>

以前の会話を再開して、複数回のやり取りにわたって文脈を維持する:

```bash  theme={null}

# これまでのチャットをすべて一覧表示
cursor-agent ls


# 直近の会話を再開
cursor-agent resume


# 特定の会話を再開
cursor-agent --resume="chat-id-here"
```



# 認証
Source: https://docs.cursor.com/ja/cli/reference/authentication

ブラウザフローまたは API キーで Cursor CLI に認証する

Cursor CLI は 2 つの認証方法をサポートしてる。推奨はブラウザベースのログインで、もう一つは API キーだよ。

<div id="browser-authentication-recommended">
  ## ブラウザ認証（推奨）
</div>

いちばん簡単に認証するなら、ブラウザフローを使おう：

```bash  theme={null}

# ブラウザフローでログイン
cursor-agent login


# 認証状態を確認
cursor-agent status


# ログアウトして保存済みの認証情報を消去
cursor-agent logout
```

login コマンドはデフォルトのブラウザを開いて、Cursor アカウントでのサインインを求められるよ。完了すると、資格情報はローカルに安全に保存される。

<div id="api-key-authentication">
  ## APIキー認証
</div>

自動化やスクリプト、CI/CD環境では、APIキー認証を使ってね:

<div id="step-1-generate-an-api-key">
  ### ステップ1: APIキーを生成
</div>

Cursorのダッシュボードの Integrations > User API Keys でAPIキーを生成してね。

<div id="step-2-set-the-api-key">
  ### ステップ2: APIキーを設定
</div>

APIキーは次の2通りの方法で設定できるよ:

**オプション1: 環境変数（推奨）**

```bash  theme={null}
export CURSOR_API_KEY=your_api_key_here
cursor-agent "ユーザー認証を実装する"
```

**オプション 2：コマンドラインフラグ**

```bash  theme={null}
cursor-agent --api-key your_api_key_here "ユーザ認証を実装する"
```

<div id="authentication-status">
  ## 認証ステータス
</div>

現在の認証状況を確認するには:

```bash  theme={null}
cursor-agent status
```

This command will display:

* 認証されているかどうか
* アカウント情報
* 現在のエンドポイント構成

<div id="troubleshooting">
  ## トラブルシューティング
</div>

* **「Not authenticated」エラー:** `cursor-agent login` を実行するか、API キーが正しく設定されているか確認してね
* **SSL 証明書エラー:** 開発環境では `--insecure` フラグを使ってね
* **エンドポイントの問題:** カスタム API エンドポイントを指定するには `--endpoint` フラグを使ってね



# 設定
Source: https://docs.cursor.com/ja/cli/reference/configuration

cli-config.json 用 Agent CLI 設定リファレンス

cli-config.json を使用して Agent CLI を構成する。

<div id="file-location">
  ## ファイルの場所
</div>

<div class="full-width-table">
  | 種別     | プラットフォーム    | パス                                         |
  | :----- | :---------- | :----------------------------------------- |
  | グローバル  | macOS/Linux | `~/.cursor/cli-config.json`                |
  | グローバル  | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | プロジェクト | All         | `<project>/.cursor/cli.json`               |
</div>

<Note>プロジェクト単位で設定できるのは権限のみ。その他の CLI 設定はすべてグローバルで設定してね。</Note>

環境変数でオーバーライド:

* **`CURSOR_CONFIG_DIR`**: カスタムディレクトリのパス
* **`XDG_CONFIG_HOME`** (Linux/BSD): `$XDG_CONFIG_HOME/cursor/cli-config.json` を使用

<div id="schema">
  ## スキーマ
</div>

<div id="required-fields">
  ### 必須フィールド
</div>

<div class="full-width-table">
  | フィールド               | 型         | 説明                                                        |
  | :------------------ | :-------- | :-------------------------------------------------------- |
  | `version`           | number    | 設定スキーマのバージョン（現在: `1`）                                     |
  | `editor.vimMode`    | boolean   | Vimキーバインドを有効化（既定値: `false`）                               |
  | `permissions.allow` | string\[] | 許可される操作（[Permissions](/ja/cli/reference/permissions) を参照） |
  | `permissions.deny`  | string\[] | 禁止される操作（[Permissions](/ja/cli/reference/permissions) を参照） |
</div>

<div id="optional-fields">
  ### 任意フィールド
</div>

<div class="full-width-table">
  | フィールド                    | 型       | 説明                    |
  | :----------------------- | :------ | :-------------------- |
  | `model`                  | object  | 選択済みモデルの設定            |
  | `hasChangedDefaultModel` | boolean | CLI 管理のデフォルトモデル上書きフラグ |
</div>

<div id="examples">
  ## 例
</div>

<div id="minimal-config">
  ### 最小構成
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="enable-vim-mode">
  ### Vim モードを有効にする
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="configure-permissions">
  ### 権限の設定
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

利用可能な権限の種類や例は、[Permissions](/ja/cli/reference/permissions)を見てね。

<div id="troubleshooting">
  ## トラブルシューティング
</div>

**設定エラー**: いったんファイルを別の場所に移動して、再起動してみて:

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**変更が保存されない**: JSON の構文が正しいか、書き込み権限があるかを確認。いくつかのフィールドは CLI によって管理されており、上書きされることがある。

<div id="notes">
  ## メモ
</div>

* 純粋な JSON 形式（コメント不可）
* 欠落フィールドは CLI が自動修復する
* 破損したファイルは `.bad` としてバックアップされ、再生成される
* 権限エントリは完全一致の文字列（詳しくは [Permissions](/ja/cli/reference/permissions) を参照）



# 出力フォーマット
Source: https://docs.cursor.com/ja/cli/reference/output-format

テキスト、JSON、stream-JSON フォーマットの出力スキーマ

Cursor Agent CLI は、`--print` と組み合わせることで `--output-format` オプションにより複数の出力フォーマットを提供する。プログラムからの利用に適した構造化フォーマット（`json`、`stream-json`）に加え、人間が進捗を読み取りやすい簡易テキストフォーマットを用意している。

<Note>
  デフォルトの `--output-format` は `stream-json`。このオプションが有効になるのは、出力を表示する場合（`--print`）か、表示モードが推定される場合（TTY でない stdout、またはパイプされた stdin）に限られる。
</Note>

<div id="json-format">
  ## JSON 形式
</div>

`json` 出力形式は、実行が正常に完了すると単一の JSON オブジェクト（末尾に改行）を出力する。デルタやツールイベントは出力されず、テキストは最終結果に集約される。

失敗時は、プロセスは非ゼロの終了コードで終了し、エラーメッセージを stderr に書き出す。失敗時には、正しく構成された JSON オブジェクトは出力されない。

<div id="success-response">
  ### 成功時のレスポンス
</div>

成功すると、CLI は次の構造の JSON オブジェクトを出力する:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "result": "<アシスタントの完全なテキスト>"
  "session_id": "<uuid>",
  "request_id": "<任意のリクエストID>"
}
```

<div class="full-width-table">
  | Field             | Description                            |
  | ----------------- | -------------------------------------- |
  | `type`            | ターミナル結果では常に `"result"`                 |
  | `subtype`         | 成功した完了時は常に `"success"`                 |
  | `is_error`        | 成功したレスポンスでは常に `false`                  |
  | `duration_ms`     | 実行時間の合計（ミリ秒）                           |
  | `duration_api_ms` | API リクエスト時間（ミリ秒、現在は `duration_ms` と同一） |
  | `result`          | アシスタントの応答全文（すべてのテキストデルタを連結したもの）        |
  | `session_id`      | 一意のセッション識別子                            |
  | `request_id`      | 任意のリクエスト識別子（省略される場合あり）                 |
</div>

<div id="stream-json-format">
  ## Stream JSON フォーマット
</div>

`stream-json` の出力フォーマットは、改行区切り JSON（NDJSON）を出力する。各行には、実行中のリアルタイムイベントを表す単一の JSON オブジェクトが含まれる。

ストリームは、成功時には終端の `result` イベントで終了する。失敗時には、プロセスは非ゼロの終了コードで終了し、終端イベントなしに早期に終了する場合がある。エラーメッセージは stderr に出力される。

<div id="event-types">
  ### イベントタイプ
</div>

<div id="system-initialization">
  #### システム初期化
</div>

各セッションの開始時に一度だけ出力される:

```json  theme={null}
{
  "type": "system",
  "subtype": "init",
  "apiKeySource": "env|flag|login"
  "cwd": "/absolute/path"
  "session_id": "<uuid>",
  "model": "<モデルの表示名>"
  "permissionMode": "default"
}
```

<Note>
  将来的に、このイベントに `tools` や `mcp_servers` といったフィールドが追加される可能性がある。
</Note>

<div id="user-message">
  #### ユーザーメッセージ
</div>

ユーザーの入力プロンプトを含む:

```json  theme={null}
{
  "type": "user",
  "message": {
    "role": "user",
    "content": [{ "type": "text", "text": "<prompt>" }]
  },
  "session_id": "<uuid>"
}
```

<div id="assistant-text-delta">
  #### Assistant text delta
</div>

アシスタントがレスポンスを生成するあいだに複数回発行される。これらのイベントには、インクリメンタルなテキストチャンクが含まれる:

```json  theme={null}
{
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [{ "type": "text", "text": "<delta チャンク>" }]
  },
  "session_id": "<uuid>"
}
```

<Note>
  完全なアシスタントの返答を再構成するには、順番どおりにすべての `message.content[].text` の値を連結してね。
</Note>

<div id="tool-call-events">
  #### ツール呼び出しイベント
</div>

ツール呼び出しは開始イベントと完了イベントで追跡される:

**ツール呼び出しの開始:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "started",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" }
    }
  },
  "session_id": "<uuid>"
}
```

**ツール呼び出しが完了しました:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "completed",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" },
      "result": {
        "success": {
          "content": "ファイルの内容...",
          "isEmpty": false,
          "exceededLimit": false,
          "totalLines": 54,
          "totalChars": 1254
        }
      }
    }
  },
  "session_id": "<uuid>"
}
```

<div id="tool-call-types">
  #### ツール呼び出しの種類
</div>

**ファイル読み取りツール:**

* **開始**: `tool_call.readToolCall.args` に `{ "path": "file.txt" }` が含まれる
* **完了**: `tool_call.readToolCall.result.success` にファイルのメタデータと内容が含まれる

**ファイル書き込みツール:**

* **開始**: `tool_call.writeToolCall.args` に `{ "path": "file.txt", "fileText": "content...", "toolCallId": "id" }` が含まれる
* **完了**: `tool_call.writeToolCall.result.success` に `{ "path": "/absolute/path", "linesCreated": 19, "fileSize": 942 }` が含まれる

**その他のツール:**

* `{ "name": "tool_name", "arguments": "..." }` を持つ `tool_call.function` 構造を使用する場合がある

<div id="terminal-result">
  #### ターミナル結果
</div>

正常終了時に発行される最終イベント:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "is_error": false,
  "result": "<アシスタントの全文>",
  "session_id": "<uuid>",
  "request_id": "<任意のリクエストID>"
}
```

<div id="example-sequence">
  ### 例のシーケンス
</div>

典型的なイベントフローを示す代表的な NDJSON シーケンスは次のとおり:

```json  theme={null}
{"type":"system","subtype":"init","apiKeySource":"login","cwd":"/Users/user/project","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","model":"Claude 4 Sonnet","permissionMode":"default"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"README.mdを読んで要約を作成して"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"やるね"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"README.mdファイルを読むね"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"},"result":{"success":{"content":"# プロジェクト\n\nこれはサンプルプロジェクトです...","isEmpty":false,"exceededLimit":false,"totalLines":54,"totalChars":1254}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"それから要約を作成するね"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README要約\n\nこのプロジェクトには…が含まれている","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README要約\n\nこのプロジェクトには…が含まれている","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"},"result":{"success":{"path":"/Users/user/project/summary.txt","linesCreated":19,"fileSize":942}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"result","subtype":"success","duration_ms":5234,"duration_api_ms":5234,"is_error":false,"result":"README.mdファイルを読んで要約を作成する","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","request_id":"10e11780-df2f-45dc-a1ff-4540af32e9c0"}
```

<div id="text-format">
  ## テキスト形式
</div>

`text` 出力形式は、エージェントの動作を人間が読みやすいシンプルなストリームで提供する。詳細な JSON イベントではなく、エージェントがリアルタイムで何をしているかを簡潔なテキストで記述して出力する。

この形式は、構造化データのパースによるオーバーヘッドなしでエージェントの進捗を監視できるため、ログ記録、デバッグ、シンプルな進捗トラッキングに最適。

<div id="example-output">
  ### 出力例
</div>

```
ファイルを読み込んだ
ファイルを編集した
ターミナルコマンドを実行した
新規ファイルを作成した
```

エージェントがアクションを実行するたびに、それぞれが新しい行に表示され、タスクの進行状況に関する即時のフィードバックが得られる。

<div id="implementation-notes">
  ## 実装メモ
</div>

* 各イベントは `\n` で終端される単一行として出力される
* `thinking` イベントはプリントモードでは抑止され、いずれの出力形式にも含まれない
* フィールドの追加は後方互換性を保つ形で段階的に行われる可能性がある（コンシューマは未知のフィールドを無視すること）
* ストリーム形式はリアルタイムに更新を提供し、JSON 形式は完了まで待機してから結果を出力する
* 完全なレスポンスを再構成するには、すべての `assistant` メッセージのデルタを連結する
* ツール呼び出し ID は開始/完了イベントの相関付けに使用できる
* セッション ID は単一のエージェント実行全体を通して一貫して維持される



# パラメータ
Source: https://docs.cursor.com/ja/cli/reference/parameters

Cursor Agent CLI のコマンド完全リファレンス

<div id="global-options">
  ## グローバルオプション
</div>

グローバルオプションはどのコマンドでも使える:

<div class="full-width-table">
  | オプション                      | 説明                                                                             |
  | -------------------------- | ------------------------------------------------------------------------------ |
  | `-v, --version`            | バージョン番号を出力                                                                     |
  | `-a, --api-key <key>`      | 認証用の API キー（`CURSOR_API_KEY` 環境変数も利用可）                                         |
  | `-p, --print`              | レスポンスをコンソールに出力（スクリプトや非対話利用向け）。write や bash を含む全ツールにアクセス可能。                     |
  | `--output-format <format>` | 出力形式（`--print` のときのみ有効）: `text`、`json`、または `stream-json`（デフォルト: `stream-json`） |
  | `-b, --background`         | バックグラウンドモードで起動（起動時に composer ピッカーを開く）                                          |
  | `--fullscreen`             | フルスクリーンモードを有効化                                                                 |
  | `--resume [chatId]`        | チャットセッションを再開                                                                   |
  | `-m, --model <model>`      | 使用するモデル                                                                        |
  | `-f, --force`              | 明示的に拒否されない限りコマンドを強制的に許可                                                        |
  | `-h, --help`               | コマンドのヘルプを表示                                                                    |
</div>

<div id="commands">
  ## コマンド
</div>

<div class="full-width-table">
  | Command           | Description                    | Usage                                           |
  | ----------------- | ------------------------------ | ----------------------------------------------- |
  | `login`           | Cursor にサインインする                | `cursor-agent login`                            |
  | `logout`          | サインアウトし、保存済みの認証情報をクリアする        | `cursor-agent logout`                           |
  | `status`          | 認証状態を確認する                      | `cursor-agent status`                           |
  | `mcp`             | MCP サーバーを管理する                  | `cursor-agent mcp`                              |
  | `update\|upgrade` | Cursor Agent を最新バージョンにアップデートする | `cursor-agent update` or `cursor-agent upgrade` |
  | `ls`              | チャットセッションの一覧を表示する              | `cursor-agent ls`                               |
  | `resume`          | 直近のチャットセッションを再開する              | `cursor-agent resume`                           |
  | `help [command]`  | コマンドのヘルプを表示する                  | `cursor-agent help [command]`                   |
</div>

<Note>
  コマンドを指定しない場合、Cursor Agent はデフォルトでインタラクティブなチャットモードで起動する。
</Note>

<div id="mcp">
  ## MCP
</div>

Cursor Agent に設定されている MCP サーバーを管理する。

<div class="full-width-table">
  | Subcommand                | Description                             | Usage                                      |
  | ------------------------- | --------------------------------------- | ------------------------------------------ |
  | `login <identifier>`      | `.cursor/mcp.json` に設定された MCP サーバーに認証する | `cursor-agent mcp login <identifier>`      |
  | `list`                    | 設定済みの MCP サーバーとそのステータスを一覧表示する           | `cursor-agent mcp list`                    |
  | `list-tools <identifier>` | 指定した MCP の利用可能なツールとその引数名を一覧表示する         | `cursor-agent mcp list-tools <identifier>` |
</div>

すべての MCP コマンドで、コマンド専用のヘルプとして `-h, --help` が使える。

<div id="arguments">
  ## 引数
</div>

チャットモードで起動する場合（デフォルト）、初期プロンプトを指定できる:

**引数:**

* `prompt` — エージェントの初期プロンプト

<div id="getting-help">
  ## ヘルプの入手
</div>

すべてのコマンドは、コマンドごとのヘルプを表示できるグローバルな `-h, --help` オプションに対応してる。



# 権限
Source: https://docs.cursor.com/ja/cli/reference/permissions

ファイルとコマンドへのエージェントのアクセスを制御するための権限タイプ

CLI 設定でパーミッショントークンを使って、エージェントに許可する操作を指定しよう。権限は `~/.cursor/cli-config.json`（グローバル）または `<project>/.cursor/cli.json`（プロジェクト固有）で設定する。

<div id="permission-types">
  ## 権限の種類
</div>

<div id="shell-commands">
  ### シェルコマンド
</div>

**形式:** `Shell(commandBase)`

シェルコマンドへのアクセスを制御する。`commandBase` はコマンドラインの先頭トークン。

<div class="full-width-table">
  | 例            | 説明                            |
  | ------------ | ----------------------------- |
  | `Shell(ls)`  | `ls` コマンドの実行を許可               |
  | `Shell(git)` | 任意の `git` サブコマンドを許可           |
  | `Shell(npm)` | npm パッケージマネージャーのコマンドを許可       |
  | `Shell(rm)`  | 破壊的なファイル削除を拒否（一般に `deny` で指定） |
</div>

<div id="file-reads">
  ### ファイルの読み取り
</div>

**形式:** `Read(pathOrGlob)`

ファイルおよびディレクトリの読み取りアクセスを制御する。glob パターンをサポート。

<div class="full-width-table">
  | 例                   | 説明                               |
  | ------------------- | -------------------------------- |
  | `Read(src/**/*.ts)` | `src` 内の TypeScript ファイルの読み取りを許可 |
  | `Read(**/*.md)`     | 任意の場所の Markdown ファイルの読み取りを許可     |
  | `Read(.env*)`       | 環境ファイルの読み取りを拒否                   |
  | `Read(/etc/passwd)` | システムファイルの読み取りを拒否                 |
</div>

<div id="file-writes">
  ### ファイルの書き込み
</div>

**形式:** `Write(pathOrGlob)`

ファイルおよびディレクトリの書き込みアクセスを制御する。glob パターンをサポート。print モードで使用する場合、ファイルを書き込むには `--force` が必要。

<div class="full-width-table">
  | 例                     | 説明                        |
  | --------------------- | ------------------------- |
  | `Write(src/**)`       | `src` 配下の任意のファイルへの書き込みを許可 |
  | `Write(package.json)` | package.json の変更を許可       |
  | `Write(**/*.key)`     | 秘密鍵ファイルへの書き込みを拒否          |
  | `Write(**/.env*)`     | 環境ファイルへの書き込みを拒否           |
</div>

<div id="configuration">
  ## 設定
</div>

CLI の設定ファイル内の `permissions` オブジェクトにパーミッションを追加しよう:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)", 
      "Read(src/**/*.ts)",
      "Write(package.json)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  }
}
```

<div id="pattern-matching">
  ## パターンマッチング
</div>

* Glob パターンでは `**`、`*`、`?` のワイルドカードを使う
* 相対パスはカレントワークスペースがスコープ
* 絶対パスはプロジェクト外のファイルも対象にできる
* 拒否ルールが許可ルールより優先される



# スラッシュコマンド
Source: https://docs.cursor.com/ja/cli/reference/slash-commands

Cursor CLI セッションで使えるクイックアクション

<div class="full-width-table">
  | Command               | Description                                |
  | --------------------- | ------------------------------------------ |
  | `/model <model>`      | モデルを設定／一覧表示                                |
  | `/auto-run [state]`   | 自動実行を切り替え（デフォルト）または \[on\|off\|status] を指定 |
  | `/new-chat`           | 新しいチャットセッションを開始                            |
  | `/vim`                | Vim キーバインドを切り替え                            |
  | `/help [command]`     | ヘルプを表示（/help \[cmd]）                       |
  | `/feedback <message>` | チームにフィードバックを送信                             |
  | `/resume <chat>`      | フォルダー名で以前のチャットを再開                          |
  | `/copy-req-id`        | 直近のリクエスト ID をコピー                           |
  | `/logout`             | Cursor からサインアウト                            |
  | `/quit`               | 終了                                         |
</div>



# シェルモード
Source: https://docs.cursor.com/ja/cli/shell-mode

会話を中断せずに、CLIから直接シェルコマンドを実行

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Shell Mode は、会話を離れずに CLI からシェルコマンドを直接実行できる。安全チェック付きで、結果が会話内に表示される、短時間で非対話型のコマンドに使おう。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

<div id="command-execution">
  ## コマンド実行
</div>

コマンドはログインシェル（`$SHELL`）で、CLI のカレントディレクトリと環境を使って実行される。別のディレクトリで実行したい場合は、コマンドを組み合わせて実行してね:

```bash  theme={null}
cd subdir && npm test
```

<div id="output">
  ## 出力
</div>

<product_visual type="screenshot">
  コマンド出力のスクリーンショット。終了コードを示すヘッダー、stdout/stderr の表示、出力の省略（トランケーション）操作を含む
</product_visual>

出力が大きい場合は自動的に省略され、長時間実行するプロセスはパフォーマンス維持のためタイムアウトする。

<div id="limitations">
  ## 制限事項
</div>

* コマンドは30秒でタイムアウトする
* 長時間実行のプロセス、サーバー、対話的なプロンプトには非対応
* ベストな結果のために、短くて非対話的なコマンドを使ってね

<div id="permissions">
  ## 権限
</div>

コマンドは実行前に、権限とチーム設定に基づいてチェックされる。詳細な設定は [Permissions](/ja/cli/reference/permissions) を参照してね。

<product_visual type="screenshot">
  承認オプションを示す決定バナー: Run、Reject/Propose、Allowlist に追加、Auto-run
</product_visual>

管理者ポリシーによって特定のコマンドがブロックされる場合があり、リダイレクトを伴うコマンドはインラインで allowlist に追加できない。

<div id="usage-guidelines">
  ## 使用ガイドライン
</div>

Shell Mode は、ステータス確認、素早いビルド、ファイル操作、環境の確認に向いてる。

長時間動かすサーバーや対話型アプリ、入力が必要なコマンドは避けて。

各コマンドは独立して実行される — 別ディレクトリで実行したい場合は `cd <dir> && ...` を使って。

<div id="troubleshooting">
  ## トラブルシューティング
</div>

* コマンドが固まったら、<Kbd>Ctrl+C</Kbd>で中断して非対話オプションを追加してみて
* 権限を求められたら、1回だけ承認するか、<Kbd>Tab</Kbd>で許可リストに追加して
* 出力が途中で切れる場合は、<Kbd>Ctrl+O</Kbd>で展開して
* 別ディレクトリで実行したいときは、変更が保持されないので `cd <dir> && ...` を使って
* Shell Mode は `$SHELL` 変数に基づき zsh と bash をサポートしてる

<div id="faq">
  ## よくある質問
</div>

<AccordionGroup>
  <Accordion title="`cd` の状態は実行ごとに引き継がれる？">
    いいえ。各コマンドは独立して実行される。別ディレクトリでコマンドを実行するなら、`cd <dir> && ...` を使って。
  </Accordion>

  <Accordion title="タイムアウトは変更できる？">
    いいえ。コマンドの実行時間は 30 秒に制限されており、変更はできない。
  </Accordion>

  <Accordion title="権限はどこで設定する？">
    権限は CLI とチーム設定で管理される。許可リストにコマンドを追加するには、意思決定バナーを使って。
  </Accordion>

  <Accordion title="Shell Mode を終了するには？">
    入力が空のときに <Kbd>Escape</Kbd>、入力が空の状態で <Kbd>Backspace</Kbd>/<Kbd>Delete</Kbd>、または <Kbd>Ctrl+C</Kbd> でクリアして終了。
  </Accordion>
</AccordionGroup>



# CLI で Agent を使う
Source: https://docs.cursor.com/ja/cli/using

Cursor CLI でプロンプト、レビュー、反復を効率よく行う

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="prompting">
  ## プロンプト設計
</div>

最良の結果を得るには、意図をはっきり伝えるのがオススメ。たとえば、エージェントにファイルを一切編集させたくないなら、「do not write any code」というプロンプトを使えばOK。これは、実装に入る前にタスクを計画するときに特に役立つ。

エージェントは現在、ファイル操作・検索・シェルコマンド実行のツールを備えてる。IDE エージェントと同様に、今後さらに多くのツールが追加されていく。

<div id="mcp">
  ## MCP
</div>

Agent は拡張機能や統合のために [MCP（Model Context Protocol）](/ja/tools/mcp) をサポートしてる。CLI は `mcp.json` の設定ファイルを自動検出して反映し、IDE で設定したのと同じ MCP サーバーとツールを有効にする。

<div id="rules">
  ## ルール
</div>

CLI エージェントは IDE と同じ[ルールシステム](/ja/context/rules)に対応してる。.cursor/rules ディレクトリにルールを作成して、エージェントにコンテキストとガイダンスを与えよう。これらのルールは設定に基づいて自動的に読み込まれて適用されるから、プロジェクトの異なる部分や特定のファイルタイプごとにエージェントの挙動をカスタマイズできる。

<Note>
  CLI は、（存在する場合）プロジェクトルートにある `AGENTS.md` と `CLAUDE.md` も読み込み、`.cursor/rules` とあわせてルールとして適用する。
</Note>

<div id="working-with-agent">
  ## Agent の使い方
</div>

<div id="navigation">
  ### ナビゲーション
</div>

前のメッセージは上矢印（<Kbd>ArrowUp</Kbd>）で呼び出せて、順番に遡れる。

<div id="review">
  ### レビュー
</div>

<Kbd>Cmd+R</Kbd> で変更内容をレビュー。<Kbd>i</Kbd> を押して追加入力を追加。スクロールは <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd>、ファイル切り替えは <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd>。

<div id="selecting-context">
  ### コンテキストの選択
</div>

<Kbd>@</Kbd> でコンテキストに含めるファイルやフォルダを選択。`/compress` を実行してコンテキストウィンドウの空きスペースを確保。詳しくは [Summarization](/ja/agent/chat/summarization) を参照。

<div id="history">
  ## 履歴
</div>

既存のスレッドから続けるには、`--resume [thread id]` でこれまでのコンテキストを読み込む。

直近の会話を再開するなら、`cursor-agent resume` を使う。

これまでの会話の一覧を見たいときは、`cursor-agent ls` を実行する。

<div id="command-approval">
  ## コマンドの承認
</div>

ターミナルコマンドを実行する前に、CLI が実行の可否を確認するよ。承認するなら (<Kbd>y</Kbd>)、拒否するなら (<Kbd>n</Kbd>) を押してね。

<div id="non-interactive-mode">
  ## 非インタラクティブモード
</div>

`-p` または `--print` を使って Agent を非インタラクティブモードで実行する。レスポンスがコンソールに出力される。

非インタラクティブモードでは、対話なしで Agent を呼び出せる。これにより、スクリプトや CI パイプラインなどに組み込める。

`--output-format` を併用すると、出力形式を制御できる。たとえば、スクリプトでパースしやすい構造化出力には `--output-format json`、プレーンテキスト出力には `--output-format text` を使う。

<Note>
  非インタラクティブモードでは、Cursor はフルの書き込み権限を持つ。
</Note>



# キーボードショートカット
Source: https://docs.cursor.com/ja/configuration/kbd

Cursor のキーボードショートカットとキーバインディング

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Cursor のキーボードショートカットの概要。すべてのキーボードショートカットは、<Kbd>Cmd R</Kbd> を押してから <Kbd>Cmd S</Kbd>、またはコマンドパレット <Kbd>Cmd Shift P</Kbd> を開いて `Keyboard Shortcuts` を検索すると確認できるよ。

Cursor のキーボードショートカットについては、Cursor のキーバインドの基準として [Key Bindings for VS Code](https://code.visualstudio.com/docs/getstarted/keybindings) を参考にするとさらに理解が深まるよ。

Cursor 固有の機能を含むすべての Cursor のキーバインドは、「Keyboard Shortcuts」の設定でリマップできるよ。

<div id="general">
  ## 全般
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut               | Action                        |
  | ---------------------- | ----------------------------- |
  | <Kbd>Cmd I</Kbd>       | サイドパネルを切り替え（モードに割り当てられていない場合） |
  | <Kbd>Cmd L</Kbd>       | サイドパネルを切り替え（モードに割り当てられていない場合） |
  | <Kbd>Cmd E</Kbd>       | Background Agent のコントロールパネル   |
  | <Kbd>Cmd .</Kbd>       | モードメニュー                       |
  | <Kbd>Cmd /</Kbd>       | AIモデルを切り替え                    |
  | <Kbd>Cmd Shift J</Kbd> | Cursor の設定                    |
  | <Kbd>Cmd ,</Kbd>       | 共通設定                          |
  | <Kbd>Cmd Shift P</Kbd> | コマンドパレット                      |
</div>

<div id="chat">
  ## Chat
</div>

チャット入力ボックスのショートカット

<div className="full-width-table equal-table-columns">
  | Shortcut                                             | Action            |
  | ---------------------------------------------------- | ----------------- |
  | <Kbd>Return</Kbd>                                    | 送信（デフォルトはプレビュー送信） |
  | <Kbd>Ctrl Return</Kbd>                               | メッセージをキューに追加      |
  | <Kbd>Cmd Return</Kbd> when typing                    | 強制送信              |
  | <Kbd>Cmd Shift Backspace</Kbd>                       | 生成をキャンセル          |
  | <Kbd>Cmd Shift L</Kbd> with code selected            | 選択中のコードをコンテキストに追加 |
  | <Kbd>Cmd V</Kbd> with code or log in clipboard       | クリップボードをコンテキストに追加 |
  | <Kbd>Cmd Shift V</Kbd> with code or log in clipboard | クリップボードを入力欄に貼り付け  |
  | <Kbd>Cmd Return</Kbd> with suggested changes         | 変更をすべて承認          |
  | <Kbd>Cmd Backspace</Kbd>                             | 変更をすべて却下          |
  | <Kbd>Tab</Kbd>                                       | 次のメッセージへ移動        |
  | <Kbd>Shift Tab</Kbd>                                 | 前のメッセージへ移動        |
  | <Kbd>Cmd Opt /</Kbd>                                 | モデルを切り替え          |
  | <Kbd>Cmd N</Kbd> / <Kbd>Cmd R</Kbd>                  | 新規チャット            |
  | <Kbd>Cmd T</Kbd>                                     | 新規チャットタブ          |
  | <Kbd>Cmd \[</Kbd>                                    | 前のチャット            |
  | <Kbd>Cmd ]</Kbd>                                     | 次のチャット            |
  | <Kbd>Cmd W</Kbd>                                     | チャットを閉じる          |
  | <Kbd>Escape</Kbd>                                    | フィールドのフォーカスを外す    |
</div>

<div id="inline-edit">
  ## インライン編集
</div>

<div className="full-width-table equal-table-columns">
  | ショートカット                        | アクション         |
  | ------------------------------ | ------------- |
  | <Kbd>Cmd K</Kbd>               | 開く            |
  | <Kbd>Cmd Shift K</Kbd>         | 入力フォーカスを切り替える |
  | <Kbd>Return</Kbd>              | 送信            |
  | <Kbd>Cmd Shift Backspace</Kbd> | キャンセル         |
  | <Kbd>Opt Return</Kbd>          | クイック質問をする     |
</div>

<div id="code-selection-context">
  ## コード選択とコンテキスト
</div>

<div className="full-width-table equal-table-columns">
  | ショートカット                                         | アクション                               |
  | ----------------------------------------------- | ----------------------------------- |
  | <Kbd>@</Kbd>                                    | [@-symbols](/ja/context/@-symbols/) |
  | <Kbd>#</Kbd>                                    | ファイル                                |
  | <Kbd>/</Kbd>                                    | ショートカットコマンド                         |
  | <Kbd>Cmd Shift L</Kbd>                          | 選択範囲をChatに追加                        |
  | <Kbd>Cmd Shift K</Kbd>                          | 選択範囲をEditに追加                        |
  | <Kbd>Cmd L</Kbd>                                | 選択範囲を新しいChatに追加                     |
  | <Kbd>Cmd M</Kbd>                                | ファイル読み取り戦略を切り替え                     |
  | <Kbd>Cmd →</Kbd>                                | 提案の次の単語を確定                          |
  | <Kbd>Cmd Return</Kbd>                           | Chatでコードベースを検索                      |
  | コードを選択し、<Kbd>Cmd C</Kbd>、<Kbd>Cmd V</Kbd>       | コピーした参照コードをコンテキストとして追加              |
  | コードを選択し、<Kbd>Cmd C</Kbd>、<Kbd>Cmd Shift V</Kbd> | コピーしたコードをテキストとしてコンテキストに追加           |
</div>

<div id="tab">
  ## Tab
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut         | Action     |
  | ---------------- | ---------- |
  | <Kbd>Tab</Kbd>   | 提案を受け入れる   |
  | <Kbd>Cmd →</Kbd> | 次の単語を受け入れる |
</div>

<div id="terminal">
  ## ターミナル
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut              | Action           |
  | --------------------- | ---------------- |
  | <Kbd>Cmd K</Kbd>      | ターミナルのプロンプトバーを開く |
  | <Kbd>Cmd Return</Kbd> | 生成コマンドを実行する      |
  | <Kbd>Escape</Kbd>     | コマンドを確定する        |
</div>



# シェルコマンド
Source: https://docs.cursor.com/ja/configuration/shell

Cursor のシェルコマンドをインストールして使用する

Cursor は、ターミナルからファイルやフォルダーを開けるコマンドラインツールを提供している。開発ワークフローに Cursor を統合するために、`cursor` と `code` の両コマンドをインストールしてね。

<div id="installing-cli-commands">
  ## CLI コマンドのインストール
</div>

Command Palette から CLI コマンドをインストールする:

1. Command Palette を開く（Cmd/Ctrl + P）
2. 「Install」と入力してインストール関連のコマンドに絞り込む
3. `Install 'cursor' to shell` を選択して実行
4. 同様に `Install 'code' to shell` を選択

<product_visual type="screenshot">
  CLI のインストールオプションを表示している Command Palette
</product_visual>

<div id="using-the-cli-commands">
  ## CLI コマンドの使い方
</div>

インストール後は、次のどちらかのコマンドで Cursor でファイルやフォルダを開ける:

```bash  theme={null}

# cursor コマンドの使用
cursor path/to/file.js
cursor path/to/folder/


# code コマンドの使用（VS Code 互換）
code path/to/file.js
code path/to/folder/
```

<div id="command-options">
  ## コマンドオプション
</div>

どちらのコマンドも次のオプションに対応してる:

* ファイルを開く: `cursor file.js`
* フォルダを開く: `cursor ./my-project`
* 複数の項目を開く: `cursor file1.js file2.js folder1/`
* 新しいウィンドウで開く: `cursor -n` または `cursor --new-window`
* ウィンドウが閉じるまで待つ: `cursor -w` または `cursor --wait`

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="cursor と code コマンドの違いは？">
    同じだよ。`code` コマンドは VS Code との互換性のために提供されてる。
  </Accordion>

  <Accordion title="両方のコマンドをインストールする必要ある？">
    ないよ。好みに合わせて片方だけでも両方でもインストールしてOK。
  </Accordion>

  <Accordion title="コマンドはどこにインストールされるの？">
    コマンドはシステムのデフォルトのシェル設定ファイル（例: `.bashrc`、`.zshrc`、`.config/fish/config.fish`）に追加されるよ。
  </Accordion>
</AccordionGroup>



# テーマ
Source: https://docs.cursor.com/ja/configuration/themes

Cursor の外観をカスタマイズ

Cursor は、コーディング環境でライトテーマとダークテーマの両方に対応してる。VS Code のテーマ機能を引き継いでいて、任意の VS Code テーマを使ったり、カスタムテーマを作成したり、マーケットプレイスからテーマ拡張をインストールできる。

<div id="changing-theme">
  ## テーマの変更
</div>

1. Command Palette を開く（Cmd/Ctrl + P）
2. コマンドを絞り込むために「theme」と入力
3. 「Preferences: Color Theme」を選択
4. テーマを選択

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de83bbba983509af2002e4dfafe703ff" alt="Cursor のテーマ選択メニューで利用可能なカラーテーマを表示" data-og-width="3584" width="3584" data-og-height="2072" height="2072" data-path="images/config/themes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=85b365baa01a725becb482e69eed6292 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=46eb0bed7d0d98612968135d727ee838 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8629851793f4498e7639ee4347484c88 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ea75113e217cc84f99f8f6d63af34ade 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ec5b85b5a4464d2af801f92b317a7e31 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=54fc29efe263f9935ba3273675ced7be 2500w" />
</Frame>

<div id="faq">
  ## よくある質問
</div>

<AccordionGroup>
  <Accordion title="VS Code のテーマは Cursor で使える？">
    使えるよ！Cursor は VS Code のテーマと互換性がある。VS Code Marketplace のテーマをインストールするか、カスタムのテーマファイルをコピーして使ってね。
  </Accordion>

  <Accordion title="カスタムテーマはどう作る？">
    VS Code と同じ手順でカスタムテーマを作れる。今の設定から始めたい場合は "Developer: Generate Color Theme From Current Settings" を使うか、VS Code のテーマ作成ガイドに従ってね。
  </Accordion>
</AccordionGroup>



# @Code
Source: https://docs.cursor.com/ja/context/@-symbols/@-code

Cursor で @Code を使って特定のコードスニペットを参照する

`@Code` シンボルで特定のコードセクションを参照できる。[`@Files & Folders`](/ja/context/@-symbols/@-files-and-folders)よりも細かくコントロールでき、ファイル全体ではなくピンポイントのコードスニペットを選択できる。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fba3d385441084e243cd168eee8c9a9a" data-og-width="1850" width="1850" data-og-height="948" height="948" data-path="images/context/symbols/@-code.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6337ef4855301fdfef729012783d3cee 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ef348ae46e4a51ee298a6a5fa356eebd 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=40ec3857dd21120790037ea409fac80d 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=604bfeb6907e96da64b1f814681232c8 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=cee1a79d449a4d163f566a6013b69318 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d4bb99b85dfa5ad539e63c3670171abe 2500w" />
</Frame>



# @Cursor ルール
Source: https://docs.cursor.com/ja/context/@-symbols/@-cursor-rules

プロジェクト固有のルールとガイドラインを適用

`@Cursor Rules` シンボルを使うと、設定済みの[プロジェクトルール](/ja/context/rules)とガイドラインにアクセスして、コンテキストに明示的に適用できるよ。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e2f45682a0b471e5726cd5452ab6bceb" data-og-width="1518" width="1518" data-og-height="973" height="973" data-path="images/context/symbols/@-rules.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6e67889ef0390f9be3c557247469c95b 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1c22061fe8c8d000deeabbf404f1650d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a220fd7fbef492c2d523ed9e31324666 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44224ba38fd2a5460963b884c994d178 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=df766d5499d8b54ca4fa2211600515f6 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a06393ddd0d85711ad72d7b8991946a5 2500w" />
</Frame>



# @Files & Folders
Source: https://docs.cursor.com/ja/context/@-symbols/@-files-and-folders

Chat と Inline Edit でコンテキストとしてファイルやフォルダーを参照

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="files">
  ## Files
</div>

Chat と Inline Edit でファイル全体を参照するには、検索したいファイル名を `@Files & Folders` から選んで指定する。サイドバーから Agent にファイルを直接ドラッグして、コンテキストとして追加することもできる。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8d46d3c961a3e898fd12c0cc1e1c8dce" data-og-width="2227" width="2227" data-og-height="1414" height="1414" data-path="images/context/symbols/@-files-folders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a3a78c7a6d2311a31efb941c40fbe11b 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bfe1eff4516dce93f789e560e92f14ad 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=462239ebfd0181acfe36d2f937f32ca6 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1a64cd3cc0a07825c51d70c40dfe72fd 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=64ea129f283dd98fd9814820d6684a99 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b40e591d3e500f06eeb32fac49d4f90c 2500w" />
</Frame>

<div id="folders">
  ## フォルダ
</div>

`@Folders` でフォルダを参照すると、Cursor はフォルダパスと内容の概要を渡して、AI が利用可能なリソースを把握できるようにするよ。

<Tip>
  フォルダを選んだら `/` を入力して、さらに深い階層へ移動し、すべてのサブフォルダを表示できるよ。
</Tip>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9a102e1c1cb7180c3ec6a1356273839a" data-og-width="2150" width="2150" data-og-height="1367" height="1367" data-path="images/context/symbols/@-folders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4b91de3b118c842aec8e1da04ca233d2 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fcba40013ff1349c28382151b52d5853 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=83cc5ac8db19a0d59de9a980c0ea10d7 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b87a80a369b62d48a2363a97a391de2 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29e93d39857f71ba7e00947e209514de 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=aa9b88463b43fa482c0654a0a0b362ca 2500w" />
</Frame>

<div id="full-folder-content">
  ### フルフォルダコンテンツ
</div>

設定で **Full Folder Content** を有効にしよう。有効にすると、Cursor はそのフォルダ内のすべてのファイルをコンテキストに含めようとする。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ee37944a2e874a708b9d8281a063e580" data-og-width="1996" width="1996" data-og-height="296" height="296" data-path="images/context/symbols/folder-setting.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=09520107c0518601c58f099ed119adab 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=748aecb97c43066f0be03416f9ed6ed0 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fd7e7c816092c9eed3182382fa77ff8f 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=91baab4860e0f671196607f3c364b4d8 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d2450ee2fcd6d8c59ba2412fad11121 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f4690bdb099c27092b9ddb6143bd8068 2500w" />
</Frame>

コンテキストウィンドウを超える大きなフォルダでは、アウトラインビューが表示され、ツールチップに含められたファイル数が表示される。Cursor が利用可能なコンテキスト領域を自動で調整するよ。

<Note>
  [Max mode enabled](/ja/context/max-mode) と併用すると、
  入力トークンが増えるぶんリクエストコストが大きくなるよ。
</Note>

<div id="context-management">
  ## コンテキスト管理
</div>

大きなファイルやフォルダは、コンテキスト上限に収まるよう自動的に要約される。詳しくは [file & folder condensation](/ja/agent/chats/summarization#file--folder-condensation) を参照。



# @Git
Source: https://docs.cursor.com/ja/context/@-symbols/@-git

Git の変更点とブランチ差分を参照

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=dba4c696d66e1274b96bf3261c8d927b" data-og-width="1658" width="1658" data-og-height="932" height="932" data-path="images/context/symbols/@-git.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=69bf90d13f034275fb78ab48e71d25ac 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e8c89a03ebdd5a1c1a576c8555380957 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5ec7309f9ec4364c4ac0d237a9977f23 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f2d82f1eb2be6275c8b91ae63e943ee7 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4e27a0a13a731fc0fe85a85a327f9884 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=aa1acf93e5e87b7a81d766a52601960d 2500w" />
</Frame>

* `@Commit`: 直前のコミットと比較した現在の作業ツリーの変更を参照。コミット前の変更・追加・削除ファイルをすべて表示。
* `@Branch`: 今いるブランチの変更を main ブランチと比較。自分のブランチにあって main にはないコミットと変更をすべて表示。



# @Link
Source: https://docs.cursor.com/ja/context/@-symbols/@-link

URL を貼り付けてウェブコンテンツを取り込む

Chat に URL を貼り付けると、Cursor が自動で `@Link` としてタグ付けし、コンテキストに使うための内容を取得する。PDF にも対応していて、公開アクセス可能な PDF の URL からテキストを抽出・解析できる。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d96b384a0480aba7981b6fbebee1fac8" data-og-width="1618" width="1618" data-og-height="1035" height="1035" data-path="images/context/symbols/@-link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d251326cc25b2835488b1f25b05f2c4f 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d1b64f393d89cfc547c6e12ae7a6adef 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d5a2aa41c6a6affea03379adac5e76c8 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e94e2c0610eafea625996386374e8898 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=404333e65fa1c98e2e92fd941d2e8b92 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=63d9a66571fde75678b6fa0d0cbac44f 2500w" />
</Frame>

<div id="unlink">
  ## リンク解除
</div>

URL の内容を取得せず、プレーンテキストとして使うには:

* タグ付きのリンクをクリックして `Unlink` を選ぶ
* または、自動タグ付けを防ぐために `Shift` を押しながら貼り付ける

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5eca9b93aa4c2ba4f8d0f6a97a34052f" data-og-width="1212" width="1212" data-og-height="408" height="408" data-path="images/context/symbols/@-link-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=be5f171437d0d3c79ded195c7a387741 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5ca29084e45c832b6aa9015fcd5cf680 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=eb394772d364e392ff794c43ed1fbfcc 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5df343df91b3bf4aed9edb32fc192059 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a35df3274c439984b2072eb758d05fb1 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a20f166b838435ade65084c844cc3c6a 2500w" />
</Frame>



# @Linter Errors
Source: https://docs.cursor.com/ja/context/@-symbols/@-linter-errors

コードベース内のリンティングエラーにアクセスして参照する

`@Linter Errors` シンボルは、現在アクティブなファイルのリンティングエラーや警告を自動取得し、そのコンテキストを提供する。[Agent](/ja/agent/overview) はデフォルトで lint エラーを参照できる。

<Note>
  linter のエラーを表示するには、使用しているプログラミング言語に対応した
  Language Server をインストールして適切に設定しておく必要がある。Cursor は
  インストール済みの Language Server を自動検出して使用するけど、特定の言語では
  追加の拡張機能やツールのインストールが必要になる場合がある。
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6ef34b3ae96a7d49695035cb5c3ac9f9" data-og-width="1590" width="1590" data-og-height="1017" height="1017" data-path="images/context/symbols/@-linter-errors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=13e682f26536e5cb104142bcc7becbeb 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=cf3947376ee2e17f83c08809b23e864c 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=13d026063f9bc5e61c78740fee8eebc5 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29c834609d2f549b295be53cdbf7eec6 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b2131adda5b89685d7d7a26ed218fee 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9cd3c3e34cbee0f73fe478024018539 2500w" />
</Frame>



# @Past Chats
Source: https://docs.cursor.com/ja/context/@-symbols/@-past-chats

履歴のチャット要約をコンテキストに含める

複雑なタスクを[Chat](/ja/chat)で進めてると、過去の会話のコンテキストや判断を参照したくなることがあるよね。`@Past Chats` シンボルは、過去のチャットを要約してコンテキストに含めてくれる。

とくに便利な場面:

* 参照したい重要なコンテキストを含む長い Chat セッションがあるとき
* 関連する新しいタスクを始めるときに、前後のつながりを保ちたいとき
* 前のセッションの考え方や判断を共有したいとき

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6839cf571e64e1ed10dd5dc270d4ac45" data-og-width="2340" width="2340" data-og-height="1485" height="1485" data-path="images/context/symbols/@-past-chats.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0278e6fdce8d8771ecd6f64faf5048db 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3a2d4722e90c1078c11fcd695993d84a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d46e21680b56820aef7a9baf34891e0 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f19f25e6988729059f40731378ce4fab 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=86f9457d09e7dd4578c8609fd3cff6b5 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8efb9e097f9e434d0b7f03cac9b02396 2500w" />
</Frame>



# @Recent Changes
Source: https://docs.cursor.com/ja/context/@-symbols/@-recent-changes

最近の変更コードをコンテキストに含める

`@Recent Changes` シンボルは、AI との会話で最近のコード変更をコンテキストとして取り込む。

* 変更は時系列順に並ぶ
* 直近の10件を優先
* `.cursorignore` の設定を遵守

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e6968afeeed9e790121d8280f63b670d" data-og-width="1556" width="1556" data-og-height="996" height="996" data-path="images/context/symbols/@-recent-changes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=beae76f109d8eb29788ab3c90f72b831 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c4e6ad386c30f9546e1485ca4c14c0f2 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7d80d31e720b167408cd308204fa666a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=868a93753377dcb2d6820c748b9b17d7 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e84e94c4fe64f9e4270fd72883a4962d 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=139ffc703716759bb8b8c35e57bd6dbf 2500w" />
</Frame>



# @Web
Source: https://docs.cursor.com/ja/context/@-symbols/@-web

最新情報をウェブで検索

`@Web` を使うと、Cursor は [exa.ai](https://exa.ai) を用いて最新の情報をウェブから検索し、コンテキストとして追加する。これには、直接リンクの PDF を解析する機能も含まれる。

<Note>
  ウェブ検索はデフォルトでオフ。Settings → Features → Web Search でオンにしてね。
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=17621610c12478f27190b96db57ca8de" data-og-width="1700" width="1700" data-og-height="1085" height="1085" data-path="images/context/symbols/@-web.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1be39cb8bbbfa22f2341635e7c5fe6d0 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=40b6aac5bee79bb5656024077bee7ece 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9a8515d8c9c5624135665a9545de32db 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8c7b721901f8cb82d39458ed054ee946 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=255c56da352f6faff0d92cf24f7dabb2 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=22561389d116bcbe01f5a860c0097b27 2500w" />
</Frame>



# 概要
Source: https://docs.cursor.com/ja/context/@-symbols/overview

@ 記号でコード、ファイル、ドキュメントを参照する

矢印キーで候補を移動、`Enter` で選択。候補が `Files` などのカテゴリなら、そのカテゴリ内の最も関連性の高い項目にフィルタされる。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=98029d0ecb83175a496ef16ccb1c92d7" data-og-width="1230" width="1230" data-og-height="794" height="794" data-path="images/context/symbols/context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=edadefb46f31037df216bdc41ff65f0e 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a0e30bf50ab5525b72b23d5d9847c7f8 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=903ab32cc5460a6573deef144b445945 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8820522f1a505b3205c0ffc2a3f1a382 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b46b89fa6da137cea339ed94eb711b3c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2e9ff863747cbf6faa2b675d400a7f6e 2500w" />
</Frame>

使える @ 記号の一覧:

* [@Files](/ja/context/@-symbols/@-files) - プロジェクト内の特定のファイルを参照
* [@Folders](/ja/context/@-symbols/@-folders) - より広いコンテキストのためにフォルダ全体を参照
* [@Code](/ja/context/@-symbols/@-code) - コードベース内の特定のコードスニペットやシンボルを参照
* [@Docs](/ja/context/@-symbols/@-docs) - ドキュメントやガイドにアクセス
* [@Git](/ja/context/@-symbols/@-git) - Git の履歴と変更にアクセス
* [@Past Chats](/ja/context/@-symbols/@-past-chats) - 要約済みの Composer セッションで作業
* [@Cursor Rules](/ja/context/@-symbols/@-cursor-rules) - Cursor ルールで作業
* [@Web](/ja/context/@-symbols/@-web) - 外部のウェブリソースやドキュメントを参照
* [@Link (paste)](/ja/context/@-symbols/@-link) - 特定のコードやドキュメントへのリンクを作成
* [@Recent Changes](/ja/context/@-symbols/@-recent-changes) - 直近の変更を参照
* [@Lint Errors](/ja/context/@-symbols/@-lint-errors) - lint エラーを参照（[Chat](/ja/chat/overview) のみ）
* [@Definitions](/ja/context/@-symbols/@-definitions) - シンボル定義を検索（[Inline Edit](/ja/inline-edit/overview) のみ）
* [# Files](/ja/context/@-symbols/pill-files) - 参照せずにファイルをコンテキストに追加
* [/ Commands](/ja/context/@-symbols/slash-commands) - 開いている/アクティブなファイルをコンテキストに追加



# #Files
Source: https://docs.cursor.com/ja/context/@-symbols/pill-files


# プレフィックスで特定のファイルを選択

特定のファイルに絞りたいときは、`#` の後にファイル名を続けて入力しよう。より正確にコンテキストを制御したい場合は、`@` 記号と組み合わせて使おう。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=398736830d51713f6d6624461e6ef676" alt="# file picker" data-og-width="1999" width="1999" data-og-height="1271" height="1271" data-path="images/context/symbols/pill-files.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=33af09f18a1b7a5fe3ba0b4e93549071 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d319809654c16625c4de82f2aeee7c4c 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5caee0c1350068f46f863e9ca95c0d3f 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2e12a692efce4423fe0bd9b8a955f84a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=eeb6db065f3cc70e660c91e8e9821e3a 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/pill-files.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b22bbb70e1c96f4b55e2edbf133733a9 2500w" />
</Frame>



# /command
Source: https://docs.cursor.com/ja/context/@-symbols/slash-commands

ファイル追加とコンテキスト制御のためのクイックコマンド

`/` コマンドは、開いてるエディタタブにすばやくアクセスできて、複数ファイルをコンテキストに追加できる。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d3700f8210564e99807492fbcc4053e9" alt="/ commands context" data-og-width="1714" width="1714" data-og-height="1094" height="1094" data-path="images/context/symbols/slash-command.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8c780db9f04819960d70c3bbd8a20d1f 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de3998b2f22ef72d254f77424e1e7d39 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7035008674181675bc50c9bc352499b0 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5b403646c8d1d9f6a1bc0c2f22fa8d2d 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=efbd3f3f46ced09844d39c0e99c81917 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/slash-command.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=391cc3a09397088b71213476219a763b 2500w" />
</Frame>

<div id="commands">
  ## コマンド
</div>

* **`/Reset Context`**: コンテキストをデフォルト状態にリセットする
* **`/Generate Cursor Rules`**: Cursor が従うルールを生成する
* **`/Disable Iterate on Lints`**: Linter のエラーや警告を自動修正しない
* **`/Add Open Files to Context`**: 現在開いているすべてのエディタータブをコンテキストに追加する
* **`/Add Active Files to Context`**: 現在表示中のエディタータブをコンテキストに追加する（分割レイアウトで便利）



# コードベースのインデックス化
Source: https://docs.cursor.com/ja/context/codebase-indexing

Cursor がコードベースを学習して理解を深める方法

Cursor は各ファイルに対して埋め込みを計算してコードベースをインデックス化する。これにより、コードに関する AI の回答の精度が上がる。プロジェクトを開くと、Cursor は自動でインデックス化を開始する。新規ファイルは差分で順次インデックス化される。
インデックス化の進行状況は `Cursor Settings` > `Indexing & Docs` で確認できる。

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="コードベースのインデックス化の進行状況インジケーター" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
</Frame>

<div id="configuration">
  ## 設定
</div>

Cursor は、[ignore files](/ja/context/ignore-files)（例: `.gitignore`, `.cursorignore`）に含まれるものを除き、すべてのファイルをインデックスするよ。

`Show Settings` をクリックして、次を行える:

* 新規リポジトリの自動インデックスを有効化
* 無視するファイルを設定

<Tip>
  [大容量コンテンツファイルを無視](/ja/context/ignore-files)すると、回答の精度が上がるよ。
</Tip>

<div id="view-indexed-files">
  ### インデックス済みファイルを表示
</div>

インデックス済みのファイルパスを見るには: `Cursor Settings` > `Indexing & Docs` > `View included files`

これで、インデックス対象のすべてのファイルを列挙した `.txt` ファイルが開くよ。

<div id="multi-root-workspaces">
  ## マルチルートワークスペース
</div>

Cursor は [マルチルートワークスペース](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces)をサポートしていて、複数のコードベースで作業できる:

* すべてのコードベースが自動でインデックス化される
* 各コードベースのコンテキストが AI で利用可能になる
* `.cursor/rules` はすべてのフォルダで有効

<div id="pr-search">
  ## PR search
</div>

PR search は、履歴上の変更を AI で検索・参照可能にして、コードベースの進化をつかみやすくする。

<div id="how-it-works">
  ### How it works
</div>

Cursor はリポジトリ履歴から**マージ済みの PR を自動で全件インデックス化**する。要約はセマンティック検索の結果に表示され、最新の変更を優先するスマートフィルタで絞り込める。

Agent は `@[PR number]`、`@[commit hash]`、`@[branch name]` を使って、**PR・コミット・Issue・ブランチ**をコンテキストに取り込める。GitHub 連携時は、GitHub のコメントや Bugbot のレビューも含まれる。

**対応プラットフォーム**は GitHub、GitHub Enterprise、Bitbucket。GitLab は現在非対応。

<Note>
  GitHub Enterprise のユーザーへ: VSCode の認証制約により、
  フェッチツールは git コマンドにフォールバックする。
</Note>

<div id="using-pr-search">
  ### Using PR search
</div>

「他の PR ではサービスがどう実装されてる？」みたいに聞くと、Agent が関連する PR を自動でコンテキストに取り込み、リポジトリの履歴に基づいて網羅的に答える。

<div id="faq">
  ## よくある質問
</div>

<AccordionGroup>
  <Accordion title="インデックス化されたコードベースはどこで全部見られる？">
    まだグローバルな一覧はないよ。各プロジェクトを個別に開いて、
    Cursor の Codebase Indexing の設定を確認してね。
  </Accordion>

  <Accordion title="インデックス化されたコードベースを全部削除するには？">
    Settings から Cursor アカウントを削除すれば、インデックス化されたコードベースはすべて消えるよ。
    それ以外なら、各プロジェクトの Codebase Indexing の設定から個別のコードベースを削除してね。
  </Accordion>

  <Accordion title="インデックス化されたコードベースはどれくらい保持される？">
    インデックス化されたコードベースは、6週間アクティビティがないと削除されるよ。プロジェクトを開き直すと
    再インデックスが走るよ。
  </Accordion>

  <Accordion title="ソースコードは Cursor のサーバーに保存される？">
    いいえ。Cursor はファイル名やソースコードを保存せずに埋め込み（embeddings）を作成するよ。ファイル名は難読化され、コードのチャンクは暗号化される。

    Agent がコードベースを検索するとき、Cursor はサーバーから埋め込みを取得してチャンクを復号するよ。
  </Accordion>
</AccordionGroup>



# ファイルの除外設定
Source: https://docs.cursor.com/ja/context/ignore-files

.cursorignore と .cursorindexingignore でファイルアクセスを制御

<div id="overview">
  ## 概要
</div>

Cursor はプロジェクトのコードベースを読み取り、インデックス化して各機能を提供する。ルートディレクトリの `.cursorignore` ファイルで、Cursor がアクセスできるディレクトリやファイルを制御できる。

Cursor は `.cursorignore` に記載されたファイルへのアクセスを次からブロックする:

* コードベースのインデックス化
* [Tab](/ja/tab/overview)、[Agent](/ja/agent/overview)、[Inline Edit](/ja/inline-edit/overview) から参照されるコード
* [@ シンボル参照](/ja/context/@-symbols/overview) 経由で参照されるコード

<Warning>
  Agent が起動するツール呼び出し（terminal や MCP サーバーなど）は、
  `.cursorignore` の対象となるコードへのアクセスをブロックできない
</Warning>

<div id="why-ignore-files">
  ## なんでファイルを無視するの？
</div>

**セキュリティ**: API キー、クレデンシャル、シークレットへのアクセスを制限するため。Cursor は無視対象のファイルをブロックするけど、LLM の予測不能性があるから完全な保護を保証できるわけじゃない。

**パフォーマンス**: 大規模コードベースやモノレポでは、関係ない部分を除外してインデックスを高速化し、ファイル探索の精度を上げる。

<div id="global-ignore-files">
  ## グローバルの無視ファイル
</div>

ユーザー設定で全プロジェクト共通の無視パターンを設定し、各プロジェクトでの個別設定なしに機密ファイルを除外する。

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d5bb9e6b18ca466ec69ddd1b216320c9" alt="Global Cursor Ignore List" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/settings/global-ignore.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ce566e71f1fcac6a85942f9fbb741889 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=c833cf55c470463ce31ae936ee122971 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=a3c3f6c6b40a9e91487237f0cf37cbca 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=03284fab1ddfadb64346dc912ea97048 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=5bd5b338808979f9fa42faa7df69d39a 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/settings/global-ignore.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=676448c72358de369a119b34a8dcf9c5 2500w" />
</Frame>

デフォルトのパターンには次が含まれる:

* 環境ファイル: `**/.env`, `**/.env.*`
* 認証情報: `**/credentials.json`, `**/secrets.json`
* キー: `**/*.key`, `**/*.pem`, `**/id_rsa`

<div id="configuring-cursorignore">
  ## `.cursorignore` の設定
</div>

ルートディレクトリに、`.gitignore` の構文で `.cursorignore` ファイルを作成する。

<div id="pattern-examples">
  ### パターンの例
</div>

```sh  theme={null}
config.json      # 特定のファイル
dist/           # ディレクトリ
*.log           # 拡張子による指定
**/logs         # 階層内のディレクトリ（再帰）
!app/           # 否定（無視対象から除外）
```

<div id="hierarchical-ignore">
  ### 階層的 ignore
</div>

親ディレクトリの`.cursorignore`ファイルも検索するには、`Cursor Settings` > `Features` > `Editor` > `Hierarchical Cursor Ignore`を有効にしよう。

**メモ**: コメントは `#` で始まる。後に書かれたパターンが前のものを上書きする。パターンはファイルの場所からの相対パス。

<div id="limit-indexing-with-cursorindexingignore">
  ## `.cursorindexingignore` でインデックスを制限
</div>

`.cursorindexingignore` を使うと、インデックス対象からのみファイルを除外できる。これらのファイルは AI 機能からは引き続きアクセスできるけど、コードベース検索には表示されない。

<div id="files-ignored-by-default">
  ## デフォルトで無視されるファイル
</div>

Cursor は `.gitignore` と以下のデフォルトの無視リストに含まれるファイルを自動的に無視する。`.cursorignore` で `!` を先頭に付ければ上書きできる。

<Accordion title="デフォルトの無視リスト">
  インデックス作成時のみ、`.gitignore`、`.cursorignore`、`.cursorindexingignore` に加えて、以下のファイルも無視される:

  ```sh  theme={null}
  package-lock.json
  pnpm-lock.yaml
  yarn.lock
  composer.lock
  Gemfile.lock
  bun.lockb
  .env*
  .git/
  .svn/
  .hg/
  *.lock
  *.bak
  *.tmp
  *.bin
  *.exe
  *.dll
  *.so
  *.lockb
  *.qwoff
  *.isl
  *.csv
  *.pdf
  *.doc
  *.doc
  *.xls
  *.xlsx
  *.ppt
  *.pptx
  *.odt
  *.ods
  *.odp
  *.odg
  *.odf
  *.sxw
  *.sxc
  *.sxi
  *.sxd
  *.sdc
  *.jpg
  *.jpeg
  *.png
  *.gif
  *.bmp
  *.tif
  *.mp3
  *.wav
  *.wma
  *.ogg
  *.flac
  *.aac
  *.mp4
  *.mov
  *.wmv
  *.flv
  *.avi
  *.zip
  *.tar
  *.gz
  *.7z
  *.rar
  *.tgz
  *.dmg
  *.iso
  *.cue
  *.mdf
  *.mds
  *.vcd
  *.toast
  *.img
  *.apk
  *.msi
  *.cab
  *.tar.gz
  *.tar.xz
  *.tar.bz2
  *.tar.lzma
  *.tar.Z
  *.tar.sz
  *.lzma
  *.ttf
  *.otf
  *.pak
  *.woff
  *.woff2
  *.eot
  *.webp
  *.vsix
  *.rmeta
  *.rlib
  *.parquet
  *.svg
  .egg-info/
  .venv/
  node_modules/
  __pycache__/
  .next/
  .nuxt/
  .cache/
  .sass-cache/
  .gradle/
  .DS_Store/
  .ipynb_checkpoints/
  .pytest_cache/
  .mypy_cache/
  .tox/
  .git/
  .hg/
  .svn/
  .bzr/
  .lock-wscript/
  .Python/
  .jupyter/
  .history/
  .yarn/
  .yarn-cache/
  .eslintcache/
  .parcel-cache/
  .cache-loader/
  .nyc_output/
  .node_repl_history/
  .pnp.js/
  .pnp/
  ```
</Accordion>

<div id="negation-pattern-limitations">
  ### 否定パターンの制限事項
</div>

否定パターン（先頭に `!` を付ける）を使う場合、親ディレクトリが \* で除外されていると、その配下のファイルを再度含めることはできない。

```sh  theme={null}

# public フォルダ内のすべてのファイルを無視
public/*


# ✅ これは有効（ファイルがトップレベルに存在するため）
!public/index.html


# ❌ これは無効 - ネストしたディレクトリ内のファイルは再包含できない
!public/assets/style.css
```

**回避策**: ネストしたディレクトリを明示的に除外する:

```sh  theme={null}
public/assets/*
!public/assets/style.css # このファイルは現在アクセス可能です
```

パフォーマンス上、除外されたディレクトリは走査しないため、その中にあるファイルに対するパターンは効かない。
これは、ネストしたディレクトリにおける否定パターンに関する .gitignore の実装と一致する。詳しくは、[gitignore のパターンについての公式 Git ドキュメント](https://git-scm.com/docs/gitignore)を参照してね。

<div id="troubleshooting">
  ## トラブルシューティング
</div>

`git check-ignore -v [file]` でパターンをテストする。



# Model Context Protocol (MCP)
Source: https://docs.cursor.com/ja/context/mcp

MCP を使って外部ツールやデータソースを Cursor に接続する

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="what-is-mcp">
  ## MCP とは？
</div>

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) は、Cursor が外部のツールやデータソースに接続するための仕組みだよ。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
</Frame>

<div id="why-use-mcp">
  ### なぜ MCP を使う？
</div>

MCP は Cursor を外部システムやデータに接続する。プロジェクト構成を毎回説明する代わりに、ツールと直接連携できる。

`stdout` に出力するか、HTTP エンドポイントを提供できる言語ならどれでも MCP サーバーを書ける — Python、JavaScript、Go など。

<div id="how-it-works">
  ### 仕組み
</div>

MCP サーバーはプロトコル経由で機能を公開し、Cursor を外部ツールやデータソースに接続する。

Cursor は 3 種類のトランスポート方式をサポートしてる:

<div className="full-width-table">
  | トランスポート                                                          | 実行環境      | デプロイ        | ユーザー   | 入力                | 認証    |
  | :--------------------------------------------------------------- | :-------- | :---------- | :----- | :---------------- | :---- |
  | **<span className="whitespace-nowrap">`stdio`</span>**           | ローカル      | Cursor が管理  | 単一ユーザー | シェルコマンド           | 手動    |
  | **<span className="whitespace-nowrap">`SSE`</span>**             | ローカル/リモート | サーバーとしてデプロイ | 複数ユーザー | SSE エンドポイントの URL  | OAuth |
  | **<span className="whitespace-nowrap">`Streamable HTTP`</span>** | ローカル/リモート | サーバーとしてデプロイ | 複数ユーザー | HTTP エンドポイントの URL | OAuth |
</div>

<div id="protocol-support">
  ### プロトコル対応
</div>

Cursor は次の MCP プロトコル機能に対応してる:

<div className="full-width-table">
  | 機能              | 対応状況 | 説明                                |
  | :-------------- | :--- | :-------------------------------- |
  | **Tools**       | 対応   | AI モデルが実行する関数                     |
  | **Prompts**     | 対応   | ユーザー向けのテンプレートメッセージとワークフロー         |
  | **Resources**   | 対応   | 読み取り・参照可能な構造化データソース               |
  | **Roots**       | 対応   | 操作対象となる URI／ファイルシステム境界へのサーバー起点の照会 |
  | **Elicitation** | 対応   | ユーザーに追加情報を求めるサーバー起点のリクエスト         |
</div>

<div id="installing-mcp-servers">
  ## MCP サーバーのインストール方法
</div>

<div id="one-click-installation">
  ### ワンクリックでインストール
</div>

コレクションから MCP サーバーをインストールして、OAuth で認証しよう。

<Columns cols={2}>
  <Card title="Browse MCP Tools" icon="table" horizontal href="/ja/tools">
    利用可能な MCP サーバーを閲覧
  </Card>

  <Card title="Add to Cursor Button" icon="plus" horizontal href="/ja/deeplinks">
    「Add to Cursor」ボタンを作成
  </Card>
</Columns>

<div id="using-mcpjson">
  ### `mcp.json` を使う
</div>

カスタム MCP サーバーを JSON ファイルで構成する:

<CodeGroup>
  ```json CLI Server - Node.js theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "npx",
        "args": ["-y", "mcp-server"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json CLI Server - Python theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "python",
        "args": ["mcp-server.py"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json Remote Server theme={null}
  // HTTP または SSE を使用する MCP サーバー — サーバー上で稼働
  {
    "mcpServers": {
      "server-name": {
        "url": "http://localhost:3000/mcp",
        "headers": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```
</CodeGroup>

<div id="stdio-server-configuration">
  ### STDIO サーバーの設定
</div>

STDIO サーバー（ローカルのコマンドラインサーバー）の場合、`mcp.json` で次のフィールドを設定してね:

<div className="full-width-table">
  | Field       | Required | Description                                     | Examples                                  |
  | :---------- | :------- | :---------------------------------------------- | :---------------------------------------- |
  | **type**    | Yes      | サーバーの接続タイプ                                      | `"stdio"`                                 |
  | **command** | Yes      | サーバー実行ファイルを起動するコマンド。システムの PATH にあるか、フルパスを指定してね。 | `"npx"`, `"node"`, `"python"`, `"docker"` |
  | **args**    | No       | コマンドに渡す引数の配列                                    | `["server.py", "--port", "3000"]`         |
  | **env**     | No       | サーバー用の環境変数                                      | `{"API_KEY": "${input:api-key}"}`         |
  | **envFile** | No       | 追加の環境変数を読み込むための環境ファイルのパス                        | `".env"`, `"${workspaceFolder}/.env"`     |
</div>

<div id="using-the-extension-api">
  ### Extension API の使用
</div>

プログラムによる MCP サーバー登録のために、Cursor は `mcp.json` ファイルを変更せずに動的に設定できる拡張 API を提供している。これは特にエンタープライズ環境や自動セットアップのワークフローで有用。

<Card title="MCP Extension API Reference" icon="code" href="/ja/context/mcp-extension-api">
  `vscode.cursor.mcp.registerServer()` を使ってプログラムから MCP サーバーを登録する方法を学ぼう
</Card>

<div id="configuration-locations">
  ### 設定の場所
</div>

<CardGroup cols={2}>
  <Card title="Project Configuration" icon="folder-tree">
    プロジェクト専用のツールには、プロジェクト内に `.cursor/mcp.json` を作成しよう。
  </Card>

  <Card title="Global Configuration" icon="globe">
    どこでも使えるツールには、ホームディレクトリに `~/.cursor/mcp.json` を作成しよう。
  </Card>
</CardGroup>

<div id="config-interpolation">
  ### コンフィグの補間
</div>

`mcp.json` の値に変数を使える。Cursor は次のフィールドで変数を解決する: `command`、`args`、`env`、`url`、`headers`。

サポートされる構文:

* `${env:NAME}` 環境変数
* `${userHome}` ホームフォルダへのパス
* `${workspaceFolder}` プロジェクトのルート（`.cursor/mcp.json` を含むフォルダ）
* `${workspaceFolderBasename}` プロジェクトルートの名前
* `${pathSeparator}` と `${/}` OS のパス区切り文字

例

```json  theme={null}
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

```json  theme={null}
{
  "mcpServers": {
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    }
  }
}
```

<div id="authentication">
  ### 認証
</div>

MCP サーバーは認証に環境変数を使う。API キーやトークンは config で渡してね。

Cursor は、OAuth が必要なサーバーにも対応してる。

<div id="using-mcp-in-chat">
  ## チャットでの MCP の使い方
</div>

Composer Agent は、必要に応じて `Available Tools` に表示されている MCP ツールを自動で使うよ。特定のツール名を指定するか、やりたいことをそのまま伝えてね。ツールの有効化・無効化は設定から切り替えられる。

<div id="toggling-tools">
  ### ツールの切り替え
</div>

チャット画面からそのまま MCP ツールを有効/無効にできる。ツール一覧でツール名をクリックすると切り替わる。無効にしたツールはコンテキストに読み込まれず、Agent からも利用できない。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-toggle.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fa3060f593cae3e5fb7c7d2f041a715" autoPlay loop muted playsInline controls data-path="images/context/mcp/tool-toggle.mp4" />
</Frame>

<div id="tool-approval">
  ### ツールの承認
</div>

デフォルトでは、Agent は MCP ツールを使う前に承認を求める。引数を確認するには、ツール名の横にある矢印をクリック。

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bf9b19d5f23abc65914f712185b3ec72" alt="" data-og-width="1212" width="1212" data-og-height="902" height="902" data-path="images/context/mcp/tool-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e3f900fad0b8f2a469460c70fa1dd1dc 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de2f90138de39d75d70c5800f13be93a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b9c616ce7a4080ea4088a0fdd0050c7c 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3f783e62a7a31957b8988edb97c139f9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10bf2c1dbfd5c2a03aa95334f53cd571 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=231c0e3cd60df5ad12455d5e8ef308d2 2500w" /></Frame>

<div id="auto-run">
  #### 自動実行
</div>

Agent が確認なしで MCP ツールを使えるよう、自動実行を有効にする。ターミナルのコマンドのように動作する。自動実行の設定については[こちら](/ja/agent/tools#auto-run)を参照。

<div id="tool-response">
  ### ツールのレスポンス
</div>

Cursor は、引数とレスポンスを展開できるビューとともに、チャット内にレスポンスを表示する:

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=30af3f35869e9a78781f455bdbc0e3b5" alt="" data-og-width="1212" width="1212" data-og-height="952" height="952" data-path="images/context/mcp/tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8821ac7bad00ad54a18abc614c2e3d5c 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9d55f089ad53a89da99b8ddd524f6de 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a107d68a1fb05ed43851548b34fb4496 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b409b4941c2fd783043770fad0bd6390 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2a331b5e2bb9be0b9659393157454c2e 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=585b769dfa2a5114b111eb901a969845 2500w" /></Frame>

<div id="images-as-context">
  ### コンテキストとしての画像
</div>

MCP サーバーは画像（スクリーンショット、ダイアグラムなど）を返せる。base64 でエンコードした文字列として返して:

```js  theme={null}
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ 可読性のために base64 全体を省略

server.tool("generate_image", async (params) => {
  return {
    content: [
      {
        type: "image",
        data: RED_CIRCLE_BASE64,
        mimeType: "image/jpeg",
      },
    ],
  };
});
```

実装の詳細はこの[example server](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js)を参照してね。Cursor は返された画像をチャットに添付するよ。モデルが画像をサポートしていれば、それらを解析する。

<div id="security-considerations">
  ## セキュリティ上の考慮事項
</div>

MCP サーバーをインストールするときは、次のセキュリティ対策を意識してね:

* **配布元の確認**: 信頼できる開発者やリポジトリからの MCP サーバーだけをインストールする
* **権限の確認**: サーバーがアクセスするデータや API をチェックする
* **API キーの最小化**: 必要最小限の権限に絞った制限付き API キーを使う
* **コードの監査**: 重要な連携では、サーバーのソースコードをレビューする

MCP サーバーは外部サービスにアクセスしたり、きみの代わりにコードを実行できることを忘れないで。インストール前に、そのサーバーが何をするのか必ず理解しておこう。

<div id="real-world-examples">
  ## 実際の例
</div>

MCP を実際に活用する具体例は、開発ワークフローに Linear、Figma、ブラウザツールを統合する方法を紹介している [Web Development ガイド](/ja/guides/tutorials/web-development) を参照してね。

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="MCP サーバーの目的は？">
    MCP サーバーは、Cursor を Google Drive や Notion などの外部ツールやサービスに接続して、ドキュメントや要件をコーディングのワークフローに取り込めるようにするものだよ。
  </Accordion>

  {" "}

  <Accordion title="MCP サーバーの問題はどうデバッグする？">
    MCP のログを見るには: 1. Cursor で Output パネルを開く (<Kbd>Cmd+Shift+U</Kbd>)
    2\. ドロップダウンから「MCP Logs」を選ぶ 3. 接続エラー、認証エラー、サーバークラッシュを確認する
    ログにはサーバーの初期化、ツール呼び出し、エラーメッセージが出るよ。
  </Accordion>

  {" "}

  <Accordion title="MCP サーバーを一時的に無効化できる？">
    できる！削除せずにオン/オフを切り替えられるよ: 1. Settings を開く (
    <Kbd>Cmd+Shift+J</Kbd>) 2. Features → Model Context Protocol に進む 3.
    任意のサーバーのトグルをクリックして有効/無効を切り替える 無効化したサーバーは読み込まれず、チャットにも出てこないよ。
    トラブルシューティングやツールの整理に便利。
  </Accordion>

  {" "}

  <Accordion title="MCP サーバーがクラッシュしたりタイムアウトしたら？">
    MCP サーバーが失敗した場合: - Cursor がチャットにエラーメッセージを表示する - ツール呼び出しは失敗としてマークされる - 操作を再試行するか、詳細はログを確認できる - 他の MCP サーバーは通常どおり動作を継続する
    Cursor はサーバーの障害を分離して、1つのサーバーが他に影響しないようにしてるよ。
  </Accordion>

  {" "}

  <Accordion title="MCP サーバーはどう更新する？">
    npm ベースのサーバーの場合: 1. 設定からサーバーを削除 2. npm キャッシュをクリア:
    `npm cache clean --force` 3. 最新版を取得するためにサーバーを再追加 カスタムサーバーの場合は、ローカルファイルを更新して Cursor を再起動してね。
  </Accordion>

  <Accordion title="機密データで MCP サーバーを使える？">
    使えるけど、セキュリティのベストプラクティスに従ってね: - 秘密情報は環境変数を使い、ハードコードしない - 機密性の高いサーバーは `stdio`
    トランスポートでローカル実行する - API キーの権限は必要最小限に絞る - 機密システムに接続する前にサーバーコードをレビューする - サーバーを分離環境で実行することを検討する
  </Accordion>
</AccordionGroup>



# Memories
Source: https://docs.cursor.com/ja/context/memories



Memories は、Chat のやり取りに基づいて自動生成されるルール。各 Memories はプロジェクト単位で適用され、セッションをまたいでコンテキストを保持する。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/memories.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d10452508d962d7a9ec37de1c22245d1" alt="Cursor の Memories" controls data-path="images/context/rules/memories.mp4" />
</Frame>

<div id="how-memories-are-created">
  ## メモリが作成される仕組み
</div>

1. **サイドカー観測**: Cursor はサイドカー方式を採用していて、別のモデルが会話を観測し、自動で関連するメモリを抽出する。これは作業中にバックグラウンドで受動的に行われる。バックグラウンドで生成されたメモリは保存前にユーザーの承認が必要で、何を記憶するかに対する信頼性とコントロールを確保する。

2. **ツールコール**: Agent は、明示的に「覚えて」と依頼した場合や、今後のセッションで保持すべき重要な情報に気づいた場合に、ツールコールを使って直接メモリを作成できる。

<div id="manage-memories">
  ## メモリの管理
</div>

Cursor の設定 → Rules からメモリを管理できるよ。



# ルール
Source: https://docs.cursor.com/ja/context/rules

再利用可能でスコープ化された指示で、Agent モデルの動作を制御する。

ルールは Agent と Inline Edit に対するシステムレベルの指示を提供する。プロジェクトにおける永続的なコンテキスト、設定、ワークフローとして考えていい。

Cursor は 4 種類のルールをサポートしている:

<CardGroup cols={2}>
  <Card title="Project Rules" icon="folder-tree">
    `.cursor/rules` に保存され、バージョン管理され、コードベースにスコープされる。
  </Card>

  <Card title="User Rules" icon="user">
    Cursor 環境全体で有効。設定で定義され、常に適用される。
  </Card>

  <Card title="AGENTS.md" icon="robot">
    Markdown 形式の Agent 向け指示。`.cursor/rules` のシンプルな代替。
  </Card>

  <Card title=".cursorrules (Legacy)" icon="clock-rotate-left">
    まだサポートされているが非推奨。代わりに Project Rules を使ってね。
  </Card>
</CardGroup>

<div id="how-rules-work">
  ## ルールの仕組み
</div>

大規模言語モデルは補完のあいだで状態を保持しない。ルールはプロンプトレベルで永続的かつ再利用可能なコンテキストを提供する。

適用されると、ルールの内容はモデルのコンテキストの先頭に含まれる。これにより、AIはコード生成、編集内容の解釈、ワークフロー支援において一貫した指針を得られる。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="チャットのコンテキストで適用されたルール" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
</Frame>

<Info>
  ルールは [Chat](/ja/chat/overview) と [Inline Edit](/ja/inline-edit/overview) に適用される。アクティブなルールは Agent サイドバーに表示される。
</Info>

<div id="project-rules">
  ## プロジェクトルール
</div>

プロジェクトルールは `.cursor/rules` に配置される。各ルールは単一ファイルで、バージョン管理の対象。パスパターンで適用範囲を絞ったり、手動で実行したり、関連性に基づいて自動的に取り込める。サブディレクトリには、そのフォルダにスコープされた独自の `.cursor/rules` ディレクトリを含められる。

プロジェクトルールの使いどころ:

* コードベースに関するドメイン固有知識を記述する
* プロジェクト固有のワークフローやテンプレートを自動化する
* スタイルやアーキテクチャの方針を標準化する

<div id="rule-anatomy">
  ### ルールの構成
</div>

各ルールファイルはメタデータとコンテンツを扱える **MDC**（`.mdc`）で書かれてる。種類のドロップダウンから `description`、`globs`、`alwaysApply` のプロパティを切り替えて、ルールの適用方法を制御できる。

| <span class="no-wrap">Rule Type</span>         | Description                    |
| :--------------------------------------------- | :----------------------------- |
| <span class="no-wrap">`Always`</span>          | つねにモデルのコンテキストに含まれる             |
| <span class="no-wrap">`Auto Attached`</span>   | グロブパターンに一致するファイルが参照されたときに含まれる  |
| <span class="no-wrap">`Agent Requested`</span> | AI が判断して必要なら含める。説明の記述が必須       |
| <span class="no-wrap">`Manual`</span>          | `@ruleName` で明示的に指定した場合にのみ含まれる |

```
---
description: RPC サービス用ボイラープレート
globs:
alwaysApply: false
---

- サービスを定義するときは、社内の RPC パターンを使用する
- サービス名は常に snake_case を使用する

@service-template.ts
```

<div id="nested-rules">
  ### ネストされたルール
</div>

プロジェクト内の各所にある `.cursor/rules` ディレクトリにルールを置いて整理しよう。ディレクトリ内のファイルが参照されると、そのディレクトリにあるネストされたルールが自動的に適用される。

```
project/
  .cursor/rules/        # プロジェクト全体のルール
  backend/
    server/
      .cursor/rules/    # バックエンド用ルール
  frontend/
    .cursor/rules/      # フロントエンド用ルール
```

<div id="creating-a-rule">
  ### ルールの作成
</div>

`New Cursor Rule` コマンドを使うか、`Cursor Settings > Rules` に進んでルールを作成しよう。これで `.cursor/rules` に新しいルールファイルが作成される。Settings では、すべてのルールとそのステータスを確認できる。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=db8142786bbb7b7771ae0db8b2704b0b" alt="簡潔なルールと長文ルールの比較" data-og-width="6016" width="6016" data-og-height="3334" height="3334" data-path="images/context/rules/rule-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b6e9b8d6ca799d1af62957726b1cc52 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bfe1482ab9afc0995fe13371b26074b 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a847d915b3f106c42cba7cb1245bb138 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=356963b3607152f7ffe128cd1a2d050e 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b1e50d3721d42c691a434189729921c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d2081cf016d65053f1e517eb5734079e 2500w" />
</Frame>

<div id="generating-rules">
  ### ルールの生成
</div>

会話の中で `/Generate Cursor Rules` コマンドを使って、ルールをその場で作成できる。エージェントのふるまいを決めて、それを再利用したいときに便利。

<Frame>
  <video src="https://www.cursor.com/changelog/049/generate-rules.mp4" controls>
    Your browser does not support the video tag.
  </video>
</Frame>

<div id="best-practices">
  ## ベストプラクティス
</div>

良いルールは、焦点が明確で、実行可能で、スコープが適切。

* ルールは500行以内に収める
* 大きなルールは、複数の組み合わせ可能なルールに分割する
* 具体的な例や参照ファイルを示す
* あいまいな指示は避ける。社内ドキュメントのように明確に書く
* チャットで同じプロンプトを繰り返す場合は、ルールを再利用する

<div id="examples">
  ## 例
</div>

<AccordionGroup>
  <Accordion title="フロントエンドコンポーネントと API バリデーションの標準">
    このルールはフロントエンドコンポーネントの標準を定める:

    components ディレクトリで作業するとき:

    * スタイリングは常に Tailwind を使う
    * アニメーションは Framer Motion を使う
    * コンポーネントの命名規則に従う

    このルールは API エンドポイントのバリデーションを徹底する:

    api ディレクトリでは:

    * すべてのバリデーションに zod を使う
    * 戻り値の型は zod スキーマで定義する
    * スキーマから生成された型をエクスポートする
  </Accordion>

  <Accordion title="Express サービスと React コンポーネントのテンプレート">
    このルールは Express サービスのテンプレートを提供する:

    Express サービスを作成するときはこのテンプレートを使う:

    * RESTful の原則に従う
    * エラーハンドリング用ミドルウェアを含める
    * 適切なロギングを設定する

    @express-service-template.ts

    このルールは React コンポーネントの構成を定義する:

    React コンポーネントは次のレイアウトに従う:

    * 先頭に Props のインターフェース
    * コンポーネントは名前付きエクスポート
    * スタイルは末尾に置く

    @component-template.tsx
  </Accordion>

  <Accordion title="開発ワークフローの自動化とドキュメント生成">
    このルールはアプリの分析を自動化する:

    アプリの分析を依頼されたら:

    1. `npm run dev` で dev サーバーを起動する
    2. コンソールのログを取得する
    3. パフォーマンス改善案を提案する

    このルールはドキュメント生成を支援する:

    ドキュメントの下書きは次で行う:

    * コードコメントを抽出する
    * README.md を分析する
    * Markdown ドキュメントを生成する
  </Accordion>

  <Accordion title="Cursor に新しい設定を追加する">
    まず `@reactiveStorageTypes.ts` にトグル用のプロパティを作成する。

    `@reactiveStorageService.tsx` の `INIT_APPLICATION_USER_PERSISTENT_STORAGE` にデフォルト値を追加する。

    ベータ機能の場合は `@settingsBetaTab.tsx` に、そうでない場合は `@settingsGeneralTab.tsx` にトグルを追加する。トグルは一般的なチェックボックスとして `<SettingsSubSection>` を使って追加できる。詳細はファイル内の他の例を参照。

    ```
    <SettingsSubSection
    				label="Your feature name"
    				description="Your feature description"
    				value={
    					vsContext.reactiveStorageService.applicationUserPersistentStorage
    						.myNewProperty ?? false
    				}
    				onChange={(newVal) => {
    					vsContext.reactiveStorageService.setApplicationUserPersistentStorage(
    						'myNewProperty',
    						newVal
    					);
    				}}
    			/>
    ```

    アプリで使うには、reactiveStorageService をインポートしてプロパティを参照する:

    ```
    const flagIsEnabled = vsContext.reactiveStorageService.applicationUserPersistentStorage.myNewProperty
    ```
  </Accordion>
</AccordionGroup>

プロバイダーやフレームワークから多くの例がある。コミュニティ提供のルールは、クラウドソースのコレクションやオンラインのリポジトリに多数ある。

<div id="agentsmd">
  ## AGENTS.md
</div>

`AGENTS.md` は、エージェント向けの指示を定義するためのシンプルな Markdown ファイル。プロジェクトのルートに配置すれば、簡単なユースケースでは `.cursor/rules` の代替として使える。

Project Rules と違い、`AGENTS.md` はメタデータや複雑な設定を持たないプレーンな Markdown ファイル。構造化ルールのオーバーヘッドなしで、シンプルで読みやすい指示がほしいプロジェクトに最適。

```markdown  theme={null}

# プロジェクト方針

## コードスタイル
- すべての新規ファイルで TypeScript を使用する
- React では関数コンポーネントを優先する
- データベースのカラム名は snake_case を使用する

## アーキテクチャ
- リポジトリパターンに従う
- ビジネスロジックはサービス層に置く
```

<div id="user-rules">
  ## User Rules
</div>

User Rules は、すべてのプロジェクトに適用される **Cursor Settings → Rules** で定義するグローバルな設定。プレーンテキストで記述できて、好みのコミュニケーションスタイルやコーディング規約を設定するのに最適だよ。

```
簡潔に返答して。不要な繰り返しや冗長な表現は避けて。
```

<div id="cursorrules-legacy">
  ## `.cursorrules`（レガシー）
</div>

プロジェクトのルートにある `.cursorrules` ファイルは引き続きサポートされるが、今後廃止予定。より細かな制御、柔軟性、可視性のために Project Rules への移行をおすすめする。

<div id="faq">
  ## よくある質問
</div>

<AccordionGroup>
  <Accordion title="ルールが適用されないのはなぜ？">
    ルールの種類を確認して。`Agent Requested` なら説明が定義されてるかチェック。`Auto Attached` ならファイルパターンが参照してるファイルにマッチしてるか確認して。
  </Accordion>

  {" "}

  <Accordion title="ルールは他のルールやファイルを参照できる？">
    できる。`@filename.ts` を使って、ルールのコンテキストにファイルを含めて。
  </Accordion>

  {" "}

  <Accordion title="チャットからルールを作成できる？">
    できる。`/Generate Cursor Rules` コマンドでチャットからプロジェクトルールを生成できる。Memories が有効なら、メモリは自動で作成されるよ。
  </Accordion>

  <Accordion title="ルールは Cursor Tab や他の AI 機能に影響する？">
    影響しない。ルールが適用されるのは Agent と Inline Edit だけだよ。
  </Accordion>
</AccordionGroup>



# 基本概念
Source: https://docs.cursor.com/ja/get-started/concepts

Cursor を強力にする主要機能を学ぶ

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div className="flex flex-col gap-12">
  <Columns className="gap-4">
    <div>
      <h2 className="text-lg font-medium mb-2">
        <a href="/ja/tab/overview" className="hover:text-primary transition-colors">
          Tab
        </a>
      </h2>

      <p className="text-sm">
        複数行の編集まで予測するコード補完。Tab を押すと、いまのコードや直近の変更に基づくサジェストをそのまま適用できる。
      </p>
    </div>

    <Frame>
      <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=5357dd01f6e7560c5ecb14367f4046f0" alt="Tab のオートコンプリート" data-og-width="960" width="960" data-og-height="540" height="540" data-path="images/tab/tab-simple.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=9248a129c1f0ff309e522a26f7a2ca2b 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=894e4b876dfefd45d4b7259fb15a1789 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fd7441e84be11187ee8d0cbcdabd0222 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=b4e150615b4f0a82a347d4f47baa775b 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=f5db727f7b719651434684d1de0cbe90 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/tab/tab-simple.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=cc1bd1fa532d878fe7e01700b28204f7 2500w" />
    </Frame>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/agent/overview" className="hover:text-primary transition-colors">
          Agent
        </a>
      </h3>

      <p className="text-sm">
        複数ファイルにまたがるコードを読み書き・変更できるAI。変更内容を自然言語で伝えるだけで、Agentが実行してくれる。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" alt="Agentモード" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/background-agent" className="hover:text-primary transition-colors">
          Background Agent
        </a>
      </h3>

      <p className="text-sm">
        作業を続けながらタスクを非同期で実行。エディタや Slack などの外部連携から利用できる。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=07d084420ba9377c6a454b519a138e1a" alt="Background agent" data-og-width="2452" width="2452" data-og-height="1380" height="1380" data-path="images/background-agent/cmd-e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=da4af3c5bedf87e80eb247c0f90b3e19 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8d2cb1c8514e6fbc965ebaeaa1ce05a7 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=50e2e022f3912f1e819ea59b128b57bc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5a0ad429a7894a70ba218609679e9e4f 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4140cf5142bb912b712bd76c828f2c9d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/cmd-e.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=67d608ee4c0a3c56647a3787a2d65661 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/inline-edit/overview" className="hover:text-primary transition-colors">
          インライン編集
        </a>
      </h3>

      <p className="text-sm">
        選択したコードを自然言語で編集できる。<Kbd>Cmd+K</Kbd> を押して
        変更内容を指示すると、その場で適用される。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=739ac6db99d802de30f55ddedc3da272" alt="Inline editing" data-og-width="2960" width="2960" data-og-height="1657" height="1657" data-path="images/inline-edit/qq.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a58d16e85db7340c0e86cdcfd38ce67b 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a50013ce1196be4d688ff832c4fa026b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ce103df31faa30ed7e9eaa40d4f0cdd1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=0f20974d2d2013dba35bca117e84d68f 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7dbd27505e9ce9665576650fec7d77d4 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/inline-edit/qq.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=0b88e0a5ce44c4f6f1aa7f25d6460244 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/agent/chats/tabs" className="hover:text-primary transition-colors">
          チャット
        </a>
      </h3>

      <p className="text-sm">
        AIとの対話用インターフェース。複数タブ、会話履歴、チェックポイント、エクスポートに対応。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/context/rules" className="hover:text-primary transition-colors">
          ルール
        </a>
      </h3>

      <p className="text-sm">
        AI の振る舞いを定義するカスタム指示。コーディング規約、フレームワークの好み、プロジェクト固有の慣例を設定できる。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1be049cdaea7bca34d91a1b5bc29d55c" alt="AI rules" data-og-width="2318" width="2318" data-og-height="1304" height="1304" data-path="images/context/rules/mdc-editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=21331e8350c3fb52634bf1060f3e0e60 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=603820d50edcfe38aaa9b148d26e450e 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=795cf8aa5a5b177132b3cfa98a9a6174 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=49a57c4b1d0a6a70a0192feda2f4e754 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=369273301d1a35916926ca382ce81951 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/mdc-editor.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=92fbb9585a42907596b983afd666dbf4 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/context/memories" className="hover:text-primary transition-colors">
          メモリー
        </a>
      </h3>

      <p className="text-sm">
        過去の会話から得たプロジェクトの文脈や判断を永続的に保存。今後のやり取りで自動的に参照される。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/memories.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d10452508d962d7a9ec37de1c22245d1" autoPlay loop muted playsInline controls data-path="images/context/rules/memories.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/context/codebase-indexing" className="hover:text-primary transition-colors">
          コードベースのインデックス化
        </a>
      </h3>

      <p className="text-sm">
        コードベースをセマンティックに解析。コード検索、参照の特定、文脈に応じたサジェストを可能にする。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="コードベースのインデックス化" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/context/mcp" className="hover:text-primary transition-colors">
          MCP
        </a>
      </h3>

      <p className="text-sm">
        外部ツールを統合するための Model Context Protocol。データベース、API、ドキュメントソースへ接続する。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/guides/working-with-context" className="hover:text-primary transition-colors">
          コンテキスト
        </a>
      </h3>

      <p className="text-sm">
        コード生成中に AI モデルに与える情報。ファイル、シンボル、会話履歴などを含む。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=98029d0ecb83175a496ef16ccb1c92d7" alt="コンテキストの管理" data-og-width="1230" width="1230" data-og-height="794" height="794" data-path="images/context/symbols/context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=edadefb46f31037df216bdc41ff65f0e 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a0e30bf50ab5525b72b23d5d9847c7f8 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=903ab32cc5460a6573deef144b445945 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8820522f1a505b3205c0ffc2a3f1a382 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b46b89fa6da137cea339ed94eb711b3c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/context-menu.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2e9ff863747cbf6faa2b675d400a7f6e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/models" className="hover:text-primary transition-colors">
          モデル
        </a>
      </h3>

      <p className="text-sm">
        コード生成に使えるAIモデルを用意してるよ。モデルごとに、速度や対応能力の特性が違う。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f039569ed0dc2ad7e02bb1b2e9cea71" alt="モデルの選択" data-og-width="2256" width="2256" data-og-height="1248" height="1248" data-path="images/models/model-picker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=49c6a091945972253eb6e819593e45f0 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f9bddfb2e130789d8d51a3d1a4eeba94 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=db7273f399bb5decfed9d1b06f389df4 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=920fe98d4f99b5d7fddd47a14fb45699 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3b049686e5826263800b63299f4c19ca 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=72ddd56b4d3ea9b2efa4001a155566fd 2500w" />
      </Frame>
    </div>
  </Columns>
</div>



# インストール
Source: https://docs.cursor.com/ja/get-started/installation

数分でコンピュータに Cursor をインストール

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="download-cursor">
  ## Cursor をダウンロード
</div>

始めるのはかんたん:

1. [cursor.com](https://cursor.com) にアクセスして「Download」をクリック
2. ダウンロード完了後、インストーラーを実行
3. インストールが完了したら Cursor を開く

<Info>
  特定のバージョンが必要なら、すべてのプラットフォームとインストール方法は
  [cursor.com/downloads](https://cursor.com/downloads) で確認できるよ
</Info>

<div id="first-time-setup">
  ## 初回セットアップ
</div>

初めて Cursor を開くと、かんたんなセットアップに案内するよ:

* 使い慣れたキーボードショートカットを選ぶ
* 好きなテーマを選ぶ
* ターミナルの設定を整える

<Frame>
  <video controls width="100%">
    <source src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/cursor-onboarding.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=cda00fa83569cd85c6b7322c34f4843e" type="video/mp4" data-path="images/get-started/cursor-onboarding.mp4" />

    お使いのブラウザは video タグをサポートしていません。
  </video>
</Frame>

<Tip>
  <Kbd>Cmd Shift P</Kbd>{" "}を押して `Cursor: Start Onboarding` を検索すれば、いつでもセットアップウィザードをやり直せるよ。
</Tip>

[Keyboard Shortcuts](/ja/kbd)、[Themes](/ja/settings/themes)、[Shell Commands](/ja/settings/shell) について詳しく見る

<CardGroup cols={3}>
  <Card title="Keyboard shortcuts" href="/ja/configuration/kbd" arrow>
    キーボードショートカットを見る
  </Card>

  <Card title="Themes" href="/ja/configuration/themes" arrow>
    Cursor のテーマを選ぶ
  </Card>

  <Card title="Shell Commands" href="/ja/configuration/shell" arrow>
    シェルコマンドをインストール
  </Card>
</CardGroup>

<div id="moving-from-another-editor">
  ## ほかのエディタから移行する？
</div>

もう別のコードエディタを使ってるなら、切り替えはカンタンだよ:

<CardGroup cols={2}>
  <Card title="VS Code" href="/ja/guides/migration/vscode" arrow>
    VS Code の設定をそのままインポート
  </Card>

  <Card title="Jetbrains" href="/ja/guides/migration/jetbrains" arrow>
    JetBrains、Eclipse、Neovim、Sublime 向けの移行ガイド
  </Card>
</CardGroup>

そのほかの移行ガイドも順次追加予定。

<div id="language-support">
  ## 言語サポート
</div>

Cursor は主要なプログラミング言語のほとんどに対応してる。以下は、AI サポートが強化されてる人気の言語の一部だよ：

<CardGroup cols={4}>
  <Card
    title="TypeScript"
    href="/ja/guides/languages/javascript"
    icon={<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none">
<rect width={512} height={512} fill="#3178c6" rx={50} />
<rect width={512} height={512} fill="#3178c6" rx={50} />
<path
fill="#fff"
fillRule="evenodd"
d="M316.939 407.424v50.061c8.138 4.172 17.763 7.3 28.875 9.386S368.637 470 380.949 470c11.999 0 23.397-1.147 34.196-3.442 10.799-2.294 20.268-6.075 28.406-11.342 8.138-5.266 14.581-12.15 19.328-20.65S470 415.559 470 403.044c0-9.074-1.356-17.026-4.069-23.857s-6.625-12.906-11.738-18.225c-5.112-5.319-11.242-10.091-18.389-14.315s-15.207-8.213-24.18-11.967c-6.573-2.712-12.468-5.345-17.685-7.9-5.217-2.556-9.651-5.163-13.303-7.822-3.652-2.66-6.469-5.476-8.451-8.448-1.982-2.973-2.974-6.336-2.974-10.091 0-3.441.887-6.544 2.661-9.308s4.278-5.136 7.512-7.118c3.235-1.981 7.199-3.52 11.894-4.615 4.696-1.095 9.912-1.642 15.651-1.642 4.173 0 8.581.313 13.224.938 4.643.626 9.312 1.591 14.008 2.894a97.514 97.514 0 0 1 13.694 4.928c4.434 1.982 8.529 4.276 12.285 6.884v-46.776c-7.616-2.92-15.937-5.084-24.962-6.492S415.797 238 404.112 238c-11.895 0-23.163 1.278-33.805 3.833s-20.006 6.544-28.093 11.967c-8.086 5.424-14.476 12.333-19.171 20.729-4.695 8.395-7.043 18.433-7.043 30.114 0 14.914 4.304 27.638 12.912 38.172 8.607 10.533 21.675 19.45 39.204 26.751 6.886 2.816 13.303 5.579 19.25 8.291s11.086 5.528 15.415 8.448c4.33 2.92 7.747 6.101 10.252 9.543 2.504 3.441 3.756 7.352 3.756 11.733 0 3.233-.783 6.231-2.348 8.995s-3.939 5.162-7.121 7.196-7.147 3.624-11.894 4.771c-4.748 1.148-10.303 1.721-16.668 1.721-10.851 0-21.597-1.903-32.24-5.71-10.642-3.806-20.502-9.516-29.579-17.13zM232.78 284.082H297V243H118v41.082h63.906V467h50.874z"
clipRule="evenodd"
/>
</svg>}
    arrow
  />

  <Card
    title="Java"
    href="/ja/guides/languages/java"
    icon={ <svg
xmlns="http://www.w3.org/2000/svg"
fill="none"
aria-label="Java"
viewBox="0 0 512 512"
width="32"

>

<rect width={512} height={512} fill="#fff" rx="15%" />
<path
fill="#f8981d"
d="M274 235c18 21-5 40-5 40s47-24 25-54-35-42 48-90c0-1-131 32-68 104m20-182s40 40-38 100c-62 49-14 77 0 109-36-33-63-61-45-88 27-40 99-59 83-121"
/>
<path
fill="#5382a1"
d="M206 347s-15 8 10 11 46 3 79-3a137 137 0 0 0 21 10c-74 32-169-1-110-18m-9-42s-16 12 9 15 58 4 102-5a45 45 0 0 0 16 10c-91 26-192 2-127-20m175 73s11 9-12 16c-43 13-179 17-217 1-14-6 15-17 33-17-17-10-98 21-42 30 153 24 278-12 238-30M213 262s-69 16-25 22c19 3 57 2 92-1s57-8 57-8a122 122 0 0 0-17 9c-70 18-206 10-167-9s60-13 60-13m124 69c73-37 39-80 7-66 36-30 101 36-9 68v-2M220 432c69 4 174-2 176-35 0 0-5 12-57 22s-131 10-174 3c1 0 10 7 55 10"
/>

</svg>}
    arrow
  />

  <Card
    title="Python"
    href="/ja/guides/languages/python"
    icon={
<svg
xmlns="http://www.w3.org/2000/svg"
width="24"
height="24"
fill="none"
viewBox="0 0 32 32"
>
<path
fill="url(#a)"
fillRule="evenodd"
d="M13.016 2C10.82 2 9.038 3.725 9.038 5.852v2.667h6.886v.74H5.978C3.781 9.26 2 10.984 2 13.111v5.778c0 2.127 1.781 3.852 3.978 3.852h2.295v-3.26c0-2.127 1.781-3.851 3.978-3.851h7.345c1.859 0 3.366-1.46 3.366-3.26V5.852C22.962 3.725 21.18 2 18.984 2h-5.968Zm-.918 4.74c.76 0 1.377-.596 1.377-1.333 0-.736-.616-1.333-1.377-1.333-.76 0-1.377.597-1.377 1.333 0 .737.617 1.334 1.377 1.334Z"
clipRule="evenodd"
/>
<path
fill="url(#b)"
fillRule="evenodd"
d="M18.983 30c2.197 0 3.979-1.724 3.979-3.852v-2.666h-6.886v-.741h9.946c2.197 0 3.978-1.725 3.978-3.852V13.11c0-2.127-1.781-3.852-3.978-3.852h-2.295v3.26c0 2.127-1.782 3.851-3.979 3.851h-7.344c-1.859 0-3.366 1.46-3.366 3.26v6.518c0 2.128 1.781 3.852 3.978 3.852h5.967Zm.918-4.74c-.76 0-1.377.596-1.377 1.333 0 .736.617 1.333 1.377 1.333.761 0 1.378-.597 1.378-1.333 0-.737-.617-1.334-1.378-1.334Z"
clipRule="evenodd"
/>
<defs>
<linearGradient
id="a"
x1={12.481}
x2={12.481}
y1={2}
y2={22.741}
gradientUnits="userSpaceOnUse"
>
<stop stopColor="#327EBD" />
<stop offset={1} stopColor="#1565A7" />
</linearGradient>
<linearGradient
id="b"
x1={19.519}
x2={19.519}
y1={9.259}
y2={30}
gradientUnits="userSpaceOnUse"
>
<stop stopColor="#FFDA4B" />
<stop offset={1} stopColor="#F9C600" />
</linearGradient>
</defs>
</svg>
}
    arrow
  />

  <Card
    title="Swift"
    href="/ja/guides/languages/swift"
    icon={
<svg
xmlns="http://www.w3.org/2000/svg"
xmlSpace="preserve"
width="24"
height="24"
viewBox="0 0 59.391 59.391"
>
<path
fill="#F05138"
d="M59.387 16.45a82.463 82.463 0 0 0-.027-1.792c-.035-1.301-.112-2.614-.343-3.9-.234-1.307-.618-2.523-1.222-3.71a12.464 12.464 0 0 0-5.453-5.452C51.156.992 49.941.609 48.635.374c-1.288-.232-2.6-.308-3.902-.343a85.714 85.714 0 0 0-1.792-.027C42.23 0 41.52 0 40.813 0H18.578c-.71 0-1.419 0-2.128.004-.597.004-1.195.01-1.792.027-.325.009-.651.02-.978.036-.978.047-1.959.133-2.924.307-.98.176-1.908.436-2.811.81A12.503 12.503 0 0 0 3.89 3.89a12.46 12.46 0 0 0-2.294 3.158C.992 8.235.61 9.45.374 10.758c-.231 1.286-.308 2.599-.343 3.9a85.767 85.767 0 0 0-.027 1.792C-.001 17.16 0 17.869 0 18.578v22.235c0 .71 0 1.418.004 2.128.004.597.01 1.194.027 1.791.035 1.302.112 2.615.343 3.901.235 1.307.618 2.523 1.222 3.71a12.457 12.457 0 0 0 5.453 5.453c1.186.603 2.401.986 3.707 1.22 1.287.232 2.6.31 3.902.344.597.016 1.195.023 1.793.027.709.005 1.417.004 2.127.004h22.235c.709 0 1.418 0 2.128-.004.597-.004 1.194-.011 1.792-.027 1.302-.035 2.614-.112 3.902-.343 1.306-.235 2.521-.618 3.707-1.222a12.461 12.461 0 0 0 5.453-5.452c.604-1.187.987-2.403 1.222-3.71.231-1.286.308-2.6.343-3.9.016-.598.023-1.194.027-1.792.004-.71.004-1.419.004-2.129V18.578c0-.71 0-1.419-.004-2.128z"
/>
<path
fill="#FFF"
d="m47.06 36.66-.004-.004c.066-.224.134-.446.191-.675 2.465-9.821-3.55-21.432-13.731-27.546 4.461 6.048 6.434 13.374 4.681 19.78-.156.571-.344 1.12-.552 1.653-.225-.148-.51-.316-.89-.527 0 0-10.127-6.252-21.103-17.312-.288-.29 5.852 8.777 12.822 16.14-3.284-1.843-12.434-8.5-18.227-13.802.712 1.187 1.558 2.33 2.489 3.43C17.573 23.932 23.882 31.5 31.44 37.314c-5.31 3.25-12.814 3.502-20.285.003a30.646 30.646 0 0 1-5.193-3.098c3.162 5.058 8.033 9.423 13.96 11.97 7.07 3.039 14.1 2.833 19.336.05l-.004.007c.024-.016.055-.032.08-.047.214-.116.428-.234.636-.358 2.516-1.306 7.485-2.63 10.152 2.559.654 1.27 2.041-5.46-3.061-11.74z"
/>
</svg>
}
    arrow
  />
</CardGroup>

VS Code と同様に、拡張機能を使ってさらに多くの言語をサポートできるよ。

<div id="creating-your-account">
  ## アカウントの作成
</div>

Cursorはアカウントなしでも使えるけど、サインアップするとAI機能をフルに使えるようになる:

1. セットアップ中にサインアップを求められるか、あとで設定からできる (<Kbd>Cmd Shift J</Kbd>)
2. サインアップ後は [cursor.com/dashboard](https://cursor.com/dashboard) でアカウントを管理

<div id="understanding-codebase-indexing">
  ## コードベースのインデックス化を理解する
</div>

プロジェクトを開くと、Cursor がコードの内容を学習し始める。これを「インデックス化」と呼び、AI の提案を正確にする土台になる。

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="コードベースのインデックス化の進行状況インジケーター" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
</Frame>

* プロジェクトを開くと自動でインデックス化が始まる
* プロジェクトの規模に応じて約 1〜15 分かかる
* Cursor がコードを学習するほど、提案は賢くなる
* チーム間でインデックスを共有して時間を節約できる
* 設定（<Kbd>Cmd Shift J</Kbd>）→ Indexing & Docs で進行状況を確認できる

もっと知りたいなら、[インデックス化の仕組み](/ja/context/codebase-indexing)をチェック

<div id="next-steps">
  ## 次のステップ
</div>

Cursor のインストールが終わったら、AI で加速するコーディングをさっそく体験しよう:

* まずは [クイックスタートガイド](/ja/get-started/quickstart) で 5 分で基本を押さえる
* Cursor の仕組みを理解するために [重要な概念](/ja/get-started/concepts) を読む
* [ガイド集](/ja/guides) で Cursor で何が作れるかを探索する
* 問題が起きたら [トラブルシューティングガイド](/ja/troubleshooting/common-issues) で解決策を探す
* [コミュニティに参加](https://cursor.com/community) して他の Cursor ユーザーとつながる



# クイックスタート
Source: https://docs.cursor.com/ja/get-started/quickstart

5分でCursorをはじめよう

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

このクイックスタートでは、Cursor のコア機能を使ったプロジェクトを順番に一緒に見ていくよ。終わる頃には、Tab、Inline Edit、Agent にしっかり慣れてるはず。

<div id="open-a-project-in-cursor">
  ## Cursor でプロジェクトを開く
</div>

手元のプロジェクトを使うか、サンプルをクローンしよう:

<Tabs>
  <Tab title="Clone example project">
    1. git がインストールされていることを確認
    2. サンプルプロジェクトをクローン:

    ```bash  theme={null}
    git clone git@github.com:voxelize/voxelize.git && \
    cd voxelize && \
    cursor .
    ```
  </Tab>

  <Tab title="Use existing project">
    1. Cursor を開く
    2. <Kbd>Cmd O</Kbd> または `cursor <path-to-project>` でプロジェクトフォルダを開く
  </Tab>
</Tabs>

ここではサンプルプロジェクトを使って紹介するけど、ローカルのどんなプロジェクトでも使えるよ。

<div id="autocomplete-with-tab">
  ## [Tab](/ja/kbd#tab) でのオートコンプリート
</div>

Tab は社内で訓練したオートコンプリートモデル。AI アシストでのコーディングにまだ慣れてなくても、気軽に使い始められる。Tab なら次のことができる:

* コードの**複数行やブロック**を一括補完
* 次の補完候補へ、ファイル**内**や**横断**でジャンプ

1. 関数の書き始めを入力する:
   ```javascript  theme={null}
   function calculate
   ```
2. Tab の候補が自動で表示される
3. 候補を採用するには Tab を押す
4. Cursor が引数や関数本体を提案する

<div id="inline-edit-a-selection">
  ## [Inline Edit](/ja/inline-edit) で選択範囲を編集
</div>

1. さっき作成した関数を選択
2. <Kbd>Cmd K</Kbd> を押す
3. 「make this function calculate fibonacci numbers」と入力
4. <Kbd>Return</Kbd> を押して変更を適用
5. Cursor が import とドキュメントを追加

<div id="chat-with-agent">
  ## [Agent](/ja/agent) とチャット
</div>

1. Chat パネルを開く (<Kbd>Cmd I</Kbd>)
2. こう聞く: 「この関数にテストを追加して実行して」
3. Agent がテストファイルを作成し、テストケースを書いて実行してくれる

<div id="bonus">
  ## ボーナス
</div>

高度な機能:

<AccordionGroup>
  <Accordion title="作業を Background Agent に引き継ぐ">
    1. Background Agent のコントロールパネルを開く (<Kbd>Cmd E</Kbd>)
    2. 次のように依頼: "このプロジェクトのバグを見つけて修正して"
    3. [Background Agent](/ja/background-agent) が以下を実行:
       * リモートの仮想マシン (VM) を作成
       * プロジェクトを探索
       * バグを検出
       * 修正案を提案

    変更をレビューして適用。
  </Accordion>

  {" "}

  <Accordion title="ルールを書く">
    1. コマンドパレットを開く (<Kbd>Cmd Shift P</Kbd>) 2. 検索: "New Cursor
       Rule" 3. 名前を付ける (例: `style-guide`) 4. ルールタイプで "Always" を選択 5. スタイルを定義: `変数名は camelCase を優先して使う`
  </Accordion>

  <Accordion title="MCP サーバーをセットアップする">
    1. [MCP ディレクトリ](https://docs.cursor.com/tools) にアクセス
    2. ツールを選ぶ
    3. "Install" をクリック

    サーバーは手動インストールも可能:

    1. Cursor Settings を開く (<Kbd>Cmd Shift J</Kbd>)
    2. "Tools & Integrations" に移動
    3. "New MCP Server" をクリック
  </Accordion>
</AccordionGroup>

<div id="next-steps">
  ## 次のステップ
</div>

詳しく知るには、これらのガイドをチェック:

<CardGroup cols={2}>
  <Card title="Working with Context" href="/ja/guides/working-with-context">
    より良い結果のために効果的なコンテキストを設定しよう
  </Card>

  <Card title="Selecting Models" href="/ja/guides/selecting-models">
    タスクに最適なモデルを選ぼう
  </Card>
</CardGroup>

[Cursor のコンセプト](/ja/get-started/concepts)をひと通り学んで、さっそく作り始めよう!




---

**Navigation:** [← Previous](./19-panduan-pemecahan-masalah.md) | [Index](./index.md) | [Next →](./21-データサイエンス.md)