---
title: "GitHub"
source: "https://docs.cursor.com/zh/integrations/github"
language: "zh"
language_name: "Chinese"
---

# GitHub
Source: https://docs.cursor.com/zh/integrations/github

面向后台代理的官方 Cursor GitHub 应用

[Background Agents](/zh/background-agent) 和 [Bugbot](/zh/bugbot) 需要安装 Cursor GitHub 应用，才能克隆仓库并推送变更。

<div id="installation">
  ## 安装
</div>

1. 前往 [Dashboard 的 Integrations](https://cursor.com/dashboard?tab=integrations)
2. 点击 GitHub 旁的 **Connect**
3. 选择仓库：**All repositories** 或 **Selected repositories**

要断开 GitHub 账户，回到 integrations 仪表盘并点击 **Disconnect Account**。

<div id="using-agent-in-github">
  ## 在 GitHub 中使用 Agent
</div>

GitHub 集成让你可以直接在拉取请求和 issue 中运行后台 agent 工作流。只需在任意 PR 或 issue 里评论 `@cursor [prompt]`，就能触发 agent 读取上下文、应用修复并推送提交。

如果你启用了 [Bugbot](/zh/bugbot)，可以评论 `@cursor fix`，让后台 agent 读取 Bugbot 给出的修复建议并自动处理该 issue。

<div id="permissions">
  ## 权限
</div>

GitHub 应用需要特定权限才能与后台代理配合工作：

<div className="full-width-table">
  | 权限                        | 用途                   |
  | ------------------------- | -------------------- |
  | **Repository access**     | 克隆你的代码并创建工作分支        |
  | **Pull requests**         | 基于代理的更改创建 PR 供你查看与审核 |
  | **Issues**                | 追踪代理发现或修复的缺陷与任务      |
  | **Checks and statuses**   | 汇报代码质量与测试结果          |
  | **Actions and workflows** | 监控 CI/CD 流水线与部署状态    |
</div>

所有权限都遵循最小必要权限原则，仅限于后台代理运行所需。

<div id="ip-allow-list-configuration">
  ## IP 允许列表配置
</div>

如果你们的组织使用 GitHub 的 IP 允许列表来限制对代码仓库的访问，先联系支持为你的团队开启 IP 允许列表功能。

<div id="contact-support">
  ### 联系支持
</div>

在配置 IP 允许列表之前，先联系 [hi@cursor.com](mailto:hi@cursor.com) 为你的团队启用该功能。下面两种配置方式都需要先完成这一步。

<div id="enable-ip-allow-list-configuration-for-installed-github-apps-recommended">
  ### 为已安装的 GitHub App 启用 IP 允许列表（推荐）
</div>

Cursor 的 GitHub App 已预先配置了 IP 列表。你可以为已安装的应用启用允许列表，这样就会自动继承这份列表。我们推荐这种方式，因为我们会维护并更新该列表，你们的组织也会自动获得更新。

要启用：

1. 前往组织的 Security 设置
2. 进入 IP allow list 设置
3. 勾选 “Allow access by GitHub Apps”

详细步骤请参阅 [GitHub 文档](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps)。

<div id="add-ips-directly-to-your-allowlist">
  ### 直接将 IP 添加到允许列表
</div>

如果你们的组织在 GitHub 中使用由 IdP 定义的允许列表，或无法使用预配置的允许列表，也可以手动添加 IP 地址：

```
184.73.225.134
3.209.66.12
52.44.113.131
```

<Note>
  IP 地址列表可能会不定期变更。使用 IP 允许列表的团队会在添加或移除 IP 地址前提前收到通知。
</Note>

<div id="troubleshooting">
  ## 疑难解答
</div>

<AccordionGroup>
  <Accordion title="Agent 无法访问仓库">
    * 安装具备仓库访问权限的 GitHub 应用
    * 检查私有仓库的权限设置
    * 确认你的 GitHub 账号权限
  </Accordion>

  <Accordion title="无法对 Pull Request 执行操作（权限被拒）">
    * 为应用授予对 Pull Request 的写入权限
    * 检查分支保护规则
    * 如果应用安装已过期，重新安装
  </Accordion>

  <Accordion title="GitHub 设置中看不到应用">
    * 检查是否安装在组织层级
    * 从 [github.com/apps/cursor](https://github.com/apps/cursor) 重新安装
    * 如果安装损坏，联系支持
  </Accordion>
</AccordionGroup>

---

← Previous: [Git](./git.md) | [Index](./index.md) | Next: [Linear](./linear.md) →