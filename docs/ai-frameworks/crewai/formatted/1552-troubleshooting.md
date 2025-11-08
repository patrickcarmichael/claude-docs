---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


* Verify Google Drive is connected and the trigger toggle is enabled
* Test locally with `crewai triggers run google_drive/file_changed` to see the exact payload structure
* If a payload is missing permission data, ensure the connected account has access to the file or folder
* The trigger sends file IDs only; use the Drive API if you need to fetch binary content during the crew run
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Monitoring Executions](./1551-monitoring-executions.md)

**Next:** [HubSpot Trigger →](./1553-hubspot-trigger.md)
