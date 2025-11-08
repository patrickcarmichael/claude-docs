---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Understanding the context window

The "context window" refers to the entirety of the amount of text a language model can look back on and reference when generating new text plus the new text it generates. This is different from the large corpus of data the language model was trained on, and instead represents a "working memory" for the model. A larger context window allows the model to understand and respond to more complex and lengthy prompts, while a smaller context window may limit the model's ability to handle longer prompts or maintain coherence over extended conversations.

The diagram below illustrates the standard context window behavior for API requests<sup>1</sup>:

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=eb9f2edc592262a3c2d498c3bf4e2ed1" alt="Context window diagram" data-og-width="960" width="960" data-og-height="540" height="540" data-path="images/context-window.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=db4d0f21a31307573711b71116ea01b9 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=e6c125e2f420030b1f11bc4fecba581a 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=9ee47a86de4979a05a3c91127170af2a 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=43902ab9eeb100a1141f24a33238c37f 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=e0c2f2b71fdb70b2b5c9bbfbb1a80e44 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window.svg?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=03a77b1bf4bde454fc4bffbd15d88fad 2500w" />

*<sup>1</sup>For chat interfaces, such as for [claude.ai](https://claude.ai/), context windows can also be set up on a rolling "first in, first out" system.*

* **Progressive token accumulation:** As the conversation advances through turns, each user message and assistant response accumulates within the context window. Previous turns are preserved completely.
* **Linear growth pattern:** The context usage grows linearly with each turn, with previous turns preserved completely.
* **200K token capacity:** The total available context window (200,000 tokens) represents the maximum capacity for storing conversation history and generating new output from Claude.
* **Input-output flow:** Each turn consists of:
  * **Input phase:** Contains all previous conversation history plus the current user message
  * **Output phase:** Generates a text response that becomes part of a future input

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
