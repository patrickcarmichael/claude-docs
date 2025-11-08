---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Response Structure

Below is a sample response from the Chat API. Here, the `role` of the `message` is going to be `assistant`.
```json JSON
{
    "id": "5a50480a-cf52-46f0-af01-53d18539bd31",
    "message": {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "The Art of API Design: Crafting Elegant and Powerful Interfaces",
            }
        ],
    },
    "finish_reason": "COMPLETE",
    "meta": {
        "api_version": {"version": "2", "is_experimental": True},
        "warnings": [
            "You are using an experimental version, for more information please refer to https://docs.cohere.com/versioning-reference"
        ],
        "billed_units": {"input_tokens": 17, "output_tokens": 12},
        "tokens": {"input_tokens": 215, "output_tokens": 12},
    },
}
```
Every response contains the following fields:

* `message` the generated message from the model.
* `id` the ID corresponding to this response.
* `finish_reason` can be one of the following:
  * `COMPLETE` the model successfully finished generating the message
  * `MAX_TOKENS` the model's context limit was reached before the generation could be completed
* `meta` contains information with token counts, billing etc.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
