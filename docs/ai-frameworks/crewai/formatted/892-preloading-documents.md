---
title: "Crewai: Preloading Documents"
description: "Preloading Documents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Preloading Documents


You can preload your Weaviate database with documents before using the tool:

```python Code theme={null}
import os
from crewai_tools import WeaviateVectorSearchTool
import weaviate
from weaviate.classes.init import Auth

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setup custom model for vectorizer and generative model](./891-setup-custom-model-for-vectorizer-and-generative-m.md)

**Next:** [Connect to Weaviate →](./893-connect-to-weaviate.md)
