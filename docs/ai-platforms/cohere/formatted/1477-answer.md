---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Answer

""".strip()
```
```python PYTHON
query = "What does the report say about biometric identification? Answer only based on the document."
short_text = query_based_retrieval(long_text, MAX_TOKENS, query)
prompt = prompt_template.format(query=query, document=short_text)
print(generate_response(message=prompt, max_tokens=300))
```
```txt title="Output"
The report discusses the restrictions on the use of biometric identification by law enforcement in publicly accessible spaces. According to the document, real-time biometric identification is prohibited unless in exceptional cases where its use is strictly necessary and proportionate to achieving a substantial public interest. The use of post-remote biometric identification systems is also mentioned, noting the requirements for authorization and limitations on its use.

The report also highlights the classification of certain AI systems as high-risk, including biometric identification systems, emotion recognition systems, and biometric categorisation systems, with the exception of systems used for biometric verification. High-risk AI systems are subject to specific requirements and obligations.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
