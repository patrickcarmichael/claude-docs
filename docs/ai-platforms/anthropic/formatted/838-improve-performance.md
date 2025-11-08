---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Improve performance

In complex scenarios, it may be helpful to consider additional strategies to improve performance beyond standard [prompt engineering techniques](/en/docs/build-with-claude/prompt-engineering/overview). Here are some advanced strategies:

### Perform meta-summarization to summarize long documents

Legal summarization often involves handling long documents or many related documents at once, such that you surpass Claude’s context window. You can use a chunking method known as meta-summarization in order to handle this use case. This technique involves breaking down documents into smaller, manageable chunks and then processing each chunk separately. You can then combine the summaries of each chunk to create a meta-summary of the entire document.

Here's an example of how to perform meta-summarization:
```python
import anthropic

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
