---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Vector Store Setup \[#sec\_step2]

There are many options for setting up a vector store. Here, we show how to do so using [Chroma](https://www.trychroma.com/) and Langchain's Multi-vector retrieval.
As the name implies, multi-vector retrieval allows us to store multiple vectors per document; for instance, for a single document chunk, one could keep embeddings for both the chunk itself, and a summary of that document. A summary may be able to distill more accurately what a chunk is about, leading to better retrieval.

You can read more about this here: [https://python.langchain.com/docs/how\_to/multi\_vector/](https://python.langchain.com/docs/how_to/multi_vector/)

Below, we demonstrate the following process:

* summaries of each chunk are embedded
* during inference, the multi-vector retrieval returns the full context document related to the summary
```python PYTHON
co = cohere.Client()
def get_chat_output(message, preamble, chat_history, model, temp, documents=None):
    return co.chat(
    message=message,
    preamble=preamble,
    chat_history=chat_history,
    documents=documents,
    model=model,
    temperature=temp
    ).text

def parallel_proc_chat(prompts,preamble,chat_history=None,model='command-a-03-2025',temp=0.1,n_jobs=10):
    """Parallel processing of chat endpoint calls."""
    responses = Parallel(n_jobs=n_jobs, prefer="threads")(delayed(get_chat_output)(prompt,preamble,chat_history,model,temp) for prompt in prompts)
    return responses

def rerank_cohere(query, returned_documents,model:str="rerank-multilingual-v3.0",top_n:int=3):
    response = co.rerank(
        query=query,
        documents=returned_documents,
        top_n=top_n,
        model=model,
        return_documents=True
    )
    top_chunks_after_rerank = [results.document.text for results in response.results]
    return top_chunks_after_rerank
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
