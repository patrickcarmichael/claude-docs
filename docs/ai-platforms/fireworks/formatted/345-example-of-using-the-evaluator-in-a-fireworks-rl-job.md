---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example of using the evaluator in a Fireworks RL job

firectl create rl-job \
  --reward-endpoint "https://api.fireworks.ai/v1/evaluations/helpfulness-evaluator" \
  --model-id "accounts/fireworks/models/llama-v3-8b-instruct" \
  --dataset-id "my-training-dataset"
```

### Programmatic Integration with TRL

For programmatic integration with the Transformer Reinforcement Learning (TRL) library:
```python
from reward_kit import RewardFunction

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
