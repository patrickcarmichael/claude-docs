---
title: "Python"
source: "https://docs.cursor.com/ja/guides/languages/python"
language: "ja"
language_name: "Japanese"
---

# Python
Source: https://docs.cursor.com/ja/guides/languages/python

拡張機能とリンターでPython開発環境をセットアップ

<Note>
  このガイドは
  [Jack Fields](https://x.com/OrdinaryInds)
  の
  [記事](https://medium.com/ordinaryindustries/the-ultimate-vs-code-setup-for-python-538026b34d94)
  「VS CodeでのPython開発環境の究極セットアップ」から大きくインスピレーションを受けてる。詳しくは彼の記事もチェックしてね。
</Note>

<div id="prerequisites">
  ## 前提条件
</div>

始める前に、次を用意しておいてね:

* [Python](https://python.org) がインストールされていること（3.8以上を推奨）
* バージョン管理用の [Git](https://git-scm.com/)
* Cursor が最新バージョンにアップデート済みであること

<div id="essential-extensions">
  ## 必須拡張機能
</div>

以下の拡張機能で、Cursor を Python 開発向けにフル機能で使えるように構成できる。構文ハイライト、Lint、デバッグ、ユニットテストを提供するよ。

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Microsoft によるコア言語サポート
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    高速な Python 言語サーバー
  </Card>

  <Card title="Python Debugger" icon="bug" href="cursor:extension/ms-python.debugpy">
    進化したデバッグ機能
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Python のリンター兼フォーマッター
  </Card>
</CardGroup>

<div id="advanced-python-tooling">
  ### 高度な Python ツーリング
</div>

上記はこれまで Cursor における Python 開発で最も人気の拡張機能だったけど、Python 開発をさらに活用できるよう、追加の拡張機能もいくつか用意してる。

<div id="uv-python-environment-manager">
  #### `uv` - Python 環境マネージャー
</div>

[uv](https://github.com/astral-sh/uv) はモダンな Python パッケージマネージャーで、pip の置き換えとして使えるだけでなく、仮想環境の作成と管理にも使える。

uv をインストールするには、ターミナルで次のコマンドを実行してね:

```bash  theme={null}
pip install uv
```

<div id="ruff-python-linter-and-formatter">
  #### `ruff` - Pythonのリンター兼フォーマッター
</div>

[Ruff](https://docs.astral.sh/ruff/) は、プログラミングエラーの検出、コーディング規約の順守支援、リファクタリング提案ができる、モダンな Python のリンター兼フォーマッター。コード整形では Black と併用できる。

Ruff をインストールするには、ターミナルで次のコマンドを実行:

```bash  theme={null}
pip install ruff
```

<div id="cursor-configuration">
  ## Cursor の設定
</div>

<div id="1-python-interpreter">
  ### 1. Python インタープリタ
</div>

Cursor で Python インタープリタを設定しよう:

1. Command Palette を開く（Cmd/Ctrl + Shift + P）
2. 「Python: Select Interpreter」を検索
3. Python インタープリタを選ぶ（仮想環境を使っている場合はその環境を選ぶ）

<div id="2-code-formatting">
  ### 2. コード整形
</div>

Black で自動コード整形を設定しよう:

<Note>
  Black はコードフォーマッタで、コードを自動的に整形して
  一貫したスタイルに保ってくれる。設定は不要で、Python コミュニティで
  広く採用されている。
</Note>

Black をインストールするには、ターミナルで次のコマンドを実行:

```bash  theme={null}
pip install black
```

次に、コード整形に Black を使うよう Cursor を設定するため、`settings.json` に次を追加してね：

```json  theme={null}
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.formatting.blackArgs": ["--line-length", "88"]
}
```

<div id="3-linting">
  ### 3. Linting
</div>

PyLint を使えば、プログラミングエラーの検出、コーディング規約の順守、リファクタリングの提案までカバーできる。

PyLint をインストールするには、ターミナルで次のコマンドを実行してね:

```bash  theme={null}
pip install pylint
```

```json  theme={null}
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.lintOnSave": true
}
```

<div id="4-type-checking">
  ### 4. 型チェック
</div>

lint に加えて、MyPy を使って型エラーをチェックできる。

MyPy をインストールするには、ターミナルで次のコマンドを実行して：

```bash  theme={null}
pip install mypy
```

```json  theme={null}
{
  "python.linting.mypyEnabled": true
}
```

<div id="debugging">
  ## デバッグ
</div>

Cursor には Python 向けの強力なデバッグ機能がある:

1. ガターをクリックしてブレークポイントを設定
2. Debug パネルを使う（Cmd/Ctrl + Shift + D）
3. `launch.json` を設定してカスタムデバッグ構成を作成

<div id="recommended-features">
  ## おすすめ機能
</div>

<CardGroup cols={3}>
  <Card title="Tab Completion" icon="wand-magic-sparkles" href="/ja/tab/overview">
    操作の意図を理解して提案するスマートなコード補完
  </Card>

  <Card title="Chat" icon="comments" href="/ja/chat/overview">
    自然な対話でコードを読み解いて探索できる
  </Card>

  <Card title="Agent" icon="robot" href="/ja/chat/agent">
    AI と一緒に複雑な開発タスクをこなす
  </Card>

  <Card title="Context" icon="network-wired" href="/ja/context/model-context-protocol">
    外部サービスから必要なコンテキストを取り込む
  </Card>

  <Card title="Auto-Imports" icon="file-import" href="/ja/tab/auto-import">
    コーディング中に必要なモジュールを自動でインポート
  </Card>

  <Card title="AI Review" icon="check-double" href="/ja/tab/overview#quality">
    Cursor が常に AI でコード品質をチェック
  </Card>
</CardGroup>

<div id="framework-support">
  ## フレームワーク対応
</div>

Cursor は主要な Python フレームワークとシームレスに連携する：

* **Web フレームワーク**: Django、Flask、FastAPI
* **データサイエンス**: Jupyter、NumPy、Pandas
* **機械学習**: TensorFlow、PyTorch、scikit-learn
* **テスト**: pytest、unittest
* **API**: requests、aiohttp
* **データベース**: SQLAlchemy、psycopg2

---

← Previous: [JavaScript & TypeScript](./javascript-typescript.md) | [Index](./index.md) | Next: [iOS & macOS (Swift)](./ios-macos-swift.md) →