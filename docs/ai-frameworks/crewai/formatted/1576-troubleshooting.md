---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


* Ensure the connected account has permission to read the file metadata included in the webhook
* Test locally with `crewai triggers run microsoft_onedrive/file_changed` to see the exact payload structure
* If the trigger fires but the payload is missing `permissions`, confirm the site-level sharing settings allow Graph to return this field
* For large tenants, filter notifications upstream so the crew only runs on relevant directories
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Simulate a OneDrive trigger with realistic payload](./1575-simulate-a-onedrive-trigger-with-realistic-payload.md)

**Next:** [Outlook Trigger →](./1577-outlook-trigger.md)
