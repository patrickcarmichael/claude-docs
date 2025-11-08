---
title: "Webhooks"
source: "https://docs.cursor.com/ja/background-agent/api/webhooks"
language: "ja"
language_name: "Japanese"
---

# Webhooks
Source: https://docs.cursor.com/ja/background-agent/api/webhooks

バックグラウンドエージェントのステータス変更をリアルタイムで受け取る

<div id="webhooks">
  # Webhooks
</div>

webhook の URL を指定してエージェントを作成すると、Cursor はステータス変更を通知するために HTTP POST リクエストを送信する。現在サポートされているのは `statusChange` イベントのみで、エージェントが `ERROR` または `FINISHED` の状態になったときに送信される。

<div id="webhook-verification">
  ## Webhook の検証
</div>

Webhook リクエストが確実に Cursor からのものか確認するため、各リクエストに含まれる署名を検証してね:

<div id="headers">
  ### ヘッダー
</div>

各 Webhook リクエストには次のヘッダーが含まれるよ:

* **`X-Webhook-Signature`** – 形式 `sha256=<hex_digest>` の HMAC-SHA256 署名を含む
* **`X-Webhook-ID`** – この配信の一意の識別子（ログに便利）
* **`X-Webhook-Event`** – イベントタイプ（現在は `statusChange` のみ）
* **`User-Agent`** – 常に `Cursor-Agent-Webhook/1.0` が設定されている

<div id="signature-verification">
  ### 署名の検証
</div>

Webhook の署名を検証するには、期待される署名を算出して、受信した署名と照合してね:

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

シグネチャを計算するときは、必ずパース前の生のリクエストボディを使用して。

<div id="payload-format">
  ## ペイロード形式
</div>

Webhook のペイロードは、次の構造の JSON として送信される:

```json  theme={null}
{
  "event": "statusChange",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "インストール手順を追加した README.md を追加"
}
```

一部のフィールドは任意で、利用可能な場合にのみ含まれる点に注意してね。

<div id="best-practices">
  ## ベストプラクティス
</div>

* **署名の検証** – リクエストが Cursor からのものか確かめるため、必ず webhook の署名を検証しよう
* **リトライへの対応** – エンドポイントがエラーステータスコードを返した場合、webhook は再送されることがある
* **すばやく返す** – 可能な限り早く 2xx のステータスコードを返そう
* **HTTPS を使う** – 本番環境の webhook エンドポイントには必ず HTTPS の URL を使おう
* **生ペイロードを保存** – デバッグや将来の検証のために、生の webhook ペイロードを保存しておこう

---

← Previous: [概要](./section.md) | [Index](./index.md) | Next: [Web とモバイル](./web.md) →