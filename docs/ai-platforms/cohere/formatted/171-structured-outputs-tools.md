---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Structured Outputs (Tools)

The [Structured Outputs](https://docs.cohere.com/docs/structured-outputs) feature guarantees that an LLM’s response will strictly follow a schema specified by the user.

While this feature is supported in two scenarios (JSON and tools), this page will focus on the tools scenario.

### Usage

When you use the Chat API with `tools`, setting the `strict_tools` parameter to `True` will guarantee that every generated tool call follows the specified tool schema.

Concretely, this means:

* No hallucinated tool names
* No hallucinated tool parameters
* Every `required` parameter is included in the tool call
* All parameters produce the requested data types

With `strict_tools` enabled, the API will ensure that the tool names and tool parameters are generated according to the tool definitions. This eliminates tool name and parameter hallucinations, ensures that each parameter matches the specified data type, and that all required parameters are included in the model response.

Additionally, this results in faster development. You don’t need to spend a lot of time prompt engineering the model to avoid hallucinations.

When the `strict_tools` parameter is set to `True`, you can define a maximum of 200 fields across all tools being passed to an API call.
```python PYTHON {4}
response = co.chat(model="command-a-03-2025",
    messages=[{"role": "user", "content": "What's the weather in Toronto?"}],
    tools=tools,
    strict_tools=True
)
```

### Important notes

When using `strict_tools`, the following notes apply:

* This parameter is only supported in Chat API V2 via the strict\_tools parameter (not API V1).
* You must specify at least one `required` parameter. Tools with only optional parameters are not supported in this mode.
* You can define a maximum of 200 fields across all tools in a single Chat API call.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
