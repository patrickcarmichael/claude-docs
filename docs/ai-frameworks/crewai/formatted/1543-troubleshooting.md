---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


* Ensure the correct Google account is connected and the trigger is enabled
* Test locally with `crewai triggers run google_calendar/event_changed` to see the exact payload structure
* Confirm your workflow handles all-day events (payloads use `start.date` and `end.date` instead of timestamps)
* Check execution logs if reminders or attendee arrays are missing—calendar permissions can limit fields in the payload
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Monitoring Executions](./1542-monitoring-executions.md)

**Next:** [Google Drive Trigger →](./1544-google-drive-trigger.md)
