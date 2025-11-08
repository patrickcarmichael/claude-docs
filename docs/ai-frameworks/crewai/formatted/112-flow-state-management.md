---
title: "Crewai: Flow State Management"
description: "Flow State Management section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Flow State Management


Managing state effectively is crucial for building reliable and maintainable AI workflows. CrewAI Flows provides robust mechanisms for both unstructured and structured state management,
allowing developers to choose the approach that best fits their application's needs.

### Unstructured State Management

In unstructured state management, all state is stored in the `state` attribute of the `Flow` class.
This approach offers flexibility, enabling developers to add or modify state attributes on the fly without defining a strict schema.
Even with unstructured states, CrewAI Flows automatically generates and maintains a unique identifier (UUID) for each state instance.

```python Code theme={null}
from crewai.flow.flow import Flow, listen, start

class UnstructuredExampleFlow(Flow):

    @start()
    def first_method(self):
        # The state automatically includes an 'id' field
        print(f"State ID: {self.state['id']}")
        self.state['counter'] = 0
        self.state['message'] = "Hello from structured flow"

    @listen(first_method)
    def second_method(self):
        self.state['counter'] += 1
        self.state['message'] += " - updated"

    @listen(second_method)
    def third_method(self):
        self.state['counter'] += 1
        self.state['message'] += " - updated again"

        print(f"State after third_method: {self.state}")

flow = UnstructuredExampleFlow()
flow.plot("my_flow_plot")
flow.kickoff()
```

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1d64a80a490430f29b7fa1085a3062c4" alt="Flow Visual image" data-og-width="1974" width="1974" data-og-height="1058" height="1058" data-path="images/crewai-flow-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=192f7a8605d3a5c12b6b61aa4a23917f 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f41cbc9a268ba4bbb466fa2e2a1c2c1e 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4d2315a6e69d8125e7e144f04180529f 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=02eb5ffde3ef5936b2cf172160c72f72 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3fc5bb51802a4a5d641834e19d24e565 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=85414106ada4d15dcb7bccc086194b84 2500w" />

**Note:** The `id` field is automatically generated and preserved throughout the flow's execution. You don't need to manage or set it manually, and it will be maintained even when updating the state with new data.

**Key Points:**

* **Flexibility:** You can dynamically add attributes to `self.state` without predefined constraints.
* **Simplicity:** Ideal for straightforward workflows where state structure is minimal or varies significantly.

### Structured State Management

Structured state management leverages predefined schemas to ensure consistency and type safety across the workflow.
By using models like Pydantic's `BaseModel`, developers can define the exact shape of the state, enabling better validation and auto-completion in development environments.

Each state in CrewAI Flows automatically receives a unique identifier (UUID) to help track and manage state instances. This ID is automatically generated and managed by the Flow system.

```python Code theme={null}
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class ExampleState(BaseModel):
    # Note: 'id' field is automatically added to all states
    counter: int = 0
    message: str = ""

class StructuredExampleFlow(Flow[ExampleState]):

    @start()
    def first_method(self):
        # Access the auto-generated ID if needed
        print(f"State ID: {self.state.id}")
        self.state.message = "Hello from structured flow"

    @listen(first_method)
    def second_method(self):
        self.state.counter += 1
        self.state.message += " - updated"

    @listen(second_method)
    def third_method(self):
        self.state.counter += 1
        self.state.message += " - updated again"

        print(f"State after third_method: {self.state}")

flow = StructuredExampleFlow()
flow.kickoff()
```

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1d64a80a490430f29b7fa1085a3062c4" alt="Flow Visual image" data-og-width="1974" width="1974" data-og-height="1058" height="1058" data-path="images/crewai-flow-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=192f7a8605d3a5c12b6b61aa4a23917f 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f41cbc9a268ba4bbb466fa2e2a1c2c1e 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4d2315a6e69d8125e7e144f04180529f 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=02eb5ffde3ef5936b2cf172160c72f72 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3fc5bb51802a4a5d641834e19d24e565 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=85414106ada4d15dcb7bccc086194b84 2500w" />

**Key Points:**

* **Defined Schema:** `ExampleState` clearly outlines the state structure, enhancing code readability and maintainability.
* **Type Safety:** Leveraging Pydantic ensures that state attributes adhere to the specified types, reducing runtime errors.
* **Auto-Completion:** IDEs can provide better auto-completion and error checking based on the defined state model.

### Choosing Between Unstructured and Structured State Management

* **Use Unstructured State Management when:**

  * The workflow's state is simple or highly dynamic.
  * Flexibility is prioritized over strict state definitions.
  * Rapid prototyping is required without the overhead of defining schemas.

* **Use Structured State Management when:**
  * The workflow requires a well-defined and consistent state structure.
  * Type safety and validation are important for your application's reliability.
  * You want to leverage IDE features like auto-completion and type checking for better developer experience.

By providing both unstructured and structured state management options, CrewAI Flows empowers developers to build AI workflows that are both flexible and robust, catering to a wide range of application requirements.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Getting Started](./111-getting-started.md)

**Next:** [Flow Persistence →](./113-flow-persistence.md)
