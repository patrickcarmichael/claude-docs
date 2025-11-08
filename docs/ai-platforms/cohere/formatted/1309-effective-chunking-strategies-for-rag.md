---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Effective Chunking Strategies for RAG

> This page describes various chunking strategies you can use to get better RAG performance.

<AuthorsContainer
  authors={[
    {
      name: "Ania Bialas",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/c5dc5a3-Ania.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Chunking_strategies.ipynb" />
```python PYTHON
%%capture
!pip install cohere
!pip install -qU langchain-text-splitters
!pip install llama-index-embeddings-cohere
!pip install llama-index-postprocessor-cohere-rerank
```
```python PYTHON
import requests
from typing import List

from bs4 import BeautifulSoup

import cohere
from getpass import getpass
from IPython.display import HTML, display

from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

from llama_index.core import Document
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.postprocessor.cohere_rerank import CohereRerank
from llama_index.core import VectorStoreIndex, ServiceContext
```
```python PYTHON
co_model = 'command-r'
co_api_key = getpass("Enter Cohere API key: ")
co = cohere.Client(api_key=co_api_key)
```
```txt title="Output"
Enter Cohere API key: ··········
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
