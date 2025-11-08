---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Retrieve training metrics for fine-tuned models.

GET https://api.cohere.com/v1/finetuning/finetuned-models/{finetuned_model_id}/training-step-metrics

Returns a list of metrics measured during the training of a fine-tuned model.
The metrics are ordered by step number, with the most recent step first.
The list can be paginated using `page_size` and `page_token` parameters.

Reference: https://docs.cohere.com/reference/listtrainingstepmetrics

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
