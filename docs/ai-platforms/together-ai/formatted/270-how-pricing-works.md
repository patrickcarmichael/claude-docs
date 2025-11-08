---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How Pricing Works

The total cost of a fine-tuning job is calculated using:

* **Model size** (e.g., Up to 16B, 16.1-69B, etc.)
* **Fine-tuning type** (Supervised Fine-tuning or Direct Preference Optimization (DPO))
* **Implementation method** (LoRA or Full Fine-tuning)
* **Total tokens processed** = (n\_epochs × n\_tokens\_per\_training\_dataset) + (n\_evals × n\_tokens\_per\_validation\_dataset)

Each combination of fine-tuning type and implementation method has its own pricing. For current rates, refer to our [fine-tuning pricing page](https://together.ai/pricing).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
