---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Sample events

type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(tool_call=None, message={'tool_calls': {'function': {'arguments': '{\n    "'}}})

type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(tool_call=None, message={'tool_calls': {'function': {'arguments': 'location'}}})

type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(tool_call=None, message={'tool_calls': {'function': {'arguments': '":'}}})

...
```

#### tool-call-end

Emitted when the tool call is finished.

#### message-end

Same as in a basic chat stream event.

### Tool Use Stream Events (For Response Generation)

#### message-start

Same as in a basic chat stream event.

#### content-start

Same as in a basic chat stream event.

#### content-delta

Same as in a basic chat stream event.

#### citation-start

Emitted for every citation generated in the response.

#### citation-end

Emitted to indicate the end of a citation. If there are multiple citations generated, the events will come as a sequence of `citation-start` and `citation-end` pairs.

#### content-end

Same as in a basic chat stream event.

#### message-end

Same as in a basic chat stream event.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
