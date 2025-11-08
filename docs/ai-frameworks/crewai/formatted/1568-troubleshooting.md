---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


* Ensure the Teams connection is active; it must be refreshed if the tenant revokes permissions
* Test locally with `crewai triggers run microsoft_teams/teams_message_created` to see the exact payload structure
* Confirm the webhook subscription in Microsoft 365 is still valid if payloads stop arriving
* Review execution logs for payload shape mismatches—Graph notifications may omit fields when a chat is private or restricted
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Simulate a Microsoft Teams trigger with realistic payload](./1567-simulate-a-microsoft-teams-trigger-with-realistic-.md)

**Next:** [OneDrive Trigger →](./1569-onedrive-trigger.md)
