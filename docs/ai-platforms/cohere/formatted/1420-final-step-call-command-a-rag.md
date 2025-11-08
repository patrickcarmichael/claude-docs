---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Final Step: Call Command-A + RAG!

```python PYTHON
"""
Call the /chat endpoint with command-a
"""

response = co.chat(
    message=prompt,
    model="command-a-03-2025",
    documents=reranked_relevant_docs
)

cited_response, citations_reference = insert_citations_in_order(response.text, response.citations, reranked_relevant_docs)
print(cited_response)
print("\n")
print("References:")
print(citations_reference)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
