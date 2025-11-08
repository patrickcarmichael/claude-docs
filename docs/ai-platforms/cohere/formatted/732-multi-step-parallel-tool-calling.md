---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multi-step, parallel tool calling

In Part 2, we saw how the Cohere API supports parallel tool calling, and in this tutorial, we looked at sequential tool calling. That also means that both scenarios can happen at the same time.

Here's an example. Suppose we ask the agent to find the CEOs of the companies with the top 3 highest market capitalization.

In the first step, it searches the Internet for information about the 3 companies with the highest market capitalization.

And in the second step, it performs parallel searches for the CEOs of the 3 identified companies.
```python PYTHON
messages = run_agent(
    "Who are the CEOs of the companies with the top 3 highest market capitalization."
)
```
```mdx
QUESTION:
Who are the CEOs of the companies with the top 3 highest market capitalization.
==================================================
TOOL PLAN:
I will search for the top 3 companies with the highest market capitalization. Then, I will search for the CEOs of those companies. 

TOOL CALLS:
Tool name: search_internet | Parameters: {"query":"top 3 companies with highest market capitalization"}
==================================================
TOOL PLAN:
The top 3 companies with the highest market capitalization are Apple, Microsoft, and Nvidia. I will now search for the CEOs of these companies. 

TOOL CALLS:
Tool name: search_internet | Parameters: {"query":"Apple CEO"}
Tool name: search_internet | Parameters: {"query":"Microsoft CEO"}
Tool name: search_internet | Parameters: {"query":"Nvidia CEO"}
==================================================
RESPONSE:
The CEOs of the top 3 companies with the highest market capitalization are:
1. Tim Cook of Apple
2. Satya Nadella of Microsoft
3. Jensen Huang of Nvidia
==================================================
CITATIONS:

Start: 79| End:87| Text:'Tim Cook' 
Sources:
1. search_internet_0f8wyxfc3hmn:0
2. search_internet_0f8wyxfc3hmn:1
3. search_internet_0f8wyxfc3hmn:2


Start: 91| End:96| Text:'Apple' 
Sources:
1. search_internet_kb9qgs1ps69e:0


Start: 100| End:113| Text:'Satya Nadella' 
Sources:
1. search_internet_wy4mn7286a88:0
2. search_internet_wy4mn7286a88:1
3. search_internet_wy4mn7286a88:2


Start: 117| End:126| Text:'Microsoft' 
Sources:
1. search_internet_kb9qgs1ps69e:0


Start: 130| End:142| Text:'Jensen Huang' 
Sources:
1. search_internet_q9ahz81npfqz:0
2. search_internet_q9ahz81npfqz:1
3. search_internet_q9ahz81npfqz:2
4. search_internet_q9ahz81npfqz:3


Start: 146| End:152| Text:'Nvidia' 
Sources:
1. search_internet_kb9qgs1ps69e:0
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
