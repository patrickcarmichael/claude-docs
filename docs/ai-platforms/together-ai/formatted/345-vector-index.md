---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Vector Index

We will now use `bge-large-en-v1.5` to embed the augmented chunks above into a vector index.
```py
from typing import List
import together
import numpy as np


def generate_embeddings(
    input_texts: List[str],
    model_api_string: str,
) -> List[List[float]]:
    """Generate embeddings from Together python library.

    Args:
        input_texts: a list of string input texts.
        model_api_string: str. An API string for a specific embedding model of your choice.

    Returns:
        embeddings_list: a list of embeddings. Each element corresponds to the each input text.
    """
    outputs = client.embeddings.create(
        input=input_texts,
        model=model_api_string,
    )
    return [x.embedding for x in outputs.data]


contextual_embeddings = generate_embeddings(
    contextual_chunks,
    "BAAI/bge-large-en-v1.5",
)
```

Next we need to write a function that can retrieve the top matching chunks from this index given a query:
```py
def vector_retrieval(
    query: str,
    top_k: int = 5,
    vector_index: np.ndarray = None,
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

    query_embedding = generate_embeddings([query], "BAAI/bge-large-en-v1.5")[0]
    similarity_scores = cosine_similarity([query_embedding], vector_index)

    return list(np.argsort(-similarity_scores)[0][:top_k])


vector_retreival(
    query="What are 'skip-level' meetings?",
    top_k=5,
    vector_index=contextual_embeddings,
)
```

We now have a way to retrieve from the vector index given a query.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
