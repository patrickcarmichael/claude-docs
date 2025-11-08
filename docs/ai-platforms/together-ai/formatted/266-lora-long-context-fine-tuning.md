---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## LoRA Long-context Fine-tuning

| Organization | Model Name                                 | Model String for API                                  | Context Length (SFT) | Context Length (DPO) | Max Batch Size (SFT) | Max Batch Size (DPO) | Min Batch Size | Training Precision Type |
| ------------ | ------------------------------------------ | ----------------------------------------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------- | ----------------------- |
| Deepseek     | DeepSeek-R1-Distill-Llama-70B-32k          | deepseek-ai/DeepSeek-R1-Distill-Llama-70B-32k         | 32768                | 16384                | 1                    | 1                    | 1              | AMP                     |
| Deepseek     | DeepSeek-R1-Distill-Llama-70B-131k         | deepseek-ai/DeepSeek-R1-Distill-Llama-70B-131k        | 131072               | 16384                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Llama-3.3-70B-32k-Instruct-Reference       | meta-llama/Llama-3.3-70B-32k-Instruct-Reference       | 32768                | 32768                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Llama-3.3-70B-131k-Instruct-Reference      | meta-llama/Llama-3.3-70B-131k-Instruct-Reference      | 131072               | 65536                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-8B-131k-Instruct-Reference  | meta-llama/Meta-Llama-3.1-8B-131k-Instruct-Reference  | 131072               | 131072               | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-8B-131k-Reference           | meta-llama/Meta-Llama-3.1-8B-131k-Reference           | 131072               | 131072               | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-70B-32k-Instruct-Reference  | meta-llama/Meta-Llama-3.1-70B-32k-Instruct-Reference  | 32768                | 32768                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-70B-131k-Instruct-Reference | meta-llama/Meta-Llama-3.1-70B-131k-Instruct-Reference | 131072               | 65536                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-70B-32k-Reference           | meta-llama/Meta-Llama-3.1-70B-32k-Reference           | 32768                | 32768                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-70B-131k-Reference          | meta-llama/Meta-Llama-3.1-70B-131k-Reference          | 131072               | 65536                | 1                    | 1                    | 1              | AMP                     |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
