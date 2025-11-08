---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Working with images

Vision-language models support [prompt caching](/guides/prompt-caching) to improve performance for requests with repeated content. Both text and image portions can benefit from caching to reduce time to first token by up to 80%.

**Tips for optimal performance:**

* **Use URLs for long conversations** – Reduces latency compared to base64 encoding
* **Downsize images** – Smaller images use fewer tokens and process faster
* **Structure prompts for caching** – Place static instructions at the beginning, variable content at the end
* **Include metadata in prompts** – Add context about the image directly in your text prompt

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
