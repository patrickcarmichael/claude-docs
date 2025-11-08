---
title: "Crewai: Tool Parameters"
description: "Tool Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Tool Parameters


### Required Parameters

* `qdrant_config` (QdrantConfig): Configuration object containing all Qdrant settings

### QdrantConfig Parameters

* `qdrant_url` (str): The URL of your Qdrant server
* `qdrant_api_key` (str, optional): API key for authentication with Qdrant
* `collection_name` (str): Name of the Qdrant collection to search
* `limit` (int): Maximum number of results to return (default: 3)
* `score_threshold` (float): Minimum similarity score threshold (default: 0.35)
* `filter` (Any, optional): Qdrant Filter instance for advanced filtering (default: None)

### Optional Tool Parameters

* `custom_embedding_fn` (Callable\[\[str], list\[float]]): Custom function for text vectorization
* `qdrant_package` (str): Base package path for Qdrant (default: "qdrant\_client")
* `client` (Any): Pre-initialized Qdrant client (optional)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run CrewAI workflow](./838-run-crewai-workflow.md)

**Next:** [Advanced Filtering →](./840-advanced-filtering.md)
