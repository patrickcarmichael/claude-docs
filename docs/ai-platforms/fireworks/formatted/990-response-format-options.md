---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Response Format Options

Fireworks supports two JSON mode variants:

* **`json_object`** – Force any valid JSON output (no specific schema)
* **`json_schema`** – Enforce a specific JSON schema (recommended)

>   **⚠️ Warning**
>
> Always instruct the model to produce JSON in your prompt. Without this, the model may generate whitespace indefinitely until hitting token limits.

<AccordionGroup>
  <Accordion title="Using arbitrary JSON mode">
    To force JSON output without a specific schema:
```python
    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        response_format={"type": "json_object"},
        messages=[{
            "role": "user",
            "content": "List the top 3 programming languages in JSON format."
        }]
    )
```
    This is similar to [OpenAI's JSON mode](https://platform.openai.com/docs/guides/text-generation/json-mode).
  </Accordion>

  <Accordion title="Important notes and limitations">
    **Token limits:** If `finish_reason="length"`, the response may be truncated and invalid JSON. Increase `max_tokens` if needed.

    **Completions API:** JSON mode works with both Chat Completions and Completions APIs.

    **Function calling:** When using [Tool Calling](/guides/function-calling), JSON mode is enabled automatically—these guidelines don't apply.
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
