---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Motivation

Users frequently engage in long conversations with LLMs with the expectation that the LLM fully recalls what was said in the previous turns.

The way we make LLMs aware of previous information is by simply providing them the full conversation history, i.e., the concatenation of previous input queries and generations.

As Agents become more and more used, we face the issue to make Agents fully aware of the info from previous turns.
The current approach is to pass the Agent the generations of the previous turns (see [https://python.langchain.com/docs/how\_to/migrate\_agent/](https://python.langchain.com/docs/how_to/migrate_agent/)). However, as we show below, while this is a good approach for LLMs it is not for Agents. Given the same input, LLMs *only* produce the final generation; conversely, Agents *first* produce a reasoning chain (intermediate steps), *then* produce the final outcome. Hence, if we only retain the final generation we lose some crucial info: the reasoning chain.

A straightforward solution to this issue would be to append to the conversation history from both the reasoning chain and the generations. This is problematic due to the fact that reasoning chains can be very long, especially when the model makes mistakes and corrects itself. Using the full reasoning chains would (i) introduce a lot of noise; (ii) quickly fill the whole input window of the model.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
