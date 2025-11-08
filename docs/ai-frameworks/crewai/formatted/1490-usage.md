---
title: "Crewai: Usage"
description: "Usage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Usage


When using the Kickoff API, include a `webhooks` object to your request, for example:

```json  theme={null}
{
  "inputs": {"foo": "bar"},
  "webhooks": {
    "events": ["crew_kickoff_started", "llm_call_started"],
    "url": "https://your.endpoint/webhook",
    "realtime": false,
    "authentication": {
      "strategy": "bearer",
      "token": "my-secret-token"
    }
  }
}
```

If `realtime` is set to `true`, each event is delivered individually and immediately, at the cost of crew/flow performance.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overview](./1489-overview.md)

**Next:** [Webhook Format →](./1491-webhook-format.md)
