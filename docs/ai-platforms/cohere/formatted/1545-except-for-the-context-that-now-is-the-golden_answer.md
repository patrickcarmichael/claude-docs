---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## except for the context, that now is the golden_answer

assessed_claims_correctness = assess_claims(query=query,
                                            claims=claims,
                                            context=golden_answer, # note the different context

                                            model=model,
                                            client=client)


print(f"Assess the claims extracted from the model's response against the golden answer:\n\n{assessed_claims_correctness}")
```
```txt title="Output"
Assess the claims extracted from the model's response against the golden answer:

- Apple's total net sales experienced a decline over the last year. SUPPORTED=1
- The three-month period ended July 1, 2023, saw a total net sale of $81,797 million. SUPPORTED=1
- This was a 1% decrease from the same period in 2022. SUPPORTED=0
- The nine-month period ended July 1, 2023, had a 3% decrease in net sales compared to the first nine months of 2022. SUPPORTED=0
- The downward trend continued into the three and six-month periods ending April 1, 2023. SUPPORTED=1
- Apple's total net sales decreased by 3% and 4% respectively, compared to the same periods in 2022. SUPPORTED=0
```
As mentioned above, automatic evaluation is a hard task, and even when using powerful models, claim assessment can present problems: for example, the third claim is labelled as 0, even if it might be inferred from the information in the gold answer.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
