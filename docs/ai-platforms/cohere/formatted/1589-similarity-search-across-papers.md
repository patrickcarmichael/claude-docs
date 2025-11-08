---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Similarity Search Across Papers

Next, we'll expand on the functionality we've built so far to make it possible to find papers related to a user-provided query.

As before, we'll begin by defining our `get_similarity` function. It takes a `target` query and compares it to `candidates` to return the most relevant papers.
```python PYTHON
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(target,candidates):
  # Turn list into array

  candidates = np.array(candidates)
  target = np.expand_dims(np.array(target),axis=0)

  # Calculate cosine similarity

  sim = cosine_similarity(target,candidates)
  sim = np.squeeze(sim).tolist()
  sort_index = np.argsort(sim)[::-1]
  sort_score = [sim[i] for i in sort_index]
  similarity_scores = zip(sort_index,sort_score)

  # Return similarity scores

  return similarity_scores
```
All we need now is to feed it a query and print out the top papers:
```python PYTHON 

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
