---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use with Fireworks Build SDK

llm = LLM(model="llama-v3p1-70b-instruct", deployment_type="auto")

response = llm.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
)
```

### Smart timestamp handling

When you need to provide current time information, consider these strategies:

**Option 1: Rounded timestamps**
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
