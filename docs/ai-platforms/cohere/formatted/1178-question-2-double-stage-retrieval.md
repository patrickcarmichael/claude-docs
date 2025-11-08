---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Question 2 - double-stage retrieval

The second question requires a double-stage retrieval because top matched document references another document. You will see below that the agentic RAG is unable to produce the correct answer initially. But when given proper tools and instructions, it finds the correct answer.

| Question                                                  | Simple Rag                                                                                                                                                                                       | Agentic Rag                                                                  |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| I live in orting, do I need to wear a helmet with a bike? | In the state of Washington, there is no law requiring you to wear a helmet when riding a bike. However, some cities and counties do require helmet use, so it is worth checking your local laws. | Yes, you do need to wear a helmet with a bike in Orting if you are under 17. |
```python PYTHON
question2 = "I live in orting, do I need to wear a helmet with a bike?"
```

### Simple RAG

```python PYTHON
output = simple_rag(question2, db)
print(output)
```
```txt title="Output"
top_matched_document 1    Title: Bicycle helmet requirement\nBody: Curre...
Name: combined, dtype: object
In the state of Washington, there is no law requiring you to wear a helmet when riding a bike. However, some cities and counties do require helmet use, so it is worth checking your local laws.
```

### Agentic RAG

Produces same quality answer as the simple rag.
```python PYTHON
preamble = """
You are an expert assistant that helps users answers question about legal documents and policies.
Use the provided documents to answer questions about an employee's specific situation.
"""

output = cohere_agent(question2, preamble, tools, verbose=True)
```
```txt title="Output"
running 0th step.
I will search for 'helmet with a bike' and then write an answer.

running 1th step.
= running tool retrieve_documents, with parameters:
{'query': 'helmet with a bike'}
== tool results:
{'top_matched_document': 1    Title: Bicycle helmet requirement\nBody: Curre...
Name: combined, dtype: object}
There is no state law requiring helmet use, however, some cities and counties do require helmet use with bicycles. I cannot find any information about Orting specifically, but you should check with your local authority.
```

### Agentic RAG - New Tools

In order for the model to retrieve correct documents, we do two things:

1. New reference\_extractor() function is added. This function finds the references to other documents when given query and documents.
2. We update the instruction that directs the agent to keep retrieving relevant documents.
```python PYTHON
def reference_extractor(query: str, documents: list[str]) -> str:
    """
    Given a query and document, find references to other documents.
    """
    prompt = f"""
    # instruction

    Does the reference document mention any other documents? If so, list them.
    If not, return empty string.

    # user query

    {query}

    # retrieved documents

    {documents}
    """

    return co.chat(message=prompt, model=COHERE_MODEL, preamble=None).text


def retrieve_documents(query: str, n=1) -> dict:
    """
    Function to retrieve most relevant documents a given query.
    It also returns other references mentioned in the top matched documents.
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
    other_references = reference_extractor(query, top_matches.combined.tolist())

    return {
        "top_matched_document": top_matches.combined,
        "other_references_to_query": other_references,
    }


functions_map = {
    "retrieve_documents": retrieve_documents,
}

tools = [
    {
        "name": "retrieve_documents",
        "description": "given a query, retrieve documents from a database to answer user's question. It also finds references to other documents that should be leveraged to retrieve more documents",
        "parameter_definitions": {
            "query": {
                "description": "user's question or question or name of other document sections or references.",
                "type": "str",
                "required": True,
            }
        },
    }
]
```
```python PYTHON
preamble2 = """# Instruction

You are an expert assistant that helps users answer questions about legal documents and policies.

Please follow these steps:
1. Using user's query, use `retrieve_documents` tool to retrieve the most relevant document from the database.
2. If you see `other_references_to_query` in the tool result, search the mentioned referenced using `retrieve_documents(<other reference="">)` tool to retrieve more documents.
3. Keep trying until you find the answer.
4. Answer with yes or no as much as you can to answer the question directly.
"""

output = cohere_agent(question2, preamble2, tools, verbose=True)
```
```txt title="Output"
running 0th step.
I will search for 'Orting' and 'bike helmet' to find the relevant information.

running 1th step.
= running tool retrieve_documents, with parameters:
{'query': 'Orting bike helmet'}
== tool results:
{'other_references_to_query': 'Section 21a, Section 3b',
    'top_matched_document': 0    Title: Bicycle law\nBody: \n        Riding on ...
Name: combined, dtype: object}
I have found that there is no state law requiring helmet use, but some cities and counties do require helmets. I will now search for 'Section 21a' to find out if Orting is one of these cities or counties.

running 2th step.
= running tool retrieve_documents, with parameters:
{'query': 'Section 21a'}
== tool results:
{'other_references_to_query': '- Section 3b',
    'top_matched_document': 2    Title: Section 21a\nBody: helmet rules by loca...
Name: combined, dtype: object}
Yes, you do need to wear a helmet when riding a bike in Orting if you are under 17.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
