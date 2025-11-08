---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming

* Event containing content:
  * v1: `chunk.event_type == "text-generation"`
  * v2: `chunk.type == "content-delta"`

* Accessing response content:
  * v1: `chunk.text`
  * v2: `chunk.delta.message.content.text`

* Events containing citations:
  * v1: `chunk.event_type == "citation-generation"`
  * v2: `chunk.type == "citation-start"`

* Accessing citations:
  * v1: `chunk.citations`
  * v2: `chunk.delta.message.citations`

**v1**
```python PYTHON
message = "Are there fitness-related benefits?"

res_v1 = co_v1.chat_stream(
    model="command-a-03-2025",
    message=message,
    documents=documents_v1,
)

for chunk in res_v1:
    if chunk.event_type == "text-generation":
        print(chunk.text, end="")
    if chunk.event_type == "citation-generation":
        print(f"\n{chunk.citations}")
```
```
Yes, we offer gym memberships, on-site yoga classes, and comprehensive health insurance as part of our health and wellness benefits.

[ChatCitation(start=14, end=87, text='gym memberships, on-site yoga classes, and comprehensive health insurance', document_ids=['doc_1'])]

[ChatCitation(start=103, end=132, text='health and wellness benefits.', document_ids=['doc_1'])]
```
**v2**
```python PYTHON
message = "Are there fitness-related benefits?"

messages = [{"role": "user", "content": message}]

res_v2 = co_v2.chat_stream(
    model="command-a-03-2025",
    messages=messages,
    documents=documents_v2,
)

for chunk in res_v2:
    if chunk:
        if chunk.type == "content-delta":
            print(chunk.delta.message.content.text, end="")
        if chunk.type == "citation-start":
            print(f"\n{chunk.delta.message.citations}")
```
```
Yes, we offer gym memberships, on-site yoga classes, and comprehensive health insurance.

start=14 end=88 text='gym memberships, on-site yoga classes, and comprehensive health insurance.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'})]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
