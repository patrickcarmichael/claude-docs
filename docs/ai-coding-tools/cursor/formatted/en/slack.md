---
title: "Slack"
source: "https://docs.cursor.com/en/integrations/slack"
language: "en"
language_name: "English"
---

# Slack
Source: https://docs.cursor.com/en/integrations/slack

Work with Background Agents from Slack

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

With Cursor's integration for Slack, you can use [Background Agents](/en/background-agent) to work on your tasks directly from Slack by mentioning <SlackInlineMessage message="@Cursor" /> with a prompt.

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-agent.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=aa7aa2681db1e363047334c6a8e33f72" controls autoplay muted loop data-path="images/background-agent/slack/slack-agent.mp4" />
</Frame>

## Get started

### Installation

1. Go to [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations)

2. Click *Connect* next to Slack or go to [installation page](https://cursor.com/api/install-slack-app) from here

3. You'll be prompted to install the Cursor app for Slack in your workspace.

4. After installing in Slack, you'll be redirected back to Cursor to finalize setup

   1. Connect GitHub (if not already connected) and pick a default repository
   2. Enable usage-based pricing
   3. Confirm privacy settings

5. Start using Background Agents in Slack by mentioning <SlackInlineMessage message="@Cursor" />

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/cursor-slack-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd5b3c65b1a0de08b46c90515b6056a6" controls autoplay muted loop data-path="images/background-agent/slack/cursor-slack-install.mp4" />
</Frame>

## How to use

Mention <SlackInlineMessage message="@Cursor" /> and give your prompt. This handles most use cases, but you can also use commands below to customize your agent.

For example, mention <SlackInlineMessage message="@Cursor fix the login bug" /> directly in conversation, or use specific commands like <SlackInlineMessage message="@Cursor [repo=torvalds/linux] fix bug" /> to target a particular repository.

### Commands

Run <SlackInlineMessage message="@Cursor help" /> for an up-to-date command list.

<div className="full-width-table">
  | Command                                                     | Description                                                                           |
  | :---------------------------------------------------------- | :------------------------------------------------------------------------------------ |
  | <SlackInlineMessage message="@Cursor [prompt]" />           | Start a Background Agent. In threads with existing agents, adds followup instructions |
  | <SlackInlineMessage message="@Cursor settings" />           | Configure defaults and channel's default repository                                   |
  | <SlackInlineMessage message="@Cursor [options] [prompt]" /> | Use advanced options: `branch`, `model`, `repo`                                       |
  | <SlackInlineMessage message="@Cursor agent [prompt]" />     | Force create a new agent in a thread                                                  |
  | <SlackInlineMessage message="@Cursor list my agents" />     | Show your running agents                                                              |
</div>

#### Options

Customize Background Agent behavior with these options:

<div className="full-width-table">
  | Option   | Description                          | Example           |
  | :------- | :----------------------------------- | :---------------- |
  | `branch` | Specify base branch                  | `branch=main`     |
  | `model`  | Choose AI model                      | `model=o3`        |
  | `repo`   | Target specific repository           | `repo=owner/repo` |
  | `autopr` | Enable/disable automatic PR creation | `autopr=false`    |
</div>

##### Syntax Formats

Use options in several ways:

1. **Bracket format**

   <SlackInlineMessage message="@Cursor [branch=dev, model=o3, repo=owner/repo, autopr=false] Fix the login bug" />

2. **Inline format**
   <SlackInlineMessage message="@Cursor branch=dev model=o3 repo=owner/repo autopr=false Fix the login bug" />

##### Option precedence

When combining options:

* **Explicit values** override defaults
* **Later values** override earlier ones if duplicated
* **Inline options** take precedence over settings modal defaults

The bot parses options from anywhere in the message, allowing natural command writing.

#### Using thread context

Background Agents understand and use context from existing thread discussions. Useful when your team discusses an issue and you want the agent to implement the solution based on that conversation.

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
  Background Agents read the entire thread for context when invoked,
  understanding and implementing solutions based on the team's discussion.
</Note>

#### When to use force commands

**When do I need <SlackInlineMessage message="@Cursor agent" />?**

In threads with existing agents, <SlackInlineMessage message="@Cursor [prompt]" /> adds followup instructions (only works if you own the agent). Use <SlackInlineMessage message="@Cursor agent [prompt]" /> to launch a separate agent.

**When do I need `Add follow-up` (from context menu)?**

Use the context menu (⋯) on an agent's response for followup instructions. Useful when multiple agents exist in a thread and you need to specify which one to follow up on.

### Status updates & handoff

When Background Agent runs, you first get an option to *Open in Cursor*.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=496d3775ca5cc1e20dd1dc34952f76fd" style={{ backgroundColor: "#1b1d21" }} data-og-width="1236" width="1236" data-og-height="258" height="258" data-path="images/background-agent/slack/slack-open-in-cursor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9136ecf72e3f7e75b2178a2922878fbd 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d6977f43055c3e8cb69071fe7b48367 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5264cb584c1160bd8ac3cdeaae320777 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a065e6c1a08d4413464e1251eab1b2a6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e067f0dc80ed77bce7843f777f2d7970 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fbcb8e474fd1681219964c558ea2952d 2500w" />
</Frame>

When Background Agent completes, you get a notification in Slack and an option to view the created PR in GitHub.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d0f5f15094f682a5617c936bea88db3d" style={{ backgroundColor: "#1b1d21" }} data-og-width="1272" width="1272" data-og-height="496" height="496" data-path="images/background-agent/slack/slack-view-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a51c98f13fef794ba8f54a28ad42e99d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbde7fe552a04a8ed44b1771bbc3f55c 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=616811c969184b9061435e9753f63ddb 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90fe4582797d75782019c7d0c3232ea8 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffe4d6a78cad700f82e770418c7f6e13 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ec4dac244e5982d0150d058ddac0d205 2500w" />
</Frame>

### Managing agents

To see all running agents, run <SlackInlineMessage message="@Cursor list my agents" />.

Manage Background Agents using the context menu by clicking the three dots (⋯) on any agent message.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a92748d0f4d3450d51a2c2cdd989eb1" style={{ backgroundColor: "#1b1d21" }} data-og-width="1982" width="1982" data-og-height="1498" height="1498" data-path="images/background-agent/slack/slack-context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6af034b2f0c1b510510622b111c8d4e7 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7d28c9785328aa414eba66704d7f4f08 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=810f99ed15ec100cdfee183ef9b7f827 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f4c00c380996793b50d31ef3ac95219c 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=94bccdd7d7a9f1301fdb4e832e008efa 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90e628735b628ec71d5a78547db2441c 2500w" />
</Frame>

Available options:

* **Add follow-up**: Add instructions to an existing agent
* **Delete**: Stop and archive the Background Agent
* **View request ID**: View unique request ID for troubleshooting (include when contacting support)
* **Give feedback**: Provide feedback about agent performance

## Configuration

Manage default settings and privacy options from [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents).

### Settings

#### Default Model

Used when no model is explicitly specified with <SlackInlineMessage message="@Cursor [model=...]" />. See [settings](https://www.cursor.com/dashboard?tab=background-agents) for available options.

#### Default Repository

Used when no repository is specified. Use these formats:

* `https://github.com/org/repository`
* `org/repository`

<Note>
  If you reference a non-existent repository, it appears as if you don't have
  access. This shows in the error message when Background Agent fails to start.
</Note>

#### Base Branch

Starting branch for Background Agent. Leave blank to use the repository's default branch (often `main`)

### Channel Settings

Configure default settings at the channel level using <SlackInlineMessage message="@Cursor settings" />. These settings are per team and override your personal defaults for that channel.

Particularly useful when:

* Different channels work on different repositories
* Teams want consistent settings across all members
* You want to avoid specifying the repository in every command

To configure channel settings:

1. Run <SlackInlineMessage message="@Cursor settings" /> in the desired channel
2. Set the default repository for that channel
3. All team members using Background Agents in that channel use these defaults

<Note>
  Channel settings take precedence over personal defaults but can be overridden
  by explicit options like{" "}

  <SlackInlineMessage message="@Cursor [repo=...] [prompt]" />
</Note>

### Privacy

Background Agents support Privacy Mode.

Read more about [Privacy Mode](https://www.cursor.com/privacy-overview) or manage your [privacy settings](https://www.cursor.com/dashboard?tab=background-agents).

<Warning>
  Privacy Mode (Legacy) is not supported. Background Agents require temporary
  code storage while running.
</Warning>

#### Display Agent Summary

Display agent summaries and diff images. May contain file paths or code snippets. Can be turned On/Off.

#### Display Agent Summary in External Channels

For Slack Connect with other workspaces or channels with external members like Guests, choose to display agent summaries in external channels.

## Permissions

Cursor requests these Slack permissions for Background Agents to work within your workspace:

<div className="full-width-table">
  | Permission          | Description                                                                         |
  | :------------------ | :---------------------------------------------------------------------------------- |
  | `app_mentions:read` | Detects @mentions to start Background Agents and respond to requests                |
  | `channels:history`  | Reads previous messages in threads for context when adding follow-up instructions   |
  | `channels:join`     | Automatically joins public channels when invited or requested                       |
  | `channels:read`     | Accesses channel metadata (IDs and names) to post replies and updates               |
  | `chat:write`        | Sends status updates, completion notifications, and PR links when agents finish     |
  | `files:read`        | Downloads shared files (logs, screenshots, code samples) for additional context     |
  | `files:write`       | Uploads visual summaries of agent changes for quick review                          |
  | `groups:history`    | Reads previous messages in private channels for context in multi-turn conversations |
  | `groups:read`       | Accesses private channel metadata to post responses and maintain conversation flow  |
  | `im:history`        | Accesses direct message history for context in continued conversations              |
  | `im:read`           | Reads DM metadata to identify participants and maintain proper threading            |
  | `im:write`          | Initiates direct messages for private notifications or individual communication     |
  | `mpim:history`      | Accesses group DM history for multi-participant conversations                       |
  | `mpim:read`         | Reads group DM metadata to address participants and ensure proper delivery          |
  | `reactions:read`    | Observes emoji reactions for user feedback and status signals                       |
  | `reactions:write`   | Adds emoji reactions to mark status - ⏳ for running, ✅ for completed, ❌ for failed  |
  | `team:read`         | Identifies workspace details to separate installations and apply settings           |
  | `users:read`        | Matches Slack users with Cursor accounts for permissions and secure access          |
</div>

---

← Previous: [Linear](./linear.md) | [Index](./index.md) | Next: [Models](./models.md) →