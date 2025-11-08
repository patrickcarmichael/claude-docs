---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multi-step tool use

The Chat endpoint supports multi-step tool use, which enables the model to perform sequential reasoning. This is especially useful in agentic workflows that require multiple steps to complete a task.

As an example, suppose a tool use application has access to a web search tool. Given the question "What was the revenue of the most valuable company in the US in 2023?”,  it will need to perform a series of steps in a specific order:

* Identify the most valuable company in the US in 2023
* Then only get the revenue figure now that the company has been identified

To illustrate this, let's start with the same weather example and add another tool called `get_capital_city`, which returns the capital city of a given country.

Here's the function definitions for the tools:
```python PYTHON
def get_weather(location):
    temperature = {
        "bern": "22°C",
        "madrid": "24°C",
        "brasilia": "28°C",
    }
    loc = location.lower()
    if loc in temperature:
        return [{"temperature": {loc: temperature[loc]}}]
    return [{"temperature": {loc: "Unknown"}}]


def get_capital_city(country):
    capital_city = {
        "switzerland": "bern",
        "spain": "madrid",
        "brazil": "brasilia",
    }
    country = country.lower()
    if country in capital_city:
        return [{"capital_city": {country: capital_city[country]}}]
    return [{"capital_city": {country: "Unknown"}}]


functions_map = {
    "get_capital_city": get_capital_city,
    "get_weather": get_weather,
}
```
And here are the corresponding tool schemas:
```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "gets the weather of a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "the location to get the weather, example: San Francisco.",
                    }
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_capital_city",
            "description": "gets the capital city of a given country",
            "parameters": {
                "type": "object",
                "properties": {
                    "country": {
                        "type": "string",
                        "description": "the country to get the capital city for",
                    }
                },
                "required": ["country"],
            },
        },
    },
]
```
Next, we implement the four-step tool use workflow as described in the [previous page](https://docs.cohere.com/v2/docs/tool-use-overview).

The key difference here is the second (tool calling) and third (tool execution) steps are put in a `while` loop, which means that a sequence of this pair can happen for a number of times. This stops when the model decides in the tool calling step that no more tool calls are needed, which then triggers the fourth step (response generation).

In this example, the user asks for the temperature in Brazil's capital city.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
