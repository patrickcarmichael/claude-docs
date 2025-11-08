---
title: "Langgraph: Functional API vs. Graph API"
description: "Functional API vs. Graph API section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Functional API vs. Graph API


For users who prefer a more declarative approach, LangGraph's [Graph API](./low_level.md) allows you to define workflows using a Graph paradigm. Both APIs share the same underlying runtime, so you can use them together in the same application.

Here are some key differences:

- **Control flow**: The Functional API does not require thinking about graph structure. You can use standard Python constructs to define workflows. This will usually trim the amount of code you need to write.
- **Short-term memory**: The **GraphAPI** requires declaring a [**State**](./low_level.md#state) and may require defining [**reducers**](./low_level.md#reducers) to manage updates to the graph state. `@entrypoint` and `@tasks` do not require explicit state management as their state is scoped to the function and is not shared across functions.
- **Checkpointing**: Both APIs generate and use checkpoints. In the **Graph API** a new checkpoint is generated after every [superstep](./low_level.md). In the **Functional API**, when tasks are executed, their results are saved to an existing checkpoint associated with the given entrypoint instead of creating a new checkpoint.
- **Visualization**: The Graph API makes it easy to visualize the workflow as a graph which can be useful for debugging, understanding the workflow, and sharing with others. The Functional API does not support visualization as the graph is dynamically generated during runtime.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overview](./309-overview.md)

**Next:** [Example →](./311-example.md)
