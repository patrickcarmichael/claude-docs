---
title: "Slack"
source: "https://docs.cursor.com/zh/integrations/slack"
language: "zh"
language_name: "Chinese"
---

# Slack
Source: https://docs.cursor.com/zh/integrations/slack

直接在 Slack 中与后台代理协作

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

通过 Cursor 的 Slack 集成，只需在 Slack 里提及 <SlackInlineMessage message="@Cursor" /> 并附上提示词，就能直接用 [Background Agents](/zh/background-agent) 处理你的任务。

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-agent.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=aa7aa2681db1e363047334c6a8e33f72" controls autoplay muted loop data-path="images/background-agent/slack/slack-agent.mp4" />
</Frame>

<div id="get-started">
  ## 快速开始
</div>

<div id="installation">
  ### 安装
</div>

1. 前往 [Cursor 集成](https://www.cursor.com/en/dashboard?tab=integrations)

2. 点击 Slack 旁的 *Connect*，或从这里进入[安装页面](https://cursor.com/api/install-slack-app)

3. 系统会提示在你的工作区安装 Slack 版 Cursor 应用

4. 在 Slack 中安装完成后，你会被重定向回 Cursor 以完成最后的配置

   1. 连接 GitHub（如尚未连接）并选择一个默认仓库
   2. 启用按用量计费
   3. 确认隐私设置

5. 在 Slack 中通过提及 <SlackInlineMessage message="@Cursor" /> 开始使用 Background Agents

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/cursor-slack-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd5b3c65b1a0de08b46c90515b6056a6" controls autoplay muted loop data-path="images/background-agent/slack/cursor-slack-install.mp4" />
</Frame>

<div id="how-to-use">
  ## 使用方法
</div>

在消息中提及 <SlackInlineMessage message="@Cursor" /> 并给出你的指令。这能覆盖大多数场景，但也可以用下面的命令来自定义你的 agent。

比如，直接在对话里提及 <SlackInlineMessage message="@Cursor fix the login bug" />，或者用 <SlackInlineMessage message="@Cursor [repo=torvalds/linux] fix bug" /> 这样的命令来指定某个仓库。

<div id="commands">
  ### 命令
</div>

运行 <SlackInlineMessage message="@Cursor help" /> 获取最新命令列表。

<div className="full-width-table">
  | Command                                                     | Description                                 |
  | :---------------------------------------------------------- | :------------------------------------------ |
  | <SlackInlineMessage message="@Cursor [prompt]" />           | 启动一个 Background Agent。在已有 agent 的线程中会添加后续指令 |
  | <SlackInlineMessage message="@Cursor settings" />           | 配置默认值和频道的默认仓库                               |
  | <SlackInlineMessage message="@Cursor [options] [prompt]" /> | 使用高级选项：`branch`、`model`、`repo`              |
  | <SlackInlineMessage message="@Cursor agent [prompt]" />     | 在线程中强制创建一个新 agent                           |
  | <SlackInlineMessage message="@Cursor list my agents" />     | 显示你正在运行的 agents                             |
</div>

<div id="options">
  #### 选项
</div>

用这些选项自定义 Background Agent 的行为：

<div className="full-width-table">
  | Option   | Description  | Example           |
  | :------- | :----------- | :---------------- |
  | `branch` | 指定基准分支       | `branch=main`     |
  | `model`  | 选择 AI 模型     | `model=o3`        |
  | `repo`   | 指定目标仓库       | `repo=owner/repo` |
  | `autopr` | 启用/禁用自动创建 PR | `autopr=false`    |
</div>

<div id="syntax-formats">
  ##### 语法格式
</div>

选项有多种写法：

1. **方括号格式**

   <SlackInlineMessage message="@Cursor [branch=dev, model=o3, repo=owner/repo, autopr=false] Fix the login bug" />

2. **内联格式**
   <SlackInlineMessage message="@Cursor branch=dev model=o3 repo=owner/repo autopr=false Fix the login bug" />

<div id="option-precedence">
  ##### 选项优先级
</div>

当同时使用多个选项时：

* 显式给定的值会覆盖默认值
* 如果重复，后面的值会覆盖前面的值
* 内联选项优先于设置面板中的默认值

机器人会从消息中的任意位置解析选项，方便你用自然语言编写命令。

<div id="using-thread-context">
  #### 使用线程上下文
</div>

Background Agents 会理解并利用现有线程讨论的上下文。当团队在讨论一个问题、而你想让 agent 基于那段对话来实现解决方案时，这就很有用。

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
  Background Agents 在被调用时会读取整条线程的上下文，
  并基于团队的讨论来理解并实现解决方案。
</Note>

<div id="when-to-use-force-commands">
  #### 何时使用强制命令
</div>

什么时候需要 <SlackInlineMessage message="@Cursor agent" />？

在已有 agent 的线程中，<SlackInlineMessage message="@Cursor [prompt]" /> 会添加后续指令（仅当你是该 agent 的所有者时生效）。用 <SlackInlineMessage message="@Cursor agent [prompt]" /> 来启动一个独立的 agent。

什么时候需要使用 `Add follow-up`（上下文菜单中）？

在某个 agent 的回复上使用上下文菜单（⋯）来添加后续指令。当一个线程里有多个 agents、且你需要指定要跟进哪一个时，这很有用。

<div id="status-updates-handoff">
  ### 状态更新与交接
</div>

当 Background Agent 运行时，你首先会看到一个 Open in Cursor 选项。

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=496d3775ca5cc1e20dd1dc34952f76fd" style={{ backgroundColor: "#1b1d21" }} data-og-width="1236" width="1236" data-og-height="258" height="258" data-path="images/background-agent/slack/slack-open-in-cursor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9136ecf72e3f7e75b2178a2922878fbd 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d6977f43055c3e8cb69071fe7b48367 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5264cb584c1160bd8ac3cdeaae320777 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a065e6c1a08d4413464e1251eab1b2a6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e067f0dc80ed77bce7843f777f2d7970 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fbcb8e474fd1681219964c558ea2952d 2500w" />
</Frame>

当 Background Agent 完成后，你会在 Slack 收到通知，并可选择在 GitHub 查看创建的 PR。

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d0f5f15094f682a5617c936bea88db3d" style={{ backgroundColor: "#1b1d21" }} data-og-width="1272" width="1272" data-og-height="496" height="496" data-path="images/background-agent/slack/slack-view-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a51c98f13fef794ba8f54a28ad42e99d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbde7fe552a04a8ed44b1771bbc3f55c 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=616811c969184b9061435e9753f63ddb 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90fe4582797d75782019c7d0c3232ea8 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffe4d6a78cad700f82e770418c7f6e13 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ec4dac244e5982d0150d058ddac0d205 2500w" />
</Frame>

<div id="managing-agents">
  ### 管理 agents
</div>

要查看所有正在运行的 agents，运行 <SlackInlineMessage message="@Cursor list my agents" />。

在任意 agent 消息上点击三点（⋯）打开上下文菜单来管理 Background Agents。

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a92748d0f4d3450d51a2c2cdd989eb1" style={{ backgroundColor: "#1b1d21" }} data-og-width="1982" width="1982" data-og-height="1498" height="1498" data-path="images/background-agent/slack/slack-context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6af034b2f0c1b510510622b111c8d4e7 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7d28c9785328aa414eba66704d7f4f08 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=810f99ed15ec100cdfee183ef9b7f827 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f4c00c380996793b50d31ef3ac95219c 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=94bccdd7d7a9f1301fdb4e832e008efa 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90e628735b628ec71d5a78547db2441c 2500w" />
</Frame>

可用选项：

* **Add follow-up**: 为现有 agent 添加后续指令
* **Delete**: 停止并归档 Background Agent
* **View request ID**: 查看用于故障排查的唯一请求 ID（联系支持时请附上）
* **Give feedback**: 提供关于 agent 表现的反馈

<div id="configuration">
  ## 配置
</div>

在 [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents) 管理默认设置和隐私选项。

<div id="settings">
  ### 设置
</div>

<div id="default-model">
  #### 默认模型
</div>

当没有通过 <SlackInlineMessage message="@Cursor [model=...]" /> 明确指定模型时使用。可用选项见 [settings](https://www.cursor.com/dashboard?tab=background-agents)。

<div id="default-repository">
  #### 默认仓库
</div>

在未指定仓库时使用。请使用以下格式：

* `https://github.com/org/repository`
* `org/repository`

<Note>
  如果引用了一个不存在的仓库，会看起来像是你没有访问权限。
  当 Background Agent 启动失败时，这会体现在错误信息中。
</Note>

<div id="base-branch">
  #### 基础分支
</div>

Background Agent 的起始分支。留空则使用仓库的默认分支（通常为 `main`）。

<div id="channel-settings">
  ### 频道设置
</div>

使用 <SlackInlineMessage message="@Cursor settings" /> 在频道级配置默认设置。这些设置按团队生效，并会覆盖你在该频道的个人默认值。

在以下情况下尤其有用：

* 不同频道处理不同的仓库
* 团队希望所有成员使用一致的设置
* 你想避免在每条命令中都指定仓库

配置频道设置：

1. 在目标频道运行 <SlackInlineMessage message="@Cursor settings" />
2. 为该频道设置默认仓库
3. 在该频道使用 Background Agents 的所有团队成员都会使用这些默认值

<Note>
  频道设置优先于个人默认值，但可以被显式选项覆盖，例如{" "}

  <SlackInlineMessage message="@Cursor [repo=...] [prompt]" />
</Note>

<div id="privacy">
  ### 隐私
</div>

Background Agents 支持隐私模式。

进一步了解 [Privacy Mode](https://www.cursor.com/privacy-overview) 或管理你的[隐私设置](https://www.cursor.com/dashboard?tab=background-agents)。

<Warning>
  不支持隐私模式（旧版）。Background Agents 在运行期间需要临时代码存储。
</Warning>

<div id="display-agent-summary">
  #### 显示 Agent 摘要
</div>

显示 Agent 摘要和差异图片。可能包含文件路径或代码片段。可开启/关闭。

<div id="display-agent-summary-in-external-channels">
  #### 在外部频道显示 Agent 摘要
</div>

对于与其他工作区的 Slack Connect，或包含外部成员（如 Guests）的频道，可选择是否在外部频道显示 Agent 摘要。

<div id="permissions">
  ## 权限
</div>

为让 Background Agents 在你的工作区内正常工作，Cursor 需要以下 Slack 权限：

<div className="full-width-table">
  | Permission          | Description                             |
  | :------------------ | :-------------------------------------- |
  | `app_mentions:read` | 监听 @mention，以启动 Background Agents 并响应请求 |
  | `channels:history`  | 在添加后续指令时读取线程历史消息，获取上下文                  |
  | `channels:join`     | 被邀请或请求时自动加入公共频道                         |
  | `channels:read`     | 访问频道元数据（ID 和名称），用于发布回复和更新               |
  | `chat:write`        | 在代理完成任务时发送状态更新、完成通知和 PR 链接              |
  | `files:read`        | 下载共享文件（日志、截图、代码示例）以补充上下文                |
  | `files:write`       | 上传代理变更的可视化摘要，便于快速审阅                     |
  | `groups:history`    | 在多轮对话中读取私有频道的历史消息以获取上下文                 |
  | `groups:read`       | 访问私有频道元数据，用于发布回复并维持对话连续性                |
  | `im:history`        | 访问私信历史，以便在持续对话中获取上下文                    |
  | `im:read`           | 读取私信元数据，以识别参与者并保持正确的线程关联                |
  | `im:write`          | 发起私信，用于私密通知或一对一沟通                       |
  | `mpim:history`      | 访问群组私信历史，以支持多参与者对话                      |
  | `mpim:read`         | 读取群组私信元数据，以定位参与者并确保正确送达                 |
  | `reactions:read`    | 读取表情回复，用于用户反馈和状态信号                      |
  | `reactions:write`   | 添加表情回复标记状态：⏳ 运行中，✅ 已完成，❌ 失败             |
  | `team:read`         | 识别工作区详情，以区分不同安装并应用设置                    |
  | `users:read`        | 将 Slack 用户与 Cursor 账号匹配，用于权限和安全访问       |
</div>

---

← Previous: [Linear](./linear.md) | [Index](./index.md) | Next: [模型](./section.md) →