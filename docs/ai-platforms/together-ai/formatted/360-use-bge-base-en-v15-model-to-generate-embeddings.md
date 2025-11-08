---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use bge-base-en-v1.5 model to generate embeddings

embeddings = generate_embeddings(to_embed, "BAAI/bge-base-en-v1.5")
```

Next we implement a function that when given the above embeddings and a test query will return indices of most semantically similar data objects:
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

We will use the above function to retrieve 25 movies most similar to our query:
```py
indices = retrieve(
    query="super hero mystery action movie about bats",
    top_k=25,
    index=embeddings,
)
```

This will give us the following movie indices and movie titles:
```
array([ 13, 265, 451,  33,  56,  17, 140, 450,  58, 828, 227,  62, 337,
       172, 724, 424, 585, 696, 933, 996, 932, 433, 883, 420, 744])
```
```py

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
