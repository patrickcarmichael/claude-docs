---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## LlamaIndex and Cohere's Models

> Learn how to use Cohere and LlamaIndex together to generate responses based on data.

### Prerequisite

To use LlamaIndex and Cohere, you will need:

* LlamaIndex Package. To install it, run:
  * `pip install llama-index`
  * `pip install llama-index-llms-cohere` (to use the Command models)
  * `pip install llama-index-embeddings-cohere` (to use the Embed models)
  * `pip install llama-index-postprocessor-cohere-rerank` (to use the Rerank models)
* Cohere's SDK. To install it, run `pip install cohere`. If you run into any issues or want more details on Cohere's SDK, [see this wiki](https://github.com/cohere-ai/cohere-python).
* A Cohere API Key. For more details on pricing [see this page](https://cohere.com/pricing). When you create an account with Cohere, we automatically create a trial API key for you. This key will be available on the dashboard where you can copy it, and it's in the dashboard section called "API Keys" as well.

### Cohere Chat with LlamaIndex

To use Cohere's chat functionality with LlamaIndex create a [Cohere model object](https://docs.llamaindex.ai/en/stable/examples/llm/cohere.html) and call the `chat` function.
```python PYTHON
from llama_index.llms.cohere import Cohere
from llama_index.core.llms import ChatMessage

cohere_model = Cohere(
    api_key="COHERE_API_KEY", model="command-a-03-2025"
)

message = ChatMessage(role="user", content="What is 2 + 3?")

response = cohere_model.chat([message])
print(response)
```

### Cohere Embeddings with LlamaIndex

To use Cohere's embeddings with LlamaIndex create a [Cohere Embeddings object](https://docs.llamaindex.ai/en/stable/examples/embeddings/cohereai.html) with an embedding model [from this list](/reference/embed) and call `get_text_embedding`.
```python PYTHON
from llama_index.embeddings.cohere import CohereEmbedding

embed_model = CohereEmbedding(
    api_key="COHERE_API_KEY",
    model_name="embed-english-v3.0",
    input_type="search_document",  # Use search_query for queries, search_document for documents

    max_tokens=8000,
    embedding_types=["float"],
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
