---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate the response

response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)

print(response.message.content[0].text)
```
```
Ticket title: "Server Access Permissions Issue"
```
Further reading:

* [Documentation on prompt engineering](https://docs.cohere.com/docs/crafting-effective-prompts)
* [LLM University module on prompt engineering](https://cohere.com/llmu#prompt-engineering)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
