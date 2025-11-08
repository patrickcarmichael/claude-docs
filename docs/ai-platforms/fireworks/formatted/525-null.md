---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## null

Source: https://docs.fireworks.ai/examples/knowledge-distillation


Transfer knowledge from large teacher models to smaller, low-cost, more efficient student models while preserving performance.

Knowledge distillation enables you to create compact models that maintain the reasoning capabilities of larger models. This tutorial demonstrates the complete workflow using GSM8K mathematical reasoning as our example task.

| **Technique**                       | **Teacher Model**      | **Student Model**                | **Primary Goal**            |
| ----------------------------------- | ---------------------- | -------------------------------- | --------------------------- |
| **Supervised Fine-Tuning (SFT)**    | DeepSeek-V3 (685B)     | Qwen2.5-7B                       | Format Learning & Structure |
| **Reinforcement Fine-Tuning (RFT)** | N/A (Self-improvement) | Supervised Fine-Tuned Qwen2.5-7B | Accuracy Optimization       |

<div
  align="center"
  style={{
fontSize: '18px', 
fontWeight: '600',
border: '1px solid #e2e8f0',
borderLeft: '4px solid #7018ff',
borderRadius: '6px',
padding: '12px 16px',
background: '#f8fafc',
margin: '16px auto',
maxWidth: 'fit-content'
}}
>
  Qwen2.5-7B (52% accuracy) + DeepSeek-V3 knowledge → Optimized 7B model (70% accuracy, structured format)
</div>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
