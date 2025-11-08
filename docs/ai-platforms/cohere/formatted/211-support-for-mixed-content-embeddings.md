---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Support for Mixed Content Embeddings

`embed-v4.0` supports text and content-rich images such as figures, slide decks, document screen shots (i.e. screenshots of PDF pages). This eliminates the need for complex text extraction or ETL pipelines. Unlike our previous `embed-v3.0` model family, `embed-v4.0` is capable of processing both images and texts together; the inputs can either be an image that contains both text and visual content, or text and images that youd like to compress into a single vector representation.

Here's a code sample illustrating how `embed-v4.0` could be used to work with fused images and texts like the following:

![Fused image and texts](file:cbe628fc-2b17-424d-97ac-b422d6a2b842)
```python PYTHON
import cohere
import base64

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
