---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Token count / price comparison and latency

```python PYTHON
def get_response(prompt, rag):
    if rag:
        # Get queries to run against our index from the model

        r = co.chat(prompt, model="command-r", search_queries_only=True)
        if r.search_queries:
            queries = [q["text"] for q in r.search_queries]
        else:
            print("No queries returned by the model")

        documents = []
        # Retrieve a set of chunks from the vector index and append them to the list of

        # documents that should be included in the final RAG step

        for query in queries:
            ret_nodes = retrieve(query)
            documents.extend(format_for_cohere_client(ret_nodes))

        # One final dedpulication step in case multiple queries return the same chunk

        documents = [dict(t) for t in {tuple(d.items()) for d in documents}]

        # Make a request to the model

        response = co.chat(
            message=prompt,
            model="command-r",
            temperature=0.3,
            documents=documents,
            prompt_truncation="AUTO"
        )
    else:
        response = co.chat(
            message=prompt,
            model="command-r",
            temperature=0.3,
        )

    return response
```
```python PYTHON
prompt_template = """# financial form 10-K

{tenk}

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
