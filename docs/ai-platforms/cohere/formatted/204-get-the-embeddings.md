---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## get the embeddings

phrases = ["i love soup", "soup is my favorite", "london is far away"]

model = "embed-v4.0"
input_type = "search_query"

res = co.embed(
    texts=phrases,
    model=model,
    input_type=input_type,
    output_dimension=1024,
    embedding_types=["float"],
)

(soup1, soup2, london) = res.embeddings.float


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
