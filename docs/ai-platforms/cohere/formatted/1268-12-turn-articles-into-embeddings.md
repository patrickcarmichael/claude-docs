---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1.2: Turn articles into embeddings

Next we turn each article text into embeddings. An [embedding](https://docs.cohere.ai/embedding-wiki) is a list of numbers that our models use to represent a piece of text, capturing its context and meaning.

We do this by calling Cohere's [Embed endpoint](https://docs.cohere.ai/embed-reference), which takes in text as input and returns embeddings as output.
```python PYTHON
articles = df_inputs['Text'].tolist()

output = co.embed(
            model ='embed-v4.0',
            input_type='search_document',
            texts = articles)
embeds = output.embeddings

print('Number of articles:', len(embeds))
```
```
Number of articles: 100
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
