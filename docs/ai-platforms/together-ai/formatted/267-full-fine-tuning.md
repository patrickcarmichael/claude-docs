---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Full Fine-tuning

| Organization | Model Name                            | Model String for API                             | Context Length (SFT) | Context Length (DPO) | Max Batch Size (SFT) | Max Batch Size (DPO) | Min Batch Size | Training Precision Type |
| ------------ | ------------------------------------- | ------------------------------------------------ | -------------------- | -------------------- | -------------------- | -------------------- | -------------- | ----------------------- |
| Deepseek     | DeepSeek-R1-Distill-Llama-70B         | deepseek-ai/DeepSeek-R1-Distill-Llama-70B        | 24576                | 8192                 | 16                   | 16                   | 16             | bf16                    |
| Deepseek     | DeepSeek-R1-Distill-Qwen-14B          | deepseek-ai/DeepSeek-R1-Distill-Qwen-14B         | 65536                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Deepseek     | DeepSeek-R1-Distill-Qwen-1.5B         | deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B        | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-270m                          | google/gemma-3-270m                              | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-270m-it                       | google/gemma-3-270m-it                           | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-1b-it                         | google/gemma-3-1b-it                             | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-1b-pt                         | google/gemma-3-1b-pt                             | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-4b-it                         | google/gemma-3-4b-it                             | 131072               | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-4b-pt                         | google/gemma-3-4b-pt                             | 131072               | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-12b-it                        | google/gemma-3-12b-it                            | 16384                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-12b-pt                        | google/gemma-3-12b-pt                            | 65536                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-27b-it                        | google/gemma-3-27b-it                            | 49152                | 8192                 | 16                   | 16                   | 16             | AMP                     |
| Google       | gemma-3-27b-pt                        | google/gemma-3-27b-pt                            | 49152                | 8192                 | 16                   | 16                   | 16             | AMP                     |
| Qwen         | Qwen3-0.6B                            | Qwen/Qwen3-0.6B                                  | 32768                | 24576                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-0.6B-Base                       | Qwen/Qwen3-0.6B-Base                             | 32768                | 24576                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-1.7B                            | Qwen/Qwen3-1.7B                                  | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-1.7B-Base                       | Qwen/Qwen3-1.7B-Base                             | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-4B                              | Qwen/Qwen3-4B                                    | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-4B-Base                         | Qwen/Qwen3-4B-Base                               | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-8B                              | Qwen/Qwen3-8B                                    | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-8B-Base                         | Qwen/Qwen3-8B-Base                               | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-14B                             | Qwen/Qwen3-14B                                   | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-14B-Base                        | Qwen/Qwen3-14B-Base                              | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-32B                             | Qwen/Qwen3-32B                                   | 24576                | 4096                 | 16                   | 16                   | 16             | AMP                     |
| Qwen         | Qwen/Qwen3-30B-A3B-Base               | Qwen/Qwen3-30B-A3B-Base                          | 8192                 | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen/Qwen3-30B-A3B                    | Qwen/Qwen3-30B-A3B                               | 8192                 | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen/Qwen3-30B-A3B-Instruct-2507      | Qwen/Qwen3-30B-A3B-Instruct-2507                 | 8192                 | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen/Qwen3-Coder-30B-A3B-Instruct     | Qwen/Qwen3-Coder-30B-A3B-Instruct                | 8192                 | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Meta         | Llama-3.3-70B-Instruct-Reference      | meta-llama/Llama-3.3-70B-Instruct-Reference      | 24576                | 8192                 | 16                   | 16                   | 16             | bf16                    |
| Meta         | Llama-3.2-3B-Instruct                 | meta-llama/Llama-3.2-3B-Instruct                 | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Llama-3.2-3B                          | meta-llama/Llama-3.2-3B                          | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Llama-3.2-1B-Instruct                 | meta-llama/Llama-3.2-1B-Instruct                 | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Llama-3.2-1B                          | meta-llama/Llama-3.2-1B                          | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Meta-Llama-3.1-8B-Instruct-Reference  | meta-llama/Meta-Llama-3.1-8B-Instruct-Reference  | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Meta-Llama-3.1-8B-Reference           | meta-llama/Meta-Llama-3.1-8B-Reference           | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Meta-Llama-3.1-70B-Instruct-Reference | meta-llama/Meta-Llama-3.1-70B-Instruct-Reference | 24576                | 8192                 | 16                   | 16                   | 16             | bf16                    |
| Meta         | Meta-Llama-3.1-70B-Reference          | meta-llama/Meta-Llama-3.1-70B-Reference          | 24576                | 8192                 | 16                   | 16                   | 16             | bf16                    |
| Meta         | Meta-Llama-3-8B-Instruct              | meta-llama/Meta-Llama-3-8B-Instruct              | 8192                 | 8192                 | 16                   | 16                   | 8              | AMP                     |
| Meta         | Meta-Llama-3-8B                       | meta-llama/Meta-Llama-3-8B                       | 8192                 | 8192                 | 16                   | 16                   | 8              | AMP                     |
| Meta         | Meta-Llama-3-70B-Instruct             | meta-llama/Meta-Llama-3-70B-Instruct             | 8192                 | 8192                 | 16                   | 16                   | 16             | bf16                    |
| Qwen         | Qwen2-7B-Instruct                     | Qwen/Qwen2-7B-Instruct                           | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2-7B                              | Qwen/Qwen2-7B                                    | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2-1.5B-Instruct                   | Qwen/Qwen2-1.5B-Instruct                         | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2-1.5B                            | Qwen/Qwen2-1.5B                                  | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Mistral AI   | Mixtral-8x7B-Instruct-v0.1            | mistralai/Mixtral-8x7B-Instruct-v0.1             | 32768                | 32768                | 16                   | 16                   | 16             | bf16                    |
| Mistral AI   | Mixtral-8x7B-v0.1                     | mistralai/Mixtral-8x7B-v0.1                      | 32768                | 32768                | 16                   | 16                   | 16             | bf16                    |
| Mistral AI   | Mistral-7B-Instruct-v0.2              | mistralai/Mistral-7B-Instruct-v0.2               | 32768                | 32768                | 8                    | 8                    | 8              | AMP                     |
| Mistral AI   | Mistral-7B-v0.1                       | mistralai/Mistral-7B-v0.1                        | 32768                | 32768                | 8                    | 8                    | 8              | AMP                     |
| Teknium      | OpenHermes-2p5-Mistral-7B             | teknium/OpenHermes-2p5-Mistral-7B                | 32768                | 32768                | 8                    | 8                    | 8              | AMP                     |
| Meta         | CodeLlama-7b-hf                       | codellama/CodeLlama-7b-hf                        | 16384                | 16384                | 16                   | 16                   | 8              | AMP                     |
| Together     | llama-2-7b-chat                       | togethercomputer/llama-2-7b-chat                 | 4096                 | 4096                 | 64                   | 64                   | 8              | AMP                     |


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
