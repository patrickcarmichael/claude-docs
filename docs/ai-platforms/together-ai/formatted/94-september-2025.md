---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## September, 2025

<Update label="Sep 15" description="/batch_api">
  **Improved Batch Inference API: Enhanced UI, Expanded Model Support, and Rate Limit Increase**

  What’s New

  * Streamlined UI: Create and track batch jobs in an intuitive interface — no complex API calls required.
  * Universal Model Access: The Batch Inference API now supports all serverless models and private deployments, so you can run batch workloads on exactly the models you need.
  * Massive Scale Jump: Rate limits are up from 10M to 30B enqueued tokens per model per user, a 3000× increase. Need more? We’ll work with you to customize.
  * Lower Cost: For most serverless models, the Batch Inference API runs at 50% the cost of our real-time API, making it the most economical way to process high-throughput workloads.
</Update>

<Update label="Sep 13" description="/chat/completions">
  **Qwen3-Next-80B Models Release**

  New Qwen3-Next-80B models now available for both thinking and instruction tasks.

  * Model ID: `Qwen/Qwen3-Next-80B-A3B-Thinking`
  * Model ID: `Qwen/Qwen3-Next-80B-A3B-Instruct`
</Update>

<Update label="Sep 10" description="/fine-tunes">
  **Fine-Tuning Platform Upgrades**

  Enhanced fine-tuning capabilities with expanded model support and increased context lengths. [Read more](https://www.together.ai/blog/fine-tuning-updates-sept-2025)

  **Enable fine-tuning for new large models:**

  * `openai/gpt-oss-120b`
  * `deepseek-ai/DeepSeek-V3.1`
  * `deepseek-ai/DeepSeek-V3.1-Base`
  * `deepseek-ai/DeepSeek-R1-0528`
  * `deepseek-ai/DeepSeek-R1`
  * `deepseek-ai/DeepSeek-V3-0324`
  * `deepseek-ai/DeepSeek-V3`
  * `deepseek-ai/DeepSeek-V3-Base`
  * `Qwen/Qwen3-Coder-480B-A35B-Instruct`
  * `Qwen/Qwen3-235B-A22B` (context length 32,768 for SFT and 16,384 for DPO)
  * `Qwen/Qwen3-235B-A22B-Instruct-2507` (context length 32,768 for SFT and 16,384 for DPO)
  * `meta-llama/Llama-4-Maverick-17B-128E`
  * `meta-llama/Llama-4-Maverick-17B-128E-Instruct`
  * `meta-llama/Llama-4-Scout-17B-16E`
  * `meta-llama/Llama-4-Scout-17B-16E-Instruct`

  ***

  **Increased maximum supported context length (per model and variant):**

  **DeepSeek Models**

  * DeepSeek-R1-Distill-Llama-70B: SFT: 8192 → 24,576, DPO: 8192 → 8192
  * DeepSeek-R1-Distill-Qwen-14B: SFT: 8192 → 65,536, DPO: 8192 → 12,288
  * DeepSeek-R1-Distill-Qwen-1.5B: SFT: 8192 → 131,072, DPO: 8192 → 16,384

  **Google Gemma Models**

  * gemma-3-1b-it: SFT: 16,384 → 32,768, DPO: 16,384 → 12,288
  * gemma-3-1b-pt: SFT: 16,384 → 32,768, DPO: 16,384 → 12,288
  * gemma-3-4b-it: SFT: 16,384 → 131,072, DPO: 16,384 → 12,288
  * gemma-3-4b-pt: SFT: 16,384 → 131,072, DPO: 16,384 → 12,288
  * gemma-3-12b-pt: SFT: 16,384 → 65,536, DPO: 16,384 → 8,192
  * gemma-3-27b-it: SFT: 12,288 → 49,152, DPO: 12,288 → 8,192
  * gemma-3-27b-pt: SFT: 12,288 → 49,152, DPO: 12,288 → 8,192

  **Qwen Models**

  * Qwen3-0.6B / Qwen3-0.6B-Base: SFT: 8192 → 32,768, DPO: 8192 → 24,576
  * Qwen3-1.7B / Qwen3-1.7B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-4B / Qwen3-4B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-8B / Qwen3-8B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-14B / Qwen3-14B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-32B: SFT: 8192 → 24,576, DPO: 8192 → 4096
  * Qwen2.5-72B-Instruct: SFT: 8192 → 24,576, DPO: 8192 → 8192
  * Qwen2.5-32B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 12,288
  * Qwen2.5-32B: SFT: 8192 → 49,152, DPO: 8192 → 12,288
  * Qwen2.5-14B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-14B: SFT: 8192 → 65,536, DPO: 8192 → 16,384
  * Qwen2.5-7B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-7B: SFT: 8192 → 131,072, DPO: 8192 → 16,384
  * Qwen2.5-3B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-3B: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-1.5B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-1.5B: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2-72B-Instruct / Qwen2-72B: SFT: 8192 → 32,768, DPO: 8192 → 8192
  * Qwen2-7B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2-7B: SFT: 8192 → 131,072, DPO: 8192 → 16,384
  * Qwen2-1.5B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2-1.5B: SFT: 8192 → 131,072, DPO: 8192 → 16,384

  **Meta Llama Models**

  * Llama-3.3-70B-Instruct-Reference: SFT: 8,192 → 24,576, DPO: 8,192 → 8,192
  * Llama-3.2-3B-Instruct: SFT: 8,192 → 131,072, DPO: 8,192 → 24,576
  * Llama-3.2-1B-Instruct: SFT: 8,192 → 131,072, DPO: 8,192 → 24,576
  * Meta-Llama-3.1-8B-Instruct-Reference: SFT: 8,192 → 131,072, DPO: 8,192 → 16,384
  * Meta-Llama-3.1-8B-Reference: SFT: 8,192 → 131,072, DPO: 8,192 → 16,384
  * Meta-Llama-3.1-70B-Instruct-Reference: SFT: 8,192 → 24,576, DPO: 8,192 → 8,192
  * Meta-Llama-3.1-70B-Reference: SFT: 8,192 → 24,576, DPO: 8,192 → 8,192

  **Mistral Models**

  * mistralai/Mistral-7B-v0.1: SFT: 8,192 → 32,768, DPO: 8,192 → 32,768
  * teknium/OpenHermes-2p5-Mistral-7B: SFT: 8,192 → 32,768, DPO: 8,192 → 32,768

  ***

  **Enhanced Hugging Face integrations:**

  * Fine-tune any \< 100B parameter CausalLM from Hugging Face Hub
  * Support for DPO variants such as LN-DPO, DPO+NLL, and SimPO
  * Support fine-tuning with maximum batch size
  * Public `fine-tunes/models/limits` and `fine-tunes/models/supported` endpoints
  * Automatic filtering of sequences with no trainable tokens (e.g., if a sequence prompt is longer than the model's context length, the completion is pushed outside the window)
</Update>

<Update label="Sep 9" description="/gpu_cluster">
  **Together Instant Clusters General Availability**

  Self-service NVIDIA GPU clusters with API-first provisioning. [Read more](https://www.together.ai/blog/together-instant-clusters-ga)

  * New API endpoints for cluster management:
    * `/v1/gpu_cluster` - Create and manage GPU clusters
    * `/v1/shared_volume` - High-performance shared storage
    * `/v1/regions` - Available data center locations
  * Support for NVIDIA Blackwell (HGX B200) and Hopper (H100, H200) GPUs
  * Scale from single-node (8 GPUs) to hundreds of interconnected GPUs
  * Pre-configured with Kubernetes, Slurm, and networking components
</Update>

<Update label="Sep 8" description="/evaluation">
  **Serverless LoRA and Dedicated Endpoints support for Evaluations**

  You can now run evaluations:

  * Using [Serverless LoRA](docs/lora-inference#serverless-lora-inference) models, including supported LoRA fine-tuned models
  * Using [Dedicated Endpoints](docs/dedicated-endpoints-1), including fine-tuned models deployed via dedicated endpoints
</Update>

<Update label="Sep 5" description="/chat/completions">
  **Kimi-K2-Instruct-0905 Model Release**

  Upgraded version of Moonshot's 1 trillion parameter MoE model with enhanced performance. [Read more](https://www.together.ai/models/kimi-k2-0905)

  * Model ID: `moonshot-ai/Kimi-K2-Instruct-0905`
</Update>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
