---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Document ID

When passing the tool results from the tool execution step, you can optionally add custom IDs to the `id` field in the `document` object. These IDs will be used by the endpoint as the citation reference.

If you don't provide the `id` field, the ID will be auto-generated in the the format of `<tool_call_id>:<auto_generated_id>`. Example: `get_weather_1byjy32y4hvq:0`.

Here is an example of using custom IDs. To keep it concise, let's start with a pre-defined list of `messages` with the user query, tool calling, and tool results are already available.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
