---
title: "Bugbot"
source: "https://docs.cursor.com/ja/bugbot"
language: "ja"
language_name: "Japanese"
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

---

← Previous: [Web とモバイル](./web.md) | [Index](./index.md) | Next: [コードレビュー](./section.md) →