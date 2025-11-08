---
title: "Langgraph: this is the agent function that will be called as tool"
description: "this is the agent function that will be called as tool section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# this is the agent function that will be called as tool

# notice that you can pass the state to the tool via InjectedState annotation
def agent_1(state: Annotated[dict, InjectedState]):
    # you can pass relevant parts of the state to the LLM (e.g., state["messages"])
    # and add any additional logic (different models, custom prompts, structured output, etc.)
    response = model.invoke(...)
    # return the LLM response as a string (expected tool response format)
    # this will be automatically turned to ToolMessage
    # by the prebuilt create_react_agent (supervisor)
    return response.content

def agent_2(state: Annotated[dict, InjectedState]):
    response = model.invoke(...)
    return response.content

tools = [agent_1, agent_2]

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Multi-agent architectures](./382-multi-agent-architectures.md)

**Next:** [the simplest way to build a supervisor w/ tool-calling is to use prebuilt ReAct agent graph →](./384-the-simplest-way-to-build-a-supervisor-w-tool-call.md)
