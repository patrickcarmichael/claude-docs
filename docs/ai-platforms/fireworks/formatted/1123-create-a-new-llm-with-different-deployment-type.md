---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a new LLM with different deployment type

serverless_llm = llm.with_deployment_type("serverless")
on_demand_llm = llm.with_deployment_type("on-demand")
```

### `with_temperature()`

Returns a new LLM instance with the specified temperature.

**Arguments:**

* `temperature` *float* - The temperature for generation

**Returns:**

* A new `LLM` instance with the specified temperature
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
