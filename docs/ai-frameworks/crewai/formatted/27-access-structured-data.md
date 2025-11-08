---
title: "Crewai: Access structured data"
description: "Access structured data section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Access structured data

print(result.pydantic.main_points)
print(result.pydantic.future_predictions)
```

### Multiple Messages

You can also provide a conversation history as a list of message dictionaries:

```python Code theme={null}
messages = [
    {"role": "user", "content": "I need information about large language models"},
    {"role": "assistant", "content": "I'd be happy to help with that! What specifically would you like to know?"},
    {"role": "user", "content": "What are the latest developments in 2025?"}
]

result = researcher.kickoff(messages)
```

### Async Support

An asynchronous version is available via `kickoff_async()` with the same parameters:

```python Code theme={null}
import asyncio

async def main():
    result = await researcher.kickoff_async("What are the latest developments in AI?")
    print(result.raw)

asyncio.run(main())
```

<Note>
  The `kickoff()` method uses a `LiteAgent` internally, which provides a simpler execution flow while preserving all of the agent's configuration (role, goal, backstory, tools, etc.).
</Note>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Get structured output](./26-get-structured-output.md)

**Next:** [Important Considerations and Best Practices →](./28-important-considerations-and-best-practices.md)
