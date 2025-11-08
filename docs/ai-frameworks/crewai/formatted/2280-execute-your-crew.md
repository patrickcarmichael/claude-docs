---
title: "Crewai: Execute your crew"
description: "Execute your crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Execute your crew

result = crew.kickoff()
```

### Step 4: Enable Tracing in Your Flow

Similarly, you can enable tracing for CrewAI Flows:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class ExampleState(BaseModel):
    counter: int = 0
    message: str = ""

class ExampleFlow(Flow[ExampleState]):
    def __init__(self):
        super().__init__(tracing=True)  # Enable tracing for the flow

    @start()
    def first_method(self):
        print("Starting the flow")
        self.state.counter = 1
        self.state.message = "Flow started"
        return "continue"

    @listen("continue")
    def second_method(self):
        print("Continuing the flow")
        self.state.counter += 1
        self.state.message = "Flow continued"
        return "finish"

    @listen("finish")
    def final_method(self):
        print("Finishing the flow")
        self.state.counter += 1
        self.state.message = "Flow completed"

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Enable tracing in your crew](./2279-enable-tracing-in-your-crew.md)

**Next:** [Create and run the flow with tracing enabled →](./2281-create-and-run-the-flow-with-tracing-enabled.md)
