---
title: "Webhooks"
source: "https://docs.cursor.com/zh/background-agent/api/webhooks"
language: "zh"
language_name: "Chinese"
---

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

---

← Previous: [概览](./section.md) | [Index](./index.md) | Next: [Web 与移动端](./web.md) →