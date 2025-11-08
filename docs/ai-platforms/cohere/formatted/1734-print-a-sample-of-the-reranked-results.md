---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Print a sample of the reranked results

print(f"Original question: {results_reranked_top_n[0]['question']}")
print(f"Top 3 reranked results:")
for i, result in enumerate(results_reranked_top_n[0]['search_results']):
    print(f"\n{i+1}. {result}")
```
```
Original question: What is the capital of France?
Top 3 reranked results:

1. France
semi-presidential republic and its capital, largest city and main cultural and economic centre is Paris. Metropolitan France was settled during the Iron Age by Celtic

2. Closed-ended question
variants of the above closed-ended questions that possess specific responses are: On what day were you born? (&quot;Saturday.&quot;) What is the capital of France? (&quot;Paris

3. Capital city
seat of the government. A capital is typically a city that physically encompasses the government&#039;s offices and meeting places; the status as capital is often
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
