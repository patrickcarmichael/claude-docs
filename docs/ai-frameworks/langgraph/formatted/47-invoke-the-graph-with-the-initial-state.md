---
title: "Langgraph: Invoke the graph with the initial state"
description: "Invoke the graph with the initial state section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Invoke the graph with the initial state

response = graph.invoke(
    {
        "a": "set at start",
    }
)

print()
print(f"Output of graph invocation: {response}")
```

```
Entered node `node_1`:
	Input: {'a': 'set at start'}.
	Returned: {'private_data': 'set by node_1'}
Entered node `node_2`:
	Input: {'private_data': 'set by node_1'}.
	Returned: {'a': 'set by node_2'}
Entered node `node_3`:
	Input: {'a': 'set by node_2'}.
	Returned: {'a': 'set by node_3'}

Output of graph invocation: {'a': 'set by node_3'}
```

### Use Pydantic models for graph state

A [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs.md#langgraph.graph.StateGraph) accepts a `state_schema` argument on initialization that specifies the "shape" of the state that the nodes in the graph can access and update.

In our examples, we typically use a python-native `TypedDict` or [`dataclass`](https://docs.python.org/3/library/dataclasses.html) for `state_schema`, but `state_schema` can be any [type](https://docs.python.org/3/library/stdtypes.html#type-objects).

Here, we'll see how a [Pydantic BaseModel](https://docs.pydantic.dev/latest/api/base_model/) can be used for `state_schema` to add run-time validation on **inputs**.

!!! note "Known Limitations" 

    - Currently, the output of the graph will **NOT** be an instance of a pydantic model. 
    - Run-time validation only occurs on inputs into nodes, not on the outputs. 
    - The validation error trace from pydantic does not show which node the error arises in. 
    - Pydantic's recursive validation can be slow. For performance-sensitive applications, you may want to consider using a `dataclass` instead.

```python
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from pydantic import BaseModel

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← node_3 does not see the private data.](./46-node_3-does-not-see-the-private-data.md)

**Next:** [The overall state of the graph (this is the public state shared across nodes) →](./48-the-overall-state-of-the-graph-this-is-the-public-.md)
