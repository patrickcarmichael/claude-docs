---
title: "JavaScript & TypeScript"
source: "https://docs.cursor.com/ja/guides/languages/javascript"
language: "ja"
language_name: "Japanese"
---

# JavaScript & TypeScript
Source: https://docs.cursor.com/ja/guides/languages/javascript

フレームワーク対応の JavaScript／TypeScript 開発

Cursor での JavaScript／TypeScript 開発へようこそ！このエディタは拡張機能エコシステムを通じて JS/TS 開発を強力にサポートしてる。ここでは Cursor を最大限に活用するために知っておきたいポイントを紹介する。

<div id="essential-extensions">
  ## 必須拡張機能
</div>

Cursor は好きな拡張機能と問題なく使えるけど、これから始めるなら次をおすすめするよ:

* **ESLint** - Cursor の AI を使ったリント修正機能に必須
* **JavaScript and TypeScript Language Features** - 言語サポートと IntelliSense を強化
* **Path Intellisense** - ファイルパスの賢い補完

<div id="cursor-features">
  ## Cursor の機能
</div>

Cursor は既存の JavaScript/TypeScript ワークフローを次の機能で強化するよ:

* **Tab Completions**: プロジェクト構成を理解するコンテキスト対応のコード補完
* **Automatic Imports**: 使った瞬間にライブラリを自動インポート
* **Inline Editing**: どの行でも `CMD+K` で正しい構文のまま編集
* **Composer Guidance**: Composer で複数ファイルにまたがってコードを計画・編集

<div id="framework-intelligence-with-docs">
  ### @Docs によるフレームワークインテリジェンス
</div>

Cursor の @Docs 機能は、AI が参照できるカスタムドキュメントソースを追加して、JavaScript 開発をさらに加速できる。MDN、Node.js、好きなフレームワークのドキュメントを追加して、より正確で文脈に沿ったコード提案を受け取ろう。

<Card title="Learn more about @Docs" icon="book" href="/ja/context/@-symbols/@-docs">
  Cursor でカスタムドキュメントソースを追加・管理する方法をチェックしよう。
</Card>

<div id="automatic-linting-resolution">
  ### 自動リンティング解決
</div>

Cursor の目玉のひとつが、Linter 拡張機能とのシームレスな統合。\
ESLint のような linter をセットアップして、"Iterate on Lints" 設定を有効にしておこう。

そのうえで Composer の Agent モードを使うと、AI が問い合わせに回答してコード変更を行ったあと、linter の出力を自動で読み取り、見落としていたかもしれない lint エラーの修正を試みるよ。

<div id="framework-support">
  ## フレームワーク対応
</div>

Cursor は、次の主要な JavaScript フレームワークやライブラリとシームレスに連携するよ:

### React & Next.js

* コンポーネントに最適化されたインテリジェント提案つきの完全な JSX/TSX 対応
* Next.js の Server Components と API Routes を理解したインテリジェンス
* 推奨: [**React Developer Tools**](cursor:extension/msjsdiag.vscode-react-native) 拡張機能

<div id="vuejs">
  ### Vue.js
</div>

* Volar 連携によるテンプレート構文サポート
* コンポーネントの補完と型チェック
* 推奨: [**Vue Language Features**](cursor:extension/vue.volar)

<div id="angular">
  ### Angular
</div>

* テンプレート検証と TypeScript デコレーター対応
* コンポーネント／サービスの生成
* 推奨: [**Angular Language Service**](cursor:extension/Angular.ng-template)

<div id="svelte">
  ### Svelte
</div>

* コンポーネント構文のハイライトとインテリジェント補完
* reactive 文と store の提案
* 推奨: [**Svelte for VS Code**](cursor:extension/svelte.svelte-vscode)

<div id="backend-frameworks-expressnestjs">
  ### バックエンドフレームワーク（Express/NestJS）
</div>

* ルーティングとミドルウェアのインテリジェンス
* NestJS 向け TypeScript デコレーター対応
* API テストツールとの連携

覚えておいて、Cursor の AI 機能はこれらすべてのフレームワークでしっかり機能し、各フレームワークのパターンやベストプラクティスを踏まえた関連性の高い提案をしてくれる。AI は、コンポーネント作成から複雑なリファクタリングまで、プロジェクトの既存パターンを尊重しながら手助けするよ。

---

← Previous: [Java](./java.md) | [Index](./index.md) | Next: [Python](./python.md) →