---
title: "Memories"
source: "https://docs.cursor.com/ja/context/memories"
language: "ja"
language_name: "Japanese"
---

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

---

← Previous: [Model Context Protocol (MCP)](./model-context-protocol-mcp.md) | [Index](./index.md) | Next: [ルール](./section.md) →