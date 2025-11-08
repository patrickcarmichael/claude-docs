---
title: "Crewai: Error Handling"
description: "Error Handling section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Error Handling


The tool handles these specific errors:

* Raises ImportError if `qdrant-client` is not installed (with option to auto-install)
* Raises ValueError if `QDRANT_URL` is not set
* Prompts to install `qdrant-client` if missing using `uv add qdrant-client`

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use custom embeddings with the tool](./852-use-custom-embeddings-with-the-tool.md)

**Next:** [Environment Variables →](./854-environment-variables.md)
