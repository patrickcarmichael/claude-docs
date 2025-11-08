---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## get the Faithfulness assessment for each claim

assessed_claims_faithfulness = assess_claims(query=query,
                                             claims=claims,
                                             context=retrieved_documents,
                                             model=model,
                                             client=client)

print(f"Assessment of the claims extracted from the model's response:\n\n{assessed_claims_faithfulness}")
```
```txt title="Output"
Assessment of the claims extracted from the model's response:

- Apple's total net sales experienced a decline over the last year. SUPPORTED=1
- The three-month period ended July 1, 2023, saw a total net sale of $81,797 million. SUPPORTED=1
- This was a 1% decrease from the same period in 2022. SUPPORTED=1
- The nine-month period ended July 1, 2023, had a 3% decrease in net sales compared to the first nine months of 2022. SUPPORTED=1
- The downward trend continued into the three and six-month periods ending April 1, 2023. SUPPORTED=1
- Apple's total net sales decreased by 3% and 4% respectively, compared to the same periods in 2022. SUPPORTED=1
```
Great, we now have an assessment for each of the claims: in the last step, we just need to use these assessments to define the final score.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
