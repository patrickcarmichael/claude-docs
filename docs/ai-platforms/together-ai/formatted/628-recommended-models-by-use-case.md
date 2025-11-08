---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Recommended Models by Use Case

| Use Case                   | Recommended Model             | Model String                                        | Alternatives                                                                    | Learn More                                                                           |
| :------------------------- | :---------------------------- | :-------------------------------------------------- | :------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------- |
| **Chat**                   | Kimi K2 Instruct 0905         | `moonshotai/Kimi-K2-Instruct-0905`                  | `deepseek-ai/DeepSeek-V3.1`, `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`          | [Chat](/docs/chat-overview)                                                          |
| **Reasoning**              | DeepSeek-R1-0528              | `deepseek-ai/DeepSeek-R1`                           | `Qwen/Qwen3-235B-A22B-Thinking-2507`, `openai/gpt-oss-120b`                     | [Reasoning Guide](/docs/reasoning-models-guide), [DeepSeek R1](/docs/deepseek-r1)    |
| **Coding Agents**          | Qwen3-Coder 480B-A35B         | `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`           | `moonshotai/Kimi-K2-Instruct-0905`, `deepseek-ai/DeepSeek-V3.1`                 | [Building Agents](/docs/how-to-build-coding-agents)                                  |
| **Small & Fast**           | GPT-OSS 20B                   | `openai/gpt-oss-20b`                                | `Qwen/Qwen2.5-7B-Instruct-Turbo`, `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo` | -                                                                                    |
| **Medium General Purpose** | GLM 4.5 Air                   | `zai-org/GLM-4.5-Air-FP8`                           | `Qwen/Qwen3-Next-80B-A3B-Instruct`, `openai/gpt-oss-120b`                       | -                                                                                    |
| **Function Calling**       | GLM 4.5 Air                   | `zai-org/GLM-4.5-Air-FP8`                           | `Qwen/Qwen3-Next-80B-A3B-Instruct`, `moonshotai/Kimi-K2-Instruct-0905`          | [Function Calling](/docs/function-calling)                                           |
| **Vision**                 | Llama 4 Maverick              | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | `Qwen/Qwen2.5-VL-72B-Instruct`                                                  | [Vision](/docs/vision-overview), [OCR](/docs/quickstart-how-to-do-ocr)               |
| **Image Generation**       | Qwen Image                    | `Qwen/Qwen-Image`                                   | `google/flash-image-2.5`, `ByteDance-Seed/Seedream-4.0`                         | [Images](/docs/images-overview)                                                      |
| **Image-to-Image**         | Flash Image 2.5 (Nano Banana) | `google/flash-image-2.5`                            | `black-forest-labs/FLUX.1-kontext-pro`                                          | [Flux Kontext](/docs/quickstart-flux-kontext)                                        |
| **Text-to-Video**          | Sora 2                        | `openai/sora-2-pro`                                 | `google/veo-3.0`, `ByteDance/Seedance-1.0-pro`                                  | [Video Generation](/docs/videos-overview)                                            |
| **Image-to-Video**         | Veo 3.0                       | `google/veo-3.0`                                    | `ByteDance/Seedance-1.0-pro`, `kwaivgI/kling-2.1-master`                        | [Video Generation](/docs/videos-overview)                                            |
| **Text-to-Speech**         | Cartesia Sonic 2              | `cartesia/sonic-2`                                  | `cartesia/sonic`                                                                | [Text-to-Speech](/docs/text-to-speech)                                               |
| **Speech-to-Text**         | Whisper Large v3              | `openai/whisper-large-v3`                           | -                                                                               | [Speech-to-Text](/docs/speech-to-text)                                               |
| **Embeddings**             | GTE-Modernbert-base           | `Alibaba-NLP/gte-modernbert-base`                   | `intfloat/multilingual-e5-large-instruct`                                       | [Embeddings](/reference/embeddings-2)                                                |
| **Rerank**                 | MixedBread Rerank Large       | `mixedbread-ai/Mxbai-Rerank-Large-V2`               | `Salesforce/Llama-Rank-v1`                                                      | [Rerank](/docs/rerank-overview), [Guide](/docs/how-to-improve-search-with-rerankers) |
| **Moderation**             | Virtue Guard                  | `VirtueAI/VirtueGuard-Text-Lite`                    | `meta-llama/Llama-Guard-4-12B`                                                  | -                                                                                    |

***

**Need Help Choosing?**

* Check our [Serverless Models](/docs/serverless-models) page for complete specifications
* See our [WhichLLM](https://whichllm.together.ai/) page which provides categorical benchmarks for the above usecases
* Review [Rate Limits](/docs/rate-limits) for your tier
* See [Pricing](https://together.ai/pricing) for cost information
* Visit [Inference FAQs](/docs/inference-faqs) for common questions

For high-volume production workloads, consider [Dedicated Inference](/docs/dedicated-inference) for guaranteed capacity and predictable performance.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
