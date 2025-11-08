---
title: "Crewai: Disable all OpenTelemetry (including CrewAI)"
description: "Disable all OpenTelemetry (including CrewAI) section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Disable all OpenTelemetry (including CrewAI)

os.environ['OTEL_SDK_DISABLED'] = 'true'
```

### Data Explanation:

| Defaulted | Data                                     | Reason and Specifics                                                                                                                                                                                                                                                                                             |
| :-------- | :--------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yes       | CrewAI and Python Version                | Tracks software versions. Example: CrewAI v1.2.3, Python 3.8.10. No personal data.                                                                                                                                                                                                                               |
| Yes       | Crew Metadata                            | Includes: randomly generated key and ID, process type (e.g., 'sequential', 'parallel'), boolean flag for memory usage (true/false), count of tasks, count of agents. All non-personal.                                                                                                                           |
| Yes       | Agent Data                               | Includes: randomly generated key and ID, role name (should not include personal info), boolean settings (verbose, delegation enabled, code execution allowed), max iterations, max RPM, max retry limit, LLM info (see LLM Attributes), list of tool names (should not include personal info). No personal data. |
| Yes       | Task Metadata                            | Includes: randomly generated key and ID, boolean execution settings (async\_execution, human\_input), associated agent's role and key, list of tool names. All non-personal.                                                                                                                                     |
| Yes       | Tool Usage Statistics                    | Includes: tool name (should not include personal info), number of usage attempts (integer), LLM attributes used. No personal data.                                                                                                                                                                               |
| Yes       | Test Execution Data                      | Includes: crew's randomly generated key and ID, number of iterations, model name used, quality score (float), execution time (in seconds). All non-personal.                                                                                                                                                     |
| Yes       | Task Lifecycle Data                      | Includes: creation and execution start/end times, crew and task identifiers. Stored as spans with timestamps. No personal data.                                                                                                                                                                                  |
| Yes       | LLM Attributes                           | Includes: name, model\_name, model, top\_k, temperature, and class name of the LLM. All technical, non-personal data.                                                                                                                                                                                            |
| Yes       | Crew Deployment attempt using crewAI CLI | Includes: The fact a deploy is being made and crew id, and if it's trying to pull logs, no other data.                                                                                                                                                                                                           |
| No        | Agent's Expanded Data                    | Includes: goal description, backstory text, i18n prompt file identifier. Users should ensure no personal info is included in text fields.                                                                                                                                                                        |
| No        | Detailed Task Information                | Includes: task description, expected output description, context references. Users should ensure no personal info is included in these fields.                                                                                                                                                                   |
| No        | Environment Information                  | Includes: platform, release, system, version, and CPU count. Example: 'Windows 10', 'x86\_64'. No personal data.                                                                                                                                                                                                 |
| No        | Crew and Task Inputs and Outputs         | Includes: input parameters and output results as non-identifiable data. Users should ensure no personal info is included.                                                                                                                                                                                        |
| No        | Comprehensive Crew Execution Data        | Includes: detailed logs of crew operations, all agents and tasks data, final output. All non-personal and technical in nature.                                                                                                                                                                                   |

<Note>
  "No" in the "Defaulted" column indicates that this data is only collected when `share_crew` is set to `true`.
</Note>

### Opt-In Further Telemetry Sharing

Users can choose to share their complete telemetry data by enabling the `share_crew` attribute to `True` in their crew configurations.
Enabling `share_crew` results in the collection of detailed crew and task execution data, including `goal`, `backstory`, `context`, and `output` of tasks.
This enables a deeper insight into usage patterns.

<Warning>
  If you enable `share_crew`, the collected data may include personal information if it has been incorporated into crew configurations, task descriptions, or outputs.
  Users should carefully review their data and ensure compliance with GDPR and other applicable privacy regulations before enabling this feature.
</Warning>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Disable CrewAI telemetry only](./2298-disable-crewai-telemetry-only.md)

**Next:** [Apify Actors →](./2300-apify-actors.md)
