---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate the response

res_v2 = co_v2.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
    documents=documents_v2,
)

print(res_v2.message.content[0].text)
```
```
Yes, we offer gym memberships, on-site yoga classes, and comprehensive health insurance.
```
The following is a list of the the different options for structuring documents for RAG in v2.
```python PYTHON
documents_v2 = [
    # List of objects with data string

    {
        "id": "123",
        "data": "I love penguins. they are fluffy",
    },
    # List of objects with data object

    {
        "id": "456",
        "data": {
            "text": "I love penguins. they are fluffy",
            "author": "Abdullah",
            "create_date": "09021989",
        },
    },
    # List of strings

    "just a string",
]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
