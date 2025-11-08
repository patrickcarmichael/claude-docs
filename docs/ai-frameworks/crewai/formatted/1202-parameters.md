---
title: "Crewai: Parameters"
description: "Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Parameters


The `YoutubeChannelSearchTool` accepts the following parameters:

* **youtube\_channel\_handle**: Optional. The handle of the YouTube channel to search within. If provided during initialization, the agent won't need to specify it when using the tool. If the handle doesn't start with '@', it will be automatically added.
* **config**: Optional. Configuration for the underlying RAG system, including LLM and embedder settings.
* **summarize**: Optional. Whether to summarize the retrieved content. Default is `False`.

When using the tool with an agent, the agent will need to provide:

* **search\_query**: Required. The search query to find relevant information in the channel content.
* **youtube\_channel\_handle**: Required only if not provided during initialization. The handle of the YouTube channel to search within.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1201-define-an-agent-that-uses-the-tool.md)

**Next:** [Custom Model and Embeddings →](./1203-custom-model-and-embeddings.md)
