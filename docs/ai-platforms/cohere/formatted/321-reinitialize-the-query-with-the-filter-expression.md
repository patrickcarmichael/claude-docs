---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## reinitialize the query with the filter expression

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
    filter_expression=filter_data,
)

results = index.query(query)
print(results)

for doc in results:
    print(
        f"Title:{doc['title']}\nText:{doc['text']}\nDistance {doc['vector_distance']}\nView {doc['views']}"
    )
```
Another feature of Redis is the ability to initialize a query with a set of filters called a [filter expression](https://www.redisvl.com/user_guide/hybrid_queries_02.html). A filter expression allows for the you to combine a set of filters over an arbitrary set of fields at query time.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
