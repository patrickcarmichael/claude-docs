---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tokenization in Python SDK

Cohere Tokenizers are publicly hosted and can be used locally to avoid network calls. If you are using the Python SDK, the `tokenize` and `detokenize` functions will take care of downloading and caching the tokenizer for you
```python PYTHON
import cohere

co = cohere.Client(api_key="<YOUR API KEY>")

co.tokenize(
    text="caterpillar", model="command-a-03-2025"
)  # -> [74, 2340,107771]

```
Notice that this downloads the tokenizer config for the model `command-r`, which might take a couple of seconds for the initial request.

### Caching and Optimization

The cache for the tokenizer configuration is declared for each client instance. This means that starting a new process will re-download the configurations again.

If you are doing development work before going to production with your application, this might be slow if you are just experimenting by redefining the client initialization. Cohere API offers endpoints for `tokenize` and `detokenize` which avoids downloading the tokenizer configuration file. In the Python SDK, these can be accessed by setting `offline=False` like so:
```python PYTHON
import cohere

co = cohere.Client(api_key="<YOUR API KEY>")

co.tokenize(
    text="caterpillar", model="command-a-03-2025", offline=False
)  # -> [74, 2340,107771], no tokenizer config was downloaded

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
