---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Supported Base Models

Currently, LoRA inference is supported for adapters based on the following base models in Together API. Whether using pre-fine-tuned models or bringing your own adapters, these are the only compatible models:

| Organization | Base Model Name           | Base Model String                                | Quantization |
| :----------- | :------------------------ | :----------------------------------------------- | :----------- |
| Meta         | Llama 4 Maverick Instruct | meta-llama/Llama-4-Maverick-17B-128E-Instruct    | FP8          |
| Meta         | Llama 3.1 8B Instruct     | meta-llama/Meta-Llama-3.1-8B-Instruct-Reference  | BF16         |
| Meta         | Llama 3.1 70B Instruct    | meta-llama/Meta-Llama-3.1-70B-Instruct-Reference | BF16         |
| Alibaba      | Qwen2.5 14B Instruct      | Qwen/Qwen2.5-14B-Instruct\*                      | FP8          |
| Alibaba      | Qwen2.5 72B Instruct      | Qwen/Qwen2.5-72B-Instruct                        | FP8          |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
