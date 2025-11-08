---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Performance data

Below are the zero-shot chain-of-thought evaluation scores for Claude models across different languages, shown as a percent relative to English performance (100%):

| Language                          | Claude Opus 4.1<sup>1</sup> | Claude Opus 4<sup>1</sup> | Claude Sonnet 4.5<sup>1</sup> | Claude Sonnet 4<sup>1</sup> | Claude Haiku 4.5<sup>1</sup> | Claude Haiku 3.5 |
| --------------------------------- | --------------------------- | ------------------------- | ----------------------------- | --------------------------- | ---------------------------- | ---------------- |
| English (baseline, fixed to 100%) | 100%                        | 100%                      | 100%                          | 100%                        | 100%                         | 100%             |
| Spanish                           | 98.1%                       | 98.0%                     | 98.2%                         | 97.5%                       | 96.4%                        | 94.6%            |
| Portuguese (Brazil)               | 97.8%                       | 97.3%                     | 97.8%                         | 97.2%                       | 96.1%                        | 94.6%            |
| Italian                           | 97.7%                       | 97.5%                     | 97.9%                         | 97.3%                       | 96.0%                        | 95.0%            |
| French                            | 97.9%                       | 97.7%                     | 97.5%                         | 97.1%                       | 95.7%                        | 95.3%            |
| Indonesian                        | 97.3%                       | 97.2%                     | 97.3%                         | 96.2%                       | 94.2%                        | 91.2%            |
| German                            | 97.7%                       | 97.1%                     | 97.0%                         | 94.7%                       | 94.3%                        | 92.5%            |
| Arabic                            | 97.1%                       | 96.9%                     | 97.2%                         | 96.1%                       | 92.5%                        | 84.7%            |
| Chinese (Simplified)              | 97.1%                       | 96.7%                     | 96.9%                         | 95.9%                       | 94.2%                        | 90.9%            |
| Korean                            | 96.6%                       | 96.4%                     | 96.7%                         | 95.9%                       | 93.3%                        | 89.1%            |
| Japanese                          | 96.9%                       | 96.2%                     | 96.8%                         | 95.6%                       | 93.5%                        | 90.8%            |
| Hindi                             | 96.8%                       | 96.7%                     | 96.7%                         | 95.8%                       | 92.4%                        | 80.1%            |
| Bengali                           | 95.7%                       | 95.2%                     | 95.4%                         | 94.4%                       | 90.4%                        | 72.9%            |
| Swahili                           | 89.8%                       | 89.5%                     | 91.1%                         | 87.1%                       | 78.3%                        | 64.7%            |
| Yoruba                            | 80.3%                       | 78.9%                     | 79.7%                         | 76.4%                       | 52.7%                        | 46.1%            |

<sup>1</sup> With [extended thinking](/en/docs/build-with-claude/extended-thinking).

>   **📝 Note**
>
> These metrics are based on [MMLU (Massive Multitask Language Understanding)](https://en.wikipedia.org/wiki/MMLU) English test sets that were translated into 14 additional languages by professional human translators, as documented in [OpenAI's simple-evals repository](https://github.com/openai/simple-evals/blob/main/multilingual_mmlu_benchmark_results.md). The use of human translators for this evaluation ensures high-quality translations, particularly important for languages with fewer digital resources.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
