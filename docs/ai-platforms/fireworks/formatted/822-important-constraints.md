---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Important constraints

### Temperature must be > 0

Greedy sampling (temperature 0) is deterministic and collapses exploration, often leading to mode-dropping and repetitive text.

### At least 2 rollouts required

Policy optimization needs multiple candidates per prompt to compute a meaningful KL divergence term. Setting `--inference-n 1` will fail.

### Range enforcement

The UI and CLI enforce the ranges shown above. Out-of-bound values throw an *Invalid rollout parameters* error immediately, saving wasted GPU hours.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
