---
title: "Langgraph: Travel agent example"
description: "Travel agent example section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Travel agent example


In this example we will build a team of travel assistant agents that can communicate with each other.

We will create 2 agents:

* `travel_advisor`: can help with travel destination recommendations. Can ask `hotel_advisor` for help.
* `hotel_advisor`: can help with hotel recommendations. Can ask `travel_advisor` for help.

This is a fully-connected network - every agent can talk to any other agent. 

First, let's create some of the tools that the agents will be using:

```python
import random
from typing_extensions import Literal
from langchain_core.tools import tool

@tool
def get_travel_recommendations():
    """Get recommendation for travel destinations"""
    return random.choice(["aruba", "turks and caicos"])

@tool
def get_hotel_recommendations(location: Literal["aruba", "turks and caicos"]):
    """Get hotel recommendations for a given destination."""
    return {
        "aruba": [
            "The Ritz-Carlton, Aruba (Palm Beach)"
            "Bucuti & Tara Beach Resort (Eagle Beach)"
        ],
        "turks and caicos": ["Grace Bay Club", "COMO Parrot Cay"],
    }[location]

@tool(return_direct=True)
def transfer_to_hotel_advisor():
    """Ask hotel advisor agent for help."""
    return "Successfully transferred to hotel advisor"

@tool(return_direct=True)
def transfer_to_travel_advisor():
    """Ask travel advisor agent for help."""
    return "Successfully transferred to travel advisor"
```

!!! note "Transfer tools"

    You might have noticed that we're using `@tool(return_direct=True)` in the transfer tools. This is done so that individual agents (e.g., `travel_advisor`) can exit the ReAct loop early once these tools are called. This is the desired behavior, as we want to detect when the agent calls this tool and hand control off _immediately_ to a different agent. 
    
    **NOTE**: This is meant to work with the prebuilt [`create_react_agent`][langgraph.prebuilt.chat_agent_executor.create_react_agent] -- if you are building a custom agent, make sure to manually add logic for handling early exit for tools that are marked with `return_direct`.

Now let's define our agent tasks and combine them into a single multi-agent network workflow:

```python
from langchain_core.messages import AIMessage
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent
from langgraph.graph import add_messages
from langgraph.func import entrypoint, task

model = ChatAnthropic(model="claude-3-5-sonnet-latest")

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setup](./155-setup.md)

**Next:** [Define travel advisor ReAct agent →](./157-define-travel-advisor-react-agent.md)
