---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 3: Format as data URL

data_url = f"data:image/jpeg;base64,{encoded_string}"

example_doc = [
    {"type": "text", "text": "This is a Scottish Fold Cat"},
    {"type": "image_url", "image_url": {"url": data_url}},
]  # This is where we're fusing text and images.

res = co.embed(
    model="embed-v4.0",
    inputs=[{"content": example_doc}],
    input_type="search_document",
    embedding_types=["float"],
    output_dimension=1024,
).embeddings.float_

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
