---
title: "Langgraph: Tool calling"
description: "Tool calling section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Tool calling


![Diagram of a tool call by a model](./img/tool_call.png)

Tool calling is typically **conditional**. Based on the user input and available tools, the model may choose to issue a tool call request. This request is returned in an `AIMessage` object, which includes a `tool_calls` field that specifies the tool name and input arguments:

```python
llm_with_tools.invoke("What is 2 multiplied by 3?")

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Tools](./271-tools.md)

**Next:** [-> AIMessage(tool_calls=[{'name': 'multiply', 'args': {'a': 2, 'b': 3}, ...}]) →](./273-aimessagetool_callsname-multiply-args-a-2-b-3.md)
