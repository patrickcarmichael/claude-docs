---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## and get assess the modified claims

assessed_modified_claims = assess_claims(query=query,
                                         claims=modified_claims,
                                         context=retrieved_documents,
                                         model=model,
                                         client=client)

print(f"Assessment of the modified claims:\n\n{assessed_modified_claims}\n")

score_faithfulness_modified_claims = get_final_score(assessed_modified_claims)
print(f'Faithfulness: {score_faithfulness_modified_claims}')
```
```txt title="Output"
Assessment of the modified claims:

- Apple's total net sales experienced a decline over the last year. SUPPORTED=1
- The three-month period ended July 1, 2023, saw a total net sale of $81,797 million. SUPPORTED=1
- This was a 1% decrease from the same period in 1922. SUPPORTED=0
- The nine-month period ended July 1, 2023, had a 3% decrease in net sales compared to the first nine months of 1922. SUPPORTED=0
- The downward trend continued into the three and six-month periods ending April 1, 2023. SUPPORTED=1
- Apple's total net sales decreased by 3% and 4% respectively, compared to the same periods in 1922. SUPPORTED=0

Faithfulness: 0.5
```
As you can see, by assessing claims one by one, we are able to spot **hallucinations**, that is, the (corrupted) cases in which the information provided by the model is not grounded in any of the retrieved documents.

### Correctness

As said, Faithfulness and Correctness share the same logic, the only difference being that we will check the claims against the gold answer. We can therefore repeat the process above, and just substitute the `context`.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
