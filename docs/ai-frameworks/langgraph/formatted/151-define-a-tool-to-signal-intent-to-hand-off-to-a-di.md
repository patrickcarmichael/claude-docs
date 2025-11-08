---
title: "Langgraph: Define a tool to signal intent to hand off to a different agent"
description: "Define a tool to signal intent to hand off to a different agent section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Define a tool to signal intent to hand off to a different agent

@tool(return_direct=True)
def transfer_to_hotel_advisor():
    """Ask hotel advisor agent for help."""
    return "Successfully transferred to hotel advisor"

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← How to build a multi-agent network (functional API)](./150-how-to-build-a-multi-agent-network-functional-api.md)

**Next:** [define an agent →](./152-define-an-agent.md)
