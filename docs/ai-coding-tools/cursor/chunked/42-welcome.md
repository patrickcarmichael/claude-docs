# Welcome

**Navigation:** [← Previous](./41-slack.md) | [Index](./index.md) | [Next →](./43-github-actions.md)

---

# Welcome
Source: https://docs.cursor.com/zh-Hant/welcome

了解 Cursor 與如何開始使用

Cursor 是一款由 AI 驅動的程式碼編輯器，能理解你的程式碼庫，並透過自然語言幫你更快寫程式。只要描述想做或要修改的內容，Cursor 就會替你產生程式碼。

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=bf7bbe430ee044eea33a0ca66edf910d" className="rounded-lg" data-og-width="2000" width="2000" data-og-height="1275" height="1275" data-path="images/welcome.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fa28a55e9896b15cbec778edf8597b5f 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=701e61d65b8f296aba427b3fe79d5360 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8cf10e0727ab76689bc983e9d69d002f 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=cddcb51dd8ccf60c6fc0b4135f3e6933 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e2e9068dc6b3e9b81c4124e7736ecd8f 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=2bd03fc2dc3a340795c5bfa868b7d30b 2500w" />
</Frame>

<CardGroup cols={3}>
  <Card title="Get started" icon="rocket" href="/zh-Hant/get-started/installation">
    <div>
      下載、安裝，幾分鐘內就能用 Cursor 開始開發
    </div>
  </Card>

  <Card title="Changelog" icon="sparkles" href="https://www.cursor.com/changelog">
    <div>
      隨時掌握最新功能與改進
    </div>
  </Card>

  <Card title="CLI" icon="terminal" href="/zh-Hant/cli/overview">
    <div>
      在終端機使用 Cursor
    </div>
  </Card>

  <Card title="Concepts" icon="lightbulb" href="/zh-Hant/get-started/concepts">
    <div>
      了解驅動 Cursor 的核心概念與功能
    </div>
  </Card>

  <Card title="Models" icon="brain" href="/zh-Hant/models">
    <div>
      探索可用的 AI 模型，並學會如何選對模型
    </div>
  </Card>

  <Card title="Guides" icon="book" href="/zh-Hant/guides/working-with-context">
    <div>
      學習不同情境下的最佳實務與工作流程
    </div>
  </Card>

  <Card title="Downloads" icon="download" href="https://cursor.com/downloads" arrow>
    <div>
      下載適用於你電腦的 Cursor
    </div>
  </Card>

  <Card title="Forum" icon="message" href="https://forum.cursor.com">
    <div>
      有技術問題或想分享經驗，來逛逛論壇
    </div>
  </Card>

  <Card title="Support" icon="headset" href="mailto:hi@cursor.com">
    <div>
      帳號與帳單問題，寄信給我們的支援團隊
    </div>
  </Card>
</CardGroup>



# 代理安全
Source: https://docs.cursor.com/zh/account/agent-security

使用 Cursor Agent 的安全注意事项

提示注入、AI 幻觉等问题可能会让 AI 出现出乎意料、甚至潜在恶意的行为。我们正从更底层持续应对提示注入，但在 Cursor 的产品里，当前的主要防护是对代理可执行的操作设置护栏，包括默认对敏感操作要求手动批准。本文档旨在说明这些护栏，以及你可以期待它们做到什么。

以下所有控制与行为均为我们的默认且推荐设置。

<div id="first-party-tool-calls">
  ## 第一方工具调用
</div>

Cursor 内置了一些工具，能让 agent 帮你写代码。这些工具包括读取文件、编辑、调用终端命令、上网查文档等。

读取类工具不需要批准（比如读取文件、跨代码库搜索）。你可以用 [.cursorignore](/zh/context/ignore-files) 完全阻止 agent 访问特定文件；除此之外，读取一般无需批准。对存在敏感数据外泄风险的操作，我们要求明确批准。

在当前工作区内修改文件通常不需要明确批准，但有一些例外。agent 对文件的更改会立刻写入磁盘。我们建议在受版本控制的工作区中使用 Cursor，这样可以随时回滚文件内容。对于会修改我们 IDE/CLI 配置的文件（例如编辑器的工作区设置文件），在变更前我们要求明确批准。另外，如果启用了文件变更自动重载，需要注意，agent 的修改可能会在你审阅之前触发自动执行。

任何由 agent 建议的终端命令默认都需要批准。我们建议你在执行前审查每条命令。愿意承担风险的用户可以选择允许 agent 无需批准执行所有命令。Cursor 提供了一个 [allowlist](/zh/agent/tools) 功能，但它不属于安全控制。有些用户会允许特定命令，但这只是尽力而为的机制，可能存在被绕过的情况。我们不建议使用“Run Everything”，它会绕过任何已配置的 allowlist。

<div id="third-party-tool-calls">
  ## 第三方工具调用
</div>

Cursor 支持通过 [MCP](/zh/context/mcp) 连接外部工具。所有第三方 MCP 连接都必须由用户明确批准。用户一旦批准某个 MCP，默认情况下，Agent Mode 中每个外部 MCP 集成所建议的每一次工具调用，在执行前都必须再次得到明确批准。

<div id="network-requests">
  ## 网络请求
</div>

攻击者可能会利用网络请求窃取数据。我们目前只允许第一方工具对极少数主机（如 GitHub）发起网络请求、进行显式链接检索，以及使用有限的提供商进行网页搜索；除此之外均不支持。默认设置会阻止代理发起任意网络请求。

<div id="workspace-trust">
  ## 工作区信任
</div>

Cursor IDE 支持标准的 [workspace trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) 功能，默认是「已禁用」。打开新工作区时，工作区信任会提示你选择正常模式或受限模式。受限模式会导致 AI 等你常用的 Cursor 功能无法正常工作。对于不信任的代码仓库，建议使用其他工具，例如基础文本编辑器。

你可以按以下步骤在用户设置中启用工作区信任：

1. 打开你的 user settings.json 文件
2. 添加以下配置：
   ```json  theme={null}
   "security.workspace.trust.enabled": true
   ```

也可以通过移动设备管理（MDM）方案在组织范围内强制启用此设置。

<div id="responsible-disclosure">
  ## 负责任披露
</div>

如果你认为在 Cursor 中发现了安全漏洞，请按照我们 GitHub 安全页面上的指南在那里提交报告。无法使用 GitHub 的话，也可以发邮件到 [security@cursor.com](mailto:security@cursor.com) 联系我们。

我们承诺在 5 个工作日内确认收到漏洞报告，并会尽快处理。处理结果将以安全公告的形式发布在我们的 GitHub 安全页面。对于严重事件，我们会同时在 GitHub 安全页面发布公告，并向所有用户发送邮件通知。



# Billing
Source: https://docs.cursor.com/zh/account/billing

管理 Cursor 订阅、退款和发票

<div id="how-do-i-access-billing-settings">
  ### 怎么进入结算设置？
</div>

