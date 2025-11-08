---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Managing Context and Costs

When working with reasoning models, it's crucial to maintain adequate space in the context window to accommodate the model's reasoning process. The number of reasoning tokens generated can vary based on the complexity of the task - simpler problems may only require a few hundred tokens, while more complex challenges could generate tens of thousands of reasoning tokens.

Cost/Latency management is an important consideration when using these models. To maintain control over resource usage, you can implement limits on the total token generation using the `max_tokens` parameter.

While limiting tokens can reduce costs/latency, it may also impact the model's ability to fully reason through complex problems. Therefore, it's recommended to adjust these parameters based on your specific use case and requirements, finding the optimal balance between thorough reasoning and resource utilization.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
