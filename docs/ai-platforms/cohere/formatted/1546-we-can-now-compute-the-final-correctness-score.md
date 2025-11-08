---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## we can now compute the final Correctness score

score_correctness = get_final_score(assessed_claims_correctness)
print(f'Correctness: {score_correctness}')
```
```txt title="Output"
Correctness: 0.5
```
For Correctness, we found that only half of the claims in the generated response are found in the gold answer. Note that this is not necessarily an issue: reference answers are often non-exhaustive, especially in dataset including open-ended questions, like the one we are considering in this post, and *both* the generated and golden answer can include relevant information.

### Coverage

We finally move to Coverage. Remember that, in this case, we want to check how many of the claims *in the gold answer* are included in the generated response. To do it, we first need to extract the claims from the gold answer.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
