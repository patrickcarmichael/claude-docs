---
title: "Langgraph: Starting Points for Resuming Workflows"
description: "Starting Points for Resuming Workflows section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Starting Points for Resuming Workflows


- If you're using a [StateGraph (Graph API)](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.StateGraph), the starting point is the beginning of the [**node**](./low_level.md#nodes) where execution stopped.
- If you're making a subgraph call inside a node, the starting point will be the **parent** node that called the subgraph that was halted.
  Inside the subgraph, the starting point will be the specific [**node**](./low_level.md#nodes) where execution stopped.
- If you're using the Functional API, the starting point is the beginning of the [**entrypoint**](./functional_api.md#entrypoint) where execution stopped.

---

concepts/langgraph_data_plane.md

---

---

search:
  boost: 2

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Resuming Workflows](./419-resuming-workflows.md)

**Next:** [LangGraph Data Plane →](./421-langgraph-data-plane.md)
