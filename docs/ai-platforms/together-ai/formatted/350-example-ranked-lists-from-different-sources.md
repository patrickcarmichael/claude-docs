---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example ranked lists from different sources

vector_top_k = vector_retreival(
    query="What are 'skip-level' meetings?",
    top_k=5,
    vector_index=contextual_embeddings,
)
bm25_top_k = bm25_retreival(
    query="What are 'skip-level' meetings?",
    k=5,
    bm25_index=retriever,
)
```

The Reciprocal Rank Fusion algorithm takes two ranked list of objects and combines them:
```py
from collections import defaultdict


def reciprocal_rank_fusion(*list_of_list_ranks_system, K=60):
    """
    Fuse rank from multiple IR systems using Reciprocal Rank Fusion.

    Args:
    * list_of_list_ranks_system: Ranked results from different IR system.
    K (int): A constant used in the RRF formula (default is 60).

    Returns:
    Tuple of list of sorted documents by score and sorted documents
    """
    # Dictionary to store RRF mapping

    rrf_map = defaultdict(float)

    # Calculate RRF score for each result in each list

    for rank_list in list_of_list_ranks_system:
        for rank, item in enumerate(rank_list, 1):
            rrf_map[item] += 1 / (rank + K)

    # Sort items based on their RRF scores in descending order

    sorted_items = sorted(rrf_map.items(), key=lambda x: x[1], reverse=True)

    # Return tuple of list of sorted documents by score and sorted documents

    return sorted_items, [item for item, score in sorted_items]
```

We can use the RRF function above as follows:
```py

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
