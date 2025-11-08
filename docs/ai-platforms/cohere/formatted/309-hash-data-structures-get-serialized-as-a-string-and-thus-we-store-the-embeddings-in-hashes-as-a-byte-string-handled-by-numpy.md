---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## hash data structures get serialized as a string and thus we store the embeddings in hashes as a byte string (handled by numpy)

res = cohere_vectorizer.embed_many(
    text_to_embed, input_type="search_document", as_buffer=True
)
```
We will be loading a subset of data which contains paragraphs from wikipedia - the data lives in a `jsonl` and we will need to parse it to get the text field which is what we are embedding. To do this, we load the file and read it line-by-line, creating a corpus object and a text\_to\_embed object. We then pass the text\_to\_embed object into `co.embed_many` which takes in an list of strings.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
