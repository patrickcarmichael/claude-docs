---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## RAG Pipeline \[#sec\_step3]

With our database in place, we can run queries against it. The query process can be broken down into the following steps:

* augment the query, this really helps retrieve all the relevant information
* use each augmented query to retrieve the top k docs and then rerank them
* concatenate all the shortlisted/reranked docs and pass them to the generation model
```python PYTHON
def process_query(query, retriever):
    """Runs query augmentation, retrieval, rerank and final generation in one call."""
    augmented_queries=co.chat(message=query,model='command-a-03-2025',temperature=0.2, search_queries_only=True)
        #augment queries
    if augmented_queries.search_queries:
        reranked_docs=[]
        for itm in augmented_queries.search_queries:
            docs=retriever.invoke(itm.text)
            temp_rerank = rerank_cohere(itm.text,docs)
            reranked_docs.extend(temp_rerank)
        documents = [{"title": f"chunk {i}", "snippet": reranked_docs[i]} for i in range(len(reranked_docs))]
    else:
        #no queries will be run through RAG
        documents = None

    preamble = """

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
