---
title: "Crewai: Simulate a Gmail trigger with realistic payload"
description: "Simulate a Gmail trigger with realistic payload section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Simulate a Gmail trigger with realistic payload

crewai triggers run gmail/new_email
```

The `crewai triggers run` command will execute your crew with a complete Gmail payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run gmail/new_email` (not `crewai run`) to simulate trigger execution during development. After deployment, your crew will automatically receive the trigger payload.
</Warning>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← View all available triggers](./1531-view-all-available-triggers.md)

**Next:** [Monitoring Executions →](./1533-monitoring-executions.md)
