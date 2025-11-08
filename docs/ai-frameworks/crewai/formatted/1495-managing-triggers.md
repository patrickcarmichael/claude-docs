---
title: "Crewai: Managing Triggers"
description: "Managing Triggers section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Managing Triggers


### Viewing Available Triggers

To access and manage your automation triggers:

1. Navigate to your deployment in the CrewAI dashboard
2. Click on the **Triggers** tab to view all available trigger integrations

<Frame caption="Example of available automation triggers for a Gmail deployment">
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5de0e753bcb9db2e7f2e126354741de8" alt="List of available automation triggers" data-og-width="2012" width="2012" data-og-height="862" height="862" data-path="images/enterprise/list-available-triggers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0b860cce01d60455055d5de942eaf93d 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=10d7cb945ddb53606092a0206e415e2e 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f522f52cf2749038b5654ece72450589 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f5d89c0da9816cf78e15004f0c82018f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bc4ed659f02b96f8312170a00a7ee7f0 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=18ed2c13e60731bfb784abd2f403ef01 2500w" />
</Frame>

This view shows all the trigger integrations available for your deployment, along with their current connection status.

### Enabling and Disabling Triggers

Each trigger can be easily enabled or disabled using the toggle switch:

<Frame caption="Enable or disable triggers with toggle">
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=10b3ee6296f323168473593b64a1e4c8" alt="Enable or disable triggers with toggle" data-og-width="1984" width="1984" data-og-height="866" height="866" data-path="images/enterprise/trigger-selected.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=27137c8d8c072ece3319e9f4c8ee0185 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=842109fa147a6a91b9f9480e450a8ee0 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5f2cbab1be7662c99854f88496f42b4b 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5fa4240b233d980059d3db96c493fda4 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=37f3001a39aab6400b8df45fad9b5cfa 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b2959938cb0f239a6113c9a8b7aa0356 2500w" />
</Frame>

* **Enabled (blue toggle)**: The trigger is active and will automatically execute your deployment when the specified events occur
* **Disabled (gray toggle)**: The trigger is inactive and will not respond to events

Simply click the toggle to change the trigger state. Changes take effect immediately.

### Monitoring Trigger Executions

Track the performance and history of your triggered executions:

<Frame caption="List of executions triggered by automation">
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=be7efd03eb810139e42a10815402158d" alt="List of executions triggered by automation" data-og-width="1950" width="1950" data-og-height="1358" height="1358" data-path="images/enterprise/list-executions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=dbc5685ae07d5239fea0fbd03b24655b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9f8787d340f3d310e37251ac78beab2 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=45d7e191c11f9fa36e7efd63702b0369 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7ecd2e3076b92d3d697788cd607bb4a8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d7537721cb056fc8782ce423ea7bcde8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5e74d26f3f7807001bac975af3fe38af 2500w" />
</Frame>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Trigger Capabilities](./1494-trigger-capabilities.md)

**Next:** [Building Trigger-Driven Automations →](./1496-building-trigger-driven-automations.md)
