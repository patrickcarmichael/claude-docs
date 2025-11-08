---
title: "Crewai: Telemetry"
description: "Telemetry section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Telemetry


<Note>
  By default, we collect no data that would be considered personal information under GDPR and other privacy regulations.
  We do collect Tool's names and Agent's roles, so be advised not to include any personal information in the tool's names or the Agent's roles.
  Because no personal information is collected, it's not necessary to worry about data residency.
  When `share_crew` is enabled, additional data is collected which may contain personal information if included by the user.
  Users should exercise caution when enabling this feature to ensure compliance with privacy regulations.
</Note>

CrewAI utilizes anonymous telemetry to gather usage statistics with the primary goal of enhancing the library.
Our focus is on improving and developing the features, integrations, and tools most utilized by our users.

It's pivotal to understand that by default, **NO personal data is collected** concerning prompts, task descriptions, agents' backstories or goals,
usage of tools, API calls, responses, any data processed by the agents, or secrets and environment variables.
When the `share_crew` feature is enabled, detailed data including task descriptions, agents' backstories or goals, and other specific attributes are collected
to provide deeper insights. This expanded data collection may include personal information if users have incorporated it into their crews or tasks.
Users should carefully consider the content of their crews and tasks before enabling `share_crew`.
Users can disable telemetry by setting the environment variable `CREWAI_DISABLE_TELEMETRY` to `true` or by setting `OTEL_SDK_DISABLED` to `true` (note that the latter disables all OpenTelemetry instrumentation globally).

### Examples:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Telemetry](./2296-telemetry.md)

**Next:** [Disable CrewAI telemetry only →](./2298-disable-crewai-telemetry-only.md)
