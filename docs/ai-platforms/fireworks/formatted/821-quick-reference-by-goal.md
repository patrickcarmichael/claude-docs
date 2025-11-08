---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quick reference by goal

| Goal                   | Parameters to adjust                           |
| ---------------------- | ---------------------------------------------- |
| **Faster convergence** | ↑ `epochs`, tune `learning-rate` \< 2× default |
| **Safer / less toxic** | ↓ `temperature`, `top_p`, `top_k`              |
| **More creative**      | `temperature` ≈ 1 – 1.2, `top_p` 0.9           |
| **Cheaper roll-outs**  | ↓ `n`, `max_tokens`, batch size                |
| **Higher capacity**    | ↑ `lora-rank`, but monitor memory usage        |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
