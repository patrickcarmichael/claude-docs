---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Text Generation

You can use this code to invoke either Command R (`cohere.command-r-v1:0`), Command R+ (`cohere.command-r-plus-v1:0`) on Amazon Bedrock:
```python PYTHON
import cohere

co = cohere.BedrockClient(
    aws_region="us-east-1",
    aws_access_key="...",
    aws_secret_key="...",
    aws_session_token="...",
)

result = co.chat(
    message="Write a LinkedIn post about starting a career in tech:",
    model="cohere.command-r-plus-v1:0",  # or 'cohere.command-r-v1:0'

)

print(result)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
