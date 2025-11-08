---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 💡 Why Reinforcement Fine-Tuning?

### The Problem with Supervised Fine-Tuning (SFT) for this use-case

SFT teaches models to mimic exact SQL syntax by showing them question-SQL pairs. But the key insight is that **we care more about the result of the query than the exact SQL syntax**.

With SFT, the model is penalized if it generates a different SQL query from the training example, even though both are perfectly correct. This can lead to:

* ❌ Overfitting to specific SQL patterns
* ❌ Poorer generalization to new questions
* ❌ Need for thousands of perfectly-matched examples

### The RFT Solution

Reinforcement Fine-Tuning (RFT) takes a fundamentally different approach:

* ✅ **Rewards correct results**, regardless of SQL syntax
* ✅ **Explores multiple solution paths** during training
* ✅ **Works with just hundreds of examples** instead of thousands

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
