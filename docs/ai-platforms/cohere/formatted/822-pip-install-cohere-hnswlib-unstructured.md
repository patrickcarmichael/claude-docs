---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## %pip install cohere hnswlib unstructured

import cohere

co_chat = cohere.ClientV2(
    api_key="AZURE_API_KEY_CHAT",
    base_url="AZURE_ENDPOINT_CHAT",  # example: "https://cohere-command-r-plus-08-2024-xyz.eastus.models.ai.azure.com/"

)

co_embed = cohere.ClientV2(
    api_key="AZURE_API_KEY_EMBED",
    base_url="AZURE_ENDPOINT_EMBED",  # example: "https://embed-v-4-0-xyz.eastus.models.ai.azure.com/"

)

co_rerank = cohere.ClientV2(
    api_key="AZURE_API_KEY_RERANK",
    base_url="AZURE_ENDPOINT_RERANK",  # example: "https://cohere-rerank-v3-multilingual-xyz.eastus.models.ai.azure.com/"

)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
