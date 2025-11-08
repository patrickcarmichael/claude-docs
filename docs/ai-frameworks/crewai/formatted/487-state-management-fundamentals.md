---
title: "Crewai: State Management Fundamentals"
description: "State Management Fundamentals section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## State Management Fundamentals


### The Flow State Lifecycle

In CrewAI Flows, the state follows a predictable lifecycle:

1. **Initialization** - When a flow is created, its state is initialized (either as an empty dictionary or a Pydantic model instance)
2. **Modification** - Flow methods access and modify the state as they execute
3. **Transmission** - State is passed automatically between flow methods
4. **Persistence** (optional) - State can be saved to storage and later retrieved
5. **Completion** - The final state reflects the cumulative changes from all executed methods

Understanding this lifecycle is crucial for designing effective flows.

### Two Approaches to State Management

CrewAI offers two ways to manage state in your flows:

1. **Unstructured State** - Using dictionary-like objects for flexibility
2. **Structured State** - Using Pydantic models for type safety and validation

Let's examine each approach in detail.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Understanding the Power of State in Flows](./486-understanding-the-power-of-state-in-flows.md)

**Next:** [Unstructured State Management →](./488-unstructured-state-management.md)
