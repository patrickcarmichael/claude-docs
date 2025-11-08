---
title: "Langgraph: define team 1 (same as the single supervisor example above)"
description: "define team 1 (same as the single supervisor example above) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# define team 1 (same as the single supervisor example above)


def team_1_supervisor(state: MessagesState) -> Command[Literal["team_1_agent_1", "team_1_agent_2", END]]:
    response = model.invoke(...)
    return Command(goto=response["next_agent"])

def team_1_agent_1(state: MessagesState) -> Command[Literal["team_1_supervisor"]]:
    response = model.invoke(...)
    return Command(goto="team_1_supervisor", update={"messages": [response]})

def team_1_agent_2(state: MessagesState) -> Command[Literal["team_1_supervisor"]]:
    response = model.invoke(...)
    return Command(goto="team_1_supervisor", update={"messages": [response]})

team_1_builder = StateGraph(Team1State)
team_1_builder.add_node(team_1_supervisor)
team_1_builder.add_node(team_1_agent_1)
team_1_builder.add_node(team_1_agent_2)
team_1_builder.add_edge(START, "team_1_supervisor")
team_1_graph = team_1_builder.compile()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← the simplest way to build a supervisor w/ tool-calling is to use prebuilt ReAct agent graph](./384-the-simplest-way-to-build-a-supervisor-w-tool-call.md)

**Next:** [define team 2 (same as the single supervisor example above) →](./386-define-team-2-same-as-the-single-supervisor-exampl.md)
