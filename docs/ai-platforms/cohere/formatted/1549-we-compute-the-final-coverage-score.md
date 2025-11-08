---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## we compute the final Coverage score

score_coverage = get_final_score(assessed_claims_coverage)
print(f'Coverage: {score_coverage}')
```
```txt title="Output"
Coverage: 0.33
```
The Coverage score is telling us that 1/3 of the information in the gold answer is present in the generated answer. This is a useful information, that, similarly to what said above regarding Correctness, can raise further questions, such as: is it acceptable to have diverging information in the generated answer? Is any crucial piece of information missing in the generated answer?

The answer to these questions is use case-specific, and has to be made by the end user: The claim-based approach implemented here supports the user by providing a clear and detailed view on what the model is assessing and how.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
