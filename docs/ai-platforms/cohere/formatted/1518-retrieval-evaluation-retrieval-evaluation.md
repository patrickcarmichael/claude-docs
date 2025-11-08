---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Retrieval Evaluation \[#retrieval-evaluation]

In the Retrieval phase, we evaluate the set of **retrieved documents** against the **golden documents** set.

We use three standard metrics to evaluate retrieval:

* **Precision**: the proportion of returned documents that are relevant, according to the gold annotation
* **Recall**: the proportion of relevant documents in the gold data found in the retrieved documents
* **Mean Average Precision** (**MAP**): measures the capability of the retriever to return relevant documents at the top of the list

We implement these three metrics in the class below:
```python PYTHON
class RetrievalEvaluator:

    def compute_precision(self, retrieved_documents, golden_documents):
      # compute the percentage of retrieved documents found in the golden docs

      return len(set(retrieved_documents).intersection(golden_documents)) / len(retrieved_documents)

    def compute_recall(self, retrieved_documents, golden_documents):
      # compute the percentage of golden documents found in the retrieved docs

      return len(set(retrieved_documents).intersection(golden_documents)) / len(golden_documents)

    def compute_mean_average_precision(self, retrieved_documents, golden_documents):
      # check which among the retrieved docs is found in the gold, keeping the order

      correct_retrieved_documents = [1 if x in golden_documents else 0 for x in retrieved_documents]
      # compute map

      map = np.mean([sum(correct_retrieved_documents[: i + 1]) / (i + 1) for i, v in enumerate(correct_retrieved_documents) if v == 1])
      return map

    def run_evals(self, retrieved_documents, golden_documents):
      precision = round(self.compute_precision(retrieved_documents, golden_documents),2)
      recall = round(self.compute_recall(retrieved_documents, golden_documents),2)
      map = round(self.compute_mean_average_precision(retrieved_documents, golden_documents),2)
      results = {'precision': [precision],
                 'recall': [recall],
                 'map': [map]}
      for k,v in results.items():
          print(f"{k}: {v[0]}")
```
Let's now see how to use the class above to compute the results on a single datapoint.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
