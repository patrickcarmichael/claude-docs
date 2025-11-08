---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Helicone

*Helicone is an open source LLM observability platform.*

Here's some sample code to get started with using Helicone + Together AI:
```python
import os
from together import Together

client = Together(
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://together.hconeai.com/v1",
    supplied_headers={
        "Helicone-Auth": f"Bearer {os.environ.get('HELICONE_API_KEY')}",
    },
)

stream = client.chat.completions.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[
        {
            "role": "user",
            "content": "What are some fun things to do in New York?",
        }
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
