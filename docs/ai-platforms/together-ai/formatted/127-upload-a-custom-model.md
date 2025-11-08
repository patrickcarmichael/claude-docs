---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Upload a Custom Model

Source: https://docs.together.ai/docs/custom-models

Run inference on your custom or fine-tuned models

You can upload custom or fine-tuned models from Hugging Face or S3 and run inference on a dedicated endpoint through Together AI. This is a quick guide that shows you how to do this through our UI or CLI.

### Requirements

Currently, we support models that meet the following criteria.

* **Source**: We support uploads from Hugging Face or S3.
* **Type**: We support text generation and embedding models.
* **Scale**: We currently only support models that fit in a single node. Multi-node models are not supported when you upload a custom model.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
