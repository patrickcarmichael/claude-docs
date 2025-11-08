---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Answer: 4.8

```
```mdx

Question:
What's the latency of the highest-scoring run for the summarize_article use case?
==================================================
Tool plan:
I will query the connected SQL database to find the latency of the highest-scoring run for the summarize_article use case.

I will filter the data for the summarize_article use case and order the results by score in descending order. I will then return the latency of the first result. 

Tool calls:
Tool name: sql_table_query | Parameters: {"query":"SELECT latency\r\nFROM evaluation_results\r\nWHERE usecase = 'summarize_article'\r\nORDER BY score DESC\r\nLIMIT 1;"}
==================================================
Response:
The latency of the highest-scoring run for the summarize_article use case is 4.8.
==================================================
CITATIONS:

Start: 77| End:81| Text:'4.8.' 
Sources:
1. sql_table_query_ekswkn14ra34:0
```
```python PYTHON
messages = run_agent(
    "Which use case uses the least amount of tokens on average? Show the comparison of all use cases in a markdown table."
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
