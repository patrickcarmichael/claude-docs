---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The context window with extended thinking

When using [extended thinking](/en/docs/build-with-claude/extended-thinking), all input and output tokens, including the tokens used for thinking, count toward the context window limit, with a few nuances in multi-turn situations.

The thinking budget tokens are a subset of your `max_tokens` parameter, are billed as output tokens, and count towards rate limits.

However, previous thinking blocks are automatically stripped from the context window calculation by the Claude API and are not part of the conversation history that the model "sees" for subsequent turns, preserving token capacity for actual conversation content.

The diagram below demonstrates the specialized token management when extended thinking is enabled:

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=3ad289c01610a87c8ec1214faa09578d" alt="Context window diagram with extended thinking" data-og-width="960" width="960" data-og-height="540" height="540" data-path="images/context-window-thinking.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a8e00261582812914cb53efe0a936e7a 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=4c0f43f4dd4e6f67c32820de8a7eba04 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=c265f69b5e1dac0f8f000d9f33253093 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=6bfb8b7c35aaf9ad13283a1108b7ec0b 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=de6d6671e549c0a407b5cc1d3cb9b078 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=e41fb48241b7526f815f05125d349f07 2500w" />

* **Stripping extended thinking:** Extended thinking blocks (shown in dark gray) are generated during each turn's output phase, **but are not carried forward as input tokens for subsequent turns**. You do not need to strip the thinking blocks yourself. The Claude API automatically does this for you if you pass them back.
* **Technical implementation details:**
  * The API automatically excludes thinking blocks from previous turns when you pass them back as part of the conversation history.
  * Extended thinking tokens are billed as output tokens only once, during their generation.
  * The effective context window calculation becomes: `context_window = (input_tokens - previous_thinking_tokens) + current_turn_tokens`.
  * Thinking tokens include both `thinking` blocks and `redacted_thinking` blocks.

This architecture is token efficient and allows for extensive reasoning without token waste, as thinking blocks can be substantial in length.

>   **📝 Note**
>
> You can read more about the context window and extended thinking in our [extended thinking guide](/en/docs/build-with-claude/extended-thinking).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
