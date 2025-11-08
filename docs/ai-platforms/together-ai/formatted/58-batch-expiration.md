---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Batch expiration

Batches that do not complete within the 24-hour window will move to an `EXPIRED` state. Unfinished requests are cancelled, and completed requests are made available via the output file. You will only be charged for tokens consumed from completed requests. Batches are *best effort completion* within 24 hours.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
