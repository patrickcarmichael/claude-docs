---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Speculative Decoding

Source: https://docs.fireworks.ai/deployments/speculative-decoding

Speed up generation with draft models and n-gram speculation

Speed up text generation by using a smaller "draft" model to assist the main model, or using n-gram based speculation.

>   **📝 Note**
>
> Speculative decoding may slow down output generation if the draft model is not a good speculator, or if token count/speculation length is too high or too low. It may also reduce max throughput. Test different models and speculation lengths for your use case.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
