---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## GPT-OSS Best Practices

Reasoning models like GPT-OSS should be used differently than standard instruct models to get optimal results:

**Recommended Parameters:**

* **Reasoning Effort**: Use the adjustable reasoning effort levels to control computational cost vs. accuracy.
* **Temperature**: Use 1.0 for maximum creativity and diverse reasoning approaches.
* **Top-p**: Use 1.0 to allow the full vocabulary distribution for optimal reasoning exploration.
* **System Prompt**: The system prompt can be provided as a `developer` message which is used to provide information about the instructions for the model and available function tools.
* **System message**: It's recommended not to modify the `system` message which is used to specify reasoning effort, meta information like knowledge cutoff and built-in tools.

**Prompting Best Practices:**
Think of GPT-OSS as a senior problem-solver – provide high-level objectives and let it determine the methodology:

* **Strengths**: Excels at open-ended reasoning, multi-step logic, and inferring unstated requirements
* **Avoid over-prompting**: Micromanaging steps can limit its advanced reasoning capabilities
* **Provide clear objectives**: Balance clarity with flexibility for optimal results

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
