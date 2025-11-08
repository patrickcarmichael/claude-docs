---
title: "Crewai: Tool Arguments"
description: "Tool Arguments section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Tool Arguments


| Argument             | Type   | Required | Default   | Description                                 |
| :------------------- | :----- | :------- | :-------- | :------------------------------------------ |
| **agent\_id**        | `str`  | Yes      | None      | The unique identifier of the Bedrock agent  |
| **agent\_alias\_id** | `str`  | Yes      | None      | The unique identifier of the agent alias    |
| **session\_id**      | `str`  | No       | timestamp | The unique identifier of the session        |
| **enable\_trace**    | `bool` | No       | False     | Whether to enable trace for debugging       |
| **end\_session**     | `bool` | No       | False     | Whether to end the session after invocation |
| **description**      | `str`  | No       | None      | Custom description for the tool             |

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the crew](./2354-run-the-crew.md)

**Next:** [Environment Variables →](./2356-environment-variables.md)
