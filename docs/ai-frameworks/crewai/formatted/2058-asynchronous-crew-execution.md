---
title: "Crewai: Asynchronous Crew Execution"
description: "Asynchronous Crew Execution section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Asynchronous Crew Execution


To kickoff a crew asynchronously, use the `kickoff_async()` method. This method initiates the crew execution in a separate thread, allowing the main thread to continue executing other tasks.

### Method Signature

```python Code theme={null}
def kickoff_async(self, inputs: dict) -> CrewOutput:
```

### Parameters

* `inputs` (dict): A dictionary containing the input data required for the tasks.

### Returns

* `CrewOutput`: An object representing the result of the crew execution.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Introduction](./2057-introduction.md)

**Next:** [Potential Use Cases →](./2059-potential-use-cases.md)
