---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a web search function

def web_search(queries: list[str]) -> list[dict]:

    documents = []

    for query in queries:
        response = tavily_client.search(query, max_results=2)

        results = [
            {
                "title": r["title"],
                "content": r["content"],
                "url": r["url"],
            }
            for r in response["results"]
        ]

        for idx, result in enumerate(results):
            document = {"id": str(idx), "data": result}
            documents.append(document)

    return documents


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
