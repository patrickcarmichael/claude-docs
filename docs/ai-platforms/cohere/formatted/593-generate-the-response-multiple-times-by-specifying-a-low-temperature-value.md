---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate the response multiple times by specifying a low temperature value

for idx in range(3):
    response = co.chat(
        model="command-a-03-2025",
        messages=[{"role": "user", "content": message}],
        temperature=0,
    )

    print(f"{idx+1}: {response.message.content[0].text}\n")
```
```
1: "Revolution Enthusiast"

2: "Revolution Enthusiast"

3: "Revolution Enthusiast"
```
And here's an example of setting `temperature` to 1.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
