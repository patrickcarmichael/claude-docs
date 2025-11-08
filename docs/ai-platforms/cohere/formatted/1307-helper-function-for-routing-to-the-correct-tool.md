---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## helper function for routing to the correct tool

def invoke_tool(tool_call: cohere.ToolCall):
  if tool_call.name == list_calendar_events_tool["name"]:
    date = tool_call.parameters["date"]
    return [{
        "events": list_calendar_events(date)
    }]
  elif tool_call.name == create_calendar_event_tool["name"]:
    date = tool_call.parameters["date"]
    time = tool_call.parameters["time"]
    duration = tool_call.parameters["duration"]

    return [{
        "is_success": create_calendar_event(date, time, duration)
    }]
  else:
    raise f"Unknown tool name '{tool_call.name}'"
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
