---
title: "Crewai: Tool Arguments"
description: "Tool Arguments section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Tool Arguments


| Argument                | Type   | Required | Default | Description                                         |
| :---------------------- | :----- | :------- | :------ | :-------------------------------------------------- |
| **crew\_api\_url**      | `str`  | Yes      | None    | Base URL of the CrewAI Platform automation API      |
| **crew\_bearer\_token** | `str`  | Yes      | None    | Bearer token for API authentication                 |
| **crew\_name**          | `str`  | Yes      | None    | Name of the crew automation                         |
| **crew\_description**   | `str`  | Yes      | None    | Description of what the crew automation does        |
| **max\_polling\_time**  | `int`  | No       | 600     | Maximum time in seconds to wait for task completion |
| **crew\_inputs**        | `dict` | No       | None    | Dictionary defining custom input schema fields      |

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the crew](./2373-run-the-crew.md)

**Next:** [Environment Variables →](./2375-environment-variables.md)
