---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Helper function to generate text

Now, let's define a function to generate text using the Command R+ model on Bedrock. We’ll use this function a few times throughout.

This function takes a user message and generates the response via the chat endpoint. Note that we don't need to specify the model as we have already set it up in the client.
```python PYTHON
def generate_text(message):
    response = co.chat(
        model="model",  # Pass a dummy string

        messages=[{"role": "user", "content": message}],
    )
    return response
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
