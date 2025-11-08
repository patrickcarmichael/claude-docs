---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Before implementing CoT

### Why let Claude think?

* **Accuracy:** Stepping through problems reduces errors, especially in math, logic, analysis, or generally complex tasks.
* **Coherence:** Structured thinking leads to more cohesive, well-organized responses.
* **Debugging:** Seeing Claude's thought process helps you pinpoint where prompts may be unclear.

### Why not let Claude think?

* Increased output length may impact latency.
* Not all tasks require in-depth thinking. Use CoT judiciously to ensure the right balance of performance and latency.

<Tip>Use CoT for tasks that a human would need to think through, like complex math, multi-step analysis, writing complex documents, or decisions with many factors.</Tip>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
