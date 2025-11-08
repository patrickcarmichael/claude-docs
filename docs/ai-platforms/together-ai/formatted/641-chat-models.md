---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Chat models

> In the table below, models marked as "Turbo" are quantized to FP8 and those marked as "Lite" are INT4. All our other models are at full precision (FP16).

If you're not sure which chat model to use, we currently recommend **Llama 3.3 70B Turbo** (`meta-llama/Llama-3.3-70B-Instruct-Turbo`) to get started.

| Organization    | Model Name                              | API Model String                                  | Context length | Quantization |
| :-------------- | :-------------------------------------- | :------------------------------------------------ | :------------- | :----------- |
| Moonshot        | Kimi K2 Instruct 0905                   | moonshotai/Kimi-K2-Instruct-0905                  | 262144         | FP8          |
| DeepSeek        | DeepSeek-V3.1                           | deepseek-ai/DeepSeek-V3.1                         | 128000         | FP8          |
| OpenAI          | GPT-OSS 120B                            | openai/gpt-oss-120b                               | 128000         | MXFP4        |
| OpenAI          | GPT-OSS 20B                             | openai/gpt-oss-20b                                | 128000         | MXFP4        |
| Moonshot        | Kimi K2 Instruct                        | moonshotai/Kimi-K2-Instruct                       | 128000         | FP8          |
| Z.ai            | GLM 4.5 Air                             | zai-org/GLM-4.5-Air-FP8                           | 131072         | FP8          |
| Qwen            | Qwen3 235B-A22B Thinking 2507           | Qwen/Qwen3-235B-A22B-Thinking-2507                | 262144         | FP8          |
| Qwen            | Qwen3-Coder 480B-A35B Instruct          | Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8           | 256000         | FP8          |
| Qwen            | Qwen3 235B-A22B Instruct 2507           | Qwen/Qwen3-235B-A22B-Instruct-2507-tput           | 262144         | FP8          |
| Qwen            | Qwen3-Next-80B-A3B-Instruct             | Qwen/Qwen3-Next-80B-A3B-Instruct                  | 262144         | BF16         |
| Qwen            | Qwen3-Next-80B-A3B-Thinking             | Qwen/Qwen3-Next-80B-A3B-Thinking                  | 262144         | BF16         |
| DeepSeek        | DeepSeek-R1-0528                        | deepseek-ai/DeepSeek-R1                           | 163839         | FP8          |
| DeepSeek        | DeepSeek-R1-0528 Throughput             | deepseek-ai/DeepSeek-R1-0528-tput                 | 163839         | FP8          |
| DeepSeek        | DeepSeek-V3-0324                        | deepseek-ai/DeepSeek-V3                           | 163839         | FP8          |
| Meta            | Llama 4 Maverick<br />(17Bx128E)        | meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 | 1048576        | FP8          |
| Meta            | Llama 4 Scout<br />(17Bx16E)            | meta-llama/Llama-4-Scout-17B-16E-Instruct         | 1048576        | FP16         |
| Meta            | Llama 3.3 70B Instruct Turbo            | meta-llama/Llama-3.3-70B-Instruct-Turbo           | 131072         | FP8          |
| Deep Cogito     | Cogito v2 Preview 70B                   | deepcogito/cogito-v2-preview-llama-70B            | 32768          | BF16         |
| Deep Cogito     | Cogito v2 Preview 109B MoE              | deepcogito/cogito-v2-preview-llama-109B-MoE       | 32768          | BF16         |
| Deep Cogito     | Cogito v2 Preview 405B                  | deepcogito/cogito-v2-preview-llama-405B           | 32768          | BF16         |
| Deep Cogito     | Cogito v2 Preview 671B MoE              | deepcogito/cogito-v2-preview-deepseek-671b        | 32768          | FP8          |
| Mistral AI      | Magistral Small 2506 API                | mistralai/Magistral-Small-2506                    | 40960          | BF16         |
| DeepSeek        | DeepSeek R1 Distill Llama 70B           | deepseek-ai/DeepSeek-R1-Distill-Llama-70B         | 131072         | FP16         |
| DeepSeek        | DeepSeek R1 Distill Qwen 14B            | deepseek-ai/DeepSeek-R1-Distill-Qwen-14B          | 131072         | FP16         |
| Marin Community | Marin 8B Instruct                       | marin-community/marin-8b-instruct                 | 4096           | FP16         |
| Mistral AI      | Mistral Small 3 Instruct (24B)          | mistralai/Mistral-Small-24B-Instruct-2501         | 32768          | FP16         |
| Meta            | Llama 3.1 8B Instruct Turbo             | meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo       | 131072         | FP8          |
| Meta            | Llama 3.3 70B Instruct Turbo (Free)\*\* | meta-llama/Llama-3.3-70B-Instruct-Turbo-Free      | 8193           | FP8          |
| Qwen            | Qwen 2.5 7B Instruct Turbo              | Qwen/Qwen2.5-7B-Instruct-Turbo                    | 32768          | FP8          |
| Qwen            | Qwen 2.5 72B Instruct Turbo             | Qwen/Qwen2.5-72B-Instruct-Turbo                   | 32768          | FP8          |
| Qwen            | Qwen2.5 Vision Language 72B Instruct    | Qwen/Qwen2.5-VL-72B-Instruct                      | 32768          | FP8          |
| Qwen            | Qwen 2.5 Coder 32B Instruct             | Qwen/Qwen2.5-Coder-32B-Instruct                   | 32768          | FP16         |
| Qwen            | QwQ-32B                                 | Qwen/QwQ-32B                                      | 32768          | FP16         |
| Qwen            | Qwen3 235B A22B Throughput              | Qwen/Qwen3-235B-A22B-fp8-tput                     | 40960          | FP8          |
| Arcee           | Arcee AI Virtuoso Medium                | arcee-ai/virtuoso-medium-v2                       | 128000         | -            |
| Arcee           | Arcee AI Coder-Large                    | arcee-ai/coder-large                              | 32768          | -            |
| Arcee           | Arcee AI Virtuoso-Large                 | arcee-ai/virtuoso-large                           | 128000         | -            |
| Arcee           | Arcee AI Maestro                        | arcee-ai/maestro-reasoning                        | 128000         | -            |
| Arcee           | Arcee AI Caller                         | arcee-ai/caller                                   | 32768          | -            |
| Arcee           | Arcee AI Blitz                          | arcee-ai/arcee-blitz                              | 32768          | -            |
| Meta            | Llama 3.1 405B Instruct Turbo           | meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo     | 130815         | FP8          |
| Meta            | Llama 3.2 3B Instruct Turbo             | meta-llama/Llama-3.2-3B-Instruct-Turbo            | 131072         | FP16         |
| Meta            | Llama 3 8B Instruct Lite                | meta-llama/Meta-Llama-3-8B-Instruct-Lite          | 8192           | INT4         |
| Meta            | Llama 3 70B Instruct Reference          | meta-llama/Llama-3-70b-chat-hf                    | 8192           | FP16         |
| Google          | Gemma Instruct (2B)                     | google/gemma-2b-it\*                              | 8192           | FP16         |
| Google          | Gemma 3N E4B Instruct                   | google/gemma-3n-E4B-it                            | 32768          | FP8          |
| Gryphe          | MythoMax-L2 (13B)                       | Gryphe/MythoMax-L2-13b\*                          | 4096           | FP16         |
| Mistral AI      | Mistral (7B) Instruct                   | mistralai/Mistral-7B-Instruct-v0.1                | 8192           | FP16         |
| Mistral AI      | Mistral (7B) Instruct v0.2              | mistralai/Mistral-7B-Instruct-v0.2                | 32768          | FP16         |
| Mistral AI      | Mistral (7B) Instruct v0.3              | mistralai/Mistral-7B-Instruct-v0.3                | 32768          | FP16         |

\* The Free version of Llama 3.3 70B Instruct Turbo has a reduced rate limit of .6 requests/minute (36/hour) for users on the free tier and 3 requests/minute for any user who has added a credit card on file.

\*Deprecated model, see [Deprecations](/docs/deprecations) for more details

**Chat Model Examples**

* [PDF to Chat App](https://www.pdftochat.com/) - Chat with your PDFs (blogs, textbooks, papers)
* [Open Deep Research Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Together_Open_Deep_Research_CookBook.ipynb) - Generate long form reports using a single prompt
* [RAG with Reasoning Models Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/RAG_with_Reasoning_Models.ipynb) - RAG with DeepSeek-R1
* [Fine-tuning Chat Models Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/Finetuning_Guide.ipynb) - Tune Language models for conversation
* [Building Agents](https://github.com/togethercomputer/together-cookbook/tree/main/Agents) - Agent workflows with language models

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
