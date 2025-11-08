---
title: "Langgraph: Next steps"
description: "Next steps section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Next steps


This guide provides a minimal implementation for dynamically selecting tools. There is a host of possible improvements and optimizations:

- **Repeating tool selection**: Here, we repeated tool selection by modifying the `select_tools` node. Another option is to equip the agent with a `reselect_tools` tool, allowing it to re-select tools at its discretion.
- **Optimizing tool selection**: In general, the full scope of [retrieval solutions](https://python.langchain.com/docs/concepts/#retrieval) are available for tool selection. Additional options include:
  - Group tools and retrieve over groups;
  - Use a chat model to select tools or groups of tool.

---

how-tos/react-agent-from-scratch.ipynb

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Repeating tool selection](./199-repeating-tool-selection.md)

**Next:** [How to create a ReAct agent from scratch →](./201-how-to-create-a-react-agent-from-scratch.md)
