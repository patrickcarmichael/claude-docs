---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Text Classification Using Embeddings

> This page discusses the creation of a text classification model using word vector embeddings.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Text_Classification_Using_Embeddings.ipynb" />

This notebook shows how to build a classifier using Cohere's embeddings.

<img alt="first we embed the text in the dataset, then we use that to train a classifier" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/simple-classifier-embeddings.png" />

The example classification task here will be sentiment analysis of film reviews. We'll train a simple classifier to detect whether a film review is negative (class 0) or positive (class 1).

We'll go through the following steps:

1. Get the dataset
2. Get the embeddings of the reviews (for both the training set and the test set).
3. Train a classifier using the training set
4. Evaluate the performance of the classifier on the testing set

If you're running an older version of the SDK you'll want to upgrade it, like this:
```python PYTHON
##!pip install --upgrade cohere
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
