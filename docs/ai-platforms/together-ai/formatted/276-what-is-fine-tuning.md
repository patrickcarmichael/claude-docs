---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## What is Fine-tuning?

Fine-tuning is the process of improving an existing LLM for a specific task or domain. You can enhance an LLM by providing labeled examples for a particular task which it can learn from. These examples can come from public datasets or private data specific to your organization.

Together AI facilitates every step of the fine-tuning process, from data preparation to model deployment. Together supports two types of fine-tuning:

1. **LoRA (Low-Rank Adaptation) fine-tuning**: Fine-tunes only a small subset of weights compared to full fine-tuning. This is faster, requires less computational resources, and is **recommended for most use cases**. Our fine-tuning API defaults to LoRA.

2. **Full fine-tuning**: Updates all weights in the model, which requires more computational resources but may provide better results for certain tasks.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
