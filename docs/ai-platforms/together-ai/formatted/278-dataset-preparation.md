---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Dataset Preparation

Fine-tuning requires data formatted in a specific way. We'll use a conversational dataset as an example - here the goal is to improve the model on multi-turn conversations.

**Data Formats**

Together AI supports several data formats:

1. **Conversational data**: A JSON object per line, where each object contains a list of conversation turns under the `"messages"` key. Each message must have a `"role"` (`system`, `user`, or `assistant`) and `"content"`. See details [here](/docs/fine-tuning-data-preparation#conversational-data).
```json
   {
     "messages": [
       { "role": "system", "content": "You are a helpful assistant." },
       { "role": "user", "content": "Hello!" },
       { "role": "assistant", "content": "Hi! How can I help you?" }
     ]
   }
```

2. **Instruction data**: For instruction-based tasks with prompt-completion pairs. See details [here](/docs/fine-tuning-data-preparation#instruction-data).

3. **Preference data**: For preference-based fine-tuning. See details [here](/docs/fine-tuning-data-preparation#preference-data).

4. **Generic text data**: For simple text completion tasks. See details [here](/docs/fine-tuning-data-preparation#generic-text-data).

**File Formats**

Together AI supports two file formats:

1. **JSONL**: Simpler and works for most cases.
2. **Parquet**: Stores pre-tokenized data, provides flexibility to specify custom attention mask and labels (loss masking).

By default, it's easier to use `JSONL`. However, `Parquet` can be useful if you need custom tokenization or specific loss masking.

**Example: Preparing the CoQA Dataset**

Here's an example of transforming the CoQA dataset into the required chat format:
```python
from datasets import load_dataset

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
