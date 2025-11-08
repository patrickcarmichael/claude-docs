---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Current refusal types

The API currently handles refusals in three different ways:

| Refusal Type                       | Response Format              | When It Occurs                                  |
| ---------------------------------- | ---------------------------- | ----------------------------------------------- |
| Streaming classifier refusals      | **`stop_reason`: `refusal`** | During streaming when content violates policies |
| API input and copyright validation | 400 error codes              | When input fails validation checks              |
| Model-generated refusals           | Standard text responses      | When the model itself decides to refuse         |

>   **📝 Note**
>
> Future API versions will expand the **`stop_reason`: `refusal`** pattern to unify refusal handling across all types.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
