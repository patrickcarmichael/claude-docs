---
title: "Crewai: Custom Embedder Configuration"
description: "Custom Embedder Configuration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Custom Embedder Configuration


CrewAI supports multiple embedding providers to give you flexibility in choosing the best option for your use case. Here's a comprehensive guide to configuring different embedding providers for your memory system.

### Why Choose Different Embedding Providers?

* **Cost Optimization**: Local embeddings (Ollama) are free after initial setup
* **Privacy**: Keep your data local with Ollama or use your preferred cloud provider
* **Performance**: Some models work better for specific domains or languages
* **Consistency**: Match your embedding provider with your LLM provider
* **Compliance**: Meet specific regulatory or organizational requirements

### OpenAI Embeddings (Default)

OpenAI provides reliable, high-quality embeddings that work well for most use cases.

```python  theme={null}
from crewai import Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Verify storage location is consistent](./228-verify-storage-location-is-consistent.md)

**Next:** [Basic OpenAI configuration (uses environment OPENAI_API_KEY) →](./230-basic-openai-configuration-uses-environment-openai.md)
