---
title: "Langgraph: Example agent setup"
description: "Example agent setup section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Example agent setup

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_user_name],
    state_schema=CustomState,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Invocation example with an agent](./139-invocation-example-with-an-agent.md)

**Next:** [Invocation: reads the name from state (initially empty) →](./141-invocation-reads-the-name-from-state-initially-emp.md)
