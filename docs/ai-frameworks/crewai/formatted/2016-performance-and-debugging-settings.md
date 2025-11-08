---
title: "Crewai: Performance and Debugging Settings"
description: "Performance and Debugging Settings section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Performance and Debugging Settings


Adjusting an agent's performance and monitoring its operations are crucial for efficient task execution.

### Verbose Mode and RPM Limit

* **Verbose Mode**: Enables detailed logging of an agent's actions, useful for debugging and optimization. Specifically, it provides insights into agent execution processes, aiding in the optimization of performance.
* **RPM Limit**: Sets the maximum number of requests per minute (`max_rpm`). This attribute is optional and can be set to `None` for no limit, allowing for unlimited queries to external services if needed.

### Maximum Iterations for Task Execution

The `max_iter` attribute allows users to define the maximum number of iterations an agent can perform for a single task, preventing infinite loops or excessively long executions.
The default value is set to 25, providing a balance between thoroughness and efficiency. Once the agent approaches this number, it will try its best to give a good answer.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced Customization Options](./2015-advanced-customization-options.md)

**Next:** [Customizing Agents and Tools →](./2017-customizing-agents-and-tools.md)
