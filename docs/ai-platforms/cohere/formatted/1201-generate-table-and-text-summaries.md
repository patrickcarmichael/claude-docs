---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## generate table and text summaries

prompt_text = """You are an assistant tasked with summarizing tables and text. \
Give a concise summary of the table or text. Table or text chunk: {element}. Only provide the summary and no other text."""

table_prompts = [prompt_text.format(element=i.text) for i in table_elements]
table_summaries = parallel_proc_chat(table_prompts,None)
text_prompts = [prompt_text.format(element=i.text) for i in text_elements]
text_summaries = parallel_proc_chat(text_prompts,None)
tables = [i.text for i in table_elements]
texts = [i.text for i in text_elements]
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
