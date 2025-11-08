---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Build a retriever using Cohere's `rerank`

The vector database we built using `VectorStoreIndex` comes with an in-built retriever. We can call that retriever to fetch the top $k$ documents most relevant to the user question with:
```python PYTHON
retriever = index.as_retriever(similarity_top_k=top_k)
```
We recently released [Rerank-3](https://cohere.com/blog/rerank-3/) (April '24), which we can use to improve the quality of retrieval, as well as reduce latency and the cost of inference. To use the retriever with `rerank`, we create a thin wrapper around `index.as_retriever` as follows:
```python PYTHON
class RetrieverWithRerank:
    def __init__(self, retriever, api_key):
        self.retriever = retriever
        self.co = cohere.Client(api_key=api_key)

    def retrieve(self, query: str, top_n: int):
        # First call to the retriever fetches the closest indices

        nodes = self.retriever.retrieve(query)
        nodes = [
            {
                "text": node.node.text,
                "llamaindex_id": node.node.id_,
            }
            for node
            in nodes
        ]
        # Call co.rerank to improve the relevance of retrieved documents

        reranked = self.co.rerank(query=query, documents=nodes, model="rerank-english-v3.0", top_n=top_n)
        nodes = [nodes[node.index] for node in reranked.results]
        return nodes


top_k = 60 # how many documents to fetch on first pass

top_n = 20 # how many documents to sub-select with rerank

retriever = RetrieverWithRerank(
    index.as_retriever(similarity_top_k=top_k),
    api_key=api_key,
)
```
```python PYTHON
query = "What happens to my Amazon EC2 instances if I delete my Auto Scaling group?"

documents = retriever.retrieve(query, top_n=top_n)

resp = co.chat(message=query, model="command-r-08-2024", temperature=0., documents=documents)
print(resp.text)
```
This works! With `co.chat`, you get the additional benefit that citations are returned for every span of text. Here's a simple function to display the citations inside square brackets.
```python PYTHON
def build_answer_with_citations(response):
    """ """
    text = response.text
    citations = response.citations

    # Construct text_with_citations adding citation spans as we iterate through citations

    end = 0
    text_with_citations = ""

    for citation in citations:
        # Add snippet between last citatiton and current citation

        start = citation.start
        text_with_citations += text[end : start]
        end = citation.end  # overwrite

        citation_blocks = " [" + ", ".join([stub[4:] for stub in citation.document_ids]) + "] "
        text_with_citations += text[start : end] + citation_blocks
    # Add any left-over

    text_with_citations += text[end:]

    return text_with_citations

grounded_answer = build_answer_with_citations(resp)
print(grounded_answer)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
