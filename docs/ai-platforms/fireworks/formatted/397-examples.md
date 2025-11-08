---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Examples

### Cosine-Scaled Accuracy + Length Example

The [cosine\_scaled\_example.py](https://github.com/fw-ai-external/reward-kit/blob/main/examples/accuracy_length/cosine_scaled_example.py) script demonstrates the reward function's behavior with different types of responses:

* Short correct answers (highest score)
* Long correct answers (moderate score)
* Short incorrect answers (very low score)
* Long incorrect answers (low score, but still penalized for being wrong)

It also shows how to customize the weighting between accuracy and length components.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
