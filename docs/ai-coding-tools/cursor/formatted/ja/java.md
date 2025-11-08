---
title: "Java"
source: "https://docs.cursor.com/ja/guides/languages/java"
language: "ja"
language_name: "Japanese"
---

# Java
Source: https://docs.cursor.com/ja/guides/languages/java

JDK、拡張機能、ビルドツールで Java 開発環境をセットアップする

このガイドでは、Cursor を Java 開発向けにセットアップする方法を解説する。JDK の導入、必要な拡張機能のインストール、デバッグ、Java アプリの実行、Maven や Gradle などのビルドツールの連携までカバー。IntelliJ や VS Code に近いワークフロー機能についても取り上げる。

<Note>
  始める前に、Cursor をインストールして最新バージョンにアップデートしておいてね。
</Note>

<div id="setting-up-java-for-cursor">
  ## Cursor 用の Java セットアップ
</div>

<div id="java-installation">
  ### Java のインストール
</div>

Cursor をセットアップする前に、マシンに Java をインストールしておく必要があるよ。

<Warning>
  Cursor には Java コンパイラが同梱されていないから、まだなら JDK をインストールしてね。
</Warning>

<CardGroup cols={1}>
  <Card title="Windows Installation" icon="windows">
    JDK（例: OpenJDK、Oracle JDK、Microsoft Build of OpenJDK）をダウンロードしてインストールする。

    <br />

    JAVA\_HOME を設定して、PATH に JAVA\_HOME\bin を追加する。
  </Card>

  <Card title="macOS Installation" icon="apple">
    Homebrew（`brew install openjdk`）でインストールするか、インストーラをダウンロードする。

    <br />

    JAVA\_HOME がインストール済みの JDK を指すように設定してね。
  </Card>

  <Card title="Linux Installation" icon="linux">
    パッケージマネージャ（`sudo apt install openjdk-17-jdk` など）を使うか、SDKMAN でインストールする。
  </Card>
</CardGroup>

インストールを確認するには、次を実行:

```bash  theme={null}
java -version
javac -version
```

<Info>
  Cursor が JDK を検出できない場合は、settings.json で手動設定してね：
</Info>

```json  theme={null}
{
  "java.jdt.ls.java.home": "/path/to/jdk",
  "java.configuration.runtimes": [
    {
      "name": "JavaSE-17",
      "path": "/path/to/jdk-17",
      "default": true
    }
  ]
}
```

<Warning>変更を反映するには Cursor を再起動して。</Warning>

<div id="cursor-setup">
  ### Cursor のセットアップ
</div>

<Info>Cursor は VS Code の拡張機能に対応。次を手動でインストールしてね：</Info>

<CardGroup cols={2}>
  <Card title="Extension Pack for Java" icon="java" href="cursor:extension/vscjava.vscode-java-pack">
    Java の言語サポート、デバッガー、テストランナー、Maven サポート、プロジェクトマネージャーを含む
  </Card>

  <Card title="Gradle for Java" icon="gears" href="cursor:extension/vscjava.vscode-gradle">
    Gradle ビルドシステムでの作業に必須
  </Card>

  <Card title="Spring Boot Extension Pack" icon="leaf" href="cursor:extension/vmware.vscode-boot-dev-pack">
    Spring Boot 開発に必須
  </Card>

  <Card title="Kotlin" icon="window" href="cursor:extension/fwcd.kotlin">
    Kotlin アプリ開発に必要
  </Card>
</CardGroup>

<div id="configure-build-tools">
  ### ビルドツールの設定
</div>

<div id="maven">
  #### Maven
</div>

Maven がインストール済みか確認してね（`mvn -version`）。必要なら [maven.apache.org](https://maven.apache.org/download.cgi) からインストール：

1. バイナリアーカイブをダウンロード
2. 任意の場所に展開
3. 展開先フォルダを MAVEN\_HOME 環境変数に設定
4. %MAVEN\_HOME%\bin（Windows）または \$MAVEN\_HOME/bin（Unix）を PATH に追加

<div id="gradle">
  #### Gradle
</div>

Gradle がインストール済みか確認してね（`gradle -version`）。必要なら [gradle.org](https://gradle.org/install/) からインストール：

1. バイナリ配布物をダウンロード
2. 任意の場所に展開
3. 展開先フォルダを GRADLE\_HOME 環境変数に設定
4. %GRADLE\_HOME%\bin（Windows）または \$GRADLE\_HOME/bin（Unix）を PATH に追加

または、Gradle Wrapper を使えば、適切な Gradle バージョンを自動でダウンロードして使用できる：

<div id="running-and-debugging">
  ## 実行とデバッグ
</div>

セットアップが完了したら、Java コードを実行してデバッグしよう。
ニーズに合わせて、次の方法が使えるよ:

<CardGroup cols={2}>
  <Card title="Run" icon="play">
    どの main メソッドの上にも表示される「Run」リンクをクリックして、
    プログラムを素早く実行
  </Card>

  <Card title="Debug" icon="bug">
    Run and Debug サイドバーを開いて、Run ボタンで
    アプリケーションを起動
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Terminal" icon="terminal">
    コマンドラインから Maven または Gradle のコマンドで実行
  </Card>

  <Card title="Spring Boot" icon="leaf">
    Spring Boot Dashboard 拡張機能から
    Spring Boot アプリケーションを直接起動
  </Card>
</CardGroup>

<div id="java-x-cursor-workflow">
  ## Java x Cursor ワークフロー
</div>

Cursor の AI 機能は、Java の開発ワークフローを大きく底上げしてくれる。ここでは、Java 向けに Cursor の機能を活用するコツを紹介する:

<CardGroup cols={2}>
  <Card title="Tab Completion" icon="arrow-right">
    <div className="text-sm">
      メソッドやシグネチャ、getters/setters といった Java のボイラープレートをスマートに補完。
    </div>
  </Card>

  <Card title="Agent Mode" icon="pen-to-square">
    <div className="text-sm">
      デザインパターンの実装、コードのリファクタリング、適切な継承を備えたクラスの生成。
    </div>
  </Card>

  <Card title="Inline Edit" icon="code">
    <div className="text-sm">
      フローを崩さずにメソッドをすばやくインライン編集、エラー修正、ユニットテストの生成。
    </div>
  </Card>

  <Card title="Chat" icon="message">
    <div className="text-sm">
      Java の概念の理解を助けたり、例外をデバッグしたり、フレームワークの機能を把握したりできる。
    </div>
  </Card>
</CardGroup>

<div id="example-workflows">
  ### 例となるワークフロー
</div>

1. **Java ボイラープレートの生成**\
   [Tab completion](/ja/tab/overview) を使って、コンストラクタ、getters/setters、equals/hashCode メソッドなどの反復的な Java パターンを素早く生成。

2. **複雑な Java 例外のデバッグ**\
   難解な Java スタックトレースに当たったら、ハイライトして [Ask](/ja/chat/overview) で根本原因の説明と修正案を聞こう。

3. **レガシー Java コードのリファクタリング**\
   [Agent mode](/ja/chat/agent) を使って古い Java コードをモダナイズ。無名クラスをラムダに変換、新しい Java 言語機能へのアップグレード、あるいはデザインパターンの実装。

4. **フレームワーク開発**\
   @docs でドキュメントを Cursor のコンテキストに追加して、Cursor 全体でフレームワーク特化のコードを生成しよう。

---

← Previous: [ドキュメントの活用](./section.md) | [Index](./index.md) | Next: [JavaScript & TypeScript](./javascript-typescript.md) →