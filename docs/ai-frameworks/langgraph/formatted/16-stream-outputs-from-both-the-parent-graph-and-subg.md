---
title: "Langgraph: stream outputs from both the parent graph and subgraph"
description: "stream outputs from both the parent graph and subgraph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# stream outputs from both the parent graph and subgraph

for chunk in graph.stream({
    "messages": [{"role": "user", "content": "what's the weather in sf"}]
}, subgraphs=True):
    print(chunk)
```

---

how-tos/autogen-integration.md

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← invoke the parent graph](./15-invoke-the-parent-graph.md)

**Next:** [How to integrate LangGraph with AutoGen, CrewAI, and other frameworks →](./17-how-to-integrate-langgraph-with-autogen-crewai-and.md)
