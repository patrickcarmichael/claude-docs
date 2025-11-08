---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The context window with extended thinking and tool use

The diagram below illustrates the context window token management when combining extended thinking with tool use:

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=557310c0bf57d88b7a6e550abd35bc75" alt="Context window diagram with extended thinking and tool use" data-og-width="960" width="960" data-og-height="540" height="540" data-path="images/context-window-thinking-tools.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a086ebd51148723ed500a924fb6c62a6 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=9d97e97afa9bc41f92232cd60044f716 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=65ed1d60de36587470712b2ca5ab4f45 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=174dc8d916dfdf284c86fddb4c9175f3 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=881aaf0622f43065cc942538f88562af 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=fd086e656df4fd7bf8cc2e6584689d58 2500w" />

<Steps>
  <Step title="First turn architecture">
    * **Input components:** Tools configuration and user message
    * **Output components:** Extended thinking + text response + tool use request
    * **Token calculation:** All input and output components count toward the context window, and all output components are billed as output tokens.
  </Step>

  <Step title="Tool result handling (turn 2)">
    * **Input components:** Every block in the first turn as well as the `tool_result`. The extended thinking block **must** be returned with the corresponding tool results. This is the only case wherein you **have to** return thinking blocks.
    * **Output components:** After tool results have been passed back to Claude, Claude will respond with only text (no additional extended thinking until the next `user` message).
    * **Token calculation:** All input and output components count toward the context window, and all output components are billed as output tokens.
  </Step>

  <Step title="Third Step">
    * **Input components:** All inputs and the output from the previous turn is carried forward with the exception of the thinking block, which can be dropped now that Claude has completed the entire tool use cycle. The API will automatically strip the thinking block for you if you pass it back, or you can feel free to strip it yourself at this stage. This is also where you would add the next `User` turn.
    * **Output components:** Since there is a new `User` turn outside of the tool use cycle, Claude will generate a new extended thinking block and continue from there.
    * **Token calculation:** Previous thinking tokens are automatically stripped from context window calculations. All other previous blocks still count as part of the token window, and the thinking block in the current `Assistant` turn counts as part of the context window.
  </Step>
</Steps>

* **Considerations for tool use with extended thinking:**
  * When posting tool results, the entire unmodified thinking block that accompanies that specific tool request (including signature/redacted portions) must be included.
  * The effective context window calculation for extended thinking with tool use becomes: `context_window = input_tokens + current_turn_tokens`.
  * The system uses cryptographic signatures to verify thinking block authenticity. Failing to preserve thinking blocks during tool use can break Claude's reasoning continuity. Thus, if you modify thinking blocks, the API will return an error.

>   **📝 Note**
>
> Claude 4 models support [interleaved thinking](/en/docs/build-with-claude/extended-thinking#interleaved-thinking), which enables Claude to think between tool calls and make more sophisticated reasoning after receiving tool results.

  Claude Sonnet 3.7 does not support interleaved thinking, so there is no interleaving of extended thinking and tool calls without a non-`tool_result` user turn in between.

  For more information about using tools with extended thinking, see our [extended thinking guide](/en/docs/build-with-claude/extended-thinking#extended-thinking-with-tool-use).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
