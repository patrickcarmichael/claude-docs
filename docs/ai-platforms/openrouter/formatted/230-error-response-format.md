---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Error Response Format

All errors follow this structure:
```json
{
  "error": {
    "code": "invalid_prompt",
    "message": "Detailed error description"
  },
  "metadata": null
}
```

### Error Codes

The API uses the following error codes:

| Code                  | Description               | Equivalent HTTP Status |
| --------------------- | ------------------------- | ---------------------- |
| `invalid_prompt`      | Request validation failed | 400                    |
| `rate_limit_exceeded` | Too many requests         | 429                    |
| `server_error`        | Internal server error     | 500+                   |


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
