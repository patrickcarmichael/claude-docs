---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Out-of-the-box summarization with Command-R \[#out-of-the-box-summarization-with-command-r]

First, let's see Command-R's out-of-the-box performance. It's a 128k-context model, so we can pass the full IMF report in a single call. We replicate the exact instructions from the original tweet (correcting for a minor typo) for enabling fair comparisons.
```python PYTHON
prompt_template = """\

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
