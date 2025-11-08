---
title: "Langgraph: What does "nodes executed" mean for LangGraph Platform usage?"
description: "What does "nodes executed" mean for LangGraph Platform usage? section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## What does "nodes executed" mean for LangGraph Platform usage?


**Nodes Executed** is the aggregate number of nodes in a LangGraph application that are called and completed successfully during an invocation of the application. If a node in the graph is not called during execution or ends in an error state, these nodes will not be counted. If a node is called and completes successfully multiple times, each occurrence will be counted.

---

concepts/mcp.md

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Can I use LangGraph Studio without logging in to LangSmith](./378-can-i-use-langgraph-studio-without-logging-in-to-l.md)

**Next:** [MCP →](./380-mcp.md)
