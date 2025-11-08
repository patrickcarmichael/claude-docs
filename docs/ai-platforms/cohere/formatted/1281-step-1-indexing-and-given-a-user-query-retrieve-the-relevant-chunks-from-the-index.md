---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 1 - Indexing and given a user query, retrieve the relevant chunks from the index

We index the document in a vector database. This requires getting the documents, chunking them, embedding, and indexing them in a vector database. Then we retrieved relevant results based on the users' query.

### We split the document into chunks of roughly 512 words

```python PYTHON
%pip install -qU langchain-text-splitters --quiet
from langchain_text_splitters import RecursiveCharacterTextSplitter
```
```txt title="Output"
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m256.9/256.9 kB[0m [31m6.6 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m66.6/66.6 kB[0m [31m8.2 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m138.5/138.5 kB[0m [31m14.5 MB/s[0m eta [36m0:00:00[0m
[?25h
```
```python PYTHON
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=False,
)

chunks_ = text_splitter.create_documents([text])
chunks = [c.page_content for c in chunks_]
print(f"The text has been broken down in {len(chunks)} chunks.")
```
```txt title="Output"
The text has been broken down in 91 chunks.
```

### Embed every text chunk

Cohere embeddings are state-of-the-art.
```python PYTHON
model="embed-v4.0"
response = co.embed(
    texts= chunks,
    model=model,
    input_type="search_document",
    embedding_types=['float']
)
embeddings = response.embeddings.float
print(f"We just computed {len(embeddings)} embeddings.")
```
```txt title="Output"
We just computed 91 embeddings.
```

### Store the embeddings in a vector database

We use the simplest vector database ever: a python dictionary using `np.array()`.
```python PYTHON
!pip install numpy --quiet
```
```python PYTHON
import numpy as np
vector_database = {i: np.array(embedding) for i, embedding in enumerate(embeddings)}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
