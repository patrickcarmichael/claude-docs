---
title: "Crewai: Process the results"
description: "Process the results section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Process the results

for result in results:
    print(f"URL: {result['metadata']['url']}")
    print(f"Content: {result.get('markdown', 'N/A')[:100]}...")
```

### Expected output

Here is the output from running the code above:

```text  theme={null}
URL: https://www.example.com/crewai-intro
Content: CrewAI is a framework for building AI-powered workflows...
URL: https://docs.crewai.com/
Content: Official documentation for CrewAI...
```

The `ApifyActorsTool` automatically fetches the Actor definition and input schema from Apify using the provided `actor_name` and then constructs the tool description and argument schema. This means you need to specify only a valid `actor_name`, and the tool handles the rest when used with agents—no need to specify the `run_input`. Here's how it works:

```python  theme={null}
from crewai import Agent
from crewai_tools import ApifyActorsTool

rag_browser = ApifyActorsTool(actor_name="apify/rag-web-browser")

agent = Agent(
    role="Research Analyst",
    goal="Find and summarize information about specific topics",
    backstory="You are an experienced researcher with attention to detail",
    tools=[rag_browser],
)
```

You can run other Actors from [Apify Store](https://apify.com/store) simply by changing the `actor_name` and, when using it manually, adjusting the `run_input` based on the Actor input schema.

For an example of usage with agents, see the [CrewAI Actor template](https://apify.com/templates/python-crewai).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the tool with input parameters](./2306-run-the-tool-with-input-parameters.md)

**Next:** [Configuration →](./2308-configuration.md)
