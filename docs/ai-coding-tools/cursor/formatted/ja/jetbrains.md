---
title: "JetBrains"
source: "https://docs.cursor.com/ja/guides/migration/jetbrains"
language: "ja"
language_name: "Japanese"
---

# JetBrains
Source: https://docs.cursor.com/ja/guides/migration/jetbrains

なじみのあるツールで JetBrains の IDE から Cursor へ移行

Cursor は、JetBrains の IDE を置き換えられる、最新の AI 搭載のコーディング体験を提供する。最初は違いを感じるかもしれないが、Cursor の VS Code ベースの基盤は強力な機能と幅広いカスタマイズ性を備えている。

<div id="editor-components">
  ## エディターコンポーネント
</div>

<div id="extensions">
  ### 拡張機能
</div>

JetBrains IDE は、対象の言語やフレームワーク向けにあらかじめ最適化されていて、とても優れたツール。

Cursor は少し違う。箱から出した直後はまっさらなキャンバスだから、IDE が想定している言語やフレームワークに縛られず、好きなようにカスタマイズできる。

Cursor は豊富な拡張機能エコシステムにアクセスできて、JetBrains IDE が提供するほぼすべての機能（それ以上も！）を拡張で再現できる。

以下の人気拡張をチェック:

<CardGroup cols={4}>
  <Card title="Remote SSH" icon="network-wired" href="cursor:extension/anysphere.remote-ssh">
    SSH 拡張
  </Card>

  <Card title="Project Manager" icon="folder-tree" href="cursor:extension/alefragnani.project-manager">
    複数プロジェクトを管理
  </Card>

  <Card title="GitLens" icon="git" href="cursor:extension/eamodio.gitlens">
    強力な Git 連携
  </Card>

  <Card title="Local History" icon="clock-rotate-left" href="cursor:extension/xyz.local-history">
    ローカルのファイル変更を追跡
  </Card>

  <Card title="Error Lens" icon="bug" href="cursor:extension/usernamehw.errorlens">
    インラインでエラーをハイライト
  </Card>

  <Card title="ESLint" icon="code-compare" href="cursor:extension/dbaeumer.vscode-eslint">
    コードのリント
  </Card>

  <Card title="Prettier" icon="wand-magic-sparkles" href="cursor:extension/esbenp.prettier-vscode">
    コード整形
  </Card>

  <Card title="Todo Tree" icon="folder-tree" href="cursor:extension/Gruntfuggly.todo-tree">
    TODO と FIXME を追跡
  </Card>
</CardGroup>

<div id="keyboard-shortcuts">
  ### キーボードショートカット
</div>

Cursor にはショートカットマネージャーが内蔵されていて、お気に入りのキーボードショートカットをアクションに割り当てられる。

この拡張を使えば、JetBrains IDE のショートカットをほぼそのまま Cursor に持ち込める！
好みに合わせた設定方法は、拡張のドキュメントを必ず読んでね:

<Card title="IntelliJ IDEA Keybindings" icon="keyboard" href="cursor:extension/k--kato.intellij-idea-keybindings">
  この拡張を入れて、JetBrains IDE のショートカットを Cursor で使おう。
</Card>

<Note>
  よく違いが出る共通ショートカット:

  * Find Action: ⌘/Ctrl+Shift+P  (vs. ⌘/Ctrl+Shift+A)
  * Quick Fix: ⌘/Ctrl+.  (vs. Alt+Enter)
  * Go to File: ⌘/Ctrl+P  (vs. ⌘/Ctrl+Shift+N)
</Note>

<div id="themes">
  ### テーマ
</div>

コミュニティ製テーマで、好きな JetBrains IDE の見た目と使い心地を Cursor で再現しよう。

標準の Darcula テーマを選ぶか、JetBrains ツールのシンタックスハイライトに合わせたテーマを選べる。

