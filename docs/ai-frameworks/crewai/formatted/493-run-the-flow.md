---
title: "Crewai: Run the flow"
description: "Run the flow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the flow

flow = StructuredStateFlow()
result = flow.kickoff()
print(f"Final result: {result}")
print(f"Final state: {flow.state}")
```

### Benefits of Structured State

Using structured state provides several advantages:

1. **Type Safety** - Catch type errors at development time
2. **Self-Documentation** - The state model clearly documents what data is available
3. **Validation** - Automatic validation of data types and constraints
4. **IDE Support** - Get autocomplete and inline documentation
5. **Default Values** - Easily define fallbacks for missing data

### When to Use Structured State

Structured state is recommended for:

* Complex flows with well-defined data schemas
* Team projects where multiple developers work on the same code
* Applications where data validation is important
* Flows that need to enforce specific data types and constraints

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a flow with typed state](./492-create-a-flow-with-typed-state.md)

**Next:** [The Automatic State ID →](./494-the-automatic-state-id.md)
