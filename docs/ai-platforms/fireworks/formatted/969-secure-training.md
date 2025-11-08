---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Secure Training

Fireworks enables secure model training, including fine-tuning and reinforcement learning, while maintaining customer control over sensitive components and data. This approach builds on our [Zero Data Retention](#zero-data-retention) policy to ensure sensitive training data never persists on our platform.

**Customer-Controlled Architecture:** For advanced training workflows like reinforcement learning, critical components remain under customer control:

* Reward models and reward functions are kept proprietary and not shared
* Rollout servers and training metrics are built and managed by customers
* Model checkpoints are managed through secure cloud storage registries

**Minimal Data Sharing:** Training data is shared via controlled bucket access with minimal sharing and step-wise retention, limiting data exposure while enabling effective training workflows.

**API-Based Integration:** Customers leverage Fireworks' training APIs while maintaining full control over sensitive components, ensuring no cross-component data leakage.

<Tip>
  For detailed guidance on secure reinforcement fine-tuning and using your own cloud storage, see [Secure Fine Tuning](/fine-tuning/secure-fine-tuning).
</Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
