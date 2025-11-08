---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Started with Logprobs

Source: https://docs.together.ai/docs/logprobs

Learn how to return log probabilities for your output tokens & build better classifiers.

Logprobs, short for log probabilities, are logarithms of probabilities that indicate the likelihood of each token occurring based on the previous tokens in the context. They allow users to gauge a model's confidence in its outputs and explore alternative responses considered by the model and are beneficial for various applications such as classification tasks, retrieval evaluations, and autocomplete suggestions.

One big use case of using logprobs is to assess how confident a model is in its answer. For example, if you were building a classifier to categorize emails into 5 categories, with logprobs, you can get back the category and the confidence of the model in that token. For example, the LLM can categorize an email as "Spam" with 87% confidence. You can then make decisions based on this probability like if it's too low, having a larger LLM classify a specific email.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
