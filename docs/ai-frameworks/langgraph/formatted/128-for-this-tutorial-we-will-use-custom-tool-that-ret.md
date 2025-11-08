---
title: "Langgraph: For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)"
description: "For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)

@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It might be cloudy in nyc"
    elif city == "sf":
        return "It's always sunny in sf"
    else:
        raise AssertionError("Unknown city")

tools = [get_weather]

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← First we initialize the model we want to use.](./127-first-we-initialize-the-model-we-want-to-use.md)

**Next:** [Define the graph →](./129-define-the-graph.md)
