---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Temperature

Sampling from generation models incorporates randomness, so the same prompt may yield different outputs from generation to generation. Temperature is a parameter ranging from `0-1` used to tune the degree of randomness, and it defaults to a value of `.3`.

### How to pick temperature when sampling

A lower temperature means less randomness; a temperature of `0` will always yield the same output. Lower temperatures (around `.1` to `.3`) are more appropriate when performing tasks that have a "correct" answer, like question answering or summarization. If the model starts repeating itself this is a sign that the temperature may be too low.

High temperature means more randomness and less grounding. This can help the model give more creative outputs, but if you're using [retrieval augmented generation](/v2/docs/retrieval-augmented-generation-rag), it can also mean that it doesn't correctly use the context you provide. If the model starts going off topic, giving nonsensical outputs, or failing to ground properly, this is a sign that the temperature is too high.

<img src="file:6174aa01-e3b0-4802-996e-f690573741ad" alt="setting" />

Temperature can be tuned for different problems, but most people will find that a temperature of `.3` or `.5` is a good starting point.

As sequences get longer, the model naturally becomes more confident in its predictions, so you can raise the temperature much higher for long prompts without going off topic. In contrast, using high temperatures on short prompts can lead to outputs being very unstable.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