<CardGroup cols={1}>
  <Card title="JetBrains - Darcula Theme" icon="moon" horizontal href="cursor:extension/rokoroku.vscode-theme-darcula">
    クラシックな JetBrains Darcula のダークテーマを体験
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="JetBrains PyCharm" icon="python" horizontal href="cursor:extension/gabemahoney.pycharm-dark-theme-for-python" />

  <Card title="IntelliJ" icon="java" horizontal href="cursor:extension/compassak.intellij-idea-new-ui" />

  <Card title="JetBrains Fleet" icon="code" horizontal href="cursor:extension/MichaelZhou.fleet-theme" />

  <Card title="JetBrains Rider" icon="hashtag" horizontal href="cursor:extension/muhammad-sammy.rider-theme" />
</CardGroup>

<CardGroup cols={1}>
  <Card title="JetBrains Icons" icon="icons" horizontal href="cursor:extension/ardonplay.vscode-jetbrains-icon-theme">
    見慣れた JetBrains のファイル／フォルダーアイコンを入手
  </Card>
</CardGroup>

<div id="font">
  ### フォント
</div>

JetBrains らしい体験を仕上げるなら、公式の JetBrains Mono フォントを使おう:

1. JetBrains Mono フォントをダウンロードしてシステムにインストール

<CardGroup cols={1}>
  <Card title="Download JetBrains Mono" icon="link" horizontal href="https://www.jetbrains.com/lp/mono/" />
</CardGroup>

2. フォントをインストールしたら Cursor を再起動
3. Cursor の Settings を開く (⌘/Ctrl + ,)
4. 「Font Family」を検索
5. フォントファミリーを 'JetBrains Mono' に設定

<Note>
  最適な体験のために、設定で "editor.fontLigatures": true を指定してフォント合字を有効にしよう。
</Note>

<div id="ide-specific-migration">
  ## IDEごとの移行
</div>

多くのユーザーは、対象の言語やフレームワークに最初から最適化されたサポートがある点でJetBrains製IDEを気に入ってる。Cursorはちょっと違う——初期状態は白紙のキャンバス。IDEが想定している言語やフレームワークに縛られず、好きなようにカスタマイズできる。

CursorはすでにVS Codeの拡張機能エコシステムにアクセスできて、JetBrains製IDEが提供する機能のほぼすべて（それ以上も！）を拡張機能で再現できる。

以下は各JetBrains IDE向けのおすすめ拡張だよ。

<div id="intellij-idea-java">
  ### IntelliJ IDEA (Java)
</div>

<CardGroup cols={2}>
  <Card title="Language Support for Java" icon="java" href="cursor:extension/redhat.java">
    Javaのコア言語機能
  </Card>

  <Card title="Debugger for Java" icon="bug" href="cursor:extension/vscjava.vscode-java-debug">
    Javaのデバッグサポート
  </Card>

  <Card title="Test Runner for Java" icon="vial" href="cursor:extension/vscjava.vscode-java-test">
    Javaテストの実行とデバッグ
  </Card>

  <Card title="Maven for Java" icon="box" href="cursor:extension/vscjava.vscode-maven">
    Mavenサポート
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Project Manager for Java" icon="folder-tree" href="cursor:extension/vscjava.vscode-java-dependency" horizontal>
    プロジェクト管理ツール
  </Card>
</CardGroup>

<Warning>
  主な相違点:

  * Build/Run構成はlaunch.jsonで管理
  * Spring Bootツールは["Spring Boot Extension Pack"](cursor:extension/vmware.vscode-boot-dev-pack)拡張で提供
  * Gradleサポートは["Gradle for Java"](cursor:extension/vscjava.vscode-gradle)拡張経由
</Warning>

<div id="pycharm-python">
  ### PyCharm (Python)
</div>

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Pythonのコアサポート
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    高速な型チェック
  </Card>

  <Card title="Jupyter" icon="notebook" href="cursor:extension/ms-toolsai.jupyter">
    Notebookサポート
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Pythonのフォーマッタとリンター
  </Card>
</CardGroup>

<Note>
  主な相違点:

  * 仮想環境はコマンドパレットで管理
  * デバッグ構成はlaunch.json
  * 依存関係管理はrequirements.txtまたはPoetry
</Note>

<div id="webstorm-javascripttypescript">
  ### WebStorm (JavaScript/TypeScript)
</div>

