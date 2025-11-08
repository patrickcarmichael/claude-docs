---
title: "Crewai: Debugging Flow State"
description: "Debugging Flow State section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Debugging Flow State


### Logging State Changes

When developing, add logging to track state changes:

```python  theme={null}
import logging
logging.basicConfig(level=logging.INFO)

class LoggingFlow(Flow):
    def log_state(self, step_name):
        logging.info(f"State after {step_name}: {self.state}")

    @start()
    def initialize(self):
        self.state["counter"] = 0
        self.log_state("initialize")
        return "Initialized"

    @listen(initialize)
    def increment(self, _):
        self.state["counter"] += 1
        self.log_state("increment")
        return f"Incremented to {self.state['counter']}"
```

### State Visualization

You can add methods to visualize your state for debugging:

```python  theme={null}
def visualize_state(self):
    """Create a simple visualization of the current state"""
    import json
    from rich.console import Console
    from rich.panel import Panel

    console = Console()

    if hasattr(self.state, "model_dump"):
        # Pydantic v2
        state_dict = self.state.model_dump()
    elif hasattr(self.state, "dict"):
        # Pydantic v1
        state_dict = self.state.dict()
    else:
        # Unstructured state
        state_dict = dict(self.state)

    # Remove id for cleaner output
    if "id" in state_dict:
        state_dict.pop("id")

    state_json = json.dumps(state_dict, indent=2, default=str)
    console.print(Panel(state_json, title="Current Flow State"))
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Consider creating new state:](./507-consider-creating-new-state.md)

**Next:** [Conclusion →](./509-conclusion.md)
