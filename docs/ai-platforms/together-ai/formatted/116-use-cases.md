---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use cases

* Routing easy/common questions to smaller models like Llama 3.1 8B and hard/unusual questions to more capable models like Deepseek v3 and Llama 3.3 70B to optimize cost and speed.
* Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.
* Different LLMs or model configurations excel at different tasks (e.g., writing summaries vs. generating code). Using a router, you can automatically detect the user's intent and send the input to the best-fit model.
* Evaluating whether a request meets certain guidelines or triggers specific filters (e.g., checking if content is disallowed). Based on the classification, forward it to the appropriate next LLM call or step.
* If one model's output doesn't meet a certain confidence threshold or fails for some reason, route automatically to a fallback model.

>   **📝 Note**
>
> ### Conditional Workflow Cookbook

  For a more detailed walk-through refer to the [notebook here](https://togetherai.link/agent-recipes-deep-dive-routing).


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
