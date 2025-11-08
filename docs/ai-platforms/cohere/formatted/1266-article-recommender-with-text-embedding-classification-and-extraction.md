---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Article Recommender with Text Embedding, Classification, and Extraction

This is a simple demonstration of how we can stack multiple NLP models together\
to get an output much closer to our desired outcome.

Embeddings can capture the meaning of a piece of text beyond keyword-matching. In this article, we will build a simple news article recommender system that computes the embeddings of all available articles and recommend the most relevant articles based on embeddings similarity.

We will also make the recommendation tighter by using text classification to recommend only articles within the same category. We will then extract a list of tags from each recommended article, which can further help readers discover new articles.

All this will be done via three Cohere API endpoints stacked together: Embed, Classify, and Chat.

<img alt="Article recommender with Embed, Classify, and Chat" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/article-recommender/article-rec-1.png" />

We will implement the following steps:

**1: Find the most similar articles to the one currently reading using embeddings.**

**2: Keep only articles of the same category using text classification.**

**3: Extract tags from these articles.**

**4: Show the top 5 recommended articles.**
```python PYTHON
! pip install cohere
```
```txt title="Output"
Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
Collecting cohere
  Downloading cohere-1.3.10-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.0 MB)
[K     |████████████████████████████████| 18.0 MB 135 kB/s
[?25hRequirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from cohere) (2.23.0)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->cohere) (1.24.3)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->cohere) (2022.6.15)
Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->cohere) (2.10)
Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->cohere) (3.0.4)
Installing collected packages: cohere
Successfully installed cohere-1.3.10
```
```python PYTHON
import numpy as np
import pandas as pd
import re
import cohere

co = cohere.Client("COHERE_API_KEY") # Get your API key: https://dashboard.cohere.com/api-keys

```
<img alt="Step 1 - Embed" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/article-recommender/article-rec-2.png" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
