---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Test our baseline model on a sample problem

sample_question = "Janet's ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much does she make every day at the farmers' market?"

baseline_response = base_llm.chat.completions.create(
    messages=[{"role": "user", "content": sample_question}],
    max_tokens = 10000
)

baseline_response.choices[0].message.content
```
**Expected Baseline Behavior**: Unstructured, verbose responses without consistent formatting patterns.

**Actual Baseline Model Outputs:**

Output 1:
```
Janet has 16 eggs per day. She eats 3 into breakfast, leaving her with 16-3 = 13 eggs. Out of these, she uses 4 for her muffin recipes, which results in 13-4 = 9 eggs left. Selling each of these leftover eggs at $2, she makes 9*2 = $18 per day at the market.

print(9*2)
```
Output 2:
````
Janet starts with 16 ducks eggs. Each day, she eats 3 for breakfast and uses 4 for her muffins, which totals 7 eggs.

The remainder she sells. So, the remaining eggs are 16 - 7. She sells these at $2 per egg.

We can calculate her daily earnings from selling eggs with this simple math. I will write a python code snippet to perform this calculation.
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
