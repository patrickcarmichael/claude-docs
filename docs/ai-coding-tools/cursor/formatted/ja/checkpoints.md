---
title: "Checkpoints"
source: "https://docs.cursor.com/ja/agent/chat/checkpoints"
language: "ja"
language_name: "Japanese"
---

# Checkpoints
Source: https://docs.cursor.com/ja/agent/chat/checkpoints

Agent の変更後に以前の状態を保存・復元

Checkpoints は、Agent がコードベースに加えた変更を自動でスナップショット化する機能。必要に応じて Agent の変更を取り消せる。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## チェックポイントの復元
</div>

復元方法は2つ:

1. **入力ボックスから**: 過去のリクエストで `Restore Checkpoint` ボタンをクリック
2. **メッセージから**: メッセージにホバーすると表示される「+」ボタンをクリック

<Warning>
  チェックポイントはバージョン管理ではないよ。恒久的な履歴には Git を使ってね。
</Warning>

<div id="how-they-work">
  ## 動作概要
</div>

* Git とは別にローカルに保存
* Agent による変更のみを追跡（手動編集は対象外）
* 自動でクリーンアップ

<Note>
  手動編集は追跡されないよ。チェックポイントは Agent の変更にだけ使ってね。
</Note>

<div id="faq">
  ## よくある質問
</div>

<AccordionGroup>
  <Accordion title="チェックポイントはGitに影響する？">
    しないよ。Gitの履歴とは別物だよ。
  </Accordion>

  {" "}

  <Accordion title="どれくらいの期間保持される？">
    現在のセッションと直近の履歴まで。自動でクリーンアップされるよ。
  </Accordion>

  <Accordion title="手動で作成できる？">
    できないよ。Cursorが自動で作成するよ。
  </Accordion>
</AccordionGroup>

{" "}

---

← Previous: [Apply](./apply.md) | [Index](./index.md) | Next: [コマンド](./section.md) →