---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Conclusion

This tutorial demonstrated how to systematically apply knowledge distillation using [Fireworks AI](https://app.fireworks.ai/account/home) to create models that combine the structural reliability of supervised learning with the performance optimization of reinforcement learning.

**Key Success Factors**:

1. **Clear separation of concerns**: SFT for structure, RFT for accuracy
2. **Consistent evaluation methodology**: Test without system prompts to measure true learning
3. **Building on foundations**: RFT builds on SFT rather than starting from scratch
4. **Quality training data**: High teacher model accuracy and format consistency

The result is a compact, efficient model that maintains the reasoning capabilities and output structure of much larger models, making it suitable for production deployment at significantly lower cost and latency.

**Next Steps**: Apply this methodology to your own domain-specific tasks by:

1. Defining appropriate outputs for your use case
2. Generating high-quality teacher demonstrations
3. Fine tuning
4. Evaluating performance improvements

This systematic approach to knowledge distillation enables you to create specialized, efficient models that retain the capabilities of their larger teachers while being practical for real-world deployment.

Questions or feedback? Reach out to us on [Discord](https://discord.gg/fireworks-ai).


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
