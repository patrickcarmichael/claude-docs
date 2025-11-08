---
title: "Crewai: Parameters"
description: "Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Parameters


The `WeaviateVectorSearchTool` accepts the following parameters:

* **collection\_name**: Required. The name of the collection to search within.
* **weaviate\_cluster\_url**: Required. The URL of the Weaviate cluster.
* **weaviate\_api\_key**: Required. The API key for the Weaviate cluster.
* **limit**: Optional. The number of results to return. Default is `3`.
* **alpha**: Optional. Controls the weighting between vector and keyword (BM25) search. alpha = 0 -> BM25 only, alpha = 1 -> vector search only. Default is `0.75`.
* **vectorizer**: Optional. The vectorizer to use. If not provided, it will use `text2vec_openai` with the `nomic-embed-text` model.
* **generative\_model**: Optional. The generative model to use. If not provided, it will use OpenAI's `gpt-4o`.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./888-initialize-the-tool.md)

**Next:** [Advanced Configuration →](./890-advanced-configuration.md)
