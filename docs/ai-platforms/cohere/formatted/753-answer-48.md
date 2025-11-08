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
TOOL PLAN:
I will write Python code to find the latency of the highest-scoring run for the summarize_article use case. 

TOOL CALLS:
Tool name: analyze_evaluation_results
    import pandas as pd
    
    df = pd.read_csv("evaluation_results.csv")
    
    # Filter for the summarize_article use case

    use_case_df = df[df["usecase"] == "summarize_article"]
    
    # Find the highest-scoring run

    highest_score_run = use_case_df.loc[use_case_df["score"].idxmax()]
    
    # Get the latency of the highest-scoring run

    latency = highest_score_run["latency"]
    
    print(f"Latency of the highest-scoring run: {latency}")
None
==================================================
RESPONSE:
The latency of the highest-scoring run for the summarize_article use case is 4.8.
==================================================
CITATIONS:

Start: 77| End:81| Text:'4.8.' 
Sources:
1. analyze_evaluation_results_es3hnnnp5pey:0
```
Next, we ask a question to compare the use cases in terms of token usage, and to show a markdown table to show the comparison.
```python PYTHON
messages = run_agent(
    "Which use case uses the least amount of tokens on average? Show the comparison of all use cases in a markdown table."
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
