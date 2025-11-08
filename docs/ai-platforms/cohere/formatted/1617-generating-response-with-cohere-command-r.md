---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating response with Cohere Command R

response = co.chat(
    message=query,
    documents=format_documents_for_chat(reranked_documents),
    model="command-a-03-2025",
    temperature=0.3,
)

print("Final answer:")
print(response.text)
```
Final answer:
Here is an overview of the companies with negative market reports or sentiment that might deter long-term investment:

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
