---
title: "Langgraph: Prebuilt implementations"
description: "Prebuilt implementations section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Prebuilt implementations


LangGraph comes with prebuilt implementations of two of the most popular multi-agent architectures:

- [supervisor](../agents/multi-agent.md#supervisor) — individual agents are coordinated by a central supervisor agent. The supervisor controls all communication flow and task delegation, making decisions about which agent to invoke based on the current context and task requirements. You can use [`langgraph-supervisor`](https://github.com/langchain-ai/langgraph-supervisor-py) library to create a supervisor multi-agent systems.
- [swarm](../agents/multi-agent.md#supervisor) — agents dynamically hand off control to one another based on their specializations. The system remembers which agent was last active, ensuring that on subsequent interactions, the conversation resumes with that agent. You can use [`langgraph-swarm`](https://github.com/langchain-ai/langgraph-swarm-py) library to create a swarm multi-agent systems.

---

how-tos/run-id-langsmith.md

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Multi-turn conversation](./119-multi-turn-conversation.md)

**Next:** [How to pass custom run ID or set tags and metadata for graph runs in LangSmith →](./121-how-to-pass-custom-run-id-or-set-tags-and-metadata.md)
