---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## response.message.citations

[Citation(start=0,
          end=16, 
          text='Emperor penguins', 
          sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'snippet': 'Emperor penguins are the tallest.', 'title': 'Tall penguins'})]), 
Citation(start=25, 
          end=42, 
          text='tallest penguins.', 
          sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'snippet': 'Emperor penguins are the tallest.', 'title': 'Tall penguins'})]), 
Citation(start=61, 
          end=72, 
          text='Antarctica.',
          sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'snippet': 'Emperor penguins only live in Antarctica.', 'title': 'Penguin habitats'})])]
```
The response also includes **inline citations**  that reference the first two documents, since they hold the answers.

![](file:c225900f-0542-42e4-b911-64136e95c5ee)

>   **📝 Note**
>
> Read more about using and customizing [RAG citations here](https://docs.cohere.com/v2/docs/rag-citations)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
