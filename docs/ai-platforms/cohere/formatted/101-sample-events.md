---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Sample events

type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='A')))

type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' large')))

type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' language')))

...
```

#### content-end

The event that indicates the end of the content block of the message. Only one `content-end` event will be emitted.

#### message-end

The final event in the stream indicating the end of the streamed response. Only one `message-end` event will be emitted.

### Retrieval Augmented Generation Stream Events

#### message-start

Same as in a basic chat stream event.

#### content-start

Same as in a basic chat stream event.

#### content-delta

Same as in a basic chat stream event.

#### citation-start

Emitted for every citation generated in the response.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
