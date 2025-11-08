---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Utils

```python PYTHON
def set_css():
  display(HTML('''

  '''))
get_ipython().events.register('pre_run_cell', set_css)

set_css()
```
```python PYTHON
def insert_citations(text: str, citations: List[dict]):
    """
    A helper function to pretty print citations.
    """
    offset = 0
    # Process citations in the order they were provided

    for citation in citations:
        # Adjust start/end with offset

        start, end = citation['start'] + offset, citation['end'] + offset
        placeholder = "[" + ", ".join(doc[4:] for doc in citation["document_ids"]) + "]"
        # ^ doc[4:] removes the 'doc_' prefix, and leaves the quoted document

        modification = f'{text[start:end]} {placeholder}'
        # Replace the cited text with its bolded version + placeholder

        text = text[:start] + modification + text[end:]
        # Update the offset for subsequent replacements

        offset += len(modification) - (end - start)

    return text

def build_retriever(documents, top_n=5):
  # Create the embedding model

  embed_model = CohereEmbedding(
      cohere_api_key=co_api_key,
      model_name="embed-v4.0",
      input_type="search_query",
  )

  # Load the data, for this example data needs to be in a test file

  index = VectorStoreIndex.from_documents(
      documents,
      embed_model=embed_model
  )

  # Create a cohere reranker

  cohere_rerank = CohereRerank(api_key=co_api_key)

  # Create the retriever

  retriever = index.as_retriever(node_postprocessors=[cohere_rerank], similarity_top_k=top_n)
  return retriever
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
