---
title: "Langgraph: Assistants"
description: "Assistants section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Assistants


**Assistants** allow you to manage configurations (like prompts, LLM selection, tools) separately from your graph's core logic, enabling rapid changes that don't alter the graph architecture. It is a way to create multiple specialized versions of the same graph architecture, each optimized for different use cases through context/configuration variations rather than structural changes.

For example, imagine a general-purpose writing agent built on a common graph architecture. While the structure remains the same, different writing styles—such as blog posts and tweets—require tailored configurations to optimize performance. To support these variations, you can create multiple assistants (e.g., one for blogs and another for tweets) that share the underlying graph but differ in model selection and system prompt.

![assistant versions](img/assistants.png)

The LangGraph Cloud API provides several endpoints for creating and managing assistants and their versions. See the [API reference](../cloud/reference/api/api_ref.html#tag/assistants) for more details.

!!! info

    Assistants are a [LangGraph Platform](langgraph_platform.md) concept. They are not available in the open source LangGraph library.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Add thread-level persistence](./243-add-thread-level-persistence.md)

**Next:** [Configuration →](./245-configuration.md)
