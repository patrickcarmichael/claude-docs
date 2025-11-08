---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Sample events

type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(tool_plan=None, message={'tool_plan': 'I'})

type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(tool_plan=None, message={'tool_plan': ' will'})

type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(tool_plan=None, message={'tool_plan': ' use'})

...
```

#### tool-call-start

Emitted when the model generates tool calls that require actioning upon. The event contains a list of `tool_calls` containing the tool name and tool call ID of the tool.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
