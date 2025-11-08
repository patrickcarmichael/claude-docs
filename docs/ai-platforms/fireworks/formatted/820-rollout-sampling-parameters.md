---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rollout (sampling) parameters

During each training step, the model generates multiple responses with stochastic decoding. These parameters control that generation process.

| Field           | CLI flag                  | Default   | Recommended range      | Why it matters                                                                                            |
| --------------- | ------------------------- | --------- | ---------------------- | --------------------------------------------------------------------------------------------------------- |
| Maximum tokens  | `--inference-max-tokens`  | **2 048** | 16 – 16 384            | Longer responses improve reward on summarisation / story tasks but add cost.                              |
| Temperature     | `--inference-temperature` | **0.7**   | 0.1 – 2.0 ( > 0 only ) | Values below 0.1 converge towards greedy decoding and kill exploration; 0.5–1.0 is a sweet spot for RLHF. |
| Top-p           | `--inference-top-p`       | **1.0**   | 0 – 1                  | Lower to 0.2–0.5 to clamp long-tail tokens when the reward penalises hallucinations.                      |
| Top-k           | `--inference-top-k`       | **40**    | 0 – 100 (0 = off)      | Combine with `temperature` for more creative exploration; keep ≤50 for latency.                           |
| *n* (choices)   | `--inference-n`           | **4**     | 2 – 8                  | Policy-Optimization needs multiple candidates to compute a meaningful KL term; ≥2 is mandatory.           |
| Extra body JSON | `--inference-extra-body`  | *empty*   | valid JSON             | Pass extra OpenAI-style params (e.g., `stop`, `logit_bias`). Invalid JSON is rejected.                    |

### Example usage

```bash
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --output-model my-model \
  --inference-max-tokens 1024 \
  --inference-temperature 0.8 \
  --inference-top-p 0.9 \
  --inference-top-k 40 \
  --inference-n 6 \
  --inference-extra-body '{"stop":["\n\n"]}'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
