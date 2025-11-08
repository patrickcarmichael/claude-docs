---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 3: Embedding Generation with Cohere

```python
from tqdm import tqdm


def get_embedding(
    text: str, input_type: str = "search_document"
) -> list[float]:
    if not text.strip():
        print("Attempted to get embedding for empty text.")
        return []

    model = "embed-v4.0"
    response = co.embed(
        texts=[text],
        model=model,
        input_type=input_type,  # Used for embeddings of search queries run against a vector DB to find relevant documents

        embedding_types=["float"],
    )

    return response.embeddings.float[0]


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
