---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Max tokens and context window size with extended thinking

In older Claude models (prior to Claude Sonnet 3.7), if the sum of prompt tokens and `max_tokens` exceeded the model's context window, the system would automatically adjust `max_tokens` to fit within the context limit. This meant you could set a large `max_tokens` value and the system would silently reduce it as needed.

With Claude 3.7 and 4 models, `max_tokens` (which includes your thinking budget when thinking is enabled) is enforced as a strict limit. The system will now return a validation error if prompt tokens + `max_tokens` exceeds the context window size.

>   **📝 Note**
>
> You can read through our [guide on context windows](/en/docs/build-with-claude/context-windows) for a more thorough deep dive.

### The context window with extended thinking

When calculating context window usage with thinking enabled, there are some considerations to be aware of:

* Thinking blocks from previous turns are stripped and not counted towards your context window
* Current turn thinking counts towards your `max_tokens` limit for that turn

The diagram below demonstrates the specialized token management when extended thinking is enabled:

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=3ad289c01610a87c8ec1214faa09578d" alt="Context window diagram with extended thinking" data-og-width="960" width="960" data-og-height="540" height="540" data-path="images/context-window-thinking.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a8e00261582812914cb53efe0a936e7a 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=4c0f43f4dd4e6f67c32820de8a7eba04 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=c265f69b5e1dac0f8f000d9f33253093 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=6bfb8b7c35aaf9ad13283a1108b7ec0b 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=de6d6671e549c0a407b5cc1d3cb9b078 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=e41fb48241b7526f815f05125d349f07 2500w" />

The effective context window is calculated as:
```
context window =
  (current input tokens - previous thinking tokens) +
  (thinking tokens + encrypted thinking tokens + text output tokens)
```
We recommend using the [token counting API](/en/docs/build-with-claude/token-counting) to get accurate token counts for your specific use case, especially when working with multi-turn conversations that include thinking.

### The context window with extended thinking and tool use

When using extended thinking with tool use, thinking blocks must be explicitly preserved and returned with the tool results.

The effective context window calculation for extended thinking with tool use becomes:
```
context window =
  (current input tokens + previous thinking tokens + tool use tokens) +
  (thinking tokens + encrypted thinking tokens + text output tokens)
```javascript
The diagram below illustrates token management for extended thinking with tool use:

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=557310c0bf57d88b7a6e550abd35bc75" alt="Context window diagram with extended thinking and tool use" data-og-width="960" width="960" data-og-height="540" height="540" data-path="images/context-window-thinking-tools.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a086ebd51148723ed500a924fb6c62a6 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=9d97e97afa9bc41f92232cd60044f716 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=65ed1d60de36587470712b2ca5ab4f45 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=174dc8d916dfdf284c86fddb4c9175f3 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=881aaf0622f43065cc942538f88562af 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=fd086e656df4fd7bf8cc2e6584689d58 2500w" />

### Managing tokens with extended thinking

Given the context window and `max_tokens` behavior with extended thinking Claude 3.7 and 4 models, you may need to:

* More actively monitor and manage your token usage
* Adjust `max_tokens` values as your prompt length changes
* Potentially use the [token counting endpoints](/en/docs/build-with-claude/token-counting) more frequently
* Be aware that previous thinking blocks don't accumulate in your context window

This change has been made to provide more predictable and transparent behavior, especially as maximum token limits have increased significantly.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
