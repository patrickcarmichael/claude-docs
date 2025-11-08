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
TOOL PLAN:
I will use the analyze_evaluation_results tool to generate Python code to find the use case that uses the least amount of tokens on average. I will also generate code to create a markdown table to compare all use cases. 

TOOL CALLS:
Tool name: analyze_evaluation_results
    import pandas as pd
    
    evaluation_results = pd.read_csv("evaluation_results.csv")
    
    # Group by 'usecase' and calculate the average tokens

    avg_tokens_by_usecase = evaluation_results.groupby('usecase')['tokens'].mean()
    
    # Find the use case with the least average tokens

    least_avg_tokens_usecase = avg_tokens_by_usecase.idxmin()
    
    print(f"Use case with the least average tokens: {least_avg_tokens_usecase}")
    
    # Create a markdown table comparing average tokens for all use cases

    markdown_table = avg_tokens_by_usecase.reset_index()
    markdown_table.columns = ["Use Case", "Average Tokens"]
    print(markdown_table.to_markdown(index=False))
None
==================================================
RESPONSE:
The use case that uses the least amount of tokens on average is extract_names.

Here is a markdown table comparing the average tokens for all use cases:

| Use Case | Average Tokens |
|:-------------------------|-------------------------------:|
| draft_email | 245.75 |
| extract_names | 106.25 |
| summarize_article | 355.75 |
==================================================
CITATIONS:

Start: 64| End:78| Text:'extract_names.' 
Sources:
1. analyze_evaluation_results_zp68h5304e3v:0


Start: 156| End:164| Text:'Use Case' 
Sources:
1. analyze_evaluation_results_zp68h5304e3v:0


Start: 167| End:181| Text:'Average Tokens' 
Sources:
1. analyze_evaluation_results_zp68h5304e3v:0


Start: 248| End:259| Text:'draft_email' 
Sources:
1. analyze_evaluation_results_zp68h5304e3v:0


Start: 262| End:268| Text:'245.75' 
Sources:
1. analyze_evaluation_results_zp68h5304e3v:0


Start: 273| End:286| Text:'extract_names' 
Sources:
1. analyze_evaluation_results_zp68h5304e3v:0


Start: 289| End:295| Text:'106.25' 
Sources:
1. analyze_evaluation_results_zp68h5304e3v:0


Start: 300| End:317| Text:'summarize_article' 
Sources:
1. analyze_evaluation_results_zp68h5304e3v:0


Start: 320| End:326| Text:'355.75' 
Sources:
1. analyze_evaluation_results_zp68h5304e3v:0
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
