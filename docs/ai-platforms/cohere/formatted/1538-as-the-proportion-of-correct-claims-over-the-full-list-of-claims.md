---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## as the proportion of correct claims over the full list of claims

def get_final_score(claims_list):
  supported = len(re.findall("SUPPORTED=1", claims_list))
  non_supported = len(re.findall("SUPPORTED=0", claims_list))
  score = supported / (supported+non_supported)
  return round(score, 2)
```
```python PYTHON
score_faithfulness = get_final_score(assessed_claims_faithfulness)
print(f'Faithfulness: {score_faithfulness}')
```
```txt title="Output"
Faithfulness: 1.0
```
The final Faithfulness score is 1, which means that the model's response is fully grounded in the retrieved documents: that's a very good news :)

Before moving on, let's modify the model's response by adding a piece of information which is **not** grounded in any document, and re-compute Faithfulness.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
