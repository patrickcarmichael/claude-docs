---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Which model should I use?

Source: https://docs.fireworks.ai/guides/recommended-models

A list of recommended open models for common use cases

Users often ask us, which open models should I use? There's no single right answer! Here's a curated list based on **Fireworks internal testing**, **community feedback**, and **external benchmarks**. We recommend using it as a starting point, and we will update it regularly as new models emerge.

<Tip>
  Model sizes are marked as *Small*, *Medium*, or *Large*. For best quality, use large models or fine-tune medium/small models. For best speeds, use small models.
</Tip>

| **Category**            | **Use Case**                          | **Recommended Models**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Code & Development**  | **Code generation & reasoning**       | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.1](https://app.fireworks.ai/models/fireworks/deepseek-v3p1), [GLM 4.6](https://app.fireworks.ai/models/fireworks/glm-4p6) *(Large)*<br />[Qwen2.5-32B-Coder](https://app.fireworks.ai/models/fireworks/qwen2p5-coder-32b-instruct) *(Medium)*<br />[Qwen3 Coder 30B A3B](https://app.fireworks.ai/models/fireworks/qwen3-coder-30b-a3b-instruct) *(Small)*                                                                                                                                                  |
|                         | **Code completion & bug fixing**      | [Qwen3 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b), [Qwen2.5-32B-Coder](https://app.fireworks.ai/models/fireworks/qwen2p5-coder-32b-instruct) *(Medium)*<br />[Qwen3 Coder 30B A3B](https://app.fireworks.ai/models/fireworks/qwen3-coder-30b-a3b-instruct), [Qwen3 14B](https://app.fireworks.ai/models/fireworks/qwen3-14b), [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b) *(Small)*                                                                                                                                                                         |
| **AI Applications**     | **AI Agents with tool use**           | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.1](https://app.fireworks.ai/models/fireworks/deepseek-v3p1), [Qwen3 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b), [GLM 4.6](https://app.fireworks.ai/models/fireworks/glm-4p6) *(Large)*<br />[Qwen 3 Family Models](https://app.fireworks.ai/models?filter=Provider\&provider=Qwen) *(Large/Medium/Small)*                                                                                                                                                                        |
|                         | **General reasoning & planning**      | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.1](https://app.fireworks.ai/models/fireworks/deepseek-v3p1), [Qwen3 235B Thinking 2507](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b-thinking-2507), [GLM 4.6](https://app.fireworks.ai/models/fireworks/glm-4p6) *(Large)*<br />[GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b), [Qwen2.5-72B-Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-72b-instruct), [Llama 3.3 70B](https://app.fireworks.ai/models/fireworks/llama-v3p3-70b-instruct) *(Medium)* |
|                         | **Long context & summarization**      | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905) *(Large)*<br />[GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b) *(Medium)*                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                         | **Fast semantic search & extraction** | [GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b) *(Medium)*<br />[Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b), [Llama 3.1 8B](https://app.fireworks.ai/models/fireworks/llama-v3p1-8b-instruct), [Llama 3.2 3B](https://app.fireworks.ai/models/fireworks/llama-v3p2-3b-instruct), [Llama 3.2 1B](https://app.fireworks.ai/models/fireworks/llama-v3p2-1b-instruct) *(Small)*                                                                                                                                                                                     |
| **Vision & Multimodal** | **Vision & document understanding**   | [Qwen3 VL 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-vl-235b-a22b), [Qwen2.5-VL 72B Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-72b-instruct), [Qwen2.5-VL 32B Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-32b-instruct) *(Medium)*<br />[Qwen3 VL 30B A3B](https://app.fireworks.ai/models/fireworks/qwen3-vl-30b-a3b), [Qwen2.5-VL 3-7B](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-7b-instruct) *(Small)*                                                                                                                              |

<Tip>
  You can explore all models in the [Fireworks Model Library](https://app.fireworks.ai/models)
</Tip>

*Last updated: Oct 25, 2025*


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
