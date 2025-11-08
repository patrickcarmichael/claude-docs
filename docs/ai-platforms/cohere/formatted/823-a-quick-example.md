---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## A quick example

Let's begin with a simple example to explore how RAG works.

The foundation of RAG is having a set of documents for the LLM to reference. Below, we'll work with a small collection of basic documents. While RAG systems usually involve retrieving relevant documents based on the user's query (which we'll explore later), for now we'll keep it simple and use this entire small set of documents as context for the LLM.

We have seen how to use the Chat endpoint in the text generation chapter. To use the RAG feature, we simply need to add one additional parameter, `documents`, to the endpoint call. These are the documents we want to provide as the context for the model to use in its response.
```python PYTHON
documents = [
    {
        "title": "Tall penguins",
        "text": "Emperor penguins are the tallest.",
    },
    {
        "title": "Penguin habitats",
        "text": "Emperor penguins only live in Antarctica.",
    },
    {
        "title": "What are animals?",
        "text": "Animals are different from plants.",
    },
]
```
Let's see how the model responds to the question "What are the tallest living penguins?"

The model leverages the provided documents as context for its response. Specifically, when mentioning that Emperor penguins are the tallest species, it references `doc_0` - the document which states that "Emperor penguins are the tallest."
```python PYTHON
message = "What are the tallest living penguins?"

response = co_chat.chat(
    model="model",  # Pass a dummy string

    messages=[{"role": "user", "content": message}],
    documents=[{"data": doc} for doc in documents],
)

print("\nRESPONSE:\n")
print(response.message.content[0].text)

if response.message.citations:
    print("\nCITATIONS:\n")
    for citation in response.message.citations:
        print(citation)
```
```mdx
RESPONSE:

The tallest living penguins are the Emperor penguins. They only live in Antarctica.

CITATIONS:

start=36 end=53 text='Emperor penguins.' sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'text': 'Emperor penguins are the tallest.', 'title': 'Tall penguins'})] type=None
start=59 end=83 text='only live in Antarctica.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Emperor penguins only live in Antarctica.', 'title': 'Penguin habitats'})] type=None
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
