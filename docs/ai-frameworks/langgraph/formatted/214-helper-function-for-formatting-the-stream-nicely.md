---
title: "Langgraph: Helper function for formatting the stream nicely"
description: "Helper function for formatting the stream nicely section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Helper function for formatting the stream nicely

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {"messages": [("user", "what is the weather in sf")]}
print_stream(graph.stream(inputs, stream_mode="values"))
```
```output
================================ Human Message =================================

what is the weather in sf
================================== Ai Message ==================================
Tool Calls:
  get_weather (call_azW0cQ4XjWWj0IAkWAxq9nLB)
 Call ID: call_azW0cQ4XjWWj0IAkWAxq9nLB
  Args:
    location: San Francisco
================================= Tool Message =================================
Name: get_weather

"It's sunny in San Francisco, but you better look out if you're a Gemini \ud83d\ude08."
================================== Ai Message ==================================

The weather in San Francisco is sunny! However, it seems there's a playful warning for Geminis. Enjoy the sunshine!
```python
Perfect! The graph correctly calls the `get_weather` tool and responds to the user after receiving the information from the tool.

---

how-tos/react-agent-structured-output.ipynb

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use ReAct agent](./213-use-react-agent.md)

**Next:** [How to force tool-calling agent to structure output →](./215-how-to-force-tool-calling-agent-to-structure-outpu.md)
