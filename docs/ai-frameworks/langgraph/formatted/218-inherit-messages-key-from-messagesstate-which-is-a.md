---
title: "Langgraph: Inherit 'messages' key from MessagesState, which is a list of chat messages"
description: "Inherit 'messages' key from MessagesState, which is a list of chat messages section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Inherit 'messages' key from MessagesState, which is a list of chat messages

class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: WeatherResponse

@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It is cloudy in NYC, with 5 mph winds in the North-East direction and a temperature of 70 degrees"
    elif city == "sf":
        return "It is 75 degrees and sunny in SF, with 3 mph winds in the South-East direction"
    else:
        raise AssertionError("Unknown city")

tools = [get_weather]

model = ChatAnthropic(model="claude-3-opus-20240229")

model_with_tools = model.bind_tools(tools)
model_with_structured_output = model.with_structured_output(WeatherResponse)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define model, tools, and graph state](./217-define-model-tools-and-graph-state.md)

**Next:** [Option 1: Bind output as tool →](./219-option-1-bind-output-as-tool.md)
