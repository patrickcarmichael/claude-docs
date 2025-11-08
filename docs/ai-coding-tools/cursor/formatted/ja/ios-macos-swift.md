---
title: "iOS & macOS (Swift)"
source: "https://docs.cursor.com/ja/guides/languages/swift"
language: "ja"
language_name: "Japanese"
---

# iOS & macOS (Swift)
Source: https://docs.cursor.com/ja/guides/languages/swift

Swift開発のためにCursorをXcodeと連携する

CursorでのSwift開発へようこそ！iOSアプリ、macOSアプリケーション、サーバーサイドのSwiftプロジェクトまで、しっかりサポートするよ。このガイドでは、基本から始めて高度な機能へと進みながら、CursorでSwift環境をセットアップする方法を紹介する。

<div id="basic-workflow">
  ## 基本的なワークフロー
</div>

Swift で Cursor を使ういちばんシンプルな方法は、ビルドやアプリの実行には Xcode を使いつつ、メインのコードエディタとして Cursor を使うこと。次のような便利な機能が使えるよ:

* スマートなコード補完
* AI ベースのコーディング支援（どの行でも [CMD+K](/ja/inline-edit/overview) を試してみて）
* [@Docs](/ja/context/@-symbols/@-docs) でドキュメントにすばやくアクセス
* シンタックスハイライト
* 基本的なコードナビゲーション

ビルドや実行が必要になったら、Xcode に切り替えるだけ。このワークフローは、デバッグやデプロイは慣れた Xcode のツールを使いながら、Cursor の AI 機能を活用したい開発者に最適だよ。

<div id="hot-reloading">
  ### ホットリロード
</div>

Xcode でフォルダを直接開くのではなく、workspace や project を使っている場合、Cursor で行った変更や Xcode の外で行われた変更を Xcode が無視してしまうことがある。

フォルダを Xcode で開けば解消できるけど、Swift の開発ワークフローとしては project を使う必要がある場合もある。

そんなときの有力な解決策が [Inject](https://github.com/krzysztofzablocki/Inject)。Swift 向けのホットリロードライブラリで、変更が加わるとリアルタイムでアプリを「ホットリロード」して更新できる。これは Xcode の workspace/project に起因する問題の副作用を受けず、Cursor での変更がアプリに即座に反映されるよ。

<CardGroup cols={1}>
  <Card title="Inject - Swift のためのホットリロード" horizontal icon="fire" href="https://github.com/krzysztofzablocki/Inject">
    Swift プロジェクトでの Inject の概要と使い方をチェックしよう。
  </Card>
</CardGroup>

<div id="advanced-swift-development">
  ## 高度な Swift 開発
</div>

<Note>
  このセクションは、[Thomas
  Ricouard](https://x.com/Dimillian) と、iOS 開発での Cursor の使い方を解説した
  [記事](https://dimillian.medium.com/how-to-use-cursor-for-ios-development-54b912c23941)
  に大きくインスパイアされてるよ。詳しくは記事をチェックして、Swift コンテンツが気に入ったらフォローしてみて。
</Note>

同時に開くエディタを 1 つに絞って、Xcode と Cursor の切り替えを避けたいなら、[Sweetpad](https://sweetpad.hyzyla.dev/) のような拡張機能で、Cursor を Xcode のビルドシステムに直接統合できる。

Sweetpad は、Xcode の機能を損なうことなく、Cursor から Swift プロジェクトを直接ビルド・実行・デバッグできる強力な拡張機能だよ。

Sweetpad を使い始めるには、まず Mac に Xcode をインストールしておく必要がある—Swift 開発の基盤だからね。Xcode は [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835) からダウンロードできる。Xcode のセットアップができたら、いくつかの必須ツールで Cursor の開発体験を強化していこう。

ターミナルを開いて、次を実行してね:

```bash  theme={null}

---

← Previous: [Python](./python.md) | [Index](./index.md) | Next: [JetBrains](./jetbrains.md) →