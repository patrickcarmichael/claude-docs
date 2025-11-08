---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Document Questions \[#document-questions]

We can now ask a set of simple + complex questions and see how each parsing solution performs with Command-R. The questions are

* **What are the most common adverse reactions of Iwilfin?**
  * Task: Simple information extraction
* **What is the recommended dosage of IWILFIN on body surface area between 0.5 and 0.75?**
  * Task: Tabular data extraction
* **I need a succinct summary of the compound name, indication, route of administration, and mechanism of action of Iwilfin.**
  * Task: Overall document summary
```python PYTHON
import cohere
co = cohere.Client(api_key="{API_KEY}")
```
```python PYTHON
"""
Document Questions
"""
prompt = "What are the most common adverse reactions of Iwilfin?"

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
