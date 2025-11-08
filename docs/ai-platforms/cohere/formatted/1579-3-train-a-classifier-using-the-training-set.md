---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Train a classifier using the training set

Now that we have the embedding, we can train our classifier. We'll use an SVM from sklearn.
```python PYTHON
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


svm_classifier = make_pipeline(StandardScaler(), SVC(class_weight='balanced'))

svm_classifier.fit(embeddings_train, labels_train)
```
```
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('svc', SVC(class_weight='balanced'))])
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
