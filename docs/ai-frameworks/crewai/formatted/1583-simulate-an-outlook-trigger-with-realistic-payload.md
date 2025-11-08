---
title: "Crewai: Simulate an Outlook trigger with realistic payload"
description: "Simulate an Outlook trigger with realistic payload section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Simulate an Outlook trigger with realistic payload

crewai triggers run microsoft_outlook/email_received
```

The `crewai triggers run` command will execute your crew with a complete Outlook payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run microsoft_outlook/email_received` (not `crewai run`) to simulate trigger execution during development. After deployment, your crew will automatically receive the trigger payload.
</Warning>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← View all available triggers](./1582-view-all-available-triggers.md)

**Next:** [Troubleshooting →](./1584-troubleshooting.md)
