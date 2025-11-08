---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## user turn 1

messages.append(
    {
        "role": "user",
        "content": "I'm joining a new startup called Co1t today. Could you help me write a short introduction message to my teammates.",
    },
)
response = co.chat(
    model="command-a-03-2025",
    messages=messages,
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
