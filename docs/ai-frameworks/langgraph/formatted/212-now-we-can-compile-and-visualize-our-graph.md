---
title: "Langgraph: Now we can compile and visualize our graph"
description: "Now we can compile and visualize our graph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Now we can compile and visualize our graph

graph = workflow.compile()

from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass
```

<p>

</p>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← We now add a normal edge from `tools` to `agent`.](./211-we-now-add-a-normal-edge-from-tools-to-agent.md)

**Next:** [Use ReAct agent →](./213-use-react-agent.md)
