---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 6: MongoDB Query language and Vector Search

**Query flexibility**

MongoDB's query language is designed to work well with document structures, making it easy to query and manipulate ingested data using familiar Python-like syntax.

**Aggregation Pipeline**

MongoDB's aggregation pipelines is a powerful feature of the MongoDB Database that allows for complex data processing and analysis within the database.
Aggregation pipeline can be thought of similarly to pipelines in data engineering or machine learning, where processes operate sequentially, each stage taking an input, performing operations, and providing an output for the next stage.

**Stages**

Stages are the building blocks of an aggregation pipeline.
Each stage represents a specific data transformation or analysis operation.
Common stages include:

* `$match`: Filters documents (similar to WHERE in SQL)
* `$group`: Groups documents by specified fields
* `$sort`: Sorts the documents
* `$project`: Reshapes documents (select, rename, compute fields)
* `$limit`: Limits the number of documents
* `$unwind`: Deconstructs array fields
* `$lookup`: Performs left outer joins with other collections

![](file:8ca192ab-21bb-45d7-ada8-53a8abc322aa)
```python
def vector_search(user_query, collection):
    """
    Perform a vector search in the MongoDB collection based on the user query.

    Args:
    user_query (str): The user's query string.
    collection (MongoCollection): The MongoDB collection to search.

    Returns:
    list: A list of matching documents.
    """

    # Generate embedding for the user query

    query_embedding = get_embedding(
        user_query, input_type="search_query"
    )

    if query_embedding is None:
        return "Invalid query or embedding generation failed."

    # Define the vector search pipeline

    vector_search_stage = {
        "$vectorSearch": {
            "index": "vector_index",
            "queryVector": query_embedding,
            "path": "embedding",
            "numCandidates": 150,  # Number of candidate matches to consider

            "limit": 5,  # Return top 4 matches

        }
    }

    unset_stage = {
        "$unset": "embedding"  # Exclude the 'embedding' field from the results

    }

    project_stage = {
        "$project": {
            "_id": 0,  # Exclude the _id field

            "company": 1,  # Include the plot field

            "reports": 1,  # Include the title field

            "combined_attributes": 1,  # Include the genres field

            "score": {
                "$meta": "vectorSearchScore"  # Include the search score

            },
        }
    }

    pipeline = [vector_search_stage, unset_stage, project_stage]

    # Execute the search

    results = collection.aggregate(pipeline)
    return list(results)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
