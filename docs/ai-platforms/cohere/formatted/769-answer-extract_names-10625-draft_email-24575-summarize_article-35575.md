---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Answer: extract_names (106.25), draft_email (245.75), summarize_article (355.75)

```
```mdx

Question:
Which use case uses the least amount of tokens on average? Show the comparison of all use cases in a markdown table.
==================================================
Tool plan:
I will query the connected SQL database to find the average number of tokens used for each use case. I will then present this information in a markdown table. 

Tool calls:
Tool name: sql_table_query | Parameters: {"query":"SELECT usecase, AVG(tokens) AS avg_tokens\nFROM evaluation_results\nGROUP BY usecase\nORDER BY avg_tokens ASC;"}
==================================================
Response:
Here is a markdown table showing the average number of tokens used for each use case:

| Use Case | Average Tokens |
|---|---|
| extract_names | 106.25 |
| draft_email | 245.75 |
| summarize_article | 355.75 |

The use case that uses the least amount of tokens on average is **extract_names**.
==================================================
CITATIONS:

Start: 129| End:142| Text:'extract_names' 
Sources:
1. sql_table_query_50yjx2cecqx1:0


Start: 145| End:151| Text:'106.25' 
Sources:
1. sql_table_query_50yjx2cecqx1:0


Start: 156| End:167| Text:'draft_email' 
Sources:
1. sql_table_query_50yjx2cecqx1:0


Start: 170| End:176| Text:'245.75' 
Sources:
1. sql_table_query_50yjx2cecqx1:0


Start: 181| End:198| Text:'summarize_article' 
Sources:
1. sql_table_query_50yjx2cecqx1:0


Start: 201| End:207| Text:'355.75' 
Sources:
1. sql_table_query_50yjx2cecqx1:0


Start: 277| End:290| Text:'extract_names' 
Sources:
1. sql_table_query_50yjx2cecqx1:0
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
