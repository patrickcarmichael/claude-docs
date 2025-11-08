---
title: "Langgraph: Define model, tools, and graph state"
description: "Define model, tools, and graph state section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Define model, tools, and graph state


Now we can define how we want to structure our output, define our graph state, and also our tools and the models we are going to use.

To use structured output, we will use the `with_structured_output` method from LangChain, which you can read more about [here](https://python.langchain.com/docs/how_to/structured_output/).

We are going to use a single tool in this example for finding the weather, and will return a structured weather response to the user.

```python
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic
from langgraph.graph import MessagesState

class WeatherResponse(BaseModel):
    """Respond to the user with this"""

    temperature: float = Field(description="The temperature in fahrenheit")
    wind_directon: str = Field(
        description="The direction of the wind in abbreviated form"
    )
    wind_speed: float = Field(description="The speed of the wind in km/h")

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setup](./216-setup.md)

**Next:** [Inherit 'messages' key from MessagesState, which is a list of chat messages →](./218-inherit-messages-key-from-messagesstate-which-is-a.md)
