---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Checking available precisions

Models may support different numerical precisions like FP16, FP8, BF16, or INT8, which affect memory usage and inference speed.

**Check default precision:**
```bash
firectl get model accounts/fireworks/models/llama-v3p1-8b-instruct | grep "Default Precision"
```
**Check supported precisions:**
```bash
firectl get model accounts/fireworks/models/llama-v3p1-8b-instruct | grep -E "(Supported Precisions|Supported Precisions With Calibration)"
```
The `Precisions` field indicates what precisions the model has been prepared for.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
