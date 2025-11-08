---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Load the document(s) as simple text nodes, to be passed to the tokenization processor

nodes = [TextNode(text=document.page_content, id_=f"doc_{i}") for i, document in enumerate(documents)]
```
```txt title="Output"
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /root/nltk_data...
[nltk_data]   Unzipping taggers/averaged_perceptron_tagger.zip.
```
We'll need to convert the text into chunks of a certain size in order for the Cohere embedding model to properly ingest them down the line.

We choose to use LlamaIndex's `SentenceSplitter` in this case in order to get these chunks. We must pass a tokenization callable, which we can do using the `transformers` library.

You may also apply further transformations from the LlamaIndex repo if you so choose. Take a look at the [docs](https://docs.llamaindex.ai/en/stable/understanding/loading/loading.html) for inspiration on what is possible with transformations.
```python PYTHON
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter

from transformers import AutoTokenizer

model_id = "CohereForAI/c4ai-command-r-v01"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
