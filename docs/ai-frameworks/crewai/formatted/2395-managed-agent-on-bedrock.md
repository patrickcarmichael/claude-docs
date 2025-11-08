---
title: "Crewai: Managed agent on Bedrock"
description: "Managed agent on Bedrock section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Managed agent on Bedrock

knowledge_router = BedrockInvokeAgentTool(
    agent_id="bedrock-agent-id",
    agent_alias_id="prod",
)

automation_strategist = Agent(
    role="Automation Strategist",
    goal="Orchestrate external automations and summarise their output",
    backstory="You coordinate enterprise workflows and know when to delegate tasks to specialised services.",
    tools=[analysis_automation, knowledge_router],
    verbose=True,
)

execute_playbook = Task(
    description="Run the analysis automation and ask the Bedrock agent for executive talking points.",
    agent=automation_strategist,
)

Crew(agents=[automation_strategist], tasks=[execute_playbook]).kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← External automation](./2394-external-automation.md)

**Next:** [**Best Practices** →](./2396-best-practices.md)
