---
title: "Langgraph: Features"
description: "Features section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Features


Key features of LangGraph Studio:

- Visualize your graph architecture
- [Run and interact with your agent](../cloud/how-tos/invoke_studio.md)
- [Manage assistants](../cloud/how-tos/studio/manage_assistants.md)
- [Manage threads](../cloud/how-tos/threads_studio.md)
- [Iterate on prompts](../cloud/how-tos/iterate_graph_studio.md)
- [Run experiments over a dataset](../cloud/how-tos/studio/run_evals.md)
- Manage [long term memory](memory.md)
- Debug agent state via [time travel](time-travel.md)

LangGraph Studio works for graphs that are deployed on [LangGraph Platform](../cloud/quick_start.md) or for graphs that are running locally via the [LangGraph Server](../tutorials/langgraph-platform/local-server.md).

Studio supports two modes:

### Graph mode

Graph mode exposes the full feature-set of Studio and is useful when you would like as many details about the execution of your agent, including the nodes traversed, intermediate states, and LangSmith integrations (such as adding to datasets and playground).

### Chat mode

Chat mode is a simpler UI for iterating on and testing chat-specific agents. It is useful for business users and those who want to test overall agent behavior. Chat mode is only supported for graph's whose state includes or extends [`MessagesState`](https://langchain-ai.github.io/langgraph/how-tos/graph-api/#messagesstate).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← LangGraph Studio](./248-langgraph-studio.md)

**Next:** [Learn more →](./250-learn-more.md)
