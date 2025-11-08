---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate the response by streaming it

response = co.chat_stream(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)

for event in response:
    if event:
        if event.type == "content-delta":
            print(event.delta.message.content.text, end="")
```
```
"Hi, I'm [Your Name] and I'm thrilled to join the Co1t team today as a [Your Role], passionate about [Your Expertise], and excited to contribute to our shared mission of [Startup's Mission]!"
```
Further reading:

* [Documentation on streaming responses](https://docs.cohere.com/docs/streaming)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
