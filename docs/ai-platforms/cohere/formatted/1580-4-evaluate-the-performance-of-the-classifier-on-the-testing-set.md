---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 4. Evaluate the performance of the classifier on the testing set

```python PYTHON
score = svm_classifier.score(embeddings_test, labels_test)
print(f"Validation accuracy on is {100*score}%!")
```
```
Validation accuracy on Large is 91.2%!
```
You may get a slightly different number when you run this code.

This was a small scale example, meant as a proof of concept and designed to illustrate how you can build a custom classifier quickly using a small amount of labelled data and Cohere's embeddings. Increase the number of training examples to achieve better performance on this task.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
