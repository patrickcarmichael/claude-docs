---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a new LLM with different temperature

creative_llm = llm.with_temperature(1.0)
deterministic_llm = llm.with_temperature(0.0)
```

### `with_perf_metrics_in_response()`

Returns a new LLM instance with the specified performance metrics setting.

**Arguments:**

* `perf_metrics_in_response` *bool* - Whether to include performance metrics in responses

**Returns:**

* A new `LLM` instance with the specified performance metrics setting
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
