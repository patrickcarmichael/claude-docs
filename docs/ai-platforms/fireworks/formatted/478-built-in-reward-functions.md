---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Built-in Reward Functions

RewardKit provides several built-in reward functions:

### Accuracy-based

* `accuracy`: Exact string matching
* `fuzzy_accuracy`: Fuzzy string matching with configurable threshold

### Length-based

* `length`: Evaluates response length
* `length_penalty`: Penalizes responses that are too long or short

### Format-based

* `json_schema`: Validates JSON responses against a schema
* `format_compliance`: Checks if responses follow expected formats

### Code-specific

* `code_execution`: Evaluates code by executing it
* `syntax_validation`: Checks code syntax

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
