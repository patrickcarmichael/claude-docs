---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tokenizers

A tokenizer is a tool used to convert text into tokens and vice versa. Tokenizers are model specific: the tokenizer for one Cohere model is not compatible with the tokenizer for another Cohere model, because they were trained using different tokenization methods.

Tokenizers are often used to count how many tokens a text contains. This is useful because models can handle only a certain number of tokens in one go. This limitation is known as “context length,” and the number varies from model to model.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
