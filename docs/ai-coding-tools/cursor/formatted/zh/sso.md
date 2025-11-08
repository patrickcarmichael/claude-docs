---
title: "SSO"
source: "https://docs.cursor.com/zh/account/teams/sso"
language: "zh"
language_name: "Chinese"
---

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

---

← Previous: [入门](./section.md) | [Index](./index.md) | Next: [更新获取](./section.md) →