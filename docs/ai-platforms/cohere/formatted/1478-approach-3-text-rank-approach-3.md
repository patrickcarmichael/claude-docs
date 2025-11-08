---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Approach 3: Text rank \[#approach-3]

In the final section we will show how we leverage graph theory to select chunks based on their centrality. Centrality is a graph-theoretic measure of how connected a node is; the higher the centrality, the more connected the node is to surrounding nodes (with fewer connections among those neighbors).

The solution presented in this document can be broken down into five functional steps:

1. Break the document into chunks.

   * This mirrors the first step in [Approach 2](#approach-2).

2. Embed each chunk using an embedding model and construct a similarity matrix.

   * We utilize `co.embed` [documentation link](https://docs.cohere.com/reference/embed).

3. Compute the centrality of each chunk.

   * We employ a package called [`NetworkX`](https://networkx.org/documentation/networkx-1.10/overview.html). It constructs a graph where the chunks are nodes, and the similarity score between them serves as the weight of the edges. Then, we calculate the centrality of each chunk as the sum of the edge weights adjacent to the node representing that chunk.

4. Retain the highest-centrality chunks until the context limit is reached.

   * This step follows a similar approach to [Approach 2](#approach-2).

5. Reassemble the shortened text by reordering chunks in their original order.
   * This step mirrors the last step in [Approach 2](#approach-2).

See `text_rank` as the starting point.

### Text rank implementation

```python PYTHON
def text_rank(text: str, max_tokens: int, n_setences_per_passage: int) -> str:
    """
    Shortens text by extracting key units of text from it based on their centrality.
    The output is the concatenation of those key units, in their original order.
    """

    # 1. Chunk text into units

    chunks = build_simple_chunks(text, n_setences_per_passage)

    # 2. Embed and construct similarity matrix

    embeddings = np.array(
        co.embed(
            texts=chunks,
            model="embed-v4.0",
            input_type="clustering",
        ).embeddings
    )
    similarities = np.dot(embeddings, embeddings.T)

    # 3. Compute centrality and sort sentences by centrality

    # Easiest to use networkx's `degree` function with similarity as weight

    g = nx.from_numpy_array(similarities, edge_attr="weight")
    centralities = g.degree(weight="weight")
    idcs_sorted_by_centrality = [node for node, degree in sorted(centralities, key=lambda item: item[1], reverse=True)]

    # 4. Add chunks back in order of centrality

    selected = _add_chunks_by_priority(chunks, idcs_sorted_by_centrality, max_tokens)

    # 5. Put condensed text back in original order

    short = " ".join([chunk for index, chunk in sorted(selected, key=lambda item: item[0], reverse=False)])

    return short
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
