---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Choosing between Sonnet 4.5 and Haiku 4.5

Both Claude Sonnet 4.5 and Claude Haiku 4.5 are powerful Claude 4 models with different strengths:

### Choose Claude Sonnet 4.5 (most intelligent) for:

* **Complex reasoning and analysis**: Best-in-class intelligence for sophisticated tasks
* **Long-running autonomous agents**: Superior performance for agents working independently for extended periods
* **Advanced coding tasks**: Our strongest coding model with advanced planning and security engineering
* **Large context workflows**: Enhanced context management with memory tool and context editing capabilities
* **Tasks requiring maximum capability**: When intelligence and accuracy are the top priorities

### Choose Claude Haiku 4.5 (fastest and most intelligent Haiku) for:

* **Real-time applications**: Fast response times for interactive user experiences with near-frontier performance
* **High-volume intelligent processing**: Cost-effective intelligence at scale with improved speed
* **Cost-sensitive deployments**: Near-frontier performance at lower price points
* **Sub-agent architectures**: Fast, intelligent agents for multi-agent systems
* **Computer use at scale**: Cost-effective autonomous desktop and browser automation
* **Tasks requiring speed**: When low latency is critical while maintaining near-frontier intelligence

### Extended thinking recommendations

Claude 4 models, particularly Sonnet and Haiku 4.5, show significant performance improvements when using [extended thinking](/en/docs/build-with-claude/extended-thinking) for coding and complex reasoning tasks. Extended thinking is **disabled by default** but we recommend enabling it for demanding work.

**Important**: Extended thinking impacts [prompt caching](/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks) efficiency. When non-tool-result content is added to a conversation, thinking blocks are stripped from cache, which can increase costs in multi-turn conversations. We recommend enabling thinking when the performance benefits outweigh the caching trade-off.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
