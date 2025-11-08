---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Chapter 4: Stage 1 - Supervised Fine-Tuning (SFT)

### Generate Formatted Training Data with Teacher Model

#### Why Use a Teacher Model

**The Knowledge Transfer Principle**

Rather than learning math reasoning from scratch, we'll have a powerful model (DeepSeek-V3) solve problems step-by-step, then train our small model to mimic those high-quality solutions.

**Why [DeepSeek-V3](https://fireworks.ai/models/fireworks/deepseek-v3-0324)**:

* **Strong mathematical reasoning** (>90% accuracy on GSM8K)
* **Clear step-by-step explanations** that provide good learning examples
* **Consistent output format** when given proper instructions
* **Cost-effective** for generating training data (no deployment required)
* **Available as serverless model on Fireworks AI platform**

**Two-Stage Data Strategy**: We'll generate one high-quality dataset from our teacher model and adapt it for both training stages:

* **Stage 1 (SFT)**: Use teacher responses as training targets to learn format patterns
* **Stage 2 (RFT)**: Use the same problems with ground truth labels for reward-based learning

### Defining Our Target Format

**Why Structured Output?**

* **Consistency**: Every response follows the same pattern
* **Parseability**: Easy to extract answers programmatically
* **Debugging**: Clear separation of reasoning and results
* **Production Ready**: Reliable format for downstream applications
* **Unique**: Different from typical model outputs
```
TARGET_FORMAT_EXAMPLE = """
[WORK]
1. Janet's ducks lay 16 eggs per day
2. She eats 3 eggs for breakfast  
3. She uses 4 eggs for muffins
4. Remaining eggs: 16 - 3 - 4 = 9 eggs
5. Revenue: 9 eggs × $2/egg = $18
[/WORK]

[RESULT]
18
[/RESULT]
"""
```

### Teaching the Teacher Model Our Format

**Strategy**: We'll use a system prompt to teach our teacher model (DeepSeek-V3) to use our desired format, then capture those formatted responses as training data.
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
