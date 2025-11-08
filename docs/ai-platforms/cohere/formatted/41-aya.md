---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Aya

[Aya](https://cohere.com/research/aya) is a family of multilingual large language models designed to expand the number of languages covered by generative AI for purposes of research and to better-serve minority linguistic communities.

Its 8-billion and 32-billion parameter “Expanse” offerings are optimized to perform well in these 23 languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese.

Its 8-billion and 32-billion parameter "Vision" models are state-of-the-art multimodal models excelling at a variety of critical benchmarks for language, text, and image capabilities.

| Model Name             | Description                                                                                                                                                                                                                                             | Modality     | Context Length | Maximum Output Tokens | Endpoints               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------- | --------------------- | ----------------------- |
| `c4ai-aya-expanse-8b`  | Aya Expanse is a highly performant 8B multilingual model, designed to rival monolingual performance through innovations in instruction tuning with data arbitrage, preference training, and model merging. Serves 23 languages.                         | Text         | 8k             | 4k                    | [Chat](/reference/chat) |
| `c4ai-aya-expanse-32b` | Aya Expanse is a highly performant 32B multilingual model, designed to rival monolingual performance through innovations in instruction tuning with data arbitrage, preference training, and model merging. Serves 23 languages.                        | Text         | 128k           | 4k                    | [Chat](/reference/chat) |
| `c4ai-aya-vision-8b`   | Aya Vision is a state-of-the-art multimodal model excelling at a variety of critical benchmarks for language, text, and image capabilities. This 8 billion parameter variant is focused on low latency and best-in-class performance.                   | Text, Images | 16k            | 4k                    | [Chat](/reference/chat) |
| `c4ai-aya-vision-32b`  | Aya Vision is a state-of-the-art multimodal model excelling at a variety of critical benchmarks for language, text, and image capabilities. Serves 23 languages. This 32 billion parameter variant is focused on state-of-art multilingual performance. | Text, Images | 16k            | 4k                    | [Chat](/reference/chat) |

### Using Aya Models on Different Platforms

Aya isn't available on other platforms, but it can be used with WhatsApp. Find more information [here](https://docs.cohere.com/docs/aya#aya-expanse-integration-with-whatsapp).


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
