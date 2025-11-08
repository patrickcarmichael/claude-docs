---
title: "GitHub Actions"
source: "https://docs.cursor.com/zh/cli/github-actions"
language: "zh"
language_name: "Chinese"
---

# GitHub Actions
Source: https://docs.cursor.com/zh/cli/github-actions

了解如何在 GitHub Actions 和其他持续集成系统中使用 Cursor CLI

在 GitHub Actions 和其他 CI/CD 系统中使用 Cursor CLI，自动化开发任务。

<div id="github-actions-integration">
  ## 集成 GitHub Actions
</div>

基础配置：

```yaml  theme={null}
- name: 安装 Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: 运行 Cursor Agent
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "你的提示词" --model gpt-5
```

<div id="cookbook-examples">
  ## 实用示例
</div>

查看我们的实用示例，了解具体工作流：[更新文档](/zh/cli/cookbook/update-docs) 和 [修复 CI 问题](/zh/cli/cookbook/fix-ci)。

<div id="other-ci-systems">
  ## 其他 CI 系统
</div>

只要满足以下条件，就能在任何 CI/CD 系统中使用 Cursor CLI：

* 支持**Shell 脚本执行**（bash、zsh 等）
* 通过**环境变量**配置 API key
* 具备**互联网连接**以访问 Cursor 的 API

<div id="autonomy-levels">
  ## 自主性级别
</div>

选择 agent 的自主性级别：

<div id="full-autonomy-approach">
  ### 完全自主方案
</div>

让 agent 全权控制 git 操作、API 调用和外部交互。设置更简单，但需要更多信任。

**示例：** 在我们的 [Update Documentation](/zh/cli/cookbook/update-docs) cookbook 中，第一个工作流让 agent 可以：

* 分析 PR 变更
* 创建并管理 git 分支
* 提交并推送更改
* 在 pull request 下发布评论
* 处理所有错误情形

```yaml  theme={null}
- name: 更新文档（完全自治）
  run: |
    cursor-agent -p "你拥有对 git、GitHub CLI 以及 PR 操作的完全访问权限。
    负责处理整个文档更新流程，包括提交、推送和 PR 评论。"
```

<div id="restricted-autonomy-approach">
  ### 受限自治方案
</div>

<Note>
  我们建议在生产 CI 工作流中，将此方案与**基于权限的约束**一起使用。这样你能两全其美：agent 可智能处理复杂分析与文件修改，而关键操作仍保持确定且可审计。
</Note>

将关键步骤放到独立的工作流步骤中处理，同时限制 agent 的操作。更可控、更可预测。

**示例：** 同一份 cookbook 中的第二个工作流将 agent 限制为仅进行文件修改：

```yaml  theme={null}
- name: 生成文档更新（受限）
  run: |
    cursor-agent -p "重要：不要创建分支、提交、推送，或在 PR 中发表评论。
    只修改工作目录中的文件。发布由后续的工作流步骤处理。"

- name: 发布文档分支（确定性）
  run: |
    # 由 CI 处理的确定性 git 操作
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: 更新此 PR"
    git push origin "docs/${{ github.head_ref }}"

- name: 发布 PR 评论（确定性）  
  run: |
    # 由 CI 处理的确定性 PR 评论
    gh pr comment ${{ github.event.pull_request.number }} --body "文档已更新"
```

<div id="permission-based-restrictions">
  ### 基于权限的限制
</div>

使用[权限配置](/zh/cli/reference/permissions)在 CLI 层面强制执行限制：

```json  theme={null}
{
  "permissions": {
    "allow": [
      "读取(**/*.md)",
      "写入(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": [
      "Shell(git)",
      "Shell(gh)", 
      "写入(.env*)",
      "写入(package.json)"
    ]
  }
}
```

<div id="authentication">
  ## 身份验证
</div>

<div id="generate-your-api-key">
  ### 生成你的 API 密钥
</div>

先在 Cursor 控制台[生成一个 API 密钥](/zh/cli/reference/authentication#api-key-authentication)。

<div id="configure-repository-secrets">
  ### 配置仓库机密
</div>

把你的 Cursor API 密钥安全地存到仓库里：

1. 打开你的 GitHub 仓库
2. 点击 **Settings** → **Secrets and variables** → **Actions**
3. 点击 **New repository secret**
4. 将名称设为 `CURSOR_API_KEY`
5. 将你的 API 密钥粘贴到值中
6. 点击 **Add secret**

<div id="use-in-workflows">
  ### 在工作流中使用
</div>

设置你的 `CURSOR_API_KEY` 环境变量：

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```

---

← Previous: [更新文档](./section.md) | [Index](./index.md) | Next: [使用无头 CLI](./cli.md) →