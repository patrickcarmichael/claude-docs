---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Summary

""".strip()
```
```python PYTHON
short_text = text_rank(long_text, MAX_TOKENS, 5)
prompt = prompt_template.format(document=short_text)
print(generate_response(message=prompt, max_tokens=600))
```
```txt title="Output"
The document outlines the requirements and obligations for developing and deploying AI systems in the European Union. It aims to establish a regulatory framework to foster innovation while ensuring the protection of fundamental rights and public interests. The regulation applies to providers and deployers of AI systems, including those established outside the EU. High-risk AI systems are subject to specific requirements, such as risk management, data governance, and transparency. Providers must ensure compliance and keep records, and deployers must use AI systems responsibly. The regulation also establishes an AI Office, advisory bodies, and a database for high-risk AI systems. Additionally, it addresses issues like testing, codes of conduct, and cooperation with third countries. Fines and penalties are proposed for non-compliance.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
