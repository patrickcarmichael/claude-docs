---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Summary

| Approach              | Description                                                                                            | Pros                                                                           | Cons                                                                           | When to use?                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Truncation            | Truncate the document to fit the context window.                                                       | - Simplicity of implementation<br />(does not rely on extrenal infrastructure) | - Loses information at the end of the document                                 | Utilize when all relevant information is contained<br /> at the beginning of the document. |
| Query Based Retrieval | Utilize semantic similarity to retrieve text chunks<br /> that are most relevant to the query.         | - Focuses on sections directly relevant to<br /> the query                     | - Relies on a semantic similarity algorithm.<br />- Might lose broader context | Employ when seeking specific<br /> information within the text.                            |
| Text Rank             | Apply graph theory to generate a cohesive set<br /> of chunks that effectively represent the document. | - Preserves the broader picture.                                               | - Might lose detailed information.                                             | Utilize in summaries and when the question<br /> requires broader context.                 |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
