---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Upload dataset to Fireworks

dataset = Dataset.from_file("kd_rft_dataset-1.jsonl")
dataset.sync()
```

This is what an RFT training data point looks like:
```json
{"messages": [{"role": "user", "content": "There are enough provisions in a castle to feed 300 people for 90 days. After 30 days, 100 people leave the castle. How many more days are left until all the food runs out?"}], "ground_truth": "90"}
```

### Understanding Reward Kit and Evaluators

**What is Reward Kit?**

[Reward Kit](https://docs.fireworks.ai/evaluators/documentation_home) is Fireworks AI's framework for creating custom evaluation functions for reinforcement learning. Think of it as the "grading system" that tells the model whether its answers are right or wrong.
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
