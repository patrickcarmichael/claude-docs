---
title: "Langgraph: Option 1: Bind output as tool"
description: "Option 1: Bind output as tool section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Option 1: Bind output as tool


Let's now examine how we would use the single LLM option.

### Define Graph

The graph definition is very similar to the one above, the only difference is we no longer call an LLM in the `response` node, and instead bind the `WeatherResponse` tool to our LLM that already contains the `get_weather` tool.

```python
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

tools = [get_weather, WeatherResponse]

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Inherit 'messages' key from MessagesState, which is a list of chat messages](./218-inherit-messages-key-from-messagesstate-which-is-a.md)

**Next:** [Force the model to use tools by passing tool_choice="any" →](./220-force-the-model-to-use-tools-by-passing-tool_choic.md)
