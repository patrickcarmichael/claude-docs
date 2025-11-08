---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multilingual Support

`embed-v4.0` is a best-in-class best-in-class multilingual model with support for over 100 languages, including Korean, Japanese, Arabic, Chinese, Spanish, and French.
```python PYTHON
import cohere

co = cohere.ClientV2(api_key="YOUR_API_KEY")

texts = [
    "Hello from Cohere!",
    "مرحبًا من كوهير!",
    "Hallo von Cohere!",
    "Bonjour de Cohere!",
    "¡Hola desde Cohere!",
    "Olá do Cohere!",
    "Ciao da Cohere!",
    "您好，来自 Cohere！",
    "कोहेरे से नमस्ते!",
]

response = co.embed(
    model="embed-v4.0",
    texts=texts,
    input_type="classification",
    output_dimension=1024,
    embedding_types=["float"],
)

embeddings = response.embeddings.float  # All text embeddings

print(embeddings[0][:5])  # Print embeddings for the first text

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
