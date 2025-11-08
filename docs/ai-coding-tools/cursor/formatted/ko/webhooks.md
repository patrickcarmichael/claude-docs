---
title: "Webhooks"
source: "https://docs.cursor.com/ko/background-agent/api/webhooks"
language: "ko"
language_name: "Korean"
---

# Webhooks
Source: https://docs.cursor.com/ko/background-agent/api/webhooks

백그라운드 에이전트 상태 변경 실시간 알림

<div id="webhooks">
  # Webhooks
</div>

웹훅 URL로 에이전트를 만들면 Cursor가 상태 변경을 알리려고 HTTP POST 요청을 보냄. 현재는 에이전트가 `ERROR` 또는 `FINISHED` 상태에 도달했을 때 발생하는 `statusChange` 이벤트만 지원함.

<div id="webhook-verification">
  ## Webhook 검증
</div>

Webhook 요청이 진짜로 Cursor에서 온 건지 확인하려면, 각 요청에 포함된 서명을 검증해:

<div id="headers">
  ### Headers
</div>

각 webhook 요청에는 다음 헤더가 포함돼:

* **`X-Webhook-Signature`** – `sha256=<hex_digest>` 형식의 HMAC-SHA256 서명
* **`X-Webhook-ID`** – 이 전달에 대한 고유 식별자(로그에 유용)
* **`X-Webhook-Event`** – 이벤트 타입(현재는 `statusChange`만)
* **`User-Agent`** – 항상 `Cursor-Agent-Webhook/1.0`으로 설정

<div id="signature-verification">
  ### 서명 검증
</div>

Webhook 서명을 검증하려면, 예상 서명을 계산해서 받은 서명과 비교해:

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

서명을 계산할 땐 항상 파싱 전에 원본 요청 본문(raw body)을 써.

<div id="payload-format">
  ## 페이로드 형식
</div>

웹훅 페이로드는 아래 구조의 JSON으로 전송돼:

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
  "summary": "설치 안내가 포함된 README.md 추가"
}
```

일부 필드는 선택적이어서, 사용 가능한 경우에만 포함돼.

<div id="best-practices">
  ## 모범 사례
</div>

* **서명 검증** – 요청이 Cursor에서 왔는지 확인하려면 항상 웹훅 서명을 검증해
* **재시도 처리** – 엔드포인트가 오류 상태 코드를 반환하면 웹훅이 재시도될 수 있어
* **빠른 응답** – 가능한 한 빨리 2xx 상태 코드를 반환해
* **HTTPS 사용** – 프로덕션 환경의 웹훅 엔드포인트에는 항상 HTTPS URL을 사용해
* **원본 페이로드 저장** – 디버깅과 추후 검증을 위해 웹훅 원본 페이로드를 저장해

---

← Previous: [개요](./section.md) | [Index](./index.md) | Next: [웹 & 모바일](./section.md) →