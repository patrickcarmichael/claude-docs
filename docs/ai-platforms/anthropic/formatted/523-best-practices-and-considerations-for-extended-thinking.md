---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Best practices and considerations for extended thinking

### Working with thinking budgets

* **Budget optimization:** The minimum budget is 1,024 tokens. We suggest starting at the minimum and increasing the thinking budget incrementally to find the optimal range for your use case. Higher token counts enable more comprehensive reasoning but with diminishing returns depending on the task. Increasing the budget can improve response quality at the tradeoff of increased latency. For critical tasks, test different settings to find the optimal balance. Note that the thinking budget is a target rather than a strict limit—actual token usage may vary based on the task.
* **Starting points:** Start with larger thinking budgets (16k+ tokens) for complex tasks and adjust based on your needs.
* **Large budgets:** For thinking budgets above 32k, we recommend using [batch processing](/en/docs/build-with-claude/batch-processing) to avoid networking issues. Requests pushing the model to think above 32k tokens causes long running requests that might run up against system timeouts and open connection limits.
* **Token usage tracking:** Monitor thinking token usage to optimize costs and performance.

### Performance considerations

* **Response times:** Be prepared for potentially longer response times due to the additional processing required for the reasoning process. Factor in that generating thinking blocks may increase overall response time.
* **Streaming requirements:** Streaming is required when `max_tokens` is greater than 21,333. When streaming, be prepared to handle both thinking and text content blocks as they arrive.

### Feature compatibility

* Thinking isn't compatible with `temperature` or `top_k` modifications as well as [forced tool use](/en/docs/agents-and-tools/tool-use/implement-tool-use#forcing-tool-use).
* When thinking is enabled, you can set `top_p` to values between 1 and 0.95.
* You cannot pre-fill responses when thinking is enabled.
* Changes to the thinking budget invalidate cached prompt prefixes that include messages. However, cached system prompts and tool definitions will continue to work when thinking parameters change.

### Usage guidelines

* **Task selection:** Use extended thinking for particularly complex tasks that benefit from step-by-step reasoning like math, coding, and analysis.
* **Context handling:** You do not need to remove previous thinking blocks yourself. The Claude API automatically ignores thinking blocks from previous turns and they are not included when calculating context usage.
* **Prompt engineering:** Review our [extended thinking prompting tips](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips) if you want to maximize Claude's thinking capabilities.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
