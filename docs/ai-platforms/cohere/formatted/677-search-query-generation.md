---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Search query generation

The previous example showed how to get started with RAG, and in particular, the augmented generation portion of RAG. But as its name implies, RAG consists of other steps, such as retrieval.

In a basic RAG application, the steps involved are:

* Transforming the user message into search queries
* Retrieving relevant documents for a given search query
* Generating the response and citations

Let's now look at the first step—search query generation. The chatbot needs to generate an optimal set of search queries to use for retrieval.

There are different possible approaches to this. In this example, we'll take a [tool use](/v2/docs/tool-use) approach.

Here, we build a tool that takes a user query and returns a list of relevant document snippets for that query. The tool can generate zero, one or multiple search queries depending on the user query.
```python PYTHON
def generate_search_queries(message: str) -> List[str]:

    # Define the query generation tool

    query_gen_tool = [
        {
            "type": "function",
            "function": {
                "name": "internet_search",
                "description": "Returns a list of relevant document snippets for a textual query retrieved from the internet",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "queries": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "a list of queries to search the internet with.",
                        }
                    },
                    "required": ["queries"],
                },
            },
        }
    ]

    # Define a system instruction to optimize search query generation

    instructions = "Write a search query that will find helpful information for answering the user's question accurately. If you need more than one search query, write a list of search queries. If you decide that a search is very unlikely to find information that would be useful in constructing a response to the user, you should instead directly answer."

    # Generate search queries (if any)

    search_queries = []

    res = co.chat(
        model="command-a-03-2025",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": message},
        ],
        tools=query_gen_tool,
    )

    if res.message.tool_calls:
        for tc in res.message.tool_calls:
            queries = json.loads(tc.function.arguments)["queries"]
            search_queries.extend(queries)

    return search_queries
```
In the example above, the tool breaks down the user message into two separate queries.
```python PYTHON
query = "How to stay connected with the company, and do you organize team events?"
queries_for_search = generate_search_queries(query)
print(queries_for_search)
```
```
['how to stay connected with the company', 'does the company organize team events']
```
And in the example below, the tool decides that one query is sufficient.
```python PYTHON
query = "How flexible are the working hours"
queries_for_search = generate_search_queries(query)
print(queries_for_search)
```
```
['how flexible are the working hours at the company']
```
And in the example below, the tool decides that no retrieval is needed to answer the query.
```python PYTHON
query = "What is 2 + 2"
queries_for_search = generate_search_queries(query)
print(queries_for_search)
```
```
[]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
