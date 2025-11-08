---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Sample event

type='citation-start' index=0 delta=CitationStartEventDelta(message=CitationStartEventDeltaMessage(citations=Citation(start=14, end=29, text='gym memberships', sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'})])))
```

#### citation-end

Emitted to indicate the end of a citation. If there are multiple citations generated, the events will come as a sequence of `citation-start` and `citation-end` pairs.

#### content-end

Same as in a basic chat stream event.

#### message-end

Same as in a basic chat stream event.

### Tool Use Stream Events (For Tool Calling)

#### message-start

Same as in a basic chat stream event.

#### tool-plan-delta

Emitted when the next token of the tool plan is generated.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
