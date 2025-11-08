---
title: "Crewai: Custom model and embeddings"
description: "Custom model and embeddings section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Custom model and embeddings


By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows. Note: a vector database is required because generated embeddings must be stored and queried from a vectordb.

```python Code theme={null}
from crewai_tools import PDFSearchTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Arguments](./1004-arguments.md)

**Next:** [- embedding_model (required): choose provider + provider-specific config →](./1006-embedding_model-required-choose-provider-provider-.md)
