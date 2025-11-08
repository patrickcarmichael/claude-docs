---
title: "Langgraph: define team 2 (same as the single supervisor example above)"
description: "define team 2 (same as the single supervisor example above) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# define team 2 (same as the single supervisor example above)

class Team2State(MessagesState):
    next: Literal["team_2_agent_1", "team_2_agent_2", "__end__"]

def team_2_supervisor(state: Team2State):
    ...

def team_2_agent_1(state: Team2State):
    ...

def team_2_agent_2(state: Team2State):
    ...

team_2_builder = StateGraph(Team2State)
...
team_2_graph = team_2_builder.compile()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← define team 1 (same as the single supervisor example above)](./385-define-team-1-same-as-the-single-supervisor-exampl.md)

**Next:** [define top-level supervisor →](./387-define-top-level-supervisor.md)
