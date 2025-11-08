---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 💻 Getting Started

The API structure is identical to our existing Command models, making integration straightforward:
```python
import cohere

co = cohere.Client("your-api-key")

response = co.chat(
    model="command-a-vision-07-2025",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Analyze this chart and extract the key data points",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "your-image-url"},
                },
            ],
        }
    ],
)
```
There's much more to be said about working with images, various limitations, and best practices, which you can find in our dedicated [Command A Vision](https://docs.cohere.com/docs/command-a-vision) and [Image Inputs](https://docs.cohere.com/docs/image-inputs) documents.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
