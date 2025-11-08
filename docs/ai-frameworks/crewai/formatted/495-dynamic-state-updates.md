---
title: "Crewai: Dynamic State Updates"
description: "Dynamic State Updates section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Dynamic State Updates


Regardless of whether you're using structured or unstructured state, you can update state dynamically throughout your flow's execution.

### Passing Data Between Steps

Flow methods can return values that are then passed as arguments to listening methods:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start

class DataPassingFlow(Flow):
    @start()
    def generate_data(self):
        # This return value will be passed to listening methods
        return "Generated data"

    @listen(generate_data)
    def process_data(self, data_from_previous_step):
        print(f"Received: {data_from_previous_step}")
        # You can modify the data and pass it along
        processed_data = f"{data_from_previous_step} - processed"
        # Also update state
        self.state["last_processed"] = processed_data
        return processed_data

    @listen(process_data)
    def finalize_data(self, processed_data):
        print(f"Received processed data: {processed_data}")
        # Access both the passed data and state
        last_processed = self.state.get("last_processed", "")
        return f"Final: {processed_data} (from state: {last_processed})"
```

This pattern allows you to combine direct data passing with state updates for maximum flexibility.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← The Automatic State ID](./494-the-automatic-state-id.md)

**Next:** [Persisting Flow State →](./496-persisting-flow-state.md)
