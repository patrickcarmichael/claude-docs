---
title: "Crewai: Tool Arguments"
description: "Tool Arguments section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Tool Arguments


| Argument                     | Type   | Required | Default | Description                                                                |
| :--------------------------- | :----- | :------- | :------ | :------------------------------------------------------------------------- |
| **knowledge\_base\_id**      | `str`  | Yes      | None    | The unique identifier of the knowledge base (0-10 alphanumeric characters) |
| **number\_of\_results**      | `int`  | No       | 5       | Maximum number of results to return                                        |
| **retrieval\_configuration** | `dict` | No       | None    | Custom configurations for the knowledge base query                         |
| **guardrail\_configuration** | `dict` | No       | None    | Content filtering settings                                                 |
| **next\_token**              | `str`  | No       | None    | Token for pagination                                                       |

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the crew](./732-run-the-crew.md)

**Next:** [Environment Variables →](./734-environment-variables.md)
