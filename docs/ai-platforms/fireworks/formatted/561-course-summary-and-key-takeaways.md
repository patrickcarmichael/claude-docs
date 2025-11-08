---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Course Summary and Key Takeaways

### What We Demonstrated

**1. SFT for Internalized Format Learning**:

* **Training Strategy**: Include format examples without system prompts in training data
* **Testing Strategy**: No system prompts needed - format is internalized
* **Result**: Model automatically uses `[WORK]/[RESULT]` structure as default behavior
* **Key Insight**: SFT teaches "how to respond" by making patterns the model's natural behavior

**2. RFT for Accuracy Improvement**:

* **Foundation**: Builds on SFT model
* **Optimization**: Reward-based learning improves content quality
* **Result**: Significantly improves reasoning accuracy
* **Key Insight**: RFT optimizes "what to respond with"

**3. Two-Stage Pipeline Synergy**:

* **Stage 1 (SFT)**: Establishes reliable, consistent response structure
* **Stage 2 (RFT)**: Optimizes content quality within that structure
* **Combined Result**: Models that are both well-formatted AND accurate

### Practical Applications

This knowledge distillation approach is valuable for:

* **API Integrations**: Reliable output parsing + improved accuracy
* **Structured Reasoning Tasks**: Clear thinking process + better results
* **Production Pipelines**: Consistent format + higher quality content
* **Evaluation Systems**: Easy answer extraction + improved performance
* **Cost Optimization**: Small models with large model capabilities

### Expected Resources

* **Cost**: \~Costs apply for API calls, deployments and training jobs

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
