---
title: "Crewai: Triggers Overview"
description: "Triggers Overview section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Triggers Overview


Source: https://docs.crewai.com/en/enterprise/guides/automation-triggers

Understand how CrewAI AMP triggers work, how to manage them, and where to find integration-specific playbooks

CrewAI AMP triggers connect your automations to real-time events across the tools your teams already use. Instead of polling systems or relying on manual kickoffs, triggers listen for changes—new emails, calendar updates, CRM status changes—and immediately launch the crew or flow you specify.

<Frame>
    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c31a4b9031f0f517fdce3baa48471f58" alt="Automation Triggers Overview" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/enterprise/crew_connectors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9e592d155e388bb67d003b26884dc081 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=0c8aa20b2dc82de9ea3d2da6920e4195 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=782fe13ea53120f6d2f8e643a7a7b838 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=780cd735280c569e6e93caa8262b12d1 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=08bfe86a58ca08ec36ae67dca4aa5cf9 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e2bbe3b0fe0234001e030b501fa4d76c 2500w" />
</Frame>

### Integration Playbooks

Deep-dive guides walk through setup and sample workflows for each integration:

<CardGroup cols={2}>
  <Card title="Gmail Trigger" icon="envelope">
    <a href="/en/enterprise/guides/gmail-trigger">Enable crews when emails arrive or threads update.</a>
  </Card>

  <Card title="Google Calendar Trigger" icon="calendar-days">
    <a href="/en/enterprise/guides/google-calendar-trigger">React to calendar events as they are created, updated, or cancelled.</a>
  </Card>

  <Card title="Google Drive Trigger" icon="folder-open">
    <a href="/en/enterprise/guides/google-drive-trigger">Handle Drive file uploads, edits, and deletions.</a>
  </Card>

  <Card title="Outlook Trigger" icon="envelope-open">
    <a href="/en/enterprise/guides/outlook-trigger">Automate responses to new Outlook messages and calendar updates.</a>
  </Card>

  <Card title="OneDrive Trigger" icon="cloud">
    <a href="/en/enterprise/guides/onedrive-trigger">Audit file activity and sharing changes in OneDrive.</a>
  </Card>

  <Card title="Microsoft Teams Trigger" icon="comments">
    <a href="/en/enterprise/guides/microsoft-teams-trigger">Kick off workflows when new Teams chats start.</a>
  </Card>

  <Card title="HubSpot Trigger" icon="hubspot">
    <a href="/en/enterprise/guides/hubspot-trigger">Launch automations from HubSpot workflows and lifecycle events.</a>
  </Card>

  <Card title="Salesforce Trigger" icon="salesforce">
    <a href="/en/enterprise/guides/salesforce-trigger">Connect Salesforce processes to CrewAI for CRM automation.</a>
  </Card>

  <Card title="Slack Trigger" icon="slack">
    <a href="/en/enterprise/guides/slack-trigger">Start crews directly from Slack slash commands.</a>
  </Card>

  <Card title="Zapier Trigger" icon="bolt">
    <a href="/en/enterprise/guides/zapier-trigger">Bridge CrewAI with thousands of Zapier-supported apps.</a>
  </Card>
</CardGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Supported Events](./1492-supported-events.md)

**Next:** [Trigger Capabilities →](./1494-trigger-capabilities.md)
