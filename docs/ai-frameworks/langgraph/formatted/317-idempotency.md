---
title: "Langgraph: Idempotency"
description: "Idempotency section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Idempotency


Idempotency ensures that running the same operation multiple times produces the same result. This helps prevent duplicate API calls and redundant processing if a step is rerun due to a failure. Always place API calls inside **tasks** functions for checkpointing, and design them to be idempotent in case of re-execution. Re-execution can occur if a **task** starts, but does not complete successfully. Then, if the workflow is resumed, the **task** will run again. Use idempotency keys or verify existing results to avoid duplication.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Determinism](./316-determinism.md)

**Next:** [Common Pitfalls →](./318-common-pitfalls.md)
