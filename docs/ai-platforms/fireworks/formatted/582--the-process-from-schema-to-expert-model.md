---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 🔄 The Process: From Schema to Expert Model

Here's the complete pipeline you'll implement:

1. **Start with just your schema** (no real data needed!): Extract table structures and relationships
2. **Generate synthetic data**: Use LLMs to create realistic fake data that maintains referential integrity
3. **Create SQL queries**: Use historical logs or generate diverse query patterns
4. **Execute for ground truth**: Run queries against synthetic data to get expected results
5. **Generate natural language questions**: Convert SQL to questions users would actually ask
6. **Train with RFT**: Model learns through trial and error, rewarded for correct results

### Why this matters

Off-the-shelf LLM copilots often guess column names, ignore schema quirks, or hallucinate tables. **Reinforcement Fine-Tuning (RFT)** fixes this by teaching the model the shape of your data *and* the patterns in your queries, boosting exact-match accuracy.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
