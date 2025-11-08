---
title: "Diffs & Review"
source: "https://docs.cursor.com/ja/agent/review"
language: "ja"
language_name: "Japanese"
---

# Diffs & Review
Source: https://docs.cursor.com/ja/agent/review

AIエージェントが提案したコード変更をレビューして管理する

Agent がコード変更を生成すると、追加と削除を色分けした行で表示するレビュー用インターフェースに並ぶ。これで、どの変更をコードベースに適用するかを確認してコントロールできる。

レビュー用インターフェースは、見慣れた diff 形式でコード変更を表示する:

<div id="diffs">
  ## Diffs
</div>

<div className="full-width-table">
  | Type              | Meaning    | Example                                                                                               |
  | :---------------- | :--------- | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | 新規コードの追加   | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | コードの削除     | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | 変更のない周辺コード | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## レビュー
</div>

生成が完了すると、先に進む前にすべての変更を確認するよう促すプロンプトが表示される。これで、どこが変更されるかを俯瞰できる。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="入力レビューインターフェース" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### ファイルごと
</div>

画面下部にフローティングのレビュー バーが表示され、次の操作ができる:

* 現在のファイルの変更を**承認**または**却下**する
* 保留中の変更がある**次のファイル**へ移動する
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      お使いのブラウザは video タグをサポートしていません。
    </video>
  </Frame>

<div id="selective-acceptance">
  ### 選択的な承認
</div>

細かく制御するには:

* 変更の大半を承認したい場合: 不要な行を却下してから **Accept all** をクリック
* 変更の大半を却下したい場合: 必要な行を承認してから **Reject all** をクリック

<div id="review-changes">
  ## 変更内容を確認
</div>

エージェントの応答の最後で **Review changes** ボタンをクリックすると、変更の差分全体を確認できる。

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>

---

← Previous: [企画](./section.md) | [Index](./index.md) | Next: [Terminal](./terminal.md) →