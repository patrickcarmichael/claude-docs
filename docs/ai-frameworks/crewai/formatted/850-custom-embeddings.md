---
title: "Crewai: Custom Embeddings"
description: "Custom Embeddings section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Custom Embeddings


Instead of using the default embedding model, you might want to use your own embedding function in cases where you:

1. Want to use a different embedding model (e.g., Cohere, HuggingFace, Ollama models)
2. Need to reduce costs by using open-source embedding models
3. Have specific requirements for vector dimensions or embedding quality
4. Want to use domain-specific embeddings (e.g., for medical or legal text)

Here's an example using a HuggingFace model:

```python  theme={null}
from transformers import AutoTokenizer, AutoModel
import torch

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Default Embedding](./849-default-embedding.md)

**Next:** [Load model and tokenizer →](./851-load-model-and-tokenizer.md)
