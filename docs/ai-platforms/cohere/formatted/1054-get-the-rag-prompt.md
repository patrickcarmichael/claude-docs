---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get the RAG prompt

input_prompt = tokenizer.apply_chat_template(
    conversation=conversation,
    documents=documents,
    tokenize=False,
    add_generation_prompt=True,
    return_tensors="pt",
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
