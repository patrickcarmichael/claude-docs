---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Migrating Monolithic Prompts to Command-R with RAG

> This page contains a discussion of how to automatically migrating monolothic prompts.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Migrating_Monolithic_Prompts_to_Command_R_with_RAG.ipynb" />

Command-R is a powerful LLM optimized for long context tasks such as retrieval augmented generation (RAG). Migrating a monolithic task such as question-answering or query-focused summarization to RAG can improve the quality of responses due to reduced hallucination and improved conciseness through grounding.

Previously, migrating an existing use case to RAG involved a lot of manual work around indexing documents, implementing at least a basic search strategy, extensive post-processing to introduce proper grounding through citations, and of course fine-tuning an LLM to work well in the RAG paradigm.

This cookbook demonstrates automatic migration of monolithic prompts through two diverse use cases where an original prompt is broken down into two parts: (1) context; and (2) instructions. The former can be done automatically or through simple chunking, while the latter is done automatically by Command-R through single shot prompt optimization.

The two use cases demonstrated here are:

1. Autobiography Assistant; and
2. Legal Question Answering
```python PYTHON
##!pip install cohere
```
```python PYTHON
import json
import os
import re

import cohere
import getpass
```
```python PYTHON
CO_API_KEY = getpass.getpass('cohere API key:')
```
```txt title="Output"
cohere API key:··········
```
```python PYTHON
co = cohere.Client(CO_API_KEY)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
