---
title: "Linear"
source: "https://docs.cursor.com/zh/integrations/linear"
language: "zh"
language_name: "Chinese"
---

# Linear
Source: https://docs.cursor.com/zh/integrations/linear

在 Linear 中使用 Background Agents

在 Linear 里直接用 [Background Agents](/zh/background-agent)：把 issue 分配给 Cursor，或在评论里提及 `@Cursor`。

<Frame>
  <video src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-agent.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ac4bacf6bf42c541f45325ba72f8c25f" controls autoPlay muted loop playsInline data-path="images/integrations/linear/linear-agent.mp4" />
</Frame>

<div id="get-started">
  ## 入门
</div>

<div id="installation">
  ### 安装
</div>

<Note>
  只有 Cursor 管理员才能连接 Linear 集成。其他团队设置对非管理员成员也可用。
</Note>

1. 前往 [Cursor 集成](https://www.cursor.com/en/dashboard?tab=integrations)
2. 点击 Linear 旁边的 *Connect*
3. 连接你的 Linear 工作区并选择团队
4. 点击 *Authorize*
5. 在 Cursor 中完成剩余的 Background Agent 设置：
   * 连接 GitHub 并选择默认仓库
   * 启用按用量计费
   * 确认隐私设置

<div id="account-linking">
  ### 账户关联
</div>

首次使用时会在 Cursor 和 Linear 之间触发账户关联。创建 PR 需要已连接 GitHub。

<div id="how-to-use">
  ## 使用方式
</div>

把 issue 委派给 Cursor，或在评论中 @`@Cursor`。Cursor 会分析 issue，并自动过滤非开发类工作。

<div id="delegating-issues">
  ### 委派 issue
</div>

1. 打开 Linear issue
2. 点击 assignee 字段
3. 选择 “Cursor”

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c9a6536a083cfe4a7798c626360e53cc" alt="在 Linear 中将 issue 委派给 Cursor" data-og-width="1637" width="1637" data-og-height="1046" height="1046" data-path="images/integrations/linear/linear-delegate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b30e2ccb68c4a15b921cf86721878676 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1ac5dfd75e06451de0e688ff87e1ce4c 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7393e80c07e1fe5c33690a970029fe31 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2a07cc74a1d65581a341cf2225b51a37 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5684841fe823ef85472f74748730278c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f7818cae47a652e14557eb20f20b04e 2500w" />
</Frame>

<div id="mentioning-cursor">
  ### 提及 Cursor
</div>

在评论中提及 `@Cursor` 来指派新的代理，或补充进一步指令，例如：`@Cursor 修复上面提到的身份验证 bug`。

<div id="workflow">
  ## 工作流程
</div>

Background Agents 会在 Linear 中显示实时状态，并在完成后自动创建 PR。你可以在 [Cursor dashboard](https://www.cursor.com/dashboard?tab=background-agents) 跟踪进度。

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eecf562be6db4d44c397f4786b8ef273" alt="Background Agent 在 Linear 中的状态更新" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-activity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=238da245aee71392f22644cb85f7cee4 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21f515fbd2e5917fcf63b8801f66307 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f88441301e6d614ba47756cb886e023 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4927a8d00768a3dbbc0bd5be1faad80e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1707f8223126480c46639428ad5fc85a 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=74ca2ad37e8158bbb86188821bf96299 2500w" />
</Frame>

<div id="follow-up-instructions">
  ### 后续指令
</div>

你可以在 agent 会话中直接回复，消息会作为后续内容发送给 agent。只需在 Linear 的评论里 @`Cursor`，就能为正在运行的 Background Agent 提供更多指导。

<div id="configuration">
  ## 配置
</div>

在 [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents) 配置 Background Agent。

<div className="full-width-table">
  | Setting                | Location         | Description                           |
  | :--------------------- | :--------------- | :------------------------------------ |
  | **Default Repository** | Cursor Dashboard | 未配置项目仓库时使用的默认仓库                       |
  | **Default Model**      | Cursor Dashboard | Background Agents 使用的 AI 模型           |
  | **Base Branch**        | Cursor Dashboard | 用于创建 PR 的基础分支（通常是 `main` 或 `develop`） |
</div>

<div id="configuration-options">
  ### 配置选项
</div>

可以通过多种方式配置 Background Agent 的行为：

**Issue 描述或评论**：使用 `[key=value]` 语法，例如：

* `@cursor please fix [repo=anysphere/everysphere]`
* `@cursor implement feature [model=claude-3.5-sonnet] [branch=feature-branch]`

**Issue 标签**：使用父子标签结构，父标签为配置键，子标签为取值。

**Project 标签**：与 issue 标签相同的父子结构，在项目级应用。

支持的配置键：

* `repo`：指定目标仓库（例如 `owner/repository`）
* `branch`：指定创建 PR 的基础分支
* `model`：指定要使用的 AI 模型

<div id="repository-selection">
  ### 仓库选择
</div>

Cursor 按以下优先级确定要处理的仓库：

1. **Issue 描述/评论**：issue 文本或评论中的 `[repo=owner/repository]` 语法
2. **Issue 标签**：附加到具体 Linear issue 的仓库标签
3. **Project 标签**：附加到 Linear 项目的仓库标签
4. **默认仓库**：在 Cursor Dashboard 设置中指定的仓库

<div id="setting-up-repository-labels">
  #### 设置仓库标签
</div>

在 Linear 中创建仓库标签：

1. 进入 Linear 工作区的 **Settings**
2. 点击 **Labels**
3. 点击 **New group**
4. 将分组命名为 "repo"（不区分大小写——必须是 "repo"，不能是 "Repository" 或其他变体）
5. 在该分组下，为每个仓库按 `owner/repo` 格式创建标签

随后可以将这些标签分配给 issue 或项目，用于指定 Background Agent 应处理的仓库。

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6e2b90ce09957a72fdef3c1ed4ef93aa" alt="在 Linear 中配置仓库标签" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-project-labels.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1933d2112631527116bd1d817f1a6153 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=93f344ff848172ce6bd97ef652ab03de 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea9f19d7248f39086a20606c6ec14ac6 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=55bfa5cf5b87def6cbe51c3345579eee 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d99c0f06c5fbf33794408350b143f655 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1f731d1978dc5e60c545b745bb9d8ad 2500w" />
</Frame>

{/* ### Getting help

  Check [agent activity](https://www.cursor.com/dashboard?tab=background-agents) and include request IDs when contacting support.

  ## Feedback

  Share feedback through Linear comments or your Cursor dashboard support channels. */}

---

← Previous: [GitHub](./github.md) | [Index](./index.md) | Next: [Slack](./slack.md) →