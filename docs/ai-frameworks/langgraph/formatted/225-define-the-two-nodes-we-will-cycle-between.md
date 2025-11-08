---
title: "Langgraph: Define the two nodes we will cycle between"
description: "Define the two nodes we will cycle between section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Define the two nodes we will cycle between

workflow.add_node("agent", call_model)
workflow.add_node("respond", respond)
workflow.add_node("tools", ToolNode(tools))

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define a new graph](./224-define-a-new-graph.md)

**Next:** [Set the entrypoint as `agent` →](./226-set-the-entrypoint-as-agent.md)
