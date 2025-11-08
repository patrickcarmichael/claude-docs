---
title: "Bugbot"
source: "https://docs.cursor.com/zh/bugbot"
language: "zh"
language_name: "Chinese"
---

# Bugbot
Source: https://docs.cursor.com/zh/bugbot

面向拉取请求的 AI 代码评审

Bugbot 会评审拉取请求，定位缺陷、安全漏洞以及代码质量问题。

<Tip>
  Bugbot 提供免费层：每位用户每月可享有限次数的免费 PR 评审。达到上限后，评审将暂停至下一个计费周期。你可以随时升级到 14 天免费 Pro 试用，享受不限次数评审（受标准滥用防护约束）。
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="Bugbot 在 PR 上留下评论" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

<div id="how-it-works">
  ## 运行机制
</div>

Bugbot 会分析 PR diff，并留下包含解释和修复建议的评论。它会在每次 PR 更新时自动运行，或在手动触发时运行。

* 在每次 PR 更新时执行**自动审查**
* 在任意 PR 下评论 `cursor review` 或 `bugbot run` 即可**手动触发**
* 点击**在 Cursor 中修复**会直接在 Cursor 中打开相关问题
* 点击**在 Web 中修复**会直接在 [cursor.com/agents](https://cursor.com/agents) 打开相关问题

<div id="setup">
  ## 设置
</div>

需要 Cursor 管理员权限和 GitHub 组织管理员权限。

1. 前往 [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot)
2. 打开 Bugbot 标签页
3. 点击 `Connect GitHub`（如果已连接则点击 `Manage Connections`）
4. 按照 GitHub 的安装流程完成配置
5. 返回仪表盘，在指定仓库启用 Bugbot

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Bugbot GitHub 设置" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

<div id="configuration">
  ## 配置
</div>

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### 仓库设置

    在安装列表中按仓库启用或禁用 Bugbot。Bugbot 只在你作为作者的 PR 上运行。

    ### 个人设置

    * 仅在被 @ 时运行：评论 `cursor review` 或 `bugbot run`
    * 每个 PR 只运行一次，跳过后续提交
  </Tab>

  <Tab title="Team">
    ### 仓库设置

    团队管理员可以按仓库启用 Bugbot、为审查者配置允许/拒绝列表，并设置：

    * 每个安装在每个 PR 上只运行一次，跳过后续提交
    * 禁用行内评审，防止 Bugbot 直接在代码行上留下评论

    无论是否属于团队，Bugbot 都会为已启用仓库的所有贡献者运行。

    ### 个人设置

    团队成员可以为自己的 PR 覆盖这些设置：

    * 仅在被 @ 时运行：评论 `cursor review` 或 `bugbot run`
    * 每个 PR 只运行一次，跳过后续提交
    * 启用草稿 PR 的评审，将草稿 Pull Request 纳入自动评审
  </Tab>
</Tabs>

<div id="analytics">
  ### 分析
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Bugbot 控制面板" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

<div id="rules">
  ## 规则
</div>

创建 `.cursor/BUGBOT.md` 文件，为审查提供项目特定的上下文。Bugbot 始终会包含根目录下的 `.cursor/BUGBOT.md` 文件，以及在从变更文件向上遍历时找到的任何其他文件。

```
project/
  .cursor/BUGBOT.md          # 始终包含（适用于整个项目的规则）
  backend/
    .cursor/BUGBOT.md        # 审阅后端文件时包含
    api/
      .cursor/BUGBOT.md      # 审阅 API 文件时包含
  frontend/
    .cursor/BUGBOT.md        # 审阅前端文件时包含
```

<AccordionGroup>
  <Accordion title="示例 .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # 项目审查指南

    ## 安全关注重点

    - 在 API 端点对用户输入进行校验
    - 检查数据库查询是否存在 SQL 注入风险
    - 确保受保护路由已正确实施身份验证

    ## 架构模式

    - 对服务使用依赖注入
    - 在数据访问层采用仓储（Repository）模式
    - 使用自定义错误类实现健全的错误处理

    ## 常见问题

    - React 组件内存泄漏（检查 useEffect 的清理逻辑）
    - UI 组件缺少错误边界
    - 命名约定不一致（函数使用 camelCase）

    ```
  </Accordion>
</AccordionGroup>

<div id="pricing">
  ## 价格
</div>

Bugbot 提供两个档位：**免费** 和 **专业版**。

<div id="free-tier">
  ### 免费方案
</div>

每位用户每月都有一定数量的免费 PR 审查。团队中每位成员都有各自的免费审查配额。达到上限后，审查会暂停，直到下一个计费周期。你可以随时升级到 14 天免费 Pro 试用，获取无限次审查。

<div id="pro-tier">
  ### 专业版
</div>

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### 统一定价

    每月 \$40，可在所有仓库中对每月最多 200 个 PR 进行不限次数的 Bugbot 审查。

    ### 入门

    在账户设置中订阅。
  </Tab>

  <Tab title="Teams">
    ### 按用户计费

    团队按每位用户每月 \$40 计费，享受不限次数的审查。

    我们将当月有 PR 被 Bugbot 审查过的作者计为一个用户。

    每个计费周期开始时，所有许可都会被释放，并按先到先得的方式重新分配。如果某位用户当月没有提交任何由 Bugbot 审查的 PR，该席位就可以给其他用户使用。

    ### 席位上限

    团队管理员可以设置每月的 Bugbot 席位上限来控制成本。

    ### 入门

    通过团队控制台订阅以启用计费。

    ### 滥用防护

    为防止滥用，我们为每个 Bugbot 许可设置了每月 200 个 pull request 的共享上限。如果每月需要超过 200 个 pull request，欢迎通过 [hi@cursor.com](mailto:hi@cursor.com) 联系我们，我们很乐意帮你解决。

    比如，如果你的团队有 100 位用户，你的组织起初每月可以审查 20,000 个 pull request。如果你自然达到了该上限，欢迎联系到我们，我们很乐意提高限额。
  </Tab>
</Tabs>

<div id="troubleshooting">
  ## 疑难排查
</div>

如果 Bugbot 不工作：

1. 通过在评论中加入 `cursor review verbose=true` 或 `bugbot run verbose=true` 来**启用详细模式**，以获取详细日志和请求 ID
2. **检查权限**，确认 Bugbot 具有仓库访问权限
3. **核实安装**，确认 GitHub 应用已安装并启用

在反馈问题时，请附上详细模式中的请求 ID。

<div id="faq">
  ## 常见问题
</div>

<AccordionGroup>
  <Accordion title="Bugbot 是否符合隐私模式要求？">
    是的，Bugbot 遵循与 Cursor 相同的隐私合规标准，数据处理方式也与其他 Cursor 请求完全一致。
  </Accordion>

  <Accordion title="触及免费档额度后会怎样？">
    当你达到每月的免费档额度时，Bugbot 的评审会暂停，直到下一个结算周期。你可以升级到 Pro 的 14 天免费试用，享受不限次数的评审（受标准滥用防护约束）。
  </Accordion>
</AccordionGroup>

```
```

---

← Previous: [Web 与移动端](./web.md) | [Index](./index.md) | Next: [代码评审](./section.md) →