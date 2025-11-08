---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## and run the evaluation

evaluate_retrieval.run_evals(retrieved_docs,golden_docs)
```
```txt title="Output"
precision: 0.67
recall: 0.5
map: 0.83
```
What are the figures above telling us?

* Precision (0.67) tells us that 2 out of 3 of the retrieved docs are correct
* Recall (0.5) means that 2 out of 4 relevant docs have been retrieved
* MAP (0.83) is computed as the average of 1/1 (the highest ranked doc is correct) and 2/3 (the 2nd ranked doc is wrong, the 3rd is correct).

While the example here focuses on a single datapoint, you can easily apply the same metrics to all your dataset and get the overall performance of your Retrieve phase.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
