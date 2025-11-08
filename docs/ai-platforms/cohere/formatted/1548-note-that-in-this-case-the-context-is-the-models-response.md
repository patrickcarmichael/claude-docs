---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## note that in, this case, the context is the model's response

assessed_claims_coverage = assess_claims(query=query,
                                         claims=gold_claims,
                                         context=response,
                                         model=model,
                                         client=client)


print(f"Assess which of the gold claims is in the model's response:\n\n{assessed_claims_coverage}")
```
```txt title="Output"
Assess which of the gold claims is in the model's response:

- For the quarterly period ended June 25, 2022, the total net sales were $82,959 million. SUPPORTED=0
- For the quarterly period ended December 31, 2022, the total net sales were $117,154 million. SUPPORTED=0
- For the quarterly period ended April 1, 2023, the total net sales were $94,836 million. SUPPORTED=0
- For the quarterly period ended July 1, 2023, the total net sales were $81,797 million. SUPPORTED=1
- There was an increase in total net sales from the quarter ended June 25, 2022, to the quarter ended December 31, 2022. SUPPORTED=0
- There was a decrease in total net sales in the quarters ended April 1, 2023, and July 1, 2023. SUPPORTED=1
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
