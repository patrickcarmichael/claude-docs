---
title: "SCIM"
source: "https://docs.cursor.com/zh/account/teams/scim"
language: "zh"
language_name: "Chinese"
---

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

---

← Previous: [成员与角色](./section.md) | [Index](./index.md) | Next: [入门](./section.md) →