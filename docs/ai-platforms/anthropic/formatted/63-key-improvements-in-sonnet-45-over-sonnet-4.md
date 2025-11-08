---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Key improvements in Sonnet 4.5 over Sonnet 4

### Coding excellence

Claude Sonnet 4.5 is our best coding model to date, with significant improvements across the entire development lifecycle:

* **SWE-bench Verified performance**: Advanced state-of-the-art on coding benchmarks
* **Enhanced planning and system design**: Better architectural decisions and code organization
* **Improved security engineering**: More robust security practices and vulnerability detection
* **Better instruction following**: More precise adherence to coding specifications and requirements

>   **📝 Note**
>
> Claude Sonnet 4.5 performs significantly better on coding tasks when [extended thinking](/en/docs/build-with-claude/extended-thinking) is enabled. Extended thinking is disabled by default, but we recommend enabling it for complex coding work. Be aware that extended thinking impacts [prompt caching efficiency](/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks). See the [migration guide](/en/docs/about-claude/models/migrating-to-claude-4#extended-thinking-recommendations) for configuration details.

### Agent capabilities

Claude Sonnet 4.5 introduces major advances in agent capabilities:

* **Extended autonomous operation**: Sonnet 4.5 can work independently for hours while maintaining clarity and focus on incremental progress. The model makes steady advances on a few tasks at a time rather than attempting everything at once. It provides fact-based progress updates that accurately reflect what has been accomplished.
* **Context awareness**: Claude now tracks its token usage throughout conversations, receiving updates after each tool call. This awareness helps prevent premature task abandonment and enables more effective execution on long-running tasks. See [Context awareness](/en/docs/build-with-claude/context-windows#context-awareness-in-claude-sonnet-4-5) for technical details and [prompting guidance](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#context-awareness-and-multi-window-workflows).
* **Enhanced tool usage**: The model more effectively uses parallel tool calls, firing off multiple speculative searches simultaneously during research and reading several files at once to build context faster. Improved coordination across multiple tools and information sources enables the model to effectively leverage a wide range of capabilities in agentic search and coding workflows.
* **Advanced context management**: Sonnet 4.5 maintains exceptional state tracking in external files, preserving goal-orientation across sessions. Combined with more effective context window usage and our new context management API features, the model optimally handles information across extended sessions to maintain coherence over time.

>   **📝 Note**
>
> Context awareness is available in Claude Sonnet 4, Sonnet 4.5, Haiku 4.5, Opus 4, and Opus 4.1.

### Communication and interaction style

Claude Sonnet 4.5 has a refined communication approach that is concise, direct, and natural. It provides fact-based progress updates and may skip verbose summaries after tool calls to maintain workflow momentum (though this can be adjusted with prompting).

For detailed guidance on working with this communication style, see [Claude 4 best practices](/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices).

### Creative content generation

Claude Sonnet 4.5 excels at creative content tasks:

* **Presentations and animations**: Matches or exceeds Claude Opus 4.1 for creating slides and visual content
* **Creative flair**: Produces polished, professional output with strong instruction following
* **First-try quality**: Generates usable, well-designed content in initial attempts

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
