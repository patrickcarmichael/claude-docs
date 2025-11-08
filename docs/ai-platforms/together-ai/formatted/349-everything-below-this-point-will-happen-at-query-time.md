---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Everything below this point will happen at query time!

Once a user submits a query we are going to use both functions above to perform Vector and BM25 retrieval and then fuse the ranks using the RRF algorithm implemented below.
```py

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
