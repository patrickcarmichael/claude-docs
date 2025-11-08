---
title: "Model Context Protocol (MCP)"
source: "https://docs.cursor.com/ja/context/mcp"
language: "ja"
language_name: "Japanese"
---

# Model Context Protocol (MCP)
Source: https://docs.cursor.com/ja/context/mcp

MCP を使って外部ツールやデータソースを Cursor に接続する

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="what-is-mcp">
  ## MCP とは？
</div>

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) は、Cursor が外部のツールやデータソースに接続するための仕組みだよ。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
</Frame>

<div id="why-use-mcp">
  ### なぜ MCP を使う？
</div>

MCP は Cursor を外部システムやデータに接続する。プロジェクト構成を毎回説明する代わりに、ツールと直接連携できる。

`stdout` に出力するか、HTTP エンドポイントを提供できる言語ならどれでも MCP サーバーを書ける — Python、JavaScript、Go など。

<div id="how-it-works">
  ### 仕組み
</div>

MCP サーバーはプロトコル経由で機能を公開し、Cursor を外部ツールやデータソースに接続する。

Cursor は 3 種類のトランスポート方式をサポートしてる:

<div className="full-width-table">
  | トランスポート                                                          | 実行環境      | デプロイ        | ユーザー   | 入力                | 認証    |
  | :--------------------------------------------------------------- | :-------- | :---------- | :----- | :---------------- | :---- |
  | **<span className="whitespace-nowrap">`stdio`</span>**           | ローカル      | Cursor が管理  | 単一ユーザー | シェルコマンド           | 手動    |
  | **<span className="whitespace-nowrap">`SSE`</span>**             | ローカル/リモート | サーバーとしてデプロイ | 複数ユーザー | SSE エンドポイントの URL  | OAuth |
  | **<span className="whitespace-nowrap">`Streamable HTTP`</span>** | ローカル/リモート | サーバーとしてデプロイ | 複数ユーザー | HTTP エンドポイントの URL | OAuth |
</div>

<div id="protocol-support">
  ### プロトコル対応
</div>

Cursor は次の MCP プロトコル機能に対応してる:

<div className="full-width-table">
  | 機能              | 対応状況 | 説明                                |
  | :-------------- | :--- | :-------------------------------- |
  | **Tools**       | 対応   | AI モデルが実行する関数                     |
  | **Prompts**     | 対応   | ユーザー向けのテンプレートメッセージとワークフロー         |
  | **Resources**   | 対応   | 読み取り・参照可能な構造化データソース               |
  | **Roots**       | 対応   | 操作対象となる URI／ファイルシステム境界へのサーバー起点の照会 |
  | **Elicitation** | 対応   | ユーザーに追加情報を求めるサーバー起点のリクエスト         |
</div>

<div id="installing-mcp-servers">
  ## MCP サーバーのインストール方法
</div>

<div id="one-click-installation">
  ### ワンクリックでインストール
</div>

コレクションから MCP サーバーをインストールして、OAuth で認証しよう。

<Columns cols={2}>
  <Card title="Browse MCP Tools" icon="table" horizontal href="/ja/tools">
    利用可能な MCP サーバーを閲覧
  </Card>

  <Card title="Add to Cursor Button" icon="plus" horizontal href="/ja/deeplinks">
    「Add to Cursor」ボタンを作成
  </Card>
</Columns>

<div id="using-mcpjson">
  ### `mcp.json` を使う
</div>

カスタム MCP サーバーを JSON ファイルで構成する:

<CodeGroup>
  ```json CLI Server - Node.js theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "npx",
        "args": ["-y", "mcp-server"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json CLI Server - Python theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "python",
        "args": ["mcp-server.py"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json Remote Server theme={null}
  // HTTP または SSE を使用する MCP サーバー — サーバー上で稼働
  {
    "mcpServers": {
      "server-name": {
        "url": "http://localhost:3000/mcp",
        "headers": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```
</CodeGroup>

<div id="stdio-server-configuration">
  ### STDIO サーバーの設定
</div>

STDIO サーバー（ローカルのコマンドラインサーバー）の場合、`mcp.json` で次のフィールドを設定してね:

