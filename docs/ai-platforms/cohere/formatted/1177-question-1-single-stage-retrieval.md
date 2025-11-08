---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Question 1 - single-stage retrieval

Here we are asking a question that can be answered easily with single-stage retrieval. Both regular and agentic RAG should be able to answer this question easily. Below is the comparsion of the response.

| Question                                        | Simple Rag                                                                                                                                   | Agentic Rag                                                                                                                  |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Is there a state level law for wearing helmets? | There is currently no state law requiring the use of helmets when riding a bicycle. However, some cities and counties do require helmet use. | There is currently no state law requiring helmet use. However, some cities and counties do require helmet use with bicycles. |
```python PYTHON
question1 = "Is there a state level law for wearing helmets?"
```

### Simple RAG

```python PYTHON
output = simple_rag(question1, db)
print(output)
```
```txt title="Output"
top_matched_document 1    Title: Bicycle helmet requirement\nBody: Curre...
Name: combined, dtype: object
There is currently no state law requiring the use of helmets when riding a bicycle. However, some cities and counties do require helmet use.
```

### Agentic RAG

```python PYTHON
preamble = """
You are an expert assistant that helps users answers question about legal documents and policies.
Use the provided documents to answer questions about an employee's specific situation.
"""

output = cohere_agent(question1, preamble, tools, verbose=True)
```
```txt title="Output"
running 0th step.
I will search for 'state level law for wearing helmets' in the documents provided and write an answer based on what I find.

running 1th step.
= running tool retrieve_documents, with parameters:
{'query': 'state level law for wearing helmets'}
== tool results:
{'top_matched_document': 1    Title: Bicycle helmet requirement\nBody: Curre...
Name: combined, dtype: object}
There is currently no state law requiring helmet use. However, some cities and counties do require helmet use with bicycles.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
