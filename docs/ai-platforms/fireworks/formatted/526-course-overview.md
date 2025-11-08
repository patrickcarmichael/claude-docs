---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Course Overview

This tutorial demonstrates a systematic two-stage knowledge distillation pipeline:

**Stage 1 - SFT (Format Learning)**:

1. Generate training data with consistent output formatting
2. Train student model to internalize structured response patterns
3. Demonstrate format learning without explicit instructions

**Stage 2 - RFT (Accuracy Improvement)**:

4. Build reward system based on answer correctness

5. Apply reinforcement learning to improve reasoning within learned format

6. Show accuracy gains while maintaining consistent structure

**Why This Two-Stage Approach Works**:

* **SFT**: Excels at learning structural patterns and making them default behavior
* **RFT**: Excels at optimizing content quality through reward-based learning
* **Together**: Create models that are both well-formatted AND more accurate

**Run this tutorial interactively in Google Colab**: [Open Notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/finetuning/knowledge_distillation.ipynb)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
