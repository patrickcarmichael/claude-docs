---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming responses

All the previous examples above generate responses in a non-streamed manner. This means that the endpoint would return a response object only after the model has generated the text in full.

The Chat endpoint also provides streaming support. In a streamed response, the endpoint would return a response object for each token as it is being generated. This means you can display the text incrementally without having to wait for the full completion.

To activate it, use `co.chat_stream()` instead of `co.chat()`.

In streaming mode, the endpoint will generate a series of objects. To get the actual text contents, we take objects whose `event_type` is `content-delta`.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
