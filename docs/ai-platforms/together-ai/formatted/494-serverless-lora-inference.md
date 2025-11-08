---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Serverless LoRA Inference

Source: https://docs.together.ai/docs/lora-inference

Deploy a fine-tuned or uploaded LoRA model on serverless for inference

LoRA (Low-Rank Adaptation of LLMs) is a popular and lightweight training technique that significantly reduces the number of trainable parameters. It works by inserting a smaller number of new weights into the model and only these are trained. During inference these updated weights are added to the frozen original model weights. This makes training with LoRA much faster, memory-efficient, and produces smaller model weights (a few hundred MBs), which are easier to store and share.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
