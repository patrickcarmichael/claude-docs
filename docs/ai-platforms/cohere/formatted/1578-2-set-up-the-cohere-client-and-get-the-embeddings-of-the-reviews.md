---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Set up the Cohere client and get the embeddings of the reviews

We're now ready to retrieve the embeddings from the API. You'll need your API key for this next cell. [Sign up to Cohere](https://dashboard.cohere.com/) and get one if you haven't yet.
```python PYTHON
model_name = "embed-v4.0"
api_key = ""

input_type = "classification"

co = cohere.Client(api_key)
```
```python PYTHON
embeddings_train = co.embed(texts=sentences_train,
                            model=model_name,
                            input_type=input_type
                            ).embeddings

embeddings_test = co.embed(texts=sentences_test,
                           model=model_name,
                           input_type=input_type
                            ).embeddings
```
Note that the ordering of the arguments is important. If you put `input_type` in before `model_name`, you'll get an error.

We now have two sets of embeddings, `embeddings_train` contains the embeddings of the training sentences while `embeddings_test` contains the embeddings of the testing sentences.

Curious what an embedding looks like? We can print it:
```python PYTHON
print(f"Review text: {sentences_train[0]}")
print(f"Embedding vector: {embeddings_train[0][:10]}")
```
```
Review text: the script was reportedly rewritten a dozen times either 11 times too many or else too few
Embedding vector: [1.1531117, -0.8543223, -1.2496399, -0.28317127, -0.75870246, 0.5373464, 0.63233083, 0.5766576, 1.8336298, 0.44203663]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
