---
title: "Crewai: Crew Attributes"
description: "Crew Attributes section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Crew Attributes


| Attribute                             | Parameters             | Description                                                                                                                                                                                           |   |
| :------------------------------------ | :--------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - |
| **Tasks**                             | `tasks`                | A list of tasks assigned to the crew.                                                                                                                                                                 |   |
| **Agents**                            | `agents`               | A list of agents that are part of the crew.                                                                                                                                                           |   |
| **Process** *(optional)*              | `process`              | The process flow (e.g., sequential, hierarchical) the crew follows. Default is `sequential`.                                                                                                          |   |
| **Verbose** *(optional)*              | `verbose`              | The verbosity level for logging during execution. Defaults to `False`.                                                                                                                                |   |
| **Manager LLM** *(optional)*          | `manager_llm`          | The language model used by the manager agent in a hierarchical process. **Required when using a hierarchical process.**                                                                               |   |
| **Function Calling LLM** *(optional)* | `function_calling_llm` | If passed, the crew will use this LLM to do function calling for tools for all agents in the crew. Each agent can have its own LLM, which overrides the crew's LLM for function calling.              |   |
| **Config** *(optional)*               | `config`               | Optional configuration settings for the crew, in `Json` or `Dict[str, Any]` format.                                                                                                                   |   |
| **Max RPM** *(optional)*              | `max_rpm`              | Maximum requests per minute the crew adheres to during execution. Defaults to `None`.                                                                                                                 |   |
| **Memory** *(optional)*               | `memory`               | Utilized for storing execution memories (short-term, long-term, entity memory).                                                                                                                       |   |
| **Cache** *(optional)*                | `cache`                | Specifies whether to use a cache for storing the results of tools' execution. Defaults to `True`.                                                                                                     |   |
| **Embedder** *(optional)*             | `embedder`             | Configuration for the embedder to be used by the crew. Mostly used by memory for now. Default is `{"provider": "openai"}`.                                                                            |   |
| **Step Callback** *(optional)*        | `step_callback`        | A function that is called after each step of every agent. This can be used to log the agent's actions or to perform other operations; it won't override the agent-specific `step_callback`.           |   |
| **Task Callback** *(optional)*        | `task_callback`        | A function that is called after the completion of each task. Useful for monitoring or additional operations post-task execution.                                                                      |   |
| **Share Crew** *(optional)*           | `share_crew`           | Whether you want to share the complete crew information and execution with the crewAI team to make the library better, and allow us to train models.                                                  |   |
| **Output Log File** *(optional)*      | `output_log_file`      | Set to True to save logs as logs.txt in the current directory or provide a file path. Logs will be in JSON format if the filename ends in .json, otherwise .txt. Defaults to `None`.                  |   |
| **Manager Agent** *(optional)*        | `manager_agent`        | `manager` sets a custom agent that will be used as a manager.                                                                                                                                         |   |
| **Prompt File** *(optional)*          | `prompt_file`          | Path to the prompt JSON file to be used for the crew.                                                                                                                                                 |   |
| **Planning** *(optional)*             | `planning`             | Adds planning ability to the Crew. When activated before each Crew iteration, all Crew data is sent to an AgentPlanner that will plan the tasks and this plan will be added to each task description. |   |
| **Planning LLM** *(optional)*         | `planning_llm`         | The language model used by the AgentPlanner in a planning process.                                                                                                                                    |   |
| **Knowledge Sources** *(optional)*    | `knowledge_sources`    | Knowledge sources available at the crew level, accessible to all the agents.                                                                                                                          |   |

<Tip>
  **Crew Max RPM**: The `max_rpm` attribute sets the maximum number of requests per minute the crew can perform to avoid rate limits and will override individual agents' `max_rpm` settings if you set it.
</Tip>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overview](./70-overview.md)

**Next:** [Creating Crews →](./72-creating-crews.md)
