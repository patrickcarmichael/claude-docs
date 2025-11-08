---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Specifying a schema

### Generating nested objects

In JSON Schema mode, there are no limitations on the levels of nesting. However, in JSON mode (no schema specified), nesting is limited to 5 levels.

### Schema constraints

When constructing a `schema` keep the following constraints in mind:

* The `type` in the top level schema must be `object`
* Every object in the schema must have at least one `required` field specified

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
