---
title: "Crewai: Parameters"
description: "Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Parameters


The `YoutubeVideoSearchTool` accepts the following parameters:

* **youtube\_video\_url**: Optional. The URL of the YouTube video to search within. If provided during initialization, the agent won't need to specify it when using the tool.
* **config**: Optional. Configuration for the underlying RAG system, including LLM and embedder settings.
* **summarize**: Optional. Whether to summarize the retrieved content. Default is `False`.

When using the tool with an agent, the agent will need to provide:

* **search\_query**: Required. The search query to find relevant information in the video content.
* **youtube\_video\_url**: Required only if not provided during initialization. The URL of the YouTube video to search within.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1221-define-an-agent-that-uses-the-tool.md)

**Next:** [Custom Model and Embeddings →](./1223-custom-model-and-embeddings.md)
