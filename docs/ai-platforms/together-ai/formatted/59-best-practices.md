---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Best practices

### Optimal Batch Size

* Aim for 1,000-10,000 requests per batch for best performance
* Maximum 50,000 requests per batch
* Keep file size under 100MB

### Error Handling

* Always check the `error_file_id` for partial failures
* Implement retry logic for failed requests
* Use unique `custom_id` values for easy tracking

### Model Selection

* Choose models based on your quality/cost requirements
* Smaller models (7B-17B) for simple tasks
* Larger models (70B+) for complex reasoning

### Request Formatting

* Validate JSON before submission
* Use consistent schema across requests
* Include all required fields

### Monitoring

* Poll status endpoint every 30-60 seconds
* Set up notifications for completion (if available)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
