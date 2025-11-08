---
title: "Langgraph: Configuration"
description: "Configuration section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Configuration


Assistants build on the LangGraph open source concepts of configuration and [runtime context](low_level.md#runtime-context).

While these features are available in the open source LangGraph library, assistants are only present in [LangGraph Platform](langgraph_platform.md). This is due to the fact that assistants are tightly coupled to your deployed graph. Upon deployment, LangGraph Server will automatically create a default assistant for each graph using the graph's default context and configuration settings.

In practice, an assistant is just an _instance_ of a graph with a specific configuration. Therefore, multiple assistants can reference the same graph but can contain different configurations (e.g. prompts, models, tools). The LangGraph Server API provides several endpoints for creating and managing assistants. See the [API reference](../cloud/reference/api/api_ref.html) and [this how-to](../cloud/how-tos/configuration_cloud.md) for more details on how to create assistants.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Assistants](./244-assistants.md)

**Next:** [Versioning →](./246-versioning.md)
