---
title: "Crewai: Customizable Attributes"
description: "Customizable Attributes section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Customizable Attributes


Crafting an efficient CrewAI team hinges on the ability to dynamically tailor your AI agents to meet the unique requirements of any project. This section covers the foundational attributes you can customize.

### Key Attributes for Customization

| Attribute                           | Description                                                                                                         |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| **Role**                            | Specifies the agent's job within the crew, such as 'Analyst' or 'Customer Service Rep'.                             |
| **Goal**                            | Defines the agent’s objectives, aligned with its role and the crew’s overarching mission.                           |
| **Backstory**                       | Provides depth to the agent's persona, enhancing motivations and engagements within the crew.                       |
| **Tools** *(Optional)*              | Represents the capabilities or methods the agent uses for tasks, from simple functions to complex integrations.     |
| **Cache** *(Optional)*              | Determines if the agent should use a cache for tool usage.                                                          |
| **Max RPM**                         | Sets the maximum requests per minute (`max_rpm`). Can be set to `None` for unlimited requests to external services. |
| **Verbose** *(Optional)*            | Enables detailed logging for debugging and optimization, providing insights into execution processes.               |
| **Allow Delegation** *(Optional)*   | Controls task delegation to other agents, default is `False`.                                                       |
| **Max Iter** *(Optional)*           | Limits the maximum number of iterations (`max_iter`) for a task to prevent infinite loops, with a default of 25.    |
| **Max Execution Time** *(Optional)* | Sets the maximum time allowed for an agent to complete a task.                                                      |
| **System Template** *(Optional)*    | Defines the system format for the agent.                                                                            |
| **Prompt Template** *(Optional)*    | Defines the prompt format for the agent.                                                                            |
| **Response Template** *(Optional)*  | Defines the response format for the agent.                                                                          |
| **Use System Prompt** *(Optional)*  | Controls whether the agent will use a system prompt during task execution.                                          |
| **Respect Context Window**          | Enables a sliding context window by default, maintaining context size.                                              |
| **Max Retry Limit**                 | Sets the maximum number of retries (`max_retry_limit`) for an agent in case of errors.                              |

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Customize Agents](./2013-customize-agents.md)

**Next:** [Advanced Customization Options →](./2015-advanced-customization-options.md)
