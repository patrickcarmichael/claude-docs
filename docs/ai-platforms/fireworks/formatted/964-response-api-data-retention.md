---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Response API data retention

For the Response API specifically, Fireworks retains conversation data with the following policy when the API request has `store=True` (the default):

* **What is stored**: Conversation messages include the complete conversation data:
  * User prompts
  * Model responses
  * Tools called by the model
* **Opt-out option**: You can disable data storage by setting `store=False` in your API requests to prevent any conversation data from being retained.
* **Retention period**: All stored conversation data is automatically deleted after 30 days.
* **Immediate deletion**: You can immediately delete stored conversation data using the DELETE API endpoint by providing the `response_id`. This will permanently remove the record.

This retention policy is designed to be consistent with the OpenAI API while providing users control over their data storage preferences.

>   **📝 Note**
>
> The Response API retention policy only applies to conversation data when using the Response API endpoints. All other Fireworks services follow the zero data retention policy described above.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
