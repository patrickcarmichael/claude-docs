---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## OpenAI Responses API Error Events

The OpenAI Responses API (`/api/alpha/responses`) uses specific event types for streaming errors:

### Error Event Types

1. **`response.failed`** - Official failure event
```json
   {
     "type": "response.failed",
     "response": {
       "id": "resp_abc123",
       "status": "failed",
       "error": {
         "code": "server_error",
         "message": "Internal server error"
       }
     }
   }
```
2. **`response.error`** - Error during response generation
```json
   {
     "type": "response.error",
     "error": {
       "code": "rate_limit_exceeded",
       "message": "Rate limit exceeded"
     }
   }
```
3. **`error`** - Plain error event (undocumented but sent by OpenAI)
```json
   {
     "type": "error",
     "error": {
       "code": "invalid_api_key",
       "message": "Invalid API key provided"
     }
   }
```

### Error Code Transformations

The Responses API transforms certain error codes into successful completions with specific finish reasons:

| Error Code                | Transformed To | Finish Reason |
| ------------------------- | -------------- | ------------- |
| `context_length_exceeded` | Success        | `length`      |
| `max_tokens_exceeded`     | Success        | `length`      |
| `token_limit_exceeded`    | Success        | `length`      |
| `string_too_long`         | Success        | `length`      |

This allows for graceful handling of limit-based errors without treating them as failures.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
