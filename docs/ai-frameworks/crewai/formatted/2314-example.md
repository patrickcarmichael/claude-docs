---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


The following example demonstrates how to initialize the tool and execute a github action:

1. Initialize Composio toolset

```python Code theme={null}
from composio_crewai import ComposioToolSet, App, Action
from crewai import Agent, Task, Crew

toolset = ComposioToolSet()
```

2. Connect your GitHub account

<CodeGroup>
  ```shell CLI theme={null}
  composio add github
  ```

  ```python Code theme={null}
  request = toolset.initiate_connection(app=App.GITHUB)
  print(f"Open this URL to authenticate: {request.redirectUrl}")
  ```
</CodeGroup>

3. Get Tools

* Retrieving all the tools from an app (not recommended for production):

```python Code theme={null}
tools = toolset.get_tools(apps=[App.GITHUB])
```

* Filtering tools based on tags:

```python Code theme={null}
tag = "users"

filtered_action_enums = toolset.find_actions_by_tags(
    App.GITHUB,
    tags=[tag], 
)

tools = toolset.get_tools(actions=filtered_action_enums)
```

* Filtering tools based on use case:

```python Code theme={null}
use_case = "Star a repository on GitHub"

filtered_action_enums = toolset.find_actions_by_use_case(
    App.GITHUB, use_case=use_case, advanced=False
)

tools = toolset.get_tools(actions=filtered_action_enums)
```

<Tip>Set `advanced` to True to get actions for complex use cases</Tip>

* Using specific tools:

In this demo, we will use the `GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER` action from the GitHub app.

```python Code theme={null}
tools = toolset.get_tools(
    actions=[Action.GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER]
)
```

Learn more about filtering actions [here](https://docs.composio.dev/patterns/tools/use-tools/use-specific-actions)

4. Define agent

```python Code theme={null}
crewai_agent = Agent(
    role="GitHub Agent",
    goal="You take action on GitHub using GitHub APIs",
    backstory="You are AI agent that is responsible for taking actions on GitHub on behalf of users using GitHub APIs",
    verbose=True,
    tools=tools,
    llm= # pass an llm
)
```

5. Execute task

```python Code theme={null}
task = Task(
    description="Star a repo composiohq/composio on GitHub",
    agent=crewai_agent,
    expected_output="Status of the operation",
)

crew = Crew(agents=[crewai_agent], tasks=[task])

crew.kickoff()
```

* More detailed list of tools can be found [here](https://app.composio.dev)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Installation](./2313-installation.md)

**Next:** [MultiOn Tool →](./2315-multion-tool.md)
