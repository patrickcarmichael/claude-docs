---
title: "Crewai: Start the crew's task execution"
description: "Start the crew's task execution section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Start the crew's task execution

result = my_crew.kickoff()
print(result)
```

### Different Ways to Kick Off a Crew

Once your crew is assembled, initiate the workflow with the appropriate kickoff method. CrewAI provides several methods for better control over the kickoff process: `kickoff()`, `kickoff_for_each()`, `kickoff_async()`, and `kickoff_for_each_async()`.

* `kickoff()`: Starts the execution process according to the defined process flow.
* `kickoff_for_each()`: Executes tasks sequentially for each provided input event or item in the collection.
* `kickoff_async()`: Initiates the workflow asynchronously.
* `kickoff_for_each_async()`: Executes tasks concurrently for each provided input event or item, leveraging asynchronous processing.

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Crew Execution Process](./82-crew-execution-process.md)

**Next:** [Start the crew's task execution →](./84-start-the-crews-task-execution.md)
