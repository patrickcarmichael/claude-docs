---
title: "Langgraph: Define agents"
description: "Define agents section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Define agents

flight_assistant = create_react_agent(
    model="anthropic:claude-3-5-sonnet-latest",
    tools=[..., transfer_to_hotel_assistant],
    name="flight_assistant"
)
hotel_assistant = create_react_agent(
    model="anthropic:claude-3-5-sonnet-latest",
    tools=[..., transfer_to_flight_assistant],
    name="hotel_assistant"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Handoffs](./116-handoffs.md)

**Next:** [Define multi-agent graph →](./118-define-multi-agent-graph.md)
