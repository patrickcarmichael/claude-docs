---
title: "Crewai: Run the flow"
description: "Run the flow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the flow

flow = UnstructuredStateFlow()
result = flow.kickoff()
print(f"Final result: {result}")
print(f"Final state: {flow.state}")
```

### When to Use Unstructured State

Unstructured state is ideal for:

* Quick prototyping and simple flows
* Dynamically evolving state needs
* Cases where the structure may not be known in advance
* Flows with simple state requirements

While flexible, unstructured state lacks type checking and schema validation, which can lead to errors in complex applications.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Unstructured State Management](./488-unstructured-state-management.md)

**Next:** [Structured State Management →](./490-structured-state-management.md)
