---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

The `examples/tool_calling_example/` directory contains scripts for:

1. **Local Evaluation (`local_eval.py`)**: Evaluating a model's ability to make tool calls against a dataset.
2. **TRL GRPO Integration (`trl_grpo_integration.py`)**: Fine-tuning a model for tool calling using TRL (Transformer Reinforcement Learning) with Group Relative Policy Optimization (GRPO).

A sample `dataset.jsonl` is provided in the example directory. For tool calling tasks, each entry in the dataset typically includes:

* `messages`: A list of conversation messages.
* `tools`: A list of tool definitions available to the model.
* `ground_truth`: The expected assistant response, which might include tool calls (e.g., `{"role": "assistant", "tool_calls": [...]}`) or a direct content response.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
