---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Error handling

When errors occur during batch processing, they are recorded in a separate error file accessible via the `error_file_id` field. Common error codes include:

| Error Code | Description            | Solution                               |
| ---------- | ---------------------- | -------------------------------------- |
| 400        | Invalid request format | Check JSONL syntax and required fields |
| 401        | Authentication failed  | Verify API key                         |
| 404        | Batch not found        | Check batch ID                         |
| 429        | Rate limit exceeded    | Reduce request frequency               |
| 500        | Server error           | Retry with exponential backoff         |

**Error File Format:**
```jsonl
{"custom_id": "req-1", "error": {"message": "Invalid model specified", "code": "invalid_model"}}
{"custom_id": "req-5", "error": {"message": "Request timeout", "code": "timeout"}}
```javascript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
