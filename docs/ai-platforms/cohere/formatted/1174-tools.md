---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tools

Following functions and tools will be used in the subsequent tasks.
```python PYTHON
def retrieve_documents(query: str, n=1) -> dict:
    """
    Function to retrieve documents a given query.

    Steps:
    1. Embed the query
    2. Calculate cosine similarity between the query embedding and the embeddings of the documents
    3. Return the top n documents with the highest similarity scores
    """
    query_emb = co.embed(
        texts=[query], model="embed-v4.0", input_type="search_query"
    )

    similarity_scores = cosine_similarity(
        [query_emb.embeddings[0]], db.embeddings.tolist()
    )
    similarity_scores = similarity_scores[0]

    top_indices = similarity_scores.argsort()[::-1][:n]
    top_matches = db.iloc[top_indices]

    return {"top_matched_document": top_matches.combined}


functions_map = {
    "retrieve_documents": retrieve_documents,
}

tools = [
    {
        "name": "retrieve_documents",
        "description": "given a query, retrieve documents from a database to answer user's question",
        "parameter_definitions": {
            "query": {"description": "query", "type": "str", "required": True}
        },
    }
]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
