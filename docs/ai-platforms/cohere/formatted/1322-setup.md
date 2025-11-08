---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup

```python PYTHON
%%capture
!pip install cohere datasets llama_index llama-index-llms-cohere llama-index-embeddings-cohere
```
```python PYTHON
import cohere
import datasets
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.core.schema import TextNode
from llama_index.embeddings.cohere import CohereEmbedding
import pandas as pd

import json
from pathlib import Path
from tqdm import tqdm
from typing import List
```
```python PYTHON
api_key = "" # <your api="" key="">

co = cohere.Client(api_key=api_key)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
