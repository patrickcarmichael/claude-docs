---
title: "Crewai: In Flow"
description: "In Flow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# In Flow

class MyFlow(Flow):
    @start()
    async def begin(self):
        crew = Crew(agents=[agent])
        result = await crew.kickoff_async()
        return result
```

The CrewAI framework automatically handles the execution of both synchronous and asynchronous tools, so you don't need to worry about how to call them differently.

### Utilizing the `tool` Decorator

```python Code theme={null}
from crewai.tools import tool
@tool("Name of my tool")
def my_tool(question: str) -> str:
    """Clear description for what this tool is useful for, your agent will need this information to use it."""
    # Function logic here
    return "Result from your custom tool"
```

### Custom Caching Mechanism

<Tip>
  Tools can optionally implement a `cache_function` to fine-tune caching
  behavior. This function determines when to cache results based on specific
  conditions, offering granular control over caching logic.
</Tip>

```python Code theme={null}
from crewai.tools import tool

@tool
def multiplication_tool(first_number: int, second_number: int) -> str:
    """Useful for when you need to multiply two numbers together."""
    return first_number * second_number

def cache_func(args, result):
    # In this case, we only cache the result if it's a multiple of 2
    cache = result % 2 == 0
    return cache

multiplication_tool.cache_function = cache_func

writer1 = Agent(
        role="Writer",
        goal="You write lessons of math for kids.",
        backstory="You're an expert in writing and you love to teach kids but you know nothing of math.",
        tools=[multiplication_tool],
        allow_delegation=False,
    )
    #...
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← In standard Crew](./346-in-standard-crew.md)

**Next:** [Conclusion →](./348-conclusion.md)
