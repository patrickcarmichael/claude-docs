---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## RAG Pipeline Class \[#sec\_step4]

Here, we connect all of the pieces discussed above into one class object, which is then used as a tool for a Cohere ReAct agent. This class definition consolidates and clarify the key parameters used to define the RAG pipeline.
```python PYTHON
co = cohere.Client()
```
```python PYTHON
class Element(BaseModel):
    type: str
    text: Any

class RAG_pipeline():
    def __init__(self,paths):
        self.embedding_model="embed-v4.0"
        self.generation_model="command-a-03-2025"
        self.summary_model="command-a-03-2025"
        self.rerank_model="rerank-multilingual-v3.0"
        self.num_docs_to_retrieve = 10
        self.top_k_rerank=3
        self.temperature=0.2
        self.preamble="""

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
