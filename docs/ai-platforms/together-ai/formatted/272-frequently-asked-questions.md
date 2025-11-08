---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Frequently Asked Questions

### Is there a minimum price for fine-tuning?

No, there is no minimum price for fine-tuning jobs. You only pay for the tokens processed.

### What happens if I cancel my job?

The final price is determined based on the tokens used up to the point of cancellation.

#### Example:

If you're fine-tuning Llama-3-8B with a batch size of 8 and cancel after 1000 training steps:

* Training tokens: 8192 \[context length] × 8 \[batch size] × 1000 \[steps] = 65,536,000 tokens
* If your validation set has 1M tokens and ran 10 evaluation steps: + 10M tokens
* Total tokens: 75,536,000
* Cost: Based on the model size, fine-tuning type (SFT or DPO), and implementation method (LoRA or Full FT) chosen (check the [pricing page](https://www.together.ai/pricing))

### How can I estimate my fine-tuning job cost?

1. Calculate your approximate training tokens: context\_length × batch\_size × steps × epochs
2. Add validation tokens: validation\_dataset\_size × evaluation\_frequency
3. Multiply by the per-token rate for your chosen model size, fine-tuning type, and implementation method


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
