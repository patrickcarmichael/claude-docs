---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create an embedding on Together AI

textToEmbed = (
    "Our solar system orbits the Milky Way galaxy at about 515,000 mph"
)
embeddings = client.embeddings.create(
    model="togethercomputer/m2-bert-80M-8k-retrieval", input=textToEmbed
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
