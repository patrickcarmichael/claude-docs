---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Supported Models

Source: https://docs.together.ai/docs/fine-tuning-models

A list of all the models available for fine-tuning.

The following models are available to use with our fine-tuning API. Get started with [fine-tuning a model](/docs/fine-tuning-quickstart)!

**Note:** This list is different from the models that support Serverless LoRA inference, which allows you to perform LoRA fine-tuning and run inference immediately. See the [LoRA inference page](/docs/lora-inference#supported-base-models) for the list of supported base models for serverless LoRA.

**Important:** When uploading LoRA adapters for serverless inference, you must use base models from the serverless LoRA list, not the fine-tuning models list. Using an incompatible base model (such as Turbo variants) will result in a "No lora\_model specified" error during upload. For example, use `meta-llama/Meta-Llama-3.1-8B-Instruct-Reference` instead of `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo` for serverless LoRA adapters.

* *Training Precision Type* indicates the precision type used during training for each model.

  * AMP (Automated Mixed Precision): AMP allows the training speed to be faster with less memory usage while preserving convergence behavior compared to using float32. Learn more about AMP in [this PyTorch blog](https://pytorch.org/blog/what-every-user-should-know-about-mixed-precision-training-in-pytorch/).
  * bf16 (bfloat 16): This uses bf16 for all weights. Some large models on our platform use full bf16 training for better memory usage and training speed.

* For batch sizes of 1, Gradient accumulation 8 is used, so effectively you will get batch size 8 (iteration time is slower).

* Long-context fine-tuning of Llama 3.1 (8B) Reference, Llama 3.1 (70B) Reference, Llama 3.1 Instruct (70B) Reference for context sizes of 32K-131K is only supported using the LoRA method.

* For Llama 3.1 (405B) Fine-tuning, please [contact us](https://www.together.ai/forms/contact-sales?prod_source=405B).

*[Request a model](https://www.together.ai/forms/model-requests)*

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
