---
title: "@Linter Errors"
source: "https://docs.cursor.com/ja/context/@-symbols/@-linter-errors"
language: "ja"
language_name: "Japanese"
---

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

---

← Previous: [@Link](./link.md) | [Index](./index.md) | Next: [@Past Chats](./past-chats.md) →