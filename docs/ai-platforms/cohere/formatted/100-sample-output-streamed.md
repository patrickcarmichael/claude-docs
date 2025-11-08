---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Sample output (streamed)

A large language model (LLM) is a type of artificial neural network model that has been trained on massive amounts of text data ...
```
The following sections describe the different types of events that are emitted during a streaming session.

### Basic Chat Stream Events

#### message-start

The first event in the stream containing metadata for the request such as the `id`. Only one `message-start` event will be emitted.

#### content-start

The event that indicates the start of the content block of the message. Only one `content-start` event will be emitted.

#### content-delta

The event that is emitted whenever the next chunk of text comes back from the model. As the model continues generating text, multiple events of this type will be emitted. Each event generates one token through the `delta.message.content.text` field.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