通过 [Dashboard](https://cursor.com/dashboard) 打开结算门户，在 Dashboard 里点击“Billing”。这会打开一个用于所有结算任务的安全门户。

<div id="what-are-cursors-billing-cycles">
  ### Cursor 的结算周期是怎样的？
</div>

结算周期按月或按年，从订阅日开始计算。Teams 账户按席位计费，并对新增成员进行按比例计费。

<div id="how-do-seats-work-for-teams-accounts">
  ### Teams 账户的席位如何计费？
</div>

Teams 账户按席位收费（每位团队成员一个席位）。在周期中途添加成员时，只会为其剩余时间收费。若成员已使用过任何额度并被移除，其席位会保留到本结算周期结束——不提供按比例退款。团队管理员可通过 dashboard 管理席位。

<div id="can-i-switch-between-monthly-and-annual-billing">
  ### 我可以在月付和年付之间切换吗？
</div>

可以！步骤如下：

**Pro 方案**

1. 前往 Cursor [dashboard](https://cursor.com/dashboard)
2. 在左侧边栏点击“Billing and Invoices”进入结算页面
3. 点击“Manage subscription”
4. 点击“Update subscription”
5. 选择“Yearly”或“Monthly”，然后点击“Continue”

**Teams 方案**

1. 前往 Cursor [dashboard](https://cursor.com/dashboard)
2. 在左侧边栏点击“Billing and Invoices”进入结算页面
3. 点击“Upgrade Now”按钮切换到年付

<Note>
  只能自行从月付切换到年付。若要从年付切换到月付，请通过
  [hi@cursor.com](mailto:hi@cursor.com) 联系我们。
</Note>

<div id="where-can-i-find-my-invoices">
  ### 哪里能找到我的发票？
</div>

在结算门户可查看全部结算历史。支持查看并下载当前和历史发票。

<div id="can-i-get-invoices-automatically-emailed-to-me">
  ### 可以自动把发票通过邮件发送给我吗？
</div>

目前需要在结算门户手动下载发票。我们正在开发发票自动邮件功能，上线后你可以选择开启。

<div id="how-do-i-update-my-billing-information">
  ### 怎么更新我的结算信息？
</div>

通过结算门户更新支付方式、公司名称、地址和税务信息。我们使用 Stripe 保障交易安全。变更只影响后续发票，历史发票无法修改。

<div id="how-do-i-cancel-my-subscription">
  ### 怎么取消我的订阅？
</div>

在 Billing and Invoices 页面点击“Manage Subscription”，然后点击“Cancel subscription”取消订阅。取消后可继续使用到当前结算周期结束。

<div id="im-having-other-billing-issues-how-can-i-get-help">
  ### 我还有其他结算问题，如何获取帮助？
</div>

对于此处未涵盖的结算问题，请使用与你账户关联的邮箱发送邮件至 [hi@cursor.com](mailto:hi@cursor.com)。请附上你的账户信息和问题描述。



# 定价
Source: https://docs.cursor.com/zh/account/pricing

Cursor 的方案与定价

你可以免费试用 Cursor，或购买个人版或团队版。

<div id="individual">
  ## 个人
</div>

所有个人方案包含：

* 无限次 Tab 补全
* 对所有模型的扩展代理（Agent）使用上限
* 可使用 Bugbot
* 可使用后台代理（Background Agents）

每个方案都按模型推理的 [API 价格](/zh/models#model-pricing)计费其用量：

* Pro 含 \$20 的 API 代理用量 + 额外奖励用量
* Pro Plus 含 \$70 的 API 代理用量 + 额外奖励用量
* Ultra 含 \$400 的 API 代理用量 + 额外奖励用量

我们会努力在保证包含用量之外赠送额外奖励容量。由于不同模型的 API 成本不同，你选择的模型会影响 token 输出以及包含用量的消耗速度。你可以在[你的仪表盘](https://cursor.com/dashboard?tab=usage)查看用量和 token 明细。编辑器里也会常规显示限额通知。

<img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c42b8ad6347f6fe9d075647dfece934c" alt="Usage limits" style={{ borderRadius: 16 }} data-og-width="666" width="666" data-og-height="394" height="394" data-path="images/account/usage-limits.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1ca3b5ab64a6ba6f3ad7d75b1ee72e2 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d39dc254e7d059ac24310f26ea47dd5d 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=153472f14b4c10ec9a096b7a9db59888 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc8b0cdb5c0677e45c1a082d0002880 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=cf4ac9875f5e587d16d4c6f1e7fdc057 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=13f21676cda8e4c2973bc3371892f4aa 2500w" />

<div id="how-much-usage-do-i-need">
  ### 我需要大概多少用量？
</div>

根据我们的用量数据，你可以参考以下用量水平：

* **每日使用 Tab 的用户**：基本都能控制在 \$20 以内
* **偶尔用 Agent 的用户**：通常不超出包含的 \$20
* **每天用 Agent 的用户**：一般每月总用量 $60–$100
* **重度用户（多个 agent/自动化）**：通常每月总用量 \$200 起

根据我们的用量数据，对*中位数用户*来说，额度大致相当于：

* Pro：约 225 次 Sonnet 4 请求、约 550 次 Gemini 请求，或约 500 次 GPT 5 请求
* Pro+：约 675 次 Sonnet 4 请求、约 1,650 次 Gemini 请求，或约 1,500 次 GPT 5 请求
* Ultra：约 4,500 次 Sonnet 4 请求、约 11,000 次 Gemini 请求，或约 10,000 次 GPT 5 请求

<div id="what-happens-when-i-reach-my-limit">
  ### 达到限额后会怎样？
</div>

当你超出每月包含的用量时，编辑器会提醒你，你可以选择：

* **添加按需用量**：按使用量付费，按照相同的 API 费率继续使用 Cursor
* **升级套餐**：升到更高档位，获得更多包含用量

按需用量按月结算，费率与包含用量相同。请求的质量和速度绝不会被降级。

<div id="teams">
  ## Teams
</div>

有两种 Teams 方案：Teams（\$40/用户/月）和 Enterprise（自定义）。

Teams 方案提供的附加功能包括：

* 强制开启隐私模式（Privacy Mode）
* 带使用统计的管理面板（Admin Dashboard）
* 团队统一计费
* 基于 SAML/OIDC 的单点登录（SSO）

如果你更喜欢自助使用，推荐选 Teams。需要优先支持、共享用量、发票结算、SCIM 或更高级安全控制的，推荐使用[Enterprise](/zh/contact-sales)。

了解更多[Teams 定价](/zh/account/teams/pricing)。

<div id="auto">
  ## Auto
</div>

启用 Auto 后，Cursor 会根据当前需求选择最适合当下任务、且在当下负载下可靠性最高的高端模型。该功能可检测到输出性能退化，并自动切换模型加以解决。

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f039569ed0dc2ad7e02bb1b2e9cea71" data-og-width="2256" width="2256" data-og-height="1248" height="1248" data-path="images/models/model-picker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=49c6a091945972253eb6e819593e45f0 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f9bddfb2e130789d8d51a3d1a4eeba94 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=db7273f399bb5decfed9d1b06f389df4 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=920fe98d4f99b5d7fddd47a14fb45699 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3b049686e5826263800b63299f4c19ca 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=72ddd56b4d3ea9b2efa4001a155566fd 2500w" />
</Frame>

<Note>我们在 Auto 的质量和整体性能上投入很大。自 9 月 15 日之后的下一次账单续期起，Auto 将按以下 API 费率计费。</Note>

* **Input + Cache Write**：每 1M tokens 收费 \$1.25
* **Output**：每 1M tokens 收费 \$6.00
* **Cache Read**：每 1M tokens 收费 \$0.25

编辑器和控制台都会显示你的用量（包括 Auto）。如果更倾向于直接选择某个模型，用量将按该模型的公开 API 价格计费。

<div id="max-mode">
  ## Max 模式
</div>

部分模型支持 [Max 模式](/zh/models#max-mode)，可启用更长的推理过程，并将上下文窗口扩展至最多 1M 个 token。虽然大多数编码任务不需要 Max 模式，但在处理更复杂的查询，尤其是大型文件或代码库时，它会很有帮助。启用 Max 模式会消耗更多用量。你可以在 [你的控制台](https://cursor.com/dashboard?tab=usage) 查看所有请求与 token 使用明细。

<div id="bugbot">
  ## Bugbot
</div>

Bugbot 是与 Cursor 订阅分开的独立产品，并有自己的定价方案。

* **Pro**（\$40/月）：对每月最多 200 个 PR 提供不限次数审查、无限访问 Cursor Ask、与 Cursor 集成以修复 bug，并可使用 Bugbot Rules
* **Teams**（\$40/用户/月）：对所有 PR 提供不限次数的代码审查、无限访问 Cursor Ask、团队用量共享，以及高级规则和设置
* **Enterprise**（自定义）：包含 Teams 的全部功能，外加高级分析与报告、优先支持和账户管理

了解更多 [Bugbot 定价](https://cursor.com/bugbot#pricing)。

<div id="background-agent">
  ## 后台代理
</div>

后台代理按所选的[模型](/zh/models)的 API 定价计费。首次使用后台代理时，会提示你设置支出上限。

<Info>
  后台代理的虚拟机（VM）计算费用将于日后公布。
</Info>



# Admin API
Source: https://docs.cursor.com/zh/account/teams/admin-api

通过 API 访问团队指标、使用数据和支出信息

Admin API 让你以编程方式访问团队数据，包括成员信息、使用指标和支出详情。你可以构建自定义仪表盘、监控工具，或与现有工作流集成。

<Note>
  该 API 为首个发布版本。我们会根据反馈逐步扩展功能——告诉我们你需要哪些端点！
</Note>

<div id="authentication">
  ## 身份验证
</div>

所有 API 请求都需要使用 API 密钥进行身份验证。只有团队管理员可以创建和管理 API 密钥。

API 密钥与组织绑定，对所有管理员可见，且不受原始创建者账号状态影响。

<div id="creating-an-api-key">
  ### 创建 API Key
</div>

1. 前往 **cursor.com/dashboard** → **Settings** 标签页 → **Cursor Admin API Keys**
2. 点击 **Create New API Key**
3. 给密钥起个清晰易懂的名字（例如：“Usage Dashboard Integration”）
4. 立刻复制生成的密钥——之后将无法再次查看

格式：`key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### 使用你的 API 密钥
</div>

在基本身份验证中，将你的 API 密钥作为用户名：

**使用 curl 进行基本身份验证：**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**或者直接设置 Authorization 标头：**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## 基础 URL
</div>

所有 API 端点都使用：

```
https://api.cursor.com
```

<div id="endpoints">
  ## 端点
</div>

<div id="get-team-members">
  ### 获取团队成员
</div>

获取所有团队成员及其详细信息。

```
GET /teams/members
```

#### 响应

返回一个团队成员对象的数组：

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: '拥有者' | '成员' | '免费拥有者';
  }[];
}
```

<div id="example-responses">
  #### 示例回复
</div>

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "成员"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "拥有者"
    }
  ]
}

```

<div id="example-requests">
  #### 示例请求
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u 你的API密钥：
```

<div id="get-daily-usage-data">
  ### 获取每日用量数据
</div>

在指定日期范围内获取你团队的每日用量指标，了解代码编辑、AI 协作使用情况与接受率等详细洞察。

```
POST /teams/daily-usage-data
```

#### 请求体

<div className="full-width-table">
  | 参数          | 类型     | 必填 | 描述             |
  | :---------- | :----- | :- | :------------- |
  | `startDate` | number | 是  | 起始日期（Epoch 毫秒） |
  | `endDate`   | number | 是  | 结束日期（Epoch 毫秒） |
</div>

<Note>
  日期范围不能超过 90 天。更长的时间段请分多次发起请求。
</Note>

#### 返回

```typescript  theme={null}
{
  data: {
    date: number;
    isActive: boolean;
    totalLinesAdded: number;
    totalLinesDeleted: number;
    acceptedLinesAdded: number;
    acceptedLinesDeleted: number;
    totalApplies: number;
    totalAccepts: number;
    totalRejects: number;
    totalTabsShown: number;
    totalTabsAccepted: number;
    composerRequests: number;
    chatRequests: number;
    agentRequests: number;
    cmdkUsages: number;
    subscriptionIncludedReqs: number;
    apiKeyReqs: number;
    usageBasedReqs: number;
    bugbotUsages: number;
    mostUsedModel: string;
    applyMostUsedExtension?: string;
    tabMostUsedExtension?: string;
    clientVersion?: string;
    email?: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### 响应字段
</div>

<div className="full-width-table">
  | 字段                         | 描述                |
  | :------------------------- | :---------------- |
  | `date`                     | 以 epoch 毫秒表示的日期   |
  | `isActive`                 | 该日用户是否活跃          |
  | `totalLinesAdded`          | 新增代码行数            |
  | `totalLinesDeleted`        | 删除代码行数            |
  | `acceptedLinesAdded`       | 来自已接受 AI 建议的新增行数  |
  | `acceptedLinesDeleted`     | 来自已接受 AI 建议的删除行数  |
  | `totalApplies`             | Apply 操作次数        |
  | `totalAccepts`             | 接受的建议数            |
  | `totalRejects`             | 拒绝的建议数            |
  | `totalTabsShown`           | 显示的 Tab 补全次数      |
  | `totalTabsAccepted`        | 接受的 Tab 补全次数      |
  | `composerRequests`         | Composer 请求数      |
  | `chatRequests`             | Chat 请求数          |
  | `agentRequests`            | Agent 请求数         |
  | `cmdkUsages`               | 命令面板（Cmd+K）使用次数   |
  | `subscriptionIncludedReqs` | 订阅内请求数            |
  | `apiKeyReqs`               | API Key 请求数       |
  | `usageBasedReqs`           | 按用量计费请求数          |
  | `bugbotUsages`             | Bug 检测使用次数        |
  | `mostUsedModel`            | 最常用的 AI 模型        |
  | `applyMostUsedExtension`   | Apply 使用最频繁的文件扩展名 |
  | `tabMostUsedExtension`     | Tab 使用最频繁的文件扩展名   |
  | `clientVersion`            | Cursor 版本         |
  | `email`                    | 用户邮箱              |
</div>

<div id="example-responses">
  #### 示例回复
</div>

```json  theme={null}
{
  "data": [
    {
      "date": 1710720000000,
      "isActive": true,
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalApplies": 87,
      "totalAccepts": 73,
      "totalRejects": 14,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "cmdkUsages": 67,
      "subscriptionIncludedReqs": 180,
      "apiKeyReqs": 0,
      "usageBasedReqs": 5,
      "bugbotUsages": 3,
      "mostUsedModel": "gpt-4",
      "applyMostUsedExtension": ".tsx",
      "tabMostUsedExtension": ".ts",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    },
    {
      "date": 1710806400000,
      "isActive": true,
      "totalLinesAdded": 2104,
      "totalLinesDeleted": 1203,
      "acceptedLinesAdded": 1876,
      "acceptedLinesDeleted": 987,
      "totalApplies": 102,
      "totalAccepts": 91,
      "totalRejects": 11,
      "totalTabsShown": 456,
      "totalTabsAccepted": 398,
      "composerRequests": 67,
      "chatRequests": 156,
      "agentRequests": 23,
      "cmdkUsages": 89,
      "subscriptionIncludedReqs": 320,
      "apiKeyReqs": 15,
      "usageBasedReqs": 0,
      "bugbotUsages": 5,
      "mostUsedModel": "claude-3-opus",
      "applyMostUsedExtension": ".py",
      "tabMostUsedExtension": ".py",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

<div id="example-requests">
  #### 示例请求
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u 你的_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### 获取支出数据
</div>

支持通过搜索、排序和分页检索本日历月的支出信息。

```
POST /teams/spend
```

#### 请求体

<div className="full-width-table">
  | 参数              | 类型     | 必填 | 描述                                     |
  | :-------------- | :----- | :- | :------------------------------------- |
  | `searchTerm`    | string | 否  | 在用户名和邮箱中搜索                             |
  | `sortBy`        | string | 否  | 排序字段：`amount`、`date`、`user`。默认值：`date` |
  | `sortDirection` | string | 否  | 排序方向：`asc`、`desc`。默认值：`desc`           |
  | `page`          | number | 否  | 页码（从 1 开始）。默认值：`1`                     |
  | `pageSize`      | number | 否  | 每页结果数                                  |
</div>

#### 返回

```typescript  theme={null}
{
  teamMemberSpend: {
    spendCents: number;
    fastPremiumRequests: number;
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
    hardLimitOverrideDollars: number;
  }[];
  subscriptionCycleStart: number;
  totalMembers: number;
  totalPages: number;
}
```

<div id="response-fields">
  #### 响应字段
</div>

<div className="full-width-table">
  | 字段                         | 描述                 |
  | :------------------------- | :----------------- |
  | `spendCents`               | 总花费（单位：美分）         |
  | `fastPremiumRequests`      | Fast 高级模型请求数       |
  | `name`                     | 成员名称               |
  | `email`                    | 成员邮箱               |
  | `role`                     | 团队角色               |
  | `hardLimitOverrideDollars` | 自定义支出上限（美元）        |
  | `subscriptionCycleStart`   | 订阅周期起始时间（Epoch 毫秒） |
  | `totalMembers`             | 团队成员总数             |
  | `totalPages`               | 总页数                |
</div>

<div id="example-responses">
  #### 示例回复
</div>

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "member",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "owner",
      "hardLimitOverrideDollars": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

<div id="example-requests">
  #### 示例请求
</div>

**基础消费数据：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**分页搜索指定用户：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

<div id="get-usage-events-data">
  ### 获取使用事件数据
</div>

通过完整的筛选、搜索和分页选项，为你的团队获取详细的使用事件数据。这个端点提供关于单次 API 调用、模型使用、令牌（token）消耗和成本的细粒度洞察。

```
POST /teams/filtered-usage-events
```

#### 请求体

<div className="full-width-table">
  | 参数          | 类型     | 必填 | 描述                 |
  | :---------- | :----- | :- | :----------------- |
  | `startDate` | number | 否  | 起始日期（epoch 毫秒）     |
  | `endDate`   | number | 否  | 结束日期（epoch 毫秒）     |
  | `userId`    | number | 否  | 按指定用户 ID 过滤        |
  | `page`      | number | 否  | 页码（从 1 开始）。默认值：`1` |
  | `pageSize`  | number | 否  | 每页返回数量。默认值：`10`    |
  | `email`     | string | 否  | 按用户邮箱地址过滤          |
</div>

#### 返回

```typescript  theme={null}
{
  totalUsageEventsCount: number; // 使用事件总数
  pagination: {
    numPages: number; // 总页数
    currentPage: number; // 当前页
    pageSize: number; // 每页大小
    hasNextPage: boolean; // 是否有下一页
    hasPreviousPage: boolean; // 是否有上一页
  };
  usageEvents: {
    timestamp: string; // 时间戳
    model: string; // 模型
    kind: string; // 类型
    maxMode: boolean; // 是否为最大模式
    requestsCosts: number; // 请求成本
    isTokenBasedCall: boolean; // 是否为按 Token 计费调用
    tokenUsage?: {
      inputTokens: number; // 输入 Token
      outputTokens: number; // 输出 Token
      cacheWriteTokens: number; // 缓存写入 Token
      cacheReadTokens: number; // 缓存读取 Token
      totalCents: number; // 总费用（美分）
    };
    isFreeBugbot: boolean; // 是否为免费 Bugbot
    userEmail: string; // 用户邮箱
  }[];
  period: {
    startDate: number; // 开始日期（时间戳）
    endDate: number; // 结束日期（时间戳）
  };
}
```

<div id="response-fields-explained">
  #### 响应字段说明
</div>

<div className="full-width-table">
  | 字段                      | 说明                                    |
  | :---------------------- | :------------------------------------ |
  | `totalUsageEventsCount` | 与查询匹配的使用事件总数                          |
  | `pagination`            | 用于浏览结果的分页元数据                          |
  | `timestamp`             | 事件时间戳（自纪元起的毫秒数）                       |
  | `model`                 | 此请求使用的 AI 模型                          |
  | `kind`                  | 使用类别（例如，“按用量计费”、“商用版包含”）              |
  | `maxMode`               | 是否启用了 Max 模式                          |
  | `requestsCosts`         | 按请求计量单位计算的成本                          |
  | `isTokenBasedCall`      | 当事件按令牌用量计费时为 true                     |
  | `tokenUsage`            | 令牌用量明细（当 isTokenBasedCall 为 true 时可用） |
  | `isFreeBugbot`          | 是否为免费 Bugbot 使用                       |
  | `userEmail`             | 发起请求的用户邮箱                             |
  | `period`                | 查询数据的日期范围                             |
</div>

<div id="example-responses">
  #### 示例回复
</div>

```json  theme={null}
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "model": "claude-4-opus",
      "kind": "按用量计费",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750979173824",
      "model": "claude-4-opus",
      "kind": "Usage-based",
      "maxMode": true,
      "requestsCosts": 10,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 5805,
        "outputTokens": 311,
        "cacheWriteTokens": 11964,
        "cacheReadTokens": 0,
        "totalCents": 40.16699999999999
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750978339901",
      "model": "claude-4-sonnet-thinking",
      "kind": "包含在商务版中"
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isFreeBugbot": false,
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

<div id="example-requests">
  #### 示例请求
</div>

**使用默认分页获取所有使用事件：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**按日期范围和指定用户筛选：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**获取特定用户的使用事件（支持自定义分页）：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### 设置用户花费上限
</div>

为各个团队成员设置花费上限。这样就能控制每个用户在团队内使用 AI 的花费额度。

```
POST /teams/user-spend-limit
```

<Note>
  **速率限制：** 每个团队每分钟最多 60 次请求
</Note>

#### 请求体

<div className="full-width-table">
  | 参数                  | 类型     | 必填 | 说明                    |
  | :------------------ | :----- | :- | :-------------------- |
  | `userEmail`         | string | 是  | 团队成员的邮箱地址             |
  | `spendLimitDollars` | number | 是  | 以美元计的花费上限（仅限整数，不含小数）。 |
</div>

<Note>
  * 该用户必须已是你团队的成员
  * 只接受整数值（不含小数金额）
  * 将 `spendLimitDollars` 设为 0 会把上限设为 \$0
</Note>

#### 响应

返回一个标准化的响应，用于指示成功或失败：

```typescript  theme={null}
{
  outcome: 'success' | 'error';
  message: string;
}
```

<div id="example-responses">
  #### 示例回复
</div>

**已成功设置限制：**

```json  theme={null}
{
  "outcome": "success",
  "message": "已将用户 developer@company.com 的支出上限设为 $100"
}
```

**错误响应：**

```json  theme={null}
{
  "outcome": "error",
  "message": "邮箱格式无效"
}
```

<div id="example-requests">
  #### 示例请求
</div>

**设置消费上限：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### Repo Blocklists API
</div>

添加仓库并使用匹配规则，防止文件或目录被索引，或被用作你团队的上下文。

<div id="get-team-repo-blocklists">
  #### 获取团队仓库黑名单
</div>

检索你团队配置的所有仓库黑名单。

```
GET /settings/repo-blocklists/repos
```

<div id="response">
  ##### 响应
</div>

返回一个仓库封禁列表对象的数组：

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-response">
  ##### 示例回复
</div>

```json  theme={null}
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

<div id="example-request">
  ##### 示例请求
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u 你的_API_KEY:
```

<div id="upsert-repo-blocklists">
  #### 覆盖更新 Repo 阻止列表
</div>

为提供的仓库替换其现有的阻止列表。
*注意：此端点只会覆盖所提供仓库的匹配模式，其他仓库不受影响。*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### 请求体
</div>

| 参数    | 类型    | 必填 | 说明         |
| ----- | ----- | -- | ---------- |
| repos | array | 是  | 仓库阻止列表对象数组 |

每个仓库对象必须包含：

| 字段       | 类型        | 必填 | 说明                      |
| -------- | --------- | -- | ----------------------- |
| url      | string    | 是  | 要加入阻止列表的仓库 URL          |
| patterns | string\[] | 是  | 要阻止的文件模式数组（支持 glob 通配符） |

<div id="response">
  ##### 响应
</div>

返回更新后的仓库封锁列表：

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-request">
  ##### 示例请求
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      },
      {
        "url": "https://github.com/company/internal-tools", 
        "patterns": ["*"]
      }
    ]
  }'
```

<div id="delete-repo-blocklist">
  #### 删除仓库封锁列表
</div>

从封锁列表中移除指定仓库。

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### 参数
</div>

| 参数     | 类型     | 必填 | 描述            |
| ------ | ------ | -- | ------------- |
| repoId | string | 是  | 要删除的仓库黑名单的 ID |

<div id="response">
  ##### 响应
</div>

删除成功时返回 204 No Content。

<div id="example-request">
  ##### 示例请求
</div>

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u 你的_API_KEY:
```

<div id="pattern-examples">
  #### 模式示例
</div>

常见的 blocklist 模式：

* `*` - 屏蔽整个仓库
* `*.env` - 屏蔽所有 .env 文件
* `config/*` - 屏蔽 config 目录中的所有文件
* `**/*.secret` - 屏蔽任意子目录中的所有 .secret 文件
* `src/api/keys.ts` - 屏蔽指定文件



# AI Code Tracking API
Source: https://docs.cursor.com/zh/account/teams/ai-code-tracking-api

获取你团队代码库的 AI 生成代码分析

获取你团队代码库的 AI 生成代码分析。支持按提交查看 AI 使用情况，以及精细到变更级别的已接受 AI 修改。

<Note>
  该 API 为首个发布版本。我们会根据反馈持续扩展能力——告诉我们你需要哪些接口！
</Note>

* **Availability**: 仅限企业团队
* **Status**: Alpha（响应结构和字段可能变动）

<div id="authentication">
  ## 身份验证
</div>

所有 API 请求都需要使用 API 密钥进行身份验证。该 API 使用与其他端点相同的 Admin API 身份验证方式。

想了解更详细的身份验证说明，去看 [Admin API 身份验证](/zh/account/teams/admin-api#authentication)。

<div id="base-url">
  ## 基础 URL
</div>

所有 API 端点均使用：

```
https://api.cursor.com
```

<div id="rate-limits">
  ## 速率限制
</div>

* 每个团队在每个端点上每分钟最多 5 次请求

<div id="query-parameters">
  ## 查询参数
</div>

以下所有端点都通过查询字符串接受相同的查询参数：

<div className="full-width-table">
  | 参数          | 类型     | 是否必填 | 描述                                                                                                               |                                                              |
  | :---------- | :----- | :--- | :--------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
  | `startDate` | string | date | 否                                                                                                                | ISO 日期字符串、字面量 "now"，或相对天数（例如 "7d"，表示 now - 7 天）。默认：now - 7 天 |
  | `endDate`   | string | date | 否                                                                                                                | ISO 日期字符串、字面量 "now"，或相对天数（例如 "0d"）。默认：now                    |
  | `page`      | number | 否    | 页码（从 1 开始）。默认：1                                                                                                  |                                                              |
  | `pageSize`  | number | 否    | 每页结果数。默认：100，最大：1000                                                                                             |                                                              |
  | `user`      | string | 否    | 可选的单用户过滤。可填写邮箱（例如 [developer@company.com](mailto:developer@company.com)）、编码 ID（例如 user\_abc123...），或数值 ID（例如 42） |                                                              |
</div>

<Note>
  响应中的 userId 会以带有前缀 user\_ 的外部编码 ID 返回，供 API 稳定使用。
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## 语义与指标的计算方式
</div>

* **Sources**："TAB" 表示接受的内联补全；"COMPOSER" 表示来自 Composer 的已接受差异（diff）
* **Lines metrics**：tabLinesAdded/Deleted 和 composerLinesAdded/Deleted 分别统计；nonAiLinesAdded/Deleted 计算为 max(0, totalLines - AI lines)
* **Privacy mode**：如果在客户端启用，某些元数据（例如 fileName）可能会被省略
* **Branch info**：当当前分支等于仓库的默认分支时，isPrimaryBranch 为 true；如果仓库信息不可用，可能为 undefined

你可以查看该文件，了解如何检测并上报提交与变更。

<div id="endpoints">
  ## 端点
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### 获取 AI 提交指标（JSON，分页）
</div>

获取按提交聚合的指标，将代码行归因于 TAB、COMPOSER 和非 AI。

```
GET /analytics/ai-code/commits
```

<div id="response">
  #### 返回
</div>

```typescript  theme={null}
{
  items: AiCommitMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### AiCommitMetric 字段
</div>

<div className="full-width-table">
  | 字段                     | 类型      | 描述                         |               |
  | :--------------------- | :------ | :------------------------- | ------------- |
  | `commitHash`           | string  | Git 提交哈希                   |               |
  | `userId`               | string  | 编码后的用户 ID（例如：user\_abc123） |               |
  | `userEmail`            | string  | 用户邮箱地址                     |               |
  | `repoName`             | string  | null                       | 仓库名称          |
  | `branchName`           | string  | null                       | 分支名称          |
  | `isPrimaryBranch`      | boolean | null                       | 是否为主分支        |
  | `totalLinesAdded`      | number  | 提交中新增加的总行数                 |               |
  | `totalLinesDeleted`    | number  | 提交中删除的总行数                  |               |
  | `tabLinesAdded`        | number  | 通过 Tab 补全新增的行数             |               |
  | `tabLinesDeleted`      | number  | 通过 Tab 补全删除的行数             |               |
  | `composerLinesAdded`   | number  | 通过 Composer 新增的行数          |               |
  | `composerLinesDeleted` | number  | 通过 Composer 删除的行数          |               |
  | `nonAiLinesAdded`      | number  | null                       | 非 AI 新增的行数    |
  | `nonAiLinesDeleted`    | number  | null                       | 非 AI 删除的行数    |
  | `message`              | string  | null                       | 提交说明          |
  | `commitTs`             | string  | null                       | 提交时间戳（ISO 格式） |
  | `createdAt`            | string  | 写入时间戳（ISO 格式）              |               |
</div>

<div id="example-response">
  #### 示例响应
</div>

```json  theme={null}
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "重构：提取 analytics 客户端"
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

<div id="example-requests">
  #### 示例请求
</div>

**基本请求：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u 你的_API_KEY:
```

**按用户（邮箱）筛选：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u 你的API密钥：
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### 下载 AI Commit 指标（CSV，流式）
</div>

以 CSV 格式下载提交指标数据，适用于大批量数据导出。

```
GET /analytics/ai-code/commits.csv
```

#### 响应

请求头：

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV 列
</div>

<div className="full-width-table">
  | 列                        | 类型      | 描述                |
  | :----------------------- | :------ | :---------------- |
  | `commit_hash`            | string  | Git 提交哈希值         |
  | `user_id`                | string  | 编码后的用户 ID         |
  | `user_email`             | string  | 用户邮箱地址            |
  | `repo_name`              | string  | 仓库名称              |
  | `branch_name`            | string  | 分支名称              |
  | `is_primary_branch`      | boolean | 是否为主分支            |
  | `total_lines_added`      | number  | 此次提交新增的总行数        |
  | `total_lines_deleted`    | number  | 此次提交删除的总行数        |
  | `tab_lines_added`        | number  | 通过 Tab 补全新增的行数    |
  | `tab_lines_deleted`      | number  | 通过 Tab 补全删除的行数    |
  | `composer_lines_added`   | number  | 通过 Composer 新增的行数 |
  | `composer_lines_deleted` | number  | 通过 Composer 删除的行数 |
  | `non_ai_lines_added`     | number  | 非 AI 新增的行数        |
  | `non_ai_lines_deleted`   | number  | 非 AI 删除的行数        |
  | `message`                | string  | 提交消息              |
  | `commit_ts`              | string  | 提交时间戳（ISO 格式）     |
  | `created_at`             | string  | 导入时间戳（ISO 格式）     |
</div>

<div id="sample-csv-output">
  #### 示例 CSV 输出
</div>

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"重构：抽取 Analytics 客户端",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"添加错误处理",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-requests">
  #### 示例请求
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u 你的 API 密钥: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### 获取 AI 代码变更指标（JSON，分页）
</div>

检索按确定性 changeId 分组的细粒度已接受 AI 变更。可用于在不依赖提交的情况下分析已接受的 AI 事件。

```
GET /analytics/ai-code/changes
```

<div id="response">
  #### 返回
</div>

```typescript  theme={null}
{
  items: AiCodeChangeMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### AiCodeChangeMetric 字段
</div>

<div className="full-width-table">
  | 字段                  | 类型     | 描述                         |          |
  | :------------------ | :----- | :------------------------- | -------- |
  | `changeId`          | string | 更改的确定性 ID                  |          |
  | `userId`            | string | 编码后的用户 ID（例如：user\_abc123） |          |
  | `userEmail`         | string | 用户邮箱地址                     |          |
  | `source`            | "TAB"  | "COMPOSER"                 | AI 更改来源  |
  | `model`             | string | null                       | 所用 AI 模型 |
  | `totalLinesAdded`   | number | 新增总行数                      |          |
  | `totalLinesDeleted` | number | 删除总行数                      |          |
  | `createdAt`         | string | 写入时间戳（ISO 格式）              |          |
  | `metadata`          | Array  | 文件元数据（隐私模式下 fileName 可能省略） |          |
</div>

<div id="example-response">
  #### 示例响应
</div>

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "Composer",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
      "metadata": [
        { "fileName": "src/analytics/report.ts", "fileExtension": "ts", "linesAdded": 12, "linesDeleted": 3 },
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

<div id="example-requests">
  #### 示例请求
</div>

**基本请求：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u 你的_API_KEY:
```

**按用户（编码后的 ID）筛选：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u YOUR_API_KEY:
```

**按用户（邮箱）筛选：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u YOUR_API_KEY:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### 下载 AI 代码变更指标（CSV，流式）
</div>

以 CSV 格式下载变更指标数据，适用于大规模数据抽取。

```
GET /analytics/ai-code/changes.csv
```

#### 响应

Headers:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV 列
</div>

<div className="full-width-table">
  | 列                     | 类型     | 描述                      |
  | :-------------------- | :----- | :---------------------- |
  | `change_id`           | string | 该变更的确定性 ID              |
  | `user_id`             | string | 编码后的用户 ID               |
  | `user_email`          | string | 用户的电子邮箱地址               |
  | `source`              | string | AI 变更来源（TAB 或 COMPOSER） |
  | `model`               | string | 使用的 AI 模型               |
  | `total_lines_added`   | number | 新增行总数                   |
  | `total_lines_deleted` | number | 删除行总数                   |
  | `created_at`          | string | 摄取时间戳（ISO 格式）           |
  | `metadata_json`       | string | JSON 字符串化的元数据条目数组       |
</div>

<div id="notes">
  #### 备注
</div>

* metadata\_json 是 JSON 字符串化的元数据条目数组（隐私模式下可能省略 fileName）
* 处理 CSV 时，务必解析带引号的字段

<div id="sample-csv-output">
  #### 示例 CSV 输出
</div>

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-requests">
  #### 示例请求
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u YOUR_API_KEY: \
  -o changes.csv
```

<div id="tips">
  ## 提示
</div>

* 使用 `user` 参数可在所有端点中快速筛选单个用户
* 对于大规模数据抽取，优先使用 CSV 端点——它们会在服务器端以每页 10,000 条记录的方式进行流式传输
* 如果客户端无法解析默认分支，`isPrimaryBranch` 可能为 undefined
* `commitTs` 是提交时间戳；`createdAt` 是我们服务器上的摄取时间
* 当客户端启用隐私模式时，某些字段可能不会返回

<div id="changelog">
  ## 更新日志
</div>

* **Alpha 版本发布**：提供用于提交（commits）和变更（changes）的初始端点（endpoints）。响应结构可能会根据反馈而调整



# Analytics
Source: https://docs.cursor.com/zh/account/teams/analytics

跟踪团队使用情况和活动指标

团队管理员可以在[仪表盘](/zh/account/teams/dashboard)中查看并跟踪各项指标。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a8a4a0ca334e5f5acac55307b2ebeadf" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=73c11df8fcb2862e5c1fd551e6399159 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c3eaa0d4faa7d6fdf5e3c79dfd11fb5a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e9ee5fc554ae46e9d0e2cf53c19e652d 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5f0afded72e0b02142c5a85e448f2d4e 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a6dec2a182ac88d7de75f7a42b1f5ff 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a8ac7dafe559da435f3f4974b04df52 2500w" />
</Frame>

<div id="total-usage">
  ### Total Usage
</div>

查看团队层面的汇总指标，包括总标签页数和高级请求数。对于创建未满 30 天的团队，指标反映自创建以来的使用情况，并包含成员加入前的个人活动。

<div id="per-active-user">
  ### Per Active User
</div>

查看每位活跃用户的平均指标：接受的标签页数、代码行数以及高级请求数。

<div id="user-activity">
  ### User Activity
</div>

跟踪每周和每月的活跃用户数。

<div id="analytics-report-headers">
  ## 分析报告表头
</div>

当你从控制台导出分析数据时，报告会包含关于用户行为和功能使用的详细指标。下面是每个表头的含义：

<div id="user-information">
  ### 用户信息
</div>

<ResponseField name="Date" type="ISO 8601 timestamp">
  记录分析数据的日期（例如：2024-01-15T04:30:00.000Z）
</ResponseField>

<ResponseField name="User ID" type="string">
  系统中每个用户的唯一标识符
</ResponseField>

<ResponseField name="Email" type="string">
  与用户账号关联的邮箱地址
</ResponseField>

<ResponseField name="Is Active" type="boolean">
  表示用户在该日期是否处于活跃状态
</ResponseField>

<div id="ai-generated-code-metrics">
  ### AI 生成代码指标
</div>

<ResponseField name="Chat Suggested Lines Added" type="number">
  AI 聊天功能建议添加的代码行总数
</ResponseField>

<ResponseField name="Chat Suggested Lines Deleted" type="number">
  AI 聊天功能建议删除的代码行总数
</ResponseField>

<ResponseField name="Chat Accepted Lines Added" type="number">
  用户接受并添加到代码中的 AI 建议行数
</ResponseField>

<ResponseField name="Chat Accepted Lines Deleted" type="number">
  用户接受的 AI 建议删除行数
</ResponseField>

<div id="feature-usage-metrics">
  ### 功能使用指标
</div>

<ResponseField name="Chat Total Applies" type="number">
  用户从聊天中应用 AI 生成改动的次数
</ResponseField>

<ResponseField name="Chat Total Accepts" type="number">
  用户接受 AI 建议的次数
</ResponseField>

<ResponseField name="Chat Total Rejects" type="number">
  用户拒绝 AI 建议的次数
</ResponseField>

<ResponseField name="Chat Tabs Shown" type="number">
  向用户展示 AI 建议标签页的次数
</ResponseField>

<ResponseField name="Tabs Accepted" type="number">
  被用户接受的 AI 建议标签页数
</ResponseField>

<div id="request-type-metrics">
  ### 请求类型指标
</div>

<ResponseField name="Edit Requests" type="number">
  通过 composer/edit 功能发起的请求（Cmd+K 内联编辑）
</ResponseField>

<ResponseField name="Ask Requests" type="number">
  用户向 AI 提问的聊天请求
</ResponseField>

<ResponseField name="Agent Requests" type="number">
  发给 AI 代理（专用 AI 助手）的请求
</ResponseField>

<ResponseField name="Cmd+K Usages" type="number">
  使用 Cmd+K（或 Ctrl+K）命令面板的次数
</ResponseField>

<div id="subscription-and-api-metrics">
  ### 订阅与 API 指标
</div>

<ResponseField name="Subscription Included Reqs" type="number">
  由用户订阅计划覆盖的 AI 请求
</ResponseField>

<ResponseField name="API Key Reqs" type="number">
  使用 API 密钥进行编程访问的请求
</ResponseField>

<ResponseField name="Usage-Based Reqs" type="number">
  计入按用量计费的请求
</ResponseField>

<div id="additional-features">
  ### 其他功能
</div>

<ResponseField name="Bugbot Usages" type="number">
  使用缺陷检测/修复 AI 功能的次数
</ResponseField>

<div id="configuration-information">
  ### 配置信息
</div>

<ResponseField name="Most Used Model" type="string">
  用户最常使用的 AI 模型（例如：GPT-4、Claude）
</ResponseField>

<ResponseField name="Most Used Apply Extension" type="string">
  应用 AI 建议时最常用的文件扩展名（例如：.ts、.py、.java）
</ResponseField>

<ResponseField name="Most Used Tab Extension" type="string">
  使用 Tab 补全功能时最常用的文件扩展名
</ResponseField>

<ResponseField name="Client Version" type="string">
  使用中的 Cursor 编辑器版本
</ResponseField>

<div id="calculated-metrics">
  ### 计算指标
</div>

报告还包含有助于理解 AI 代码贡献的加工数据：

* Total Lines Added/Deleted：所有代码变更的原始计数
* Accepted Lines Added/Deleted：源自 AI 建议并被接受的行数
* Composer Requests：通过内联 composer 功能发起的请求
* Chat Requests：通过聊天界面发起的请求

<Note>
  若未提供，所有数值型字段默认为 0，布尔型字段默认为 false，字符串字段默认为空字符串。指标按日按用户聚合。
</Note>



# Analytics V2
Source: https://docs.cursor.com/zh/account/teams/analyticsV2

高级团队使用与活动指标跟踪

我们正在推出分析基础设施的 V2 版本，其中包含对各类指标采集方式的重构。

自**2025 年 9 月 1 日**起，且对于使用**Cursor 1.5 版本**的用户，分析功能将切换至我们的 V2 基础设施。较早版本会对多项指标低估计数，包括：

* 接受的代码行总数
* 建议的代码行总数
* 接受的补全总数

请持续关注，我们会继续投入分析能力，并在这一领域发布新功能。



# Dashboard
Source: https://docs.cursor.com/zh/account/teams/dashboard

在你的控制面板中管理账单、用量和团队设置

控制面板让你查看账单、设置按用量计费，并管理你的团队。

<div id="overview">
  ## 概览
</div>

快速了解团队活动、使用统计和最新变更。概览页为你的工作区提供开箱即看的关键信息。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=48ee98a4d9b168b93c26a03c1af74ddd" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2ac6f157659354866eaa03b38cd1eb90 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8e9e84e894a3faf2846e3aae5deb9a2b 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1034c739d961ccc69c17ba947edda90 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dbeed5506f7ae3fc4fabc7d248d69e64 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=afac07ce763fccf7eded7248fb990745 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4ed8c8161c3f2a964371a237134b1ae 2500w" />
</Frame>

<div id="settings">
  ## 设置
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5edb18df1ddc2d20e69abdd83140a509" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4d4c8f244231868bf4111f05b1f46c93 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=582ddf5415a973010e3bcbeeb13d4f64 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74a5d5f4644b701adc25b6d847f5752e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9250830c64e8c3490c3ca6f7b6f65eec 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7ce96a620ac6d447e79abd901b5c6cdc 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6d24738577e0ffd837d87f8926339215 2500w" />
</Frame>

配置团队级的偏好和安全设置。设置页面包括：

<div id="teams-enterprise-settings">
  ## 团队与企业设置
</div>

<AccordionGroup>
  <Accordion title="隐私设置">
    管理团队的数据共享偏好。为 AI 提供商（OpenAI、Anthropic、Google Vertex AI、xAi Grok）配置零数据保留策略，并在团队范围内强制执行隐私策略。
  </Accordion>

  {" "}

  <Accordion title="按用量计费设置">
    启用按用量计费并设置支出上限。可配置团队月度总上限和可选的按用户上限。还可控制是否仅管理员可以修改这些设置。
  </Accordion>

  {" "}

  <Accordion title="Bedrock IAM 角色">
    配置 AWS Bedrock IAM 角色，实现安全的云端集成。
  </Accordion>

  {" "}

  <Accordion title="单点登录（SSO）">
    为企业团队设置 SSO 身份验证，简化用户访问并提升安全性。
  </Accordion>

  {" "}

  <Accordion title="Cursor 管理 API 密钥">
    创建和管理用于以编程方式访问 Cursor 管理功能的 API 密钥。
  </Accordion>

  {" "}

  <Accordion title="活动会话">
    监控并管理团队范围内的活动用户会话。
  </Accordion>

  <Accordion title="邀请码管理">
    创建和管理用于添加新团队成员的的邀请码。
  </Accordion>

  <Accordion title="API 端点">
    访问 Cursor 的 REST API 端点以进行程序化集成。所有 API 端点在 Team 和 Enterprise 方案中均可使用，唯独 [AI Code Tracking API](/zh/docs/account/teams/ai-code-tracking-api) 需要 Enterprise 订阅。
  </Accordion>
</AccordionGroup>

<div id="enterprise-only-settings">
  ## 仅限 Enterprise 的设置
</div>

<AccordionGroup>
  {" "}

  <Accordion title="Model Access Control">
    控制团队成员可用的 AI 模型。可对特定模型或模型等级设置限制，以管理成本并确保在组织内合规、适度地使用。
  </Accordion>

  {" "}

  <Accordion title="Auto Run Configuration (0.49+)">
    为 Cursor 0.49 及以上版本配置自动命令执行。控制可自动执行的命令，并为代码执行设定安全策略。
  </Accordion>

  <Accordion title="Repository Blocklist">
    因安全或合规需求，阻止访问特定代码仓库。
  </Accordion>

  {" "}

  <Accordion title="MCP Configuration (0.51+)">
    为 Cursor 0.51 及以上版本配置 Model Context Protocol。管理模型如何从开发环境访问与处理上下文。
  </Accordion>

  {" "}

  <Accordion title="Cursor Ignore Configuration (0.50+)">
    为 Cursor 0.50 及以上版本设置文件与目录的忽略规则。控制哪些文件和目录会被排除在 AI 分析与建议之外。
  </Accordion>

  <Accordion title=".cursor Directory Protection (0.51+)">
    在 0.51 及以上版本中保护 .cursor 目录免受未授权访问。确保敏感的配置与缓存文件安全。
  </Accordion>

  <Accordion title="AI Code Tracking API">
    获取团队仓库的 AI 生成代码详尽分析。通过 REST API 端点检索按提交划分的 AI 使用指标，以及更细粒度的已接受 AI 变更。需 Enterprise 方案。更多信息见[此处](/zh/account/teams/ai-code-tracking-api)。
  </Accordion>
</AccordionGroup>

<Note>
  **SCIM**（跨域身份管理系统）配置同样适用于 Enterprise 方案。设置说明参见我们的[SCIM 文档](/zh/account/teams/scim)。
</Note>

<div id="members">
  ## 成员
</div>

管理团队成员、邀请新用户并控制访问权限。设置基于角色的权限，监控成员活动。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4ac43692626733caf2da4b53e4cd9055" data-og-width="1390" width="1390" data-og-height="591" height="591" data-path="images/account/team/members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a2a24d3282df1e875d73fd2bf29b9c04 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1abe9715816149f577a5d9c9e2f3545d 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ccc84260c5139119e5b16ad6c214af72 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5fe34e422fa9540004c25a61570029c3 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dee7c3ade8ef46b5ead5dbe2bfd2a6be 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a42bce921a799886b8e3e0a389b8589 2500w" />
</Frame>

<div id="integrations">
  ## 集成
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=187b9e77d6b99c77caec81e1b3063417" data-og-width="1390" width="1390" data-og-height="592" height="592" data-path="images/account/team/integrations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=470d5697ff2bfb9db2ae745b2c33cce6 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1e7d589f1f208ecdba9840629897968 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2285e05c99c3a6ace609b51770475a3e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7c44649c5e8cd0f2a3791a3085252eca 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0cf7111171c8019f7a59adc79cb9639d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8423a209b4e1c753045dca1514cbfbad 2500w" />
</Frame>

{" "}

把 Cursor 跟常用的工具和服务连起来。配置与版本控制系统、项目管理工具，以及其他开发者服务的集成。

<div id="background-agents">
  ## 后台代理
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=187b9e77d6b99c77caec81e1b3063417" data-og-width="1390" width="1390" data-og-height="592" height="592" data-path="images/account/team/integrations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=470d5697ff2bfb9db2ae745b2c33cce6 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1e7d589f1f208ecdba9840629897968 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2285e05c99c3a6ace609b51770475a3e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7c44649c5e8cd0f2a3791a3085252eca 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0cf7111171c8019f7a59adc79cb9639d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8423a209b4e1c753045dca1514cbfbad 2500w" />
</Frame>

{" "}

在工作区中监控并管理后台代理。查看代理状态、日志和资源占用。

<div id="bugbot">
  ## Bugbot
</div>

使用自动化的缺陷检测与修复功能。Bugbot 会自动识别并修复代码库中的常见问题。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=20d841dfc7837445103a933dab18b470" alt="Bugbot 代码评审" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/bugbot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=975f5e3f9f9a0334c8a5bcc12faf72be 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=17099f8bbe0701750d0ba212879d8a93 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=041c82a4c3bada0524527609dfc134a4 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90ac57ea38768ace4b9404476fafdf32 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5785673a93f899ccca7b70e7a3752ef7 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a1a1dc51872967e392e10d6b85c31a04 2500w" />
</Frame>

<div id="active-directory-management">
  ## Active Directory 管理
</div>

面向企业团队，通过集成 Active Directory 管理用户身份验证和访问。配置 SSO 和用户预配。

<div id="usage">
  ## 使用
</div>

跟踪详细的使用指标，包括 AI 请求、模型用量和资源消耗。按团队成员和项目维度监控使用情况。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8744e41430d162199d85ca8e966c91cd" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc43eaaeca3c2a531a56243037a7a53f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=34700d63fabf072e9906aab74f79f7d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7f2bcdb271d6b30e333374c798638989 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=424bd0eeda69200668f8f0b86dc360bf 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f0e716c72f01a3297a53a5b63d191ef4 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffa574322508a07cc5ab867b331b6d35 2500w" />
</Frame>

<div id="billing-invoices">
  ## 结算与发票
</div>

管理订阅、更新付款方式、查看结算历史。可下载发票，并配置按用量计费设置。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d76d20a7fafc6ed2135f2f9c78ec6c2d" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/billing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45501f34dd144ecd74e982fe5f8f8364 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=19860b61e083a8550cb3caa16bdb1ba0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7005bae381a362b39980a49113ca367c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e47c9ee55e3699ba46429b0ac0563b5b 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=039106fd5ff42f2e343b2b853614e7e7 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e598f83559985558f5825a3da25bb554 2500w" />
</Frame>



# 企业设置
Source: https://docs.cursor.com/zh/account/teams/enterprise-settings

为你的组织集中管理 Cursor 设置

<div id="enterprise-settings">
  # 企业设置
</div>

可以通过设备管理方案对 Cursor 的特定功能进行集中管理，确保满足组织需求。当你指定 Cursor 策略时，其取值会覆盖用户设备上相应的 Cursor 设置。

设置编辑器显示“Extensions: Allowed”设置由组织统一管理。

Cursor 目前提供以下可由管理员控制的功能策略：

| Policy            | Description                          | Cursor setting           | Available since |
| ----------------- | ------------------------------------ | ------------------------ | --------------- |
| AllowedExtensions | 控制哪些扩展可以安装。                          | extensions.allowed       | 1.2             |
| AllowedTeamId     | 控制允许登录的团队 ID。使用未授权团队 ID 的用户会被强制退出登录。 | cursorAuth.allowedTeamId | 1.3             |

<div id="configure-allowed-extensions">
  ## 配置允许的扩展
</div>

`extensions.allowed` 是 Cursor 的一个设置项，用来控制哪些扩展可以安装。它接受一个 JSON 对象，其中键为发布者名称，值为布尔类型，表示是否允许该发布者的扩展。

例如，将 `extensions.allowed` 设置为 `{"anysphere": true, "github": true}` 会允许来自 Anysphere 和 GitHub 的扩展；而设置为 `{"anysphere": false}` 则会禁止 Anysphere 的扩展。

如果想在组织层面集中管理允许的扩展，可以通过你的设备管理方案配置 `AllowedExtensions` 策略。该策略会覆盖用户设备上的 `extensions.allowed` 设置。此策略的值是一个 JSON 字符串，用于定义被允许的发布者。

想了解更多 Cursor 的扩展信息，去看看扩展文档。

<div id="configure-allowed-team-ids">
  ## 配置允许的团队 ID
</div>

`cursorAuth.allowedTeamId` 是 Cursor 的一个设置项，用于控制哪些团队 ID 可以登录 Cursor。该设置接受以逗号分隔的团队 ID 列表，只有列表中的团队 ID 才有访问权限。

例如，将 `cursorAuth.allowedTeamId` 设置为 `"1,3,7"` 时，来自这些团队 ID 的用户可以登录。

当用户尝试使用不在允许列表中的团队 ID 登录时：

* 会被立即强制登出
* 会显示错误消息
* 应用会阻止继续进行身份验证，直到使用有效的团队 ID

想要在组织层面集中管理允许的团队 ID，可以通过你的设备管理解决方案配置 `AllowedTeamId` 策略。该策略会覆盖用户设备上的 `cursorAuth.allowedTeamId` 设置。该策略的值为一个字符串，包含以逗号分隔的授权团队 ID 列表。

<div id="group-policy-on-windows">
  ## Windows 上的组策略
</div>

Cursor 支持基于 Windows 注册表的组策略。安装策略定义后，管理员可以使用本地组策略编辑器管理策略值。

要添加策略：

1. 从 `AppData\Local\Programs\cursor\policies` 复制 ADMX 和 ADML 策略文件。
2. 将 ADMX 文件放入 `C:\Windows\PolicyDefinitions` 目录，将 ADML 文件放入 `C:\Windows\PolicyDefinitions\<your-locale>\` 目录。
3. 重启本地组策略编辑器。
4. 在本地组策略编辑器中设置相应的策略值（例如，在 `AllowedExtensions` 策略中设置 `{"anysphere": true, "github": true}`）。

策略既可以在计算机级别设置，也可以在用户级别设置。如果两者都设置，计算机级别将优先生效。当策略值被设置后，该值会覆盖在任何级别（默认、用户、工作区等）配置的 Cursor 设置。

<div id="configuration-profiles-on-macos">
  ## macOS 上的配置描述文件
</div>

配置描述文件用于管理 macOS 设备上的设置。配置描述文件是一个包含与可用策略相对应键值对的 XML 文件。这些描述文件可以通过移动设备管理（MDM）方案部署，或手动安装。

<Accordion title="示例 .mobileconfig 文件">
  下面是一个适用于 macOS 的 `.mobileconfig` 文件示例：

  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  <plist version="1.0">
  	<dict>
  		<key>PayloadContent</key>
  		<array>
  			<dict>
  				<key>PayloadDisplayName</key>
  				<string>Cursor</string>
  				<key>PayloadIdentifier</key>
  				<string>com.todesktop.230313mzl4w4u92.J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadType</key>
  				<string>com.todesktop.230313mzl4w4u92</string>
  				<key>PayloadUUID</key>
  				<string>J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadVersion</key>
  				<integer>1</integer>
  				<key>AllowedExtensions</key>
  				<string>{"anysphere":true}</string>
  				<key>AllowedTeamId</key>
  				<string>1,2</string>
  			</dict>
  		</array>
  		<key>PayloadDescription</key>
  		<string>This profile manages Cursor.</string>
  		<key>PayloadDisplayName</key>
  		<string>Cursor</string>
  		<key>PayloadIdentifier</key>
  		<string>com.todesktop.230313mzl4w4u92</string>
  		<key>PayloadOrganization</key>
  		<string>Anysphere</string>
  		<key>PayloadType</key>
  		<string>Configuration</string>
  		<key>PayloadUUID</key>
  		<string>F2C1A7B3-9D4E-4B2C-8E1F-7A6C5D4B3E2F</string>
  		<key>PayloadVersion</key>
  		<integer>1</integer>
  		<key>TargetDeviceType</key>
  		<integer>5</integer>
  	</dict>
  </plist>
  ```
</Accordion>

<div id="string-policies">
  ### 字符串类策略
</div>

下面的示例演示如何配置 `AllowedExtensions` 策略。示例文件中该策略的值初始为空（不允许任何扩展）。

```
<key>允许的扩展名</key>
<string></string>
```

在 `<string>` 标签之间添加用于定义策略的相应 JSON 字符串。

```
<key>AllowedExtensions</key>
<string>{"anysphere": true, "github": true}</string>
```

对于 `AllowedTeamId` 策略，添加以逗号分隔的团队 ID 列表：

```
<key>AllowedTeamId</key>
<string>1,3,7</string>
```

**重要：** 提供的 `.mobileconfig` 文件会初始化该版本 Cursor 中可用的**所有**策略。请删除任何不需要的策略。

如果你没有在示例 `.mobileconfig` 中编辑或移除某个策略，该策略将按其默认（更为严格）的值被强制执行。

要手动安装配置描述文件，在 Finder 中双击该 `.mobileconfig` 文件，然后在“系统设置”的 **通用** > **设备管理** 中启用它。从“系统设置”中移除该描述文件会同时从 Cursor 中移除这些策略。

关于配置描述文件的更多信息，请参阅 Apple 的文档。

<div id="additional-policies">
  ## 其他策略
</div>

我们的目标是把当前的 Cursor 设置上升为策略，并尽可能与现有设置保持一致，从而确保命名和行为一致。如果需要新增策略，请在 Cursor 的 GitHub 仓库里提交 issue。团队会评估是否已有对应该行为的设置，或是否需要创建一个新设置来控制所需的行为。

<div id="frequently-asked-questions">
  ## 常见问题
</div>

<div id="does-cursor-support-configuration-profiles-on-linux">
  ### Cursor 在 Linux 上是否支持配置档案？
</div>

对 Linux 的支持不在当前路线图中。如果你对在 Linux 上使用配置档案感兴趣，欢迎在 Cursor 的 GitHub 仓库提交 issue，并分享你的具体使用场景。



# 成员与角色
Source: https://docs.cursor.com/zh/account/teams/members

管理团队成员和角色

Cursor 团队有三种角色：

<div id="roles">
  ## 角色
</div>

**Members** 是默认角色，能使用 Cursor 的 Pro 功能。

* 完整使用 Cursor 的 Pro 功能
* 无法访问账单设置或管理控制台
* 可以查看自己的使用情况和剩余额度（基于用量的预算）

**Admins** 负责团队管理和安全设置。

* 完整使用 Pro 功能
* 添加/移除成员、修改角色、配置 SSO
* 配置按用量计费与支出上限
* 访问团队分析数据

**Unpaid Admins** 可在不占用付费席位的情况下管理团队——非常适合不需要使用 Cursor 的 IT 或财务人员。

* 不计费，无法使用 Pro 功能
* 拥有与 Admins 相同的管理权限

<Info>使用 Unpaid Admins 前，团队中至少需要有一名付费用户。</Info>

<div id="role-comparison">
  ## 角色对比
</div>

<div className="full-width-table">
  | 能力           |  成员 | 管理员 | 未付费管理员 |
  | ------------ | :-: | :-: | :----: |
  | 使用 Cursor 功能 |  ✓  |  ✓  |        |
  | 邀请成员         |  ✓  |  ✓  |    ✓   |
  | 移除成员         |     |  ✓  |    ✓   |
  | 更改用户角色       |     |  ✓  |    ✓   |
  | 管理员仪表板       |     |  ✓  |    ✓   |
  | 配置 SSO/安全    |     |  ✓  |    ✓   |
  | 管理账务         |     |  ✓  |    ✓   |
  | 查看分析数据       |     |  ✓  |    ✓   |
  | 管理访问权限       |     |  ✓  |    ✓   |
  | 设置使用限制       |     |  ✓  |    ✓   |
  | 需要付费席位       |  ✓  |  ✓  |        |
</div>

<div id="managing-members">
  ## 管理成员
</div>

所有团队成员都可以邀请他人。我们目前不限制邀请。

<div id="add-member">
  ### 添加成员
</div>

有三种方式添加成员：

1. **邮件邀请**

   * 点击 `Invite Members`
   * 输入邮箱地址
   * 用户会收到邮件邀请

2. **邀请链接**

   * 点击 `Invite Members`
   * 复制 `Invite Link`
   * 分享给团队成员

3. **SSO**
   * 在 [admin dashboard](/zh/account/teams/sso) 配置 SSO
   * 用户使用 SSO 邮箱登录时会自动加入

<Warning>
  邀请链接的有效期很长——任何拿到链接的人都能加入。
  请撤销这些链接，或改用 [SSO](/zh/account/teams/sso)
</Warning>

<div id="remove-member">
  ### 移除成员
</div>

管理员可以随时通过上下文菜单 → “Remove” 移除成员。如果成员已使用过任何额度，其席位会在当前计费周期结束前保持占用。

<div id="change-role">
  ### 更改角色
</div>

管理员可以点击上下文菜单，然后使用 “Change role” 选项更改其他成员的角色。<br />

团队中始终至少需要一名管理员和一名付费成员。

<div id="security-sso">
  ## 安全与 SSO
</div>

SAML 2.0 单点登录（SSO）适用于 Team 计划。主要功能包括：

* 配置 SSO 连接（[了解更多](/zh/account/teams/sso)）
* 设置域名验证
* 自动为用户开通
* SSO 强制策略选项
* 身份提供商集成（如 Okta）

<Note>
  <p className="!mb-0">启用 SSO 前需要完成域名验证。</p>
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: `32px 64px`, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="usage-controls">
  ## 使用控制
</div>

打开“使用”设置以：

* 启用按用量计费
* 启用高级模型
* 仅允许管理员修改
* 设定每月支出上限
* 监控全队使用情况

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8149f830c27308af1bcc329c25e38b5" style={{ backgroundColor: "#0c0c0c" }} data-og-width="1668" width="1668" data-og-height="1160" height="1160" data-path="images/account/usage-based-pricing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc308a967251694ad7b03189c1083c61 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ddc293e19fa993e65be8c09ced649b4f 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a4df7d48d75c6166ab215550a641ca6 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f9051947c802ae54fd964196c50a3701 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ed775e3e98611ead1b938aedaf917f11 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b26f86bce94dc981d3cf71853a965374 2500w" />
</Frame>

<div id="billing">
  ## 计费
</div>

添加团队成员时：

* 每位成员或管理员都会占用一个可计费席位（参见[pricing](https://cursor.com/pricing)）
* 新成员会按当前计费周期剩余时长按比例计费
* 未付费管理员的席位不计入

在月中添加成员只按实际使用天数计费。移除已使用过额度的成员时，其席位会保留至本计费周期结束——不提供按比例退款。

角色变更（例如从 Admin 变更为 Unpaid Admin）会从变更当日起调整计费。可选择按月或按年计费。

按月/按年续订会在你最初注册的日期进行，与成员变更无关。

<div id="switch-to-yearly-billing">
  ### 切换为按年计费
</div>

从按月切换为按年可节省**20%**：

1. 前往[Dashboard](https://cursor.com/dashboard)
2. 在账户部分，点击“Advanced”，然后点击“Upgrade to yearly billing”

<Note>
  只能通过 dashboard 从按月切换为按年。若要从
  按年切换为按月，请联系 [hi@cursor.com](mailto:hi@cursor.com)。
</Note>



# SCIM
Source: https://docs.cursor.com/zh/account/teams/scim

设置 SCIM 供应以自动化管理用户和群组

<div id="overview">
  ## 概述
</div>

SCIM 2.0 预配可通过你的身份提供商自动管理团队成员和目录组。适用于启用 SSO 的 Enterprise 方案。

<product_visual type="screenshot">
  SCIM 设置面板，显示 Active Directory Management 配置
</product_visual>

<div id="prerequisites">
  ## 前提条件
</div>

* Cursor Enterprise 订阅
* 必须先完成 SSO 配置——**SCIM 需要处于活动状态的 SSO 连接**
* 拥有身份提供商（Okta、Azure AD 等）的管理员权限
* 拥有 Cursor 组织的管理员权限

<div id="how-it-works">
  ## 工作原理
</div>

<div id="user-provisioning">
  ### 用户供应
</div>

当用户在身份提供商中被分配到 SCIM 应用时，会自动添加到 Cursor；取消分配时会被移除。更改会实时同步。

<div id="directory-groups">
  ### 目录组
</div>

目录组及其成员关系会从身份提供商同步。组和用户的管理必须在身份提供商中进行，Cursor 仅以只读方式展示这些信息。

<div id="spend-management">
  ### 花费管理
</div>

可以为每个目录组设置不同的按用户花费上限。目录组的上限优先于团队级上限。属于多个组的用户将获得其中最高的适用上限。

<div id="setup">
  ## 设置
</div>

<Steps>
  <Step title="确保已配置 SSO">
    SCIM 需要先完成 SSO 设置。如果你还没配置 SSO，
    先按照 [SSO 设置指南](/zh/account/teams/sso) 操作再继续。
  </Step>

  <Step title="进入 Active Directory 管理">
    使用管理员账号前往
    [cursor.com/dashboard?tab=active-directory](https://www.cursor.com/dashboard?tab=active-directory)，
    或进入你的仪表盘设置并选择
    “Active Directory Management” 选项卡。
  </Step>

  <Step title="开始 SCIM 设置">
    完成 SSO 验证后，你会看到一个分步 SCIM 设置的链接。点击开始配置向导。
  </Step>

  <Step title="在身份提供商中配置 SCIM">
    在你的身份提供商中：- 创建或配置 SCIM 应用 - 使用 Cursor 提供的 SCIM 端点与令牌 - 启用用户与群组推送配置 - 测试连接
  </Step>

  <Step title="配置支出上限（可选）">
    返回 Cursor 的 Active Directory Management 页面：- 查看已同步的目录群组 - 按需为特定群组设置每用户支出上限 - 查看适用于属于多个群组用户的限额
  </Step>
</Steps>

<div id="identity-provider-setup">
  ### 身份提供商设置
</div>

不同提供商的设置指南：

<Card title="身份提供商指南" icon="book" href="https://workos.com/docs/integrations">
  Okta、Azure AD、Google Workspace 等的设置说明。
</Card>

<div id="managing-users-and-groups">
  ## 管理用户和群组
</div>

<Warning>
  所有用户和群组的管理都必须通过你的身份提供商完成。
  在身份提供商中所做的更改会自动同步到 Cursor，但
  你无法直接在 Cursor 中修改用户或群组。
</Warning>

<div id="user-management">
  ### 用户管理
</div>

* 在身份提供商中将用户分配到你的 SCIM 应用以添加用户
* 在身份提供商中将用户从 SCIM 应用取消分配以移除用户
* 用户资料变更（姓名、邮箱）会从身份提供商自动同步

<div id="group-management">
  ### 群组管理
</div>

* 目录群组会从身份提供商自动同步
* 群组成员变更会实时生效
* 使用群组来组织用户并设置不同的消费限额

<div id="spend-limits">
  ### 消费限额
</div>

* 为每个目录群组设置不同的单用户限额
* 用户会继承其所属群组中的最高消费限额
* 群组限额会覆盖默认的团队范围内的单用户限额

<div id="faq">
  ## 常见问题
</div>

<div id="why-isnt-scim-management-showing-up-in-my-dashboard">
  ### 为什么我的控制台里没有显示 SCIM 管理？
</div>

在设置 SCIM 之前，先确认 SSO 已正确配置并正常运行。SCIM 需要一个有效的 SSO 连接才能工作。

<div id="why-arent-users-syncing">
  ### 为什么用户没有同步？
</div>

确认用户已在你的身份提供商中被分配到 SCIM 应用。只有明确分配的用户才会在 Cursor 中显示。

<div id="why-arent-groups-appearing">
  ### 为什么群组没有出现？
</div>

检查你的身份提供商的 SCIM 设置里是否启用了群组推送配置。群组同步需要独立于用户同步单独配置。

<div id="why-arent-spend-limits-applying">
  ### 为什么支出上限没有生效？
</div>

确认用户在你的身份提供商中被正确分配到预期的群组。群组成员关系决定适用的支出上限。

<div id="can-i-manage-scim-users-and-groups-directly-in-cursor">
  ### 我能在 Cursor 里直接管理 SCIM 的用户和群组吗？
</div>

不能。所有用户和群组的管理都需要通过你的身份提供商完成。Cursor 仅以只读的方式展示这些信息。

<div id="how-quickly-do-changes-sync">
  ### 变更同步有多快？
</div>

你在身份提供商中的变更会实时同步到 Cursor。对于大规模的批量操作，可能会有短暂的延迟。



# 入门
Source: https://docs.cursor.com/zh/account/teams/setup

创建并设置 Cursor 团队

<div id="cursor-for-teams">
  ## Cursor 团队版
</div>

Cursor 适用于个人和团队。团队版为组织提供一整套工具：SSO、团队管理、访问控制和使用分析。

<div id="creating-a-team">
  ## 创建团队
</div>

按下面的步骤创建团队：

<Steps>
  <Step title="设置 Teams 订阅">
    要创建团队，请这样做：

    1. **新用户**：访问 [cursor.com/team/new-team](https://cursor.com/team/new-team) 创建新账号和团队
    2. **已有用户**：前往你的[控制台](/zh/account/dashboard)，点击“Upgrade to Teams”
  </Step>

  <Step title="填写团队信息">
    选择团队名称和计费周期

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3b9df20d032b544dcbc0343d9ddf056f" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/account/team/new-team.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b81f3241069a8a0fb9278b6a2e246057 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c26976bf06297d36ec9224ec1496a630 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fed5c7c95914ff47cfceae81f1441208 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc5986368419ef54f45803547741cfe 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4eb38a9618399ddadbf7596b185d2732 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c7d720a1e20d2aa23463a1b9001d545 2500w" />
    </Frame>
  </Step>

  <Step title="邀请成员">
    邀请团队成员。成员人数按比例计费——只为他们处于成员期间的时间付费。

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbd84dd96a7003415c2d2f038b1aaa77" style={{ paddingLeft: 16, paddingRight: 16, backgroundColor: '#0c0c0c' }} data-og-width="880" width="880" data-og-height="422" height="422" data-path="images/account/invite-members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=988e36ee874f704dfaae1b0a69ed2f84 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c0f85aacd3be59e11b1bfd05f9e5d6cd 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=411456e375f8c406ad2972965e0b549e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57ae04799be300a7e61464490344146f 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2faa0cf8ed56865c19916e33fde97900 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0bdb5040f44338e748246b4f1ddf2ddf 2500w" />
    </Frame>
  </Step>

  <Step title="启用 SSO（可选）">
    为了安全性与自动化入职，启用 [SSO](/zh/account/teams/sso)。

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
    </Frame>
  </Step>
</Steps>

<div id="faq">
  ## 常见问题
</div>

<AccordionGroup>
  <Accordion title="我的团队使用 Zscaler / 代理 / VPN，Cursor 能正常工作吗？">
    Cursor 默认使用 HTTP/2。某些代理和 VPN 会拦截该协议。

    在设置中启用 HTTP/1.1 回退，以改用 HTTP/1.1。
  </Accordion>

  <Accordion title="如何为公司购买授权？">
    Cursor 按活跃用户计费，而非按席位。你可以随时添加或移除用户——新成员会按剩余时间按比例计费。若移除的用户已使用过任意额度，其席位会一直占用到本计费周期结束。

    续订日期保持不变。
  </Accordion>

  <Accordion title="不使用 Cursor 的情况下，如何设置团队？">
    将自己设置为[未付费管理员](/zh/account/teams/members)，即可在无授权的情况下进行管理。

    <Warning>
      团队至少需要一名付费成员。你可以先完成设置、邀请成员，然后在扣费前更改你的角色。
    </Warning>
  </Accordion>

  <Accordion title="如何将 Cursor 加入公司的 MDM？">
    各平台的下载链接见 [cursor.com/downloads](https://cursor.com/downloads)。

    MDM 指南：

    * [Omnissa Workspace ONE](https://docs.omnissa.com/bundle/MobileApplicationManagementVSaaS/page/DeployInternalApplications.html)（原 VMware）
    * [Microsoft Intune（Windows）](https://learn.microsoft.com/en-us/mem/intune-service/apps/apps-win32-app-management)
    * [Microsoft Intune（Mac）](https://learn.microsoft.com/en-us/mem/intune-service/apps/lob-apps-macos-dmg)
    * [Kandji MDM](https://support.kandji.io/kb/custom-apps-overview)
  </Accordion>
</AccordionGroup>



# SSO
Source: https://docs.cursor.com/zh/account/teams/sso

为你的团队配置单点登录

<div id="overview">
  ## 概览
</div>

Business 方案包含 SAML 2.0 SSO，无需额外费用。用现有的身份提供商（IdP）为团队成员进行身份验证，无需单独创建 Cursor 账户。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## 前置条件
</div>

* Cursor Team 订阅
* 你在身份提供商（如 Okta）中的管理员权限
* 你在 Cursor 组织中的管理员权限

<div id="configuration-steps">
  ## 配置步骤
</div>

<Steps>
  <Step title="登录到你的 Cursor 账户">
    使用管理员账号前往 [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings)。
  </Step>

  <Step title="找到 SSO 配置">
    找到“Single Sign-On (SSO)”部分并展开。
  </Step>

  <Step title="开始设置流程">
    点击“SSO Provider Connection settings”按钮开始进行 SSO 设置，并按照向导操作。
  </Step>

  <Step title="配置你的身份提供商">
    在你的身份提供商（例如 Okta）中：

    * 创建新的 SAML 应用
    * 使用 Cursor 提供的信息配置 SAML 设置
    * 设置 Just-in-Time（JIT）即时预配
  </Step>

  <Step title="验证域名">
    在 Cursor 中点击“Domain verification settings”按钮验证你用户的域名。
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### 身份提供商设置指南
</div>

查看针对特定提供商的设置说明：

<Card title="身份提供商指南" icon="book" href="https://workos.com/docs/integrations">
  Okta、Azure AD、Google Workspace 等的设置说明。
</Card>

<div id="additional-settings">
  ## 其他设置
</div>

* 在管理控制台里管理 SSO 强制策略
* 新用户通过 SSO 登录时将自动加入
* 在你的身份提供商中进行用户管理

<div id="troubleshooting">
  ## 疑难解答
</div>

如果遇到问题：

* 确认你的域名已在 Cursor 中完成验证
* 确保已正确映射 SAML 属性
* 在管理员控制台检查是否已启用 SSO
* 确认身份提供商与 Cursor 中的名字和姓氏一致
* 查看上面的各提供商专属指南
* 如果问题仍未解决，联系 [hi@cursor.com](mailto:hi@cursor.com)



# 更新获取
Source: https://docs.cursor.com/zh/account/update-access

选择接收更新的频率

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

Cursor 有两个更新渠道。

<Tabs>
  <Tab title="Default">
    默认更新渠道，提供经过充分测试的版本。

    * 稳定版本
    * 预发布测试阶段的缺陷修复
    * 所有用户的默认选项
    * 团队用户的唯一选项

    <Note>
      团队和企业账号使用 Default 模式。
    </Note>
  </Tab>

  <Tab title="Early Access">
    含有新功能的预发布版本。

    <Warning>
      Early Access 构建可能存在缺陷或稳定性问题。
    </Warning>

    * 访问开发中的功能
    * 可能包含缺陷
    * 不适用于团队账号
  </Tab>
</Tabs>

<div id="change-update-channel">
  ## 更改更新渠道
</div>

1. **打开设置**：按 <Kbd>Cmd+Shift+J</Kbd>
2. **前往 Beta**：在侧边栏选择 Beta
3. **选择渠道**：选择 Default 或 Early Access

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=36c55c2deb93bc734b6ee0099a0d184c" data-og-width="1798" width="1798" data-og-height="442" height="442" data-path="images/account/early-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=624bfea7b3643f55afaa85b38b1c56e1 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f32c8e59596f024223735b4f929949e0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd8c4bf3265ab802b6188aa81a620244 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8600f42cc363c61377f158972187e01 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=32c83b2109587d299959c2d46ce67353 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b2c4032824d39c62a7cbada5578b1a98 2500w" />
</Frame>

在 [论坛](https://forum.cursor.com) 上报告 Early Access 问题。



# Apply
Source: https://docs.cursor.com/zh/agent/apply

了解如何使用 Apply 从聊天中应用、接受或拒绝代码建议

<div id="how-apply-works">
  ## Apply 的工作原理
</div>

Apply 是 Cursor 的一个专用模型，用于把聊天生成的代码集成进你的文件。它会处理聊天对话里的代码块，并把这些改动应用到你的代码库中。

Apply 本身不生成代码。代码由聊天模型生成，Apply 负责把它集成到现有文件。它可以处理跨多个文件和大型代码库的改动。

<div id="apply-code-blocks">
  ## 应用代码块
</div>

要采纳代码块中的建议，点击代码块右上角的播放按钮。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
</Frame>



# Checkpoints
Source: https://docs.cursor.com/zh/agent/chat/checkpoints

在 Agent 更改后保存并恢复先前状态

Checkpoints 会自动为 Agent 对你代码库的更改创建快照。需要时，你可以用它们撤销 Agent 的修改。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## 恢复检查点
</div>

有两种恢复方式：

1. **从输入框**：在之前的请求上点击 `Restore Checkpoint` 按钮
2. **从消息**：鼠标悬停在消息上时点击“+”按钮

<Warning>
  检查点不是版本控制。需要永久历史请用 Git。
</Warning>

<div id="how-they-work">
  ## 工作原理
</div>

* 本地存储，独立于 Git
* 仅跟踪 Agent 的变更（不包含手动编辑）
* 自动清理

<Note>
  手动编辑不会被跟踪。检查点只用于记录 Agent 的变更。
</Note>

<div id="faq">
  ## 常见问题
</div>

<AccordionGroup>
  <Accordion title="检查点会影响 Git 吗？">
    不会。它们独立于 Git 历史。
  </Accordion>

  {" "}

  <Accordion title="会保存多久？">
    仅在当前会话和近期历史中保存，并会自动清理。
  </Accordion>

  <Accordion title="可以手动创建吗？">
    不行。它们由 Cursor 自动创建。
  </Accordion>
</AccordionGroup>

{" "}



# Commands
Source: https://docs.cursor.com/zh/agent/chat/commands

为可复用的工作流定义命令

自定义命令让你创建可复用的工作流，并可在聊天输入框中通过简单的 `/` 前缀触发。这些命令有助于在团队内标准化流程并提升常见任务的效率。

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  命令目前处于 beta 阶段。随着我们持续改进，功能与语法可能会发生变化。
</Info>

<div id="how-commands-work">
  ## 命令的工作方式
</div>

命令是以纯 Markdown 文件的形式定义的，可以存放在两个位置：

1. **项目命令**：位于项目的 `.cursor/commands` 目录
2. **全局命令**：位于用户主目录的 `~/.cursor/commands` 目录

当你在聊天输入框中输入 `/` 时，Cursor 会自动检测并显示这两个目录中的可用命令，让它们在整个工作流程中随取随用。

<div id="creating-commands">
  ## 创建命令
</div>

1. 在项目根目录下创建一个 `.cursor/commands` 目录
2. 添加带有描述性名称的 `.md` 文件（例如 `review-code.md`、`write-tests.md`）
3. 用纯 Markdown 编写该命令应执行的说明
4. 当你输入 `/` 时，命令会自动出现在聊天中

下面是你的 commands 目录结构可能的样子：

```
.cursor/
└── commands/
    ├── 处理 GitHub PR 评论.md
    ├── 代码审查清单.md
    ├── 创建 PR.md
    ├── 轻量审阅现有改动.md
    ├── 新开发者入职.md
    ├── 运行全部测试并修复.md
    ├── 安全审计.md
    └── 新功能设置.md
```

<div id="examples">
  ## 示例
</div>

在项目里试试这些命令，感受一下它们是如何工作的。

<AccordionGroup>
  <Accordion title="代码评审清单">
    ```markdown  theme={null}
    # 代码评审清单

    ## 概览
    用于开展全面代码评审的完整清单，确保质量、安全性和可维护性。

    ## 评审类别

    ### 功能
    - [ ] 代码按预期工作
    - [ ] 已覆盖边界情况
    - [ ] 错误处理得当
    - [ ] 无明显缺陷或逻辑错误

    ### 代码质量
    - [ ] 代码可读、结构清晰
    - [ ] 函数小而专注
    - [ ] 变量命名清晰且具描述性
    - [ ] 无重复代码
    - [ ] 遵循项目约定

    ### 安全
    - [ ] 无明显安全漏洞
    - [ ] 具备输入验证
    - [ ] 正确处理敏感数据
    - [ ] 未硬编码敏感信息/密钥
    ```
  </Accordion>

  <Accordion title="安全审计">
    ```markdown  theme={null}
    # 安全审计

    ## 概览
    对代码库进行全面安全审查，识别并修复漏洞。

    ## 步骤
    1. **依赖审计**
       - 检查已知漏洞
       - 更新过时包
       - 审查第三方依赖

    2. **代码安全审查**
       - 检查常见漏洞
       - 审查认证/授权
       - 审计数据处理实践

    3. **基础设施安全**
       - 审查环境变量
       - 检查访问控制
       - 审计网络安全

    ## 安全清单
    - [ ] 依赖已更新且安全
    - [ ] 无硬编码机密
    - [ ] 已实施输入校验
    - [ ] 认证安全
    - [ ] 授权配置正确
    ```
  </Accordion>

  <Accordion title="设置新功能">
    ```markdown  theme={null}
    # 设置新特性

    ## 概览
    从前期规划到实现结构，系统化地搭建一个新特性。

    ## 步骤
    1. **定义需求**
       - 明确特性范围和目标
       - 梳理用户故事和验收标准
       - 制定技术方案

    2. **创建特性分支**
       - 从 main/develop 派生分支
       - 搭建本地开发环境
       - 配置新增依赖

    3. **规划架构**
       - 设计数据模型和 API
       - 规划 UI 组件与流程
       - 制定测试策略

    ## 特性设置清单
    - [ ] 需求已记录
    - [ ] 用户故事已编写
    - [ ] 技术方案已制定
    - [ ] 特性分支已创建
    - [ ] 开发环境已就绪
    ```
  </Accordion>

  <Accordion title="创建 pull request">
    ```markdown  theme={null}
    # 创建 PR

    ## 概览
    创建一个结构清晰的 pull request，包含完善的描述、标签和评审人。

    ## 步骤
    1. **准备分支**
       - 确保所有更改已提交
       - 将分支推送到远程仓库
       - 确认分支与 main 同步最新

    2. **撰写 PR 描述**
       - 清晰总结更改
       - 包含背景与动机
       - 列出任何破坏性变更
       - 如果涉及 UI 变更，附上截图

    3. **设置 PR**
       - 使用具描述性的标题创建 PR
       - 添加合适的标签
       - 指定评审人
       - 关联相关 issue

    ## PR 模板
    - [ ] 功能 A
    - [ ] Bug 修复 B
    - [ ] 单元测试通过
    - [ ] 手动测试完成
    ```
  </Accordion>

  <Accordion title="运行测试并修复失败">
    ```markdown  theme={null}
    # 运行全部测试并修复失败

    ## 概览
    执行完整测试套件，并系统化地修复任何失败，确保代码质量与功能正确性。

    ## 步骤
    1. **运行测试套件**
       - 运行项目中的所有测试
       - 捕获输出并定位失败
       - 同时检查单元测试和集成测试

    2. **分析失败**
       - 按类型分类：不稳定（flaky）、已损坏、新增失败
       - 按影响优先级进行修复
       - 检查是否与近期改动相关

    3. **系统化地修复问题**
       - 先从最关键的失败着手
       - 一次修复一个问题
       - 每次修复后重新运行测试
    ```
  </Accordion>

  <Accordion title="引导新开发者上手">
    ```markdown  theme={null}
    # 新开发者上手指南

    ## 概览
    完整的入职流程，帮新开发者快速上手并开始工作。

    ## 步骤
    1. **环境搭建**
       - 安装必需工具
       - 搭建开发环境
       - 配置 IDE 与扩展
       - 配置 Git 和 SSH 密钥

    2. **项目熟悉**
       - 查看项目结构
       - 理解架构
       - 阅读关键文档
       - 配置本地数据库

    ## 入职清单
    - [ ] 开发环境就绪
    - [ ] 所有测试通过
    - [ ] 能在本地运行应用
    - [ ] 数据库已配置且可用
    - [ ] 已提交首个 PR
    ```
  </Accordion>
</AccordionGroup>



# 紧凑
Source: https://docs.cursor.com/zh/agent/chat/compact

通过紧凑模式界面在聊天中节省空间

紧凑模式通过减少视觉干扰并最大化对话区域，为你提供更精简的聊天界面。

<div id="overview">
  ## 概览
</div>

启用后，紧凑模式会这样优化聊天界面：

* **隐藏图标**，让界面更干净、极简
* **自动折叠差异视图（diff）**，减少视觉干扰
* **自动折叠输入框**，最大化对话空间

这个设置在用小屏设备，或者想要更专注、无干扰的聊天体验时特别好用。

<div id="before-and-after">
  ## 前后对比
</div>

<div id="default-mode">
  ### 默认模式
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e0f8b97ecd5201be396fcd09cec54de6" alt="默认模式的聊天界面，显示所有图标与展开的元素" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/off.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9395c8d1f324033631508dc9cdfd6f3e 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d8025ef65ad2fc9fe8c30e5c4fcda32 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=28050b27b683af948bc1ed939f31786c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dc443705188da9d3368acefd917cc890 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=be6603e2cedb7e88e7c20d797b18599c 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3afe563c9cd4576623adce5dcaaccddf 2500w" />
</Frame>

<div id="compact-mode">
  ### 紧凑模式
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e9f068889026827422b2a9d943b55ded" alt="紧凑模式的聊天界面，隐藏图标并折叠元素" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/on.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44e86a79eb893b4de6c57c65487bbe9a 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=539b71c72ed2fb3508e3aec0624429c1 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2c0da715a5daf93e94dbf2a5eefbb7eb 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b5bddca39109779c9d91bb6bc8bb42e9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bb334bb055e49d4d51cd137d2396db0 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=70730d151a24440eeb6dc31e18189c7d 2500w" />
</Frame>

<div id="enabling-compact-mode">
  ## 启用紧凑模式
</div>

要启用紧凑模式：

1. 打开 Cursor 设置
2. 前往 **Chat** 设置
3. 打开 **Compact Mode**

界面会立即切换到精简视图，让你有更多空间专注对话。



# 复制
Source: https://docs.cursor.com/zh/agent/chat/duplicate

从对话的任意节点创建分支

复制或分叉聊天，在不丢失当前对话的前提下探索替代解决方案。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/duplicate-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29fdb23214ba3e2c5b94ccefc01f7615" autoPlay loop muted playsInline controls data-path="images/chat/duplicate-chat.mp4" />
</Frame>

<div id="how-to-duplicate">
  ## 如何复制
</div>

1. 找到你想要分叉的位置
2. 点击消息上的省略号
3. 选择“Duplicate Chat”

<div id="what-happens">
  ## 会发生什么
</div>

* 之前的上下文会被保留
* 原始对话不会被更改
* 两个聊天各自有独立的历史记录



# 导出
Source: https://docs.cursor.com/zh/agent/chat/export

将聊天导出为 Markdown 格式

将 Agent 聊天导出为 Markdown 文件，便于分享或撰写文档。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
</Frame>

<div id="whats-exported">
  ## 导出内容
</div>

* 所有消息与回复
* 语法高亮的代码块
* 文件引用与上下文
* 按时间顺序排列的对话流

<div id="how-to-export">
  ## 如何导出
</div>

1. 打开想要导出的聊天
2. 点击更多菜单 → “导出聊天”
3. 将文件保存到本地

<Warning>
  导出前请检查是否包含敏感信息：API 密钥、内部 URL、专有代码、
  个人信息
</Warning>



# 历史记录
Source: https://docs.cursor.com/zh/agent/chat/history

查看并管理聊天会话

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

在历史面板里查看以往的 Agent 对话。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Chat History" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
</Frame>

<div id="opening-history">
  ## 打开历史
</div>

* 点击 Agent 侧边栏中的历史图标
* 按下 <Kbd tooltip="Open chat history">Opt Cmd '</Kbd>

<div id="managing-chats">
  ## 管理聊天
</div>

* **编辑标题**：点击即可重命名
* **删除**：移除不需要的聊天
* **打开**：点击查看完整对话

聊天历史会以 SQLite 数据库存储在本机。

<Note>
  想保留聊天的话，把它们[导出](/zh/agent/chats/export)为 Markdown。
</Note>

<div id="background-agents">
  ## 后台代理
</div>

后台代理的聊天不会出现在常规历史中，而是会存储在远程数据库里。按下 <Kbd tooltip="Open background agent control panel">Cmd E</Kbd> 查看。

<div id="referencing-past-chats">
  ## 引用历史聊天
</div>

在当前聊天中使用 [@Past Chats](/zh/context/@-symbols/@-past-chats) 把之前对话的上下文带进来。



# 摘要
Source: https://docs.cursor.com/zh/agent/chat/summarization

管理聊天中的长对话上下文

<div id="message-summarization">
  ## 消息总结
</div>

随着对话拉长，Cursor 会自动总结并管理上下文，帮你保持聊天高效。了解如何使用上下文菜单，以及文件如何被压缩以适配模型的上下文窗口。

<div id="using-the-summarize-command">
  ### 使用 /summarize 命令
</div>

你可以在聊天中手动输入 `/summarize` 命令来触发摘要。当对话变得过长时，这个命令能帮助管理上下文，让你在不丢失重要信息的情况下高效继续工作。

<Info>
  想更深入了解 Cursor 中上下文的工作原理？查看我们的 [Working with
  Context](/zh/guides/working-with-context) 指南。
</Info>

<div id="how-summarization-works">
  ### 摘要机制如何运作
</div>

当对话变长时，它会超过模型的上下文窗口上限：

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">上下文窗口上限</div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

为了解决这个问题，Cursor 会把较早的消息压缩成摘要，为新的对话腾出空间。

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">
          上下文窗口上限
        </div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-neutral-100 px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">
          摘要消息
        </div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

<div id="file-folder-condensation">
  ## 文件与文件夹压缩呈现
</div>

虽然聊天摘要可以处理长对话，但在管理大型文件和文件夹时，Cursor 采取了不同的策略：**智能压缩**。当你在对话中包含文件时，Cursor 会根据文件大小和可用的上下文空间来决定最佳的呈现方式。

文件/文件夹可能处于以下几种状态：

<div id="condensed">
  ### 摘要视图
</div>

当文件或文件夹过大，超出上下文窗口容量时，Cursor 会自动将其摘要化。摘要会向模型提供关键的结构信息，例如函数签名、类和方法。基于这个摘要视图，模型可以在需要时选择展开特定文件。这样可以最大化地高效利用可用的上下文窗口。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0c3a07b6fef6402945138f7ee38b44c1" alt="Context menu" data-og-width="1226" width="1226" data-og-height="793" height="793" data-path="images/context/context-management/condensed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4cc08626f9cfce1d186cdd6aa96c7d09 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fa49ce9605bdb0186c98712f4c0a32cc 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=84874b2f40bff0a2cd54796865469914 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=050290a85c154e92f9298883afcdf892 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f953aa28f11926b2d6fdf734cf928402 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=50aa9973ccf2027814860f3d97a2b031 2500w" />
</Frame>

<div id="significantly-condensed">
  ### 大幅精简
</div>

当文件名标注为“大幅精简”时，说明该文件过大，即便精简后也无法完整包含。模型只能看到文件名。

<div id="not-included">
  ### 未包含
</div>

当文件或文件夹旁出现警告图标时，表示该项过大，即使经过压缩也无法纳入上下文窗口。这样有助于你了解代码库中哪些部分对模型可访问。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=06df9854c74c257d1ceb7d18b1864ceb" alt="Context menu" data-og-width="1090" width="1090" data-og-height="346" height="346" data-path="images/context/context-management/not-included.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=072e75878f27a151f1310007d0e5e534 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6f3f71351ddf8e367096651b455bf9d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c407f7870412007549f8eb2871f9ca12 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b0d17023b5734c8d7584c56f5419bd1a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f1bedff398cee6c957fe62877f7d2012 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8b00fbaff658c384f69bfddf3f3a4cfe 2500w" />
</Frame>



# 标签页
Source: https://docs.cursor.com/zh/agent/chat/tabs

同时运行多个 Agent 对话

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

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
</Frame>

<div id="overview">
  ## 概览
</div>

按 <Kbd>Cmd+T</Kbd> 新建标签页。每个标签页都有独立的对话历史、上下文和模型选择。

<Tip>
  想并行处理任务，试试 [Background Agents](/zh/background-agents)
</Tip>

<div id="managing-tabs">
  ## 管理标签页
</div>

* 使用 <Kbd>Cmd+T</Kbd> 新建标签页。每个标签页都会从全新的对话开始，并维护自己的上下文。

* 通过点击标签页标题，或使用 <Kbd>Ctrl+Tab</Kbd> 在标签页之间切换。

* 标签页标题会在第一条消息后自动生成，你也可以右键点击标签页标题进行重命名。

<Tip>
  一页一事，开头把需求说明清楚，完成后及时关闭标签页，保持工作区干净有序。
</Tip>

<div id="conflicts">
  ### 冲突
</div>

Cursor 会防止多个标签页同时编辑同一文件，并提示你解决冲突。

<div id="reference-other-chats">
  ## 引用其他聊天
</div>

使用 [@Past Chats](/zh/context/@-symbols/@-past-chats) 把其他标签页或之前会话的上下文带进来。



# 模式
Source: https://docs.cursor.com/zh/agent/modes

为任务选择合适的模式——从自主编码到精准编辑

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

Agent 提供多种针对特定任务优化的模式。每种模式启用的能力和工具各不相同，以满足你的工作流需求。

<div className="full-width-table">
  | 模式                    | 适用场景     | 能力          | 工具     |
  | :-------------------- | :------- | :---------- | :----- |
  | **[Agent](#agent)**   | 复杂功能、重构  | 自主探索、跨文件编辑  | 启用全部工具 |
  | **[Ask](#ask)**       | 学习、规划、提问 | 只读探索，不会自动更改 | 仅搜索工具  |
  | **[Custom](#custom)** | 专业化工作流   | 用户自定义能力     | 可配置    |
</div>

<div id="agent">
  ## Agent
</div>

处理复杂编码任务的默认模式。Agent 会自主探索你的代码库、编辑多个文件、运行命令并修复错误，来完成你的请求。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
</Frame>

<div id="ask">
  ## Ask
</div>

用于学习和探索的只读模式。Ask 会在你的代码库中搜索并给出答案，且不会进行任何更改——非常适合在修改前先理解代码。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=15e531cb84f0a18228723870fd84fa4f" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/ask.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=592ac5a681910a075ae88dec89bee25d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74b98cce3b5bb83c79d0566cd3c65c34 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4d80f50e20e7ca28db5a3ee71718979 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a4a6e017fd64149cf68d997114bbf6b6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7354479ecd644b86ddbcb9fe1131f100 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=274125e614eadd17522e0dacfcc6a38e 2500w" />
</Frame>

<div id="custom">
  ## 自定义
</div>

用特定的工具组合和指令创建你自己的模式。按需混搭能力，贴合你的工作流。

<Note>
  自定义模式目前为测试版。可在 `Cursor Settings` → `Chat` → `Custom
      Modes` 中启用
</Note>

<div id="examples">
  ### 示例
</div>

<AccordionGroup>
  <Accordion title="Learn">
    **Tools:** All Search\
    **Instructions:** 重点把概念讲清楚，并主动提出澄清性问题
  </Accordion>

  {" "}

  <Accordion title="Refactor">
    **Tools:** Edit & Reapply **Instructions:** 优化代码结构，不新增任何功能
  </Accordion>

  {" "}

  <Accordion title="Plan">
    **Tools:** Codebase, Read file, Terminal **Instructions:** 在 `plan.md` 中制定详细的实现计划
  </Accordion>

  <Accordion title="Debug">
    **Tools:** All Search, Terminal, Edit & Reapply\
    **Instructions:** 在提出修复方案前先充分排查问题
  </Accordion>
</AccordionGroup>

<div id="switching-modes">
  ## 切换模式
</div>

* 在 Agent 中使用模式选择器下拉菜单
* 按 <Kbd>Cmd+.</Kbd> 快速切换
* 在[设置](#settings)中自定义键盘快捷键

<div id="settings">
  ## 设置
</div>

所有模式都有通用的配置项：

<div className="full-width-table">
  | 设置    | 描述            |
  | :---- | :------------ |
  | 模型    | 选择要使用的 AI 模型  |
  | 键盘快捷键 | 设置在各模式间切换的快捷键 |
</div>

特定模式的设置：

<div className="full-width-table">
  | 模式         | 设置        | 描述                                  |
  | :--------- | :-------- | :---------------------------------- |
  | **Agent**  | 自动运行与自动修错 | 自动执行命令并修复错误                         |
  | **Ask**    | 搜索代码库     | 自动查找相关文件                            |
  | **Custom** | 工具选择与指令   | 配置 [tools](/zh/agent/tools) 和自定义提示词 |
</div>



# 概览
Source: https://docs.cursor.com/zh/agent/overview

面向自主编码任务、终端命令与代码编辑的助手

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

Agent 是 Cursor 的助手，能独立完成复杂的编码任务、运行终端命令并编辑代码。可在侧边栏按 <Kbd>Cmd+I</Kbd> 打开。

<Frame caption="侧边栏中的 Agent">
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b17d6a1225b4992ea19978b6a6c259e1" autoPlay loop muted playsInline data-path="images/chat/overview.mp4" />
</Frame>

<div className="mt-24 flex flex-col gap-12">
  <Columns className="gap-4">
    <div>
      <h2 className="text-lg font-medium mb-2">
        <a href="/zh/agent/modes" className="hover:text-primary transition-colors">
          模式
        </a>
      </h2>

      <p className="text-sm">
        选择 Agent、Ask，或创建自定义模式。每种模式都提供
        不同的功能和工具，贴合你的工作流程。
      </p>
    </div>

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" alt="Agent 模式" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
    </Frame>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh/agent/tools" className="hover:text-primary transition-colors">
          工具
        </a>
      </h3>

      <p className="text-sm">
        Agent 通过工具来搜索、编辑并运行命令。从语义代码库搜索到终端执行，这些工具让任务能够自动完成。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Agent tools" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh/agent/apply" className="hover:text-primary transition-colors">
          应用更改
        </a>
      </h3>

      <p className="text-sm">
        把 AI 推荐的代码块集成进你的代码库。Apply 在保证精确的同时，能高效处理大规模改动。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" alt="应用更改" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh/agent/review" className="hover:text-primary transition-colors">
          审查差异
        </a>
      </h3>

      <p className="text-sm">
        在接受更改前先仔细查看。Review 界面用不同颜色标注的行显示新增和删除，帮你精确掌控修改。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh/agent/chats/tabs" className="hover:text-primary transition-colors">
          聊天标签页
        </a>
      </h3>

      <p className="text-sm">
        使用 <Kbd>Cmd+T</Kbd> 同时开启多条对话。每个标签页
        都维护各自的上下文、历史记录和模型选择。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh/agent/chats/checkpoints" className="hover:text-primary transition-colors">
          检查点
        </a>
      </h3>

      <p className="text-sm">
        系统会自动生成快照来追踪 Agent 的更改。若更改不符合预期，或想尝试不同思路，可以恢复到之前的状态。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh/agent/terminal" className="hover:text-primary transition-colors">
          终端集成
        </a>
      </h3>

      <p className="text-sm">
        Agent 可执行终端命令、监控输出并处理多步流程。你可以为可信工作流配置自动运行，或为安全起见启用确认。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="终端集成" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh/agent/chats/history" className="hover:text-primary transition-colors">
          聊天记录
        </a>
      </h3>

      <p className="text-sm">
        按下 <Kbd>Opt Cmd '</Kbd> 查看过往对话。回顾之前的讨论、跟踪编码会话，并便捷引用更早聊天中的上下文。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Chat history" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh/agent/chats/export" className="hover:text-primary transition-colors">
          导出聊天
        </a>
      </h3>

      <p className="text-sm">
        将对话导出为 Markdown 格式。把解决方案分享给团队成员、记录决策，或基于编码会话创建知识库。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/zh/context/rules" className="hover:text-primary transition-colors">
          规则
        </a>
      </h3>

      <p className="text-sm">
        为 Agent 的行为定义自定义指令。规则有助于维护编码标准、落实约定，并让 Agent 的协作方式更贴合你的项目。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Agent 规则" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
      </Frame>
    </div>
  </Columns>
</div>



# 规划
Source: https://docs.cursor.com/zh/agent/planning

Agent 如何通过待办事项与队列来规划并管理复杂任务

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

Agent 可以通过结构化的待办列表和消息队列进行前瞻性规划并管理复杂任务，让长周期任务更容易理解与跟踪。

<div id="agent-to-dos">
  ## Agent 待办
</div>

Agent 会把较长的任务拆分成带有依赖关系的可管理步骤，生成一个会随进度更新的结构化计划。

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### 工作原理
</div>

* Agent 会自动为复杂任务生成待办列表
* 每个条目都可以设置对其他任务的依赖
* 随着进度推进，列表会实时更新
* 已完成的任务会自动勾选

<div id="visibility">
  ### 可见性
</div>

* 待办会显示在聊天界面里
* 如果已设置 [Slack 集成](/zh/slack)，待办也会在那边显示
* 随时都能查看完整的任务拆解

<Tip>
  想要更好地规划，清晰描述你的最终目标。当 Agent 理解了完整范围时，会生成更准确的任务拆解。
</Tip>

<Note>自动模式目前不支持规划和待办。</Note>

<div id="queued-messages">
  ## 排队消息
</div>

在 Agent 处理当前任务时，把后续消息先排到队列里。你的指令会依次等待，并在就绪后自动执行。

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

<div id="using-the-queue">
  ### 使用队列
</div>

1. 当 Agent 正在工作时，输入你的下一条指令
2. 按 <Kbd>Ctrl+Enter</Kbd> 添加到队列
3. 消息会按顺序显示在当前任务下方
4. 点击箭头可调整已排队消息的顺序
5. Agent 完成后会按序处理它们

<div id="override-the-queue">
  ### 覆盖队列
</div>

想把消息加入队列而不是按默认方式发送，按 <Kbd>Ctrl+Enter</Kbd>。想跳过排队、立刻发送，按 <Kbd>Cmd+Enter</Kbd>。这会“强制推送”消息，绕过队列立即执行。

<div id="default-messaging">
  ## 默认消息
</div>

默认情况下，消息会尽可能快地发送，通常会在 Agent 完成一次工具调用后立刻出现。这样能带来最敏捷的体验。

<div id="how-default-messaging-works">
  ### 默认消息的工作方式
</div>

* 你的消息会被追加到聊天中最近的一条用户消息后
* 消息通常会附着在工具结果上，并在就绪后立即发送
* 这能在不打断 Agent 当前工作的情况下，让对话更自然地衔接
* 默认情况下，当 Agent 正在工作时，你按下 Enter 就会触发这一行为



# 差异与评审
Source: https://docs.cursor.com/zh/agent/review

评审并管理由 AI Agent 生成的代码更改

当 Agent 生成代码更改时，会在评审界面中展示：新增与删除以不同颜色标注的行显示。这样你就能检查并控制要应用到代码库的更改。

评审界面以熟悉的 diff 格式展示代码更改：

<div id="diffs">
  ## 差异
</div>

<div className="full-width-table">
  | 类型       | 含义        | 示例                                                                                                    |
  | :------- | :-------- | :---------------------------------------------------------------------------------------------------- |
  | **新增行**  | 新增的代码     | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **删除行**  | 删除的代码     | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **上下文行** | 未更改的上下文代码 | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## 审阅
</div>

生成完成后，你会看到一个提示，先审阅所有更改再继续。这样你可以先总览即将被修改的内容。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="输入审阅界面" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### 按文件
</div>

屏幕底部会出现一个悬浮审阅栏，你可以：

* 对当前文件的更改**接受**或**拒绝**
* 跳转到有待更改的**下一个文件**
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      你的浏览器不支持 video 标签。
    </video>
  </Frame>

<div id="selective-acceptance">
  ### 选择性接受
</div>

需要更细粒度的控制时：

* 想接受大部分更改：先拒绝不需要的行，然后点击**全部接受**
* 想拒绝大部分更改：先接受需要的行，然后点击**全部拒绝**

<div id="review-changes">
  ## 查看更改
</div>

在 agent 的回复末尾，点击 **Review changes** 按钮以查看完整的差异对比。

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>



# Terminal
Source: https://docs.cursor.com/zh/agent/terminal

将终端命令作为代理操作的一部分自动运行

Agent 会在 Cursor 的原生终端中执行命令，并保留命令历史。点击“跳过”以发送 <kbd>Ctrl+C</kbd> 并中断命令。

<div id="troubleshooting">
  ## 故障排除
</div>

<Info>
  某些 shell 主题（比如 Powerlevel9k/Powerlevel10k）可能会干扰
  内联终端的输出。如果你的命令输出出现截断或
  格式错乱，Agent 运行时请禁用该主题，或切换到更简洁的提示符。
</Info>

<div id="disable-heavy-prompts-for-agent-sessions">
  ### 在 Agent 会话中禁用重量级提示符
</div>

在你的 shell 配置中使用 `CURSOR_AGENT` 环境变量来检测
Agent 是否正在运行，并跳过初始化花哨的提示符/主题。

```zsh  theme={null}

# ~/.zshrc — 当 Cursor Agent 运行时禁用 Powerlevel10k
if [[ -n "$CURSOR_AGENT" ]]; then
  # 为提升兼容性，跳过主题初始化
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash  theme={null}

# ~/.bashrc — 在 Agent 会话中使用简洁提示符作为回退
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```



# 工具
Source: https://docs.cursor.com/zh/agent/tools

Agent 可用于搜索、编辑和运行代码的工具

[Agent](/zh/agent/overview) 中各个模式可用的全部工具列表。构建自己的[自定义模式](/zh/agent/modes#custom)时，你可以选择启用或禁用这些工具。

<Note>
  在执行任务时，Agent 的工具调用次数没有上限。Agent 会按需持续使用工具来完成你的请求。
</Note>

<div id="search">
  ## 搜索
</div>

用于在你的代码库和网页中查找相关信息的工具。

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    读取单个文件的最多 250 行（在最大模式下可达 750 行）。
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    在不读取文件内容的情况下查看目录结构。
  </Accordion>

  <Accordion title="Codebase" icon="database">
    在你的[已索引代码库](/zh/context/codebase-indexing)中执行语义搜索。
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    在文件中搜索精确的关键词或模式。
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    通过模糊匹配按名称查找文件。
  </Accordion>

  <Accordion title="Web" icon="globe">
    生成搜索查询并进行网页搜索。
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    按类型和描述检索特定[规则](/zh/context/rules)。
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## 编辑
</div>

用于对你的文件和代码库进行特定修改的工具。

<AccordionGroup>
  <Accordion title="编辑并重新应用" icon="pencil">
    给文件提出修改建议，并自动[应用](/zh/agent/apply)这些更改。
  </Accordion>

  <Accordion title="删除文件" icon="trash">
    自动删除文件（可在设置中关闭）。
  </Accordion>
</AccordionGroup>

<div id="run">
  ## 运行
</div>

Chat 可以和你的终端交互。

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    执行终端命令并查看输出。
  </Accordion>
</AccordionGroup>

<Note>默认情况下，Cursor 使用第一个可用的终端配置文件。</Note>

设置你偏好的终端配置文件：

1. 打开 Command Palette（`Cmd/Ctrl+Shift+P`）
2. 搜索 “Terminal: Select Default Profile”
3. 选择你想要的配置文件

<div id="mcp">
  ## MCP
</div>

Chat 可以使用已配置的 MCP 服务器与外部服务交互，比如数据库或第三方 API。

<AccordionGroup>
  <Accordion title="切换 MCP 服务器" icon="server">
    切换可用的 MCP 服务器。遵循自动运行设置。
  </Accordion>
</AccordionGroup>

进一步了解 [Model Context Protocol](/zh/context/model-context-protocol)，并在 [MCP 目录](/zh/tools) 中探索可用服务器。

<div id="advanced-options">
  ## 高级选项
</div>

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    自动应用修改，无需手动确认。
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    自动执行终端命令并接受修改。适合运行测试套件和验证变更。

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    配置允许列表，指定哪些工具可以自动执行。通过明确定义允许的操作来提升安全性。
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    当 Agent 遇到时，自动修复 linter 的错误和警告。
  </Accordion>
</AccordionGroup>



# 后台智能体
Source: https://docs.cursor.com/zh/background-agent

Cursor 中的异步远程智能体

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

借助后台代理，可在远程环境中启动异步代理来编辑和运行代码。随时查看它们的状态、发送后续指令，或随时接管。

<div id="how-to-use">
  ## 使用方法
</div>

你可以通过两种方式访问后台代理：

1. **后台代理侧边栏**：在原生 Cursor 侧边栏中使用“后台代理”标签页，查看与你账号关联的所有后台代理、搜索现有代理，并新建代理。
2. **后台代理模式**：按下 <Kbd tooltip="Trigger background agent mode">Cmd E</Kbd>，在 UI 中触发后台代理模式。

提交提示词后，从列表中选择你的代理以查看状态并进入该机器。

<Note>
  <p className="!mb-0">
    后台代理需要保留数据数天。
  </p>
</Note>

<div id="setup">
  ## 设置
</div>

后台代理默认在隔离的 Ubuntu 基础环境中运行。代理可联网并安装软件包。

<div id="github-connection">
  #### 连接 GitHub
</div>

后台智能体会从 GitHub 克隆你的仓库，在单独的分支上工作，并推送到你的仓库，方便交接。

请为你的仓库（以及任何依赖的仓库或子模块）授予读写权限。我们未来也会支持其他提供商（GitLab、Bitbucket 等）。

<div id="ip-allow-list-configuration">
  ##### IP 允许列表配置
</div>

如果你的组织启用了 GitHub 的 IP 允许列表功能，需要为后台代理配置访问权限。完整的设置步骤（包含联系方式和 IP 地址）请查看 [GitHub 集成文档](/zh/integrations/github#ip-allow-list-configuration)。

<div id="base-environment-setup">
  #### 基础环境设置
</div>

在更高级的场景中，自己配置环境。先获取一个连接远程机器的 IDE 实例。配置你的机器、安装工具和包，然后创建快照。接着配置运行时设置：

* Install 命令会在代理启动前运行，用于安装运行时依赖，比如执行 `npm install` 或 `bazel build`。
* Terminals 会在代理工作期间运行后台进程——例如启动 Web 服务器或编译 protobuf 文件。

在最复杂的场景下，用 Dockerfile 来进行机器配置。Dockerfile 允许你设置系统级依赖：安装特定版本的编译器、调试器，或切换基础 OS 镜像。不要 `COPY` 整个项目——我们会管理工作区并检出正确的提交。依赖安装仍然放在 install 脚本中处理。

输入开发环境所需的任意密钥（secrets）——它们会以静态加密（使用 KMS）的方式存储在我们的数据库中，并在后台代理的环境中提供。

机器配置保存在 `.cursor/environment.json` 中，可以提交到你的仓库（推荐）或私下存储。设置流程会引导你创建 `environment.json`。

<div id="maintenance-commands">
  #### 维护命令
</div>

在设置新机器时，我们从基础环境开始，然后运行你在 `environment.json` 中的 `install` 命令。这个命令等同于开发者在切换分支时会运行的操作——用于安装新增依赖。

对大多数人来说，`install` 命令是 `npm install` 或 `bazel build`。

为确保机器能快速启动，我们会在 `install` 命令运行完成后缓存磁盘状态。把它设计成可重复运行。只有由 `install` 命令产生的磁盘状态会被保留——在这里启动的进程在代理启动时不会继续存在。

<div id="startup-commands">
  #### 启动命令
</div>

运行 `install` 之后，机器会启动，我们会先运行 `start` 命令，再启动所有 `terminals`。这会拉起在代理运行期间需要常驻的进程。

`start` 命令通常可以省略。如果你的开发环境依赖 Docker，可以在 `start` 命令里加上 `sudo service docker start`。

`terminals` 用于应用代码。这些终端会在一个你和代理都能访问的 `tmux` 会话中运行。比如，很多网站仓库会把 `npm run watch` 配成一个 terminal。

<div id="the-environmentjson-spec">
  #### `environment.json` 规范
</div>

`environment.json` 文件可能如下：

```json  theme={null}
{
  "snapshot": "POPULATED_FROM_SETTINGS",
  "install": "npm install",
  "terminals": [
    {
      "name": "运行 Next.js",
      "command": "npm run dev"
    }
  ]
}
```

严格来说，规范[定义在这里](https://www.cursor.com/schemas/environment.schema.json)。

<div id="models">
  ## 模型
</div>

只有与 [Max Mode](/zh/context/max-mode) 兼容的模型才能用于后台代理。

<div id="pricing">
  ## 定价
</div>

进一步了解 [Background Agent 的定价](/zh/account/pricing#background-agent)。

<div id="security">
  ## 安全性
</div>

Background Agents 可在隐私模式下使用。我们绝不会用你的代码进行训练，只会在运行 agent 时临时保留代码。[了解更多隐私模式](https://www.cursor.com/privacy-overview)。

你需要知道：

1. 为你想编辑的仓库授予我们 GitHub 应用的读写权限。我们会用它来克隆仓库并进行更改。
2. 你的代码会在我们基于 AWS 的隔离 VM 中运行，并在 agent 可用期间存储在 VM 磁盘上。
3. agent 可以访问互联网。
4. agent 会自动执行所有终端命令，方便它循环运行测试。这和前台 agent 不同，前台每条命令都需要用户批准。自动执行会带来数据外泄风险：攻击者可能通过提示注入攻击，诱使 agent 将代码上传到恶意网站。参见 [OpenAI 关于后台 agent 提示注入风险的说明](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access)。
5. 如果关闭隐私模式，我们会收集提示词和开发环境信息，用于改进产品。
6. 如果在启动后台 agent 时禁用隐私模式，且在其运行过程中再启用，agent 会在完成前一直以禁用的隐私模式继续运行。

<div id="dashboard-settings">
  ## 仪表板设置
</div>

Workspace 管理员可以在仪表板的 Background Agents 选项卡中配置更多设置。

<div id="defaults-settings">
  ### 默认设置
</div>

* **默认模型** – 运行未指定模型时使用的模型。选择任一支持 Max Mode 的模型。
* **默认仓库** – 留空时，agent 会让你选择仓库。在这里填上仓库就能跳过这一步。
* **基础分支** – agent 在创建拉取请求时进行 fork 的源分支。留空则使用仓库的默认分支。

<div id="security-settings">
  ### 安全设置
</div>

所有安全选项都需要管理员权限。

* **用户限制** – 选择 *None*（所有成员都可以启动后台 agent）或 *Allow list*。当设置为 *Allow list* 时，你需要明确指定哪些队友可以创建 agent。
* **团队跟进** – 开启后，工作区内的任何人都可以给他人启动的 agent 添加跟进消息。关闭后，跟进仅限该 agent 的所有者和管理员。
* **显示 agent 摘要** – 控制 Cursor 是否显示该 agent 的文件差异图和代码片段。如果不想在侧边栏暴露文件路径或代码，就把它关掉。
* **在外部渠道显示 agent 摘要** – 将上一个开关扩展到 Slack 或你已连接的任何外部渠道。

更改会即时保存，并立即作用于新创建的 agent。



# 添加后续操作
Source: https://docs.cursor.com/zh/background-agent/api/add-followup

en/background-agent/api/openapi.yaml post /v0/agents/{id}/followup
向正在运行的后台代理发送额外指令。




# 代理会话
Source: https://docs.cursor.com/zh/background-agent/api/agent-conversation

en/background-agent/api/openapi.yaml get /v0/agents/{id}/conversation
获取后台代理的会话历史。

如果该后台代理已被删除，则无法访问其会话。



# 代理状态
Source: https://docs.cursor.com/zh/background-agent/api/agent-status

en/background-agent/api/openapi.yaml get /v0/agents/{id}
获取指定后台代理的当前状态与结果。




# API 密钥信息
Source: https://docs.cursor.com/zh/background-agent/api/api-key-info

en/background-agent/api/openapi.yaml get /v0/me
获取用于认证的 API 密钥的元数据。




# 删除 Agent
Source: https://docs.cursor.com/zh/background-agent/api/delete-agent

en/background-agent/api/openapi.yaml delete /v0/agents/{id}
永久删除后台代理及其关联资源。




# 启动 Agent
Source: https://docs.cursor.com/zh/background-agent/api/launch-an-agent

en/background-agent/api/openapi.yaml post /v0/agents
启动新的后台 Agent，为你的代码仓库工作。




# 列出代理
Source: https://docs.cursor.com/zh/background-agent/api/list-agents

en/background-agent/api/openapi.yaml get /v0/agents
为已认证用户获取其所有后台代理的分页列表。




# 列出模型
Source: https://docs.cursor.com/zh/background-agent/api/list-models

en/background-agent/api/openapi.yaml get /v0/models
获取后台代理的推荐模型列表。

如果你想在创建时指定后台代理使用的模型，可以用这个端点查看推荐的模型列表。

同时也推荐提供一个“Auto”选项。选择该选项时，你无需向创建端点提供模型名称，
我们会自动选择最合适的模型。



# 列出 GitHub 仓库
Source: https://docs.cursor.com/zh/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
获取已认证用户可访问的 GitHub 仓库列表。

<Warning>
  **此端点的速率限制非常严格。**

  将请求限制为**每位用户每分钟 1 次**，以及**每位用户每小时 30 次**。

  对于能访问许多仓库的用户，请求可能需要几十秒才能返回。

  请确保在该信息暂不可用时进行友好处理。
</Warning>



# 概览
Source: https://docs.cursor.com/zh/background-agent/api/overview

通过编程方式创建并管理在你仓库中运行的后台代理

<div id="background-agents-api">
  # Background Agents API
</div>

<Badge variant="beta">Beta</Badge>

Background Agents API 让你可以以编程方式创建和管理在你仓库中自主运行的 AI 驱动编码代理。
你可以用这个 API 自动回应用户反馈、修复 bug、更新文档，等等！

<Info>
  Background Agents API 目前处于 beta，期待你的反馈！
</Info>

<div id="key-features">
  ## 关键功能
</div>

* **自主代码生成** - 创建能理解你的提示并对代码库进行修改的代理
* **仓库集成** - 可直接对接 GitHub 仓库
* 后续提示 - 为正在运行的代理追加指令
* **按用量计费** - 只为你使用的 token 付费
* **可扩展** - 每个 API key 最多支持 256 个活跃代理

<div id="quick-start">
  ## 快速上手
</div>

<div id="1-get-your-api-key">
  ### 1. 获取 API 密钥
</div>

**前往** [Cursor Dashboard → Integrations](https://cursor.com/dashboard?tab=integrations) 创建你的 API 密钥。

<div id="2-start-using-the-api">
  ### 2. 开始使用 API
</div>

所有 API 端点都基于以下相对路径：

```
https://api.cursor.com
```

查看 [API 参考](/zh/background-agent/api/launch-an-agent) 以获取端点的详细列表。

<div id="authentication">
  ## 身份验证
</div>

所有 API 请求都需要使用 Bearer 令牌进行身份验证：

```
Authorization: Bearer YOUR_API_KEY
```

API 密钥可在 [Cursor Dashboard](https://cursor.com/dashboard?tab=integrations) 创建。密钥以你的账户为作用域，并授予创建和管理智能体的权限（受你的套餐限制和代码仓库访问权限约束）。

<div id="pricing">
  ## 定价
</div>

API 目前处于测试阶段，价格与 Background Agents 相同。随着服务扩容，价格可能会调整。查看 [Background Agent 价格](/zh/account/pricing#background-agent)。

<div id="next-steps">
  ## 接下来
</div>

* 阅读主要的 [Background Agents 概览](/zh/background-agent)，了解环境、权限和工作流。
* 通过 [Web 与移动端](/zh/background-agent/web-and-mobile) 试用 Background Agents。
* 加入 [Discord #background-agent](https://discord.gg/jfgpZtYpmb) 频道讨论，或发送邮件至 [background-agent-feedback@cursor.com](mailto:background-agent-feedback@cursor.com)。



# Webhooks
Source: https://docs.cursor.com/zh/background-agent/api/webhooks

实时接收后台代理状态变更通知

<div id="webhooks">
  # Webhooks
</div>

当你创建带有 webhook URL 的 agent 时，Cursor 会通过 HTTP POST 请求通知你状态变更。目前仅支持 `statusChange` 事件，具体在 agent 进入 `ERROR` 或 `FINISHED` 状态时触发。

<div id="webhook-verification">
  ## Webhook 验证
</div>

为了确保 webhook 请求确实来自 Cursor，需要验证每个请求所带的签名：

<div id="headers">
  ### 请求头
</div>

每个 webhook 请求都会包含以下请求头：

* **`X-Webhook-Signature`** – 以 `sha256=<hex_digest>` 格式携带 HMAC-SHA256 签名
* **`X-Webhook-ID`** – 本次投递的唯一标识（便于日志记录）
* **`X-Webhook-Event`** – 事件类型（目前仅支持 `statusChange`）
* **`User-Agent`** – 固定为 `Cursor-Agent-Webhook/1.0`

<div id="signature-verification">
  ### 签名验证
</div>

要验证 webhook 签名，先计算期望的签名，再与接收到的签名进行比对：

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
  const expectedSignature = 'sha256=' +
    crypto.createHmac('sha256', secret)
          .update(rawBody)
          .digest('hex');
  
  return signature === expectedSignature;
}
```

```python  theme={null}
import hmac
import hashlib

def verify_webhook(secret, raw_body, signature):
    expected_signature = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return signature == expected_signature
```

计算签名时，一定要使用原始请求体（在任何解析之前）。

<div id="payload-format">
  ## 载荷格式
</div>

Webhook 载荷以 JSON 形式发送，结构如下：

```json  theme={null}
{
  "event": "状态更改",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "已完成",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "添加了包含安装说明的 README.md"
}
```

请注意：部分字段为可选，仅在有数据时才会包含。

<div id="best-practices">
  ## 最佳实践
</div>

* **验证签名** – 始终校验 webhook 签名，确保请求来自 Cursor
* **处理重试** – 如果你的端点返回错误状态码，webhook 可能会被重试
* **快速返回** – 尽快返回 2xx 状态码
* **使用 HTTPS** – 在生产环境中始终为 webhook 端点使用 HTTPS URL
* **存储原始载荷** – 保存原始 webhook 载荷，以便调试和后续验签



# Web 与移动端
Source: https://docs.cursor.com/zh/background-agent/web-and-mobile

在任意设备上运行代码代理，且可无缝切换到桌面端

<div id="overview">
  ## 概览
</div>

Cursor 的 Web 版 Agent 将强大的编码助手带到每一台设备。无论是散步时用手机，还是在浏览器中工作，现在都能启动在后台运行的强大编码代理。
完成后，可在 Cursor 中接续它们的工作、审查并合并更改，或与团队共享链接进行协作。

前往 [cursor.com/agents](https://cursor.com/agents) 开始使用。

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=79c7d14df82cfcae369bccb8a1431cf3" alt="Cursor Web 版 Agent 界面" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=099c28633151e6c20eebc7fe03b3d420 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=452e0216c7e270d760072032f1e2b36d 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=baaa4a73d4822b5daa293814dc201d37 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8c5255fbf16aa60924e78a8285afb95d 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=7cc5a04ff6b24ad4ce0cfb4a35a9919c 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=f5f1b15fa508e20f89a4089f81417774 2500w" /></Frame>

<div id="getting-started">
  ## 入门
</div>

<div id="quick-setup">
  ### 快速设置
</div>

1. **访问网页版**：在任意设备上打开 [cursor.com/agents](https://cursor.com/agents)
2. **登录**：使用你的 Cursor 账号登录
3. **连接 GitHub**：关联你的 GitHub 账号以访问仓库
4. **启动第一个 Agent**：输入一个任务，看看 Agent 如何开始工作

<div id="mobile-installation">
  ### 移动端安装
</div>

为了获得更好的移动端体验，把 Cursor 安装为渐进式 Web 应用（PWA）：

* **iOS**：在 Safari 中打开 [cursor.com/agents](https://cursor.com/agents)，点分享按钮，然后选择“添加到主屏幕”
* **Android**：在 Chrome 中打开该链接，点菜单，然后选择“添加到主屏幕”或“安装应用”

<Tip>
  以 PWA 方式安装可带来接近原生的体验，包括：- 全屏界面 - 更快的启动 - 主屏幕上的应用图标
</Tip>

<div id="working-across-devices">
  ## 跨设备协同
</div>

Web 和 Mobile Agent 专为配合你的桌面端工作流而设计；点击“Open in Cursor”，即可在 IDE 中继续代理的工作。

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=352140fd4bf3f3d98a1e1b9f4a995cad" alt="Review and handoff" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=eedd50318503fd3d3961b6da27a386d9 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fd8c730cf62a0af6f873945a6a23b90b 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ac537cc639471556f1afa0e09425ef30 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d512cddda6890c0749a7ad6396682def 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e208297f414976bcfeea6850b39e8abb 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=54683ff7f25750fdc788e87c30bb6d6d 2500w" /></Frame>

<div id="team-collaboration">
  ### 团队协作
</div>

* **共享访问**：把链接分享给团队成员，共同协作运行代理。
* **评审流程**：协作者可以查看代码差异并给出反馈。
* **Pull Request 管理**：直接在网页端创建、评审并合并 Pull Request。

<div id="slack-integration">
  ### Slack 集成
</div>

在 Slack 中 @`Cursor` 直接触发代理；从 Web 或移动端启动代理时，还可以选择在完成后接收 Slack 通知。

<Card title="在 Slack 中使用 Cursor" icon="slack" href="/zh/slack">
  了解如何设置并使用 Slack 集成功能，包括
  触发代理和接收通知。
</Card>

<div id="pricing">
  ## 定价
</div>

Web 和移动端代理与 Background Agents 采用相同的计费模式。

想了解更多[Background Agent 的计费](/zh/account/pricing#background-agent)。

<div id="troubleshooting">
  ## 疑难解答
</div>

<AccordionGroup>
  <Accordion title="代理运行未启动">
    * 确保你已登录并已连接 GitHub 账号。
    * 检查你是否具备所需的仓库权限。
    * 你还需要处于 Pro 试用或付费计划，并启用按用量计费。要启用按用量计费，请前往
      [Dashboard](https://www.cursor.com/dashboard?tab=settings) 的设置页。
  </Accordion>

  <Accordion title="在移动端看不到代理运行">
    试着刷新页面或清除浏览器缓存。确保你在各设备上使用的是同一账号。
  </Accordion>

  <Accordion title="Slack 集成不可用">
    确认你的工作区管理员已安装 Cursor Slack 应用，并且你拥有相应的权限。
  </Accordion>
</AccordionGroup>



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



# 代码评审
Source: https://docs.cursor.com/zh/cli/cookbook/code-review

构建一个使用 Cursor CLI 的 GitHub Actions 工作流程，自动评审 pull request 并提供反馈

本教程演示如何在 GitHub Actions 中使用 Cursor CLI 设置代码评审。该工作流程会分析 pull request、定位问题，并以评论形式发布反馈。

<Tip>
  对于大多数用户，推荐直接使用 [Bugbot](/zh/bugbot)。Bugbot 提供托管的自动化代码评审，无需任何配置。CLI 方案适合用来探索能力和进行高级自定义。
</Tip>

<div className="space-y-4">
  <Expandable title="完整的工作流文件">
    ```yaml cursor-code-review.yml theme={null}
    name: 代码评审

    on:
      pull_request:
        types: [opened, synchronize, reopened, ready_for_review]

    permissions:
      pull-requests: write
      contents: read
      issues: write

    jobs:
      code-review:
        runs-on: ubuntu-latest
        # 对草稿 PR 跳过自动代码评审
        if: github.event.pull_request.draft == false
        steps:
          - name: 检出仓库
            uses: actions/checkout@v4
            with:
              fetch-depth: 0
              ref: ${{ github.event.pull_request.head.sha }}

          - name: 安装 Cursor CLI
            run: |
              curl https://cursor.com/install -fsS | bash
              echo "$HOME/.cursor/bin" >> $GITHUB_PATH

          - name: 配置 git 身份
            run: |
              git config user.name "Cursor Agent"
              git config user.email "cursoragent@cursor.com"

          - name: 执行自动代码评审
            env:
              CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
              MODEL: gpt-5
              GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
              BLOCKING_REVIEW: ${{ vars.BLOCKING_REVIEW || 'false' }}
            run: |
              cursor-agent --force --model "$MODEL" --output-format=text --print '你正在 GitHub Actions 运行器中执行自动代码评审。gh CLI 可用并已通过 GH_TOKEN 认证。你可以在拉取请求上发表评论。

              上下文：
              - 仓库：${{ github.repository }}
              - PR 编号：${{ github.event.pull_request.number }}
              - PR Head SHA：${{ github.event.pull_request.head.sha }}
              - PR Base SHA：${{ github.event.pull_request.base.sha }}
              - 阻塞评审：${{ env.BLOCKING_REVIEW }}

              目标：
              1) 复查已有评审评论，对已处理的标记为 resolved。
              2) 审查当前 PR diff，只标记明确且高严重度的问题。
              3) 仅在变更行留下非常简短的行内评论（1-2 句），并在末尾附上简要总结。

              流程：
              - 获取现有评论：gh pr view --json comments
              - 获取 diff：gh pr diff
              - 获取带补丁的变更文件以计算行内位置：gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/files --paginate --jq '.[] | {filename,patch}'
              - 为每个问题计算精确的行内锚点（文件路径 + diff 位置）。评论必须放在 diff 的变更行内，而不是作为顶层评论。
              - 检测由该机器人撰写的此前顶层“无问题”类评论（匹配正文如："✅ no issues"、"No issues found"、"LGTM"）。
              - 如果本次运行发现问题，且存在此前“无问题”评论：
                - 优先移除它们以避免混淆：
                  - 尝试通过以下方式删除顶层评论：gh api -X DELETE repos/${{ github.repository }}/issues/comments/<comment_id>
                  - 若无法删除，通过 GraphQL（minimizeComment）最小化，或编辑为添加前缀"[已被新发现取代]"。
                - 若既不能删除也不能最小化，则回复该评论："⚠️ 已被取代：在较新的提交中发现了问题"
              - 若此前报告的问题看起来已被附近的变更修复，回复：✅ 此问题似乎已被近期变更解决
              - 仅分析以下内容：
                - null/undefined 解引用
                - 资源泄漏（未关闭的文件或连接）
                - 注入（SQL/XSS）
                - 并发/竞态条件
                - 对关键操作缺少错误处理
                - 明显的逻辑错误导致不正确行为
                - 明确的性能反模式且具有可衡量影响
                - 明确的安全漏洞
              - 避免重复：如果相似反馈已在相同或相邻行存在则跳过。

              评论规则：
              - 最多 10 条行内评论；优先最关键问题
              - 一条评论只包含一个问题；放在精确的变更行上
              - 所有问题评论必须是行内的（锚定到 PR diff 中的文件与行/位置）
              - 语气自然、具体且可执行；不要提及“自动化”或“高置信度”
              - 使用表情：🚨 严重 🔒 安全 ⚡ 性能 ⚠️ 逻辑 ✅ 已解决 ✨ 改进

              提交：
              - 如果没有可报告的问题，且已存在指示“无问题”的顶层评论（例如："✅ no issues"、"No issues found"、"LGTM"），不要再提交新评论。跳过提交以避免冗余。
              - 如果没有可报告的问题，且不存在此前“无问题”评论，提交一条简短摘要评论说明无问题。
              - 如果存在可报告的问题，且此前存在“无问题”评论，确保在提交新的评审前删除/最小化/标记为已被取代该评论。
              - 若存在可报告问题，提交一份评审，仅包含行内评论以及可选的精炼摘要正文。使用 GitHub Reviews API 以确保评论为行内：
                - 构建如下的评论 JSON 数组：[{ "path": "<file>", "position": <diff_position>, "body": "..." }]
                - 通过以下方式提交：gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/reviews -f event=COMMENT -f body="$SUMMARY" -f comments='[$COMMENTS_JSON]'
              - 不要使用：gh pr review --approve 或 --request-changes

              阻塞策略：
              - 如果 BLOCKING_REVIEW 为 true 且发布了任何 🚨 或 🔒 问题：echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
              - 否则：echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
              - 最后务必设置 CRITICAL_ISSUES_FOUND
              '

          - name: 检查阻塞评审结果
            if: env.BLOCKING_REVIEW == 'true'
            run: |
              echo "正在检查严重问题..."
              echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

              if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
                echo "❌ 发现严重问题，且启用了阻塞评审。工作流失败。"
                exit 1
              else
                echo "✅ 未发现阻塞性问题。"
              fi
    ```
  </Expandable>

  <Frame>
    <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=31c7e4b54276532df8010645686ebbbc" alt="自动化代码审查演示：在拉取请求中显示行内评论" data-og-width="2920" width="2920" data-og-height="1272" height="1272" data-path="images/cli/cookbook/code-review/comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=25e552210fa8425a10ff459bf4cd6006 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=234bf271bc595e763549c4f04d2e6fbb 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=b6f6d1444de7fe0197e3d35fa35955e8 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=300314314f5071b77f735460be33985f 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=10e4db857ee84c55d17222cef492611d 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=e65add70ffebfeb9ad05c9bb19a5f4e1 2500w" />
  </Frame>
</div>

<div id="configure-authentication">
  ## 配置身份验证
</div>

[设置你的 API 密钥和仓库密钥](/zh/cli/github-actions#authentication)，以在 GitHub Actions 中对 Cursor CLI 进行身份验证。

<div id="set-up-agent-permissions">
  ## 配置代理权限
</div>

创建一个配置文件来限制代理可执行的操作，避免发生像推送代码或创建 Pull Request 这样的意外操作。

在仓库根目录创建 `.cursor/cli.json`：

```json  theme={null}
{
  "permissions": {
    "deny": [
      "Shell(git push)",
      "Shell(gh pr create)",
      "Write(**)"
    ]
  }
}
```

此配置允许 agent 读取文件并使用 GitHub CLI 发表评论，但会阻止它修改你的仓库。查看[权限参考](/zh/cli/reference/permissions)以了解更多配置选项。

<div id="build-the-github-actions-workflow">
  ## 构建 GitHub Actions 工作流
</div>

现在我们来一步一步搭建这个工作流。

<div id="set-up-the-workflow-trigger">
  ### 设置工作流触发器
</div>

创建 `.github/workflows/cursor-code-review.yml`，并将其配置为在 pull request 上运行：

```yaml  theme={null}
name: Cursor 代码评审

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

jobs:
  code-review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    
    steps:
```

<div id="checkout-the-repository">
  ### 检出仓库
</div>

添加检出步骤以获取 pull request 的代码：

```yaml  theme={null}
- name: 检出仓库
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    ref: ${{ github.event.pull_request.head.sha }}
```

<div id="install-cursor-cli">
  ### 安装 Cursor CLI
</div>

添加 CLI 的安装步骤：

```yaml  theme={null}
- name: 安装 Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH
```

<div id="configure-the-review-agent">
  ### 配置审查代理
</div>

在实现完整的审查步骤之前，先弄清我们的审查提示词是怎么构成的。本节会说明我们希望代理的行为方式：

**目标**：
我们希望代理审查当前 PR 的 diff，只标注明确且高严重度的问题；仅在变更的行上留下非常简短的行内评论（1-2 句），并在末尾附上一段简要总结。这样可以保持良好的信噪比。

**格式**：
评论要简短且直击要点。我们会用表情符号便于快速扫描，并在末尾给出一次高层级的完整审查总结。

**提交**：
审查完成后，代理需要根据审查结果附上一段简短评论。代理应提交一次包含行内评论和精炼总结的单次审查。

**边界情况**：
需要处理：

* 既有评论已被解决：当问题已修复时，代理应将其标记为已完成
* 避免重复：如果同类反馈已存在于相同或相邻行，代理应跳过评论

**最终提示词**：
完整的提示词将上述行为要求组合起来，产出聚焦且可执行的反馈

现在让我们实现审查代理步骤：

```yaml  theme={null}
- name: 执行代码审查
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
    GH_TOKEN: ${{ github.token }}
  run: |
    cursor-agent --force --model "$MODEL" --output-format=text --print "你当前在 GitHub Actions runner 中执行自动化代码审查。gh CLI 可用并已通过 GH_TOKEN 认证。你可以在拉取请求上发表评论。
    
    上下文：
    - 仓库：${{ github.repository }}
    - PR 编号：${{ github.event.pull_request.number }}
    - PR Head SHA：${{ github.event.pull_request.head.sha }}
    - PR Base SHA：${{ github.event.pull_request.base.sha }}
    
    目标：
    1) 复核已有审查评论，若已处理则回复：已解决
    2) 审查当前 PR diff，仅标注明确且高严重度的问题
    3) 只在变更的行留下非常简短的行内评论（1-2 句），并在末尾给出简要总结
    
    流程：
    - 获取已有评论：gh pr view --json comments
    - 获取 diff：gh pr diff
    - 若先前报告的问题似乎已被附近的更改修复，回复：✅ 此问题似乎已被最近的更改解决
    - 避免重复：如果同类反馈已在相同行或附近存在，则跳过
    
    评论规则：
    - 最多 10 条行内评论；优先处理最关键的问题
    - 每条评论只包含一个问题；放在准确的变更行
    - 语气自然，具体且可执行；不要提及自动化或高置信度
    - 使用表情：🚨 严重 🔒 安全 ⚡ 性能 ⚠️ 逻辑 ✅ 已解决 ✨ 改进
    
    提交：
    - 提交一次审查，包含行内评论与简明总结
    - 仅使用：gh pr review --comment
    - 不要使用：gh pr review --approve 或 --request-changes"
```

```text  theme={null}
.
├── .cursor/
│   └── cli.json
├── .github/
│   └── workflows/
│       └── cursor-code-review.yml
```

<div id="test-your-reviewer">
  ## 测试你的审阅器
</div>

创建一个测试 Pull Request，确认工作流正常运行，并且代理会发布带有表情反馈的审阅评论。

<Frame>
  <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=aa989eb5b7520e6718a48afd8daa70d9" alt="Pull Request 显示自动审阅评论，包含表情符号以及针对特定代码行的内联反馈" data-og-width="1250" width="1250" data-og-height="704" height="704" data-path="images/cli/cookbook/code-review/github-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=9f2e324beb1cccb8052dcd0682323e47 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f08497ddb17921f4bb4638ef4eec3379 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=3c869c0ed8eb8b5743dd3821e57cd406 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=19e98ed953f4cc17b2c578ce543cf88d 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=4d9f47472af81254bd09b5f6234fc97f 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f3af19e3edd7f8bbbb77ba6566d8e183 2500w" />
</Frame>

<div id="next-steps">
  ## 后续步骤
</div>

现在你已经有了一个可用的自动化代码审查系统。可以考虑进一步优化：

* 为[修复 CI 失败](/zh/cli/cookbook/fix-ci)设置额外的工作流
* 为不同分支配置不同的审查等级
* 与团队现有的代码审查流程集成
* 针对不同的文件类型或目录自定义 agent 的行为

<Expandable title="高级：阻塞式审查">
  你可以配置在发现关键问题时让工作流失败，在问题被处理之前阻止合并该 pull request。

  **为提示添加阻塞行为**

  首先，更新你的审查 agent 步骤以包含 `BLOCKING_REVIEW` 环境变量，并把这种阻塞行为加入提示：

  ```
  Blocking behavior:
  - If BLOCKING_REVIEW is true and any 🚨 or 🔒 issues were posted: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
  - Otherwise: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
  - Always set CRITICAL_ISSUES_FOUND at the end
  ```

  **添加阻塞检查步骤**

  然后在代码审查步骤之后添加这个新步骤：

  ```yaml  theme={null}
        - name: Check blocking review results
          if: env.BLOCKING_REVIEW == 'true'
          run: |
            echo "Checking for critical issues..."
            echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

            if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
              echo "❌ Critical issues found and blocking review is enabled. Failing the workflow."
              exit 1
            else
              echo "✅ No blocking issues found."
            fi
  ```
</Expandable>



# 修复 CI 失败
Source: https://docs.cursor.com/zh/cli/cookbook/fix-ci

在 GitHub Actions 中使用 Cursor CLI 为仓库修复 CI 问题

在 GitHub Actions 中使用 Cursor CLI 修复 CI 失败。该工作流会分析失败、进行有针对性的修复，并创建一个修复分支和一个可快速创建 PR 的链接。

该工作流会按名称监控指定的工作流。把 `workflows` 列表更新为你实际的 CI 工作流名称。

<CodeGroup>
  ```yaml auto-fix-ci.yml theme={null}
  name: Fix CI Failures

  on:
    workflow_run:
      workflows: [Test]
      types: [completed]

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    attempt-fix:
      if: >-
        ${{ github.event.workflow_run.conclusion == 'failure' && github.event.workflow_run.name != 'Fix CI Failures' }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Fix CI failure
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: ci-fix
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - Workflow Run ID: ${{ github.event.workflow_run.id }}
            - Workflow Run URL: ${{ github.event.workflow_run.html_url }}
            - Fix Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Implement an end-to-end CI fix flow driven by the failing PR, creating a separate persistent fix branch and proposing a quick-create PR back into the original PR's branch.

            # Requirements:
            1) Identify the PR associated with the failed workflow run and determine its base and head branches. Let HEAD_REF be the PR's head branch (the contributor/origin branch).
            2) Maintain a persistent fix branch for this PR head using the Fix Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            3) Attempt to resolve the CI failure by making minimal, targeted edits consistent with the repo's style. Keep changes scoped and safe.
            4) You do NOT have permission to create PRs. Instead, post or update a single natural-language PR comment (1–2 sentences) that briefly explains the CI fix and includes an inline compare link to quick-create a PR.

            # Inputs and conventions:
            - Use `gh api`, `gh run view`, `gh pr view`, `gh pr diff`, `gh pr list`, `gh run download`, and git commands as needed to discover the failing PR and branches.
            - Avoid duplicate comments; if a previous bot comment exists, update it instead of posting a new one.
            - If no actionable fix is possible, make no changes and post no comment.

            # Deliverables when updates occur:
            - Pushed commits to the persistent fix branch for this PR head.
            - A single natural-language PR comment on the original PR that includes the inline compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Secret Audit
Source: https://docs.cursor.com/zh/cli/cookbook/secret-audit

使用 Cursor CLI 在 GitHub Actions 中审计仓库敏感信息

用 Cursor CLI 审计你的仓库，发现安全漏洞与敏感信息泄露。这个工作流会扫描潜在敏感信息、检测高风险的工作流模式，并给出安全加固建议。

<CodeGroup>
  ```yaml auto-secret-audit.yml theme={null}
  name: Secrets Audit

  on:
    schedule:
      - cron: "0 4 * * *"
    workflow_dispatch:

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    secrets-audit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Scan and propose hardening
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: audit
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
             - Hardening Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Perform a repository secrets exposure and workflow hardening audit on a schedule, and propose minimal safe fixes.

            # Requirements:
            1) Scan for potential secrets in tracked files and recent history; support allowlist patterns if present (e.g., .gitleaks.toml).
            2) Detect risky workflow patterns: unpinned actions, overbroad permissions, unsafe pull_request_target usage, secrets in forked PR contexts, deprecated insecure commands, missing permissions blocks.
            3) Maintain a persistent branch for this run using the Hardening Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            4) Propose minimal edits: redact literals where safe, add ignore rules, pin actions to SHA, reduce permissions, add guardrails to workflows, and add a SECURITY_LOG.md summarizing changes and remediation guidance.
            5) Push to origin.
            6) If there is at least one open PR in the repo, post or update a single natural-language comment (1–2 sentences) on the most recently updated open PR that briefly explains the hardening changes and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update an existing bot comment if present. If no changes or no open PRs, post nothing.

            # Inputs and conventions:
            - Use `gh` to list PRs and to post comments. Avoid duplicate comments.

            # Deliverables when updates occur:
             - Pushed commits to the persistent hardening branch for this run.
            - A single natural-language PR comment with the compare link above (only if an open PR exists).
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# 翻译键
Source: https://docs.cursor.com/zh/cli/cookbook/translate-keys

使用 Cursor CLI 在 GitHub Actions 中为仓库翻译键

使用 Cursor CLI 管理国际化的翻译键。该工作流会在 Pull Request 中检测新增或变更的 i18n 键，并仅补全缺失的翻译，绝不覆盖现有内容。

<CodeGroup>
  ```yaml auto-translate-keys.yml theme={null}
  name: Translate Keys

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    i18n:
      if: ${{ !startsWith(github.head_ref, 'translate/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Propose i18n updates
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: translate
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Head Ref: ${{ github.head_ref }}
            - Translate Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Detect i18n keys added or changed in the PR and fill only missing locales in message files. Never overwrite existing translations.

            # Requirements:
            1) Determine changed keys by inspecting the PR diff (source files and messages files).
            2) Compute missing keys per locale using the source/canonical locale as truth.
            3) Add entries only for missing keys. Preserve all existing values untouched.
            4) Validate JSON formatting and schemas.
            5) Maintain a persistent translate branch for this PR head using the Translate Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            6) Post or update a single PR comment on the original PR written in natural language (1–2 sentences) that briefly explains what was updated and why, and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update a previous bot comment if present.
            8) If no changes are necessary, make no commits and post no comment.

            # Inputs and conventions:
            - Use `gh pr diff` and git history to detect changes.

            # Deliverables when updates occur:
            - Pushed commits to the persistent translate branch for this PR head.
            - A single natural-language PR comment on the original PR with the compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# 更新文档
Source: https://docs.cursor.com/zh/cli/cookbook/update-docs

使用 Cursor CLI 在 GitHub Actions 中为仓库更新文档

在 GitHub Actions 中使用 Cursor CLI 更新文档。提供两种方案：完全由代理自主执行，或采用确定性工作流，仅允许代理修改文件。

<CodeGroup>
  ```yaml auto-update-docs.yml theme={null}
  name: 更新文档

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: 检出仓库
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: 安装 Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: 配置 git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: 更新文档
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "你正在 GitHub Actions 运行器中操作。

            GitHub CLI 可通过 `gh` 使用，并已使用 `GH_TOKEN` 完成认证。Git 可用。你对仓库内容有写入权限，也可以在拉取请求上发表评论，但不得创建或编辑 PR。

            # 上下文：
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}
            - Docs Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # 目标：
            - 基于原始 PR 的增量变更，实施端到端的文档更新流程。

            # 要求：
            1) 确定原始 PR 中的变更内容；如有多次推送，自上次文档成功更新以来计算增量差异。
            2) 仅根据这些增量变更更新相关文档。
            3) 使用上下文中的文档分支前缀，为该 PR 的 head 维护一个持久化的文档分支；若不存在则创建，存在则更新，并将变更推送至 origin。
            4) 你无权创建 PR。请改为发布或更新一条自然语言 PR 评论（1–2 句），简要说明本次文档更新，并包含一个内联对比链接以便快速创建 PR。

            # 输入与约定：
            - 使用 `gh pr diff` 与 git 历史记录检测变更，并据此推导自上次文档更新以来的增量范围。
            - 不要尝试直接创建或编辑 PR。请使用上述对比链接格式。
            - 将变更保持最小且符合仓库风格。若无需更新文档，则不要做任何变更，也不要发布评论。

            # 更新发生时的交付物：
            - 将提交推送到该 PR head 的持久化文档分支。
            - 在原始 PR 上发布一条自然语言评论，包含上述内联对比链接。避免重复发布；如已有先前的机器人评论，请更新它。
            " --force --model "$MODEL" --output-format=text
  ```

  ```yaml auto-update-docs-deterministic.yml theme={null}
  name: 更新文档

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: 检出仓库
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: 安装 Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: 配置 git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: 生成文档更新（不进行提交/推送/评论）
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "你正在 GitHub Actions 的 runner 中运行。

            GitHub CLI（命令为 `gh`）已可用，并通过 `GH_TOKEN` 完成鉴权。Git 也已可用。

            重要：不要创建分支、不要提交、不要推送、不要在 PR 中发表评论。只在需要时修改工作目录中的文件。后续的工作流步骤会负责发布更改并在 PR 上评论。

            # 上下文：
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}

            # 目标：
            - 基于此 PR 引入的增量更改更新仓库文档。

            # 要求：
            1) 确定原始 PR 中的变更内容（按需使用 `gh pr diff` 和 git 历史）。如果存在持久化的文档分支 `${{ env.BRANCH_PREFIX }}/${{ github.head_ref }}`，可将其作为只读参考点以理解之前的更新。
            2) 仅依据这些更改更新相关文档。保持改动最小，并与仓库风格一致。
            3) 不要提交、推送、创建分支或发表 PR 评论。仅保留已更新文件在工作树中；后续步骤会负责发布。

            # 输入与约定：
            - 使用 `gh pr diff` 和 git 历史来检测变更，并据此聚焦文档编辑。
            - 如不需要文档更新，则不要做任何更改，也不要产生任何输出。

            # 有更新时的交付物：
            - 仅在工作目录中的已修改文档文件（不提交/不推送/不评论）。
            " --force --model "$MODEL" --output-format=text

        - name: 发布文档分支
          id: publish_docs
          env:
            BRANCH_PREFIX: docs
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |
            echo "changes_published=false" >> "$GITHUB_OUTPUT"

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"

            # 确保当前位于可推送的本地分支上
            git fetch origin --prune

            # 创建/切换到持久化文档分支，同时保留当前工作树的更改
            git checkout -B "$DOCS_BRANCH"

            # 暂存并检测更改
            git add -A
            if git diff --staged --quiet; then
              echo "没有可发布的文档更改。跳过提交/推送。"
              exit 0
            fi

            COMMIT_MSG="docs: update for PR #${PR_NUMBER} (${HEAD_REF} @ $(git rev-parse --short HEAD))"
            git commit -m "$COMMIT_MSG"
            git push --set-upstream origin "$DOCS_BRANCH"

            echo "changes_published=true" >> "$GITHUB_OUTPUT"

        - name: 发布或更新 PR 评论
          if: steps.publish_docs.outputs.changes_published == 'true'
          env:
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
            REPO: ${{ github.repository }}
            BASE_REF: ${{ github.base_ref }}
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"
            COMPARE_URL="https://github.com/${REPO}/compare/${BASE_REF}...${DOCS_BRANCH}?quick_pull=1&title=docs%3A+updates+for+PR+%23${PR_NUMBER}"

            COMMENT_FILE="${RUNNER_TEMP}/auto-docs-comment.md"
            {
              echo "Cursor 已更新文档分支：\`${DOCS_BRANCH}\`"
              echo "现在可以[查看 diff 并快速创建一个 PR 来合并这些文档更新](${COMPARE_URL})。"
              echo
              echo "_随着 PR 的变动，后续运行会更新此评论。_"
              echo
              echo "<!-- auto-update-docs-split -->"
            } > "$COMMENT_FILE"

            # 如果编辑最后一条机器人评论失败（较旧版本的 gh），则回退为创建新评论
            if gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE" --edit-last; then
              echo "已更新现有 PR 评论。"
            else
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              echo "已发布新的 PR 评论。"
            fi
  ```
</CodeGroup>




---

**Navigation:** [← Previous](./41-slack.md) | [Index](./index.md) | [Next →](./43-github-actions.md)