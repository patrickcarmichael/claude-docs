---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deprecation History

All deprecations are listed below, with the most recent deprecations at the top.

| Removal Date | Model                                               | Supported by on-demand dedicated endpoints                                                             |
| :----------- | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| 2025-08-28   | `Qwen/Qwen2-VL-72B-Instruct`                        | Yes                                                                                                    |
| 2025-08-28   | `nvidia/Llama-3.1-Nemotron-70B-Instruct-HF`         | Yes                                                                                                    |
| 2025-08-28   | `perplexity-ai/r1-1776`                             | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Meta-Llama-3-8B-Instruct`               | Yes                                                                                                    |
| 2025-08-28   | `google/gemma-2-27b-it`                             | Yes                                                                                                    |
| 2025-08-28   | `Qwen/Qwen2-72B-Instruct`                           | Yes                                                                                                    |
| 2025-08-28   | `meta-llama/Llama-Vision-Free`                      | No                                                                                                     |
| 2025-08-28   | `Qwen/Qwen2.5-14B`                                  | Yes                                                                                                    |
| 2025-08-28   | `meta-llama-llama-3-3-70b-instruct-lora`            | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo`    | No (coming soon!)                                                                                      |
| 2025-08-28   | `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`       | Yes                                                                                                    |
| 2025-08-28   | `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`         | Yes                                                                                                    |
| 2025-08-28   | `black-forest-labs/FLUX.1-depth`                    | No (coming soon!)                                                                                      |
| 2025-08-28   | `black-forest-labs/FLUX.1-redux`                    | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Llama-3-8b-chat-hf`                     | Yes                                                                                                    |
| 2025-08-28   | `black-forest-labs/FLUX.1-canny`                    | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo`    | No (coming soon!)                                                                                      |
| 2025-06-13   | `gryphe-mythomax-l2-13b`                            | No (coming soon!)                                                                                      |
| 2025-06-13   | `mistralai-mixtral-8x22b-instruct-v0-1`             | No (coming soon!)                                                                                      |
| 2025-06-13   | `mistralai-mixtral-8x7b-v0-1`                       | No (coming soon!)                                                                                      |
| 2025-06-13   | `togethercomputer-m2-bert-80m-2k-retrieval`         | No (coming soon!)                                                                                      |
| 2025-06-13   | `togethercomputer-m2-bert-80m-8k-retrieval`         | No (coming soon!)                                                                                      |
| 2025-06-13   | `whereisai-uae-large-v1`                            | No (coming soon!)                                                                                      |
| 2025-06-13   | `google-gemma-2-9b-it`                              | No (coming soon!)                                                                                      |
| 2025-06-13   | `google-gemma-2b-it`                                | No (coming soon!)                                                                                      |
| 2025-06-13   | `gryphe-mythomax-l2-13b-lite`                       | No (coming soon!)                                                                                      |
| 2025-05-16   | `meta-llama-llama-3-2-3b-instruct-turbo-lora`       | No (coming soon!)                                                                                      |
| 2025-05-16   | `meta-llama-meta-llama-3-8b-instruct-turbo`         | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama/Llama-2-13b-chat-hf`                    | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-meta-llama-3-70b-instruct-turbo`        | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-meta-llama-3-1-8b-instruct-turbo-lora`  | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-meta-llama-3-1-70b-instruct-turbo-lora` | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-llama-3-2-1b-instruct-lora`             | No (coming soon!)                                                                                      |
| 2025-04-24   | `microsoft-wizardlm-2-8x22b`                        | No (coming soon!)                                                                                      |
| 2025-04-24   | `upstage-solar-10-7b-instruct-v1`                   | No (coming soon!)                                                                                      |
| 2025-04-14   | `stabilityai/stable-diffusion-xl-base-1.0`          | No (coming soon!)                                                                                      |
| 2025-04-04   | `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo-lora`  | No (coming soon!)                                                                                      |
| 2025-03-27   | `mistralai/Mistral-7B-v0.1`                         | No                                                                                                     |
| 2025-03-25   | `Qwen/QwQ-32B-Preview`                              | No                                                                                                     |
| 2025-03-13   | `databricks-dbrx-instruct`                          | No                                                                                                     |
| 2025-03-11   | `meta-llama/Meta-Llama-3-70B-Instruct-Lite`         | No                                                                                                     |
| 2025-03-08   | `Meta-Llama/Llama-Guard-7b`                         | No                                                                                                     |
| 2025-02-06   | `sentence-transformers/msmarco-bert-base-dot-v5`    | No                                                                                                     |
| 2025-02-06   | `bert-base-uncased`                                 | No                                                                                                     |
| 2024-10-29   | `Qwen/Qwen1.5-72B-Chat`                             | No                                                                                                     |
| 2024-10-29   | `Qwen/Qwen1.5-110B-Chat`                            | No                                                                                                     |
| 2024-10-07   | `NousResearch/Nous-Hermes-2-Yi-34B`                 | No                                                                                                     |
| 2024-10-07   | `NousResearch/Hermes-3-Llama-3.1-405B-Turbo`        | No                                                                                                     |
| 2024-08-22   | `NousResearch/Nous-Hermes-2-Mistral-7B-DPO`         | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-2-Mistral-7B-DPO#dedicated_endpoints)   |
| 2024-08-22   | `SG161222/Realistic_Vision_V3.0_VAE`                | No                                                                                                     |
| 2024-08-22   | `meta-llama/Llama-2-70b-chat-hf`                    | No                                                                                                     |
| 2024-08-22   | `mistralai/Mixtral-8x22B`                           | No                                                                                                     |
| 2024-08-22   | `Phind/Phind-CodeLlama-34B-v2`                      | No                                                                                                     |
| 2024-08-22   | `meta-llama/Meta-Llama-3-70B`                       | [Yes](https://api.together.xyz/models/meta-llama/Meta-Llama-3-70B#dedicated_endpoints)                 |
| 2024-08-22   | `teknium/OpenHermes-2p5-Mistral-7B`                 | [Yes](https://api.together.xyz/models/teknium/OpenHermes-2p5-Mistral-7B#dedicated_endpoints)           |
| 2024-08-22   | `openchat/openchat-3.5-1210`                        | [Yes](https://api.together.xyz/models/openchat/openchat-3.5-1210#dedicated_endpoints)                  |
| 2024-08-22   | `WizardLM/WizardCoder-Python-34B-V1.0`              | No                                                                                                     |
| 2024-08-22   | `NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT`       | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT#dedicated_endpoints) |
| 2024-08-22   | `NousResearch/Nous-Hermes-Llama2-13b`               | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-Llama2-13b#dedicated_endpoints)         |
| 2024-08-22   | `zero-one-ai/Yi-34B-Chat`                           | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-34b-Instruct-hf`               | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-34b-Python-hf`                 | No                                                                                                     |
| 2024-08-22   | `teknium/OpenHermes-2-Mistral-7B`                   | [Yes](https://api.together.xyz/models/teknium/OpenHermes-2-Mistral-7B#dedicated_endpoints)             |
| 2024-08-22   | `Qwen/Qwen1.5-14B-Chat`                             | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-14B-Chat#dedicated_endpoints)                       |
| 2024-08-22   | `stabilityai/stable-diffusion-2-1`                  | No                                                                                                     |
| 2024-08-22   | `meta-llama/Llama-3-8b-hf`                          | [Yes](https://api.together.xyz/models/meta-llama/Llama-3-8b-hf#dedicated_endpoints)                    |
| 2024-08-22   | `prompthero/openjourney`                            | No                                                                                                     |
| 2024-08-22   | `runwayml/stable-diffusion-v1-5`                    | No                                                                                                     |
| 2024-08-22   | `wavymulder/Analog-Diffusion`                       | No                                                                                                     |
| 2024-08-22   | `Snowflake/snowflake-arctic-instruct`               | No                                                                                                     |
| 2024-08-22   | `deepseek-ai/deepseek-coder-33b-instruct`           | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-7B-Chat`                              | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-7B-Chat#dedicated_endpoints)                        |
| 2024-08-22   | `Qwen/Qwen1.5-32B-Chat`                             | No                                                                                                     |
| 2024-08-22   | `cognitivecomputations/dolphin-2.5-mixtral-8x7b`    | No                                                                                                     |
| 2024-08-22   | `garage-bAInd/Platypus2-70B-instruct`               | No                                                                                                     |
| 2024-08-22   | `google/gemma-7b-it`                                | [Yes](https://api.together.xyz/models/google/gemma-7b-it#dedicated_endpoints)                          |
| 2024-08-22   | `meta-llama/Llama-2-7b-chat-hf`                     | [Yes](https://api.together.xyz/models/meta-llama/Llama-2-7b-chat-hf#dedicated_endpoints)               |
| 2024-08-22   | `Qwen/Qwen1.5-32B`                                  | No                                                                                                     |
| 2024-08-22   | `Open-Orca/Mistral-7B-OpenOrca`                     | [Yes](https://api.together.xyz/models/Open-Orca/Mistral-7B-OpenOrca#dedicated_endpoints)               |
| 2024-08-22   | `codellama/CodeLlama-13b-Instruct-hf`               | [Yes](https://api.together.xyz/models/codellama/CodeLlama-13b-Instruct-hf#dedicated_endpoints)         |
| 2024-08-22   | `NousResearch/Nous-Capybara-7B-V1p9`                | [Yes](https://api.together.xyz/models/NousResearch/Nous-Capybara-7B-V1p9#dedicated_endpoints)          |
| 2024-08-22   | `lmsys/vicuna-13b-v1.5`                             | [Yes](https://api.together.xyz/models/lmsys/vicuna-13b-v1.5#dedicated_endpoints)                       |
| 2024-08-22   | `Undi95/ReMM-SLERP-L2-13B`                          | [Yes](https://api.together.xyz/models/Undi95/ReMM-SLERP-L2-13B#dedicated_endpoints)                    |
| 2024-08-22   | `Undi95/Toppy-M-7B`                                 | [Yes](https://api.together.xyz/models/Undi95/Toppy-M-7B#dedicated_endpoints)                           |
| 2024-08-22   | `meta-llama/Llama-2-13b-hf`                         | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-70b-Instruct-hf`               | No                                                                                                     |
| 2024-08-22   | `snorkelai/Snorkel-Mistral-PairRM-DPO`              | [Yes](https://api.together.xyz/models/snorkelai/Snorkel-Mistral-PairRM-DPO#dedicated_endpoints)        |
| 2024-08-22   | `togethercomputer/LLaMA-2-7B-32K-Instruct`          | [Yes](https://api.together.xyz/models/togethercomputer/Llama-2-7B-32K-Instruct#dedicated_endpoints)    |
| 2024-08-22   | `Austism/chronos-hermes-13b`                        | [Yes](https://api.together.xyz/models/Austism/chronos-hermes-13b#dedicated_endpoints)                  |
| 2024-08-22   | `Qwen/Qwen1.5-72B`                                  | No                                                                                                     |
| 2024-08-22   | `zero-one-ai/Yi-34B`                                | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-7b-Instruct-hf`                | [Yes](https://api.together.xyz/models/codellama/CodeLlama-7b-Instruct-hf#dedicated_endpoints)          |
| 2024-08-22   | `togethercomputer/evo-1-131k-base`                  | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-70b-hf`                        | No                                                                                                     |
| 2024-08-22   | `WizardLM/WizardLM-13B-V1.2`                        | [Yes](https://api.together.xyz/models/WizardLM/WizardLM-13B-V1.2#dedicated_endpoints)                  |
| 2024-08-22   | `meta-llama/Llama-2-7b-hf`                          | No                                                                                                     |
| 2024-08-22   | `google/gemma-7b`                                   | [Yes](https://api.together.xyz/models/google/gemma-7b#dedicated_endpoints)                             |
| 2024-08-22   | `Qwen/Qwen1.5-1.8B-Chat`                            | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-1.8B-Chat#dedicated_endpoints)                      |
| 2024-08-22   | `Qwen/Qwen1.5-4B-Chat`                              | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-4B-Chat#dedicated_endpoints)                        |
| 2024-08-22   | `lmsys/vicuna-7b-v1.5`                              | [Yes](https://api.together.xyz/models/lmsys/vicuna-7b-v1.5#dedicated_endpoints)                        |
| 2024-08-22   | `zero-one-ai/Yi-6B`                                 | [Yes](https://api.together.xyz/models/zero-one-ai/Yi-6B#dedicated_endpoints)                           |
| 2024-08-22   | `Nexusflow/NexusRaven-V2-13B`                       | [Yes](https://api.together.xyz/models/Nexusflow/NexusRaven-V2-13B#dedicated_endpoints)                 |
| 2024-08-22   | `google/gemma-2b`                                   | [Yes](https://api.together.xyz/models/google/gemma-2b#dedicated_endpoints)                             |
| 2024-08-22   | `Qwen/Qwen1.5-7B`                                   | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-7B#dedicated_endpoints)                             |
| 2024-08-22   | `NousResearch/Nous-Hermes-llama-2-7b`               | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-llama-2-7b#dedicated_endpoints)         |
| 2024-08-22   | `togethercomputer/alpaca-7b`                        | [Yes](https://api.together.xyz/models/togethercomputer/alpaca-7b#dedicated_endpoints)                  |
| 2024-08-22   | `Qwen/Qwen1.5-14B`                                  | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-14B#dedicated_endpoints)                            |
| 2024-08-22   | `codellama/CodeLlama-70b-Python-hf`                 | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-4B`                                   | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-4B#dedicated_endpoints)                             |
| 2024-08-22   | `togethercomputer/StripedHyena-Hessian-7B`          | No                                                                                                     |
| 2024-08-22   | `allenai/OLMo-7B-Instruct`                          | No                                                                                                     |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-7B-Instruct`     | No                                                                                                     |
| 2024-08-22   | `togethercomputer/LLaMA-2-7B-32K`                   | [Yes](https://api.together.xyz/models/togethercomputer/LLaMA-2-7B-32K#dedicated_endpoints)             |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-7B-Base`         | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-0.5B-Chat`                            | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-0.5B-Chat#dedicated_endpoints)                      |
| 2024-08-22   | `microsoft/phi-2`                                   | [Yes](https://api.together.xyz/models/microsoft/phi-2#dedicated_endpoints)                             |
| 2024-08-22   | `Qwen/Qwen1.5-0.5B`                                 | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-0.5B#dedicated_endpoints)                           |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-7B-Chat`         | No                                                                                                     |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-Chat-3B-v1`      | No                                                                                                     |
| 2024-08-22   | `togethercomputer/GPT-JT-Moderation-6B`             | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-1.8B`                                 | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-1.8B#dedicated_endpoints)                           |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-Instruct-3B-v1`  | No                                                                                                     |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-Base-3B-v1`      | No                                                                                                     |
| 2024-08-22   | `WhereIsAI/UAE-Large-V1`                            | No                                                                                                     |
| 2024-08-22   | `allenai/OLMo-7B`                                   | No                                                                                                     |
| 2024-08-22   | `togethercomputer/evo-1-8k-base`                    | No                                                                                                     |
| 2024-08-22   | `WizardLM/WizardCoder-15B-V1.0`                     | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-13b-Python-hf`                 | [Yes](https://api.together.xyz/models/codellama/CodeLlama-13b-Python-hf#dedicated_endpoints)           |
| 2024-08-22   | `allenai-olmo-7b-twin-2t`                           | No                                                                                                     |
| 2024-08-22   | `sentence-transformers/msmarco-bert-base-dot-v5`    | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-7b-Python-hf`                  | [Yes](https://api.together.xyz/models/codellama/CodeLlama-7b-Python-hf#dedicated_endpoints)            |
| 2024-08-22   | `hazyresearch/M2-BERT-2k-Retrieval-Encoder-V1`      | No                                                                                                     |
| 2024-08-22   | `bert-base-uncased`                                 | No                                                                                                     |
| 2024-08-22   | `mistralai/Mistral-7B-Instruct-v0.1-json`           | No                                                                                                     |
| 2024-08-22   | `mistralai/Mistral-7B-Instruct-v0.1-tools`          | No                                                                                                     |
| 2024-08-22   | `togethercomputer-codellama-34b-instruct-json`      | No                                                                                                     |
| 2024-08-22   | `togethercomputer-codellama-34b-instruct-tools`     | No                                                                                                     |

\*\*Notes on model support: \*\*

* Models marked "Yes" in the on-demand dedicated endpoint support column can be spun up as dedicated endpoints with customizable hardware.
* Models marked "No" are not available as on-demand endpoints and will require migration to a different model or a monthly reserved dedicated endpoint.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