<div className="full-width-table">
  | Field       | Required | Description                                     | Examples                                  |
  | :---------- | :------- | :---------------------------------------------- | :---------------------------------------- |
  | **type**    | Yes      | サーバーの接続タイプ                                      | `"stdio"`                                 |
  | **command** | Yes      | サーバー実行ファイルを起動するコマンド。システムの PATH にあるか、フルパスを指定してね。 | `"npx"`, `"node"`, `"python"`, `"docker"` |
  | **args**    | No       | コマンドに渡す引数の配列                                    | `["server.py", "--port", "3000"]`         |
  | **env**     | No       | サーバー用の環境変数                                      | `{"API_KEY": "${input:api-key}"}`         |
  | **envFile** | No       | 追加の環境変数を読み込むための環境ファイルのパス                        | `".env"`, `"${workspaceFolder}/.env"`     |
</div>

<div id="using-the-extension-api">
  ### Extension API の使用
</div>

プログラムによる MCP サーバー登録のために、Cursor は `mcp.json` ファイルを変更せずに動的に設定できる拡張 API を提供している。これは特にエンタープライズ環境や自動セットアップのワークフローで有用。

<Card title="MCP Extension API Reference" icon="code" href="/ja/context/mcp-extension-api">
  `vscode.cursor.mcp.registerServer()` を使ってプログラムから MCP サーバーを登録する方法を学ぼう
</Card>

<div id="configuration-locations">
  ### 設定の場所
</div>

<CardGroup cols={2}>
  <Card title="Project Configuration" icon="folder-tree">
    プロジェクト専用のツールには、プロジェクト内に `.cursor/mcp.json` を作成しよう。
  </Card>

  <Card title="Global Configuration" icon="globe">
    どこでも使えるツールには、ホームディレクトリに `~/.cursor/mcp.json` を作成しよう。
  </Card>
</CardGroup>

<div id="config-interpolation">
  ### コンフィグの補間
</div>

`mcp.json` の値に変数を使える。Cursor は次のフィールドで変数を解決する: `command`、`args`、`env`、`url`、`headers`。

サポートされる構文:

* `${env:NAME}` 環境変数
* `${userHome}` ホームフォルダへのパス
* `${workspaceFolder}` プロジェクトのルート（`.cursor/mcp.json` を含むフォルダ）
* `${workspaceFolderBasename}` プロジェクトルートの名前
* `${pathSeparator}` と `${/}` OS のパス区切り文字

例

```json  theme={null}
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

```json  theme={null}
{
  "mcpServers": {
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    }
  }
}
```

<div id="authentication">
  ### 認証
</div>

MCP サーバーは認証に環境変数を使う。API キーやトークンは config で渡してね。

Cursor は、OAuth が必要なサーバーにも対応してる。

<div id="using-mcp-in-chat">
  ## チャットでの MCP の使い方
</div>

Composer Agent は、必要に応じて `Available Tools` に表示されている MCP ツールを自動で使うよ。特定のツール名を指定するか、やりたいことをそのまま伝えてね。ツールの有効化・無効化は設定から切り替えられる。

<div id="toggling-tools">
  ### ツールの切り替え
</div>

チャット画面からそのまま MCP ツールを有効/無効にできる。ツール一覧でツール名をクリックすると切り替わる。無効にしたツールはコンテキストに読み込まれず、Agent からも利用できない。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-toggle.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fa3060f593cae3e5fb7c7d2f041a715" autoPlay loop muted playsInline controls data-path="images/context/mcp/tool-toggle.mp4" />
</Frame>

<div id="tool-approval">
  ### ツールの承認
</div>

デフォルトでは、Agent は MCP ツールを使う前に承認を求める。引数を確認するには、ツール名の横にある矢印をクリック。

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bf9b19d5f23abc65914f712185b3ec72" alt="" data-og-width="1212" width="1212" data-og-height="902" height="902" data-path="images/context/mcp/tool-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e3f900fad0b8f2a469460c70fa1dd1dc 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de2f90138de39d75d70c5800f13be93a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b9c616ce7a4080ea4088a0fdd0050c7c 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3f783e62a7a31957b8988edb97c139f9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10bf2c1dbfd5c2a03aa95334f53cd571 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=231c0e3cd60df5ad12455d5e8ef308d2 2500w" /></Frame>

<div id="auto-run">
  #### 自動実行
</div>

Agent が確認なしで MCP ツールを使えるよう、自動実行を有効にする。ターミナルのコマンドのように動作する。自動実行の設定については[こちら](/ja/agent/tools#auto-run)を参照。

<div id="tool-response">
  ### ツールのレスポンス
</div>

Cursor は、引数とレスポンスを展開できるビューとともに、チャット内にレスポンスを表示する:

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=30af3f35869e9a78781f455bdbc0e3b5" alt="" data-og-width="1212" width="1212" data-og-height="952" height="952" data-path="images/context/mcp/tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8821ac7bad00ad54a18abc614c2e3d5c 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9d55f089ad53a89da99b8ddd524f6de 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a107d68a1fb05ed43851548b34fb4496 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b409b4941c2fd783043770fad0bd6390 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2a331b5e2bb9be0b9659393157454c2e 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=585b769dfa2a5114b111eb901a969845 2500w" /></Frame>

<div id="images-as-context">
  ### コンテキストとしての画像
</div>

MCP サーバーは画像（スクリーンショット、ダイアグラムなど）を返せる。base64 でエンコードした文字列として返して:

```js  theme={null}
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ 可読性のために base64 全体を省略

