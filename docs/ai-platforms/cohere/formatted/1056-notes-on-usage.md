---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Notes on Usage

We recommend document snippets be short chunks (around 100-400 words per chunk) instead of long documents. They should also be formatted as key-value pairs, where the keys are short descriptive strings and the values are either text or semi-structured.

You may find that simply including relevant documents directly in a user message works as well as or better than using the `documents` parameter to render the special RAG template (though the template is a strong default for those wanting [citations](https://docs.cohere.com/docs/retrieval-augmented-generation-rag#citation-modes)). We encourage users to experiment with both approaches, and to evaluate which mode works best for their specific use case.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
