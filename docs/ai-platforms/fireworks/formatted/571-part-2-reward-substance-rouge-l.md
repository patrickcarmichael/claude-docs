---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Part 2: Reward substance (ROUGE-L)

Once the model has learned that shorter is better, we need to remind it that substance still counts. The second evaluator rewards each summary according to how much of the source document’s wording it captures. A quick overlap measure—ROUGE‑L—is enough to push the policy toward mentioning the main ideas instead of trimming indiscriminately.
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
