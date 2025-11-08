---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Try Command R7B Arabic

If you want to try Command R7B Arabic, it's very easy: you can use it through the [Cohere playground](https://dashboard.cohere.com/playground/chat) or in our dedicated [Hugging Face Space](https://huggingface.co/spaces/CohereForAI/c4ai-command-r-plus).

Alternatively, you can use the model in your own code. To do that, first install the `transformers` library from its source repository:
```bash
pip install 'git+https://github.com/huggingface/transformers.git'
```
Then, use this Python snippet to run a simple text-generation task with the model:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CohereForAI/c4ai-command-r7b-12-2024"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
