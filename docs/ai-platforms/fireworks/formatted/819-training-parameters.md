---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Training parameters

| Flag                   | Default         | Valid range                 | When to change                                                                                                        |
| ---------------------- | --------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--epochs`             | **1**           | 1 – 10 (whole numbers only) | Add 1-2 more passes if the reward still climbs steadily near the end of training. Too many epochs risks over-fitting. |
| `--batch-size`         | **32 k tokens** | Hardware-bounded            | Lower if you hit OOM; raise only when GPUs have >30 % headroom.                                                       |
| `--learning-rate`      | **1 e-4**       | 1 e-5 – 5 e-4               | Decrease when the reward spikes then collapses; increase when the curve plateaus too early.                           |
| `--lora-rank`          | **8**           | 4 – 128 (powers of 2)       | Higher ranks give more capacity but require more GPU memory; stay ≤64 unless you have high-end GPUs.                  |
| `--max-context-length` | **8192 tokens** | Up to model limit           | Raise only when your prompts truncate; remember longer sequences consume quadratic compute.                           |

### Example usage

```bash
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --output-model my-rft-model \
  --epochs 3 \
  --learning-rate 1e-4 \
  --lora-rank 16 \
  --max-context-length 16384
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
