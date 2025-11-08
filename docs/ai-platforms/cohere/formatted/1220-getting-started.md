---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## **Getting Started**

You may use this script to jumpstart financial analysis of 10-Ks or 10-Qs with Cohere's Command model.

This cookbook relies on helpful tooling from LlamaIndex, as well as our Cohere SDK. If you're familiar with LlamaIndex, it should be easy to slot this process into your own productivity flows.
```python PYTHON
%%capture
!sudo apt install tesseract-ocr poppler-utils
!pip install "cohere<5" langchain llama-index llama-index-embeddings-cohere llama-index-postprocessor-cohere-rerank pytesseract pdf2image
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
