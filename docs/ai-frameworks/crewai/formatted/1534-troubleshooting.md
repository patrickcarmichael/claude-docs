---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


* Ensure Gmail is connected in Tools & Integrations
* Verify the Gmail Trigger is enabled on the Triggers tab
* Test locally with `crewai triggers run gmail/new_email` to see the exact payload structure
* Check the execution logs and confirm the payload is passed as `crewai_trigger_payload`
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Monitoring Executions](./1533-monitoring-executions.md)

**Next:** [Google Calendar Trigger →](./1535-google-calendar-trigger.md)
