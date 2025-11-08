---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Best practices

* **Monitor for refusals**: Include **`stop_reason`: `refusal`** checks in your error handling
* **Reset automatically**: Implement automatic context reset when refusals are detected
* **Provide custom messaging**: Create user-friendly messages for better UX when refusals occur
* **Track refusal patterns**: Monitor refusal frequency to identify potential issues with your prompts

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
