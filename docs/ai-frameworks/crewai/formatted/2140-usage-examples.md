---
title: "Crewai: Usage Examples"
description: "Usage Examples section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Usage Examples


Let's go through examples of how to use these annotations:

### 1. Crew Base Class

```python  theme={null}
@CrewBase
class LinkedinProfileCrew():
    """LinkedinProfile crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
```

The `@CrewBase` annotation is used to decorate the main crew class. This class typically contains configurations and methods for creating agents, tasks, and the crew itself.

<Tip>
  `@CrewBase` does more than register the class:

  * **Configuration bootstrapping:** looks for `agents_config` and `tasks_config` (defaulting to `config/agents.yaml` and `config/tasks.yaml`) beside the class file, loads them at instantiation, and safely falls back to empty dicts if files are missing.
  * **Decorator orchestration:** keeps memoized references to every method marked with `@agent`, `@task`, `@before_kickoff`, or `@after_kickoff` so they are instantiated once per crew and executed in declaration order.
  * **Hook wiring:** automatically attaches the preserved kickoff hooks to the `Crew` object returned by the `@crew` method, making them run before and after `.kickoff()`.
  * **MCP integration:** when the class defines `mcp_server_params`, `get_mcp_tools()` lazily starts an MCP server adapter, hydrates the declared tools, and an internal after-kickoff hook stops the adapter. See [MCP overview](/en/mcp/overview) for adapter configuration details.
</Tip>

### 2. Tool Definition

```python  theme={null}
@tool
def myLinkedInProfileTool(self):
    return LinkedInProfileTool()
```

The `@tool` annotation is used to decorate methods that return tool objects. These tools can be used by agents to perform specific tasks.

### 3. LLM Definition

```python  theme={null}
@llm
def groq_llm(self):
    api_key = os.getenv('api_key')
    return ChatGroq(api_key=api_key, temperature=0, model_name="mixtral-8x7b-32768")
```

The `@llm` annotation is used to decorate methods that initialize and return Language Model objects. These LLMs are used by agents for natural language processing tasks.

### 4. Agent Definition

```python  theme={null}
@agent
def researcher(self) -> Agent:
    return Agent(
        config=self.agents_config['researcher']
    )
```

The `@agent` annotation is used to decorate methods that define and return Agent objects.

### 5. Task Definition

```python  theme={null}
@task
def research_task(self) -> Task:
    return Task(
        config=self.tasks_config['research_linkedin_task'],
        agent=self.researcher()
    )
```

The `@task` annotation is used to decorate methods that define and return Task objects. These methods specify the task configuration and the agent responsible for the task.

### 6. Crew Creation

```python  theme={null}
@crew
def crew(self) -> Crew:
    """Creates the LinkedinProfile crew"""
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.sequential,
        verbose=True
    )
```

The `@crew` annotation is used to decorate the method that creates and returns the `Crew` object. This method assembles all the components (agents and tasks) into a functional crew.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Available Annotations](./2139-available-annotations.md)

**Next:** [YAML Configuration →](./2141-yaml-configuration.md)
