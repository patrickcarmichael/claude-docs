---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Learn How Cohere's Rerank Models Work

> This page contains a basic tutorial on how Cohere's ReRank models work and how to use them.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/rerank-demo.ipynb" />

In the past months, we engineered a novel relevance endpoint that takes a query and a list of documents and predicts the relevance between the query and each document.

It can be used in a two-stage retrieval setup: First you take the user question, and retrieve the top-100 documents from your collection by either using lexical search or semantic search.

You then pass the question and these top-100 documents to our relevance-endpoint to get a score for each document. You can then rank these documents based on these scores.

In our benchmarks across 20 datasets, we **saw significant improvements compared to lexical and semantic search**, especially for use-cases where no training data is available.

We will demonstrate the rerank endpoint in this notebook.
```python PYTHON
!pip install "cohere<5"
```
```txt title="Output"
[33mDEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621[0m[33m
[0mRequirement already satisfied: cohere<5 in /opt/homebrew/lib/python3.9/site-packages (4.45)
Requirement already satisfied: aiohttp<4.0,>=3.0 in /opt/homebrew/lib/python3.9/site-packages (from cohere<5) (3.8.1)
Requirement already satisfied: backoff<3.0,>=2.0 in /opt/homebrew/lib/python3.9/site-packages (from cohere<5) (2.2.1)
Requirement already satisfied: fastavro<2.0,>=1.8 in /opt/homebrew/lib/python3.9/site-packages (from cohere<5) (1.9.3)
Requirement already satisfied: importlib_metadata<7.0,>=6.0 in /opt/homebrew/lib/python3.9/site-packages (from cohere<5) (6.6.0)
Requirement already satisfied: requests<3.0.0,>=2.25.0 in /Users/elliottchoi/Library/Python/3.9/lib/python/site-packages (from cohere<5) (2.28.2)
Requirement already satisfied: urllib3<3,>=1.26 in /Users/elliottchoi/Library/Python/3.9/lib/python/site-packages (from cohere<5) (1.26.14)
Requirement already satisfied: attrs>=17.3.0 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (22.1.0)
Requirement already satisfied: charset-normalizer<3.0,>=2.0 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (2.0.12)
Requirement already satisfied: multidict<7.0,>=4.5 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (6.0.2)
Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (4.0.2)
Requirement already satisfied: yarl<2.0,>=1.0 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (1.8.1)
Requirement already satisfied: frozenlist>=1.1.1 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (1.3.1)
Requirement already satisfied: aiosignal>=1.1.2 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (1.2.0)
Requirement already satisfied: zipp>=0.5 in /opt/homebrew/lib/python3.9/site-packages (from importlib_metadata<7.0,>=6.0->cohere<5) (3.15.0)
Requirement already satisfied: idna<4,>=2.5 in /Users/elliottchoi/Library/Python/3.9/lib/python/site-packages (from requests<3.0.0,>=2.25.0->cohere<5) (3.4)
Requirement already satisfied: certifi>=2017.4.17 in /Users/elliottchoi/Library/Python/3.9/lib/python/site-packages (from requests<3.0.0,>=2.25.0->cohere<5) (2022.12.7)
[33mDEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621[0m[33m
[0m
```
```python PYTHON
import cohere
import requests
import numpy as np
from time import time
from typing import List
from pprint import pprint
```
```python PYTHON
API_KEY = "<insert api="" key="" your="">"
co = cohere.Client(API_KEY)
MODEL_NAME = "rerank-english-v3.0" # another option is rerank-multilingual-02

query = "What is the capital of the United States?"
docs = [
    "Carson City is the capital city of the American state of Nevada. At the 2010 United States Census, Carson City had a population of 55,274.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean that are a political division controlled by the United States. Its capital is Saipan.",
    "Charlotte Amalie is the capital and largest city of the United States Virgin Islands. It has about 20,000 people. The city is on the island of Saint Thomas.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district. The President of the USA and many major national government offices are in the territory. This makes it the political center of the United States of America.",
    "West Virginia is a state in the Appalachian region of the United States. Its capital and largest city is Charleston. It is often abbreviated W. Va. or simply WV.",
    "Capital punishment has existed in the United States since before the United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states. The federal government (including the United States military) also uses capital punishment.",
    "North Dakota is a state in the United States. 672,591 people lived in North Dakota in the year 2010. The capital and seat of government is Bismarck.",
    "Kentucky is a state in the United States. Its capital is Frankfort. It touches the states of Missouri (by the Mississippi River), Illinois, Indiana, Ohio, West Virginia (by the Ohio River), Tennessee and Virginia. There are many rivers in Kentucky",
    "Micronesia, officially the Federated States of Micronesia, is an island nation in the Pacific Ocean, northeast of Papua New Guinea. The country is a sovereign state in free association with the United States. The capital city of Federated States of Micronesia is Palikir.",
    "Utah is a state in the west United States. The capital and largest city is Salt Lake City. Utah became a state in the U.S. on January 4, 1896."]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