<CardGroup cols={2}>
  <Card title="JavaScript and TypeScript Nightly" icon="js" href="cursor:extension/ms-vscode.vscode-typescript-next">
    最新の言語機能
  </Card>

  <Card title="ES7+ React/Redux Snippets" icon="react" href="cursor:extension/dsznajder.es7-react-js-snippets">
    React開発
  </Card>

  <Card title="Vue Language Features" icon="vuejs" href="cursor:extension/Vue.volar">
    Vue.jsサポート
  </Card>

  <Card title="Angular Language Service" icon="angular" href="cursor:extension/Angular.ng-template">
    Angular開発
  </Card>
</CardGroup>

<Info>
  WebStormの機能の大半はCursor/VS Codeに標準で含まれているよ。例:

  * npmスクリプトビュー
  * デバッグ
  * Git連携
  * TypeScriptサポート
</Info>

<div id="phpstorm-php">
  ### PhpStorm (PHP)
</div>

<CardGroup cols={2}>
  <Card title="PHP Intelephense" icon="php" href="cursor:extension/bmewburn.vscode-intelephense-client">
    PHP言語サーバー
  </Card>

  <Card title="PHP Debug" icon="bug" href="cursor:extension/xdebug.php-debug">
    Xdebug連携
  </Card>

  <Card title="PHP Intellisense" icon="brain" href="cursor:extension/felixfbecker.php-intellisense">
    コードインテリジェンス
  </Card>

  <Card title="PHP DocBlocker" icon="comment-dots" href="cursor:extension/neilbrayfield.php-docblocker">
    ドキュメント作成ツール
  </Card>
</CardGroup>

<Note>
  主な相違点:

  * Xdebugの設定はlaunch.json経由
  * Composer連携はターミナル経由
  * データベースツールは["SQLTools"](cursor:extension/mtxr.sqltools)拡張
</Note>

<div id="rider-net">
  ### Rider (.NET)
</div>

<CardGroup cols={2}>
  <Card title="C#" icon="code" href="cursor:extension/anysphere.csharp">
    C# の基本サポート
  </Card>

  <Card title="DotRush" icon="toolbox" href="cursor:extension/nromanov.dotrush">
    オープンソースの C# 開発環境
  </Card>

  <Card title="ReSharper Plugin" icon="box" href="https://www.jetbrains.com/help/resharper-vscode/Get_started.html#installation">
    JetBrains 製 C# プラグイン
  </Card>

  <Card title=".NET Install Tool" icon="box-open" href="cursor:extension/ms-dotnettools.vscode-dotnet-runtime">
    .NET SDK の管理
  </Card>
</CardGroup>

<Warning>
  主な違い:

  * ファイル エクスプローラーからのソリューション エクスプローラー
  * CLI または拡張機能を使った NuGet パッケージ管理
  * テスト エクスプローラー経由のテスト ランナー統合
</Warning>

<div id="goland-go">
  ### GoLand (Go)
</div>

<CardGroup cols={1}>
  <Card title="Go" icon="golang" href="cursor:extension/golang.Go">
    公式 Go 拡張機能
  </Card>
</CardGroup>

<Note>
  主な違い:

  * Go ツールのインストールが自動で促される
  * launch.json を使ったデバッグ
  * go.mod と統合されたパッケージ管理
</Note>

<div id="tips-for-a-smooth-transition">
  ## スムーズに移行するためのヒント
</div>

<Steps>
  <Step title="コマンドパレットを使う">
    コマンドを探すには <kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> を押す
  </Step>

  <Step title="AI 機能">
    コード補完やリファクタリングに Cursor の AI 機能を活用する
  </Step>

  <Step title="設定をカスタマイズ">
    最適なワークフローのために settings.json を細かく調整する
  </Step>

  <Step title="ターミナル統合">
    コマンドライン操作には内蔵ターミナルを使う
  </Step>

  <Step title="拡張機能">
    追加ツールは VS Code Marketplace をチェックする
  </Step>
</Steps>

<Info>
  一部のワークフローは異なるかもしれないけど、Cursor は従来の IDE を超える生産性を引き出す強力な AI 支援コーディング機能を備えてる。
</Info>

---

← Previous: [iOS & macOS (Swift)](./ios-macos-swift.md) | [Index](./index.md) | Next: [VS Code](./vs-code.md) →