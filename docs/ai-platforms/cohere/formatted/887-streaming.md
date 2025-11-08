---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming

* Events containing content:
  * v1: `chunk.event_type == "text-generation"`
  * v2: `chunk.type == "content-delta"`

* Accessing response content:
  * v1: `chunk.text`
  * v2: `chunk.delta.message.content.text`

**v1**
```python PYTHON
message = "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates."

res = co_v1.chat_stream(model="command-a-03-2025", message=message)

for chunk in res:
    if chunk.event_type == "text-generation":
        print(chunk.text, end="")
```
```
"Hi, I'm [your name] and I'm thrilled to join the Co1t team today as a [your role], eager to contribute my skills and ideas to help drive innovation and success for our startup!"
```
**v2**
```python PYTHON
message = "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates."

res = co_v2.chat_stream(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)

for chunk in res:
    if chunk:
        if chunk.type == "content-delta":
            print(chunk.delta.message.content.text, end="")
```
```
"Hi everyone, I'm thrilled to join the Co1t team today and look forward to contributing my skills and ideas to drive innovation and success!"
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
