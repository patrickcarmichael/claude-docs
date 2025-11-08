---
title: "Langgraph: Supported stream modes"
description: "Supported stream modes section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Supported stream modes


Pass one or more of the following stream modes as a list to the [`stream()`](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.CompiledStateGraph.stream) or [`astream()`](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.CompiledStateGraph.astream) methods:

| Mode       | Description                                                                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `values`   | Streams the full value of the state after each step of the graph.                                                                                                                   |
| `updates`  | Streams the updates to the state after each step of the graph. If multiple updates are made in the same step (e.g., multiple nodes are run), those updates are streamed separately. |
| `custom`   | Streams custom data from inside your graph nodes.                                                                                                                                   |
| `messages` | Streams 2-tuples (LLM token, metadata) from any graph nodes where an LLM is invoked.                                                                                                |
| `debug`    | Streams as much information as possible throughout the execution of the graph.                                                                                                      |

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Stream outputs](./74-stream-outputs.md)

**Next:** [Stream from an agent →](./76-stream-from-an-agent.md)
