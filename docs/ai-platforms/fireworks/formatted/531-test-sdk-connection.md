---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Test SDK connection

llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="serverless")

response = llm.chat.completions.create(
    messages=[{"role": "user", "content": "Hello! Can you help me learn about AI?"}]
)

print("SDK Connection Test:")
print(response.choices[0].message.content)
```typescript
**What's Happening Here:**

* Fireworks SDK: Simplified interface for model deployment and fine-tuning
* Serverless Models: Pre-deployed models you can use immediately
* API Key: Authenticates your requests and tracks usage

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
