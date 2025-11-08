---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## New Maximum Number of Input Documents for Rerank

> Stay up to date with our latest changes to co.rerank, now with an improved maximum document limit.

We have updated how the maximum number of documents is calculated for co.rerank. The endpoint will error if `len(documents) * max_chunks_per_doc >10,000` where `max_chunks_per_doc` is set to 10 as default.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
