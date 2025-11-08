---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Calculate cosine similarity between the query embedding and each movie embedding

similarity_scores = cosine_similarity([query_embedding], embeddings)
```
We get a similarity score for each of our 1000 movies - the higher the score, the more similar the movie is to the query.

We can sort this similarity score to get the movies most similar to our query = `super hero action movie with a timeline twist`
```py

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
