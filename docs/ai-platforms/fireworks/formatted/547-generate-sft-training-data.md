---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate SFT training data

sft_training_data, successful_count = generate_sft_training_data(sampled_problems)
```

**Actual result:**
```
Generated 5700 high-quality training examples
Teacher success rate: 5700/6000 examples
```

**Why Use a Teacher Model When We Already Have Answers?**

**You might be wondering**: "Wait, the GSM8K dataset already has the correct answers. Why do we need a teacher model to generate new ones?"

**Great question!** This tutorial uses GSM8K because it provides a controlled environment where we can verify our teacher model's accuracy. But in real-world applications, you typically **don't have the correct answers** for your specific domain.

**The Knowledge Distillation Advantage**

The Pattern: In production, you have:

* Questions/Inputs: Your domain-specific problems
* No Perfect Answers: No ground truth responses
* Solution: Use a powerful teacher model to create accurate high-quality training data

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
