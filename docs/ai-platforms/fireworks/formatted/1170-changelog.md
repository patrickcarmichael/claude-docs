---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Changelog

Source: https://docs.fireworks.ai/updates/changelog


<Update label="2025-10-20">
  ## 🏗️ Build SDK: RFT and Evaluators APIs removed

  The Build SDK no longer supports Reinforcement Fine-Tuning (RFT) and Evaluators-related APIs. To perform RFT, please use our web app via [Reinforcement Fine-Tuning](/fine-tuning/reinforcement-fine-tuning-models).
</Update>

<Update label="2025-08-22">
  ## Supervised Fine-Tuning

  We now support supervised fine tuning with separate thinking traces for reasoning models (e.g. DeepSeek R1, GPT OSS, Qwen3 Thinking etc) that ensures training-inference consistency. An example including thinking traces would look like:
```json
    {
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}, 
        {"role": "assistant", "content": "Paris.", "reasoning_content": "The user is asking about the capital city of France, it should be Paris."}
      ]
    }
    {
      "messages": [
        {"role": "user", "content": "What is 1+1?"},
        {"role": "assistant", "content": "2", "weight": 0, "reasoning_content": "The user is asking about the result of 1+1, the answer is 2."},
        {"role": "user", "content": "Now what is 2+2?"},
        {"role": "assistant", "content": "4", "reasoning_content": "The user is asking about the result of 2+2, the answer should be 4."}
      ]
    }
```
  We are also properly supporting multi-turn fine tuning (with or without thinking traces) for GPT OSS model family that ensures training-inference consistency.
</Update>

<Update label="2025-08-10">
  ## Supervised Fine-Tuning

  We now support Qwen3 MoE model (Qwen3 dense models are already supported) and GPT OSS models for supervised fine-tuning. GPT OSS model fine tunning support is single-turn without thinking traces at the moment.
</Update>

