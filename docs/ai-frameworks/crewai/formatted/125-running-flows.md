---
title: "Crewai: Running Flows"
description: "Running Flows section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Running Flows


There are two ways to run a flow:

### Using the Flow API

You can run a flow programmatically by creating an instance of your flow class and calling the `kickoff()` method:

```python  theme={null}
flow = ExampleFlow()
result = flow.kickoff()
```

### Using the CLI

Starting from version 0.103.0, you can run flows using the `crewai run` command:

```shell  theme={null}
crewai run
```

This command automatically detects if your project is a flow (based on the `type = "flow"` setting in your pyproject.toml) and runs it accordingly. This is the recommended way to run flows from the command line.

For backward compatibility, you can also use:

```shell  theme={null}
crewai flow kickoff
```

However, the `crewai run` command is now the preferred method as it works for both crews and flows.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Next Steps](./124-next-steps.md)

**Next:** [Knowledge →](./126-knowledge.md)
