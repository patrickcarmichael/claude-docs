---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prompting tips

| Tip                                                                                                                       | Rationale                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Keep the system prompt simple** - `"You are Kimi, an AI assistant created by Moonshot AI."` is the recommended default. | Matches the prompt used during instruction tuning.                                                                                       |
| **Temperature ≈ 0.6**                                                                                                     | Calibrated to Kimi-K2-Instruct's RLHF alignment curve; higher values yield verbosity.                                                    |
| **Leverage native tool calling**                                                                                          | Pass a JSON schema in `tools=[...]`; set `tool_choice="auto"`. Kimi decides when/what to call.                                           |
| **Think in goals, not steps**                                                                                             | Because the model is "agentic", give a *high-level objective* ("Analyse this CSV and write a report"), letting it orchestrate sub-tasks. |
| **Chunk very long contexts**                                                                                              | 256 K is huge, but response speed drops on >100 K inputs; supply a short executive summary in the final user message to focus the model. |

Many of this information was found in the [Kimi GitHub repo](https://github.com/MoonshotAI/Kimi-K2).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