<Update label="2025-07-29">
  ## 🎨 Vision-Language Model Fine-Tuning

  You can now fine-tune Vision-Language Models (VLMs) on Fireworks AI using the Qwen 2.5 VL model family.
  This extends our Supervised Fine-tuning V2 platform to support multimodal training with both images and text data.

  **Supported models:**

  * Qwen 2.5 VL 3B Instruct
  * Qwen 2.5 VL 7B Instruct
  * Qwen 2.5 VL 32B Instruct
  * Qwen 2.5 VL 72B Instruct

  **Features:**

  * Fine-tune on datasets containing both images and text in JSONL format with base64-encoded images
  * Support for up to 64K context length during training
  * Built on the same Supervised Fine-tuning V2 infrastructure as text models

  See the [VLM fine-tuning documentation](/fine-tuning/fine-tuning-vlm) for setup instructions and dataset formatting requirements.

  ## 🔧 Build SDK: Deployment Configuration Application Requirement

  The Build SDK now requires you to call `.apply()` to apply any deployment configurations to Fireworks when using `deployment_type="on-demand"` or `deployment_type="on-demand-lora"`. This change ensures explicit control over when deployments are created and helps prevent accidental deployment creation.

  **Key changes:**

  * `.apply()` is now required for on-demand and on-demand-lora deployments
  * Serverless deployments do not require `.apply()` calls
  * If you do not call `.apply()`, you are expected to set up the deployment through the deployment page at [https://app.fireworks.ai/dashboard/deployments](https://app.fireworks.ai/dashboard/deployments)

  **Migration guide:**

  * Add `llm.apply()` after creating LLM instances with `deployment_type="on-demand"` or `deployment_type="on-demand-lora"`
  * No changes needed for serverless deployments
  * See updated documentation for examples and best practices

  This change improves deployment management and provides better control over resource creation.

  >   **📝 Note**
>
> This applies to Python SDK version `>=0.19.14`.
</Update>

<Update label="2025-07-23">
  ## 🚀 Bring Your Own Rollout and Reward Development for Reinforcement Learning

  You can now develop your own custom rollout and reward functionality while using
  Fireworks to manage the training and deployment of your models. This gives you
  full control over your reinforcement learning workflows while leveraging
  Fireworks' infrastructure for model training and deployment.

  See the new [LLM.reinforcement\_step()](/tools-sdks/python-client/sdk-reference#reinforcement-step) method and [ReinforcementStep](/tools-sdks/python-client/sdk-reference#reinforcementstep) class for usage examples and details.
</Update>

<Update label="2025-07-16">
  ## Supervised Fine-Tuning V2

  We now support Llama 4 MoE model supervised fine-tuning (Llama 4 Scout, Llama 4 Maverick, Text only).
</Update>

<Update label="2025-07-10">
  ## 🏗️ Build SDK `LLM` Deployment Logic Refactor

  Based on early feedback from users and internal testing, we've refactored the
  `LLM` class deployment logic in the Build SDK to make it easier to understand.

  **Key changes:**

  * The `id` parameter is now required when `deployment_type` is `"on-demand"`
  * The `base_id` parameter is now required when `deployment_type` is `"on-demand-lora"`
  * The `deployment_display_name` parameter is now optional and defaults to the filename where the LLM was instantiated

  A new deployment will be created if a deployment with the same `id` does not
  exist. Otherwise, the existing deployment will be reused.
</Update>

<Update label="2025-07-02">
  ## 🚀 Support for Responses API in Python SDK

  You can now use the Responses API in the Python SDK. This is useful if you want to use the Responses API in your own applications.

  See the [Responses API guide](/guides/response-api) for usage examples and details.
</Update>

<Update label="2025-07-01">
  ## Support for LinkedIn authentication

  You can now log in to Fireworks using your LinkedIn account. This is useful if
  you already have a LinkedIn account and want to use it to log in to Fireworks.

  To log in with LinkedIn, go to the [Fireworks login
  page](https://fireworks.ai/login) and click the "Continue with LinkedIn"
  button.

  You can also log in with LinkedIn from the CLI using the `firectl login`
  command.

  **How it works:**

  * Fireworks uses your LinkedIn primary email address for account identification
  * You can switch between different Fireworks accounts by changing your LinkedIn primary email
  * See our [LinkedIn authentication FAQ](/faq-new/account-access/what-email-does-linkedin-authentication-use) for detailed instructions on managing email addresses
</Update>

<Update label="2025-06-30">
  ## Support for GitHub authentication

  You can now log in to Fireworks using your GitHub account. This is useful if
  you already have a GitHub account and want to use it to log in to Fireworks.

  To log in with GitHub, go to the [Fireworks login
  page](https://fireworks.ai/login) and click the "Continue with GitHub"
  button.

  You can also log in with GitHub from the CLI using the `firectl login`
  command.

  ## 🚨 Document Inlining Deprecation

  Document Inlining has been deprecated and is no longer available on the Fireworks platform. This feature allowed LLMs to process images and PDFs through the chat completions API by appending `#transform=inline` to document URLs.

  **Migration recommendations:**

  * For image processing: Use Vision Language Models (VLMs) like [Qwen2.5-VL 32B Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-32b-instruct)
  * For PDF processing: Use dedicated PDF processing libraries combined with text-based LLMs
  * For structured extraction: Leverage our [structured responses](/structured-responses/structured-response-formatting) capabilities

  For assistance with migration, please contact our support team or visit our [Discord community](https://discord.gg/fireworks-ai).
</Update>

<Update label="2025-06-24">
  ## 🎯 Build SDK: Reward-kit integration for evaluator development

  The Build SDK now natively integrates with [reward-kit](https://github.com/fw-ai-external/reward-kit) to simplify evaluator development for [Reinforcement Fine-Tuning (RFT)](/fine-tuning/reinforcement-fine-tuning-models). You can now create custom evaluators in Python with automatic dependency management and seamless deployment to Fireworks infrastructure.

  **Key features:**

  * Native reward-kit integration for evaluator development
  * Automatic packaging of dependencies from `pyproject.toml` or `requirements.txt`
  * Local testing capabilities before deployment
  * Direct integration with Fireworks datasets and evaluation jobs
  * Support for third-party libraries and complex evaluation logic

  See our [Developing Evaluators](/tools-sdks/python-client/developing-evaluators) guide to get started with your first evaluator in minutes.

  ## Added new Responses API for advanced conversational workflows and integrations

  * Continue conversations across multiple turns using the `previous_response_id` parameter to maintain context without resending full history
  * Stream responses in real time as they are generated for responsive applications
  * Control response storage with the `store` parameter—choose whether responses are retrievable by ID or ephemeral

  See the [Response API guide](/guides/response-api) for usage examples and details.
</Update>

<Update label="2025-06-13">
  ## Supervised Fine-Tuning V2

  Supervised Fine-Tuning V2 released.

  **Key features:**

  * Supports Qwen 2/2.5/3 series, Phi 4, Gemma 3, the Llama 3 family, Deepseek V2, V3, R1
  * Longer context window up to full context length of the supported models
  * Multi-turn function calling fine-tuning
  * Quantization aware training

  More details in the [blogpost](https://fireworks.ai/blog/supervised-finetuning-v2).

  ## Reinforcement Fine-Tuning (RFT)

  Reinforcement Fine-Tuning released. Train expert models to surpass closed source frontier models through verifiable reward. More details in [blospost](https://fireworks.ai/blog/reinforcement-fine-tuning-models).
</Update>

<Update label="2025-05-20">
  ## Diarization and batch processing support added to audio inference

  See our [blog post](https://fireworks.ai/blog/audio-summer-updates-and-new-features) for details.
</Update>

<Update label="2025-05-19">
  ## 🚀 Easier & faster LoRA fine-tune deployments on Fireworks

  You can now deploy a LoRA fine-tune with a single command and get speeds that approximately match the base model:
```bash
  firectl create deployment "accounts/fireworks/models/<MODEL_ID of lora model>"
```

  Previously, this involved two distinct steps, and the resulting deployment was slower than the base model:

  1. Create a deployment using `firectl create deployment "accounts/fireworks/models/<MODEL_ID of base model>" --enable-addons`
  2. Then deploy the addon to the deployment: `firectl load-lora <MODEL_ID> --deployment <DEPLOYMENT_ID>`

  For more information, see our [deployment documentation](https://docs.fireworks.ai/models/deploying#deploying-to-on-demand).

  >   **📝 Note**
>
> This change is for dedicated deployments with a single LoRA. You can still deploy multiple LoRAs on a deployment or deploy LoRA(s) on some Serverless models as described in the documentation.
</Update>



---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
