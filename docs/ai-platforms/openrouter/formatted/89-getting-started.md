---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Started

All multimodal inputs use the same `/api/v1/chat/completions` endpoint with the `messages` parameter. Different content types are specified in the message content array:

* **Images**: Use `image_url` content type
* **PDFs**: Use `file` content type with PDF data
* **Audio**: Use `input_audio` content type
* **Video**: Use `input_video` content type

You can combine multiple modalities in a single request, and the number of files you can send varies by provider and model.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
