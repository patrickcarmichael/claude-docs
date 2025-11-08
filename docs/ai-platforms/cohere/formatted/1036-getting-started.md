---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Started

The model is available immediately through Cohere's Chat API endpoint. You can start translating text with simple prompts or integrate it programmatically into your applications.
```python
from cohere import ClientV2

co = ClientV2(api_key="<YOUR API KEY>")

response = co.chat(
    model="command-a-translate-08-2025",
    messages=[
        {
            "role": "user",
            "content": "Translate this text to Spanish: Hello, how are you?",
        }
    ],
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
