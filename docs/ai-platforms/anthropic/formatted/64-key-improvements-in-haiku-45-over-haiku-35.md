---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Key improvements in Haiku 4.5 over Haiku 3.5

Claude Haiku 4.5 represents a transformative leap for the Haiku model family, bringing frontier capabilities to our fastest model class:

### Near-frontier intelligence with blazing speed

Claude Haiku 4.5 delivers near-frontier performance matching Sonnet 4 at significantly lower cost and faster speed:

* **Near-frontier intelligence**: Matches Sonnet 4 performance across reasoning, coding, and complex tasks
* **Enhanced speed**: More than twice the speed of Sonnet 4, with optimizations for output tokens per second (OTPS)
* **Optimal cost-performance**: Near-frontier intelligence at one-third the cost, ideal for high-volume deployments

### Extended thinking capabilities

Claude Haiku 4.5 is the **first Haiku model** to support extended thinking, bringing advanced reasoning capabilities to the Haiku family:

* **Reasoning at speed**: Access to Claude's internal reasoning process for complex problem-solving
* **Thinking Summarization**: Summarized thinking output for production-ready deployments
* **Interleaved thinking**: Think between tool calls for more sophisticated multi-step workflows
* **Budget control**: Configure thinking token budgets to balance reasoning depth with speed

Extended thinking must be enabled explicitly by adding a `thinking` parameter to your API requests. See the [Extended thinking documentation](/en/docs/build-with-claude/extended-thinking) for implementation details.

>   **📝 Note**
>
> Claude Haiku 4.5 performs significantly better on coding and reasoning tasks when [extended thinking](/en/docs/build-with-claude/extended-thinking) is enabled. Extended thinking is disabled by default, but we recommend enabling it for complex problem-solving, coding work, and multi-step reasoning. Be aware that extended thinking impacts [prompt caching efficiency](/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks). See the [migration guide](/en/docs/about-claude/models/migrating-to-claude-4#extended-thinking-recommendations) for configuration details.

>   **📝 Note**
>
> Available in Claude Sonnet 3.7, Sonnet 4, Sonnet 4.5, Haiku 4.5, Opus 4, and Opus 4.1.

### Context awareness

Claude Haiku 4.5 features **context awareness**, enabling the model to track its remaining context window throughout a conversation:

* **Token budget tracking**: Claude receives real-time updates on remaining context capacity after each tool call
* **Better task persistence**: The model can execute tasks more effectively by understanding available working space
* **Multi-context-window workflows**: Improved handling of state transitions across extended sessions

This is the first Haiku model with native context awareness capabilities. For prompting guidance, see [Claude 4 best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#context-awareness-and-multi-window-workflows).

>   **📝 Note**
>
> Available in Claude Sonnet 4, Sonnet 4.5, Haiku 4.5, Opus 4, and Opus 4.1.

### Strong coding and tool use

Claude Haiku 4.5 delivers robust coding capabilities expected from modern Claude models:

* **Coding proficiency**: Strong performance across code generation, debugging, and refactoring tasks
* **Full tool support**: Compatible with all Claude 4 tools including bash, code execution, text editor, web search, and computer use
* **Enhanced computer use**: Optimized for autonomous desktop interaction and browser automation workflows
* **Parallel tool execution**: Efficient coordination across multiple tools for complex workflows

Haiku 4.5 is designed for use cases that demand both intelligence and efficiency:

* **Real-time applications**: Fast response times for interactive user experiences
* **High-volume processing**: Cost-effective intelligence for large-scale deployments
* **Free tier implementations**: Premium model quality at accessible pricing
* **Sub-agent architectures**: Fast, intelligent agents for multi-agent systems
* **Computer use at scale**: Cost-effective autonomous desktop and browser automation

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
