---
title: "API Keys"
source: "https://docs.cursor.com/zh/settings/api-keys"
language: "zh"
language_name: "Chinese"
---

# API Keys
Source: https://docs.cursor.com/zh/settings/api-keys

自带你的 LLM 提供商

用你自己的 API key，以你自己的费用无限发送 AI 消息。配置好后，Cursor 会直接用你的 API key 调用对应的 LLM 提供商。

要使用你的 API key，前往 `Cursor Settings` > `Models`，输入你的 API key 并点击 **Verify**。验证通过后，你的 API key 就会启用。

<Warning>
  自定义 API key 仅适用于标准聊天模型。需要专用模型的功能（例如 Tab Completion）会继续使用 Cursor 的内置模型。
</Warning>

<div id="supported-providers">
  ## 支持的提供商
</div>

* **OpenAI** - 仅支持标准的非推理型聊天模型。模型选择器会显示可用的 OpenAI 模型。
* **Anthropic** - 通过 Anthropic API 提供的所有 Claude 模型。
* **Google** - 通过 Google AI API 提供的 Gemini 模型。
* **Azure OpenAI** - 部署在你 Azure OpenAI Service 实例中的模型。
* **AWS Bedrock** - 使用 AWS 访问密钥、私密密钥或 IAM 角色。适用于你 Bedrock 配置中可用的模型。

在验证你的 Bedrock IAM 角色后，会生成一个唯一的 external ID；你可以把它添加到 IAM 角色的信任策略中以增强安全性。

<div id="faq">
  ## 常见问题
</div>

<AccordionGroup>
  <Accordion title="我的 API Key 会被存储或离开我的设备吗？">
    你的 API Key 不会被存储，但每次请求都会随请求发送到我们的服务器。所有请求都会通过我们的后端进行最终的提示构建。
  </Accordion>
</AccordionGroup>

---

← Previous: [模型](./section.md) | [Index](./index.md) | Next: [Tab](./tab.md) →