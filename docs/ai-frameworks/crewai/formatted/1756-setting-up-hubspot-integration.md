---
title: "Crewai: Setting Up HubSpot Integration"
description: "Setting Up HubSpot Integration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setting Up HubSpot Integration


### 1. Connect Your HubSpot Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors).
2. Find **HubSpot** in the Authentication Integrations section.
3. Click **Connect** and complete the OAuth flow.
4. Grant the necessary permissions for company and contact management.
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prerequisites](./1755-prerequisites.md)

**Next:** [Available Actions →](./1757-available-actions.md)
