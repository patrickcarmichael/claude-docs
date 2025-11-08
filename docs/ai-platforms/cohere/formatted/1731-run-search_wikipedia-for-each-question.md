---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run search_wikipedia for each question

results = []

for question in geography_questions:
    question_results = search_wikipedia(question, limit=10)
    
    # Format the results as requested

    formatted_results = []
    for item in question_results:
        formatted_result = f"{item['title']}\n{item['snippet']}"
        formatted_results.append(formatted_result)
    
    # Add to the results list

    results.append({
        "question": question,
        "search_results": formatted_results
    })
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
