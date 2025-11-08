---
title: "CLI で Agent を使う"
source: "https://docs.cursor.com/ja/cli/using"
language: "ja"
language_name: "Japanese"
---

# CLI で Agent を使う
Source: https://docs.cursor.com/ja/cli/using

Cursor CLI でプロンプト、レビュー、反復を効率よく行う

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

<div id="prompting">
  ## プロンプト設計
</div>

最良の結果を得るには、意図をはっきり伝えるのがオススメ。たとえば、エージェントにファイルを一切編集させたくないなら、「do not write any code」というプロンプトを使えばOK。これは、実装に入る前にタスクを計画するときに特に役立つ。

エージェントは現在、ファイル操作・検索・シェルコマンド実行のツールを備えてる。IDE エージェントと同様に、今後さらに多くのツールが追加されていく。

<div id="mcp">
  ## MCP
</div>

Agent は拡張機能や統合のために [MCP（Model Context Protocol）](/ja/tools/mcp) をサポートしてる。CLI は `mcp.json` の設定ファイルを自動検出して反映し、IDE で設定したのと同じ MCP サーバーとツールを有効にする。

<div id="rules">
  ## ルール
</div>

CLI エージェントは IDE と同じ[ルールシステム](/ja/context/rules)に対応してる。.cursor/rules ディレクトリにルールを作成して、エージェントにコンテキストとガイダンスを与えよう。これらのルールは設定に基づいて自動的に読み込まれて適用されるから、プロジェクトの異なる部分や特定のファイルタイプごとにエージェントの挙動をカスタマイズできる。

<Note>
  CLI は、（存在する場合）プロジェクトルートにある `AGENTS.md` と `CLAUDE.md` も読み込み、`.cursor/rules` とあわせてルールとして適用する。
</Note>

<div id="working-with-agent">
  ## Agent の使い方
</div>

<div id="navigation">
  ### ナビゲーション
</div>

前のメッセージは上矢印（<Kbd>ArrowUp</Kbd>）で呼び出せて、順番に遡れる。

<div id="review">
  ### レビュー
</div>

<Kbd>Cmd+R</Kbd> で変更内容をレビュー。<Kbd>i</Kbd> を押して追加入力を追加。スクロールは <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd>、ファイル切り替えは <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd>。

<div id="selecting-context">
  ### コンテキストの選択
</div>

<Kbd>@</Kbd> でコンテキストに含めるファイルやフォルダを選択。`/compress` を実行してコンテキストウィンドウの空きスペースを確保。詳しくは [Summarization](/ja/agent/chat/summarization) を参照。

<div id="history">
  ## 履歴
</div>

既存のスレッドから続けるには、`--resume [thread id]` でこれまでのコンテキストを読み込む。

直近の会話を再開するなら、`cursor-agent resume` を使う。

これまでの会話の一覧を見たいときは、`cursor-agent ls` を実行する。

<div id="command-approval">
  ## コマンドの承認
</div>

ターミナルコマンドを実行する前に、CLI が実行の可否を確認するよ。承認するなら (<Kbd>y</Kbd>)、拒否するなら (<Kbd>n</Kbd>) を押してね。

<div id="non-interactive-mode">
  ## 非インタラクティブモード
</div>

`-p` または `--print` を使って Agent を非インタラクティブモードで実行する。レスポンスがコンソールに出力される。

非インタラクティブモードでは、対話なしで Agent を呼び出せる。これにより、スクリプトや CI パイプラインなどに組み込める。

`--output-format` を併用すると、出力形式を制御できる。たとえば、スクリプトでパースしやすい構造化出力には `--output-format json`、プレーンテキスト出力には `--output-format text` を使う。

<Note>
  非インタラクティブモードでは、Cursor はフルの書き込み権限を持つ。
</Note>

---

← Previous: [シェルモード](./section.md) | [Index](./index.md) | Next: [キーボードショートカット](./section.md) →