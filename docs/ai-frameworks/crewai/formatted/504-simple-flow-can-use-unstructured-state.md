---
title: "Crewai: Simple flow can use unstructured state"
description: "Simple flow can use unstructured state section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Simple flow can use unstructured state

class SimpleGreetingFlow(Flow):
    @start()
    def greet(self):
        self.state["name"] = "World"
        return f"Hello, {self.state['name']}!"

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Better: Focused state](./503-better-focused-state.md)

**Next:** [Complex flow benefits from structured state →](./505-complex-flow-benefits-from-structured-state.md)
