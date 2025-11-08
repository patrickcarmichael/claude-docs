---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Print a sample of the top_n results (without reranking)

print(f"Original question: {results_top_n[0]['question']}")
print(f"Top {top_n} results (without reranking):")
for i, result in enumerate(results_top_n[0]['search_results']):
    print(f"\n{i+1}. {result}")
```
```
Original question: What is the capital of France?
Top 3 results (without reranking):

1. Closed-ended question
variants of the above closed-ended questions that possess specific responses are: On what day were you born? (&quot;Saturday.&quot;) What is the capital of France? (&quot;Paris

2. France
semi-presidential republic and its capital, largest city and main cultural and economic centre is Paris. Metropolitan France was settled during the Iron Age by Celtic

3. What Is a Nation?
&quot;What Is a Nation?&quot; (French: Qu&#039;est-ce qu&#039;une nation ?) is an 1882 lecture by French historian Ernest Renan (1823–1892) at the Sorbonne, known for the
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
