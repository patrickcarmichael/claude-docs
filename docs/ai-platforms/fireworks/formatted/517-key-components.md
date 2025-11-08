---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Key Components

* **`examples/math_with_formatting/main.py`**: Contains the `evaluate()` function with the core reward logic, including:
  * `accuracy_reward_fn`: Extracts and compares numerical answers.
  * `format_reward_fn`: Checks for the `<think>...</think><answer>...</answer>` structure.
* **Dataset Configuration**: Uses a derived dataset (`gsm8k_math_with_formatting_prompts.yaml`) to add specific system prompts to the base `gsm8k` dataset.

This example highlights how to enforce and evaluate structured output from LLMs alongside correctness for tasks like mathematical reasoning.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
