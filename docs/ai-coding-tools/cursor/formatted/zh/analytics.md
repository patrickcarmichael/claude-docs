---
title: "Analytics"
source: "https://docs.cursor.com/zh/account/teams/analytics"
language: "zh"
language_name: "Chinese"
---

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

---

← Previous: [AI Code Tracking API](./ai-code-tracking-api.md) | [Index](./index.md) | Next: [Analytics V2](./analytics-v2.md) →