---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Running LoRA Inference on Together

The Together API now supports LoRA inference on select base models, allowing you to either:

1. Do LoRA fine-tuning on the many available models through Together AI, then run inference right away
2. Bring Your Own Adapters: If you have custom LoRA adapters, that you've trained or obtained from HuggingFace, you can upload them and run inference

You can follow the instructions provided in the [Fine-Tuning Overview](/docs/fine-tuning-quickstart) to get started with LoRA Fine-tuning. Otherwise, follow the instructions below.

Adapters trained previous to 12/17 will not be available for LoRA serverless at the moment. We will be migrating your previous adapters to work with LoRA Serverless. A workaround is to download the adapter and re-upload it using Option 2 below.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
