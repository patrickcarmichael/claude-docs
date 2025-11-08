---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Response Structure

All response objects include the following fields:

* `id`: Unique identifier for the response (e.g., `resp_abc123...`)
* `created_at`: Unix timestamp when the response was created
* `status`: Status of the response (typically `"completed"`)
* `model`: The model used to generate the response
* `output`: Array of message objects, tool calls, and tool outputs
* `usage`: Token usage information:
  * `prompt_tokens`: Number of tokens in the prompt
  * `completion_tokens`: Number of tokens in the completion
  * `total_tokens`: Total tokens used
* `previous_response_id`: ID of the previous response in the conversation (if any)
* `store`: Whether the response was stored (boolean)
* `max_tool_calls`: Maximum number of tool calls allowed (if set)

### Example Response

```json
{
  "id": "resp_abc123...",
  "created_at": 1735000000,
  "status": "completed",
  "model": "accounts/fireworks/models/qwen3-235b-a22b",
  "output": [
    {
      "id": "msg_xyz789...",
      "role": "user",
      "content": [{"type": "input_text", "text": "What is 2+2?"}],
      "status": "completed"
    },
    {
      "id": "msg_def456...",
      "role": "assistant",
      "content": [{"type": "output_text", "text": "2 + 2 equals 4."}],
      "status": "completed"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 8,
    "total_tokens": 23
  },
  "previous_response_id": null,
  "store": true,
  "max_tool_calls": null
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
