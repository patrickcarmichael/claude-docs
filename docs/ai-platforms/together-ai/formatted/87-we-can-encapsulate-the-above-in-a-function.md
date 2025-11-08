---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## We can encapsulate the above in a function

```py
def retrieve(
    query: str,
    top_k: int = 5,
    index: np.ndarray = None,
) -> List[int]:
    """
    Retrieve the top-k most similar items from an index based on a query.
    Args:
        query (str): The query string to search for.
        top_k (int, optional): The number of top similar items to retrieve. Defaults to 5.
        index (np.ndarray, optional): The index array containing embeddings to search against. Defaults to None.
    Returns:
        List[int]: A list of indices corresponding to the top-k most similar items in the index.
    """

    query_embedding = generate_embeddings([query], "BAAI/bge-base-en-v1.5")[0]
    similarity_scores = cosine_similarity([query_embedding], index)

    return np.argsort(-similarity_scores)[0][:top_k]
```
Which can be used as follows:
```py
retrieve(
    "super hero action movie with a timeline twist",
    top_k=5,
    index=embeddings,
)
```
Which returns an array of indices for movies that best match the query.
```
array([172, 265, 768, 621, 929])
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
