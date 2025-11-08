---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Larger Cohere Representation Models

> New Representation Model sizes and an increased token limit offer improved performance and flexibility.

Representation Models are now available in the sizes of `medium-20220217` and `large-20220217` as well as an updated version of `small-20220217`. Our previous `small` model will be available as `small-20211115`. In addition, the maximum tokens length per text has increased from 512 to 1024. We recommend keeping text lengths below 128 tokens for optimal performance; for any text longer than 128 tokens, the text is spliced and the resulting embeddings of each component are then averaged and returned.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
