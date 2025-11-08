---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 0 - Imports & Getting some data

In this example, we'll use a recent piece of text, that wasn't in the training data: the Wikipedia page of the movie "Dune 2".

In practice, you would typically do RAG on much longer text, that doesn't fit in the context window of the model.
```python PYTHON
%pip install "cohere<5" --quiet
```
```txt title="Output"
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m52.8/52.8 kB[0m [31m1.6 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m3.1/3.1 MB[0m [31m33.6 MB/s[0m eta [36m0:00:00[0m
[?25h
```
```python PYTHON
import cohere
API_KEY = "..." # fill in your Cohere API key here

co = cohere.Client(API_KEY)
```
```python PYTHON
!pip install wikipedia --quiet
import wikipedia
```
```txt title="Output"
Preparing metadata (setup.py) ... [?25l[?25hdone
Building wheel for wikipedia (setup.py) ... [?25l[?25hdone
```
```python PYTHON
article = wikipedia.page('Dune Part Two')
text = article.content
print(f"The text has roughly {len(text.split())} words.")
```
```txt title="Output"
The text has roughly 5323 words.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
