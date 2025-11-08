---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Managing Context and Costs

#### **Reasoning Effort Control:**

GPT-OSS features adjustable reasoning effort levels to optimize for your specific use case:

* **Low effort:** Faster responses for simpler tasks with reduced reasoning depth
* **Medium effort:** Balanced performance for most use cases (recommended default)
* **High effort:** Maximum reasoning for complex problems requiring deep analysis. You should also specify `max_tokens` of \~30,000 with this setting.

#### **Token Management:**

When working with reasoning models, it's crucial to maintain adequate space in the context window:

* Use `max_tokens` parameter to control response length and costs
* Monitor reasoning token usage vs. output tokens - reasoning tokens can vary from hundreds to tens of thousands based on complexity
* Consider reasoning effort level based on task complexity and budget constraints
* Simpler problems may only require a few hundred reasoning tokens, while complex challenges could generate extensive reasoning

#### **Cost/Latency Optimization:**

* Implement limits on total token generation using the `max_tokens` parameter
* Balance thorough reasoning with resource utilization based on your specific requirements
* Consider using lower reasoning effort for routine tasks and higher effort for critical decisions

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
