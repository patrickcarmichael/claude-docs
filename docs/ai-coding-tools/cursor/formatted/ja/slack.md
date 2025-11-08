---
title: "Slack"
source: "https://docs.cursor.com/ja/integrations/slack"
language: "ja"
language_name: "Japanese"
---

# Slack
Source: https://docs.cursor.com/ja/integrations/slack

Slack から Background Agents を操作する

export const SlackThread = ({messages = []}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg bg-neutral-50 dark:bg-neutral-900/50 py-4 overflow-hidden">
      {messages.map((msg, index) => <div key={index} className={`group hover:bg-[#f0f0f0] dark:hover:bg-[#333] px-6 py-2 -mx-2 -my-1 transition-colors`}>
          <div className="flex items-start gap-3">
            <div className="w-9 h-9 rounded-md bg-neutral-300 dark:bg-neutral-800 flex items-center justify-center text-white text-sm font-semibold flex-shrink-0">
              {msg.name ? msg.name.charAt(0).toUpperCase() : 'U'}
            </div>

            <div className="flex-1 min-w-0">
              <div className="flex items-baseline gap-2">
                <span className="font-semibold text-neutral-900 dark:text-neutral-100 text-sm">
                  {msg.name || 'User'}
                </span>
                <span className="text-xs text-neutral-500 dark:text-neutral-400">
                  {msg.timestamp || ''}
                </span>
              </div>
              <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
                <MessageWithMentions text={msg.message} />
              </div>

              {msg.reactions && msg.reactions.length > 0 && <div className="flex gap-1 mt-1">
                  {msg.reactions.map((reaction, rIndex) => <div key={rIndex} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded text-xs hover:bg-neutral-100 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
                      <span>{reaction.emoji}</span>
                      <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
                    </div>)}
                </div>}
            </div>
          </div>
        </div>)}
    </div>;
};

export const SlackInlineMessage = ({message}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] hover:bg-[#1264A3]/10 dark:hover:bg-[#1264A3]/25 px-0.5 rounded">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <span className="inline rounded p-0.5 bg-neutral-50 dark:bg-neutral-800/30">
      <MessageWithMentions text={message} />
    </span>;
};

export const SlackUserMessage = ({message, reactions = [], replies = null}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-800/50 transition-colors px-5 py-3 group">
      <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
        <MessageWithMentions text={message} />
      </div>

      {reactions.length > 0 && <div className="flex gap-1 mt-1">
          {reactions.map((reaction, index) => <div key={index} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-neutral-100 dark:bg-neutral-800 rounded text-xs hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
              <span>{reaction.emoji}</span>
              <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
            </div>)}
        </div>}

      {replies && <div className="flex items-center gap-1.5 mt-2 text-[#1264A3] hover:underline cursor-pointer">
          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M7.707 10.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V6h5a2 2 0 012 2v7a2 2 0 01-2 2H4a2 2 0 01-2-2V8a2 2 0 012-2h5v5.586l-1.293-1.293z" />
          </svg>
          <span className="text-sm font-medium">{replies.count} {replies.count === 1 ? 'reply' : 'replies'}</span>
          {replies.lastReplyTime && <span className="text-xs text-neutral-500 dark:text-neutral-400">{replies.lastReplyTime}</span>}
        </div>}
    </div>;
};

Cursor の Slack 連携を使えば、Slack で <SlackInlineMessage message="@Cursor" /> にプロンプトを添えてメンションするだけで、[Background Agents](/ja/background-agent) がタスクを直接実行してくれる。

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-agent.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=aa7aa2681db1e363047334c6a8e33f72" controls autoplay muted loop data-path="images/background-agent/slack/slack-agent.mp4" />
</Frame>

<div id="get-started">
  ## はじめよう
</div>

<div id="installation">
  ### インストール
</div>

1. [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations) に移動

