---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

The "Math with Formatting" example demonstrates a multi-metric evaluation:

1. **Accuracy Reward**: Assesses if the extracted numerical answer is correct.
2. **Format Reward**: Checks if the model's response follows the prescribed XML-like structure for thoughts and the final answer.
   The final score reported is typically an average of these two rewards.

* **Dataset**: Uses the `gsm8k` dataset, configured via `gsm8k_math_with_formatting_prompts.yaml` which adds specific system prompts to guide the model's output format.
* **Reward Logic**: The core evaluation logic is in `examples/math_with_formatting/main.py`, referenced in the run configuration as `examples.math_with_formatting.main.evaluate`.
* **System Prompt Example** (from `gsm8k_math_with_formatting_prompts.yaml`):
```
  Solve the following math problem. Provide your reasoning and then put the final numerical answer between <answer> and </answer> tags.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
