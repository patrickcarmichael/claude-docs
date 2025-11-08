---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup

Let's start by installing the tools we'll need and then importing them.
```python PYTHON
!pip install cohere umap-learn altair annoy bertopic
```
```
Requirement already satisfied: cohere in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (5.1.5)
Requirement already satisfied: umap-learn in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (0.5.5)
Requirement already satisfied: altair in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (5.2.0)
Requirement already satisfied: annoy in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (1.17.3)
Requirement already satisfied: bertopic in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (0.16.0)
Requirement already satisfied: httpx>=0.21.2 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from cohere) (0.27.0)
Requirement already satisfied: pydantic>=1.9.2 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from cohere) (2.6.0)
Requirement already satisfied: typing_extensions>=4.0.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from cohere) (4.10.0)
Requirement already satisfied: numpy>=1.17 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from umap-learn) (1.24.3)
Requirement already satisfied: scipy>=1.3.1 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from umap-learn) (1.11.1)
Requirement already satisfied: scikit-learn>=0.22 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from umap-learn) (1.3.0)
Requirement already satisfied: numba>=0.51.2 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from umap-learn) (0.57.0)
Requirement already satisfied: pynndescent>=0.5 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from umap-learn) (0.5.12)
Requirement already satisfied: tqdm in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from umap-learn) (4.65.0)
Requirement already satisfied: jinja2 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from altair) (3.1.2)
Requirement already satisfied: jsonschema>=3.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from altair) (4.17.3)
Requirement already satisfied: packaging in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from altair) (23.2)
Requirement already satisfied: pandas>=0.25 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from altair) (2.0.3)
Requirement already satisfied: toolz in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from altair) (0.12.0)
Requirement already satisfied: hdbscan>=0.8.29 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from bertopic) (0.8.33)
Requirement already satisfied: sentence-transformers>=0.4.1 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from bertopic) (2.6.1)
Requirement already satisfied: plotly>=4.7.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from bertopic) (5.9.0)
Requirement already satisfied: cython<3,>=0.27 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from hdbscan>=0.8.29->bertopic) (0.29.37)
Requirement already satisfied: joblib>=1.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from hdbscan>=0.8.29->bertopic) (1.2.0)
Requirement already satisfied: anyio in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from httpx>=0.21.2->cohere) (3.5.0)
Requirement already satisfied: certifi in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from httpx>=0.21.2->cohere) (2023.11.17)
Requirement already satisfied: httpcore==1.* in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from httpx>=0.21.2->cohere) (1.0.2)
Requirement already satisfied: idna in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from httpx>=0.21.2->cohere) (3.4)
Requirement already satisfied: sniffio in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from httpx>=0.21.2->cohere) (1.2.0)
Requirement already satisfied: h11<0.15,>=0.13 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from httpcore==1.*->httpx>=0.21.2->cohere) (0.14.0)
Requirement already satisfied: attrs>=17.4.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair) (22.1.0)
Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair) (0.18.0)
Requirement already satisfied: llvmlite<0.41,>=0.40.0dev0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from numba>=0.51.2->umap-learn) (0.40.0)
Requirement already satisfied: python-dateutil>=2.8.2 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from pandas>=0.25->altair) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from pandas>=0.25->altair) (2023.3.post1)
Requirement already satisfied: tzdata>=2022.1 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from pandas>=0.25->altair) (2023.3)
Requirement already satisfied: tenacity>=6.2.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from plotly>=4.7.0->bertopic) (8.2.2)
Requirement already satisfied: annotated-types>=0.4.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from pydantic>=1.9.2->cohere) (0.6.0)
Requirement already satisfied: pydantic-core==2.16.1 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from pydantic>=1.9.2->cohere) (2.16.1)
Requirement already satisfied: threadpoolctl>=2.0.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from scikit-learn>=0.22->umap-learn) (2.2.0)
Requirement already satisfied: transformers<5.0.0,>=4.32.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from sentence-transformers>=0.4.1->bertopic) (4.39.3)
Requirement already satisfied: torch>=1.11.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from sentence-transformers>=0.4.1->bertopic) (2.2.2)
Requirement already satisfied: huggingface-hub>=0.15.1 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from sentence-transformers>=0.4.1->bertopic) (0.22.2)
Requirement already satisfied: Pillow in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from sentence-transformers>=0.4.1->bertopic) (10.0.1)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from jinja2->altair) (2.1.1)
Requirement already satisfied: filelock in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from huggingface-hub>=0.15.1->sentence-transformers>=0.4.1->bertopic) (3.9.0)
Requirement already satisfied: fsspec>=2023.5.0 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from huggingface-hub>=0.15.1->sentence-transformers>=0.4.1->bertopic) (2024.3.1)
Requirement already satisfied: pyyaml>=5.1 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from huggingface-hub>=0.15.1->sentence-transformers>=0.4.1->bertopic) (6.0)
Requirement already satisfied: requests in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from huggingface-hub>=0.15.1->sentence-transformers>=0.4.1->bertopic) (2.31.0)
Requirement already satisfied: six>=1.5 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas>=0.25->altair) (1.16.0)
Requirement already satisfied: sympy in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from torch>=1.11.0->sentence-transformers>=0.4.1->bertopic) (1.11.1)
Requirement already satisfied: networkx in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from torch>=1.11.0->sentence-transformers>=0.4.1->bertopic) (3.1)
Requirement already satisfied: regex!=2019.12.17 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from transformers<5.0.0,>=4.32.0->sentence-transformers>=0.4.1->bertopic) (2022.7.9)
Requirement already satisfied: tokenizers<0.19,>=0.14 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from transformers<5.0.0,>=4.32.0->sentence-transformers>=0.4.1->bertopic) (0.15.2)
Requirement already satisfied: safetensors>=0.4.1 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from transformers<5.0.0,>=4.32.0->sentence-transformers>=0.4.1->bertopic) (0.4.2)
Requirement already satisfied: charset-normalizer<4,>=2 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from requests->huggingface-hub>=0.15.1->sentence-transformers>=0.4.1->bertopic) (3.3.2)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from requests->huggingface-hub>=0.15.1->sentence-transformers>=0.4.1->bertopic) (1.26.18)
Requirement already satisfied: mpmath>=0.19 in /Users/alexiscook/anaconda3/lib/python3.11/site-packages (from sympy->torch>=1.11.0->sentence-transformers>=0.4.1->bertopic) (1.3.0)
```
```python PYTHON
import cohere
import numpy as np
import pandas as pd
import umap
import altair as alt
from annoy import AnnoyIndex
import warnings
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from bertopic.vectorizers import ClassTfidfTransformer

warnings.filterwarnings('ignore')
pd.set_option('display.max_colwidth', None)
```
Fill in your Cohere API key in the next cell. To do this, begin by [signing up to Cohere](https://dashboard.cohere.com/) (for free!) if you haven't yet. Then get your API key [here](https://dashboard.cohere.com/api-keys).
```python PYTHON
co = cohere.Client("COHERE_API_KEY") # Insert your Cohere API key

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
