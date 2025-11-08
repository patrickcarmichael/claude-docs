---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Frequency and Presence Penalties

The final set of parameters worth discussing in this context are `frequency_penalty` and `presence_penalty`, both of which work on logits (which are log probabilities that haven't been normalized) in order to influence how often a given token appears in output.

The frequency penalty penalizes tokens that have already appeared in the preceding text (including the prompt), and scales based on how many times that token has appeared. So a token that has already appeared 10 times gets a higher penalty (which reduces its probability of appearing) than a token that has appeared only once.

The presence penalty, on the other hand, applies the penalty regardless of frequency. As long as the token has appeared once before, it will get penalized.

These settings are useful if you want to get rid of repetition in your outputs.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
