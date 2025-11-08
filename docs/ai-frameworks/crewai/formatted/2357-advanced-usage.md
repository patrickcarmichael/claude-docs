---
title: "Crewai: Advanced Usage"
description: "Advanced Usage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Advanced Usage


### Multi-Agent Workflow with Session Management

```python {2, 4-22} theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools.aws.bedrock.agents.invoke_agent_tool import BedrockInvokeAgentTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Environment Variables](./2356-environment-variables.md)

**Next:** [Initialize tools with session management →](./2358-initialize-tools-with-session-management.md)
