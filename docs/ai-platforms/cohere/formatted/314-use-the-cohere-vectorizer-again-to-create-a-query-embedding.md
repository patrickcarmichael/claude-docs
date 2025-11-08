---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## use the Cohere vectorizer again to create a query embedding

query_embedding = cohere_vectorizer.embed(
    "What did Microsoft release in 2015?",
    input_type="search_query",
    as_buffer=True,
)


query = VectorQuery(
    vector=query_embedding,
    vector_field_name="embedding",
    return_fields=[
        "url",
        "wiki_id",
        "paragraph_id",
        "id",
        "views",
        "langs",
        "title",
        "text",
    ],
    num_results=5,
)

results = index.query(query)

for doc in results:
    print(
        f"Title:{doc['title']}\nText:{doc['text']}\nDistance {doc['vector_distance']}\n\n"
    )
```
Use the `VectorQuery` class to construct a query object - here you can specify the fields you’d like Redis to return as well as the number of results (i.e. for this example we set it to `5`).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
