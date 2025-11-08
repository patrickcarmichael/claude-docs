---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## List Active Sessions

To retrieve all your active sessions:
```bash
curl -X GET "https://api.together.ai/tci/sessions" \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json"
```
Output:
```json
{
  "data": {
  "sessions": [
    {
      "id":"ses_CM3zokEcfkdh5G8UiKApw",
      "started_at":"2025-03-12T10:34:22.125248Z",
      "execute_count":2,
      "last_execute_at":"2025-03-12T10:37:24.145685Z",
      "expires_at":"2025-03-12T11:04:22.125248Z"
    }
    ]
  },
  "errors": null
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
