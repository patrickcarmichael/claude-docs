---
title: "Langgraph: Define the function that responds to the user"
description: "Define the function that responds to the user section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Define the function that responds to the user

def respond(state: AgentState):
    # Construct the final answer from the arguments of the last tool call
    weather_tool_call = state["messages"][-1].tool_calls[0]
    response = WeatherResponse(**weather_tool_call["args"])
    # Since we're using tool calling to return structured output,
    # we need to add  a tool message corresponding to the WeatherResponse tool call,
    # This is due to LLM providers' requirement that AI messages with tool calls
    # need to be followed by a tool message for each tool call
    tool_message = {
        "type": "tool",
        "content": "Here is your structured response",
        "tool_call_id": weather_tool_call["id"],
    }
    # We return the final answer
    return {"final_response": response, "messages": [tool_message]}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define the function that calls the model](./221-define-the-function-that-calls-the-model.md)

**Next:** [Define the function that determines whether to continue or not →](./223-define-the-function-that-determines-whether-to-con.md)
