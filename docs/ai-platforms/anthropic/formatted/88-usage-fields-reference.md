---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Usage Fields Reference

Each usage object contains:

* `input_tokens`: Base input tokens processed
* `output_tokens`: Tokens generated in the response
* `cache_creation_input_tokens`: Tokens used to create cache entries
* `cache_read_input_tokens`: Tokens read from cache
* `service_tier`: The service tier used (e.g., "standard")
* `total_cost_usd`: Total cost in USD (only in result message)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