server.tool("generate_image", async (params) => {
  return {
    content: [
      {
        type: "image",
        data: RED_CIRCLE_BASE64,
        mimeType: "image/jpeg",
      },
    ],
  };
});
```

実装の詳細はこの[example server](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js)を参照してね。Cursor は返された画像をチャットに添付するよ。モデルが画像をサポートしていれば、それらを解析する。

<div id="security-considerations">
  ## セキュリティ上の考慮事項
</div>

MCP サーバーをインストールするときは、次のセキュリティ対策を意識してね:

* **配布元の確認**: 信頼できる開発者やリポジトリからの MCP サーバーだけをインストールする
* **権限の確認**: サーバーがアクセスするデータや API をチェックする
* **API キーの最小化**: 必要最小限の権限に絞った制限付き API キーを使う
* **コードの監査**: 重要な連携では、サーバーのソースコードをレビューする

MCP サーバーは外部サービスにアクセスしたり、きみの代わりにコードを実行できることを忘れないで。インストール前に、そのサーバーが何をするのか必ず理解しておこう。

<div id="real-world-examples">
  ## 実際の例
</div>

MCP を実際に活用する具体例は、開発ワークフローに Linear、Figma、ブラウザツールを統合する方法を紹介している [Web Development ガイド](/ja/guides/tutorials/web-development) を参照してね。

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="MCP サーバーの目的は？">
    MCP サーバーは、Cursor を Google Drive や Notion などの外部ツールやサービスに接続して、ドキュメントや要件をコーディングのワークフローに取り込めるようにするものだよ。
  </Accordion>

  {" "}

  <Accordion title="MCP サーバーの問題はどうデバッグする？">
    MCP のログを見るには: 1. Cursor で Output パネルを開く (<Kbd>Cmd+Shift+U</Kbd>)
    2\. ドロップダウンから「MCP Logs」を選ぶ 3. 接続エラー、認証エラー、サーバークラッシュを確認する
    ログにはサーバーの初期化、ツール呼び出し、エラーメッセージが出るよ。
  </Accordion>

  {" "}

  <Accordion title="MCP サーバーを一時的に無効化できる？">
    できる！削除せずにオン/オフを切り替えられるよ: 1. Settings を開く (
    <Kbd>Cmd+Shift+J</Kbd>) 2. Features → Model Context Protocol に進む 3.
    任意のサーバーのトグルをクリックして有効/無効を切り替える 無効化したサーバーは読み込まれず、チャットにも出てこないよ。
    トラブルシューティングやツールの整理に便利。
  </Accordion>

  {" "}

  <Accordion title="MCP サーバーがクラッシュしたりタイムアウトしたら？">
    MCP サーバーが失敗した場合: - Cursor がチャットにエラーメッセージを表示する - ツール呼び出しは失敗としてマークされる - 操作を再試行するか、詳細はログを確認できる - 他の MCP サーバーは通常どおり動作を継続する
    Cursor はサーバーの障害を分離して、1つのサーバーが他に影響しないようにしてるよ。
  </Accordion>

  {" "}

  <Accordion title="MCP サーバーはどう更新する？">
    npm ベースのサーバーの場合: 1. 設定からサーバーを削除 2. npm キャッシュをクリア:
    `npm cache clean --force` 3. 最新版を取得するためにサーバーを再追加 カスタムサーバーの場合は、ローカルファイルを更新して Cursor を再起動してね。
  </Accordion>

  <Accordion title="機密データで MCP サーバーを使える？">
    使えるけど、セキュリティのベストプラクティスに従ってね: - 秘密情報は環境変数を使い、ハードコードしない - 機密性の高いサーバーは `stdio`
    トランスポートでローカル実行する - API キーの権限は必要最小限に絞る - 機密システムに接続する前にサーバーコードをレビューする - サーバーを分離環境で実行することを検討する
  </Accordion>
</AccordionGroup>

---

← Previous: [ファイルの除外設定](./section.md) | [Index](./index.md) | Next: [Memories](./memories.md) →