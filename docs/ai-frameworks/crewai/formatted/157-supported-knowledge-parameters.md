---
title: "Crewai: Supported Knowledge Parameters"
description: "Supported Knowledge Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Supported Knowledge Parameters


<ParamField body="sources" type="List[BaseKnowledgeSource]" required="Yes">
  List of knowledge sources that provide content to be stored and queried. Can include PDF, CSV, Excel, JSON, text files, or string content.
</ParamField>

<ParamField body="collection_name" type="str">
  Name of the collection where the knowledge will be stored. Used to identify different sets of knowledge. Defaults to "knowledge" if not provided.
</ParamField>

<ParamField body="storage" type="Optional[KnowledgeStorage]">
  Custom storage configuration for managing how the knowledge is stored and retrieved. If not provided, a default storage will be created.
</ParamField>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Knowledge Configuration](./156-knowledge-configuration.md)

**Next:** [Knowledge Storage Transparency →](./158-knowledge-storage-transparency.md)
