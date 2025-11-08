---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Response content

* v1: Accessed via `text`
* v2: Accessed via `message.content[0].text`

**v1**
```python PYTHON
res = co_v1.chat(model="command-a-03-2025", message="What is 2 + 2")

print(res.text)
```
```
The answer is 4.
```
**v2**
```python PYTHON
res = co_v2.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": "What is 2 + 2"}],
)

print(res.message.content[0].text)
```
```
The answer is 4.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