2. Slack の横にある *Connect* をクリック、またはここから [installation page](https://cursor.com/api/install-slack-app) へ移動

3. ワークスペースに Cursor の Slack アプリをインストールするよう求められる

4. Slack にインストール後、セットアップを完了するために Cursor にリダイレクトされる

   1. GitHub を接続（未接続の場合）し、デフォルトのリポジトリを選ぶ
   2. 従量課金を有効にする
   3. プライバシー設定を確認する

5. <SlackInlineMessage message="@Cursor" /> をメンションして、Slack で Background Agents の利用を開始

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/cursor-slack-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd5b3c65b1a0de08b46c90515b6056a6" controls autoplay muted loop data-path="images/background-agent/slack/cursor-slack-install.mp4" />
</Frame>

<div id="how-to-use">
  ## 使い方
</div>

<SlackInlineMessage message="@Cursor" /> にメンションしてプロンプトを送るだけ。これでほとんどのケースはカバーできるけど、エージェントをカスタマイズしたい場合は下のコマンドも使える。

たとえば会話の中で <SlackInlineMessage message="@Cursor fix the login bug" /> と直接メンションするか、特定のリポジトリを対象にするなら <SlackInlineMessage message="@Cursor [repo=torvalds/linux] fix bug" /> みたいに専用のコマンドを使う。

<div id="commands">
  ### コマンド
</div>

最新のコマンド一覧は <SlackInlineMessage message="@Cursor help" /> を実行。

<div className="full-width-table">
  | Command                                                     | Description                                    |
  | :---------------------------------------------------------- | :--------------------------------------------- |
  | <SlackInlineMessage message="@Cursor [prompt]" />           | Background Agent を起動。既存のエージェントがいるスレッドでは追加入力を渡す |
  | <SlackInlineMessage message="@Cursor settings" />           | デフォルト設定とチャンネルのデフォルトリポジトリを設定                    |
  | <SlackInlineMessage message="@Cursor [options] [prompt]" /> | 高度なオプションを使用: `branch`, `model`, `repo`         |
  | <SlackInlineMessage message="@Cursor agent [prompt]" />     | スレッド内に新しいエージェントを強制的に作成                         |
  | <SlackInlineMessage message="@Cursor list my agents" />     | 実行中の自分のエージェントを表示                               |
</div>

<div id="options">
  #### オプション
</div>

以下のオプションで Background Agent の動作をカスタマイズ:

<div className="full-width-table">
  | Option   | Description  | Example           |
  | :------- | :----------- | :---------------- |
  | `branch` | ベースブランチを指定   | `branch=main`     |
  | `model`  | AIモデルを選択     | `model=o3`        |
  | `repo`   | 対象リポジトリを指定   | `repo=owner/repo` |
  | `autopr` | 自動PR作成の有効/無効 | `autopr=false`    |
</div>

<div id="syntax-formats">
  ##### 構文フォーマット
</div>

オプションは複数の方法で指定できる:

1. **ブラケット形式**

   <SlackInlineMessage message="@Cursor [branch=dev, model=o3, repo=owner/repo, autopr=false] Fix the login bug" />

2. **インライン形式**
   <SlackInlineMessage message="@Cursor branch=dev model=o3 repo=owner/repo autopr=false Fix the login bug" />

<div id="option-precedence">
  ##### オプションの優先順位
</div>

オプションを組み合わせる場合:

* 明示的な値がデフォルトを上書き
* 重複した場合は後に指定した値が前を上書き
* インライン指定は設定モーダルのデフォルトより優先

ボットはメッセージ内のどこからでもオプションを解析するから、自然な書き方でコマンドを書ける。

<div id="using-thread-context">
  #### スレッドコンテキストの活用
</div>

Background Agents は既存のスレッドの議論からコンテキストを理解して活用する。チームで課題を議論して、その会話に基づいてエージェントに実装してほしいときに便利。

<SlackThread
  messages={[
{
  message:
    "Hey team, we're getting reports that users can't log in after the latest deploy",
  timestamp: "2:30 PM",
  name: "Sarah",
},
{
  message:
    "I checked the logs - looks like the auth token validation is failing on line 247 of auth.js",
  timestamp: "2:32 PM",
  name: "Mike",
},
{
  message:
    "Oh, I think it's because we changed the token format but didn't update the validation regex",
  timestamp: "2:33 PM",
  name: "Alex",
},
{
  message:
    "Yeah, the regex still expects the old format. We need to update it to handle both old and new formats for backwards compatibility",
  timestamp: "2:35 PM",
  name: "Sarah",
},
{
  message: "@Cursor fix this",
  timestamp: "2:36 PM",
  name: "You",
  reactions: [{ emoji: "⏳", count: 1 }],
},
]}
/>

<Note>
  Background Agents は呼び出されたときにスレッド全体を読み込みコンテキストを取得し、
  チームの議論に基づいて解決策を理解して実装する。
</Note>

<div id="when-to-use-force-commands">
  #### 強制コマンドを使うタイミング
</div>

**<SlackInlineMessage message="@Cursor agent" /> はいつ必要？**

既存のエージェントがいるスレッドでは、<SlackInlineMessage message="@Cursor [prompt]" /> は追加入力を渡す（そのエージェントの所有者である場合のみ有効）。別のエージェントを起動したいときは <SlackInlineMessage message="@Cursor agent [prompt]" /> を使う。

**`Add follow-up`（コンテキストメニュー）はいつ必要？**

エージェントのレスポンスのコンテキストメニュー（⋯）から追加入力を渡せる。スレッド内に複数のエージェントがいる場合に、どれにフォローアップするかを指定したいときに便利。

<div id="status-updates-handoff">
  ### ステータス更新と引き継ぎ
</div>

Background Agent が走り始めると、最初に「Open in Cursor」のオプションが出る。

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=496d3775ca5cc1e20dd1dc34952f76fd" style={{ backgroundColor: "#1b1d21" }} data-og-width="1236" width="1236" data-og-height="258" height="258" data-path="images/background-agent/slack/slack-open-in-cursor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9136ecf72e3f7e75b2178a2922878fbd 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d6977f43055c3e8cb69071fe7b48367 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5264cb584c1160bd8ac3cdeaae320777 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a065e6c1a08d4413464e1251eab1b2a6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e067f0dc80ed77bce7843f777f2d7970 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fbcb8e474fd1681219964c558ea2952d 2500w" />
</Frame>

Background Agent の処理が完了すると、Slack に通知が届いて、GitHub で作成された PR を表示できるよ。

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d0f5f15094f682a5617c936bea88db3d" style={{ backgroundColor: "#1b1d21" }} data-og-width="1272" width="1272" data-og-height="496" height="496" data-path="images/background-agent/slack/slack-view-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a51c98f13fef794ba8f54a28ad42e99d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbde7fe552a04a8ed44b1771bbc3f55c 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=616811c969184b9061435e9753f63ddb 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90fe4582797d75782019c7d0c3232ea8 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffe4d6a78cad700f82e770418c7f6e13 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ec4dac244e5982d0150d058ddac0d205 2500w" />
</Frame>

<div id="managing-agents">
  ### エージェントの管理
</div>

実行中のエージェントをすべて見るには、<SlackInlineMessage message="@Cursor list my agents" /> を実行してね。

任意のエージェントメッセージの三点（⋯）をクリックして、コンテキストメニューから Background Agent を管理できるよ。

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a92748d0f4d3450d51a2c2cdd989eb1" style={{ backgroundColor: "#1b1d21" }} data-og-width="1982" width="1982" data-og-height="1498" height="1498" data-path="images/background-agent/slack/slack-context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6af034b2f0c1b510510622b111c8d4e7 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7d28c9785328aa414eba66704d7f4f08 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=810f99ed15ec100cdfee183ef9b7f827 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f4c00c380996793b50d31ef3ac95219c 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=94bccdd7d7a9f1301fdb4e832e008efa 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90e628735b628ec71d5a78547db2441c 2500w" />
</Frame>

利用できるオプション:

* **Add follow-up**: 既存のエージェントに追加入力（指示）を送る
* **Delete**: Background Agent を停止してアーカイブする
* **View request ID**: トラブルシューティング用の一意のリクエスト ID を表示（サポートに連絡する際に含めてね）
* **Give feedback**: エージェントのパフォーマンスに関するフィードバックを送る

<div id="configuration">
  ## 設定
</div>

[Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents) からデフォルト設定とプライバシーオプションを管理できる。

<div id="settings">
  ### 設定
</div>

<div id="default-model">
  #### デフォルトモデル
</div>

<SlackInlineMessage message="@Cursor [model=...]" /> で明示的にモデルを指定していない場合に使用される。利用可能なオプションは [settings](https://www.cursor.com/dashboard?tab=background-agents) を参照。

<div id="default-repository">
  #### デフォルトリポジトリ
</div>

リポジトリが指定されていない場合に使用される。次の形式を使う:

* `https://github.com/org/repository`
* `org/repository`

<Note>
  存在しないリポジトリを参照すると、アクセス権がないように見える。
  これは Background Agent の起動失敗時のエラーメッセージに表示される。
</Note>

<div id="base-branch">
  #### ベースブランチ
</div>

Background Agent の開始ブランチ。空欄にするとリポジトリのデフォルトブランチ（多くは `main`）が使用される。

<div id="channel-settings">
  ### チャンネル設定
</div>

<SlackInlineMessage message="@Cursor settings" /> を使ってチャンネル単位でデフォルト設定を構成する。これらの設定はチーム単位で、そのチャンネルにおける個人のデフォルトを上書きする。

特に便利なケース:

* チャンネルごとに異なるリポジトリで作業している
* チームでメンバー間の設定を統一したい
* 毎回コマンドでリポジトリを指定するのを避けたい

チャンネル設定の手順:

1. 対象のチャンネルで <SlackInlineMessage message="@Cursor settings" /> を実行
2. そのチャンネルのデフォルトリポジトリを設定
3. そのチャンネルで Background Agents を使用するチームメンバー全員がこのデフォルトを使用

<Note>
  チャンネル設定は個人のデフォルトより優先されるが、{" "}
  <SlackInlineMessage message="@Cursor [repo=...] [prompt]" /> のような明示的なオプションで上書きできる
</Note>

<div id="privacy">
  ### プライバシー
</div>

Background Agents はプライバシーモードをサポートしている。

[Privacy Mode](https://www.cursor.com/privacy-overview) の詳細を読むか、[privacy settings](https://www.cursor.com/dashboard?tab=background-agents) を管理しよう。

<Warning>
  プライバシーモード（レガシー）はサポートされていない。Background Agents は実行中に一時的な
  コードの保存を必要とする。
</Warning>

<div id="display-agent-summary">
  #### エージェントサマリーの表示
</div>

エージェントのサマリーと差分画像を表示。ファイルパスやコードスニペットを含む場合がある。オン/オフ切り替え可。

<div id="display-agent-summary-in-external-channels">
  #### 外部チャンネルでのエージェントサマリー表示
</div>

他のワークスペースとの Slack Connect や、ゲストなど外部メンバーがいるチャンネルで、エージェントサマリーを表示するかどうかを選択。

<div id="permissions">
  ## 権限
</div>

Cursor は、ワークスペースで Background Agents が動作するために次の Slack 権限をリクエストする:

<div className="full-width-table">
  | Permission          | Description                                        |
  | :------------------ | :------------------------------------------------- |
  | `app_mentions:read` | @メンションを検出して Background Agents を起動し、リクエストに応答する      |
  | `channels:history`  | 追加入力の指示を追加する際のコンテキストとして、スレッド内の過去メッセージを読む           |
  | `channels:join`     | 招待やリクエストに応じて自動的にパブリックチャンネルに参加する                    |
  | `channels:read`     | 返信や更新を投稿するために、チャンネルのメタデータ（ID・名前）にアクセスする            |
  | `chat:write`        | エージェント完了時にステータス更新、完了通知、PR リンクを送信する                 |
  | `files:read`        | 追加コンテキストのために、共有ファイル（ログ、スクリーンショット、コードサンプル）をダウンロードする |
  | `files:write`       | 迅速なレビューのために、エージェントの変更点をビジュアルサマリーとしてアップロードする        |
  | `groups:history`    | マルチターン会話のコンテキストとして、プライベートチャンネルの過去メッセージを読む          |
  | `groups:read`       | 応答の投稿や会話の流れ維持のために、プライベートチャンネルのメタデータにアクセスする         |
  | `im:history`        | 継続中の会話のコンテキストとして、ダイレクトメッセージの履歴にアクセスする              |
  | `im:read`           | 参加者の特定と適切なスレッド運用のために、DM のメタデータを読む                  |
  | `im:write`          | プライベート通知や個別コミュニケーションのために、ダイレクトメッセージを開始する           |
  | `mpim:history`      | 複数人の会話のために、グループ DM の履歴にアクセスする                      |
  | `mpim:read`         | 参加者へのアドレス指定と適切な配信のために、グループ DM のメタデータを読む            |
  | `reactions:read`    | ユーザーのフィードバックやステータス信号として、絵文字リアクションを確認する             |
  | `reactions:write`   | ステータスを示す絵文字リアクションを追加する（⏳ 実行中、✅ 完了、❌ 失敗）            |
  | `team:read`         | ワークスペースの詳細を特定してインストールを分離し、設定を適用する                  |
  | `users:read`        | 権限とセキュアなアクセスのために、Slack ユーザーと Cursor アカウントを照合する     |
</div>

---

← Previous: [Linear](./linear.md) | [Index](./index.md) | Next: [モデル](./section.md) →