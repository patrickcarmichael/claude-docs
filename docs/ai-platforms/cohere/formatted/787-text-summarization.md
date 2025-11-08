---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Text summarization

Another type of use case is text summarization. Now, let's summarize the customer inquiry into a single sentence. We add an instruction to the prompt and then pass the inquiry to the prompt.
```python PYTHON
prompt = f"""Summarize this customer inquiry into one short sentence.

Inquiry: {inquiry}"""

response = generate_text(prompt)

print(response.message.content[0].text)
```
```mdx
A customer is experiencing intermittent slow data speeds on their mobile network several times a day.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
