---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define the question

question = "Who mentions Jonathan Nolan?"
```
In this case, we are more concerned about accuracy than a verbose answer, so we **focus on keeping the chunks small**. To ensure that the desired size is not exceeded, we will randomly split the list of characters, in our case `["\n\n", "\n", " ", ""]`.

We employ the `RecursiveCharacterTextSplitter` from [LangChain](https://python.langchain.com/docs/get_started/introduction) for this task.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
