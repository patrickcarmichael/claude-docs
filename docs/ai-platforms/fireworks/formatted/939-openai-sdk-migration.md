---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## OpenAI SDK Migration

<Accordion title="OpenAI SDK compatibility notes">
  Fireworks provides an OpenAI-compatible API, making migration straightforward. However, there are some minor differences to be aware of:

  ### Behavioral differences

  **`stop` parameter:**

  * **Fireworks**: Returns text including the stop word
  * **OpenAI**: Omits the stop word
  * *You can easily truncate it client-side if needed*

  **`max_tokens` with context limits:**

  * **Fireworks**: Automatically adjusts `max_tokens` lower if `prompt + max_tokens` exceeds the model's context window
  * **OpenAI**: Returns an invalid request error
  * *Control this behavior with the `context_length_exceeded_behavior` parameter*

  **Streaming usage stats:**

  * **Fireworks**: Returns `usage` field in the final chunk (where `finish_reason` is set) for both streaming and non-streaming
  * **OpenAI**: Only returns usage for non-streaming responses

  Example accessing streaming usage:
```python
  for chunk in client.chat.completions.create(stream=True, ...):
      if chunk.usage:  # Available in final chunk

          print(f"Tokens: {chunk.usage.total_tokens}")
```
  ### Unsupported parameters

  The following OpenAI parameters are not yet supported:

  * `presence_penalty`
  * `frequency_penalty`
  * `best_of` (use `n` instead)
  * `logit_bias`
  * `functions` (deprecated - use [Tool Calling](/guides/function-calling) with the `tools` parameter instead)

  Have a use case requiring one of these? [Join our Discord](https://discord.gg/fireworks-ai) to discuss.
</Accordion>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
