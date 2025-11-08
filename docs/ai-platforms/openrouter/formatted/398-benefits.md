---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Benefits

### Improved Caching Performance

When you consistently use the same user identifier for a specific user, OpenRouter can optimize caching to be "sticky" to that user. This means:

* A given user of your application (assuming you are using caching) will always get routed to the same provider and the cache will stay warm
* But separate users can be spread over different providers, improving load-balancing and throughput

### Enhanced Reporting and Analytics

The user parameter is available in the /activity page, in the exports from that page, and in the /generations API.

* **Activity Feed**: View requests broken down by user ID in your OpenRouter dashboard
* **Usage Analytics**: Understand which users are making the most requests
* **Export Data**: Get detailed exports that include user-level breakdowns

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
