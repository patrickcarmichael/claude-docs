---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Perform Wikipedia search

Next, we implement a function to query Wikipedia for relevant information based on user input. The `search_wikipedia()` function allows us to retrieve a specified number of Wikipedia search results, extracting their titles, snippets, and page IDs.

This will provide us with the dataset for our retrieval evaluation experiment, where we'll compare different approaches to finding and ranking relevant information.

We'll use a small dataset of 10 questions about geography to test the Wikipedia search.
```python PYTHON
import requests

def search_wikipedia(query, limit=10):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': query,
        'format': 'json',
        'srlimit': limit
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    # Format the results

    results = []
    for item in data['query']['search']:
        results.append({
            "title": item["title"],
            "snippet": item["snippet"].replace("<span class=\"searchmatch\">", "").replace("</span>", ""),
        })
            
    return results
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
