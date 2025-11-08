---
title: "Langgraph: LangGraph runtime"
description: "LangGraph runtime section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# LangGraph runtime


[Pregel](https://langchain-ai.github.io/langgraph/reference/pregel/) implements LangGraph's runtime, managing the execution of LangGraph applications.

Compiling a [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.StateGraph) or creating an [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) produces a [Pregel](https://langchain-ai.github.io/langgraph/reference/pregel/) instance that can be invoked with input.

This guide explains the runtime at a high level and provides instructions for directly implementing applications with Pregel.

> **Note:** The [Pregel](https://langchain-ai.github.io/langgraph/reference/pregel/) runtime is named after [Google's Pregel algorithm](https://research.google/pubs/pub37252/), which describes an efficient method for large-scale parallel computation using graphs.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Rollback](./255-rollback.md)

**Next:** [Overview →](./257-overview.md)
