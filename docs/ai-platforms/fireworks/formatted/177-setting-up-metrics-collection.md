---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setting Up Metrics Collection

### Endpoint

The metrics endpoint is as follows. This URL and authorization header can be directly used by services like Grafana Cloud to ingest Fireworks metrics.
```
https://api.fireworks.ai/v1/accounts/<account-id>/metrics
```

### Authentication

Use the Authorization header with your Fireworks API key:
```json
{
  "Authorization": "Bearer YOUR_API_KEY"
}
```

### Scrape Interval

We recommend using a 1-minute scrape interval as metrics are updated every 30s.

### Rate Limits

To ensure service stability and fair usage:

* Maximum of 6 requests per minute per account
* Exceeding this limit results in HTTP 429 (Too Many Requests) responses
* Use a 1-minute scrape interval to stay within limits

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
