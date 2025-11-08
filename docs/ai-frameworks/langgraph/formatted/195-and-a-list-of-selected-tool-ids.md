---
title: "Langgraph: and a list of selected tool IDs."
description: "and a list of selected tool IDs. section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# and a list of selected tool IDs.

class State(TypedDict):
    messages: Annotated[list, add_messages]
    selected_tools: list[str]

builder = StateGraph(State)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define the state structure using TypedDict.](./194-define-the-state-structure-using-typeddict.md)

**Next:** [Retrieve all available tools from the tool registry. →](./196-retrieve-all-available-tools-from-the-tool-registr.md)
