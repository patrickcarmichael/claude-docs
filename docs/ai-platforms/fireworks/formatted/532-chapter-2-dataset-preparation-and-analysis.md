---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Chapter 2: Dataset Preparation and Analysis

**Why GSM8K?**

* **Standard Benchmark**: Widely used for evaluating mathematical reasoning
* **Clear Evaluation**: Numerical answers are easy to check for correctness
* **Appropriate Difficulty**: Challenging enough to demonstrate knowledge transfer

**Why We Need Proper Train/Test Splits**

**Critical for Valid Evaluation**: Using the same data for training and testing leads to inflated results that don't reflect real-world performance. GSM8K provides standard splits that enable fair comparison with other research.

### Load GSM8K Dataset

```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
