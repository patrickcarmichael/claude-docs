---
title: "Langgraph: Define travel advisor ReAct agent"
description: "Define travel advisor ReAct agent section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Define travel advisor ReAct agent

travel_advisor_tools = [
    get_travel_recommendations,
    transfer_to_hotel_advisor,
]
travel_advisor = create_react_agent(
    model,
    travel_advisor_tools,
    prompt=(
        "You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc). "
        "If you need hotel recommendations, ask 'hotel_advisor' for help. "
        "You MUST include human-readable response before transferring to another agent."
    ),
)

@task
def call_travel_advisor(messages):
    # You can also add additional logic like changing the input to the agent / output from the agent, etc.
    # NOTE: we're invoking the ReAct agent with the full history of messages in the state
    response = travel_advisor.invoke({"messages": messages})
    return response["messages"]

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← %%capture --no-stderr](./166-capture-no-stderr.md)

**Next:** [Define hotel advisor ReAct agent →](./168-define-hotel-advisor-react-agent.md)
